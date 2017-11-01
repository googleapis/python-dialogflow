#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""DialogFlow API Entity Python sample.

Examples:
  python entity_service.py -h
  python entity_service.py list \
  --entity-type-id e57238e2-e692-44ea-9216-6be1b2332e2a
  python entity_service.py create new_room --synonyms basement cellar \
  --entity-type-id e57238e2-e692-44ea-9216-6be1b2332e2a
  python entity_service.py delete new_room \
  --entity-type-id e57238e2-e692-44ea-9216-6be1b2332e2a
"""

# [START import_libraries]
import argparse
import os

from google.cloud import dialogflow
from google.cloud.dialogflow import types
# [END import_libraries]


def list_entities(entity_type_id, project_id=None):
    """List entities."""
    entity_types_client = dialogflow.EntityTypesClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or os.getenv('GOOGLE_CLOUD_PROJECT'))

    parent = entity_types_client.entity_type_path(
        project_id, entity_type_id)

    entities = entity_types_client.get_entity_type(parent).entities

    for entity in entities:
        print('Entity value: {}'.format(entity.value))
        print('Entity synonyms: {}\n'.format(entity.synonyms))


def create_entity(entity_type_id, entity_value, synonyms=[],
                  project_id=None):
    """Create an entity of the given entity type."""
    entity_types_client = dialogflow.EntityTypesClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or os.getenv('GOOGLE_CLOUD_PROJECT'))
    # Note: synonyms must be exactly [entity_value] if the
    # entity_type's kind is KIND_LIST
    synonyms = synonyms or [entity_value]

    entity_type_path = entity_types_client.entity_type_path(
        project_id, entity_type_id)

    entity = types.EntityType.Entity()
    entity.value = entity_value
    entity.synonyms.extend(synonyms)

    response = entity_types_client.batch_create_entities(
        entity_type_path, [entity])

    print('Entity created: {}'.format(response))


def delete_entity(entity_type_id, entity_value, project_id=None):
    """Delete entity with the given entity type and entity value."""
    entity_types_client = dialogflow.EntityTypesClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or os.getenv('GOOGLE_CLOUD_PROJECT'))

    entity_type_path = entity_types_client.entity_type_path(
        project_id, entity_type_id)

    entity_types_client.batch_delete_entities(
        entity_type_path, [entity_value])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--project-id',
        help='Project/agent id. Defaults to the value of the '
        'GCLOUD_PROJECT or GOOGLE_CLOUD_PROJECT environment '
        'variables.')

    subparsers = parser.add_subparsers(dest='command')

    list_parser = subparsers.add_parser(
        'list', help=list_entities.__doc__)
    list_parser.add_argument(
        '--entity-type-id',
        help='The id of the entity_type.')

    create_parser = subparsers.add_parser(
        'create', help=create_entity.__doc__)
    create_parser.add_argument(
        'entity_value',
        help='The entity value to be added.')
    create_parser.add_argument(
        '--entity-type-id',
        help='The id of the entity_type to which to add an entity.',
        required=True)
    create_parser.add_argument(
        '--synonyms',
        nargs='*',
        help='The synonyms that will map to the provided entity value.')

    delete_parser = subparsers.add_parser(
        'delete', help=delete_entity.__doc__)
    delete_parser.add_argument(
        '--entity-type-id',
        help='The id of the entity_type.',
        required=True)
    delete_parser.add_argument(
        'entity_value',
        help='The value of the entity to delete.')

    args = parser.parse_args()

    if args.command == 'list':
        list_entities(args.entity_type_id, args.project_id)
    elif args.command == 'create':
        create_entity(
            args.entity_type_id, args.entity_value, args.synonyms,
            args.project_id)
    elif args.command == 'delete':
        delete_entity(
            args.entity_type_id, args.entity_value, args.project_id)
