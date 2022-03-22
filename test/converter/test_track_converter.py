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
from deepracer_compat_reward_function.converter.track_converter import TrackConverter


class TrackConverterTest(TestCase):
    def setUp(self):
        self.deepracer_env_state = MagicMock()
        self.deepracer_env_state.track.to_dict.return_value = {
            "is_clockwise": True,
            "test_key": "test_value"}
        self.track_converter = TrackConverter(self.deepracer_env_state)

    def test_convert(self) -> None:
        self.assertEqual(self.track_converter.convert(),
                         {"is_reversed": True,
                          "test_key": "test_value"})
