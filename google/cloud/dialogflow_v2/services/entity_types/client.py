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

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.dialogflow_v2.services.entity_types import pagers
from google.cloud.dialogflow_v2.types import entity_type
from google.cloud.dialogflow_v2.types import entity_type as gcd_entity_type
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import struct_pb2  # type: ignore
from .transports.base import EntityTypesTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import EntityTypesGrpcTransport
from .transports.grpc_asyncio import EntityTypesGrpcAsyncIOTransport


class EntityTypesClientMeta(type):
    """Metaclass for the EntityTypes client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[EntityTypesTransport]]
    _transport_registry["grpc"] = EntityTypesGrpcTransport
    _transport_registry["grpc_asyncio"] = EntityTypesGrpcAsyncIOTransport

    def get_transport_class(
        cls,
        label: str = None,
    ) -> Type[EntityTypesTransport]:
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


class EntityTypesClient(metaclass=EntityTypesClientMeta):
    """Service for managing
    [EntityTypes][google.cloud.dialogflow.v2.EntityType].
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
            EntityTypesClient: The constructed client.
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
            EntityTypesClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> EntityTypesTransport:
        """Returns the transport used by the client instance.

        Returns:
            EntityTypesTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def entity_type_path(
        project: str,
        entity_type: str,
    ) -> str:
        """Returns a fully-qualified entity_type string."""
        return "projects/{project}/agent/entityTypes/{entity_type}".format(
            project=project,
            entity_type=entity_type,
        )

    @staticmethod
    def parse_entity_type_path(path: str) -> Dict[str, str]:
        """Parses a entity_type path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/agent/entityTypes/(?P<entity_type>.+?)$", path
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
        transport: Union[str, EntityTypesTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the entity types client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, EntityTypesTransport]): The
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
        if isinstance(transport, EntityTypesTransport):
            # transport is a EntityTypesTransport instance.
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

    def list_entity_types(
        self,
        request: Union[entity_type.ListEntityTypesRequest, dict] = None,
        *,
        parent: str = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListEntityTypesPager:
        r"""Returns the list of all entity types in the specified
        agent.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            def sample_list_entity_types():
                # Create a client
                client = dialogflow_v2.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2.ListEntityTypesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_entity_types(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.ListEntityTypesRequest, dict]):
                The request object. The request message for
                [EntityTypes.ListEntityTypes][google.cloud.dialogflow.v2.EntityTypes.ListEntityTypes].
            parent (str):
                Required. The agent to list all entity types from.
                Format: ``projects/<Project ID>/agent``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (str):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.services.entity_types.pagers.ListEntityTypesPager:
                The response message for
                [EntityTypes.ListEntityTypes][google.cloud.dialogflow.v2.EntityTypes.ListEntityTypes].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a entity_type.ListEntityTypesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, entity_type.ListEntityTypesRequest):
            request = entity_type.ListEntityTypesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if language_code is not None:
                request.language_code = language_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_entity_types]

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
        response = pagers.ListEntityTypesPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_entity_type(
        self,
        request: Union[entity_type.GetEntityTypeRequest, dict] = None,
        *,
        name: str = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> entity_type.EntityType:
        r"""Retrieves the specified entity type.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            def sample_get_entity_type():
                # Create a client
                client = dialogflow_v2.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2.GetEntityTypeRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_entity_type(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.GetEntityTypeRequest, dict]):
                The request object. The request message for
                [EntityTypes.GetEntityType][google.cloud.dialogflow.v2.EntityTypes.GetEntityType].
            name (str):
                Required. The name of the entity type. Format:
                ``projects/<Project ID>/agent/entityTypes/<EntityType ID>``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (str):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.EntityType:
                Each intent parameter has a type, called the entity type, which dictates
                   exactly how data from an end-user expression is
                   extracted.

                   Dialogflow provides predefined system entities that
                   can match many common types of data. For example,
                   there are system entities for matching dates, times,
                   colors, email addresses, and so on. You can also
                   create your own custom entities for matching custom
                   data. For example, you could define a vegetable
                   entity that can match the types of vegetables
                   available for purchase with a grocery store agent.

                   For more information, see the [Entity
                   guide](\ https://cloud.google.com/dialogflow/docs/entities-overview).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a entity_type.GetEntityTypeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, entity_type.GetEntityTypeRequest):
            request = entity_type.GetEntityTypeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if language_code is not None:
                request.language_code = language_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_entity_type]

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

    def create_entity_type(
        self,
        request: Union[gcd_entity_type.CreateEntityTypeRequest, dict] = None,
        *,
        parent: str = None,
        entity_type: gcd_entity_type.EntityType = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_entity_type.EntityType:
        r"""Creates an entity type in the specified agent.

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            def sample_create_entity_type():
                # Create a client
                client = dialogflow_v2.EntityTypesClient()

                # Initialize request argument(s)
                entity_type = dialogflow_v2.EntityType()
                entity_type.display_name = "display_name_value"
                entity_type.kind = "KIND_REGEXP"

                request = dialogflow_v2.CreateEntityTypeRequest(
                    parent="parent_value",
                    entity_type=entity_type,
                )

                # Make the request
                response = client.create_entity_type(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.CreateEntityTypeRequest, dict]):
                The request object. The request message for
                [EntityTypes.CreateEntityType][google.cloud.dialogflow.v2.EntityTypes.CreateEntityType].
            parent (str):
                Required. The agent to create a entity type for. Format:
                ``projects/<Project ID>/agent``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entity_type (google.cloud.dialogflow_v2.types.EntityType):
                Required. The entity type to create.
                This corresponds to the ``entity_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (str):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.EntityType:
                Each intent parameter has a type, called the entity type, which dictates
                   exactly how data from an end-user expression is
                   extracted.

                   Dialogflow provides predefined system entities that
                   can match many common types of data. For example,
                   there are system entities for matching dates, times,
                   colors, email addresses, and so on. You can also
                   create your own custom entities for matching custom
                   data. For example, you could define a vegetable
                   entity that can match the types of vegetables
                   available for purchase with a grocery store agent.

                   For more information, see the [Entity
                   guide](\ https://cloud.google.com/dialogflow/docs/entities-overview).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, entity_type, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a gcd_entity_type.CreateEntityTypeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, gcd_entity_type.CreateEntityTypeRequest):
            request = gcd_entity_type.CreateEntityTypeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if entity_type is not None:
                request.entity_type = entity_type
            if language_code is not None:
                request.language_code = language_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_entity_type]

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

    def update_entity_type(
        self,
        request: Union[gcd_entity_type.UpdateEntityTypeRequest, dict] = None,
        *,
        entity_type: gcd_entity_type.EntityType = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_entity_type.EntityType:
        r"""Updates the specified entity type.

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            def sample_update_entity_type():
                # Create a client
                client = dialogflow_v2.EntityTypesClient()

                # Initialize request argument(s)
                entity_type = dialogflow_v2.EntityType()
                entity_type.display_name = "display_name_value"
                entity_type.kind = "KIND_REGEXP"

                request = dialogflow_v2.UpdateEntityTypeRequest(
                    entity_type=entity_type,
                )

                # Make the request
                response = client.update_entity_type(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.UpdateEntityTypeRequest, dict]):
                The request object. The request message for
                [EntityTypes.UpdateEntityType][google.cloud.dialogflow.v2.EntityTypes.UpdateEntityType].
            entity_type (google.cloud.dialogflow_v2.types.EntityType):
                Required. The entity type to update.
                This corresponds to the ``entity_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (str):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2.types.EntityType:
                Each intent parameter has a type, called the entity type, which dictates
                   exactly how data from an end-user expression is
                   extracted.

                   Dialogflow provides predefined system entities that
                   can match many common types of data. For example,
                   there are system entities for matching dates, times,
                   colors, email addresses, and so on. You can also
                   create your own custom entities for matching custom
                   data. For example, you could define a vegetable
                   entity that can match the types of vegetables
                   available for purchase with a grocery store agent.

                   For more information, see the [Entity
                   guide](\ https://cloud.google.com/dialogflow/docs/entities-overview).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([entity_type, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a gcd_entity_type.UpdateEntityTypeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, gcd_entity_type.UpdateEntityTypeRequest):
            request = gcd_entity_type.UpdateEntityTypeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if entity_type is not None:
                request.entity_type = entity_type
            if language_code is not None:
                request.language_code = language_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_entity_type]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("entity_type.name", request.entity_type.name),)
            ),
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

    def delete_entity_type(
        self,
        request: Union[entity_type.DeleteEntityTypeRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the specified entity type.

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            def sample_delete_entity_type():
                # Create a client
                client = dialogflow_v2.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2.DeleteEntityTypeRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_entity_type(request=request)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.DeleteEntityTypeRequest, dict]):
                The request object. The request message for
                [EntityTypes.DeleteEntityType][google.cloud.dialogflow.v2.EntityTypes.DeleteEntityType].
            name (str):
                Required. The name of the entity type to delete. Format:
                ``projects/<Project ID>/agent/entityTypes/<EntityType ID>``.

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

        # Minor optimization to avoid making a copy if the user passes
        # in a entity_type.DeleteEntityTypeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, entity_type.DeleteEntityTypeRequest):
            request = entity_type.DeleteEntityTypeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_entity_type]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def batch_update_entity_types(
        self,
        request: Union[entity_type.BatchUpdateEntityTypesRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Updates/Creates multiple entity types in the specified agent.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``:
           [BatchUpdateEntityTypesResponse][google.cloud.dialogflow.v2.BatchUpdateEntityTypesResponse]

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            def sample_batch_update_entity_types():
                # Create a client
                client = dialogflow_v2.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2.BatchUpdateEntityTypesRequest(
                    entity_type_batch_uri="entity_type_batch_uri_value",
                    parent="parent_value",
                )

                # Make the request
                operation = client.batch_update_entity_types(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.BatchUpdateEntityTypesRequest, dict]):
                The request object. The request message for
                [EntityTypes.BatchUpdateEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dialogflow_v2.types.BatchUpdateEntityTypesResponse`
                The response message for
                [EntityTypes.BatchUpdateEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes].

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a entity_type.BatchUpdateEntityTypesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, entity_type.BatchUpdateEntityTypesRequest):
            request = entity_type.BatchUpdateEntityTypesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.batch_update_entity_types
        ]

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            entity_type.BatchUpdateEntityTypesResponse,
            metadata_type=struct_pb2.Struct,
        )

        # Done; return the response.
        return response

    def batch_delete_entity_types(
        self,
        request: Union[entity_type.BatchDeleteEntityTypesRequest, dict] = None,
        *,
        parent: str = None,
        entity_type_names: Sequence[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Deletes entity types in the specified agent.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            def sample_batch_delete_entity_types():
                # Create a client
                client = dialogflow_v2.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2.BatchDeleteEntityTypesRequest(
                    parent="parent_value",
                    entity_type_names=['entity_type_names_value_1', 'entity_type_names_value_2'],
                )

                # Make the request
                operation = client.batch_delete_entity_types(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.BatchDeleteEntityTypesRequest, dict]):
                The request object. The request message for
                [EntityTypes.BatchDeleteEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntityTypes].
            parent (str):
                Required. The name of the agent to delete all entities
                types for. Format: ``projects/<Project ID>/agent``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entity_type_names (Sequence[str]):
                Required. The names entity types to delete. All names
                must point to the same agent as ``parent``.

                This corresponds to the ``entity_type_names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
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
        has_flattened_params = any([parent, entity_type_names])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a entity_type.BatchDeleteEntityTypesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, entity_type.BatchDeleteEntityTypesRequest):
            request = entity_type.BatchDeleteEntityTypesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if entity_type_names is not None:
                request.entity_type_names = entity_type_names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.batch_delete_entity_types
        ]

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=struct_pb2.Struct,
        )

        # Done; return the response.
        return response

    def batch_create_entities(
        self,
        request: Union[entity_type.BatchCreateEntitiesRequest, dict] = None,
        *,
        parent: str = None,
        entities: Sequence[entity_type.EntityType.Entity] = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Creates multiple new entities in the specified entity type.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            def sample_batch_create_entities():
                # Create a client
                client = dialogflow_v2.EntityTypesClient()

                # Initialize request argument(s)
                entities = dialogflow_v2.Entity()
                entities.value = "value_value"
                entities.synonyms = ['synonyms_value_1', 'synonyms_value_2']

                request = dialogflow_v2.BatchCreateEntitiesRequest(
                    parent="parent_value",
                    entities=entities,
                )

                # Make the request
                operation = client.batch_create_entities(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.BatchCreateEntitiesRequest, dict]):
                The request object. The request message for
                [EntityTypes.BatchCreateEntities][google.cloud.dialogflow.v2.EntityTypes.BatchCreateEntities].
            parent (str):
                Required. The name of the entity type to create entities
                in. Format:
                ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entities (Sequence[google.cloud.dialogflow_v2.types.EntityType.Entity]):
                Required. The entities to create.
                This corresponds to the ``entities`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (str):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
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
        has_flattened_params = any([parent, entities, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a entity_type.BatchCreateEntitiesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, entity_type.BatchCreateEntitiesRequest):
            request = entity_type.BatchCreateEntitiesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if entities is not None:
                request.entities = entities
            if language_code is not None:
                request.language_code = language_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_create_entities]

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=struct_pb2.Struct,
        )

        # Done; return the response.
        return response

    def batch_update_entities(
        self,
        request: Union[entity_type.BatchUpdateEntitiesRequest, dict] = None,
        *,
        parent: str = None,
        entities: Sequence[entity_type.EntityType.Entity] = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Updates or creates multiple entities in the specified entity
        type. This method does not affect entities in the entity type
        that aren't explicitly specified in the request.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            def sample_batch_update_entities():
                # Create a client
                client = dialogflow_v2.EntityTypesClient()

                # Initialize request argument(s)
                entities = dialogflow_v2.Entity()
                entities.value = "value_value"
                entities.synonyms = ['synonyms_value_1', 'synonyms_value_2']

                request = dialogflow_v2.BatchUpdateEntitiesRequest(
                    parent="parent_value",
                    entities=entities,
                )

                # Make the request
                operation = client.batch_update_entities(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.BatchUpdateEntitiesRequest, dict]):
                The request object. The request message for
                [EntityTypes.BatchUpdateEntities][google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntities].
            parent (str):
                Required. The name of the entity type to update or
                create entities in. Format:
                ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entities (Sequence[google.cloud.dialogflow_v2.types.EntityType.Entity]):
                Required. The entities to update or
                create.

                This corresponds to the ``entities`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (str):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
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
        has_flattened_params = any([parent, entities, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a entity_type.BatchUpdateEntitiesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, entity_type.BatchUpdateEntitiesRequest):
            request = entity_type.BatchUpdateEntitiesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if entities is not None:
                request.entities = entities
            if language_code is not None:
                request.language_code = language_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_update_entities]

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=struct_pb2.Struct,
        )

        # Done; return the response.
        return response

    def batch_delete_entities(
        self,
        request: Union[entity_type.BatchDeleteEntitiesRequest, dict] = None,
        *,
        parent: str = None,
        entity_values: Sequence[str] = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Deletes entities in the specified entity type.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        .. code-block:: python

            from google.cloud import dialogflow_v2

            def sample_batch_delete_entities():
                # Create a client
                client = dialogflow_v2.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2.BatchDeleteEntitiesRequest(
                    parent="parent_value",
                    entity_values=['entity_values_value_1', 'entity_values_value_2'],
                )

                # Make the request
                operation = client.batch_delete_entities(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2.types.BatchDeleteEntitiesRequest, dict]):
                The request object. The request message for
                [EntityTypes.BatchDeleteEntities][google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntities].
            parent (str):
                Required. The name of the entity type to delete entries
                for. Format:
                ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entity_values (Sequence[str]):
                Required. The reference ``values`` of the entities to
                delete. Note that these are not fully-qualified names,
                i.e. they don't start with ``projects/<Project ID>``.

                This corresponds to the ``entity_values`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (str):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation.Operation:
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
        has_flattened_params = any([parent, entity_values, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a entity_type.BatchDeleteEntitiesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, entity_type.BatchDeleteEntitiesRequest):
            request = entity_type.BatchDeleteEntitiesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if entity_values is not None:
                request.entity_values = entity_values
            if language_code is not None:
                request.language_code = language_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_delete_entities]

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=struct_pb2.Struct,
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


__all__ = ("EntityTypesClient",)
