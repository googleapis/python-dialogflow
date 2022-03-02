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
# Snippet for SetAgent
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_generated_dialogflow_v2_Agents_SetAgent_sync]
from google.cloud import dialogflow_v2


def sample_set_agent():
    # Create a client
    client = dialogflow_v2.AgentsClient()

    # Initialize request argument(s)
    agent = dialogflow_v2.Agent()
    agent.parent = "parent_value"
    agent.display_name = "display_name_value"
    agent.default_language_code = "default_language_code_value"
    agent.time_zone = "time_zone_value"

    request = dialogflow_v2.SetAgentRequest(
        agent=agent,
    )

    # Make the request
    response = client.set_agent(request=request)

    # Handle the response
    print(response)

# [END dialogflow_generated_dialogflow_v2_Agents_SetAgent_sync]