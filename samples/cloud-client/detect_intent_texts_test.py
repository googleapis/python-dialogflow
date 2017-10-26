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
import re
import pytest

from detect_intent_texts import detect_intent_texts

PROJECT_ID = os.getenv('GCLOUD_PROJECT') or (os.getenv('GOOGLE_CLOUD_PROJECT'))
TEXTS = ["hello", "book a meeting room", "Mountain View",
    "tomorrow", "10am", "2 hours", "10 people", "A", "yes"]


def test_detect_intent_texts(capsys):
    detect_intent_texts(PROJECT_ID, TEXTS)
    out, _ = capsys.readouterr()

    assert 'Fulfillment text: All set!' in out