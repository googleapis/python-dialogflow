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
from google.cloud.dialogflow_v2beta1.proto import intent_pb2
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2


class CustomException(Exception):
    pass


class TestIntentsClient(unittest.TestCase):
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_intents(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')

        # Mock response
        next_page_token = ''
        intents_element = {}
        intents = [intents_element]
        expected_response = {
            'next_page_token': next_page_token,
            'intents': intents
        }
        expected_response = intent_pb2.ListIntentsResponse(**expected_response)
        grpc_stub.ListIntents.return_value = expected_response

        paged_list_response = client.list_intents(parent)
        resources = list(paged_list_response)
        self.assertEqual(1, len(resources))
        self.assertEqual(expected_response.intents[0], resources[0])

        grpc_stub.ListIntents.assert_called_once()
        args, kwargs = grpc_stub.ListIntents.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.ListIntentsRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_intents_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')

        # Mock exception response
        grpc_stub.ListIntents.side_effect = CustomException()

        paged_list_response = client.list_intents(parent)
        self.assertRaises(errors.GaxError, list, paged_list_response)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        name = client.intent_path('[PROJECT]', '[INTENT]')

        # Mock response
        name_2 = 'name2-1052831874'
        display_name = 'displayName1615086568'
        priority = -1165461084
        is_fallback = False
        ml_enabled = False
        action = 'action-1422950858'
        reset_contexts = True
        root_followup_intent_name = 'rootFollowupIntentName402253784'
        parent_followup_intent_name = 'parentFollowupIntentName-1131901680'
        expected_response = {
            'name': name_2,
            'display_name': display_name,
            'priority': priority,
            'is_fallback': is_fallback,
            'ml_enabled': ml_enabled,
            'action': action,
            'reset_contexts': reset_contexts,
            'root_followup_intent_name': root_followup_intent_name,
            'parent_followup_intent_name': parent_followup_intent_name
        }
        expected_response = intent_pb2.Intent(**expected_response)
        grpc_stub.GetIntent.return_value = expected_response

        response = client.get_intent(name)
        self.assertEqual(expected_response, response)

        grpc_stub.GetIntent.assert_called_once()
        args, kwargs = grpc_stub.GetIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.GetIntentRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        name = client.intent_path('[PROJECT]', '[INTENT]')

        # Mock exception response
        grpc_stub.GetIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.get_intent, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')
        intent = {}

        # Mock response
        name = 'name3373707'
        display_name = 'displayName1615086568'
        priority = -1165461084
        is_fallback = False
        ml_enabled = False
        action = 'action-1422950858'
        reset_contexts = True
        root_followup_intent_name = 'rootFollowupIntentName402253784'
        parent_followup_intent_name = 'parentFollowupIntentName-1131901680'
        expected_response = {
            'name': name,
            'display_name': display_name,
            'priority': priority,
            'is_fallback': is_fallback,
            'ml_enabled': ml_enabled,
            'action': action,
            'reset_contexts': reset_contexts,
            'root_followup_intent_name': root_followup_intent_name,
            'parent_followup_intent_name': parent_followup_intent_name
        }
        expected_response = intent_pb2.Intent(**expected_response)
        grpc_stub.CreateIntent.return_value = expected_response

        response = client.create_intent(parent, intent)
        self.assertEqual(expected_response, response)

        grpc_stub.CreateIntent.assert_called_once()
        args, kwargs = grpc_stub.CreateIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.CreateIntentRequest(
            parent=parent, intent=intent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')
        intent = {}

        # Mock exception response
        grpc_stub.CreateIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.create_intent, parent,
                          intent)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        intent = {}
        language_code = 'languageCode-412800396'

        # Mock response
        name = 'name3373707'
        display_name = 'displayName1615086568'
        priority = -1165461084
        is_fallback = False
        ml_enabled = False
        action = 'action-1422950858'
        reset_contexts = True
        root_followup_intent_name = 'rootFollowupIntentName402253784'
        parent_followup_intent_name = 'parentFollowupIntentName-1131901680'
        expected_response = {
            'name': name,
            'display_name': display_name,
            'priority': priority,
            'is_fallback': is_fallback,
            'ml_enabled': ml_enabled,
            'action': action,
            'reset_contexts': reset_contexts,
            'root_followup_intent_name': root_followup_intent_name,
            'parent_followup_intent_name': parent_followup_intent_name
        }
        expected_response = intent_pb2.Intent(**expected_response)
        grpc_stub.UpdateIntent.return_value = expected_response

        response = client.update_intent(intent, language_code)
        self.assertEqual(expected_response, response)

        grpc_stub.UpdateIntent.assert_called_once()
        args, kwargs = grpc_stub.UpdateIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.UpdateIntentRequest(
            intent=intent, language_code=language_code)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        intent = {}
        language_code = 'languageCode-412800396'

        # Mock exception response
        grpc_stub.UpdateIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.update_intent, intent,
                          language_code)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        name = client.intent_path('[PROJECT]', '[INTENT]')

        client.delete_intent(name)

        grpc_stub.DeleteIntent.assert_called_once()
        args, kwargs = grpc_stub.DeleteIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.DeleteIntentRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        name = client.intent_path('[PROJECT]', '[INTENT]')

        # Mock exception response
        grpc_stub.DeleteIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.delete_intent, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_update_intents(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')
        language_code = 'languageCode-412800396'

        # Mock response
        expected_response = {}
        expected_response = intent_pb2.BatchUpdateIntentsResponse(
            **expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_batch_update_intents', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.BatchUpdateIntents.return_value = operation

        response = client.batch_update_intents(parent, language_code)
        self.assertEqual(expected_response, response.result())

        grpc_stub.BatchUpdateIntents.assert_called_once()
        args, kwargs = grpc_stub.BatchUpdateIntents.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.BatchUpdateIntentsRequest(
            parent=parent, language_code=language_code)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_update_intents_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        parent = client.agent_path('[PROJECT]', '[AGENT]')
        language_code = 'languageCode-412800396'

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_batch_update_intents_exception', done=True)
        operation.error.CopyFrom(error)
        grpc_stub.BatchUpdateIntents.return_value = operation

        response = client.batch_update_intents(parent, language_code)
        self.assertEqual(error, response.exception())

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_delete_intents(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')
        intents = []

        # Mock response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_batch_delete_intents', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.BatchDeleteIntents.return_value = operation

        response = client.batch_delete_intents(parent, intents)
        self.assertEqual(expected_response, response.result())

        grpc_stub.BatchDeleteIntents.assert_called_once()
        args, kwargs = grpc_stub.BatchDeleteIntents.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = intent_pb2.BatchDeleteIntentsRequest(
            parent=parent, intents=intents)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_delete_intents_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.IntentsClient()

        # Mock request
        parent = client.project_path('[PROJECT]')
        intents = []

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_batch_delete_intents_exception', done=True)
        operation.error.CopyFrom(error)
        grpc_stub.BatchDeleteIntents.return_value = operation

        response = client.batch_delete_intents(parent, intents)
        self.assertEqual(error, response.exception())
