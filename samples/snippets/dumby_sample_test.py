# Copyright 2021 Google LLC
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

import os

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

import pytest

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")


# We cannot test setAgent because Dialogflow ES can only have one agent
# and if we create a agent it will delete the exisitng testing agent and
# would cause all tests to fail
def test_dumby():
    
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
    project_body = {
        'name': 'GalsDumbyTestingProject',
        'projectId': 'gals-testing-123'
    }
    request = service.projects().create(body=project_body)
    request.execute()
    pprint(request)
