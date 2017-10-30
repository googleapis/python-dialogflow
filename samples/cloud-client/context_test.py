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

import detect_intent_texts
import context_service

# NOTE: This will actually affect the project's agent during the test.

SESSION_ID = 'fake_session_for_testing'
CONTEXT_ID = 'fake_context_for_testing'


def test_create_context(capsys):
    # Calling detect intent to create a session.
    detect_intent_texts.detect_intent_texts(['hi'], session_id=SESSION_ID)

    context_service.create_context(CONTEXT_ID, SESSION_ID)
    context_service.list_contexts(SESSION_ID)

    out, _ = capsys.readouterr()
    assert CONTEXT_ID in out


def test_delete_context(capsys):
    context_service.delete_context(CONTEXT_ID, SESSION_ID)
    context_service.list_contexts(SESSION_ID)

    out, _ = capsys.readouterr()
    assert CONTEXT_ID not in out
