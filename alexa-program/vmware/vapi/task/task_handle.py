"""
Task Handle interface for publishing task info
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2017-2018 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

from com.vmware.vapi.std_provider import LocalizableMessage
from vmware.vapi.bindings.type import BooleanType, StringType
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.common.context import get_event, clear_event
from vmware.vapi.data.definition import OpaqueDefinition
from vmware.vapi.exception import CoreException
from vmware.vapi.l10n.runtime import message_factory
from vmware.vapi.lib.context import get_task_id
from vmware.vapi.lib.log import get_vapi_logger
from vmware.vapi.task.task_manager_impl import get_task_manager

logger = get_vapi_logger(__name__)


class TaskHandle(object):
    """
    The TaskHandle interface for publishing task info.
    This class is not thread safe. Info returned from the get is mutable.
    Task method will not return task ID to client until provider calls publish
    method with accept=True once.
    Provider must call publish to save the updates to task state into
    TaskManager.
    """
    def __init__(self, info_type, result_type):
        self.task_manager = get_task_manager()
        self.info_type = info_type
        self.result_type = result_type
        self.task_id = get_task_id()
        self.info = info_type()
        self._initialize_common_info()

    def _initialize_common_info(self):
        """
        Initialize common task info fields
        """
        published_info = self.task_manager.get_info(self.task_id)
        self._override_api_info(published_info)
        self.info.cancelable = TypeConverter.convert_to_python(
                                    published_info.get_field('cancelable'),
                                    BooleanType())
        desc = published_info.get_field('description')
        if desc is not None:
            self.info.description = TypeConverter.convert_to_python(
                                        desc,
                                        LocalizableMessage.get_binding_type())
        self.info.status = TypeConverter.convert_to_python(
                                published_info.get_field('status'),
                                StringType())

    def _override_api_info(self, published_info):
        """
        Override service and operation task info fields
        """
        self.info.service = TypeConverter.convert_to_python(
                                published_info.get_field('service'),
                                StringType())
        self.info.operation = TypeConverter.convert_to_python(
                                published_info.get_field('operation'),
                                StringType())

    def get_info(self):
        """
        Returns the Task Info.
        """
        return self.info

    def get_published_info(self):
        """
        Returns the current published task Info
        """
        info = self.task_manager.get_info(self.task_id)
        converted_info = TypeConverter.convert_to_python(
                            info,
                            self.info_type.get_binding_type())
        return converted_info

    def publish(self, accept=False):
        """
        Publish the temporary task info into task manager

        :type  accept: :class:`bool`
        :param accept: Accept task and return task id to client
        """
        published_info = self.task_manager.get_info(self.task_id)

        # Override the common info fields which can't be modified by providers
        self._override_api_info(published_info)

        if self.info.result is not None:
            # Check if result type is Opaque or actual type
            res_type = self.info_type.get_binding_type().get_field('result')
            if isinstance(res_type.element_type.definition, OpaqueDefinition):
                result = None
                try:
                    result = TypeConverter.convert_to_vapi(
                                self.info.result,
                                self.result_type.get_binding_type())
                except AttributeError:
                    result = TypeConverter.convert_to_vapi(self.info.result,
                                                           self.result_type)
                self.info.result = result

        info = TypeConverter.convert_to_vapi(
                    self.info,
                    self.info_type.get_binding_type())
        self.task_manager.set_info(self.task_id, info)

        if accept:
            event = get_event()
            event.set()
            clear_event()
            # Validate that description is set while accepting the task
            if (self.info.description is None or
                    (not self.info.description.id and
                     not self.info.description.default_message)):
                msg = message_factory.get_message(
                        'vapi.data.structure.field.missing',
                        self.info_type, 'description')
                logger.debug(msg)
                raise CoreException(msg)


def get_task_handle(info_type, result_type):
    """
    Creates and returns the TaskHandle instance

    :type  info_type: :class:`com.vmware.cis.task_provider.Info`
    :param info_type: Task Info class.
    :type  result_type: :class:`com.vmware.cis.task_provider.Result`
    :param result_type: Result type.
    """
    return TaskHandle(info_type, result_type)
