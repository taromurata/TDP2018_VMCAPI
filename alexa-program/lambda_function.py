"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

import boto3

import json
import yaml
import re
import requests
import urllib3
from com.vmware.vapi.std.errors_client import InvalidRequest
from com.vmware.vmc.model_client import AwsSddcConfig, ErrorResponse, AccountLinkSddcConfig, SddcConfig
from tabulate import tabulate
from vmware.vapi.vmc.client import create_vmc_client
from tdp_vmcapi.vmc_util import *
from tdp_state import TdpState
from state_manager import StateManager


# --------------- Global Variables ---------------------------------------------
BUCKET_NAME = 'tdp2018-vmcapi'
INFOFILE_NAME = 'info.yaml'

TEST_SDDC_CONFIG_FILE = 'sddc_config.json'

# State Manager per sessionId
g_id_state_manager = {}

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, speech_output, card_output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': speech_output
        },
        'card': {
            'type': 'Simple',
            'title': 'TDP2018 VMC API - ' + title,
            'content': card_output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def info_file():
    s3 = boto3.client('s3')
    bucket_name = BUCKET_NAME
    file_name = INFOFILE_NAME

    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    info = yaml.load(response['Body'].read())

    return info


def vmc_login(sessionId, info):
    global g_id_state_manager

    g_id_state_manager[sessionId] = StateManager()

    g_id_state_manager[sessionId].vmc_util = VMCUtil()
    g_id_state_manager[sessionId].vmc_util.set_info(info)
    g_id_state_manager[sessionId].vmc_util.login()

    print("vmc_login: Logged in successfully")

def get_welcome_response(sessionId):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    global g_id_state_manager

    session_attributes = {TdpState.KEY: TdpState.STATE_NORMAL}
    card_title = "Welcome!"
    speech_output = "TDP 2018 VMC API スキルにようこそ。\n" \
                    "VMC にログインしました。"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "なにかおっしゃってください。"

    secure_refresh_token = re.sub("[0-9|a-z|A-Z]", "*",
        g_id_state_manager[sessionId].vmc_util.refresh_token, 26)
    secure_org_id = re.sub("[0-9|a-z|A-Z]", "*",
        g_id_state_manager[sessionId].vmc_util.org_id, 26)
    card_output = "Successfully logged in to VMC:\n" \
                  f"  refresh_token: {secure_refresh_token}\n" \
                  f"  org_id: {secure_org_id}"

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, card_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Bye!"
    speech_output = "TDP 2018 VMC API をご利用いただきありがとうございました。\n" \
                    "良いいちにちを。"
    card_output = "TDP 2018 VMC API をご利用いただきありがとうございました。\n" \
                  "良い一日を！"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, card_output, None, should_end_session))


def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}

# --------------- Events ------------------
def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    sid = session['sessionId']
    vmc_login(sid, info_file())

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response(sid)

def sddc_config():
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=BUCKET_NAME, Key=TEST_SDDC_CONFIG_FILE)
    return json.loads(response['Body'].read().decode('utf-8'))

def delete_latest_sddc_intent(sid):
    global g_id_state_manager

    sddc_name = g_id_state_manager[sid].sddc_config['name']

    sddcs = g_id_state_manager[sid].vmc_util.list_sddc()
    sddc_ready = True
    sddc_id = None
    for sddc in sddcs:
        if sddc.name == sddc_name:
            sddc_id = sddc.id
            if sddc.sddc_state != 'READY':
                sddc_ready = False
                break

    speech_output = ""

    if sddc_ready:
        # g_id_state_manager[sid].vmc_util.delete_latest_sddc()
        g_id_state_manager[sid].vmc_util.delete_sddc_id(sddc_id)
        speech_output = f"SDDC {sddc_name} の削除が正常に終了しました。"
    else:
        speech_output = f"SDDC {sddc_name} は READY ではありません。削除できませんでした。"
        
    card_title = "SDDC Delete:"
    card_output = speech_output
    reprompt_text = ""
    should_end_session = False
    session_attributes = {TdpState.KEY: TdpState.STATE_NORMAL}

    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))

