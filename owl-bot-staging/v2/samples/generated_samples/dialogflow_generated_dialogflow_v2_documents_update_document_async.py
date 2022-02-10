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
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateDocument
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_generated_dialogflow_v2_Documents_UpdateDocument_async]
from google.cloud import dialogflow_v2


async def sample_update_document():
    # Create a client
    client = dialogflow_v2.DocumentsAsyncClient()

    # Initialize request argument(s)
    document = dialogflow_v2.Document()
    document.content_uri = "content_uri_value"
    document.display_name = "display_name_value"
    document.mime_type = "mime_type_value"
    document.knowledge_types = "ARTICLE_SUGGESTION"

    request = dialogflow_v2.UpdateDocumentRequest(
        document=document,
    )

    # Make the request
    operation = client.update_document(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

# [END dialogflow_generated_dialogflow_v2_Documents_UpdateDocument_async]
