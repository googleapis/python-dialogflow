#!/usr/bin/env python

# Copyright 2018 Google LLC
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

"""Dialogflow API Python sample showing how to manage Knowledge bases.

Examples:
  python knowledge_base_management.py -h
  python knowledge_base_management.py --project-id PROJECT_ID \
  list
  python knowledge_base_management.py --project-id PROJECT_ID \
  create --display-name DISPLAY_NAME
  python knowledge_base_management.py --project-id PROJECT_ID \
  get --knowledge-base-id knowledge_base_id
  python knowledge_base_management.py --project-id PROJECT_ID \
  delete --knowledge-base-id knowledge_base_id
"""

import argparse


# [START dialogflow_list_knowledge_base]
def list_knowledge_bases(project_id):
    """Lists the Knowledge bases belonging to a project.

    Args:
        project_id: The GCP project linked with the agent."""
    import dialogflow_v2beta1 as dialogflow
    client = dialogflow.KnowledgeBasesClient()
    agent_path = client.project_agent_path(project_id)

    print('Knowledge Bases for: {}'.format(project_id))
    for knowledge_base in client.list_knowledge_bases(agent_path):
        print(' - Display Name: {}'.format(knowledge_base.display_name))
        print(' - Knowledge ID: {}\n'.format(knowledge_base.name))
# [END dialogflow_list_knowledge_base]


# [START dialogflow_create_knowledge_base]
def create_knowledge_base(project_id, display_name):
    """Creates a Knowledge base.

    Args:
        project_id: The GCP project linked with the agent.
        display_name: The display name of the Knowledge base."""
    import dialogflow_v2beta1 as dialogflow
    client = dialogflow.KnowledgeBasesClient()
    agent_path = client.project_agent_path(project_id)

    knowledge_base = dialogflow.types.KnowledgeBase(
        display_name=display_name)

    response = client.create_knowledge_base(agent_path, knowledge_base)

    print('Knowledge Base created:\n')
    print('Display Name: {}\n'.format(response.display_name))
    print('Knowledge ID: {}\n'.format(response.name))
# [END dialogflow_create_knowledge_base]


# [START dialogflow_get_knowledge_base]
def get_knowledge_base(project_id, knowledge_base_id):
    """Gets a specific Knowledge base.

    Args:
        project_id: The GCP project linked with the agent.
        knowledge_base_id: Id of the Knowledge base."""
    import dialogflow_v2beta1 as dialogflow
    client = dialogflow.KnowledgeBasesClient()
    name = client.knowledge_base_path(project_id, knowledge_base_id)

    response = client.get_knowledge_base(name)

    print('Got Knowledge Base:')
    print(' - Display Name: {}'.format(response.display_name))
    print(' - Knowledge ID: {}'.format(response.name))
# [END dialogflow_get_knowledge_base]


# [START dialogflow_delete_knowledge_base]
def delete_knowledge_base(project_id, knowledge_base_id):
    """Deletes a specific Knowledge base.

    Args:
        project_id: The GCP project linked with the agent.
        knowledge_base_id: Id of the Knowledge base."""
    import dialogflow_v2beta1 as dialogflow
    client = dialogflow.KnowledgeBasesClient()
    name = client.knowledge_base_path(project_id, knowledge_base_id)

    response = client.delete_knowledge_base(name)

    print('Knowledge Base deleted.'.format(response))
# [END dialogflow_delete_knowledge_base]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--project-id', help='Project/agent id.', required=True)

    subparsers = parser.add_subparsers(dest='command')

    list_parser = subparsers.add_parser(
        'list', help='List all Knowledge bases that belong to the project.')

    create_parser = subparsers.add_parser(
        'create', help='Create a new Knowledge base.')
    create_parser.add_argument(
        '--display-name',
        help='A name of the Knowledge base, used for display purpose, '
             'can not be used to identify the Knowledge base.',
        default=str(''))

    get_parser = subparsers.add_parser(
        'get', help='Get a Knowledge base by its id.')
    get_parser.add_argument(
        '--knowledge-base-id', help='The id of the Knowledge base.',
        required=True)

    delete_parser = subparsers.add_parser(
        'delete', help='Delete a Knowledge base by its id.')
    delete_parser.add_argument(
        '--knowledge-base-id',
        help='The id of the Knowledge base you want to delete.',
        required=True)

    args = parser.parse_args()

    if args.command == 'list':
        list_knowledge_bases(args.project_id)
    elif args.command == 'create':
        create_knowledge_base(args.project_id, args.display_name)
    elif args.command == 'get':
        get_knowledge_base(args.project_id, args.knowledge_base_id)
    elif args.command == 'delete':
        delete_knowledge_base(args.project_id, args.knowledge_base_id)
