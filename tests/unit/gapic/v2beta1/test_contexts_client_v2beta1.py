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

from google.cloud import dialogflow_v2beta1
from google.cloud.dialogflow_v2beta1.proto import context_pb2
from google.protobuf import empty_pb2


class CustomException(Exception):
    pass


class TestContextsClient(unittest.TestCase):
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_contexts(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[SESSION]')

        # Mock response
        next_page_token = ''
        contexts_element = {}
        contexts = [contexts_element]
        expected_response = {
            'next_page_token': next_page_token,
            'contexts': contexts
        }
        expected_response = context_pb2.ListContextsResponse(
            **expected_response)
        grpc_stub.ListContexts.return_value = expected_response

        paged_list_response = client.list_contexts(parent)
        resources = list(paged_list_response)
        self.assertEqual(1, len(resources))
        self.assertEqual(expected_response.contexts[0], resources[0])

        grpc_stub.ListContexts.assert_called_once()
        args, kwargs = grpc_stub.ListContexts.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.ListContextsRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_contexts_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[SESSION]')

        # Mock exception response
        grpc_stub.ListContexts.side_effect = CustomException()

        paged_list_response = client.list_contexts(parent)
        self.assertRaises(errors.GaxError, list, paged_list_response)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_context(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        name = client.context_path('[PROJECT]', '[SESSION]', '[CONTEXT]')

        # Mock response
        name_2 = 'name2-1052831874'
        lifespan_count = 1178775510
        expected_response = {'name': name_2, 'lifespan_count': lifespan_count}
        expected_response = context_pb2.Context(**expected_response)
        grpc_stub.GetContext.return_value = expected_response

        response = client.get_context(name)
        self.assertEqual(expected_response, response)

        grpc_stub.GetContext.assert_called_once()
        args, kwargs = grpc_stub.GetContext.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.GetContextRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_context_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        name = client.context_path('[PROJECT]', '[SESSION]', '[CONTEXT]')

        # Mock exception response
        grpc_stub.GetContext.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.get_context, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_context(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[SESSION]')
        context = {}

        # Mock response
        name = 'name3373707'
        lifespan_count = 1178775510
        expected_response = {'name': name, 'lifespan_count': lifespan_count}
        expected_response = context_pb2.Context(**expected_response)
        grpc_stub.CreateContext.return_value = expected_response

        response = client.create_context(parent, context)
        self.assertEqual(expected_response, response)

        grpc_stub.CreateContext.assert_called_once()
        args, kwargs = grpc_stub.CreateContext.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.CreateContextRequest(
            parent=parent, context=context)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_context_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[SESSION]')
        context = {}

        # Mock exception response
        grpc_stub.CreateContext.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.create_context, parent,
                          context)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_context(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        context = {}

        # Mock response
        name = 'name3373707'
        lifespan_count = 1178775510
        expected_response = {'name': name, 'lifespan_count': lifespan_count}
        expected_response = context_pb2.Context(**expected_response)
        grpc_stub.UpdateContext.return_value = expected_response

        response = client.update_context(context)
        self.assertEqual(expected_response, response)

        grpc_stub.UpdateContext.assert_called_once()
        args, kwargs = grpc_stub.UpdateContext.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.UpdateContextRequest(context=context)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_context_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        context = {}

        # Mock exception response
        grpc_stub.UpdateContext.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.update_context, context)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_context(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        name = client.context_path('[PROJECT]', '[SESSION]', '[CONTEXT]')

        client.delete_context(name)

        grpc_stub.DeleteContext.assert_called_once()
        args, kwargs = grpc_stub.DeleteContext.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.DeleteContextRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_context_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        name = client.context_path('[PROJECT]', '[SESSION]', '[CONTEXT]')

        # Mock exception response
        grpc_stub.DeleteContext.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.delete_context, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_all_contexts(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[SESSION]')

        client.delete_all_contexts(parent)

        grpc_stub.DeleteAllContexts.assert_called_once()
        args, kwargs = grpc_stub.DeleteAllContexts.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = context_pb2.DeleteAllContextsRequest(parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_all_contexts_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.ContextsClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[SESSION]')

        # Mock exception response
        grpc_stub.DeleteAllContexts.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.delete_all_contexts, parent)
