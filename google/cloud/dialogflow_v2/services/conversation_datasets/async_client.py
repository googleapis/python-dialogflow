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
from google.cloud.dialogflow_v2.services.conversation_datasets import pagers
from google.cloud.dialogflow_v2.types import conversation_dataset
from google.cloud.dialogflow_v2.types import (
    conversation_dataset as gcd_conversation_dataset,
)
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import ConversationDatasetsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ConversationDatasetsGrpcAsyncIOTransport
from .client import ConversationDatasetsClient


class ConversationDatasetsAsyncClient:
    """Conversation datasets.
    Conversation datasets contain raw conversation files and their
    customizable metadata that can be used for model training.
    """

    _client: ConversationDatasetsClient

    DEFAULT_ENDPOINT = ConversationDatasetsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ConversationDatasetsClient.DEFAULT_MTLS_ENDPOINT

    conversation_dataset_path = staticmethod(
        ConversationDatasetsClient.conversation_dataset_path
    )
    parse_conversation_dataset_path = staticmethod(
        ConversationDatasetsClient.parse_conversation_dataset_path
    )
    common_billing_account_path = staticmethod(
        ConversationDatasetsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ConversationDatasetsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ConversationDatasetsClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ConversationDatasetsClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ConversationDatasetsClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ConversationDatasetsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ConversationDatasetsClient.common_project_path)
    parse_common_project_path = staticmethod(
        ConversationDatasetsClient.parse_common_project_path
    )
    common_location_path = staticmethod(ConversationDatasetsClient.common_location_path)
    parse_common_location_path = staticmethod(
        ConversationDatasetsClient.parse_common_location_path
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
            ConversationDatasetsAsyncClient: The constructed client.
        """
        return ConversationDatasetsClient.from_service_account_info.__func__(ConversationDatasetsAsyncClient, info, *args, **kwargs)  # type: ignore

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
            ConversationDatasetsAsyncClient: The constructed client.
        """
        return ConversationDatasetsClient.from_service_account_file.__func__(ConversationDatasetsAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return ConversationDatasetsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ConversationDatasetsTransport:
        """Returns the transport used by the client instance.

        Returns:
            ConversationDatasetsTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ConversationDatasetsClient).get_transport_class,
        type(ConversationDatasetsClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, ConversationDatasetsTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the conversation datasets client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ConversationDatasetsTransport]): The
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
        self._client = ConversationDatasetsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_conversation_dataset(
        self,
        request: Union[
            gcd_conversation_dataset.CreateConversationDatasetRequest, dict
        ] = None,
        *,
        parent: str = None,
        conversation_dataset: gcd_conversation_dataset.ConversationDataset = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new conversation dataset.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [CreateConversationDatasetOperationMetadata][google.cloud.dialogflow.v2.CreateConversationDatasetOperationMetadata]
        -  ``response``:
           [ConversationDataset][google.cloud.dialogflow.v2.ConversationDataset]

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_create_conversation_dataset():
                # Create a client
                client = dialogflow_v2.ConversationDatasetsAsyncClient()

                # Initialize request argument(s)
                conversation_dataset = dialogflow_v2.ConversationDataset()
                conversation_dataset.display_name = "display_name_value"

                request = dialogflow_v2.CreateConversationDatasetRequest(
                    parent="parent_value",
                    conversation_dataset=conversation_dataset,
                )

                # Make the request
                operation = client.create_conversation_dataset(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.CreateConversationDatasetRequest, dict]):
                The request object. The request message for
                [ConversationDatasets.CreateConversationDataset][google.cloud.dialogflow.v2.ConversationDatasets.CreateConversationDataset].
            parent (:class:`str`):
                Required. The project to create conversation dataset
                for. Format:
                ``projects/<Project ID>/locations/<Location ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            conversation_dataset (:class:`google.cloud.dialogflow_v2.types.ConversationDataset`):
                Required. The conversation dataset to
                create.

                This corresponds to the ``conversation_dataset`` field
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

                The result type for the operation will be :class:`google.cloud.dialogflow_v2.types.ConversationDataset` Represents a conversation dataset that a user imports raw data into.
                   The data inside ConversationDataset can not be
                   changed after ImportConversationData finishes (and
                   calling ImportConversationData on a dataset that
                   already has data is not allowed).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, conversation_dataset])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_conversation_dataset.CreateConversationDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if conversation_dataset is not None:
            request.conversation_dataset = conversation_dataset

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_conversation_dataset,
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
            gcd_conversation_dataset.ConversationDataset,
            metadata_type=gcd_conversation_dataset.CreateConversationDatasetOperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_conversation_dataset(
        self,
        request: Union[conversation_dataset.GetConversationDatasetRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> conversation_dataset.ConversationDataset:
        r"""Retrieves the specified conversation dataset.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_get_conversation_dataset():
                # Create a client
                client = dialogflow_v2.ConversationDatasetsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.GetConversationDatasetRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_conversation_dataset(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.GetConversationDatasetRequest, dict]):
                The request object. The request message for
                [ConversationDatasets.GetConversationDataset][google.cloud.dialogflow.v2.ConversationDatasets.GetConversationDataset].
            name (:class:`str`):
                Required. The conversation dataset to retrieve. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.ConversationDataset:
                Represents a conversation dataset
                that a user imports raw data into. The
                data inside ConversationDataset can not
                be changed after ImportConversationData
                finishes (and calling
                ImportConversationData on a dataset that
                already has data is not allowed).

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

        request = conversation_dataset.GetConversationDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_conversation_dataset,
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

    async def list_conversation_datasets(
        self,
        request: Union[
            conversation_dataset.ListConversationDatasetsRequest, dict
        ] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListConversationDatasetsAsyncPager:
        r"""Returns the list of all conversation datasets in the
        specified project and location.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_list_conversation_datasets():
                # Create a client
                client = dialogflow_v2.ConversationDatasetsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.ListConversationDatasetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_conversation_datasets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.ListConversationDatasetsRequest, dict]):
                The request object. The request message for
                [ConversationDatasets.ListConversationDatasets][google.cloud.dialogflow.v2.ConversationDatasets.ListConversationDatasets].
            parent (:class:`str`):
                Required. The project and location name to list all
                conversation datasets for. Format:
                ``projects/<Project ID>/locations/<Location ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.services.conversation_datasets.pagers.ListConversationDatasetsAsyncPager:
                The response message for
                   [ConversationDatasets.ListConversationDatasets][google.cloud.dialogflow.v2.ConversationDatasets.ListConversationDatasets].

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

        request = conversation_dataset.ListConversationDatasetsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_conversation_datasets,
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
        response = pagers.ListConversationDatasetsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_conversation_dataset(
        self,
        request: Union[
            conversation_dataset.DeleteConversationDatasetRequest, dict
        ] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes the specified conversation dataset.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [DeleteConversationDatasetOperationMetadata][google.cloud.dialogflow.v2.DeleteConversationDatasetOperationMetadata]
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_delete_conversation_dataset():
                # Create a client
                client = dialogflow_v2.ConversationDatasetsAsyncClient()

                # Initialize request argument(s)
                request = dialogflow_v2.DeleteConversationDatasetRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_conversation_dataset(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.DeleteConversationDatasetRequest, dict]):
                The request object. The request message for
                [ConversationDatasets.DeleteConversationDataset][google.cloud.dialogflow.v2.ConversationDatasets.DeleteConversationDataset].
            name (:class:`str`):
                Required. The conversation dataset to delete. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>``

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

        request = conversation_dataset.DeleteConversationDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_conversation_dataset,
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
            metadata_type=conversation_dataset.DeleteConversationDatasetOperationMetadata,
        )

        # Done; return the response.
        return response

    async def import_conversation_data(
        self,
        request: Union[conversation_dataset.ImportConversationDataRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Import data into the specified conversation dataset. Note that
        it is not allowed to import data to a conversation dataset that
        already has data in it.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [ImportConversationDataOperationMetadata][google.cloud.dialogflow.v2.ImportConversationDataOperationMetadata]
        -  ``response``:
           [ImportConversationDataOperationResponse][google.cloud.dialogflow.v2.ImportConversationDataOperationResponse]

        .. code-block:: python

            from google.cloud import dialogflow_v2

            async def sample_import_conversation_data():
                # Create a client
                client = dialogflow_v2.ConversationDatasetsAsyncClient()

                # Initialize request argument(s)
                input_config = dialogflow_v2.InputConfig()
                input_config.gcs_source.uris = ['uris_value_1', 'uris_value_2']

                request = dialogflow_v2.ImportConversationDataRequest(
                    name="name_value",
                    input_config=input_config,
                )

                # Make the request
                operation = client.import_conversation_data(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.ImportConversationDataRequest, dict]):
                The request object. The request message for
                [ConversationDatasets.ImportConversationData][google.cloud.dialogflow.v2.ConversationDatasets.ImportConversationData].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.dialogflow_v2.types.ImportConversationDataOperationResponse` Response used for [ConversationDatasets.ImportConversationData][google.cloud.dialogflow.v2.ConversationDatasets.ImportConversationData] long
                   running operation.

        """
        # Create or coerce a protobuf request object.
        request = conversation_dataset.ImportConversationDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.import_conversation_data,
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
            conversation_dataset.ImportConversationDataOperationResponse,
            metadata_type=conversation_dataset.ImportConversationDataOperationMetadata,
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


__all__ = ("ConversationDatasetsAsyncClient",)
