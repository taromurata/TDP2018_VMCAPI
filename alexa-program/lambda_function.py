"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

import boto3

import yaml
import re
import requests
import urllib3
from com.vmware.vapi.std.errors_client import InvalidRequest
from com.vmware.vmc.model_client import AwsSddcConfig, ErrorResponse, AccountLinkSddcConfig, SddcConfig
from tabulate import tabulate
from vmware.vapi.vmc.client import create_vmc_client
from tdp_vmcapi.vmc_util import *


# --------------- Global Variables ---------------------------------------------
BUCKET_NAME = 'tdp2018-vmcapi'
INFOFILE_NAME = 'info.yaml'

vmc_util = None

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


def vmc_login(info):
    global vmc_util

    vmc_util = VMCUtil()
    vmc_util.set_info(info)

    print(vmc_util.refresh_token)
    print(vmc_util.org_id)

    vmc_util.login()
    print("vmc_login: Logged in successfully")
    # vmc_util.list_sddc()


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome!"
    speech_output = "TDP 2018 VMC API スキルにようこそ。\n" \
                    "VMC にログインしました。"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "なにかおっしゃってください。"

    secure_refresh_token = re.sub("[0-9|a-z|A-Z]", "*", vmc_util.refresh_token, 26)
    secure_org_id = re.sub("[0-9|a-z|A-Z]", "*", vmc_util.org_id, 26)
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
    vmc_login(info_file())

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()

def delete_sddc_intent():
    # TODO: Code.
    return get_welcome_response()

def add_sddc_intent():
    # TODO: Code.
    return get_welcome_response()

def list_sddcs_intent():
    global vmc_util
    
    sddcs = vmc_util.list_sddc()
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

    return build_response({}, build_speechlet_response(card_title,
        speech_output, card_output, reprompt_text, should_end_session))

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "ListSddcsIntent":
        return list_sddcs_intent()
    elif intent_name == "AddSddcIntent":
        return add_sddc_intent()
    elif intent_name == "DeleteSddcIntent":
        return delete_sddc_intent()
    elif intent_name == "EndSessionIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here
    # TODO: return Good bye message 



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
