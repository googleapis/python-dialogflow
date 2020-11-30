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
from distutils import util
import os
import re
from typing import Callable, Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core import client_options as client_options_lib  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.dialogflow_v2beta1.services.documents import pagers
from google.cloud.dialogflow_v2beta1.types import document
from google.cloud.dialogflow_v2beta1.types import document as gcd_document
from google.cloud.dialogflow_v2beta1.types import gcs
from google.protobuf import empty_pb2 as empty  # type: ignore
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore

from .transports.base import DocumentsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import DocumentsGrpcTransport
from .transports.grpc_asyncio import DocumentsGrpcAsyncIOTransport


class DocumentsClientMeta(type):
    """Metaclass for the Documents client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[DocumentsTransport]]
    _transport_registry["grpc"] = DocumentsGrpcTransport
    _transport_registry["grpc_asyncio"] = DocumentsGrpcAsyncIOTransport

    def get_transport_class(cls, label: str = None,) -> Type[DocumentsTransport]:
        """Return an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class DocumentsClient(metaclass=DocumentsClientMeta):
    """Service for managing knowledge
    [Documents][google.cloud.dialogflow.v2beta1.Document].
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Convert api endpoint to mTLS endpoint.
        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "dialogflow.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

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
            {@api.name}: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> DocumentsTransport:
        """Return the transport used by the client instance.

        Returns:
            DocumentsTransport: The transport used by the client instance.
        """
        return self._transport

    @staticmethod
    def document_path(project: str, knowledge_base: str, document: str,) -> str:
        """Return a fully-qualified document string."""
        return "projects/{project}/knowledgeBases/{knowledge_base}/documents/{document}".format(
            project=project, knowledge_base=knowledge_base, document=document,
        )

    @staticmethod
    def parse_document_path(path: str) -> Dict[str, str]:
        """Parse a document path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/knowledgeBases/(?P<knowledge_base>.+?)/documents/(?P<document>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(billing_account: str,) -> str:
        """Return a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str,) -> str:
        """Return a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder,)

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str,) -> str:
        """Return a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization,)

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str,) -> str:
        """Return a fully-qualified project string."""
        return "projects/{project}".format(project=project,)

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str,) -> str:
        """Return a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project, location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    def __init__(
        self,
        *,
        credentials: Optional[credentials.Credentials] = None,
        transport: Union[str, DocumentsTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the documents client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DocumentsTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (client_options_lib.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
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
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        # Create SSL credentials for mutual TLS if needed.
        use_client_cert = bool(
            util.strtobool(os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false"))
        )

        ssl_credentials = None
        is_mtls = False
        if use_client_cert:
            if client_options.client_cert_source:
                import grpc  # type: ignore

                cert, key = client_options.client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
                is_mtls = True
            else:
                creds = SslCredentials()
                is_mtls = creds.is_mtls
                ssl_credentials = creds.ssl_credentials if is_mtls else None

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        else:
            use_mtls_env = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
            if use_mtls_env == "never":
                api_endpoint = self.DEFAULT_ENDPOINT
            elif use_mtls_env == "always":
                api_endpoint = self.DEFAULT_MTLS_ENDPOINT
            elif use_mtls_env == "auto":
                api_endpoint = (
                    self.DEFAULT_MTLS_ENDPOINT if is_mtls else self.DEFAULT_ENDPOINT
                )
            else:
                raise MutualTLSChannelError(
                    "Unsupported GOOGLE_API_USE_MTLS_ENDPOINT value. Accepted values: never, auto, always"
                )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, DocumentsTransport):
            # transport is a DocumentsTransport instance.
            if credentials or client_options.credentials_file:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its scopes directly."
                )
            self._transport = transport
        else:
            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                ssl_channel_credentials=ssl_credentials,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
            )

    def list_documents(
        self,
        request: document.ListDocumentsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListDocumentsPager:
        r"""Returns the list of all documents of the knowledge base.

        Note: The ``projects.agent.knowledgeBases.documents`` resource
        is deprecated; only use ``projects.knowledgeBases.documents``.

        Args:
            request (:class:`~.document.ListDocumentsRequest`):
                The request object. Request message for
                [Documents.ListDocuments][google.cloud.dialogflow.v2beta1.Documents.ListDocuments].
            parent (:class:`str`):
                Required. The knowledge base to list all documents for.
                Format:
                ``projects/<Project ID>/knowledgeBases/<Knowledge Base ID>``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListDocumentsPager:
                Response message for
                [Documents.ListDocuments][google.cloud.dialogflow.v2beta1.Documents.ListDocuments].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a document.ListDocumentsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, document.ListDocumentsRequest):
            request = document.ListDocumentsRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_documents]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDocumentsPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_document(
        self,
        request: document.GetDocumentRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> document.Document:
        r"""Retrieves the specified document.

        Note: The ``projects.agent.knowledgeBases.documents`` resource
        is deprecated; only use ``projects.knowledgeBases.documents``.

        Args:
            request (:class:`~.document.GetDocumentRequest`):
                The request object. Request message for
                [Documents.GetDocument][google.cloud.dialogflow.v2beta1.Documents.GetDocument].
            name (:class:`str`):
                Required. The name of the document to retrieve. Format
                ``projects/<Project ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.document.Document:
                A knowledge document to be used by a
                [KnowledgeBase][google.cloud.dialogflow.v2beta1.KnowledgeBase].

                For more information, see the `knowledge base
                guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

                Note: The ``projects.agent.knowledgeBases.documents``
                resource is deprecated; only use
                ``projects.knowledgeBases.documents``.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a document.GetDocumentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, document.GetDocumentRequest):
            request = document.GetDocumentRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_document]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def create_document(
        self,
        request: gcd_document.CreateDocumentRequest = None,
        *,
        parent: str = None,
        document: gcd_document.Document = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Creates a new document.

        Note: The ``projects.agent.knowledgeBases.documents`` resource
        is deprecated; only use ``projects.knowledgeBases.documents``.

        Args:
            request (:class:`~.gcd_document.CreateDocumentRequest`):
                The request object. Request message for
                [Documents.CreateDocument][google.cloud.dialogflow.v2beta1.Documents.CreateDocument].
            parent (:class:`str`):
                Required. The knowledge base to create a document for.
                Format:
                ``projects/<Project ID>/knowledgeBases/<Knowledge Base ID>``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            document (:class:`~.gcd_document.Document`):
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
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.gcd_document.Document``: A knowledge document
                to be used by a
                [KnowledgeBase][google.cloud.dialogflow.v2beta1.KnowledgeBase].

                For more information, see the `knowledge base
                guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

                Note: The ``projects.agent.knowledgeBases.documents``
                resource is deprecated; only use
                ``projects.knowledgeBases.documents``.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, document])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a gcd_document.CreateDocumentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, gcd_document.CreateDocumentRequest):
            request = gcd_document.CreateDocumentRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if parent is not None:
                request.parent = parent
            if document is not None:
                request.document = document

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_document]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gcd_document.Document,
            metadata_type=gcd_document.KnowledgeOperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_document(
        self,
        request: document.DeleteDocumentRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Deletes the specified document.

        Note: The ``projects.agent.knowledgeBases.documents`` resource
        is deprecated; only use ``projects.knowledgeBases.documents``.

        Args:
            request (:class:`~.document.DeleteDocumentRequest`):
                The request object. Request message for
                [Documents.DeleteDocument][google.cloud.dialogflow.v2beta1.Documents.DeleteDocument].
            name (:class:`str`):
                Required. The name of the document to delete. Format:
                ``projects/<Project ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.empty.Empty``: A generic empty message that
                you can re-use to avoid defining duplicated empty
                messages in your APIs. A typical example is to use it as
                the request or the response type of an API method. For
                instance:

                ::

                    service Foo {
                      rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);
                    }

                The JSON representation for ``Empty`` is empty JSON
                object ``{}``.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a document.DeleteDocumentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, document.DeleteDocumentRequest):
            request = document.DeleteDocumentRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_document]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty.Empty,
            metadata_type=document.KnowledgeOperationMetadata,
        )

        # Done; return the response.
        return response

    def update_document(
        self,
        request: gcd_document.UpdateDocumentRequest = None,
        *,
        document: gcd_document.Document = None,
        update_mask: field_mask.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Updates the specified document.

        Note: The ``projects.agent.knowledgeBases.documents`` resource
        is deprecated; only use ``projects.knowledgeBases.documents``.

        Args:
            request (:class:`~.gcd_document.UpdateDocumentRequest`):
                The request object. Request message for
                [Documents.UpdateDocument][google.cloud.dialogflow.v2beta1.Documents.UpdateDocument].
            document (:class:`~.gcd_document.Document`):
                Required. The document to update.
                This corresponds to the ``document`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`~.field_mask.FieldMask`):
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
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.gcd_document.Document``: A knowledge document
                to be used by a
                [KnowledgeBase][google.cloud.dialogflow.v2beta1.KnowledgeBase].

                For more information, see the `knowledge base
                guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

                Note: The ``projects.agent.knowledgeBases.documents``
                resource is deprecated; only use
                ``projects.knowledgeBases.documents``.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([document, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a gcd_document.UpdateDocumentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, gcd_document.UpdateDocumentRequest):
            request = gcd_document.UpdateDocumentRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if document is not None:
                request.document = document
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_document]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("document.name", request.document.name),)
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gcd_document.Document,
            metadata_type=gcd_document.KnowledgeOperationMetadata,
        )

        # Done; return the response.
        return response

    def reload_document(
        self,
        request: document.ReloadDocumentRequest = None,
        *,
        name: str = None,
        gcs_source: gcs.GcsSource = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Reloads the specified document from its specified source,
        content_uri or content. The previously loaded content of the
        document will be deleted. Note: Even when the content of the
        document has not changed, there still may be side effects
        because of internal implementation changes.

        Note: The ``projects.agent.knowledgeBases.documents`` resource
        is deprecated; only use ``projects.knowledgeBases.documents``.

        Args:
            request (:class:`~.document.ReloadDocumentRequest`):
                The request object. Request message for
                [Documents.ReloadDocument][google.cloud.dialogflow.v2beta1.Documents.ReloadDocument].
            name (:class:`str`):
                Required. The name of the document to reload. Format:
                ``projects/<Project ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            gcs_source (:class:`~.gcs.GcsSource`):
                The path for a Cloud Storage source
                file for reloading document content. If
                not provided, the Document's existing
                source will be reloaded.
                This corresponds to the ``gcs_source`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.document.Document``: A knowledge document to
                be used by a
                [KnowledgeBase][google.cloud.dialogflow.v2beta1.KnowledgeBase].

                For more information, see the `knowledge base
                guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

                Note: The ``projects.agent.knowledgeBases.documents``
                resource is deprecated; only use
                ``projects.knowledgeBases.documents``.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, gcs_source])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a document.ReloadDocumentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, document.ReloadDocumentRequest):
            request = document.ReloadDocumentRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name
            if gcs_source is not None:
                request.gcs_source = gcs_source

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.reload_document]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            document.Document,
            metadata_type=document.KnowledgeOperationMetadata,
        )

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-dialogflow",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("DocumentsClient",)
