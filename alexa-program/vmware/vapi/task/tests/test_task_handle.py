#!/usr/bin/env python

"""
Unit tests for the task handle
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2017-2018 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

from datetime import datetime
import decimal
import unittest
import uuid

from com.vmware.cis.task_provider import Info, Progress
from com.vmware.vapi.std_provider import LocalizableMessage
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.type import AnyErrorType, StringType
from vmware.vapi.common.context import TLS
from vmware.vapi.core import ExecutionContext, SecurityContext
from vmware.vapi.lib.context import create_default_application_context
from vmware.vapi.lib.constants import TASK_ID
from vmware.vapi.data.value import (BooleanValue, IntegerValue, ListValue,
    OptionalValue, StringValue, StructValue)
from vmware.vapi.stdlib.provider.factories import MessageFactory
from vmware.vapi.task.task_manager_impl import get_task_manager
from vmware.vapi.task.task_handle import get_task_handle


class TestTaskHandle(unittest.TestCase):
    task_manager = None
    task_id = None
    task_handle = None
    description = None
    msgs = {
        'msg1': 'task1',
        'prog1': 'progress'
    }
    progress_msg = None

    @classmethod
    def setUpClass(cls):
        cls.task_manager = get_task_manager()
        msg_factory = MessageFactory(cls.msgs)
        cls.description = LocalizableMessage(id='msg1',
                                             default_message='task1',
                                             args=[])
        cls.progress_msg = LocalizableMessage(id='prog1',
                                              default_message='progress',
                                              args=[])
        cls.task_id = cls.task_manager.create_task(str(uuid.uuid4()),
                                                   cls.description,
                                                   'test.service',
                                                   'op1',
                                                   True)
        app_ctx = create_default_application_context()
        app_ctx[TASK_ID] = cls.task_id
        sec_ctx = SecurityContext()
        TLS.ctx = ExecutionContext(app_ctx, sec_ctx)
        cls.task_handle = get_task_handle(Info, StringType())

    def test_get_info(self):
        info = self.task_handle.get_info()
        self.assertEqual(info.description, self.description)
        self.assertEqual(info.service, 'test.service')
        self.assertEqual(info.operation, 'op1')
        self.assertEqual(info.cancelable, True)

    def test_get_published_info(self):
        published_info = self.task_handle.get_published_info()
        self.assertEqual(published_info.description, self.description)
        self.assertEqual(published_info.service, 'test.service')
        self.assertEqual(published_info.operation, 'op1')
        self.assertEqual(published_info.cancelable, True)

        info = self.task_handle.get_info()
        info.cancelable = False
        info.operation = 'op2'
        self.task_handle.publish()

        published_info = self.task_handle.get_published_info()
        self.assertEqual(published_info.operation, 'op1')
        self.assertEqual(published_info.cancelable, False)

    def test_publish(self):
        info = self.task_handle.get_info()
        progress = Progress()
        progress.total = 100
        progress.completed = 42
        progress.message = self.progress_msg
        desc2 = LocalizableMessage(id='msg2',
                                   default_message='task1',
                                   args=[])
        info.description = desc2
        info.cancelable = False
        info.status = 'RUNNING'
        info.start_time = datetime.utcnow()
        info.progress = progress
        self.task_handle.publish()
        result = self.task_manager.get_info(self.task_id)
        self.assertEqual(result.get_field('status'), StringValue('RUNNING'))
        progress_val = StructValue('com.vmware.cis.task.progress')
        progress_val.set_field('total', IntegerValue(100))
        progress_val.set_field('completed', IntegerValue(42))
        progress_val.set_field('message', TypeConverter.convert_to_vapi(self.progress_msg,
                                    LocalizableMessage.get_binding_type()))
        self.assertEqual(result.get_field('progress'), OptionalValue(progress_val))
        self.assertEqual(result.get_field('cancelable'), BooleanValue(False))


if __name__ == "__main__":
    unittest.main()
