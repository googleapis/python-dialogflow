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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import pkg_resources

import google.auth  # type: ignore
import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account # type: ignore

from google.cloud.dialogflow_v2beta1.types import agent
from google.cloud.dialogflow_v2beta1.types import agent as gcd_agent
from google.cloud.dialogflow_v2beta1.types import validation_result
from google.cloud.location import locations_pb2 # type: ignore
from google.longrunning import operations_pb2
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'google-cloud-dialogflow',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class AgentsTransport(abc.ABC):
    """Abstract transport class for Agents."""

    AUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
        'https://www.googleapis.com/auth/dialogflow',
    )

    DEFAULT_HOST: str = 'dialogflow.googleapis.com'
    def __init__(
            self, *,
            host: str = DEFAULT_HOST,
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            **kwargs,
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
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                                credentials_file,
                                **scopes_kwargs,
                                quota_project_id=quota_project_id
                            )
        elif credentials is None:
            credentials, _ = google.auth.default(**scopes_kwargs, quota_project_id=quota_project_id)
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(api_audience if api_audience else host)

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if always_use_jwt_access and isinstance(credentials, service_account.Credentials) and hasattr(service_account.Credentials, "with_always_use_jwt_access"):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.get_agent: gapic_v1.method.wrap_method(
                self.get_agent,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_agent: gapic_v1.method.wrap_method(
                self.set_agent,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_agent: gapic_v1.method.wrap_method(
                self.delete_agent,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_agents: gapic_v1.method.wrap_method(
                self.search_agents,
                default_timeout=None,
                client_info=client_info,
            ),
            self.train_agent: gapic_v1.method.wrap_method(
                self.train_agent,
                default_timeout=None,
                client_info=client_info,
            ),
            self.export_agent: gapic_v1.method.wrap_method(
                self.export_agent,
                default_timeout=None,
                client_info=client_info,
            ),
            self.import_agent: gapic_v1.method.wrap_method(
                self.import_agent,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_agent: gapic_v1.method.wrap_method(
                self.restore_agent,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_validation_result: gapic_v1.method.wrap_method(
                self.get_validation_result,
                default_timeout=None,
                client_info=client_info,
            ),
         }

    def close(self):
        """Closes resources associated with the transport.

       .. warning::
            Only call this method if the transport is NOT shared
            with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def get_agent(self) -> Callable[
            [agent.GetAgentRequest],
            Union[
                agent.Agent,
                Awaitable[agent.Agent]
            ]]:
        raise NotImplementedError()

    @property
    def set_agent(self) -> Callable[
            [gcd_agent.SetAgentRequest],
            Union[
                gcd_agent.Agent,
                Awaitable[gcd_agent.Agent]
            ]]:
        raise NotImplementedError()

    @property
    def delete_agent(self) -> Callable[
            [agent.DeleteAgentRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def search_agents(self) -> Callable[
            [agent.SearchAgentsRequest],
            Union[
                agent.SearchAgentsResponse,
                Awaitable[agent.SearchAgentsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def train_agent(self) -> Callable[
            [agent.TrainAgentRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def export_agent(self) -> Callable[
            [agent.ExportAgentRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def import_agent(self) -> Callable[
            [agent.ImportAgentRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def restore_agent(self) -> Callable[
            [agent.RestoreAgentRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def get_validation_result(self) -> Callable[
            [agent.GetValidationResultRequest],
            Union[
                validation_result.ValidationResult,
                Awaitable[validation_result.ValidationResult]
            ]]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[operations_pb2.ListOperationsResponse, Awaitable[operations_pb2.ListOperationsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [operations_pb2.CancelOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def get_location(self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[locations_pb2.ListLocationsResponse, Awaitable[locations_pb2.ListLocationsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = (
    'AgentsTransport',
)
