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
"""DialogFlow API Context Python sample.

Examples:
  python context_service.py -h
  python context_service.py list --session-id mysession
  python context_service.py create --session-id mysession \
  --context-id mycontext
  python context_service.py delete --session-id mysession \
  --context-id mycontext
"""

# [START import_libraries]
import argparse
import os

from google.cloud import dialogflow
from google.cloud.dialogflow import types
# [END import_libraries]


def list_contexts(session_id, project_id=None):
    """List contexts."""
    contexts_client = dialogflow.ContextsClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or os.getenv('GOOGLE_CLOUD_PROJECT'))

    session_path = contexts_client.session_path(project_id, session_id)

    contexts = contexts_client.list_contexts(session_path)

    print('Contexts for session {}:\n'.format(session_path))
    for context in contexts:
        print('Context name: {}'.format(context.name))
        print('Lifespan count: {}'.format(context.lifespan_count))
        print('Fields:')
        for field, string_value in context.parameters.fields.items():
            if string_value.string_value:
                print('\t{}: {}'.format(field, string_value))


def create_context(context_id, session_id, lifespan_count=None,
                   project_id=None):
    """Create an entity type with the given display name."""
    contexts_client = dialogflow.ContextsClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or os.getenv('GOOGLE_CLOUD_PROJECT'))
    lifespan_count = lifespan_count or 1

    session_path = contexts_client.session_path(project_id, session_id)
    context_name = contexts_client.context_path(
        project_id, session_id, context_id)

    context = types.Context(name=context_name, lifespan_count=lifespan_count)

    response = contexts_client.create_context(session_path, context)

    print('Context created: \n{}'.format(response))


def delete_context(context_id, session_id, project_id=None):
    """Delete entity type with the given entity type name.
    """
    contexts_client = dialogflow.ContextsClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or os.getenv('GOOGLE_CLOUD_PROJECT'))

    context_name = contexts_client.context_path(
        project_id, session_id, context_id)

    contexts_client.delete_context(context_name)


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
        'list', help=list_contexts.__doc__)
    list_parser.add_argument(
        '--session-id',
        required=True)

    create_parser = subparsers.add_parser(
        'create', help=create_context.__doc__)
    create_parser.add_argument(
        '--session-id',
        required=True)
    create_parser.add_argument(
        '--context-id',
        help='The id of the context.',
        required=True)
    create_parser.add_argument(
        '--lifespan-count',
        help='The lifespan_count of the context.  Defaults to 1.')

    delete_parser = subparsers.add_parser(
        'delete', help=delete_context.__doc__)
    delete_parser.add_argument(
        '--session-id',
        required=True)
    delete_parser.add_argument(
        '--context-id',
        help='The id of the context.',
        required=True)

    args = parser.parse_args()

    if args.command == 'list':
        list_contexts(args.session_id, args.project_id)
    elif args.command == 'create':
        create_context(
            args.context_id, args.session_id, args.lifespan_count,
            args.project_id)
    elif args.command == 'delete':
        delete_context(args.context_id, args.session_id, args.project_id)
