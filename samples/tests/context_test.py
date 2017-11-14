# Copyright 2017 Google LLC
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

from __future__ import absolute_import
import os

from .. import detect_intent_texts
from .. import context_management

PROJECT_ID = os.getenv('GCLOUD_PROJECT')
SESSION_ID = 'fake_session_for_testing'
CONTEXT_ID = 'fake_context_for_testing'


def test_create_context(capsys):
    # Calling detect intent to create a session.
    detect_intent_texts.detect_intent_texts(
        PROJECT_ID, SESSION_ID, ['hi'], 'en-US')

    context_management.create_context(PROJECT_ID, SESSION_ID, CONTEXT_ID, 1)
    context_management.list_contexts(PROJECT_ID, SESSION_ID)

    out, _ = capsys.readouterr()
    assert CONTEXT_ID in out


def test_delete_context(capsys):
    context_management.delete_context(PROJECT_ID, SESSION_ID, CONTEXT_ID)
    context_management.list_contexts(PROJECT_ID, SESSION_ID)

    out, _ = capsys.readouterr()
    assert CONTEXT_ID not in out
