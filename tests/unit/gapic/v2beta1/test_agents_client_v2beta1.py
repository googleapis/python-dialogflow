# Copyright 2017, Google Inc. All rights reserved.
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
"""Unit tests."""

import mock
import unittest

from google.gax import errors
from google.rpc import status_pb2

from google.cloud import dialogflow_v2beta1
from google.cloud.dialogflow_v2beta1.proto import agent_pb2
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2


class CustomException(Exception):
    pass


class TestAgentsClient(unittest.TestCase):
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_agent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock response
        parent_2 = 'parent21175163357'
        display_name = 'displayName1615086568'
        default_language_code = 'defaultLanguageCode856575222'
        time_zone = 'timeZone36848094'
        description = 'description-1724546052'
        avatar_uri = 'avatarUri-402824826'
        enable_logging = False
        classification_threshold = 1.11581064E8
        expected_response = {
            'parent': parent_2,
            'display_name': display_name,
            'default_language_code': default_language_code,
            'time_zone': time_zone,
            'description': description,
            'avatar_uri': avatar_uri,
            'enable_logging': enable_logging,
            'classification_threshold': classification_threshold
        }
        expected_response = agent_pb2.Agent(**expected_response)
        grpc_stub.GetAgent.return_value = expected_response

        response = client.get_agent(parent)
        self.assertEqual(expected_response, response)

        grpc_stub.GetAgent.assert_called_once()
        args, kwargs = grpc_stub.GetAgent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = agent_pb2.GetAgentRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_agent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock exception response
        grpc_stub.GetAgent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.get_agent, parent)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_search_agents(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock response
        next_page_token = ''
        agents_element = {}
        agents = [agents_element]
        expected_response = {
            'next_page_token': next_page_token,
            'agents': agents
        }
        expected_response = agent_pb2.SearchAgentsResponse(**expected_response)
        grpc_stub.SearchAgents.return_value = expected_response

        paged_list_response = client.search_agents(parent)
        resources = list(paged_list_response)
        self.assertEqual(1, len(resources))
        self.assertEqual(expected_response.agents[0], resources[0])

        grpc_stub.SearchAgents.assert_called_once()
        args, kwargs = grpc_stub.SearchAgents.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = agent_pb2.SearchAgentsRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_search_agents_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock exception response
        grpc_stub.SearchAgents.side_effect = CustomException()

        paged_list_response = client.search_agents(parent)
        self.assertRaises(errors.GaxError, list, paged_list_response)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_train_agent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_train_agent', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.TrainAgent.return_value = operation

        response = client.train_agent(parent)
        self.assertEqual(expected_response, response.result())

        grpc_stub.TrainAgent.assert_called_once()
        args, kwargs = grpc_stub.TrainAgent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = agent_pb2.TrainAgentRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_train_agent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_train_agent_exception', done=True)
        operation.error.CopyFrom(error)
        grpc_stub.TrainAgent.return_value = operation

        response = client.train_agent(parent)
        self.assertEqual(error, response.exception())

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_export_agent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock response
        agent_uri = 'agentUri-1700713166'
        agent_content = b'63'
        expected_response = {
            'agent_uri': agent_uri,
            'agent_content': agent_content
        }
        expected_response = agent_pb2.ExportAgentResponse(**expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_export_agent', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.ExportAgent.return_value = operation

        response = client.export_agent(parent)
        self.assertEqual(expected_response, response.result())

        grpc_stub.ExportAgent.assert_called_once()
        args, kwargs = grpc_stub.ExportAgent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = agent_pb2.ExportAgentRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_export_agent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_export_agent_exception', done=True)
        operation.error.CopyFrom(error)
        grpc_stub.ExportAgent.return_value = operation

        response = client.export_agent(parent)
        self.assertEqual(error, response.exception())

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_import_agent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_import_agent', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.ImportAgent.return_value = operation

        response = client.import_agent(parent)
        self.assertEqual(expected_response, response.result())

        grpc_stub.ImportAgent.assert_called_once()
        args, kwargs = grpc_stub.ImportAgent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = agent_pb2.ImportAgentRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_import_agent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_import_agent_exception', done=True)
        operation.error.CopyFrom(error)
        grpc_stub.ImportAgent.return_value = operation

        response = client.import_agent(parent)
        self.assertEqual(error, response.exception())

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_restore_agent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_restore_agent', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.RestoreAgent.return_value = operation

        response = client.restore_agent(parent)
        self.assertEqual(expected_response, response.result())

        grpc_stub.RestoreAgent.assert_called_once()
        args, kwargs = grpc_stub.RestoreAgent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = agent_pb2.RestoreAgentRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_restore_agent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.AgentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_restore_agent_exception', done=True)
        operation.error.CopyFrom(error)
        grpc_stub.RestoreAgent.return_value = operation

        response = client.restore_agent(parent)
        self.assertEqual(error, response.exception())
