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
"""A class for agent converter"""
from typing import Dict, Any

from deepracer_env_state import DeepRacerEnvState
from deepracer_compat_reward_function.converter.state_converter_interface import StateConverterInterface
from deepracer_compat_reward_function.utils import radian_to_degree


class AgentConverter(StateConverterInterface):
    """
    AgentConverter class
    """
    def __init__(self, agent_name: str, deepracer_env_state: DeepRacerEnvState):
        """
        AgentConverter constructor

        Args:
            agent_name (str): agent name
            deepracer_env_state (DeepRacerEnvState): DeepRacerEnvState class instance
        """
        self._agent_name = agent_name
        self._deepracer_env_state = deepracer_env_state

    def convert(self) -> Dict[str, Any]:
        """
        Convert to dict format for agent

        Returns:
            Dict[str, Any]: dict with key as str and value as Any
        """
        agent_dict = self._deepracer_env_state.agents[self._agent_name].to_dict()
        agent_dict["heading"] = radian_to_degree(agent_dict["yaw"])
        del agent_dict["yaw"]
        del agent_dict["roll"]
        del agent_dict["pitch"]
        del agent_dict["z"]
        agent_dict["is_crashed"] = False
        agent_dict["closest_objects"] = [0, 0]
        agent_dict["objects_distance"] = []
        return agent_dict
