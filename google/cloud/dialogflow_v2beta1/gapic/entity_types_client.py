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
# https://github.com/google/googleapis/blob/master/google/cloud/dialogflow/v2beta1/entity_type.proto,
# and updates to that file get reflected here through a refresh process.
# For the short term, the refresh process will only be runnable by Google engineers.
#
# The only allowed edits are to method and file documentation. A 3-way
# merge preserves those additions if the generated source changes.
"""Accesses the google.cloud.dialogflow.v2beta1 EntityTypes API."""

import collections
import json
import os
import pkg_resources
import platform

from google.gapic.longrunning import operations_client
from google.gax import api_callable
from google.gax import config
from google.gax import path_template
from google.gax.utils import oneof
import google.gax

from google.cloud.dialogflow_v2beta1.gapic import entity_types_client_config
from google.cloud.dialogflow_v2beta1.gapic import enums
from google.cloud.dialogflow_v2beta1.proto import agent_pb2
from google.cloud.dialogflow_v2beta1.proto import context_pb2
from google.cloud.dialogflow_v2beta1.proto import entity_type_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import struct_pb2

_PageDesc = google.gax.PageDescriptor


class EntityTypesClient(object):
    """
    Manages agent entity types.


    Refer to `documentation <https://api.ai/docs/entities>`_ for more details about
    # entity types.

    Standard methods.
    """

    SERVICE_ADDRESS = 'dialogflow.googleapis.com'
    """The default address of the service."""

    DEFAULT_SERVICE_PORT = 443
    """The default port of the service."""

    _PAGE_DESCRIPTORS = {
        'list_entity_types':
        _PageDesc('page_token', 'next_page_token', 'entity_types')
    }

    # The scopes needed to make gRPC calls to all of the methods defined in
    # this service
    _ALL_SCOPES = ('https://www.googleapis.com/auth/cloud-platform', )

    _PROJECT_AGENT_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agent')
    _ENTITY_TYPE_PATH_TEMPLATE = path_template.PathTemplate(
        'projects/{project}/agent/entityTypes/{entity_type}')

    @classmethod
    def project_agent_path(cls, project):
        """Returns a fully-qualified project_agent resource name string."""
        return cls._PROJECT_AGENT_PATH_TEMPLATE.render({
            'project': project,
        })

    @classmethod
    def entity_type_path(cls, project, entity_type):
        """Returns a fully-qualified entity_type resource name string."""
        return cls._ENTITY_TYPE_PATH_TEMPLATE.render({
            'project':
            project,
            'entity_type':
            entity_type,
        })

    @classmethod
    def match_project_from_project_agent_name(cls, project_agent_name):
        """Parses the project from a project_agent resource.

        Args:
            project_agent_name (str): A fully-qualified path representing a project_agent
                resource.

        Returns:
            A string representing the project.
        """
        return cls._PROJECT_AGENT_PATH_TEMPLATE.match(project_agent_name).get(
            'project')

    @classmethod
    def match_project_from_entity_type_name(cls, entity_type_name):
        """Parses the project from a entity_type resource.

        Args:
            entity_type_name (str): A fully-qualified path representing a entity_type
                resource.

        Returns:
            A string representing the project.
        """
        return cls._ENTITY_TYPE_PATH_TEMPLATE.match(entity_type_name).get(
            'project')

    @classmethod
    def match_entity_type_from_entity_type_name(cls, entity_type_name):
        """Parses the entity_type from a entity_type resource.

        Args:
            entity_type_name (str): A fully-qualified path representing a entity_type
                resource.

        Returns:
            A string representing the entity_type.
        """
        return cls._ENTITY_TYPE_PATH_TEMPLATE.match(entity_type_name).get(
            'entity_type')

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
            'google.cloud.dialogflow.v2beta1.EntityTypes',
            entity_types_client_config.config,
            client_config,
            config.STATUS_CODE_NAMES,
            metrics_headers=metrics_headers,
            page_descriptors=self._PAGE_DESCRIPTORS, )
        self.entity_types_stub = config.create_stub(
            entity_type_pb2.EntityTypesStub,
            channel=channel,
            service_path=self.SERVICE_ADDRESS,
            service_port=self.DEFAULT_SERVICE_PORT,
            credentials=credentials,
            scopes=scopes,
            ssl_credentials=ssl_credentials)

        self.operations_client = operations_client.OperationsClient(
            service_path=self.SERVICE_ADDRESS,
            channel=channel,
            credentials=credentials,
            ssl_credentials=ssl_credentials,
            scopes=scopes,
            client_config=client_config,
            metrics_headers=metrics_headers, )

        self._list_entity_types = api_callable.create_api_call(
            self.entity_types_stub.ListEntityTypes,
            settings=defaults['list_entity_types'])
        self._get_entity_type = api_callable.create_api_call(
            self.entity_types_stub.GetEntityType,
            settings=defaults['get_entity_type'])
        self._create_entity_type = api_callable.create_api_call(
            self.entity_types_stub.CreateEntityType,
            settings=defaults['create_entity_type'])
        self._update_entity_type = api_callable.create_api_call(
            self.entity_types_stub.UpdateEntityType,
            settings=defaults['update_entity_type'])
        self._delete_entity_type = api_callable.create_api_call(
            self.entity_types_stub.DeleteEntityType,
            settings=defaults['delete_entity_type'])
        self._batch_update_entity_types = api_callable.create_api_call(
            self.entity_types_stub.BatchUpdateEntityTypes,
            settings=defaults['batch_update_entity_types'])
        self._batch_delete_entity_types = api_callable.create_api_call(
            self.entity_types_stub.BatchDeleteEntityTypes,
            settings=defaults['batch_delete_entity_types'])
        self._batch_create_entities = api_callable.create_api_call(
            self.entity_types_stub.BatchCreateEntities,
            settings=defaults['batch_create_entities'])
        self._batch_update_entities = api_callable.create_api_call(
            self.entity_types_stub.BatchUpdateEntities,
            settings=defaults['batch_update_entities'])
        self._batch_delete_entities = api_callable.create_api_call(
            self.entity_types_stub.BatchDeleteEntities,
            settings=defaults['batch_delete_entities'])

    # Service calls
    def list_entity_types(self,
                          parent,
                          language_code=None,
                          page_size=None,
                          options=None):
        """
        Returns the list of all entity types in the specified agent.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>> from google.gax import CallOptions, INITIAL_PAGE
            >>>
            >>> client = dialogflow_v2beta1.EntityTypesClient()
            >>>
            >>> parent = client.project_agent_path('[PROJECT]')
            >>>
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_entity_types(parent):
            ...     # process element
            ...     pass
            >>>
            >>> # Or iterate over results one page at a time
            >>> for page in client.list_entity_types(parent, options=CallOptions(page_token=INITIAL_PAGE)):
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The agent to list all entity types from.
                Format: ``projects/<Project ID>/agent``.
            language_code (str): Optional. The language to list entity synonyms for. If not specified,
                the agent's default language is used.
                `More than a dozen languages <https://api.ai/docs/reference/language>`_
                are supported.
                Note: languages must be enabled in the agent, before they can be used.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.gax.PageIterator` instance. By default, this
            is an iterable of :class:`~google.cloud.dialogflow_v2beta1.types.EntityType` instances.
            This object can also be configured to iterate over the pages
            of the response through the `options` parameter.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = entity_type_pb2.ListEntityTypesRequest(
            parent=parent, language_code=language_code, page_size=page_size)
        return self._list_entity_types(request, options)

    def get_entity_type(self, name, language_code=None, options=None):
        """
        Retrieves the specified entity type.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.EntityTypesClient()
            >>>
            >>> name = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
            >>>
            >>> response = client.get_entity_type(name)

        Args:
            name (str): Required. The name of the entity type.
                Format: ``projects/<Project ID>/agent/entityTypes/<EntityType ID>``.
            language_code (str): Optional. The language to retrieve entity synonyms for. If not specified,
                the agent's default language is used.
                `More than a dozen languages <https://api.ai/docs/reference/language>`_
                are supported.
                Note: languages must be enabled in the agent, before they can be used.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types.EntityType` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = entity_type_pb2.GetEntityTypeRequest(
            name=name, language_code=language_code)
        return self._get_entity_type(request, options)

    def create_entity_type(self,
                           parent,
                           entity_type,
                           language_code=None,
                           options=None):
        """
        Creates an entity type in the specified agent.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.EntityTypesClient()
            >>>
            >>> parent = client.project_agent_path('[PROJECT]')
            >>> entity_type = {}
            >>>
            >>> response = client.create_entity_type(parent, entity_type)

        Args:
            parent (str): Required. The agent to create a entity type for.
                Format: ``projects/<Project ID>/agent``.
            entity_type (Union[dict, ~google.cloud.dialogflow_v2beta1.types.EntityType]): Required. The entity type to create.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.EntityType`
            language_code (str): Optional. The language of entity synonyms defined in ``entity_type``. If not
                specified, the agent's default language is used.
                `More than a dozen languages <https://api.ai/docs/reference/language>`_
                are supported.
                Note: languages must be enabled in the agent, before they can be used.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types.EntityType` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = entity_type_pb2.CreateEntityTypeRequest(
            parent=parent,
            entity_type=entity_type,
            language_code=language_code)
        return self._create_entity_type(request, options)

    def update_entity_type(self,
                           entity_type,
                           language_code=None,
                           update_mask=None,
                           options=None):
        """
        Updates the specified entity type.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.EntityTypesClient()
            >>>
            >>> entity_type = {}
            >>>
            >>> response = client.update_entity_type(entity_type)

        Args:
            entity_type (Union[dict, ~google.cloud.dialogflow_v2beta1.types.EntityType]): Required. The entity type to update.
                Format: ``projects/<Project ID>/agent/entityTypes/<EntityType ID>``.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.EntityType`
            language_code (str): Optional. The language of entity synonyms defined in ``entity_type``. If not
                specified, the agent's default language is used.
                `More than a dozen languages <https://api.ai/docs/reference/language>`_
                are supported.
                Note: languages must be enabled in the agent, before they can be used.
            update_mask (Union[dict, ~google.cloud.dialogflow_v2beta1.types.FieldMask]): Optional. The mask to control which fields get updated.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.FieldMask`
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types.EntityType` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = entity_type_pb2.UpdateEntityTypeRequest(
            entity_type=entity_type,
            language_code=language_code,
            update_mask=update_mask)
        return self._update_entity_type(request, options)

    def delete_entity_type(self, name, options=None):
        """
        Deletes the specified entity type.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.EntityTypesClient()
            >>>
            >>> name = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
            >>>
            >>> client.delete_entity_type(name)

        Args:
            name (str): Required. The name of the entity type to delete.
                Format: ``projects/<Project ID>/agent/entityTypes/<EntityType ID>``.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = entity_type_pb2.DeleteEntityTypeRequest(name=name)
        self._delete_entity_type(request, options)

    def batch_update_entity_types(self,
                                  parent,
                                  entity_type_batch_uri=None,
                                  entity_type_batch_inline=None,
                                  language_code=None,
                                  update_mask=None,
                                  options=None):
        """
        Updates/Creates multiple entity types in the specified agent.

        Operation<response: BatchUpdateEntityTypesResponse>

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.EntityTypesClient()
            >>>
            >>> parent = client.project_agent_path('[PROJECT]')
            >>>
            >>> response = client.batch_update_entity_types(parent)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            parent (str): Required. The name of the agent to update or create entity types in.
                Format: ``projects/<Project ID>/agents/<Agent ID>``.
            entity_type_batch_uri (str): The URI to a file containing entity types to update or create. The file
                format can be either a serialized proto (of EntityBatch type) or a JSON
                object. Note: The URI must start with \"gs://\".
            entity_type_batch_inline (Union[dict, ~google.cloud.dialogflow_v2beta1.types.EntityTypeBatch]): The collection of entity type to update or create.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.EntityTypeBatch`
            language_code (str): Optional. The language of entity synonyms defined in ``entity_types``. If not
                specified, the agent's default language is used.
                `More than a dozen languages <https://api.ai/docs/reference/language>`_
                are supported.
                Note: languages must be enabled in the agent, before they can be used.
            update_mask (Union[dict, ~google.cloud.dialogflow_v2beta1.types.FieldMask]): Optional. The mask to control which fields get updated.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.FieldMask`
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types._OperationFuture` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        oneof.check_oneof(
            entity_type_batch_uri=entity_type_batch_uri,
            entity_type_batch_inline=entity_type_batch_inline, )

        request = entity_type_pb2.BatchUpdateEntityTypesRequest(
            parent=parent,
            entity_type_batch_uri=entity_type_batch_uri,
            entity_type_batch_inline=entity_type_batch_inline,
            language_code=language_code,
            update_mask=update_mask)
        return google.gax._OperationFuture(
            self._batch_update_entity_types(request,
                                            options), self.operations_client,
            entity_type_pb2.BatchUpdateEntityTypesResponse, struct_pb2.Struct,
            options)

    def batch_delete_entity_types(self,
                                  parent,
                                  entity_type_names,
                                  options=None):
        """
        Deletes entity types in the specified agent.

        Operation<response: google.protobuf.Empty>

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.EntityTypesClient()
            >>>
            >>> parent = client.project_agent_path('[PROJECT]')
            >>> entity_type_names = []
            >>>
            >>> response = client.batch_delete_entity_types(parent, entity_type_names)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            parent (str): Required. The name of the agent to delete all entities types for. Format:
                ``projects/<Project ID>/agent``.
            entity_type_names (list[str]): Required. The names entity types to delete. All names must point to the
                same agent as ``parent``.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types._OperationFuture` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = entity_type_pb2.BatchDeleteEntityTypesRequest(
            parent=parent, entity_type_names=entity_type_names)
        return google.gax._OperationFuture(
            self._batch_delete_entity_types(request,
                                            options), self.operations_client,
            empty_pb2.Empty, struct_pb2.Struct, options)

    def batch_create_entities(self,
                              parent,
                              entities,
                              language_code=None,
                              options=None):
        """
        Creates multiple new entities in the specified entity type (extends the
        existing collection of entries).

        Operation<response: google.protobuf.Empty>

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.EntityTypesClient()
            >>>
            >>> parent = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
            >>> entities = []
            >>>
            >>> response = client.batch_create_entities(parent, entities)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            parent (str): Required. The name of the entity type to create entities in. Format:
                ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``.
            entities (list[Union[dict, ~google.cloud.dialogflow_v2beta1.types.Entity]]): Required. The collection of entities to create.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.Entity`
            language_code (str): Optional. The language of entity synonyms defined in ``entities``. If not
                specified, the agent's default language is used.
                `More than a dozen languages <https://api.ai/docs/reference/language>`_
                are supported.
                Note: languages must be enabled in the agent, before they can be used.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types._OperationFuture` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = entity_type_pb2.BatchCreateEntitiesRequest(
            parent=parent, entities=entities, language_code=language_code)
        return google.gax._OperationFuture(
            self._batch_create_entities(request,
                                        options), self.operations_client,
            empty_pb2.Empty, struct_pb2.Struct, options)

    def batch_update_entities(self,
                              parent,
                              entities,
                              language_code=None,
                              update_mask=None,
                              options=None):
        """
        Updates entities in the specified entity type (replaces the existing
        collection of entries).

        Operation<response: google.protobuf.Empty>

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.EntityTypesClient()
            >>>
            >>> parent = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
            >>> entities = []
            >>>
            >>> response = client.batch_update_entities(parent, entities)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            parent (str): Required. The name of the entity type to update the entities in. Format:
                ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``.
            entities (list[Union[dict, ~google.cloud.dialogflow_v2beta1.types.Entity]]): Required. The collection of new entities to replace the existing entities.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.Entity`
            language_code (str): Optional. The language of entity synonyms defined in ``entities``. If not
                specified, the agent's default language is used.
                `More than a dozen languages <https://api.ai/docs/reference/language>`_
                are supported.
                Note: languages must be enabled in the agent, before they can be used.
            update_mask (Union[dict, ~google.cloud.dialogflow_v2beta1.types.FieldMask]): Optional. The mask to control which fields get updated.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.dialogflow_v2beta1.types.FieldMask`
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types._OperationFuture` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = entity_type_pb2.BatchUpdateEntitiesRequest(
            parent=parent,
            entities=entities,
            language_code=language_code,
            update_mask=update_mask)
        return google.gax._OperationFuture(
            self._batch_update_entities(request,
                                        options), self.operations_client,
            empty_pb2.Empty, struct_pb2.Struct, options)

    def batch_delete_entities(self,
                              parent,
                              entity_values,
                              language_code=None,
                              options=None):
        """
        Deletes entities in the specified entity type.

        Operation<response: google.protobuf.Empty>

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.EntityTypesClient()
            >>>
            >>> parent = client.entity_type_path('[PROJECT]', '[ENTITY_TYPE]')
            >>> entity_values = []
            >>>
            >>> response = client.batch_delete_entities(parent, entity_values)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            parent (str): Required. The name of the entity type to delete entries for. Format:
                ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``.
            entity_values (list[str]): Required. The canonical ``values`` of the entities to delete. Note that
                these are not fully-qualified names, i.e. they don't start with
                ``projects/<Project ID>``.
            language_code (str): Optional. The language of entity synonyms defined in ``entities``. If not
                specified, the agent's default language is used.
                `More than a dozen languages <https://api.ai/docs/reference/language>`_
                are supported.
                Note: languages must be enabled in the agent, before they can be used.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types._OperationFuture` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = entity_type_pb2.BatchDeleteEntitiesRequest(
            parent=parent,
            entity_values=entity_values,
            language_code=language_code)
        return google.gax._OperationFuture(
            self._batch_delete_entities(request,
                                        options), self.operations_client,
            empty_pb2.Empty, struct_pb2.Struct, options)
