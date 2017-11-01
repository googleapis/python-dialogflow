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
"""DialogFlow API Intent Python sample.

Examples:
  python intent_service.py -h
  python intent_service.py list
  python intent_service.py create "room.cancellation - yes" \
  --action room.cancel
  python intent_service.py delete 74892d81-7901-496a-bb0a-c769eda5180e
"""

# [START import_libraries]
import argparse
import os

from google.cloud import dialogflow
from google.cloud.dialogflow import types
# [END import_libraries]


def list_intents(project_id=None):
    """List intents."""
    intents_client = dialogflow.IntentsClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or (os.getenv('GOOGLE_CLOUD_PROJECT')))

    parent = intents_client.project_agent_path(project_id)

    intents = intents_client.list_intents(parent)

    for intent in intents:
        print('=' * 20)
        print('Intent name: {}'.format(intent.name))
        print('Intent display_name: {}'.format(intent.display_name))
        print('Action: {}\n'.format(intent.action))
        print('Root followup intent: {}'.format(
            intent.root_followup_intent_name))
        print('Parent followup intent: {}\n'.format(
            intent.parent_followup_intent_name))

        print('Input contexts:')
        for input_context_name in intent.input_context_names:
            print('\tName: {}'.format(input_context_name))

        print('Output contexts:')
        for output_context in intent.output_contexts:
            print('\tName: {}'.format(output_context.name))


def create_intent(display_name, action=None, project_id=None):
    """Create an intent of the given intent type."""
    intents_client = dialogflow.IntentsClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or (os.getenv('GOOGLE_CLOUD_PROJECT')))

    parent = intents_client.project_agent_path(project_id)
    intent = types.Intent(display_name=display_name, action=action)

    response = intents_client.create_intent(parent, intent)

    print('Intent created: {}'.format(response))


def delete_intent(intent_id, project_id=None):
    """Delete intent with the given intent type and intent value."""
    intents_client = dialogflow.IntentsClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or (os.getenv('GOOGLE_CLOUD_PROJECT')))

    intent_path = intents_client.intent_path(project_id, intent_id)

    intents_client.delete_intent(intent_path)


# Helper to get intent from display name.
def _get_intent_ids(display_name, project_id=None):
    intents_client = dialogflow.IntentsClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or (os.getenv('GOOGLE_CLOUD_PROJECT')))

    parent = intents_client.project_agent_path(project_id)
    intents = intents_client.list_intents(parent)
    intent_names = [
        intent.name for intent in intents
        if intent.display_name == display_name]

    intent_ids = [
        intent_name.split('/')[-1] for intent_name
        in intent_names]

    return intent_ids


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
        'list', help=list_intents.__doc__)

    create_parser = subparsers.add_parser(
        'create', help=create_intent.__doc__)
    create_parser.add_argument(
        'display_name')
    create_parser.add_argument(
        '--action')

    delete_parser = subparsers.add_parser(
        'delete', help=delete_intent.__doc__)
    delete_parser.add_argument(
        'intent_id',
        help='The id of the intent.')

    args = parser.parse_args()

    if args.command == 'list':
        list_intents(args.project_id)
    elif args.command == 'create':
        create_intent(args.display_name, args.action, args.project_id)
    elif args.command == 'delete':
        delete_intent(args.intent_id, args.project_id)
