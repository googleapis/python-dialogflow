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
import entity_service

# NOTE: This will actually affect the project's agent during the test.

ENTITY_TYPE_DISPLAY_NAME = 'fake_entity_type_for_testing'
ENTITY_VALUE_1 = 'fake_entity_for_testing_1'
ENTITY_VALUE_2 = 'fake_entity_for_testing_2'
SYNONYMS = ['fake_synonym_for_testing_1', 'fake_synonym_for_testing_2']


def test_create_entity_type(capsys):
    entity_type_ids = entity_type_service._get_entity_type_ids(ENTITY_TYPE_DISPLAY_NAME)

    assert len(entity_type_ids) == 0

    entity_type = entity_type_service.create_entity_type(ENTITY_TYPE_DISPLAY_NAME)
    out, _ = capsys.readouterr()

    assert 'display_name: "{}"'.format(ENTITY_TYPE_DISPLAY_NAME) in out

    entity_type_ids = entity_type_service._get_entity_type_ids(ENTITY_TYPE_DISPLAY_NAME)

    assert len(entity_type_ids) == 1


def test_create_entity(capsys):
    entity_type_id = entity_type_service._get_entity_type_ids(ENTITY_TYPE_DISPLAY_NAME)[0]
    
    entity_service.create_entity(entity_type_id, ENTITY_VALUE_1)
    entity_service.create_entity(entity_type_id, ENTITY_VALUE_2, SYNONYMS)

    entity_service.list_entities(entity_type_id)
    out, _ = capsys.readouterr()

    assert 'Entity value: {}'.format(ENTITY_VALUE_1) in out
    assert 'Entity value: {}'.format(ENTITY_VALUE_2) in out
    for synonym in SYNONYMS:
        assert synonym in out
    

def test_delete_entity(capsys):
    entity_type_id = entity_type_service._get_entity_type_ids(ENTITY_TYPE_DISPLAY_NAME)[0]
    
    entity_service.delete_entity(entity_type_id, ENTITY_VALUE_1)
    entity_service.delete_entity(entity_type_id, ENTITY_VALUE_2)

    entity_service.list_entities(entity_type_id)
    out, _ = capsys.readouterr()

    assert out == ''


def test_delete_entity_type(capsys):
    entity_type_ids = entity_type_service._get_entity_type_ids(ENTITY_TYPE_DISPLAY_NAME)

    for entity_type_id in entity_type_ids:
        entity_type_service.delete_entity_type(entity_type_id)

    entity_type_ids = entity_type_service._get_entity_type_ids(ENTITY_TYPE_DISPLAY_NAME)

    assert len(entity_type_ids) == 0
