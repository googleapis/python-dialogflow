#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
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
"""DialogFlow API Detect Intent Python sample with text inputs.

Examples:
  python detect_intent_texts.py -h
  python detect_intent_texts.py --session-id mysession \
  "hello" "book a meeting room" "Mountain View"
  python detect_intent_textx.py --session-id mysession \
  "tomorrow" "10am" "2 hours" "10 people" "A" "yes"
"""

# [START import_libraries]
import argparse
import os
import uuid

from google.cloud import dialogflow
from google.cloud.dialogflow import types
# [END import_libraries]


def detect_intent_texts(texts, language_code=None, session_id=None,
                        project_id=None):
    """Returns the result of DetectIntent() with a text input."""
    session_client = dialogflow.SessionsClient()

    project_id = (
        project_id or os.getenv('GCLOUD_PROJECT')
        or (os.getenv('GOOGLE_CLOUD_PROJECT')))
    session_id = session_id or str(uuid.uuid4())
    language_code = language_code or 'en-US'

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = types.TextInput(
            text=text, language_code=language_code)

        query_input = types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)
        query_result = response.query_result

        print('=' * 20)
        print('Query text: {}'.format(query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            query_result.intent.display_name,
            query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            query_result.fulfillment_text))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--project-id',
        help='Project/agent id. Defaults to the value of the '
        'GCLOUD_PROJECT or GOOGLE_CLOUD_PROJECT environment '
        'variables.')
    parser.add_argument(
        '--session-id',
        help='Identifier of the DetectIntent session. '
             'Defaults to a random UUID.')
    parser.add_argument(
        '--language-code',
        help='Language code of the query. Defaults to "en-US".')
    parser.add_argument(
        'texts',
        nargs='+',
        type=str,
        help='Text inputs.')

    args = parser.parse_args()

    detect_intent_texts(
        args.texts, args.language_code, args.session_id, args.project_id)
