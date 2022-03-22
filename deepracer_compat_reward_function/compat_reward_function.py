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
"""A class for compatible reward function"""
from typing import Dict, Callable

from deepracer_compat_reward_function.reward_function_wrapper import RewardFunctionWrapper
from deepracer_env import DeepRacerEnv
from deepracer_env_state import DeepRacerEnvState


class CompatRewardFunction():
    """
    CompatRewardFunction class
    """
    def __init__(self,
                 reward_function_dict: Dict[str, Callable],
                 deepracer_env: DeepRacerEnv):
        """
        CompatRewardFunction constructor

        Args:
            reward_function_dict(Dict[str, Callable]: dict with key of agent name and value of
                                                      reward function callable
            deepracer_env (DeepRacerEnv): DeepRacerEnv instance
        """
        self._deepracer_env_state = DeepRacerEnvState(deepracer_env)
        self._reward_functions = [
            RewardFunctionWrapper(name, function, self._deepracer_env_state)
            for name, function in reward_function_dict.items()]

    def get_reward(self) -> Dict[str, float]:
        """
        Get reward for each agents

        Returns:
            Dict[str, float]: dict with key of agent name and value of reward values
        """
        rewards = {}
        for reward_function in self._reward_functions:
            rewards.update(reward_function.get_reward())
        return rewards
