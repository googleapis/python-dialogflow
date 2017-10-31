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
"""DialogFlow API SessionEntityType Python sample.

Examples:
  python session_entity_type_service.py -h

  python session_entity_type_service.py list --session-id mysession

  python session_entity_type_service.py create --session-id mysession \
  --entity-type-display-name room --entity-values C D E F

  python session_entity_type_service.py delete --session-id mysession \
  --entity-type-display-name room
"""

# [START import_libraries]
import argparse
import os

from google.cloud import dialogflow
from google.cloud.dialogflow import enums
from google.cloud.dialogflow import types
# [END import_libraries]


def list_session_entity_types(session_id, project_id=None):
    """List session_entity_types."""
    session_entity_types_client = dialogflow.SessionEntityTypesClient()

    project_id = project_id or os.getenv('GCLOUD_PROJECT') or (os.getenv('GOOGLE_CLOUD_PROJECT'))
    
    session_path = session_entity_types_client.session_path(project_id, session_id)
    
    session_entity_types = session_entity_types_client.list_session_entity_types(session_path)

    print('SessionEntityTypes for session {}:\n'.format(session_path))
    for session_entity_type in session_entity_types:
        print('\tSessionEntityType name: {}'.format(session_entity_type.name))
        print('\tNumber of entities: {}\n'.format(len(session_entity_type.entities)))


def create_session_entity_type(entity_values, entity_type_display_name, session_id, entity_override_mode=None, project_id=None):
    """Create an entity type with the given display name."""
    session_entity_types_client = dialogflow.SessionEntityTypesClient()

    project_id = project_id or os.getenv('GCLOUD_PROJECT') or (os.getenv('GOOGLE_CLOUD_PROJECT'))
    entity_override_mode = entity_override_mode or enums.SessionEntityType.EntityOverrideMode.ENTITY_OVERRIDE_MODE_OVERRIDE
    
    session_path = session_entity_types_client.session_path(project_id, session_id)
    session_entity_type_name = session_entity_types_client.session_entity_type_path(project_id, session_id, entity_type_display_name)

    # Here we use the entity value as the only synonym.
    entities = [types.EntityType.Entity(value=value, synonyms=[value]) for value in entity_values]
    session_entity_type = types.SessionEntityType(name=session_entity_type_name, entity_override_mode=entity_override_mode, entities=entities)

    response = session_entity_types_client.create_session_entity_type(session_path, session_entity_type)

    print('SessionEntityType created: \n\n{}'.format(response))


def delete_session_entity_type(entity_type_display_name, session_id, project_id=None):
    """Delete entity type with the given entity type name.
    """
    session_entity_types_client = dialogflow.SessionEntityTypesClient()

    project_id = project_id or os.getenv('GCLOUD_PROJECT') or (os.getenv('GOOGLE_CLOUD_PROJECT'))
    
    session_entity_type_name = session_entity_types_client.session_entity_type_path(project_id, session_id, entity_type_display_name)

    response = session_entity_types_client.delete_session_entity_type(session_entity_type_name)


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
        'list', help=list_session_entity_types.__doc__)
    list_parser.add_argument(
        '--session-id',
        required=True)

    create_parser = subparsers.add_parser(
        'create', help=create_session_entity_type.__doc__)
    create_parser.add_argument(
        '--session-id',
        required=True)
    create_parser.add_argument(
        '--entity-type-display-name',
        help='The DISPLAY NAME of the entity type to be overridden in the session.',
        required=True)
    create_parser.add_argument(
        '--entity-values',
        nargs='*',
        help='The entity values of the session entity type.',
        required=True)
    create_parser.add_argument(
        '--entity-override-mode',
        help='ENTITY_OVERRIDE_MODE_OVERRIDE (default) or ENTITY_OVERRIDE_MODE_SUPPLEMENT')


    delete_parser = subparsers.add_parser(
        'delete', help=delete_session_entity_type.__doc__)
    delete_parser.add_argument(
        '--session-id',
        required=True)
    delete_parser.add_argument(
        '--entity-type-display-name',
        help='The DISPLAY NAME of the entity type.',
        required=True)

    args = parser.parse_args()

    if args.command == 'list':
        list_session_entity_types(args.session_id, args.project_id)
    elif args.command == 'create':
        create_session_entity_type(args.entity_values, args.entity_type_display_name, args.session_id, args.entity_override_mode, args.project_id)
    elif args.command == 'delete':
        delete_session_entity_type(args.entity_type_display_name, args.session_id, args.project_id)

