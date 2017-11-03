# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import pytest

import intent_service

# NOTE: This will actually affect the project's agent during the test.
INTENT_DISPLAY_NAME = 'fake_display_name_for_testing'
ACTION = 'fake_action_for_testing'
INPUT_CONTEXT_IDS = [
    'fake_context_id_for_testing_1',
    'fake_context_id_for_testing_2'
]
TRAINING_PHRASE_PARTS = [
    'fake_training_phrase_part_1',
    'fake_training_phease_part_2'
]


def test_create_intent(capsys):
    intent_service.create_intent(INTENT_DISPLAY_NAME, ACTION, TRAINING_PHRASE_PARTS, INPUT_CONTEXT_IDS)

    intent_ids = intent_service._get_intent_ids(INTENT_DISPLAY_NAME)

    assert len(intent_ids) == 1

    intent_service.list_intents()

    out, _ = capsys.readouterr()

    assert INTENT_DISPLAY_NAME in out
    assert ACTION in out
    for intent_content_id in INPUT_CONTEXT_IDS:
        assert intent_content_id in out


def test_delete_session_entity_type(capsys):
    intent_ids = intent_service._get_intent_ids(INTENT_DISPLAY_NAME)

    for intent_id in intent_ids:
        intent_service.delete_intent(intent_id)

    intent_service.list_intents()
    out, _ = capsys.readouterr()

    assert INTENT_DISPLAY_NAME not in out

    intent_ids = intent_service._get_intent_ids(INTENT_DISPLAY_NAME)

    assert len(intent_ids) == 0

