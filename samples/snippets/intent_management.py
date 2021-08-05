#!/usr/bin/env python

# Copyright 2017 Google LLC
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
  python intent_management.py --project-id PROJECT_ID create \
  "room.cancellation - yes" \
  --training-phrases-parts "cancel" "cancellation" \
  --message-texts "Are you sure you want to cancel?" "Cancelled."
  python intent_management.py --project-id PROJECT_ID delete \
  74892d81-7901-496a-bb0a-c769eda5180e
"""

import argparse


# [START dialogflow_delete_intent]
def delete_intent(project_id, intent_id):
    """Delete intent with the given intent type and intent value."""
    from google.cloud import dialogflow

    intents_client = dialogflow.IntentsClient()

    intent_path = intents_client.intent_path(project_id, intent_id)

    intents_client.delete_intent(request={"name": intent_path})


# [END dialogflow_delete_intent]


# Helper to get intent from display name.
def _get_intent_ids(project_id, display_name):
    from google.cloud import dialogflow

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    intents = intents_client.list_intents(request={"parent": parent})
    intent_names = [
        intent.name for intent in intents if intent.display_name == display_name
    ]

    intent_ids = [intent_name.split("/")[-1] for intent_name in intent_names]

    return intent_ids


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--project-id", help="Project/agent id.  Required.", required=True
    )

    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list", help=list_intents.__doc__)

    create_parser = subparsers.add_parser("create", help=create_intent.__doc__)
    create_parser.add_argument("display_name")
    create_parser.add_argument(
        "--training-phrases-parts",
        nargs="*",
        type=str,
        help="Training phrases.",
        default=[],
    )
    create_parser.add_argument(
        "--message-texts",
        nargs="*",
        type=str,
        help="Message texts for the agent's response when the intent " "is detected.",
        default=[],
    )

    delete_parser = subparsers.add_parser("delete", help=delete_intent.__doc__)
    delete_parser.add_argument("intent_id", help="The id of the intent.")

    args = parser.parse_args()

    if args.command == "list":
        list_intents(args.project_id)
    elif args.command == "create":
        create_intent(
            args.project_id,
            args.display_name,
            args.training_phrases_parts,
            args.message_texts,
        )
    elif args.command == "delete":
        delete_intent(args.project_id, args.intent_id)
