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
# Snippet for BatchCreateMessages
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_generated_dialogflow_v2beta1_Conversations_BatchCreateMessages_sync]
from google.cloud import dialogflow_v2beta1


def sample_batch_create_messages():
    # Create a client
    client = dialogflow_v2beta1.ConversationsClient()

    # Initialize request argument(s)
    requests = dialogflow_v2beta1.CreateMessageRequest()
    requests.parent = "parent_value"
    requests.message.content = "content_value"

    request = dialogflow_v2beta1.BatchCreateMessagesRequest(
        parent="parent_value",
        requests=requests,
    )

    # Make the request
    response = client.batch_create_messages(request=request)

    # Handle the response
    print(response)

# [END dialogflow_generated_dialogflow_v2beta1_Conversations_BatchCreateMessages_sync]
