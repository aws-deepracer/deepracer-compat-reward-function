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
"""A class for object converter"""
from typing import Dict, Any

from deepracer_env_state import DeepRacerEnvState
from deepracer_compat_reward_function.converter.state_converter_interface import StateConverterInterface


class ObjectConverter(StateConverterInterface):
    """
    ObjectConverter class
    """
    def __init__(self, deepracer_env_state: DeepRacerEnvState):
        """
        ObjectConverter constructor

        Args:
            deepracer_env_state (DeepRacerEnvState): DeepRacerEnvState class instance
        """
        self._deepracer_env_state = deepracer_env_state

    def convert(self) -> Dict[str, Any]:
        """
        Convert to dict format for object

        DeepRacer is currently only suport time trial, so we
        assign default value for objects

        Returns:
            Dict[str, Any]: dict with key as str and value as Any
        """
        object_dict = dict()
        object_dict["objects_speed"] = []
        object_dict["objects_location"] = []
        object_dict["objects_heading"] = []
        object_dict["objects_left_of_center"] = []
        return object_dict
