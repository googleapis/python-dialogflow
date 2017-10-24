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
#
# EDITING INSTRUCTIONS
# This file was generated from the file
# https://github.com/google/googleapis/blob/master/google/cloud/dialogflow/v2beta1/session.proto,
# and updates to that file get reflected here through a refresh process.
# For the short term, the refresh process will only be runnable by Google engineers.
#
# The only allowed edits are to method and file documentation. A 3-way
# merge preserves those additions if the generated source changes.
"""Accesses the google.cloud.dialogflow.v2beta1 Sessions API."""

import collections
import json
import os
import pkg_resources
import platform

from google.gax import api_callable
from google.gax import config
from google.gax import path_template
import google.gax

from google.cloud.dialogflow_v2beta1.gapic import enums
from google.cloud.dialogflow_v2beta1.gapic import sessions_client_config
from google.cloud.dialogflow_v2beta1.proto import agent_pb2
from google.cloud.dialogflow_v2beta1.proto import context_pb2
from google.cloud.dialogflow_v2beta1.proto import entity_type_pb2
from google.cloud.dialogflow_v2beta1.proto import intent_pb2
from google.cloud.dialogflow_v2beta1.proto import session_entity_type_pb2
from google.cloud.dialogflow_v2beta1.proto import session_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import struct_pb2


