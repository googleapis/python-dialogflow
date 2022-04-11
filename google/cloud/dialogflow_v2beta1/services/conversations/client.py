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
import os
import re
from typing import Dict, Mapping, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.dialogflow_v2beta1.services.conversations import pagers
from google.cloud.dialogflow_v2beta1.types import conversation
from google.cloud.dialogflow_v2beta1.types import conversation as gcd_conversation
from google.cloud.dialogflow_v2beta1.types import participant
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import ConversationsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import ConversationsGrpcTransport
from .transports.grpc_asyncio import ConversationsGrpcAsyncIOTransport


class ConversationsClientMeta(type):
    """Metaclass for the Conversations client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[ConversationsTransport]]
    _transport_registry["grpc"] = ConversationsGrpcTransport
    _transport_registry["grpc_asyncio"] = ConversationsGrpcAsyncIOTransport

    def get_transport_class(
        cls,
        label: str = None,
    ) -> Type[ConversationsTransport]:
        """Returns an appropriate transport class.

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


class ConversationsClient(metaclass=ConversationsClientMeta):
    """Service for managing
    [Conversations][google.cloud.dialogflow.v2beta1.Conversation].
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

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
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ConversationsClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

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
            ConversationsClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> ConversationsTransport:
        """Returns the transport used by the client instance.

        Returns:
            ConversationsTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def conversation_path(
        project: str,
        conversation: str,
    ) -> str:
        """Returns a fully-qualified conversation string."""
        return "projects/{project}/conversations/{conversation}".format(
            project=project,
            conversation=conversation,
        )

    @staticmethod
    def parse_conversation_path(path: str) -> Dict[str, str]:
        """Parses a conversation path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/conversations/(?P<conversation>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def conversation_profile_path(
        project: str,
        conversation_profile: str,
    ) -> str:
        """Returns a fully-qualified conversation_profile string."""
        return "projects/{project}/conversationProfiles/{conversation_profile}".format(
            project=project,
            conversation_profile=conversation_profile,
        )

    @staticmethod
    def parse_conversation_profile_path(path: str) -> Dict[str, str]:
        """Parses a conversation_profile path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/conversationProfiles/(?P<conversation_profile>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def message_path(
        project: str,
        conversation: str,
        message: str,
    ) -> str:
        """Returns a fully-qualified message string."""
        return (
            "projects/{project}/conversations/{conversation}/messages/{message}".format(
                project=project,
                conversation=conversation,
                message=message,
            )
        )

    @staticmethod
    def parse_message_path(path: str) -> Dict[str, str]:
        """Parses a message path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/conversations/(?P<conversation>.+?)/messages/(?P<message>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(
        billing_account: str,
    ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(
            folder=folder,
        )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(
            project=project,
        )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
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
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
            )
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, ConversationsTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the conversations client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ConversationsTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
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

        api_endpoint, client_cert_source_func = self.get_mtls_endpoint_and_cert_source(
            client_options
        )

        api_key_value = getattr(client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, ConversationsTransport):
            # transport is a ConversationsTransport instance.
            if credentials or client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
            )

    def create_conversation(
        self,
        request: Union[gcd_conversation.CreateConversationRequest, dict] = None,
        *,
        parent: str = None,
        conversation: gcd_conversation.Conversation = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_conversation.Conversation:
        r"""Creates a new conversation. Conversations are auto-completed
        after 24 hours.

        Conversation Lifecycle: There are two stages during a
        conversation: Automated Agent Stage and Assist Stage.

        For Automated Agent Stage, there will be a dialogflow agent
        responding to user queries.

        For Assist Stage, there's no dialogflow agent responding to user
        queries. But we will provide suggestions which are generated
        from conversation.

        If
        [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile]
        is configured for a dialogflow agent, conversation will start
        from ``Automated Agent Stage``, otherwise, it will start from
        ``Assist Stage``. And during ``Automated Agent Stage``, once an
        [Intent][google.cloud.dialogflow.v2beta1.Intent] with
        [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff]
        is triggered, conversation will transfer to Assist Stage.

        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_create_conversation():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                conversation = dialogflow_v2beta1.Conversation()
                conversation.conversation_profile = "conversation_profile_value"

                request = dialogflow_v2beta1.CreateConversationRequest(
                    parent="parent_value",
                    conversation=conversation,
                )

                # Make the request
                response = client.create_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.CreateConversationRequest, dict]):
                The request object. The request message for
                [Conversations.CreateConversation][google.cloud.dialogflow.v2beta1.Conversations.CreateConversation].
            parent (str):
                Required. Resource identifier of the project creating
                the conversation. Format:
                ``projects/<Project ID>/locations/<Location ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            conversation (google.cloud.dialogflow_v2beta1.types.Conversation):
                Required. The conversation to create.
                This corresponds to the ``conversation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.Conversation:
                Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, conversation])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a gcd_conversation.CreateConversationRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, gcd_conversation.CreateConversationRequest):
            request = gcd_conversation.CreateConversationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if conversation is not None:
                request.conversation = conversation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_conversation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_conversations(
        self,
        request: Union[conversation.ListConversationsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListConversationsPager:
        r"""Returns the list of all conversations in the
        specified project.

        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_list_conversations():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListConversationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_conversations(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.ListConversationsRequest, dict]):
                The request object. The request message for
                [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].
            parent (str):
                Required. The project from which to list all
                conversation. Format:
                ``projects/<Project ID>/locations/<Location ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.services.conversations.pagers.ListConversationsPager:
                The response message for
                [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].

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

        # Minor optimization to avoid making a copy if the user passes
        # in a conversation.ListConversationsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, conversation.ListConversationsRequest):
            request = conversation.ListConversationsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_conversations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListConversationsPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_conversation(
        self,
        request: Union[conversation.GetConversationRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> conversation.Conversation:
        r"""Retrieves the specific conversation.

        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_get_conversation():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.GetConversationRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.GetConversationRequest, dict]):
                The request object. The request message for
                [Conversations.GetConversation][google.cloud.dialogflow.v2beta1.Conversations.GetConversation].
            name (str):
                Required. The name of the conversation. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.Conversation:
                Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

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

        # Minor optimization to avoid making a copy if the user passes
        # in a conversation.GetConversationRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, conversation.GetConversationRequest):
            request = conversation.GetConversationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_conversation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def complete_conversation(
        self,
        request: Union[conversation.CompleteConversationRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> conversation.Conversation:
        r"""Completes the specified conversation. Finished
        conversations are purged from the database after 30
        days.

        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_complete_conversation():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.CompleteConversationRequest(
                    name="name_value",
                )

                # Make the request
                response = client.complete_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.CompleteConversationRequest, dict]):
                The request object. The request message for
                [Conversations.CompleteConversation][google.cloud.dialogflow.v2beta1.Conversations.CompleteConversation].
            name (str):
                Required. Resource identifier of the conversation to
                close. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.Conversation:
                Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

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

        # Minor optimization to avoid making a copy if the user passes
        # in a conversation.CompleteConversationRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, conversation.CompleteConversationRequest):
            request = conversation.CompleteConversationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.complete_conversation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_create_messages(
        self,
        request: Union[conversation.BatchCreateMessagesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> conversation.BatchCreateMessagesResponse:
        r"""Batch ingests messages to conversation. Customers can
        use this RPC to ingest historical messages to
        conversation.

        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_batch_create_messages():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                requests = dialogflow_v2beta1.CreateMessageRequest()
                requests.parent = "parent_value"
                requests.message.content = "content_value"

                request = dialogflow_v2beta1.BatchCreateMessagesRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = client.batch_create_messages(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.BatchCreateMessagesRequest, dict]):
                The request object. The request message for
                [Conversations.BatchCreateMessagesRequest][].
            parent (str):
                Required. Resource identifier of the conversation to
                create message. Format:
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
            google.cloud.dialogflow_v2beta1.types.BatchCreateMessagesResponse:
                The request message for
                [Conversations.BatchCreateMessagesResponse][].

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

        # Minor optimization to avoid making a copy if the user passes
        # in a conversation.BatchCreateMessagesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, conversation.BatchCreateMessagesRequest):
            request = conversation.BatchCreateMessagesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_create_messages]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_messages(
        self,
        request: Union[conversation.ListMessagesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListMessagesPager:
        r"""Lists messages that belong to a given conversation. ``messages``
        are ordered by ``create_time`` in descending order. To fetch
        updates without duplication, send request with filter
        ``create_time_epoch_microseconds > [first item's create_time of previous request]``
        and empty page_token.

        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_list_messages():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListMessagesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_messages(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.ListMessagesRequest, dict]):
                The request object. The request message for
                [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages].
            parent (str):
                Required. The name of the conversation to list messages
                for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.services.conversations.pagers.ListMessagesPager:
                The response message for
                [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages].

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

        # Minor optimization to avoid making a copy if the user passes
        # in a conversation.ListMessagesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, conversation.ListMessagesRequest):
            request = conversation.ListMessagesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_messages]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListMessagesPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-dialogflow",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("ConversationsClient",)