def delete_sddc_intent():
    global g_id_state_manager
    sid = "dummy"

    return get_welcome_response(sid)

def add_sddc_intent(sid):
    global g_id_state_manager

    if g_id_state_manager[sid].sddc_config is None:
        g_id_state_manager[sid].sddc_config = sddc_config()

    sddc_id = g_id_state_manager[sid].vmc_util.create_sddc(
        g_id_state_manager[sid].sddc_config)

    card_title = "Create SDDC"
    speech_output = "SDDCの作成が正常に終了しました。"
    reprompt_text = ""
    card_output = f"Creating SDDC: sddc_id is {sddc_id}"
    should_end_session = False
    # TODO: Use name from user input by using STATE_ADD_NAME
    session_attributes = {TdpState.KEY: TdpState.STATE_NORMAL}

    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))

def list_sddcs_intent(sid):
    global g_id_state_manager
    
    sddcs = g_id_state_manager[sid].vmc_util.list_sddc()
    print(sddcs)

    sddc_names = [sddc.name for sddc in sddcs]
    sddc_names_str = '、'.join(sddc_names)

    table = []
    for sddc in sddcs:
        table.append([sddc.id, sddc.name, sddc.resource_config.region])
    card_output = tabulate(table, ['ID', 'Name', 'AWS Region'])

    card_title = "List SDDC"
    speech_output = "VMC上のSDDCは、" + sddc_names_str + "です。"

    reprompt_text = ""
    should_end_session = False
    session_attributes = {TdpState.KEY: TdpState.STATE_NORMAL}

    return build_response(session_attributes, build_speechlet_response(card_title,
        speech_output, card_output, reprompt_text, should_end_session))

def sddc_stats_intent(sid):
    global g_id_state_manager

    sddcs = g_id_state_manager[sid].vmc_util.list_sddc()

    speech_output = ""
    table = []
    for sddc in sddcs:
        speech_output += f"{sddc.name} は {sddc.sddc_state}、"
        table.append([sddc.id, sddc.name, sddc.sddc_state])

    speech_output += "です。"
    card_output = tabulate(table, ['ID', 'Name', 'State'])
    card_title = 'SDDC Stats'
    reprompt_text = ""
    should_end_session = False
    session_attributes = {TdpState.KEY: TdpState.STATE_NORMAL}

    return build_response(session_attributes, build_speechlet_response(card_title,
        speech_output, card_output, reprompt_text, should_end_session))

def not_implemented_message():
    card_title = "わかりません、、、"
    card_output = "そのうち実装されるでしょう、、、"
    speech_output = "まだ、わかりません。"
    reprompt_text = ""
    should_end_session = False

    return build_response({}, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """
    sid = session['sessionId']

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    attributes = session['attributes']

    print(f'attributes = {attributes}')

    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.HelpIntent":
        return get_welcome_response(sid)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "ListSddcsIntent":
        return list_sddcs_intent(sid)
    elif intent_name == "AddSddcIntent":
        return add_sddc_intent(sid)
    elif intent_name == "AddSddcWithNameIntent":
        return not_implemented_message()
    elif intent_name == "DeleteSddcIntent":
        # return delete_sddc_intent()
        return delete_latest_sddc_intent(sid)
        # return not_implemented_message()
    elif intent_name == "SddcStatsIntent":
        return sddc_stats_intent(sid)
    elif intent_name == "EndSessionIntent":
        return handle_session_end_request()
    else:
        return not_implemented_message()


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here
    # TODO: return Good bye message 

# --------------- Test handler ------------------
def _lambda_handler(event, context):
    sddc_conf = sddc_config()
    return handle_session_end_request()

# --------------- Main handler ------------------
def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """

    print(f"[INFO] event = {event}")
    # print(f"[INFO] context = {str(context)}")

    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
