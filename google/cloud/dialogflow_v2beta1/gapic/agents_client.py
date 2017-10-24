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
# https://github.com/google/googleapis/blob/master/google/cloud/dialogflow/v2beta1/agent.proto,
# and updates to that file get reflected here through a refresh process.
# For the short term, the refresh process will only be runnable by Google engineers.
#
# The only allowed edits are to method and file documentation. A 3-way
# merge preserves those additions if the generated source changes.
"""Accesses the google.cloud.dialogflow.v2beta1 Agents API."""

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

from google.cloud.dialogflow_v2beta1.gapic import agents_client_config
from google.cloud.dialogflow_v2beta1.gapic import enums
from google.cloud.dialogflow_v2beta1.proto import agent_pb2
from google.protobuf import empty_pb2
from google.protobuf import struct_pb2

_PageDesc = google.gax.PageDescriptor


class AgentsClient(object):
    """
    Manages conversational agents.


    Refer to `documentation <https://api.ai/docs/agents>`_ for more details about
    # agents.

    Standard methods.
    """

    SERVICE_ADDRESS = 'dialogflow.googleapis.com'
    """The default address of the service."""

    DEFAULT_SERVICE_PORT = 443
    """The default port of the service."""

    _PAGE_DESCRIPTORS = {
        'search_agents': _PageDesc('page_token', 'next_page_token', 'agents')
    }

    # The scopes needed to make gRPC calls to all of the methods defined in
    # this service
    _ALL_SCOPES = ('https://www.googleapis.com/auth/cloud-platform', )

    _PROJECT_PATH_TEMPLATE = path_template.PathTemplate('projects/{project}')

    @classmethod
    def project_path(cls, project):
        """Returns a fully-qualified project resource name string."""
        return cls._PROJECT_PATH_TEMPLATE.render({
            'project': project,
        })

    @classmethod
    def match_project_from_project_name(cls, project_name):
        """Parses the project from a project resource.

        Args:
            project_name (str): A fully-qualified path representing a project
                resource.

        Returns:
            A string representing the project.
        """
        return cls._PROJECT_PATH_TEMPLATE.match(project_name).get('project')

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
            'google.cloud.dialogflow.v2beta1.Agents',
            agents_client_config.config,
            client_config,
            config.STATUS_CODE_NAMES,
            metrics_headers=metrics_headers,
            page_descriptors=self._PAGE_DESCRIPTORS, )
        self.agents_stub = config.create_stub(
            agent_pb2.AgentsStub,
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

        self._get_agent = api_callable.create_api_call(
            self.agents_stub.GetAgent, settings=defaults['get_agent'])
        self._search_agents = api_callable.create_api_call(
            self.agents_stub.SearchAgents, settings=defaults['search_agents'])
        self._train_agent = api_callable.create_api_call(
            self.agents_stub.TrainAgent, settings=defaults['train_agent'])
        self._export_agent = api_callable.create_api_call(
            self.agents_stub.ExportAgent, settings=defaults['export_agent'])
        self._import_agent = api_callable.create_api_call(
            self.agents_stub.ImportAgent, settings=defaults['import_agent'])
        self._restore_agent = api_callable.create_api_call(
            self.agents_stub.RestoreAgent, settings=defaults['restore_agent'])

    # Service calls
    def get_agent(self, parent, options=None):
        """
        Retrieves the specified agent.

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.AgentsClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> response = client.get_agent(parent)

        Args:
            parent (str): Required. The name of the agent.
                Format: ``projects/<Project ID>``.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types.Agent` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = agent_pb2.GetAgentRequest(parent=parent)
        return self._get_agent(request, options)

    def search_agents(self, parent, page_size=None, options=None):
        """
        Returns the list of agents.

        Since there is at most one conversational agent per project, this method is
        useful primarily for listing all agents across projects the caller has
        access to. One can achieve that with a wildcard project collection id \"-\".
        Refer to [List
        Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>> from google.gax import CallOptions, INITIAL_PAGE
            >>>
            >>> client = dialogflow_v2beta1.AgentsClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>>
            >>> # Iterate over all results
            >>> for element in client.search_agents(parent):
            ...     # process element
            ...     pass
            >>>
            >>> # Or iterate over results one page at a time
            >>> for page in client.search_agents(parent, options=CallOptions(page_token=INITIAL_PAGE)):
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The project to list agents from.
                Format: ``projects/<Project ID or '-'>``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.gax.PageIterator` instance. By default, this
            is an iterable of :class:`~google.cloud.dialogflow_v2beta1.types.Agent` instances.
            This object can also be configured to iterate over the pages
            of the response through the `options` parameter.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = agent_pb2.SearchAgentsRequest(
            parent=parent, page_size=page_size)
        return self._search_agents(request, options)

    def train_agent(self, parent, options=None):
        """
        Trains the specified agent.


        Operation<response: google.protobuf.Empty>

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.AgentsClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> response = client.train_agent(parent)
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
            parent (str): Required. The name of the agent to train.
                Format: ``projects/<Project ID>``.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types._OperationFuture` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = agent_pb2.TrainAgentRequest(parent=parent)
        return google.gax._OperationFuture(
            self._train_agent(request, options), self.operations_client,
            empty_pb2.Empty, struct_pb2.Struct, options)

    def export_agent(self, parent, agent_uri=None, options=None):
        """
        Exports the specified agent to a ZIP file.


        Operation<response: ExportAgentResponse>

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.AgentsClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> response = client.export_agent(parent)
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
            parent (str): Required. The name of the agent to export.
                Format: ``projects/<Project ID>``.
            agent_uri (str): Optional. The URI to export the agent to. Note: The URI must start with
                \"gs://\". If left unspecified, the serialized agent is returned inline.
            options (~google.gax.CallOptions): Overrides the default
                settings for this call, e.g, timeout, retries etc.

        Returns:
            A :class:`~google.cloud.dialogflow_v2beta1.types._OperationFuture` instance.

        Raises:
            :exc:`google.gax.errors.GaxError` if the RPC is aborted.
            :exc:`ValueError` if the parameters are invalid.
        """
        request = agent_pb2.ExportAgentRequest(
            parent=parent, agent_uri=agent_uri)
        return google.gax._OperationFuture(
            self._export_agent(request, options), self.operations_client,
            agent_pb2.ExportAgentResponse, struct_pb2.Struct, options)

    def import_agent(self,
                     parent,
                     agent_uri=None,
                     agent_content=None,
                     options=None):
        """
        Imports the specified agent from a ZIP file.

        Uploads new intents and entity types without deleting the existing ones.
        Intents and entity types with the same name are replaced with the new
        versions from ImportAgentRequest.


        Operation<response: google.protobuf.Empty>

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.AgentsClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> response = client.import_agent(parent)
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
            parent (str): Required. The name of the agent to import.
                Format: ``projects/<Project ID>``.
            agent_uri (str): The URI to a file containing the agent to import. Note: The URI must
                start with \"gs://\".
            agent_content (bytes): The agent to import.
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
            agent_uri=agent_uri,
            agent_content=agent_content, )

        request = agent_pb2.ImportAgentRequest(
            parent=parent, agent_uri=agent_uri, agent_content=agent_content)
        return google.gax._OperationFuture(
            self._import_agent(request, options), self.operations_client,
            empty_pb2.Empty, struct_pb2.Struct, options)

    def restore_agent(self,
                      parent,
                      agent_uri=None,
                      agent_content=None,
                      options=None):
        """
        Restores the specified agent from a ZIP file.

        Replaces the current agent version with a new one. All the intents and
        entity types in the older version are deleted.


        Operation<response: google.protobuf.Empty>

        Example:
            >>> from google.cloud import dialogflow_v2beta1
            >>>
            >>> client = dialogflow_v2beta1.AgentsClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> response = client.restore_agent(parent)
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
            parent (str): Required. The name of the agent to restore.
                Format: ``projects/<Project ID>``.
            agent_uri (str): The URI to a file containing the agent to restore. Note: The URI must
                start with \"gs://\".
            agent_content (bytes): The agent to restore.
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
            agent_uri=agent_uri,
            agent_content=agent_content, )

        request = agent_pb2.RestoreAgentRequest(
            parent=parent, agent_uri=agent_uri, agent_content=agent_content)
        return google.gax._OperationFuture(
            self._restore_agent(request, options), self.operations_client,
            empty_pb2.Empty, struct_pb2.Struct, options)
