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
"""A class for reward function wrapper"""
from typing import Callable, Dict

from deepracer_env_state import DeepRacerEnvState
from deepracer_compat_reward_function.converter.agent_converter import AgentConverter
from deepracer_compat_reward_function.converter.object_converter import ObjectConverter
from deepracer_compat_reward_function.converter.track_converter import TrackConverter


class RewardFunctionWrapper():
    """
    RewardFunctionWrapper class
    """
    def __init__(self,
                 agent_name: str,
                 reward_function: Callable,
                 deepracer_env_state: DeepRacerEnvState):
        """
        RewardFunctionWrapper constructor

        Args:
            agent_name (str): agent name
            reward_function (Callable): reward function Callable
            deepracer_env_state (DeepRacerEnvState): DeepRacerEnvState class instance
        """
        self._agent_name = agent_name
        self._reward_function = reward_function
        self._deepracer_env_state = deepracer_env_state
        self._converters = {
            AgentConverter(self._agent_name, self._deepracer_env_state),
            ObjectConverter(self._deepracer_env_state),
            TrackConverter(self._deepracer_env_state)}

    def get_reward(self) -> Dict[str, float]:
        """
        Get reward value

        Returns:
            Dict[str, float]: dict with key of agent name and value of reward value
        """
        reward_param_dict = dict()
        for converter in self._converters:
            reward_param_dict.update(converter.convert())
        return {self._agent_name: self._reward_function(reward_param_dict)}
