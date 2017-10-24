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
from google.cloud.dialogflow_v2beta1.proto import entity_type_pb2
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2


class CustomException(Exception):
    pass


class TestEntityTypesClient(unittest.TestCase):
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_entity_types(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')

        # Mock response
        next_page_token = ''
        entity_types_element = {}
        entity_types = [entity_types_element]
        expected_response = {
            'next_page_token': next_page_token,
            'entity_types': entity_types
        }
        expected_response = entity_type_pb2.ListEntityTypesResponse(
            **expected_response)
        grpc_stub.ListEntityTypes.return_value = expected_response

        paged_list_response = client.list_entity_types(parent)
        resources = list(paged_list_response)
        self.assertEqual(1, len(resources))
        self.assertEqual(expected_response.entity_types[0], resources[0])

        grpc_stub.ListEntityTypes.assert_called_once()
        args, kwargs = grpc_stub.ListEntityTypes.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.ListEntityTypesRequest(
            parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_list_entity_types_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')

        # Mock exception response
        grpc_stub.ListEntityTypes.side_effect = CustomException()

        paged_list_response = client.list_entity_types(parent)
        self.assertRaises(errors.GaxError, list, paged_list_response)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        name = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')

        # Mock response
        name_2 = 'name2-1052831874'
        display_name = 'displayName1615086568'
        expected_response = {'name': name_2, 'display_name': display_name}
        expected_response = entity_type_pb2.EntityType(**expected_response)
        grpc_stub.GetEntityType.return_value = expected_response

        response = client.get_entity_type(name)
        self.assertEqual(expected_response, response)

        grpc_stub.GetEntityType.assert_called_once()
        args, kwargs = grpc_stub.GetEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.GetEntityTypeRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_get_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        name = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')

        # Mock exception response
        grpc_stub.GetEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.get_entity_type, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')
        entity_type = {}

        # Mock response
        name = 'name3373707'
        display_name = 'displayName1615086568'
        expected_response = {'name': name, 'display_name': display_name}
        expected_response = entity_type_pb2.EntityType(**expected_response)
        grpc_stub.CreateEntityType.return_value = expected_response

        response = client.create_entity_type(parent, entity_type)
        self.assertEqual(expected_response, response)

        grpc_stub.CreateEntityType.assert_called_once()
        args, kwargs = grpc_stub.CreateEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.CreateEntityTypeRequest(
            parent=parent, entity_type=entity_type)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_create_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')
        entity_type = {}

        # Mock exception response
        grpc_stub.CreateEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.create_entity_type, parent,
                          entity_type)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        entity_type = {}

        # Mock response
        name = 'name3373707'
        display_name = 'displayName1615086568'
        expected_response = {'name': name, 'display_name': display_name}
        expected_response = entity_type_pb2.EntityType(**expected_response)
        grpc_stub.UpdateEntityType.return_value = expected_response

        response = client.update_entity_type(entity_type)
        self.assertEqual(expected_response, response)

        grpc_stub.UpdateEntityType.assert_called_once()
        args, kwargs = grpc_stub.UpdateEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.UpdateEntityTypeRequest(
            entity_type=entity_type)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_update_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        entity_type = {}

        # Mock exception response
        grpc_stub.UpdateEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.update_entity_type,
                          entity_type)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_entity_type(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        name = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')

        client.delete_entity_type(name)

        grpc_stub.DeleteEntityType.assert_called_once()
        args, kwargs = grpc_stub.DeleteEntityType.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.DeleteEntityTypeRequest(name=name)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_delete_entity_type_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        name = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')

        # Mock exception response
        grpc_stub.DeleteEntityType.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.delete_entity_type, name)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_update_entity_types(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')

        # Mock response
        expected_response = {}
        expected_response = entity_type_pb2.BatchUpdateEntityTypesResponse(
            **expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_batch_update_entity_types', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.BatchUpdateEntityTypes.return_value = operation

        response = client.batch_update_entity_types(parent)
        self.assertEqual(expected_response, response.result())

        grpc_stub.BatchUpdateEntityTypes.assert_called_once()
        args, kwargs = grpc_stub.BatchUpdateEntityTypes.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.BatchUpdateEntityTypesRequest(
            parent=parent)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_update_entity_types_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_batch_update_entity_types_exception',
            done=True)
        operation.error.CopyFrom(error)
        grpc_stub.BatchUpdateEntityTypes.return_value = operation

        response = client.batch_update_entity_types(parent)
        self.assertEqual(error, response.exception())

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_delete_entity_types(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')
        entity_type_names = []

        # Mock response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_batch_delete_entity_types', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.BatchDeleteEntityTypes.return_value = operation

        response = client.batch_delete_entity_types(parent, entity_type_names)
        self.assertEqual(expected_response, response.result())

        grpc_stub.BatchDeleteEntityTypes.assert_called_once()
        args, kwargs = grpc_stub.BatchDeleteEntityTypes.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.BatchDeleteEntityTypesRequest(
            parent=parent, entity_type_names=entity_type_names)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_delete_entity_types_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.project_agent_path('[PROJECT]')
        entity_type_names = []

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_batch_delete_entity_types_exception',
            done=True)
        operation.error.CopyFrom(error)
        grpc_stub.BatchDeleteEntityTypes.return_value = operation

        response = client.batch_delete_entity_types(parent, entity_type_names)
        self.assertEqual(error, response.exception())

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_create_entities(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
        entities = []

        # Mock response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_batch_create_entities', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.BatchCreateEntities.return_value = operation

        response = client.batch_create_entities(parent, entities)
        self.assertEqual(expected_response, response.result())

        grpc_stub.BatchCreateEntities.assert_called_once()
        args, kwargs = grpc_stub.BatchCreateEntities.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.BatchCreateEntitiesRequest(
            parent=parent, entities=entities)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_create_entities_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
        entities = []

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_batch_create_entities_exception', done=True)
        operation.error.CopyFrom(error)
        grpc_stub.BatchCreateEntities.return_value = operation

        response = client.batch_create_entities(parent, entities)
        self.assertEqual(error, response.exception())

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_update_entities(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
        entities = []

        # Mock response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_batch_update_entities', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.BatchUpdateEntities.return_value = operation

        response = client.batch_update_entities(parent, entities)
        self.assertEqual(expected_response, response.result())

        grpc_stub.BatchUpdateEntities.assert_called_once()
        args, kwargs = grpc_stub.BatchUpdateEntities.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.BatchUpdateEntitiesRequest(
            parent=parent, entities=entities)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_update_entities_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
        entities = []

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_batch_update_entities_exception', done=True)
        operation.error.CopyFrom(error)
        grpc_stub.BatchUpdateEntities.return_value = operation

        response = client.batch_update_entities(parent, entities)
        self.assertEqual(error, response.exception())

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_delete_entities(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
        entity_values = []

        # Mock response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name='operations/test_batch_delete_entities', done=True)
        operation.response.Pack(expected_response)
        grpc_stub.BatchDeleteEntities.return_value = operation

        response = client.batch_delete_entities(parent, entity_values)
        self.assertEqual(expected_response, response.result())

        grpc_stub.BatchDeleteEntities.assert_called_once()
        args, kwargs = grpc_stub.BatchDeleteEntities.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = entity_type_pb2.BatchDeleteEntitiesRequest(
            parent=parent, entity_values=entity_values)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_batch_delete_entities_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.EntityTypesClient()

        # Mock request
        parent = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
        entity_values = []

        # Mock exception response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name='operations/test_batch_delete_entities_exception', done=True)
        operation.error.CopyFrom(error)
        grpc_stub.BatchDeleteEntities.return_value = operation

        response = client.batch_delete_entities(parent, entity_values)
        self.assertEqual(error, response.exception())
