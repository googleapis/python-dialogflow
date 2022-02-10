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

from google.cloud.dialogflow_v2.services.contexts import pagers
from google.cloud.dialogflow_v2.types import context
from google.cloud.dialogflow_v2.types import context as gcd_context
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import struct_pb2  # type: ignore
from .transports.base import ContextsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ContextsGrpcAsyncIOTransport
from .client import ContextsClient


class ContextsAsyncClient:
    """Service for managing [Contexts][google.cloud.dialogflow.v2.Context]."""

    _client: ContextsClient

    DEFAULT_ENDPOINT = ContextsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ContextsClient.DEFAULT_MTLS_ENDPOINT

    context_path = staticmethod(ContextsClient.context_path)
    parse_context_path = staticmethod(ContextsClient.parse_context_path)
    common_billing_account_path = staticmethod(
        ContextsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ContextsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ContextsClient.common_folder_path)
    parse_common_folder_path = staticmethod(ContextsClient.parse_common_folder_path)
    common_organization_path = staticmethod(ContextsClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        ContextsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ContextsClient.common_project_path)
    parse_common_project_path = staticmethod(ContextsClient.parse_common_project_path)
    common_location_path = staticmethod(ContextsClient.common_location_path)
    parse_common_location_path = staticmethod(ContextsClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ContextsAsyncClient: The constructed client.
        """
        return ContextsClient.from_service_account_info.__func__(ContextsAsyncClient, info, *args, **kwargs)  # type: ignore

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
            ContextsAsyncClient: The constructed client.
        """
        return ContextsClient.from_service_account_file.__func__(ContextsAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return ContextsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ContextsTransport:
        """Returns the transport used by the client instance.

        Returns:
            ContextsTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ContextsClient).get_transport_class, type(ContextsClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, ContextsTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the contexts client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ContextsTransport]): The
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
        self._client = ContextsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_contexts(
        self,
        request: Union[context.ListContextsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListContextsAsyncPager:
        r"""Returns the list of all contexts in the specified
        session.


        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_list_contexts():
                # Create a client
                client = dialogflow_v2.ContextsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.ListContextsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_contexts(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.ListContextsRequest, dict]):
                The request object. The request message for
                [Contexts.ListContexts][google.cloud.dialogflow.v2.Contexts.ListContexts].
            parent (:class:`str`):
                Required. The session to list all contexts from. Format:
                ``projects/<Project ID>/agent/sessions/<Session ID>`` or
                ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>``.
                If ``Environment ID`` is not specified, we assume
                default 'draft' environment. If ``User ID`` is not
                specified, we assume default '-' user.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.services.contexts.pagers.ListContextsAsyncPager:
                The response message for
                [Contexts.ListContexts][google.cloud.dialogflow.v2.Contexts.ListContexts].

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

        request = context.ListContextsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_contexts,
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
        response = pagers.ListContextsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_context(
        self,
        request: Union[context.GetContextRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> context.Context:
        r"""Retrieves the specified context.

        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_get_context():
                # Create a client
                client = dialogflow_v2.ContextsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.GetContextRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_context(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.GetContextRequest, dict]):
                The request object. The request message for
                [Contexts.GetContext][google.cloud.dialogflow.v2.Contexts.GetContext].
            name (:class:`str`):
                Required. The name of the context. Format:
                ``projects/<Project ID>/agent/sessions/<Session ID>/contexts/<Context ID>``
                or
                ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>/contexts/<Context ID>``.
                If ``Environment ID`` is not specified, we assume
                default 'draft' environment. If ``User ID`` is not
                specified, we assume default '-' user.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.Context:
                Dialogflow contexts are similar to natural language context. If a person says
                   to you "they are orange", you need context in order
                   to understand what "they" is referring to. Similarly,
                   for Dialogflow to handle an end-user expression like
                   that, it needs to be provided with context in order
                   to correctly match an intent.

                   Using contexts, you can control the flow of a
                   conversation. You can configure contexts for an
                   intent by setting input and output contexts, which
                   are identified by string names. When an intent is
                   matched, any configured output contexts for that
                   intent become active. While any contexts are active,
                   Dialogflow is more likely to match intents that are
                   configured with input contexts that correspond to the
                   currently active contexts.

                   For more information about context, see the [Contexts
                   guide](\ https://cloud.google.com/dialogflow/docs/contexts-overview).

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

        request = context.GetContextRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_context,
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

    async def create_context(
        self,
        request: Union[gcd_context.CreateContextRequest, dict] = None,
        *,
        parent: str = None,
        context: gcd_context.Context = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_context.Context:
        r"""Creates a context.
        If the specified context already exists, overrides the
        context.


        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_create_context():
                # Create a client
                client = dialogflow_v2.ContextsClient()

                # Initialize request argument(s)
                context = dialogflow_v2.Context()
                context.name = "name_value"

                request = dialogflow_v2.CreateContextRequest(
                    parent="parent_value",
                    context=context,
                )

                # Make the request
                response = client.create_context(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.CreateContextRequest, dict]):
                The request object. The request message for
                [Contexts.CreateContext][google.cloud.dialogflow.v2.Contexts.CreateContext].
            parent (:class:`str`):
                Required. The session to create a context for. Format:
                ``projects/<Project ID>/agent/sessions/<Session ID>`` or
                ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>``.
                If ``Environment ID`` is not specified, we assume
                default 'draft' environment. If ``User ID`` is not
                specified, we assume default '-' user.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            context (:class:`google.cloud.dialogflow_v2.types.Context`):
                Required. The context to create.
                This corresponds to the ``context`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.Context:
                Dialogflow contexts are similar to natural language context. If a person says
                   to you "they are orange", you need context in order
                   to understand what "they" is referring to. Similarly,
                   for Dialogflow to handle an end-user expression like
                   that, it needs to be provided with context in order
                   to correctly match an intent.

                   Using contexts, you can control the flow of a
                   conversation. You can configure contexts for an
                   intent by setting input and output contexts, which
                   are identified by string names. When an intent is
                   matched, any configured output contexts for that
                   intent become active. While any contexts are active,
                   Dialogflow is more likely to match intents that are
                   configured with input contexts that correspond to the
                   currently active contexts.

                   For more information about context, see the [Contexts
                   guide](\ https://cloud.google.com/dialogflow/docs/contexts-overview).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, context])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_context.CreateContextRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if context is not None:
            request.context = context

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_context,
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

        # Done; return the response.
        return response

    async def update_context(
        self,
        request: Union[gcd_context.UpdateContextRequest, dict] = None,
        *,
        context: gcd_context.Context = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_context.Context:
        r"""Updates the specified context.

        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_update_context():
                # Create a client
                client = dialogflow_v2.ContextsClient()

                # Initialize request argument(s)
                context = dialogflow_v2.Context()
                context.name = "name_value"

                request = dialogflow_v2.UpdateContextRequest(
                    context=context,
                )

                # Make the request
                response = client.update_context(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.UpdateContextRequest, dict]):
                The request object. The request message for
                [Contexts.UpdateContext][google.cloud.dialogflow.v2.Contexts.UpdateContext].
            context (:class:`google.cloud.dialogflow_v2.types.Context`):
                Required. The context to update.
                This corresponds to the ``context`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The mask to control which
                fields get updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.Context:
                Dialogflow contexts are similar to natural language context. If a person says
                   to you "they are orange", you need context in order
                   to understand what "they" is referring to. Similarly,
                   for Dialogflow to handle an end-user expression like
                   that, it needs to be provided with context in order
                   to correctly match an intent.

                   Using contexts, you can control the flow of a
                   conversation. You can configure contexts for an
                   intent by setting input and output contexts, which
                   are identified by string names. When an intent is
                   matched, any configured output contexts for that
                   intent become active. While any contexts are active,
                   Dialogflow is more likely to match intents that are
                   configured with input contexts that correspond to the
                   currently active contexts.

                   For more information about context, see the [Contexts
                   guide](\ https://cloud.google.com/dialogflow/docs/contexts-overview).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([context, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_context.UpdateContextRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if context is not None:
            request.context = context
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_context,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("context.name", request.context.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def delete_context(
        self,
        request: Union[context.DeleteContextRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the specified context.

        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_delete_context():
                # Create a client
                client = dialogflow_v2.ContextsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.DeleteContextRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_context(request=request)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.DeleteContextRequest, dict]):
                The request object. The request message for
                [Contexts.DeleteContext][google.cloud.dialogflow.v2.Contexts.DeleteContext].
            name (:class:`str`):
                Required. The name of the context to delete. Format:
                ``projects/<Project ID>/agent/sessions/<Session ID>/contexts/<Context ID>``
                or
                ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>/contexts/<Context ID>``.
                If ``Environment ID`` is not specified, we assume
                default 'draft' environment. If ``User ID`` is not
                specified, we assume default '-' user.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
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

        request = context.DeleteContextRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_context,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    async def delete_all_contexts(
        self,
        request: Union[context.DeleteAllContextsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes all active contexts in the specified session.

        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_delete_all_contexts():
                # Create a client
                client = dialogflow_v2.ContextsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.DeleteAllContextsRequest(
                    parent="parent_value",
                )

                # Make the request
                client.delete_all_contexts(request=request)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.DeleteAllContextsRequest, dict]):
                The request object. The request message for
                [Contexts.DeleteAllContexts][google.cloud.dialogflow.v2.Contexts.DeleteAllContexts].
            parent (:class:`str`):
                Required. The name of the session to delete all contexts
                from. Format:
                ``projects/<Project ID>/agent/sessions/<Session ID>`` or
                ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>``.
                If ``Environment ID`` is not specified we assume default
                'draft' environment. If ``User ID`` is not specified, we
                assume default '-' user.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
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

        request = context.DeleteAllContextsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_all_contexts,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

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


__all__ = ("ContextsAsyncClient",)
