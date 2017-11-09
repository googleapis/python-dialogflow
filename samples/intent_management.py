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

"""DialogFlow API Intent Python sample showing how to manage intents.

Examples:
  python intent_management.py -h
  python intent_management.py --project-id PROJECT_ID list
  python intent_management.py create "room.cancellation - yes" \
  --action room.cancel --input-context-ids today tomorrow \
  --training-phrases-parts "cancel" "cancellation"
  python intent_management.py delete 74892d81-7901-496a-bb0a-c769eda5180e
"""

# [START import_libraries]
import argparse

from google.cloud import dialogflow
# [END import_libraries]


def list_intents(project_id):
    intents_client = dialogflow.IntentsClient()

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


def create_intent(project_id, display_name, action, training_phrases_parts,
                  input_context_ids):
    """Create an intent of the given intent type."""
    intents_client = dialogflow.IntentsClient()
    contexts_client = dialogflow.ContextsClient()

    parent = intents_client.project_agent_path(project_id)
    # Setting session_id as '-' for contexts which are not
    # session-bound.
    input_context_names = [
        contexts_client.context_path(project_id, '-', context_id)
        for context_id in input_context_ids]
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    intent = dialogflow.types.Intent(
        display_name=display_name, action=action,
        training_phrases=training_phrases,
        input_context_names=input_context_names)

    response = intents_client.create_intent(parent, intent)

    print('Intent created: {}'.format(response))


def delete_intent(project_id, intent_id):
    """Delete intent with the given intent type and intent value."""
    intents_client = dialogflow.IntentsClient()

    intent_path = intents_client.intent_path(project_id, intent_id)

    intents_client.delete_intent(intent_path)


# Helper to get intent from display name.
def _get_intent_ids(project_id, display_name):
    intents_client = dialogflow.IntentsClient()

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
        help='Project/agent id.  Required.',
        required=True)

    subparsers = parser.add_subparsers(dest='command')

    list_parser = subparsers.add_parser(
        'list', help=list_intents.__doc__)

    create_parser = subparsers.add_parser(
        'create', help=create_intent.__doc__)
    create_parser.add_argument(
        'display_name')
    create_parser.add_argument(
        '--action')
    create_parser.add_argument(
        '--training-phrases-parts',
        nargs='*',
        type=str,
        help='Training phrases.',
        default=[])
    create_parser.add_argument(
        '--input-context-ids',
        nargs='*',
        type=str,
        help='Input context ids.',
        default=[])

    delete_parser = subparsers.add_parser(
        'delete', help=delete_intent.__doc__)
    delete_parser.add_argument(
        'intent_id',
        help='The id of the intent.')

    args = parser.parse_args()

    if args.command == 'list':
        list_intents(args.project_id)
    elif args.command == 'create':
        create_intent(
            args.project_id, args.display_name, args.action,
            args.training_phrases_parts,
            args.input_context_ids, )
    elif args.command == 'delete':
        delete_intent(args.project_id, args.intent_id)
