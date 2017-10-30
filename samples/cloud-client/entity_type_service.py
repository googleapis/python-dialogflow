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
"""DialogFlow API Entity Type Python sample.

Examples:
  python entity_type_service.py -h
  python entity_type_service.py list
  python entity_type_service.py create employee
  python entity_type_service.py delete e57238e2-e692-44ea-9216-6be1b2332e2a
"""

# [START import_libraries]
import argparse
import os

from google.cloud import dialogflow
from google.cloud.dialogflow import enums
from google.cloud.dialogflow import types
# [END import_libraries]


def list_entity_types(project_id=None):
    """List entity types."""
    entity_types_client = dialogflow.EntityTypesClient()

    project_id = project_id or os.getenv('GCLOUD_PROJECT') or (os.getenv('GOOGLE_CLOUD_PROJECT'))
    
    parent = entity_types_client.project_agent_path(project_id)
    
    entity_types = entity_types_client.list_entity_types(parent)

    for entity_type in entity_types:
        print('Entity type name: {}'.format(entity_type.name))
        print('Entity type display name: {}'.format(entity_type.display_name))
        print('Number of entities: {}\n'.format(len(entity_type.entities)))



def create_entity_type(display_name, kind=None, project_id=None):
    """Create an entity type with the given display name."""
    entity_types_client = dialogflow.EntityTypesClient()

    project_id = project_id or os.getenv('GCLOUD_PROJECT') or (os.getenv('GOOGLE_CLOUD_PROJECT'))
    kind = kind or enums.EntityType.Kind.KIND_MAP
    
    parent = entity_types_client.project_agent_path(project_id)

    entity_type = types.EntityType(display_name=display_name, kind=kind)

    response = entity_types_client.create_entity_type(parent, entity_type)

    print('Entity type created: \n{}'.format(response))


def delete_entity_type(entity_type, project_id=None):
    """Delete entity type with the given entity type name."""
    entity_types_client = dialogflow.EntityTypesClient()

    project_id = project_id or os.getenv('GCLOUD_PROJECT') or (os.getenv('GOOGLE_CLOUD_PROJECT'))
    
    entity_type_path = entity_types_client.entity_type_path(project_id, entity_type)

    response = entity_types_client.delete_entity_type(entity_type_path)


# Helper to get entity_type_id from display name.
def _get_entity_type_ids(display_name, project_id=None):
    entity_types_client = dialogflow.EntityTypesClient()

    project_id = project_id or os.getenv('GCLOUD_PROJECT') or (os.getenv('GOOGLE_CLOUD_PROJECT'))

    parent = entity_types_client.project_agent_path(project_id)
    entity_types = entity_types_client.list_entity_types(parent)
    entity_type_names = [entity_type.name for entity_type in entity_types if entity_type.display_name == display_name]

    entity_type_ids = [entity_type_name.split('/')[-1] for entity_type_name in entity_type_names]

    return entity_type_ids


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--project-id',
        help='Project/agent id. Defaults to the value of the GCLOUD_PROJECT or '
        'GOOGLE_CLOUD_PROJECT environment variables.')

    subparsers = parser.add_subparsers(dest='command')

    list_parser = subparsers.add_parser(
        'list', help=list_entity_types.__doc__)

    create_parser = subparsers.add_parser(
        'create', help=create_entity_type.__doc__)
    create_parser.add_argument(
        'display_name',
        help='The display name of the entity.')
    create_parser.add_argument(
        '--kind',
        help='The kind of entity.  KIND_MAP (default) or KIND_LIST.')

    delete_parser = subparsers.add_parser(
        'delete', help=delete_entity_type.__doc__)
    delete_parser.add_argument(
        'entity_type',
        help='The id of the entity_type.')

    args = parser.parse_args()

    if args.command == 'list':
        list_entity_types(args.project_id)
    elif args.command == 'create':
        create_entity_type(args.display_name, args.project_id)
    elif args.command == 'delete':
        delete_entity_type(args.entity_type, args.project_id)

