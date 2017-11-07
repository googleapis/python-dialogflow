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

from detect_intent_stream import detect_intent_stream

AUDIO_FILE_PATH = 'resources/book_a_room.wav'


def test_detect_intent_stream(capsys):
    detect_intent_stream(AUDIO_FILE_PATH)
    out, _ = capsys.readouterr()

    assert 'Intermediate transcript: "book"' in out
    assert 'Fulfillment text: I can help with that.' in out
