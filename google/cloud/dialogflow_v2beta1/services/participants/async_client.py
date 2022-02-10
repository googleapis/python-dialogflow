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
import warnings

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

from google.cloud.dialogflow_v2beta1.services.participants import pagers
from google.cloud.dialogflow_v2beta1.types import participant
from google.cloud.dialogflow_v2beta1.types import participant as gcd_participant
from google.cloud.dialogflow_v2beta1.types import session
from google.protobuf import field_mask_pb2  # type: ignore
from .transports.base import ParticipantsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ParticipantsGrpcAsyncIOTransport
from .client import ParticipantsClient


class ParticipantsAsyncClient:
    """Service for managing
    [Participants][google.cloud.dialogflow.v2beta1.Participant].
    """

    _client: ParticipantsClient

    DEFAULT_ENDPOINT = ParticipantsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ParticipantsClient.DEFAULT_MTLS_ENDPOINT

    answer_record_path = staticmethod(ParticipantsClient.answer_record_path)
    parse_answer_record_path = staticmethod(ParticipantsClient.parse_answer_record_path)
    context_path = staticmethod(ParticipantsClient.context_path)
    parse_context_path = staticmethod(ParticipantsClient.parse_context_path)
    document_path = staticmethod(ParticipantsClient.document_path)
    parse_document_path = staticmethod(ParticipantsClient.parse_document_path)
    intent_path = staticmethod(ParticipantsClient.intent_path)
    parse_intent_path = staticmethod(ParticipantsClient.parse_intent_path)
    message_path = staticmethod(ParticipantsClient.message_path)
    parse_message_path = staticmethod(ParticipantsClient.parse_message_path)
    participant_path = staticmethod(ParticipantsClient.participant_path)
    parse_participant_path = staticmethod(ParticipantsClient.parse_participant_path)
    session_entity_type_path = staticmethod(ParticipantsClient.session_entity_type_path)
    parse_session_entity_type_path = staticmethod(
        ParticipantsClient.parse_session_entity_type_path
    )
    common_billing_account_path = staticmethod(
        ParticipantsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ParticipantsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ParticipantsClient.common_folder_path)
    parse_common_folder_path = staticmethod(ParticipantsClient.parse_common_folder_path)
    common_organization_path = staticmethod(ParticipantsClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        ParticipantsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ParticipantsClient.common_project_path)
    parse_common_project_path = staticmethod(
        ParticipantsClient.parse_common_project_path
    )
    common_location_path = staticmethod(ParticipantsClient.common_location_path)
    parse_common_location_path = staticmethod(
        ParticipantsClient.parse_common_location_path
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
            ParticipantsAsyncClient: The constructed client.
        """
        return ParticipantsClient.from_service_account_info.__func__(ParticipantsAsyncClient, info, *args, **kwargs)  # type: ignore

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
            ParticipantsAsyncClient: The constructed client.
        """
        return ParticipantsClient.from_service_account_file.__func__(ParticipantsAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return ParticipantsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ParticipantsTransport:
        """Returns the transport used by the client instance.

        Returns:
            ParticipantsTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ParticipantsClient).get_transport_class, type(ParticipantsClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, ParticipantsTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the participants client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ParticipantsTransport]): The
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
        self._client = ParticipantsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_participant(
        self,
        request: Union[gcd_participant.CreateParticipantRequest, dict] = None,
        *,
        parent: str = None,
        participant: gcd_participant.Participant = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_participant.Participant:
        r"""Creates a new participant in a conversation.

        .. code-block::

            from google.cloud import dialogflow_v2beta1

            def sample_create_participant():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.CreateParticipantRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_participant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.CreateParticipantRequest, dict]):
                The request object. The request message for
                [Participants.CreateParticipant][google.cloud.dialogflow.v2beta1.Participants.CreateParticipant].
            parent (:class:`str`):
                Required. Resource identifier of the conversation adding
                the participant. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            participant (:class:`google.cloud.dialogflow_v2beta1.types.Participant`):
                Required. The participant to create.
                This corresponds to the ``participant`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.Participant:
                Represents a conversation participant
                (human agent, virtual agent, end-user).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, participant])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_participant.CreateParticipantRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if participant is not None:
            request.participant = participant

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_participant,
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

    async def get_participant(
        self,
        request: Union[participant.GetParticipantRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> participant.Participant:
        r"""Retrieves a conversation participant.

        .. code-block::

            from google.cloud import dialogflow_v2beta1

            def sample_get_participant():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.GetParticipantRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_participant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.GetParticipantRequest, dict]):
                The request object. The request message for
                [Participants.GetParticipant][google.cloud.dialogflow.v2beta1.Participants.GetParticipant].
            name (:class:`str`):
                Required. The name of the participant. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.Participant:
                Represents a conversation participant
                (human agent, virtual agent, end-user).

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

        request = participant.GetParticipantRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_participant,
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

    async def list_participants(
        self,
        request: Union[participant.ListParticipantsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListParticipantsAsyncPager:
        r"""Returns the list of all participants in the specified
        conversation.


        .. code-block::

            from google.cloud import dialogflow_v2beta1

            def sample_list_participants():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListParticipantsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_participants(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.ListParticipantsRequest, dict]):
                The request object. The request message for
                [Participants.ListParticipants][google.cloud.dialogflow.v2beta1.Participants.ListParticipants].
            parent (:class:`str`):
                Required. The conversation to list all participants
                from. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.services.participants.pagers.ListParticipantsAsyncPager:
                The response message for
                [Participants.ListParticipants][google.cloud.dialogflow.v2beta1.Participants.ListParticipants].

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

        request = participant.ListParticipantsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_participants,
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
        response = pagers.ListParticipantsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_participant(
        self,
        request: Union[gcd_participant.UpdateParticipantRequest, dict] = None,
        *,
        participant: gcd_participant.Participant = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_participant.Participant:
        r"""Updates the specified participant.

        .. code-block::

            from google.cloud import dialogflow_v2beta1

            def sample_update_participant():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.UpdateParticipantRequest(
                )

                # Make the request
                response = client.update_participant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.UpdateParticipantRequest, dict]):
                The request object. The request message for
                [Participants.UpdateParticipant][google.cloud.dialogflow.v2beta1.Participants.UpdateParticipant].
            participant (:class:`google.cloud.dialogflow_v2beta1.types.Participant`):
                Required. The participant to update.
                This corresponds to the ``participant`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The mask to specify which
                fields to update.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.Participant:
                Represents a conversation participant
                (human agent, virtual agent, end-user).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([participant, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_participant.UpdateParticipantRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if participant is not None:
            request.participant = participant
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_participant,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("participant.name", request.participant.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def analyze_content(
        self,
        request: Union[gcd_participant.AnalyzeContentRequest, dict] = None,
        *,
        participant: str = None,
        text_input: session.TextInput = None,
        event_input: session.EventInput = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_participant.AnalyzeContentResponse:
        r"""Adds a text (chat, for example), or audio (phone recording, for
        example) message from a participant into the conversation.

        Note: Always use agent versions for production traffic sent to
        virtual agents. See `Versions and
        environments <https://cloud.google.com/dialogflow/es/docs/agents-versions>`__.


        .. code-block::

            from google.cloud import dialogflow_v2beta1

            def sample_analyze_content():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.AnalyzeContentRequest(
                    participant="participant_value",
                )

                # Make the request
                response = client.analyze_content(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.AnalyzeContentRequest, dict]):
                The request object. The request message for
                [Participants.AnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent].
            participant (:class:`str`):
                Required. The name of the participant this text comes
                from. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.

                This corresponds to the ``participant`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            text_input (:class:`google.cloud.dialogflow_v2beta1.types.TextInput`):
                The natural language text to be
                processed.

                This corresponds to the ``text_input`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            event_input (:class:`google.cloud.dialogflow_v2beta1.types.EventInput`):
                An input event to send to Dialogflow.
                This corresponds to the ``event_input`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.AnalyzeContentResponse:
                The response message for
                [Participants.AnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([participant, text_input, event_input])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_participant.AnalyzeContentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if participant is not None:
            request.participant = participant
        if text_input is not None:
            request.text_input = text_input
        if event_input is not None:
            request.event_input = event_input

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.analyze_content,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=220.0,
            ),
            default_timeout=220.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("participant", request.participant),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def suggest_articles(
        self,
        request: Union[participant.SuggestArticlesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> participant.SuggestArticlesResponse:
        r"""Gets suggested articles for a participant based on specific
        historical messages.

        Note that
        [ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions]
        will only list the auto-generated suggestions, while
        [CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion]
        will try to compile suggestion based on the provided
        conversation context in the real time.


        .. code-block::

            from google.cloud import dialogflow_v2beta1

            def sample_suggest_articles():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SuggestArticlesRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.suggest_articles(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.SuggestArticlesRequest, dict]):
                The request object. The request message for
                [Participants.SuggestArticles][google.cloud.dialogflow.v2beta1.Participants.SuggestArticles].
            parent (:class:`str`):
                Required. The name of the participant to fetch
                suggestion for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.SuggestArticlesResponse:
                The response message for
                [Participants.SuggestArticles][google.cloud.dialogflow.v2beta1.Participants.SuggestArticles].

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

        request = participant.SuggestArticlesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.suggest_articles,
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

    async def suggest_faq_answers(
        self,
        request: Union[participant.SuggestFaqAnswersRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> participant.SuggestFaqAnswersResponse:
        r"""Gets suggested faq answers for a participant based on
        specific historical messages.


        .. code-block::

            from google.cloud import dialogflow_v2beta1

            def sample_suggest_faq_answers():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SuggestFaqAnswersRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.suggest_faq_answers(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersRequest, dict]):
                The request object. The request message for
                [Participants.SuggestFaqAnswers][google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers].
            parent (:class:`str`):
                Required. The name of the participant to fetch
                suggestion for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersResponse:
                The request message for
                [Participants.SuggestFaqAnswers][google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers].

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

        request = participant.SuggestFaqAnswersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.suggest_faq_answers,
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

    async def suggest_smart_replies(
        self,
        request: Union[participant.SuggestSmartRepliesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> participant.SuggestSmartRepliesResponse:
        r"""Gets smart replies for a participant based on
        specific historical messages.


        .. code-block::

            from google.cloud import dialogflow_v2beta1

            def sample_suggest_smart_replies():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SuggestSmartRepliesRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.suggest_smart_replies(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesRequest, dict]):
                The request object. The request message for
                [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2beta1.Participants.SuggestSmartReplies].
            parent (:class:`str`):
                Required. The name of the participant to fetch
                suggestion for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesResponse:
                The response message for
                [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2beta1.Participants.SuggestSmartReplies].

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

        request = participant.SuggestSmartRepliesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.suggest_smart_replies,
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

    async def list_suggestions(
        self,
        request: Union[participant.ListSuggestionsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListSuggestionsAsyncPager:
        r"""Deprecated: Use inline suggestion, event based suggestion or
        Suggestion\* API instead. See
        [HumanAgentAssistantConfig.name][google.cloud.dialogflow.v2beta1.HumanAgentAssistantConfig.name]
        for more details. Removal Date: 2020-09-01.

        Retrieves suggestions for live agents.

        This method should be used by human agent client software to
        fetch auto generated suggestions in real-time, while the
        conversation with an end user is in progress. The functionality
        is implemented in terms of the `list
        pagination <https://cloud.google.com/apis/design/design_patterns#list_pagination>`__
        design pattern. The client app should use the
        ``next_page_token`` field to fetch the next batch of
        suggestions. ``suggestions`` are sorted by ``create_time`` in
        descending order. To fetch latest suggestion, just set
        ``page_size`` to 1. To fetch new suggestions without
        duplication, send request with filter
        ``create_time_epoch_microseconds > [first item's create_time of previous request]``
        and empty page_token.


        .. code-block::

            from google.cloud import dialogflow_v2beta1

            def sample_list_suggestions():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListSuggestionsRequest(
                )

                # Make the request
                page_result = client.list_suggestions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.ListSuggestionsRequest, dict]):
                The request object. The request message for
                [Participants.ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.services.participants.pagers.ListSuggestionsAsyncPager:
                The response message for
                [Participants.ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "ParticipantsAsyncClient.list_suggestions is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        request = participant.ListSuggestionsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_suggestions,
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
        response = pagers.ListSuggestionsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def compile_suggestion(
        self,
        request: Union[participant.CompileSuggestionRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> participant.CompileSuggestionResponse:
        r"""Deprecated. use
        [SuggestArticles][google.cloud.dialogflow.v2beta1.Participants.SuggestArticles]
        and
        [SuggestFaqAnswers][google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers]
        instead.

        Gets suggestions for a participant based on specific historical
        messages.

        Note that
        [ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions]
        will only list the auto-generated suggestions, while
        [CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion]
        will try to compile suggestion based on the provided
        conversation context in the real time.


        .. code-block::

            from google.cloud import dialogflow_v2beta1

            def sample_compile_suggestion():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.CompileSuggestionRequest(
                )

                # Make the request
                response = client.compile_suggestion(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.CompileSuggestionRequest, dict]):
                The request object. The request message for
                [Participants.CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.CompileSuggestionResponse:
                The response message for
                [Participants.CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion].

        """
        warnings.warn(
            "ParticipantsAsyncClient.compile_suggestion is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        request = participant.CompileSuggestionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.compile_suggestion,
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


__all__ = ("ParticipantsAsyncClient",)
