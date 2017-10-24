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
from google.cloud.dialogflow_v2beta1.proto import session_entity_type_pb2
from google.protobuf import empty_pb2


class CustomException(Exception):
    pass


class TestSessionEntityTypesClient(unittest.TestCase):
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_session_entity_types(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionEntityTypesClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[SESSION]')

        # Mock response
        next_page_token = ''
        session_entity_types_element = {}
        session_entity_types = [session_entity_types_element]
        expected_response = {
            'next_page_token': next_page_token,
            'session_entity_types': session_entity_types
        }
        expected_response = session_entity_type_pb2.ListSessionEntityTypesResponse(
            **expected_response)
        grpc_stub.ListSessionEntityTypes.return_value = expected_response

        paged_list_response = client.list_session_entity_types(parent)
        resources = list(paged_list_response)
        self.assertEqual(1, len(resources))
        self.assertEqual(expected_response.session_entity_types[0],
                         resources[0])

        grpc_stub.ListSessionEntityTypes.assert_called_once()
        args, kwargs = grpc_stub.ListSessionEntityTypes.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = session_entity_type_pb2.ListSessionEntityTypesRequest(
            parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_session_entity_types_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionEntityTypesClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[SESSION]')

        # Mock exception response
        grpc_stub.ListSessionEntityTypes.side_effect = CustomException()

        paged_list_response = client.list_session_entity_types(parent)
        self.assertRaises(errors.GaxError, list, paged_list_response)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_session_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionEntityTypesClient()

        # Mock request
        name = client.session_entity_type_path('[PROJECT]', '[SESSION]',
                                               '[ENTITY_TYPE]')

        # Mock response
        name_2 = 'name2-1052831874'
        expected_response = {'name': name_2}
        expected_response = session_entity_type_pb2.SessionEntityType(
            **expected_response)
        grpc_stub.GetSessionEntityType.return_value = expected_response

        response = client.get_session_entity_type(name)
        self.assertEqual(expected_response, response)

        grpc_stub.GetSessionEntityType.assert_called_once()
        args, kwargs = grpc_stub.GetSessionEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = session_entity_type_pb2.GetSessionEntityTypeRequest(
            name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_session_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionEntityTypesClient()

        # Mock request
        name = client.session_entity_type_path('[PROJECT]', '[SESSION]',
                                               '[ENTITY_TYPE]')

        # Mock exception response
        grpc_stub.GetSessionEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.get_session_entity_type,
                          name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_session_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionEntityTypesClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[SESSION]')
        session_entity_type = {}

        # Mock response
        name = 'name3373707'
        expected_response = {'name': name}
        expected_response = session_entity_type_pb2.SessionEntityType(
            **expected_response)
        grpc_stub.CreateSessionEntityType.return_value = expected_response

        response = client.create_session_entity_type(parent,
                                                     session_entity_type)
        self.assertEqual(expected_response, response)

        grpc_stub.CreateSessionEntityType.assert_called_once()
        args, kwargs = grpc_stub.CreateSessionEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = session_entity_type_pb2.CreateSessionEntityTypeRequest(
            parent=parent, session_entity_type=session_entity_type)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_session_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionEntityTypesClient()

        # Mock request
        parent = client.session_path('[PROJECT]', '[SESSION]')
        session_entity_type = {}

        # Mock exception response
        grpc_stub.CreateSessionEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.create_session_entity_type,
                          parent, session_entity_type)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_session_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionEntityTypesClient()

        # Mock request
        session_entity_type = {}

        # Mock response
        name = 'name3373707'
        expected_response = {'name': name}
        expected_response = session_entity_type_pb2.SessionEntityType(
            **expected_response)
        grpc_stub.UpdateSessionEntityType.return_value = expected_response

        response = client.update_session_entity_type(session_entity_type)
        self.assertEqual(expected_response, response)

        grpc_stub.UpdateSessionEntityType.assert_called_once()
        args, kwargs = grpc_stub.UpdateSessionEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = session_entity_type_pb2.UpdateSessionEntityTypeRequest(
            session_entity_type=session_entity_type)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_session_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionEntityTypesClient()

        # Mock request
        session_entity_type = {}

        # Mock exception response
        grpc_stub.UpdateSessionEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.update_session_entity_type,
                          session_entity_type)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_session_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionEntityTypesClient()

        # Mock request
        name = client.session_entity_type_path('[PROJECT]', '[SESSION]',
                                               '[ENTITY_TYPE]')

        client.delete_session_entity_type(name)

        grpc_stub.DeleteSessionEntityType.assert_called_once()
        args, kwargs = grpc_stub.DeleteSessionEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = session_entity_type_pb2.DeleteSessionEntityTypeRequest(
            name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_session_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionEntityTypesClient()

        # Mock request
        name = client.session_entity_type_path('[PROJECT]', '[SESSION]',
                                               '[ENTITY_TYPE]')

        # Mock exception response
        grpc_stub.DeleteSessionEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.delete_session_entity_type,
                          name)
