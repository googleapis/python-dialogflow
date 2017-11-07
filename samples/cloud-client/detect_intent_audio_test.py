# Copyright 2017, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import pytest

from detect_intent_audio import detect_intent_audio

AUDIOS = [
    'resources/book_a_room.wav',
    'resources/mountain_view.wav',
    'resources/today.wav'
]


def test_detect_intent_audio(capsys):
    session_id = 'test-session-id'
    for audio_file_path in AUDIOS:
        detect_intent_audio(audio_file_path, session_id=session_id)
    out, _ = capsys.readouterr()

    assert 'Fulfillment text: What time will the meeting start?' in out
