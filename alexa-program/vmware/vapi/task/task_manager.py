"""
Task Manager Interface
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import abc
import six


@six.add_metaclass(abc.ABCMeta)
class TaskManager(object):
    """
    The TaskManager interface providing methods to manage tasks
    """

    @abc.abstractmethod
    def create_task(self, provider_id, description, service_id,
                    operation_id, cancelable, id_):
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
        pass

    @abc.abstractmethod
    def get_info(self, task_id):
        """
        Get task info.

        :type  task_id: :class:`str`
        :param task_id: Task Id.

        :rtype:  :class:`vmware.vapi.data.value.StructValue`
        :return: Task Info
        """
        pass

    @abc.abstractmethod
    def set_info(self, task_id, info):
        """
        Set task info.

        :type  task_id: :class:`str`
        :param task_id: Task Id.
        :type  status: :class:`vmware.vapi.data.value.StructValue`
        :param status: Task Info.
        """
        pass

    @abc.abstractmethod
    def remove_task(self, task_id):
        """
        Remove task from tasks map.

        :type  task_id: :class:`str`
        :param task_id: Task Id.
        """
        pass
