# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START dialogflow_set_agent_sample]

import os
import logging

from google.api_core.exceptions import InvalidArgument

import pytest
from google.auth.transport import requests
from google.oauth2 import service_account

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
CREDENTIAL_SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
CREDENTIALS_KEY_PATH = os.getenv("GCLOUD_SECRETS_SERVICE_ACCOUNT")

# We cannot test setAgent because Dialogflow ES can only have one agent
# and if we create a agent it will delete the exisitng testing agent and
# would cause all tests to fail
def test_set_agent():
    credentials = service_account.Credentials.from_service_account_file(
          CREDENTIALS_KEY_PATH, scopes=CREDENTIAL_SCOPES)
    credentials.refresh(requests.Request())
    raise ValueError(credentials.token)
