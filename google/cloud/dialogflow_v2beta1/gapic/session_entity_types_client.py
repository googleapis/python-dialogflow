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
# https://github.com/google/googleapis/blob/master/google/cloud/dialogflow/v2beta1/session_entity_type.proto,
# and updates to that file get reflected here through a refresh process.
# For the short term, the refresh process will only be runnable by Google engineers.
#
# The only allowed edits are to method and file documentation. A 3-way
# merge preserves those additions if the generated source changes.
"""Accesses the google.cloud.dialogflow.v2beta1 SessionEntityTypes API."""

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
from google.cloud.dialogflow_v2beta1.gapic import session_entity_types_client_config
from google.cloud.dialogflow_v2beta1.proto import agent_pb2
from google.cloud.dialogflow_v2beta1.proto import context_pb2
from google.cloud.dialogflow_v2beta1.proto import entity_type_pb2
from google.cloud.dialogflow_v2beta1.proto import intent_pb2
from google.cloud.dialogflow_v2beta1.proto import session_entity_type_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import struct_pb2

_PageDesc = google.gax.PageDescriptor


class SessionEntityTypesClient(object):
    """
    Manages session entity types.

    Session entity types can be redefined on a session level, allowing for
    specific concepts, like a user's playlists.


    Standard methods.
    """

    SERVICE_ADDRESS = 'dialogflow.googleapis.com'
    """The default address of the service."""

    DEFAULT_SERVICE_PORT = 443
    """The default port of the service."""

    _PAGE_DESCRIPTORS = {
        'list_session_entity_types':
        _PageDesc('page_token', 'next_page_token', 'session_entity_types')
    }

    # The scopes needed to make gRPC calls to all of the methods defined in
    # this service
    _ALL_SCOPES = ('https://www.googleapis.com/auth/cloud-platform', )

    _SESSION_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agent/sessions/{session}')
    _SESSION_ENTITY_TYPE_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agent/sessions/{session}/entityTypes/{entity_type}'
    )

    @classmethod
    def session_path(cls, project, session):
        """Returns a fully-qualified session resource name string."""
        return cls._SESSION_PATH_TEMPLATE.render({
            'project': project,
            'session': session,
        })

    @classmethod
    def session_entity_type_path(cls, project, session, entity_type):
        """Returns a fully-qualified session_entity_type resource name string."""
        return cls._SESSION_ENTITY_TYPE_PATH_TEMPLATE.render({
            'project':
            project,
            'session':
            session,
            'entity_type':
            entity_type,
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

    @classmethod
    def match_project_from_session_entity_type_name(cls,
                                                    session_entity_type_name):
        """Parses the project from a session_entity_type resource.

        Args:
            session_entity_type_name (str): A fully-qualified path representing a session_entity_type
                resource.

        Returns:
            A string representing the project.
        """
        return cls._SESSION_ENTITY_TYPE_PATH_TEMPLATE.match(
            session_entity_type_name).get('project')

    @classmethod
    def match_session_from_session_entity_type_name(cls,
                                                    session_entity_type_name):
        """Parses the session from a session_entity_type resource.

        Args:
            session_entity_type_name (str): A fully-qualified path representing a session_entity_type
                resource.

        Returns:
            A string representing the session.
        """
        return cls._SESSION_ENTITY_TYPE_PATH_TEMPLATE.match(
            session_entity_type_name).get('session')

    @classmethod
    def match_entity_type_from_session_entity_type_name(
            cls, session_entity_type_name):
        """Parses the entity_type from a session_entity_type resource.

        Args:
            session_entity_type_name (str): A fully-qualified path representing a session_entity_type
                resource.

        Returns:
            A string representing the entity_type.
        """
        return cls._SESSION_ENTITY_TYPE_PATH_TEMPLATE.match(
            session_entity_type_name).get('entity_type')

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
            'google.cloud.dialogflow.v2beta1.SessionEntityTypes',
            session_entity_types_client_config.config,
            client_config,
            config.STATUS_CODE_NAMES,
            metrics_headers=metrics_headers,
            page_descriptors=self._PAGE_DESCRIPTORS, )
        self.session_entity_types_stub = config.create_stub(
            session_entity_type_pb2.SessionEntityTypesStub,
            channel=channel,
            service_path=self.SERVICE_ADDRESS,
            service_port=self.DEFAULT_SERVICE_PORT,
            credentials=credentials,
            scopes=scopes,
            ssl_credentials=ssl_credentials)

        self._list_session_entity_types = api_callable.create_api_call(
            self.session_entity_types_stub.ListSessionEntityTypes,
            settings=defaults['list_session_entity_types'])
        self._get_session_entity_type = api_callable.create_api_call(
            self.session_entity_types_stub.GetSessionEntityType,
            settings=defaults['get_session_entity_type'])
        self._create_session_entity_type = api_callable.create_api_call(
            self.session_entity_types_stub.CreateSessionEntityType,
            settings=defaults['create_session_entity_type'])
        self._update_session_entity_type = api_callable.create_api_call(
            self.session_entity_types_stub.UpdateSessionEntityType,
            settings=defaults['update_session_entity_type'])
        self._delete_session_entity_type = api_callable.create_api_call(
            self.session_entity_types_stub.DeleteSessionEntityType,
            settings=defaults['delete_session_entity_type'])

    # Service calls
    def list_session_entity_types(self, parent, page_size=None, options=None):
        """
        Returns the list of all session entity types in the specified session.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>> from google.gax import CallOptions, INITIAL_PAGE
            >>>
            >>> client = dialogflow_v2beta1.SessionEntityTypesClient()
            >>>
            >>> parent = client.session_path('[PROJECT]', '[SESSION]')
            >>>
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_session_entity_types(parent):
            ...     # process element
            ...     pass
            >>>
            >>> # Or iterate over results one page at a time
            >>> for page in client.list_session_entity_types(parent, options=CallOptions(page_token=INITIAL_PAGE)):
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The session to list all session entity types from.
                Format: ``projects/<Project ID>/agent/sessions/<Session ID>``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.gax.PageIterator` instance. By default, this
            is an iterable of :class:`~google.cloud.dialogflow_v2beta1.types.SessionEntityType` instances.
            This object can also be configured to iterate over the pages
            of the response through the `options` parameter.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = session_entity_type_pb2.ListSessionEntityTypesRequest(
            parent=parent, page_size=page_size)
        return self._list_session_entity_types(request, options)

    def get_session_entity_type(self, name, options=None):
        """
        Retrieves the specified session entity type.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.SessionEntityTypesClient()
            >>>
            >>> name = client.session_entity_type_path('[PROJECT]', '[SESSION]', '[ENTITY_TYPE]')
            >>>
            >>> response = client.get_session_entity_type(name)

        Args:
            name (str): Required. The name of the session entity type. Format:
                ``projects/<Project ID>/agent/sessions/<Session ID>/entityTypes/<Session
                Entity Type ID>``.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types.SessionEntityType` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = session_entity_type_pb2.GetSessionEntityTypeRequest(
            name=name)
        return self._get_session_entity_type(request, options)

    def create_session_entity_type(self,
                                   parent,
                                   session_entity_type,
                                   options=None):
        """
        Creates a session entity type.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.SessionEntityTypesClient()
            >>>
            >>> parent = client.session_path('[PROJECT]', '[SESSION]')
            >>> session_entity_type = {}
            >>>
            >>> response = client.create_session_entity_type(parent, session_entity_type)

        Args:
            parent (str): Required. The session to create a session entity type for.
                Format: ``projects/<Project ID>/agent/sessions/<Session ID>``.
            session_entity_type (Union[dict, ~google.cloud.dialogflow_v2beta1.types.SessionEntityType]): Required. The session entity type to create.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.SessionEntityType`
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types.SessionEntityType` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = session_entity_type_pb2.CreateSessionEntityTypeRequest(
            parent=parent, session_entity_type=session_entity_type)
        return self._create_session_entity_type(request, options)

    def update_session_entity_type(self,
                                   session_entity_type,
                                   update_mask=None,
                                   options=None):
        """
        Updates the specified session entity type.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.SessionEntityTypesClient()
            >>>
            >>> session_entity_type = {}
            >>>
            >>> response = client.update_session_entity_type(session_entity_type)

        Args:
            session_entity_type (Union[dict, ~google.cloud.dialogflow_v2beta1.types.SessionEntityType]): Required. The entity type to update. Format:
                ``projects/<Project ID>/agent/sessions/<Session ID>/entityTypes/<Session
                Entity Type ID>``.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.SessionEntityType`
            update_mask (Union[dict, ~google.cloud.dialogflow_v2beta1.types.FieldMask]): Optional. The mask to control which fields get updated.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.FieldMask`
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types.SessionEntityType` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = session_entity_type_pb2.UpdateSessionEntityTypeRequest(
            session_entity_type=session_entity_type, update_mask=update_mask)
        return self._update_session_entity_type(request, options)

    def delete_session_entity_type(self, name, options=None):
        """
        Deletes the specified session entity type.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.SessionEntityTypesClient()
            >>>
            >>> name = client.session_entity_type_path('[PROJECT]', '[SESSION]', '[ENTITY_TYPE]')
            >>>
            >>> client.delete_session_entity_type(name)

        Args:
            name (str): Required. The name of the entity type to delete. Format:
                ``projects/<Project ID>/agent/sessions/<Session ID>/entityTypes/<Session
                Entity Type ID>``.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = session_entity_type_pb2.DeleteSessionEntityTypeRequest(
            name=name)
        self._delete_session_entity_type(request, options)
