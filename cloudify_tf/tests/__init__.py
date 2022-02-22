########
# Copyright (c) 2018-2020 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from uuid import uuid1
from mock import MagicMock

from cloudify.mocks import MockCloudifyContext


class MockCloudifyContextAbortOperation(MockCloudifyContext):

    abort_operation = MagicMock()

    @staticmethod
    def returns(value):
        return value


class TestBase(unittest.TestCase):
    def setUp(self):
        super(TestBase, self).setUp()

    def mock_ctx(self, test_name, test_properties,
                 test_runtime_properties=None):
        test_node_id = uuid1()
        ctx = MockCloudifyContextAbortOperation(
            node_id=test_node_id,
            properties=test_properties,
            runtime_properties=None if not test_runtime_properties
            else test_runtime_properties,
            deployment_id=test_name
        )
        return ctx
