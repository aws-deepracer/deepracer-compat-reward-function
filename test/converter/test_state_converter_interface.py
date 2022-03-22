#################################################################################
#   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.          #
#                                                                               #
#   Licensed under the Apache License, Version 2.0 (the "License").             #
#   You may not use this file except in compliance with the License.            #
#   You may obtain a copy of the License at                                     #
#                                                                               #
#       http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                               #
#   Unless required by applicable law or agreed to in writing, software         #
#   distributed under the License is distributed on an "AS IS" BASIS,           #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
#   See the License for the specific language governing permissions and         #
#   limitations under the License.                                              #
#################################################################################
from unittest import TestCase
from unittest.mock import MagicMock
from deepracer_compat_reward_function.converter.state_converter_interface import StateConverterInterface


class DummyConverter(StateConverterInterface):
    def __init__(self, deepracer_env_state):
        self._deepracer_env_state = deepracer_env_state

    def convert(self):
        return {"dummy_key": "dummy_value"}


class DummyConverterTest(TestCase):
    def setUp(self) -> None:
        self.deepracer_env_state = MagicMock()
        self.dummy_converter = DummyConverter(self.deepracer_env_state)

    def test_init(self) -> None:
        self.assertEqual(self.deepracer_env_state, self.dummy_converter._deepracer_env_state)

    def test_convert(self) -> None:
        self.assertEqual(self.dummy_converter.convert(), {"dummy_key": "dummy_value"})
