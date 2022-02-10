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
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
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
from google.cloud.dialogflow_v2.services.documents import pagers
from google.cloud.dialogflow_v2.types import document
from google.cloud.dialogflow_v2.types import document as gcd_document
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from .transports.base import DocumentsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import DocumentsGrpcAsyncIOTransport
from .client import DocumentsClient


class DocumentsAsyncClient:
    """Service for managing knowledge
    [Documents][google.cloud.dialogflow.v2.Document].
    """

    _client: DocumentsClient

    DEFAULT_ENDPOINT = DocumentsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DocumentsClient.DEFAULT_MTLS_ENDPOINT

    document_path = staticmethod(DocumentsClient.document_path)
    parse_document_path = staticmethod(DocumentsClient.parse_document_path)
    common_billing_account_path = staticmethod(
        DocumentsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DocumentsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DocumentsClient.common_folder_path)
    parse_common_folder_path = staticmethod(DocumentsClient.parse_common_folder_path)
    common_organization_path = staticmethod(DocumentsClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        DocumentsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DocumentsClient.common_project_path)
    parse_common_project_path = staticmethod(DocumentsClient.parse_common_project_path)
    common_location_path = staticmethod(DocumentsClient.common_location_path)
    parse_common_location_path = staticmethod(
        DocumentsClient.parse_common_location_path
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
            DocumentsAsyncClient: The constructed client.
        """
        return DocumentsClient.from_service_account_info.__func__(DocumentsAsyncClient, info, *args, **kwargs)  # type: ignore

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
            DocumentsAsyncClient: The constructed client.
        """
        return DocumentsClient.from_service_account_file.__func__(DocumentsAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return DocumentsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DocumentsTransport:
        """Returns the transport used by the client instance.

        Returns:
            DocumentsTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(DocumentsClient).get_transport_class, type(DocumentsClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, DocumentsTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the documents client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DocumentsTransport]): The
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
        self._client = DocumentsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_documents(
        self,
        request: Union[document.ListDocumentsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListDocumentsAsyncPager:
        r"""Returns the list of all documents of the knowledge
        base.


        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_list_documents():
                # Create a client
                client = dialogflow_v2.DocumentsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.ListDocumentsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_documents(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.ListDocumentsRequest, dict]):
                The request object. Request message for
                [Documents.ListDocuments][google.cloud.dialogflow.v2.Documents.ListDocuments].
            parent (:class:`str`):
                Required. The knowledge base to list all documents for.
                Format:
                ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.services.documents.pagers.ListDocumentsAsyncPager:
                Response message for
                [Documents.ListDocuments][google.cloud.dialogflow.v2.Documents.ListDocuments].

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

        request = document.ListDocumentsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_documents,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListDocumentsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_document(
        self,
        request: Union[document.GetDocumentRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> document.Document:
        r"""Retrieves the specified document.

        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_get_document():
                # Create a client
                client = dialogflow_v2.DocumentsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.GetDocumentRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_document(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.GetDocumentRequest, dict]):
                The request object. Request message for
                [Documents.GetDocument][google.cloud.dialogflow.v2.Documents.GetDocument].
            name (:class:`str`):
                Required. The name of the document to retrieve. Format
                ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.Document:
                A knowledge document to be used by a
                [KnowledgeBase][google.cloud.dialogflow.v2.KnowledgeBase].

                   For more information, see the [knowledge base
                   guide](\ https://cloud.google.com/dialogflow/docs/how/knowledge-bases).

                   Note: The projects.agent.knowledgeBases.documents
                   resource is deprecated; only use
                   projects.knowledgeBases.documents.

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

        request = document.GetDocumentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_document,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_document(
        self,
        request: Union[gcd_document.CreateDocumentRequest, dict] = None,
        *,
        parent: str = None,
        document: gcd_document.Document = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new document.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [KnowledgeOperationMetadata][google.cloud.dialogflow.v2.KnowledgeOperationMetadata]
        -  ``response``: [Document][google.cloud.dialogflow.v2.Document]


        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_create_document():
                # Create a client
                client = dialogflow_v2.DocumentsClient()

                # Initialize request argument(s)
                document = dialogflow_v2.Document()
                document.content_uri = "content_uri_value"
                document.display_name = "display_name_value"
                document.mime_type = "mime_type_value"
                document.knowledge_types = "ARTICLE_SUGGESTION"

                request = dialogflow_v2.CreateDocumentRequest(
                    parent="parent_value",
                    document=document,
                )

                # Make the request
                operation = client.create_document(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.CreateDocumentRequest, dict]):
                The request object. Request message for
                [Documents.CreateDocument][google.cloud.dialogflow.v2.Documents.CreateDocument].
            parent (:class:`str`):
                Required. The knowledge base to create a document for.
                Format:
                ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            document (:class:`google.cloud.dialogflow_v2.types.Document`):
                Required. The document to create.
                This corresponds to the ``document`` field
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
                :class:`google.cloud.dialogflow_v2.types.Document` A
                knowledge document to be used by a
                [KnowledgeBase][google.cloud.dialogflow.v2.KnowledgeBase].

                   For more information, see the [knowledge base
                   guide](\ https://cloud.google.com/dialogflow/docs/how/knowledge-bases).

                   Note: The projects.agent.knowledgeBases.documents
                   resource is deprecated; only use
                   projects.knowledgeBases.documents.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, document])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_document.CreateDocumentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if document is not None:
            request.document = document

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_document,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            gcd_document.Document,
            metadata_type=gcd_document.KnowledgeOperationMetadata,
        )

        # Done; return the response.
        return response

    async def import_documents(
        self,
        request: Union[document.ImportDocumentsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates documents by importing data from external sources.
        Dialogflow supports up to 350 documents in each request. If you
        try to import more, Dialogflow will return an error.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [KnowledgeOperationMetadata][google.cloud.dialogflow.v2.KnowledgeOperationMetadata]
        -  ``response``:
           [ImportDocumentsResponse][google.cloud.dialogflow.v2.ImportDocumentsResponse]


        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_import_documents():
                # Create a client
                client = dialogflow_v2.DocumentsClient()

                # Initialize request argument(s)
                gcs_source = dialogflow_v2.GcsSources()
                gcs_source.uris = ['uris_value_1', 'uris_value_2']

                document_template = dialogflow_v2.ImportDocumentTemplate()
                document_template.mime_type = "mime_type_value"
                document_template.knowledge_types = "ARTICLE_SUGGESTION"

                request = dialogflow_v2.ImportDocumentsRequest(
                    gcs_source=gcs_source,
                    parent="parent_value",
                    document_template=document_template,
                )

                # Make the request
                operation = client.import_documents(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.ImportDocumentsRequest, dict]):
                The request object. Request message for
                [Documents.ImportDocuments][google.cloud.dialogflow.v2.Documents.ImportDocuments].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dialogflow_v2.types.ImportDocumentsResponse`
                Response message for
                [Documents.ImportDocuments][google.cloud.dialogflow.v2.Documents.ImportDocuments].

        """
        # Create or coerce a protobuf request object.
        request = document.ImportDocumentsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.import_documents,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document.ImportDocumentsResponse,
            metadata_type=document.KnowledgeOperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_document(
        self,
        request: Union[document.DeleteDocumentRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes the specified document.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [KnowledgeOperationMetadata][google.cloud.dialogflow.v2.KnowledgeOperationMetadata]
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__


        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_delete_document():
                # Create a client
                client = dialogflow_v2.DocumentsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.DeleteDocumentRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_document(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.DeleteDocumentRequest, dict]):
                The request object. Request message for
                [Documents.DeleteDocument][google.cloud.dialogflow.v2.Documents.DeleteDocument].
            name (:class:`str`):
                Required. The name of the document to delete. Format:
                ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.

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

        request = document.DeleteDocumentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_document,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=document.KnowledgeOperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_document(
        self,
        request: Union[gcd_document.UpdateDocumentRequest, dict] = None,
        *,
        document: gcd_document.Document = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the specified document.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [KnowledgeOperationMetadata][google.cloud.dialogflow.v2.KnowledgeOperationMetadata]
        -  ``response``: [Document][google.cloud.dialogflow.v2.Document]


        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_update_document():
                # Create a client
                client = dialogflow_v2.DocumentsClient()

                # Initialize request argument(s)
                document = dialogflow_v2.Document()
                document.content_uri = "content_uri_value"
                document.display_name = "display_name_value"
                document.mime_type = "mime_type_value"
                document.knowledge_types = "ARTICLE_SUGGESTION"

                request = dialogflow_v2.UpdateDocumentRequest(
                    document=document,
                )

                # Make the request
                operation = client.update_document(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.UpdateDocumentRequest, dict]):
                The request object. Request message for
                [Documents.UpdateDocument][google.cloud.dialogflow.v2.Documents.UpdateDocument].
            document (:class:`google.cloud.dialogflow_v2.types.Document`):
                Required. The document to update.
                This corresponds to the ``document`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Not specified means ``update all``. Currently,
                only ``display_name`` can be updated, an InvalidArgument
                will be returned for attempting to update other fields.

                This corresponds to the ``update_mask`` field
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
                :class:`google.cloud.dialogflow_v2.types.Document` A
                knowledge document to be used by a
                [KnowledgeBase][google.cloud.dialogflow.v2.KnowledgeBase].

                   For more information, see the [knowledge base
                   guide](\ https://cloud.google.com/dialogflow/docs/how/knowledge-bases).

                   Note: The projects.agent.knowledgeBases.documents
                   resource is deprecated; only use
                   projects.knowledgeBases.documents.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([document, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_document.UpdateDocumentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if document is not None:
            request.document = document
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_document,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("document.name", request.document.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            gcd_document.Document,
            metadata_type=gcd_document.KnowledgeOperationMetadata,
        )

        # Done; return the response.
        return response

    async def reload_document(
        self,
        request: Union[document.ReloadDocumentRequest, dict] = None,
        *,
        name: str = None,
        content_uri: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Reloads the specified document from its specified source,
        content_uri or content. The previously loaded content of the
        document will be deleted. Note: Even when the content of the
        document has not changed, there still may be side effects
        because of internal implementation changes.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [KnowledgeOperationMetadata][google.cloud.dialogflow.v2.KnowledgeOperationMetadata]
        -  ``response``: [Document][google.cloud.dialogflow.v2.Document]

        Note: The ``projects.agent.knowledgeBases.documents`` resource
        is deprecated; only use ``projects.knowledgeBases.documents``.


        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_reload_document():
                # Create a client
                client = dialogflow_v2.DocumentsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.ReloadDocumentRequest(
                    content_uri="content_uri_value",
                    name="name_value",
                )

                # Make the request
                operation = client.reload_document(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.ReloadDocumentRequest, dict]):
                The request object. Request message for
                [Documents.ReloadDocument][google.cloud.dialogflow.v2.Documents.ReloadDocument].
            name (:class:`str`):
                Required. The name of the document to reload. Format:
                ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            content_uri (:class:`str`):
                Optional. The path of gcs source file for reloading
                document content. For now, only gcs uri is supported.

                For documents stored in Google Cloud Storage, these URIs
                must have the form ``gs://<bucket-name>/<object-name>``.

                This corresponds to the ``content_uri`` field
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
                :class:`google.cloud.dialogflow_v2.types.Document` A
                knowledge document to be used by a
                [KnowledgeBase][google.cloud.dialogflow.v2.KnowledgeBase].

                   For more information, see the [knowledge base
                   guide](\ https://cloud.google.com/dialogflow/docs/how/knowledge-bases).

                   Note: The projects.agent.knowledgeBases.documents
                   resource is deprecated; only use
                   projects.knowledgeBases.documents.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, content_uri])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document.ReloadDocumentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if content_uri is not None:
            request.content_uri = content_uri

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.reload_document,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document.Document,
            metadata_type=document.KnowledgeOperationMetadata,
        )

        # Done; return the response.
        return response

    async def export_document(
        self,
        request: Union[document.ExportDocumentRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports a smart messaging candidate document into the specified
        destination.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``:
           [KnowledgeOperationMetadata][google.cloud.dialogflow.v2.KnowledgeOperationMetadata]
        -  ``response``: [Document][google.cloud.dialogflow.v2.Document]


        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_export_document():
                # Create a client
                client = dialogflow_v2.DocumentsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.ExportDocumentRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.export_document(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.ExportDocumentRequest, dict]):
                The request object. Request message for
                [Documents.ExportDocument][google.cloud.dialogflow.v2.Documents.ExportDocument].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dialogflow_v2.types.Document` A
                knowledge document to be used by a
                [KnowledgeBase][google.cloud.dialogflow.v2.KnowledgeBase].

                   For more information, see the [knowledge base
                   guide](\ https://cloud.google.com/dialogflow/docs/how/knowledge-bases).

                   Note: The projects.agent.knowledgeBases.documents
                   resource is deprecated; only use
                   projects.knowledgeBases.documents.

        """
        # Create or coerce a protobuf request object.
        request = document.ExportDocumentRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.export_document,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document.Document,
            metadata_type=document.KnowledgeOperationMetadata,
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


__all__ = ("DocumentsAsyncClient",)