class SessionsClient(object):
    """
    Manages user sessions.


    Custom methods.
    """

    SERVICE_ADDRESS = 'dialogflow.googleapis.com'
    """The default address of the service."""

    DEFAULT_SERVICE_PORT = 443
    """The default port of the service."""

    # The scopes needed to make gRPC calls to all of the methods defined in
    # this service
    _ALL_SCOPES = ('https://www.googleapis.com/auth/cloud-platform', )

    _SESSION_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agent/sessions/{session}')

    @classmethod
    def session_path(cls, project, session):
        """Returns a fully-qualified session resource name string."""
        return cls._SESSION_PATH_TEMPLATE.render({
            'project': project,
            'session': session,
        })

    @classmethod
    def match_project_from_session_name(cls, session_name):
        """Parses the project from a session resource.

        Args:
            session_name (str): A fully-qualified path representing a session
                resource.

        Returns:
            A string representing the project.
        """
        return cls._SESSION_PATH_TEMPLATE.match(session_name).get('project')

    @classmethod
    def match_session_from_session_name(cls, session_name):
        """Parses the session from a session resource.

        Args:
            session_name (str): A fully-qualified path representing a session
                resource.

        Returns:
            A string representing the session.
        """
        return cls._SESSION_PATH_TEMPLATE.match(session_name).get('session')

    def __init__(self,
                 channel=None,
                 credentials=None,
                 ssl_credentials=None,
                 scopes=None,
                 client_config=None,
                 lib_name=None,
                 lib_version='',
                 metrics_headers=()):
        """Constructor.

        Args:
            channel (~grpc.Channel): A ``Channel`` instance through
                which to make calls.
            credentials (~google.auth.credentials.Credentials): The authorization
                credentials to attach to requests. These credentials identify this
                application to the service.
            ssl_credentials (~grpc.ChannelCredentials): A
                ``ChannelCredentials`` instance for use with an SSL-enabled
                channel.
            scopes (Sequence[str]): A list of OAuth2 scopes to attach to requests.
            client_config (dict):
                A dictionary for call options for each method. See
                :func:`google.gax.construct_settings` for the structure of
                this data. Falls back to the default config if not specified
                or the specified config is missing data points.
            lib_name (str): The API library software used for calling
                the service. (Unless you are writing an API client itself,
                leave this as default.)
            lib_version (str): The API library software version used
                for calling the service. (Unless you are writing an API client
                itself, leave this as default.)
            metrics_headers (dict): A dictionary of values for tracking
                client library metrics. Ultimately serializes to a string
                (e.g. 'foo/1.2.3 bar/3.14.1'). This argument should be
                considered private.
        """
        # Unless the calling application specifically requested
        # OAuth scopes, request everything.
        if scopes is None:
            scopes = self._ALL_SCOPES

        # Initialize an empty client config, if none is set.
        if client_config is None:
            client_config = {}

        # Initialize metrics_headers as an ordered dictionary
        # (cuts down on cardinality of the resulting string slightly).
        metrics_headers = collections.OrderedDict(metrics_headers)
        metrics_headers['gl-python'] = platform.python_version()

        # The library may or may not be set, depending on what is
        # calling this client. Newer client libraries set the library name
        # and version.
        if lib_name:
            metrics_headers[lib_name] = lib_version

        # Finally, track the GAPIC package version.
        metrics_headers['gapic'] = pkg_resources.get_distribution(
            'google-cloud-dialogflow', ).version

        # Load the configuration defaults.
        defaults = api_callable.construct_settings(
            'google.cloud.dialogflow.v2beta1.Sessions',
            sessions_client_config.config,
            client_config,
            config.STATUS_CODE_NAMES,
            metrics_headers=metrics_headers, )
        self.sessions_stub = config.create_stub(
            session_pb2.SessionsStub,
            channel=channel,
            service_path=self.SERVICE_ADDRESS,
            service_port=self.DEFAULT_SERVICE_PORT,
            credentials=credentials,
            scopes=scopes,
            ssl_credentials=ssl_credentials)

        self._detect_intent = api_callable.create_api_call(
            self.sessions_stub.DetectIntent,
            settings=defaults['detect_intent'])
        self._streaming_detect_intent = api_callable.create_api_call(
            self.sessions_stub.StreamingDetectIntent,
            settings=defaults['streaming_detect_intent'])

    # Service calls
    def detect_intent(self,
                      session,
                      query_input,
                      query_params=None,
                      input_audio=None,
                      options=None):
        """
        Processes a natural language query and returns structured, actionable data
        as a result. This method is not idempotent, because it may cause contexts
        and session entity types to be updated, which in turn might affect
        results of future queries.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.SessionsClient()
            >>>
            >>> session = client.session_path('[PROJECT]', '[SESSION]')
            >>> query_input = {}
            >>>
            >>> response = client.detect_intent(session, query_input)

        Args:
            session (str): Required. The name of the session this query is sent to. Format:
                ``projects/<Project ID>/agent/sessions/<Session ID>``.
                It's up to the API caller to choose an appropriate session ID. It can be
                a random number or some type of user identifier (preferably hashed).
                The length of the session ID must not exceed 36 bytes.
            query_input (Union[dict, ~google.cloud.dialogflow_v2beta1.types.QueryInput]): Required. The input specification. It can be set to:

                1.  an audio config
                ::

                    which instructs the speech recognizer how to process the speech audio,

                2.  a conversational query in the form of text, or

                3.  an event that specifies which intent to trigger.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.QueryInput`
            query_params (Union[dict, ~google.cloud.dialogflow_v2beta1.types.QueryParameters]): Optional. The parameters of this query.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.QueryParameters`
            input_audio (bytes): Optional. The natural language speech audio to be processed. This field
                should be populated iff ``query_input`` is set to an input audio config.
                A single request can contain up to 1 minute of speech audio data.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types.DetectIntentResponse` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = session_pb2.DetectIntentRequest(
            session=session,
            query_input=query_input,
            query_params=query_params,
            input_audio=input_audio)
        return self._detect_intent(request, options)

    def streaming_detect_intent(self, requests, options=None):
        """
        Processes a natural language query in audio format in a streaming fashion
        and returns structured, actionable data as a result. This method is only
        available via the gRPC API (not REST).

        EXPERIMENTAL: This method interface might change in the future.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.SessionsClient()
            >>>
            >>> session = ''
            >>> query_input = {}
            >>> request = {'session': session, 'query_input': query_input}
            >>>
            >>> requests = [request]
            >>> for element in client.streaming_detect_intent(requests):
            ...     # process element
            ...     pass

        Args:
            requests (iterator[dict|google.cloud.dialogflow_v2beta1.proto.session_pb2.StreamingDetectIntentRequest]): The input objects. If a dict is provided, it must be of the
                same form as the protobuf message :class:`~google.cloud.dialogflow_v2beta1.types.StreamingDetectIntentRequest`
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            Iterable[~google.cloud.dialogflow_v2beta1.types.StreamingDetectIntentResponse].

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        return self._streaming_detect_intent(requests, options)
