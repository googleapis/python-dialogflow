# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.dialogflow_v2.services.conversation_models import pagers
from google.cloud.dialogflow_v2.types import conversation_model
from google.cloud.dialogflow_v2.types import (
    conversation_model as gcd_conversation_model,
)
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import ConversationModelsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ConversationModelsGrpcAsyncIOTransport
from .client import ConversationModelsClient


class ConversationModelsAsyncClient:
    """Manages a collection of models for human agent assistant."""

    _client: ConversationModelsClient

    DEFAULT_ENDPOINT = ConversationModelsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ConversationModelsClient.DEFAULT_MTLS_ENDPOINT

    conversation_dataset_path = staticmethod(
        ConversationModelsClient.conversation_dataset_path
    )
    parse_conversation_dataset_path = staticmethod(
        ConversationModelsClient.parse_conversation_dataset_path
    )
    conversation_model_path = staticmethod(
        ConversationModelsClient.conversation_model_path
    )
    parse_conversation_model_path = staticmethod(
        ConversationModelsClient.parse_conversation_model_path
    )
    conversation_model_evaluation_path = staticmethod(
        ConversationModelsClient.conversation_model_evaluation_path
    )
    parse_conversation_model_evaluation_path = staticmethod(
        ConversationModelsClient.parse_conversation_model_evaluation_path
    )
    document_path = staticmethod(ConversationModelsClient.document_path)
    parse_document_path = staticmethod(ConversationModelsClient.parse_document_path)
    common_billing_account_path = staticmethod(
        ConversationModelsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ConversationModelsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ConversationModelsClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ConversationModelsClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ConversationModelsClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ConversationModelsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ConversationModelsClient.common_project_path)
    parse_common_project_path = staticmethod(
        ConversationModelsClient.parse_common_project_path
    )
    common_location_path = staticmethod(ConversationModelsClient.common_location_path)
    parse_common_location_path = staticmethod(
        ConversationModelsClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ConversationModelsAsyncClient: The constructed client.
        """
        return ConversationModelsClient.from_service_account_info.__func__(ConversationModelsAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ConversationModelsAsyncClient: The constructed client.
        """
        return ConversationModelsClient.from_service_account_file.__func__(ConversationModelsAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return ConversationModelsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ConversationModelsTransport:
        """Returns the transport used by the client instance.

        Returns:
            ConversationModelsTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ConversationModelsClient).get_transport_class,
        type(ConversationModelsClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, ConversationModelsTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the conversation models client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ConversationModelsTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = ConversationModelsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_conversation_model(
        self,
        request: Union[
            gcd_conversation_model.CreateConversationModelRequest, dict
        ] = None,
        *,
        parent: str = None,
        conversation_model: gcd_conversation_model.ConversationModel = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a model.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [CreateConversationModelOperationMetadata][google.cloud.dialogflow.v2.CreateConversationModelOperationMetadata]
        -  ``response``:
           [ConversationModel][google.cloud.dialogflow.v2.ConversationModel]

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_create_conversation_model():
                # Create a client
                client = dialogflow_v2.ConversationModelsAsyncClient()

                # Initialize request argument(s)
                conversation_model = dialogflow_v2.ConversationModel()
                conversation_model.display_name = "display_name_value"
                conversation_model.datasets.dataset = "dataset_value"

                request = dialogflow_v2.CreateConversationModelRequest(
                    conversation_model=conversation_model,
                )

                # Make the request
                operation = client.create_conversation_model(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.CreateConversationModelRequest, dict]):
                The request object. The request message for
                [ConversationModels.CreateConversationModel][google.cloud.dialogflow.v2.ConversationModels.CreateConversationModel]
            parent (:class:`str`):
                The project to create conversation model for. Format:
                ``projects/<Project ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            conversation_model (:class:`google.cloud.dialogflow_v2.types.ConversationModel`):
                Required. The conversation model to
                create.

                This corresponds to the ``conversation_model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dialogflow_v2.types.ConversationModel`
                Represents a conversation model.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, conversation_model])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_conversation_model.CreateConversationModelRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if conversation_model is not None:
            request.conversation_model = conversation_model

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_conversation_model,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            gcd_conversation_model.ConversationModel,
            metadata_type=gcd_conversation_model.CreateConversationModelOperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_conversation_model(
        self,
        request: Union[conversation_model.GetConversationModelRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> conversation_model.ConversationModel:
        r"""Gets conversation model.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_get_conversation_model():
                # Create a client
                client = dialogflow_v2.ConversationModelsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.GetConversationModelRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_conversation_model(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.GetConversationModelRequest, dict]):
                The request object. The request message for
                [ConversationModels.GetConversationModel][google.cloud.dialogflow.v2.ConversationModels.GetConversationModel]
            name (:class:`str`):
                Required. The conversation model to retrieve. Format:
                ``projects/<Project ID>/conversationModels/<Conversation Model ID>``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.ConversationModel:
                Represents a conversation model.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversation_model.GetConversationModelRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_conversation_model,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_conversation_models(
        self,
        request: Union[conversation_model.ListConversationModelsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListConversationModelsAsyncPager:
        r"""Lists conversation models.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_list_conversation_models():
                # Create a client
                client = dialogflow_v2.ConversationModelsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.ListConversationModelsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_conversation_models(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.ListConversationModelsRequest, dict]):
                The request object. The request message for
                [ConversationModels.ListConversationModels][google.cloud.dialogflow.v2.ConversationModels.ListConversationModels]
            parent (:class:`str`):
                Required. The project to list all conversation models
                for. Format: ``projects/<Project ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.services.conversation_models.pagers.ListConversationModelsAsyncPager:
                The response message for
                   [ConversationModels.ListConversationModels][google.cloud.dialogflow.v2.ConversationModels.ListConversationModels]

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversation_model.ListConversationModelsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_conversation_models,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListConversationModelsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_conversation_model(
        self,
        request: Union[conversation_model.DeleteConversationModelRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a model.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [DeleteConversationModelOperationMetadata][google.cloud.dialogflow.v2.DeleteConversationModelOperationMetadata]
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_delete_conversation_model():
                # Create a client
                client = dialogflow_v2.ConversationModelsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.DeleteConversationModelRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_conversation_model(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.DeleteConversationModelRequest, dict]):
                The request object. The request message for
                [ConversationModels.DeleteConversationModel][google.cloud.dialogflow.v2.ConversationModels.DeleteConversationModel]
            name (:class:`str`):
                Required. The conversation model to delete. Format:
                ``projects/<Project ID>/conversationModels/<Conversation Model ID>``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversation_model.DeleteConversationModelRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_conversation_model,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=conversation_model.DeleteConversationModelOperationMetadata,
        )

        # Done; return the response.
        return response

    async def deploy_conversation_model(
        self,
        request: Union[conversation_model.DeployConversationModelRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deploys a model. If a model is already deployed, deploying it
        has no effect. A model can only serve prediction requests after
        it gets deployed. For article suggestion, custom model will not
        be used unless it is deployed.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [DeployConversationModelOperationMetadata][google.cloud.dialogflow.v2.DeployConversationModelOperationMetadata]
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_deploy_conversation_model():
                # Create a client
                client = dialogflow_v2.ConversationModelsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.DeployConversationModelRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.deploy_conversation_model(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.DeployConversationModelRequest, dict]):
                The request object. The request message for
                [ConversationModels.DeployConversationModel][google.cloud.dialogflow.v2.ConversationModels.DeployConversationModel]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        request = conversation_model.DeployConversationModelRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.deploy_conversation_model,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=conversation_model.DeployConversationModelOperationMetadata,
        )

        # Done; return the response.
        return response

    async def undeploy_conversation_model(
        self,
        request: Union[
            conversation_model.UndeployConversationModelRequest, dict
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Undeploys a model. If the model is not deployed this method has
        no effect. If the model is currently being used:

        -  For article suggestion, article suggestion will fallback to
           the default model if model is undeployed.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [UndeployConversationModelOperationMetadata][google.cloud.dialogflow.v2.UndeployConversationModelOperationMetadata]
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_undeploy_conversation_model():
                # Create a client
                client = dialogflow_v2.ConversationModelsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.UndeployConversationModelRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.undeploy_conversation_model(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.UndeployConversationModelRequest, dict]):
                The request object. The request message for
                [ConversationModels.UndeployConversationModel][google.cloud.dialogflow.v2.ConversationModels.UndeployConversationModel]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        request = conversation_model.UndeployConversationModelRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.undeploy_conversation_model,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=conversation_model.UndeployConversationModelOperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_conversation_model_evaluation(
        self,
        request: Union[
            conversation_model.GetConversationModelEvaluationRequest, dict
        ] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> conversation_model.ConversationModelEvaluation:
        r"""Gets an evaluation of conversation model.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_get_conversation_model_evaluation():
                # Create a client
                client = dialogflow_v2.ConversationModelsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.GetConversationModelEvaluationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_conversation_model_evaluation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.GetConversationModelEvaluationRequest, dict]):
                The request object. The request message for
                [ConversationModels.GetConversationModelEvaluation][google.cloud.dialogflow.v2.ConversationModels.GetConversationModelEvaluation]
            name (:class:`str`):
                Required. The conversation model evaluation resource
                name. Format:
                ``projects/<Project ID>/conversationModels/<Conversation Model ID>/evaluations/<Evaluation ID>``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.ConversationModelEvaluation:
                Represents evaluation result of a
                conversation model.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversation_model.GetConversationModelEvaluationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_conversation_model_evaluation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_conversation_model_evaluations(
        self,
        request: Union[
            conversation_model.ListConversationModelEvaluationsRequest, dict
        ] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListConversationModelEvaluationsAsyncPager:
        r"""Lists evaluations of a conversation model.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_list_conversation_model_evaluations():
                # Create a client
                client = dialogflow_v2.ConversationModelsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.ListConversationModelEvaluationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_conversation_model_evaluations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsRequest, dict]):
                The request object. The request message for
                [ConversationModels.ListConversationModelEvaluations][google.cloud.dialogflow.v2.ConversationModels.ListConversationModelEvaluations]
            parent (:class:`str`):
                Required. The conversation model resource name. Format:
                ``projects/<Project ID>/conversationModels/<Conversation Model ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.services.conversation_models.pagers.ListConversationModelEvaluationsAsyncPager:
                The response message for
                   [ConversationModels.ListConversationModelEvaluations][google.cloud.dialogflow.v2.ConversationModels.ListConversationModelEvaluations]

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversation_model.ListConversationModelEvaluationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_conversation_model_evaluations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListConversationModelEvaluationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_conversation_model_evaluation(
        self,
        request: Union[
            conversation_model.CreateConversationModelEvaluationRequest, dict
        ] = None,
        *,
        parent: str = None,
        conversation_model_evaluation: conversation_model.ConversationModelEvaluation = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates evaluation of a conversation model.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_create_conversation_model_evaluation():
                # Create a client
                client = dialogflow_v2.ConversationModelsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.CreateConversationModelEvaluationRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = client.create_conversation_model_evaluation(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.CreateConversationModelEvaluationRequest, dict]):
                The request object. The request message for
                [ConversationModels.CreateConversationModelEvaluation][google.cloud.dialogflow.v2.ConversationModels.CreateConversationModelEvaluation]
            parent (:class:`str`):
                Required. The conversation model resource name. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversationModels/<Conversation Model ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            conversation_model_evaluation (:class:`google.cloud.dialogflow_v2.types.ConversationModelEvaluation`):
                Required. The conversation model
                evaluation to be created.

                This corresponds to the ``conversation_model_evaluation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dialogflow_v2.types.ConversationModelEvaluation`
                Represents evaluation result of a conversation model.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, conversation_model_evaluation])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversation_model.CreateConversationModelEvaluationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if conversation_model_evaluation is not None:
            request.conversation_model_evaluation = conversation_model_evaluation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_conversation_model_evaluation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            conversation_model.ConversationModelEvaluation,
            metadata_type=conversation_model.CreateConversationModelEvaluationOperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-dialogflow",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("ConversationModelsAsyncClient",)
