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

import entity_type_service
import session_entity_type_service

# NOTE: This will actually affect the project's agent during the test.

SESSION_ID = 'fake_session_for_testing'
ENTITY_TYPE_DISPLAY_NAME = 'fake_display_name_for_testing'
ENTITY_VALUES = ['fake_entity_value_1', 'fake_entity_value_2']


def test_create_session_entity_type(capsys):
    # Create an entity type
    entity_type_service.create_entity_type(ENTITY_TYPE_DISPLAY_NAME)

    session_entity_type_service.create_session_entity_type(ENTITY_VALUES, ENTITY_TYPE_DISPLAY_NAME, SESSION_ID)
    session_entity_type_service.list_session_entity_types(SESSION_ID)

    out, _ = capsys.readouterr()

    assert SESSION_ID in out
    assert ENTITY_TYPE_DISPLAY_NAME in out
    for entity_value in ENTITY_VALUES:
        assert entity_value in out


def test_delete_session_entity_type(capsys):
    session_entity_type_service.delete_session_entity_type(ENTITY_TYPE_DISPLAY_NAME, SESSION_ID)
    session_entity_type_service.list_session_entity_types(SESSION_ID)

    out, _ = capsys.readouterr()
    assert ENTITY_TYPE_DISPLAY_NAME not in out
    for entity_value in ENTITY_VALUES:
        assert entity_value not in out

    # Clean up entity type
    entity_type_ids = entity_type_service._get_entity_type_ids(ENTITY_TYPE_DISPLAY_NAME)
    for entity_type_id in entity_type_ids:
        entity_type_service.delete_entity_type(entity_type_id)
