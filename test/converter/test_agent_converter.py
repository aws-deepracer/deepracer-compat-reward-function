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
from deepracer_compat_reward_function.converter.agent_converter import AgentConverter
from deepracer_compat_reward_function.utils import radian_to_degree


class AgentConverterTest(TestCase):
    def setUp(self) -> None:
        self.deepracer_env_state = MagicMock()
        self.agent_name = "agent0"
        agent = MagicMock()
        self.deepracer_env_state.agents = {self.agent_name: agent}
        self.agent_converter = AgentConverter(self.agent_name, self.deepracer_env_state)

    def test_convert(self) -> None:
        agent = MagicMock()
        self.deepracer_env_state.agents = {self.agent_name: agent}
        agent.to_dict.return_value = {
            "roll": 0.1,
            "pitch": 0.2,
            "yaw": 0.3,
            "z": 0.4,
            "agent_key": "agent_value"}
        self.assertEqual(self.agent_converter.convert(),
                         {"heading": radian_to_degree(0.3),
                          "agent_key": "agent_value",
                          "is_crashed": False,
                          "closest_objects": [0, 0],
                          "objects_distance": []})
