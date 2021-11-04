# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers   # type: ignore
from google.api_core import gapic_v1       # type: ignore
import google.auth                         # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.dialogflow_v2beta1.types import knowledge_base
from google.cloud.dialogflow_v2beta1.types import knowledge_base as gcd_knowledge_base
from google.protobuf import empty_pb2  # type: ignore
from .base import KnowledgeBasesTransport, DEFAULT_CLIENT_INFO


class KnowledgeBasesGrpcTransport(KnowledgeBasesTransport):
    """gRPC backend transport for KnowledgeBases.

    Service for managing
    [KnowledgeBases][google.cloud.dialogflow.v2beta1.KnowledgeBase].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]

    def __init__(self, *,
            host: str = 'dialogflow.googleapis.com',
            credentials: ga_credentials.Credentials = None,
            credentials_file: str = None,
            scopes: Sequence[str] = None,
            channel: grpc.Channel = None,
            api_mtls_endpoint: str = None,
            client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
            ssl_channel_credentials: grpc.ChannelCredentials = None,
            client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(cls,
                       host: str = 'dialogflow.googleapis.com',
                       credentials: ga_credentials.Credentials = None,
                       credentials_file: str = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def list_knowledge_bases(self) -> Callable[
            [knowledge_base.ListKnowledgeBasesRequest],
            knowledge_base.ListKnowledgeBasesResponse]:
        r"""Return a callable for the list knowledge bases method over gRPC.

        Returns the list of all knowledge bases of the specified agent.

        Note: The ``projects.agent.knowledgeBases`` resource is
        deprecated; only use ``projects.knowledgeBases``.

        Returns:
            Callable[[~.ListKnowledgeBasesRequest],
                    ~.ListKnowledgeBasesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_knowledge_bases' not in self._stubs:
            self._stubs['list_knowledge_bases'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.v2beta1.KnowledgeBases/ListKnowledgeBases',
                request_serializer=knowledge_base.ListKnowledgeBasesRequest.serialize,
                response_deserializer=knowledge_base.ListKnowledgeBasesResponse.deserialize,
            )
        return self._stubs['list_knowledge_bases']

    @property
    def get_knowledge_base(self) -> Callable[
            [knowledge_base.GetKnowledgeBaseRequest],
            knowledge_base.KnowledgeBase]:
        r"""Return a callable for the get knowledge base method over gRPC.

        Retrieves the specified knowledge base.

        Note: The ``projects.agent.knowledgeBases`` resource is
        deprecated; only use ``projects.knowledgeBases``.

        Returns:
            Callable[[~.GetKnowledgeBaseRequest],
                    ~.KnowledgeBase]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_knowledge_base' not in self._stubs:
            self._stubs['get_knowledge_base'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.v2beta1.KnowledgeBases/GetKnowledgeBase',
                request_serializer=knowledge_base.GetKnowledgeBaseRequest.serialize,
                response_deserializer=knowledge_base.KnowledgeBase.deserialize,
            )
        return self._stubs['get_knowledge_base']

    @property
    def create_knowledge_base(self) -> Callable[
            [gcd_knowledge_base.CreateKnowledgeBaseRequest],
            gcd_knowledge_base.KnowledgeBase]:
        r"""Return a callable for the create knowledge base method over gRPC.

        Creates a knowledge base.

        Note: The ``projects.agent.knowledgeBases`` resource is
        deprecated; only use ``projects.knowledgeBases``.

        Returns:
            Callable[[~.CreateKnowledgeBaseRequest],
                    ~.KnowledgeBase]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_knowledge_base' not in self._stubs:
            self._stubs['create_knowledge_base'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.v2beta1.KnowledgeBases/CreateKnowledgeBase',
                request_serializer=gcd_knowledge_base.CreateKnowledgeBaseRequest.serialize,
                response_deserializer=gcd_knowledge_base.KnowledgeBase.deserialize,
            )
        return self._stubs['create_knowledge_base']

    @property
    def delete_knowledge_base(self) -> Callable[
            [knowledge_base.DeleteKnowledgeBaseRequest],
            empty_pb2.Empty]:
        r"""Return a callable for the delete knowledge base method over gRPC.

        Deletes the specified knowledge base.

        Note: The ``projects.agent.knowledgeBases`` resource is
        deprecated; only use ``projects.knowledgeBases``.

        Returns:
            Callable[[~.DeleteKnowledgeBaseRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_knowledge_base' not in self._stubs:
            self._stubs['delete_knowledge_base'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.v2beta1.KnowledgeBases/DeleteKnowledgeBase',
                request_serializer=knowledge_base.DeleteKnowledgeBaseRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_knowledge_base']

    @property
    def update_knowledge_base(self) -> Callable[
            [gcd_knowledge_base.UpdateKnowledgeBaseRequest],
            gcd_knowledge_base.KnowledgeBase]:
        r"""Return a callable for the update knowledge base method over gRPC.

        Updates the specified knowledge base.

        Note: The ``projects.agent.knowledgeBases`` resource is
        deprecated; only use ``projects.knowledgeBases``.

        Returns:
            Callable[[~.UpdateKnowledgeBaseRequest],
                    ~.KnowledgeBase]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_knowledge_base' not in self._stubs:
            self._stubs['update_knowledge_base'] = self.grpc_channel.unary_unary(
                '/google.cloud.dialogflow.v2beta1.KnowledgeBases/UpdateKnowledgeBase',
                request_serializer=gcd_knowledge_base.UpdateKnowledgeBaseRequest.serialize,
                response_deserializer=gcd_knowledge_base.KnowledgeBase.deserialize,
            )
        return self._stubs['update_knowledge_base']

    def close(self):
        self.grpc_channel.close()

__all__ = (
    'KnowledgeBasesGrpcTransport',
)
