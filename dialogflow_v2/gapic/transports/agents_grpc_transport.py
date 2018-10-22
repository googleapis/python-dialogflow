# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import google.api_core.grpc_helpers
import google.api_core.operations_v1

from dialogflow_v2.proto import agent_pb2_grpc


class AgentsGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.dialogflow.v2 Agents API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """
    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ('https://www.googleapis.com/auth/cloud-platform', )

    def __init__(self,
                 channel=None,
                 credentials=None,
                 address='dialogflow.googleapis.com:443'):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                'The `channel` and `credentials` arguments are mutually '
                'exclusive.', )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
            )

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            'agents_stub': agent_pb2_grpc.AgentsStub(channel),
        }

        # Because this API includes a method that returns a
        # long-running operation (proto: google.longrunning.Operation),
        # instantiate an LRO client.
        self._operations_client = google.api_core.operations_v1.OperationsClient(
            channel)

    @classmethod
    def create_channel(cls,
                       address='dialogflow.googleapis.com:443',
                       credentials=None):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address,
            credentials=credentials,
            scopes=cls._OAUTH_SCOPES,
        )

    @property
    def get_agent(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Retrieves the specified agent.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['agents_stub'].GetAgent

    @property
    def search_agents(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Returns the list of agents.

        Since there is at most one conversational agent per project, this method is
        useful primarily for listing all agents across projects the caller has
        access to. One can achieve that with a wildcard project collection id \"-\".
        Refer to [List
        Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['agents_stub'].SearchAgents

    @property
    def train_agent(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Trains the specified agent.

        Operation <response: ``google.protobuf.Empty``,
        metadata: [google.protobuf.Struct][google.protobuf.Struct]>

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['agents_stub'].TrainAgent

    @property
    def export_agent(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Exports the specified agent to a ZIP file.

        Operation <response: ``ExportAgentResponse``,
        metadata: [google.protobuf.Struct][google.protobuf.Struct]>

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['agents_stub'].ExportAgent

    @property
    def import_agent(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Imports the specified agent from a ZIP file.

        Uploads new intents and entity types without deleting the existing ones.
        Intents and entity types with the same name are replaced with the new
        versions from ImportAgentRequest.

        Operation <response: ``google.protobuf.Empty``,
        metadata: [google.protobuf.Struct][google.protobuf.Struct]>

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['agents_stub'].ImportAgent

    @property
    def restore_agent(self):
        """Return the gRPC stub for {$apiMethod.name}.

        Restores the specified agent from a ZIP file.

        Replaces the current agent version with a new one. All the intents and
        entity types in the older version are deleted.

        Operation <response: ``google.protobuf.Empty``,
        metadata: [google.protobuf.Struct][google.protobuf.Struct]>

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['agents_stub'].RestoreAgent
