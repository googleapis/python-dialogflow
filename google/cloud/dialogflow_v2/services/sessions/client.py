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
import os
import re
from typing import Dict, Optional, Iterable, Iterator, Sequence, Tuple, Type, Union
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

from google.cloud.dialogflow_v2.types import audio_config
from google.cloud.dialogflow_v2.types import session
from google.cloud.dialogflow_v2.types import session as gcd_session
from google.rpc import status_pb2  # type: ignore
from .transports.base import SessionsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import SessionsGrpcTransport
from .transports.grpc_asyncio import SessionsGrpcAsyncIOTransport


class SessionsClientMeta(type):
    """Metaclass for the Sessions client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[SessionsTransport]]
    _transport_registry["grpc"] = SessionsGrpcTransport
    _transport_registry["grpc_asyncio"] = SessionsGrpcAsyncIOTransport

    def get_transport_class(cls, label: str = None,) -> Type[SessionsTransport]:
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


class SessionsClient(metaclass=SessionsClientMeta):
    """A service used for session interactions.

    For more information, see the `API interactions
    guide <https://cloud.google.com/dialogflow/docs/api-overview>`__.
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
            SessionsClient: The constructed client.
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
            SessionsClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> SessionsTransport:
        """Returns the transport used by the client instance.

        Returns:
            SessionsTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def context_path(project: str, session: str, context: str,) -> str:
        """Returns a fully-qualified context string."""
        return "projects/{project}/agent/sessions/{session}/contexts/{context}".format(
            project=project, session=session, context=context,
        )

    @staticmethod
    def parse_context_path(path: str) -> Dict[str, str]:
        """Parses a context path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/agent/sessions/(?P<session>.+?)/contexts/(?P<context>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def intent_path(project: str, intent: str,) -> str:
        """Returns a fully-qualified intent string."""
        return "projects/{project}/agent/intents/{intent}".format(
            project=project, intent=intent,
        )

    @staticmethod
    def parse_intent_path(path: str) -> Dict[str, str]:
        """Parses a intent path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/agent/intents/(?P<intent>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def session_path(project: str, session: str,) -> str:
        """Returns a fully-qualified session string."""
        return "projects/{project}/agent/sessions/{session}".format(
            project=project, session=session,
        )

    @staticmethod
    def parse_session_path(path: str) -> Dict[str, str]:
        """Parses a session path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/agent/sessions/(?P<session>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def session_entity_type_path(project: str, session: str, entity_type: str,) -> str:
        """Returns a fully-qualified session_entity_type string."""
        return "projects/{project}/agent/sessions/{session}/entityTypes/{entity_type}".format(
            project=project, session=session, entity_type=entity_type,
        )

    @staticmethod
    def parse_session_entity_type_path(path: str) -> Dict[str, str]:
        """Parses a session_entity_type path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/agent/sessions/(?P<session>.+?)/entityTypes/(?P<entity_type>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(billing_account: str,) -> str:
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
    def common_folder_path(folder: str,) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder,)

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str,) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization,)

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str,) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(project=project,)

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str,) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project, location=location,
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
        transport: Union[str, SessionsTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the sessions client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, SessionsTransport]): The
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
        if isinstance(transport, SessionsTransport):
            # transport is a SessionsTransport instance.
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

    def detect_intent(
        self,
        request: Union[gcd_session.DetectIntentRequest, dict] = None,
        *,
        session: str = None,
        query_input: gcd_session.QueryInput = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_session.DetectIntentResponse:
        r"""Processes a natural language query and returns structured,
        actionable data as a result. This method is not idempotent,
        because it may cause contexts and session entity types to be
        updated, which in turn might affect results of future queries.

        If you might use `Agent
        Assist <https://cloud.google.com/dialogflow/docs/#aa>`__ or
        other CCAI products now or in the future, consider using
        [AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent]
        instead of ``DetectIntent``. ``AnalyzeContent`` has additional
        functionality for Agent Assist and other CCAI products.

        Note: Always use agent versions for production traffic. See
        `Versions and
        environments <https://cloud.google.com/dialogflow/es/docs/agents-versions>`__.



        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_detect_intent():
                # Create a client
                client = dialogflow_v2.SessionsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.DetectIntentRequest(
                    session="session_value",
                )

                # Make the request
                response = client.detect_intent(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.DetectIntentRequest, dict]):
                The request object. The request to detect user's intent.
            session (str):
                Required. The name of the session this query is sent to.
                Format:
                ``projects/<Project ID>/agent/sessions/<Session ID>``,
                or
                ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>``.
                If ``Environment ID`` is not specified, we assume
                default 'draft' environment (``Environment ID`` might be
                referred to as environment name at some places). If
                ``User ID`` is not specified, we are using "-". It's up
                to the API caller to choose an appropriate
                ``Session ID`` and ``User Id``. They can be a random
                number or some type of user and session identifiers
                (preferably hashed). The length of the ``Session ID``
                and ``User ID`` must not exceed 36 characters.

                For more information, see the `API interactions
                guide <https://cloud.google.com/dialogflow/docs/api-overview>`__.

                Note: Always use agent versions for production traffic.
                See `Versions and
                environments <https://cloud.google.com/dialogflow/es/docs/agents-versions>`__.

                This corresponds to the ``session`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            query_input (google.cloud.dialogflow_v2.types.QueryInput):
                Required. The input specification. It
                can be set to:
                1.  an audio config
                    which instructs the speech
                recognizer how to process the speech
                audio,
                2.  a conversational query in the form
                of text, or
                3.  an event that specifies which intent
                to trigger.

                This corresponds to the ``query_input`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.DetectIntentResponse:
                The message returned from the
                DetectIntent method.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([session, query_input])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a gcd_session.DetectIntentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, gcd_session.DetectIntentRequest):
            request = gcd_session.DetectIntentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if session is not None:
                request.session = session
            if query_input is not None:
                request.query_input = query_input

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.detect_intent]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("session", request.session),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def streaming_detect_intent(
        self,
        requests: Iterator[session.StreamingDetectIntentRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> Iterable[session.StreamingDetectIntentResponse]:
        r"""Processes a natural language query in audio format in a
        streaming fashion and returns structured, actionable data as a
        result. This method is only available via the gRPC API (not
        REST).

        If you might use `Agent
        Assist <https://cloud.google.com/dialogflow/docs/#aa>`__ or
        other CCAI products now or in the future, consider using
        [StreamingAnalyzeContent][google.cloud.dialogflow.v2.Participants.StreamingAnalyzeContent]
        instead of ``StreamingDetectIntent``.
        ``StreamingAnalyzeContent`` has additional functionality for
        Agent Assist and other CCAI products.

        Note: Always use agent versions for production traffic. See
        `Versions and
        environments <https://cloud.google.com/dialogflow/es/docs/agents-versions>`__.



        .. code-block::

            from google.cloud import dialogflow_v2

            def sample_streaming_detect_intent():
                # Create a client
                client = dialogflow_v2.SessionsClient()

                # Initialize request argument(s)
                request = dialogflow_v2.StreamingDetectIntentRequest(
                    session="session_value",
                )

                # This method expects an iterator which contains
                # 'dialogflow_v2.StreamingDetectIntentRequest' objects
                # Here we create a generator that yields a single `request` for
                # demonstrative purposes.
                requests = [request]

                def request_generator():
                    for request in requests:
                        yield request

                # Make the request
                stream = client.streaming_detect_intent(requests=request_generator())

                # Handle the response
                for response in stream:
                    print(response)

        Args:
            requests (Iterator[google.cloud.dialogflow_v2.types.StreamingDetectIntentRequest]):
                The request object iterator. The top-level message sent by the
                client to the
                [Sessions.StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]
                method.
                Multiple request messages should be sent in order:

                1.  The first message must contain
                [session][google.cloud.dialogflow.v2.StreamingDetectIntentRequest.session],
                [query_input][google.cloud.dialogflow.v2.StreamingDetectIntentRequest.query_input]
                plus optionally
                [query_params][google.cloud.dialogflow.v2.StreamingDetectIntentRequest.query_params].
                If the client     wants to receive an audio response, it
                should also contain
                [output_audio_config][google.cloud.dialogflow.v2.StreamingDetectIntentRequest.output_audio_config].
                The message must not contain
                [input_audio][google.cloud.dialogflow.v2.StreamingDetectIntentRequest.input_audio].
                2.  If
                [query_input][google.cloud.dialogflow.v2.StreamingDetectIntentRequest.query_input]
                was set to
                [query_input.audio_config][google.cloud.dialogflow.v2.InputAudioConfig],
                all subsequent     messages must contain
                [input_audio][google.cloud.dialogflow.v2.StreamingDetectIntentRequest.input_audio]
                to continue with     Speech recognition.
                    If you decide to rather detect an intent from text
                input after you     already started Speech recognition,
                please send a message with
                [query_input.text][google.cloud.dialogflow.v2.QueryInput.text].
                    However, note that:

                    * Dialogflow will bill you for the audio duration so
                far.     * Dialogflow discards all Speech recognition
                results in favor of the       input text.
                    * Dialogflow will use the language code from the
                first message.
                After you sent all input, you must half-close or abort
                the request stream.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            Iterable[google.cloud.dialogflow_v2.types.StreamingDetectIntentResponse]:
                The top-level message returned from the
                   StreamingDetectIntent method.

                   Multiple response messages can be returned in order:

                   1. If the StreamingDetectIntentRequest.input_audio
                      field was set, the recognition_result field is
                      populated for one or more messages. See the
                      [StreamingRecognitionResult][google.cloud.dialogflow.v2.StreamingRecognitionResult]
                      message for details about the result message
                      sequence.
                   2. The next message contains response_id,
                      query_result and optionally webhook_status if a
                      WebHook was called.

        """

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.streaming_detect_intent]

        # Send the request.
        response = rpc(requests, retry=retry, timeout=timeout, metadata=metadata,)

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


__all__ = ("SessionsClient",)
