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
from google.cloud.dialogflow_v2beta1.proto import session_pb2


class CustomException(Exception):
    pass


class TestSessionsClient(unittest.TestCase):
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_detect_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionsClient()

        # Mock request
        session = client.session_path('[PROJECT]', '[SESSION]')
        query_input = {}

        # Mock response
        response_id = 'responseId1847552473'
        expected_response = {'response_id': response_id}
        expected_response = session_pb2.DetectIntentResponse(
            **expected_response)
        grpc_stub.DetectIntent.return_value = expected_response

        response = client.detect_intent(session, query_input)
        self.assertEqual(expected_response, response)

        grpc_stub.DetectIntent.assert_called_once()
        args, kwargs = grpc_stub.DetectIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_request = args[0]

        expected_request = session_pb2.DetectIntentRequest(
            session=session, query_input=query_input)
        self.assertEqual(expected_request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_detect_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionsClient()

        # Mock request
        session = client.session_path('[PROJECT]', '[SESSION]')
        query_input = {}

        # Mock exception response
        grpc_stub.DetectIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.detect_intent, session,
                          query_input)

    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_streaming_detect_intent(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionsClient()

        # Mock request
        session = 'session1984987798'
        query_input = {}
        request = {'session': session, 'query_input': query_input}
        requests = [request]

        # Mock response
        response_id = 'responseId1847552473'
        expected_response = {'response_id': response_id}
        expected_response = session_pb2.StreamingDetectIntentResponse(
            **expected_response)
        grpc_stub.StreamingDetectIntent.return_value = iter(
            [expected_response])

        response = client.streaming_detect_intent(requests)
        resources = list(response)
        self.assertEqual(1, len(resources))
        self.assertEqual(expected_response, resources[0])

        grpc_stub.StreamingDetectIntent.assert_called_once()
        args, kwargs = grpc_stub.StreamingDetectIntent.call_args
        self.assertEqual(len(args), 2)
        self.assertEqual(len(kwargs), 1)
        self.assertIn('metadata', kwargs)
        actual_requests = args[0]
        self.assertEqual(1, len(actual_requests))
        actual_request = list(actual_requests)[0]
        self.assertEqual(request, actual_request)

    @mock.patch('google.gax.config.API_ERRORS', (CustomException, ))
    @mock.patch('google.gax.config.create_stub', spec=True)
    def test_streaming_detect_intent_exception(self, mock_create_stub):
        # Mock gRPC layer
        grpc_stub = mock.Mock()
        mock_create_stub.return_value = grpc_stub

        client = dialogflow_v2beta1.SessionsClient()

        # Mock request
        session = 'session1984987798'
        query_input = {}
        request = {'session': session, 'query_input': query_input}
        requests = [request]

        # Mock exception response
        grpc_stub.StreamingDetectIntent.side_effect = CustomException()

        self.assertRaises(errors.GaxError, client.streaming_detect_intent,
                          requests)
