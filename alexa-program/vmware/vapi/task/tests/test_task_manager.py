#!/usr/bin/env python

"""
Unit tests for the task publisher
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest
import uuid
from datetime import datetime
import decimal

from com.vmware.cis.task_provider import Info, Progress, Status
from com.vmware.vapi.std_provider import LocalizableMessage
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.data.value import BooleanValue, OptionalValue, StringValue
from vmware.vapi.stdlib.provider.factories import MessageFactory
from vmware.vapi.task.task_manager_impl import get_task_manager


class TestTaskManager(unittest.TestCase):
    task_manager = None
    task_id = None
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

    def test_create_task(self):
        service_uuid = str(uuid.uuid4())
        task_id = self.task_manager.create_task(service_uuid,
                                                self.description,
                                                'test.service1',
                                                'op',
                                                False)
        info = self.task_manager.get_info(task_id)
        self.assertIn(service_uuid, task_id)
        self.assertEqual(info.get_field('description'),
                         TypeConverter.convert_to_vapi(self.description,
                            LocalizableMessage.get_binding_type()))
        self.assertEqual(info.get_field('service'), StringValue('test.service1'))
        self.assertEqual(info.get_field('operation'), StringValue('op'))
        self.assertEqual(info.get_field('cancelable'), BooleanValue(False))
        self.assertEqual(info.get_field('status'), StringValue('PENDING'))

    def test_create_task_no_desc(self):
        service_uuid = str(uuid.uuid4())
        task_id = self.task_manager.create_task(service_uuid,
                                                None,
                                                'test.service1',
                                                'op',
                                                False)
        info = self.task_manager.get_info(task_id)
        self.assertIn(service_uuid, task_id)
        self.assertEqual(info.get_field('service'), StringValue('test.service1'))
        self.assertEqual(info.get_field('operation'), StringValue('op'))
        self.assertEqual(info.get_field('cancelable'), BooleanValue(False))
        self.assertEqual(info.get_field('status'), StringValue('PENDING'))

    def test_create_task_with_id(self):
        service_uuid = str(uuid.uuid4())
        base_id = str(uuid.uuid4())
        task_id = self.task_manager.create_task(service_uuid,
                                                None,
                                                'test.service1',
                                                'op',
                                                False,
                                                base_id)
        info = self.task_manager.get_info(task_id)
        self.assertIn(service_uuid, task_id)
        self.assertIn(base_id, task_id)
        self.assertEqual(info.get_field('service'), StringValue('test.service1'))
        self.assertEqual(info.get_field('operation'), StringValue('op'))
        self.assertEqual(info.get_field('cancelable'), BooleanValue(False))
        self.assertEqual(info.get_field('status'), StringValue('PENDING'))

    def test_set_info(self):
        service_uuid = str(uuid.uuid4())
        task_id = self.task_manager.create_task(service_uuid,
                                                None,
                                                'test.service',
                                                'op',
                                                False)
        info_val = self.task_manager.get_info(task_id)
        info = TypeConverter.convert_to_python(info_val,
                                               Info.get_binding_type())
        info.description = self.description
        progress = Progress()
        progress.total = 100
        progress.completed = 10
        progress.message = self.progress_msg
        info.progress = progress
        info.start_time = datetime.utcnow()
        info.status = Status.RUNNING
        info.cancelable = True
        self.task_manager.set_info(task_id,
                                   TypeConverter.convert_to_vapi(info, Info.get_binding_type()))
        result = self.task_manager.get_info(task_id)
        self.assertEqual(result.get_field('progress'),
                         OptionalValue(TypeConverter.convert_to_vapi(progress,
                            Progress.get_binding_type())))
        self.assertEqual(result.get_field('cancelable'), BooleanValue(info.cancelable))
        self.assertEqual(result.get_field('status'), StringValue('RUNNING'))


if __name__ == "__main__":
    unittest.main()
