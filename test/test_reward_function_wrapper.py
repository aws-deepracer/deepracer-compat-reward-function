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
from deepracer_compat_reward_function.reward_function_wrapper import RewardFunctionWrapper
from unittest.mock import MagicMock, patch


@patch("deepracer_compat_reward_function.reward_function_wrapper.AgentConverter")
@patch("deepracer_compat_reward_function.reward_function_wrapper.ObjectConverter")
@patch("deepracer_compat_reward_function.reward_function_wrapper.TrackConverter")
class RewardFunctionWrapperTest(TestCase):
    def setUp(self) -> None:
        self.agent_name = "agent0"
        self.fun_callable = MagicMock()
        self.deepracer_env_state = MagicMock()

    def test_init(self, track_converter_mock, object_converter_mock, agent_converter_mock) -> None:
        track_converter_mock.return_value = "track"
        object_converter_mock.return_value = "object"
        agent_converter_mock.return_value = "agent"
        reward_function = RewardFunctionWrapper(self.agent_name, self.fun_callable, self.deepracer_env_state)
        self.assertEqual(reward_function._agent_name, self.agent_name)
        self.assertEqual(reward_function._reward_function, self.fun_callable)
        self.assertEqual(reward_function._deepracer_env_state, self.deepracer_env_state)
        self.assertEqual(reward_function._converters, {"track", "object", "agent"})

    def test_get_reward(self, track_converter_mock, object_converter_mock, agent_converter_mock) -> None:
        self.fun_callable.return_value = 10.0
        reward_function = RewardFunctionWrapper(self.agent_name, self.fun_callable, self.deepracer_env_state)
        reward_function._converters = {track_converter_mock, agent_converter_mock, object_converter_mock}
        track_converter_mock.convert.return_value = {"track": "track_test"}
        agent_converter_mock.convert.return_value = {"agent": "agent_test"}
        object_converter_mock.convert.return_value = {"object": "object_test"}
        reward = reward_function.get_reward()
        self.fun_callable.assert_called_once_with({
            "track": "track_test",
            "agent": "agent_test",
            "object": "object_test"})
        self.assertEqual(reward, {self.agent_name: 10.0})
