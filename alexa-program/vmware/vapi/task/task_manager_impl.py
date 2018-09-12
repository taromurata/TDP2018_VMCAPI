"""
Task Manager Interface Implementation
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

from datetime import datetime
import threading
import uuid
from com.vmware.vapi.std_provider import LocalizableMessage
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.data.value import (BooleanValue, ListValue,
                                    StringValue, StructValue)
from vmware.vapi.task.task_manager import TaskManager

URI_DELIMITER = ':'
TASK_EXPIRE_DURATION_SEC = 24 * 60 * 60


class TaskManagerImpl(TaskManager):
    """
    The TaskManager interface implementation providing methods to manage tasks
    """
    def __init__(self):
        self.task_map = {}
        self.tasks_to_remove = []
        self.lock = threading.RLock()
        TaskManager.__init__(self)

    def create_task(self, provider_id, description, service_id,
                    operation_id, cancelable, id_=None):
        """
        Creates a task in task manager.

        :type  provider_id: :class:`str`
        :param provider_id: Service UUID
        :type  description: :class:`com.vmware.vapi.std.LocalizableMessage`
        :param description: Task description.
        :type  service_id: :class:`str`
        :param service_id: Service Id.
        :type  operation_id: :class:`str`
        :param operation_id: Operation Id.
        :type  cancelable: :class:`bool`
        :param cancelable: Is the task cancelable.
        :type  id_: :class:`str`
        :param id_: Base task id
        """
        task_info = StructValue()
        if description is not None:
            task_info.set_field(
                'description', TypeConverter.convert_to_vapi(
                                    description,
                                    LocalizableMessage.get_binding_type()))
        else:
            desc_value = StructValue()
            desc_value.set_field('id', StringValue())
            desc_value.set_field('default_message', StringValue())
            desc_value.set_field('args', ListValue())
            task_info.set_field('description', desc_value)

        task_info.set_field('service', StringValue(service_id))
        task_info.set_field('operation', StringValue(operation_id))
        task_info.set_field('cancelable',
                            BooleanValue(True if cancelable else False))
        task_info.set_field('status', StringValue('PENDING'))
        base_id = id_ if id_ is not None else str(uuid.uuid4())
        task_id = self._create_task_id(base_id, provider_id)

        with self.lock:
            self.task_map.setdefault(task_id, task_info)

        self._remove_expired_task()
        return task_id

    def get_info(self, task_id):
        """
        Get task info.

        :type  task_id: :class:`str`
        :param task_id: Task Id.

        :rtype:  :class:`vmware.vapi.data.value.StructValue`
        :return: Task Info
        """
        return self.task_map[task_id]

    def set_info(self, task_id, info):
        """
        Set task info.

        :type  task_id: :class:`str`
        :param task_id: Task Id.
        :type  status: :class:`vmware.vapi.data.value.StructValue`
        :param status: Task Info.
        """
        self.task_map[task_id] = info
        if info.get_field('status') in [StringValue('SUCCEEDED'),
                                        StringValue('FAILED')]:
            with self.lock:
                self.tasks_to_remove.append((task_id, datetime.utcnow()))

    def _create_task_id(self, base_id, provider_id):
        """
        Create task id.

        :type  base_id: :class:`str`
        :param base_id: Task Id.
        :type  provider_id: :class:`str`
        :param provider_id: Service UUID
        """
        return '%s%s%s' % (base_id, URI_DELIMITER, provider_id)

    def remove_task(self, task_id):
        """
        Remove task from tasks map
        """
        with self.lock:
            self.task_map.pop(task_id)

    def _remove_expired_task(self):
        """
        Remove expired tasks from the task map
        """
        with self.lock:
            curr_time = datetime.utcnow()
            tasks_list = self.tasks_to_remove
            for task_id, t in tasks_list:
                time_elapsed = curr_time - t
                if (time_elapsed.total_seconds() < TASK_EXPIRE_DURATION_SEC):
                    break
                self.tasks_to_remove.remove((task_id, t))
                self.task_map.pop(task_id)


# Task manager instance
_task_manager = None


def get_task_manager(task_manager=None):
    """
    Returns the singleton task manager instance

    :type:  :class:`str`
    :param: Task manager class
    """
    global _task_manager
    if _task_manager is None:
        if task_manager is None:
            _task_manager = TaskManagerImpl()
        else:
            constructor = dynamic_import(task_manager)
            _task_manager = constructor()

    return _task_manager
