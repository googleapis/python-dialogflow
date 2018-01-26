#!/usr/bin/env python

# Copyright 2017 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def run_quickstart():
    # [START dailogflow_quickstart]
    import dialogflow
    import uuid

    text = 'Hi, what can I do with your app?'

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path('YOUR_PROJECT_ID', uuid.uuid4())
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(
        text=text, language_code='en-US')

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
    # [END dailogflow_quickstart]

if __name__ == '__main__':
    run_quickstart()
