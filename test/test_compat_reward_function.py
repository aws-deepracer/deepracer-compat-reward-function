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
from deepracer_compat_reward_function.compat_reward_function import CompatRewardFunction
from unittest.mock import MagicMock, patch, call


class CompatRewardFunctionTest(TestCase):
    def setUp(self) -> None:
        self.function0 = MagicMock()
        self.function1 = MagicMock()
        self.reward_function_dict = {
            "agent0": self.function0,
            "agent1": self.function1}
        self.deepracer_env = MagicMock()

    @patch("deepracer_compat_reward_function.compat_reward_function.RewardFunctionWrapper")
    @patch("deepracer_compat_reward_function.compat_reward_function.DeepRacerEnvState")
    def test_init(self, deepracer_env_state_mock, reward_function_mock) -> None:
        compat_reward_function = CompatRewardFunction(
            self.reward_function_dict,
            self.deepracer_env)
        [reward_function_mock.assert_has_calls(
            [call(name, function, compat_reward_function._deepracer_env_state)])
            for name, function in self.reward_function_dict.items()]
        deepracer_env_state_mock.assert_called_once_with(self.deepracer_env)

    def test_get_reward(self) -> None:
        compat_reward_function = CompatRewardFunction(
            self.reward_function_dict,
            self.deepracer_env)
        func1 = MagicMock()
        func2 = MagicMock()
        func1.get_reward.return_value = {"agent0": 10}
        func2.get_reward.return_value = {"agent1": 20}
        compat_reward_function._reward_functions = [func1, func2]
        self.assertEqual(compat_reward_function.get_reward(),
                         {"agent0": 10, "agent1": 20})
