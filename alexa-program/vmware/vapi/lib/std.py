
"""
Helper functions for manipulating vAPI runtime objects corresponding to
the standard types (e.g. LocalizableMessage) and errors
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

from vmware.vapi.data.definition import (
    DynamicStructDefinition, ErrorDefinition, ListDefinition,
    OptionalDefinition, StringDefinition, StructDefinition)
from vmware.vapi.l10n.runtime import message_factory


_ID_FIELD_NAME = 'id'
_DEFAULT_MESSAGE_FIELD_NAME = 'default_message'
_ARGS_FIELD_NAME = 'args'
localizable_message_def = StructDefinition(
    'com.vmware.vapi.std.localizable_message',
    ((_ID_FIELD_NAME, StringDefinition()),
     (_DEFAULT_MESSAGE_FIELD_NAME, StringDefinition()),
     (_ARGS_FIELD_NAME, ListDefinition(StringDefinition()))))


_MESSAGES_FIELD_NAME = 'messages'
messages_list_def = ListDefinition(localizable_message_def)
_DATA_FIELD_NAME = 'data'
data_optional_dynamicstructure_def = OptionalDefinition(
    DynamicStructDefinition())
_ERROR_DEF_FIELDS = [(_MESSAGES_FIELD_NAME, messages_list_def),
                     (_DATA_FIELD_NAME, data_optional_dynamicstructure_def)]


def make_std_error_def(name):
    """
    Internal function to create a "standard" ErrorDefinition for use only by
    the vAPI runtime.
    :type  name: :class:`str`
    :param args: Fully qualified name of the standard error type
    :rtype: :class:`vmware.vapi.data.definition.ErrorDefinition`
    :return: ErrorDefinition containing a single message field
    """
    return ErrorDefinition(name, _ERROR_DEF_FIELDS)


def _make_struct_value_from_message(message):
    """
    Helper function to create a StructValue matching the LocalizableMessage
    type defined in VMODL from a Message object.
    """
    id_def = localizable_message_def.get_field(_ID_FIELD_NAME)
    default_message_def = localizable_message_def.get_field(
        _DEFAULT_MESSAGE_FIELD_NAME)
    args_def = localizable_message_def.get_field(_ARGS_FIELD_NAME)
    result = localizable_message_def.new_value()
    result.set_field(_ID_FIELD_NAME, id_def.new_value(message.id))
    result.set_field(_DEFAULT_MESSAGE_FIELD_NAME,
                     default_message_def.new_value(message.def_msg))
    args_list_value = args_def.new_value()
    arg_def = args_def.element_type
    for arg in message.args:
        args_list_value.add(arg_def.new_value(arg))
    result.set_field(_ARGS_FIELD_NAME, args_list_value)
    return result


def make_error_value_from_msg_id(error_def, msg_id, *args):
    """
    Create an error result for a "standard" error

    :type  error_def: :class:`vmware.vapi.data.type.ErrorDefinition`
    :param error_def: ErrorDefintion for the error
    :type  msg_id: :class:`str`
    :param msg_id: Message identifier
    :type  args: :class:`list` of :class:`str`
    :param args: Argument list for constructing a Message
    :rtype: :class:`vmware.vapi.data.value.ErrorValue`
    :return: ErrorValue containing a single message
    """
    msg = message_factory.get_message(msg_id, *args)
    messages = error_def.get_field(_MESSAGES_FIELD_NAME).new_value()
    messages.add(_make_struct_value_from_message(msg))
    data = data_optional_dynamicstructure_def.new_value()
    error_value = error_def.new_value()
    error_value.set_field(_MESSAGES_FIELD_NAME, messages)
    error_value.set_field(_DATA_FIELD_NAME, data)
    return error_value


def make_error_value_from_msgs(error_def, *msg_list):
    """
    Create an error result for a "standard" error

    :type  error_def: :class:`vmware.vapi.data.type.ErrorDefinition`
    :param error_def: ErrorDefintion for the error
    :type  msg_list: :class:`list` of :class:`vmware.vapi.message.Message`
    :param msg_list: list of localizable messages
    :rtype: :class:`vmware.vapi.data.value.ErrorValue`
    :return: ErrorValue containing a single message
    """
    messages = error_def.get_field(_MESSAGES_FIELD_NAME).new_value()
    for msg in msg_list:
        messages.add(_make_struct_value_from_message(msg))
    data = data_optional_dynamicstructure_def.new_value()
    error_value = error_def.new_value()
    error_value.set_field(_MESSAGES_FIELD_NAME, messages)
    error_value.set_field(_DATA_FIELD_NAME, data)
    return error_value


def make_error_value_from_error_value_and_msgs(error_def,
                                               cause,
                                               *msg_list):
    """
    Create an error result for a "standard" error from a cause ErrorValue
    and an list of messages.

    The list of message will be prepended to the messages from the cause
    (if any).

    :type  error_def: :class:`vmware.vapi.data.type.ErrorDefinition`
    :param error_def: ErrorDefintion for the error
    :type  cause: :class:`vmware.vapi.data.value.ErrorValue`
    :param cause: Lower level ErrorValue that "caused" the error
    :type  msg_list: :class:`list` of :class:`vmware.vapi.message.Message`
    :param msg_list: list of localizable messages
    :rtype: :class:`vmware.vapi.data.value.ErrorValue`
    :return: ErrorValue containing a single message
    """
    messages = error_def.get_field(_MESSAGES_FIELD_NAME).new_value()
    for msg in msg_list:
        messages.add(_make_struct_value_from_message(msg))
    try:
        cause_msg_list = cause.get_field(_MESSAGES_FIELD_NAME)
        for msg in cause_msg_list:
            messages.add(msg)
    except Exception:
        # If cause doesn't have a message field or it isn't a ListValue,
        # just ignore it.
        pass
    data = data_optional_dynamicstructure_def.new_value()
    error_value = error_def.new_value()
    error_value.set_field(_MESSAGES_FIELD_NAME, messages)
    error_value.set_field(_DATA_FIELD_NAME, data)
    return error_value
