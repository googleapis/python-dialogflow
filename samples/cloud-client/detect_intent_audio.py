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
  python detect_intent_audio.py -h

  python detect_intent_audio.py --session-id mysession \
  --audio-file-path resources/book_a_room.wav

  python detect_intent_audio.py --session-id mysession \
  --audio-file-path resources/mountain_view.wav
  
  python detect_intent_audio.py --session-id mysession \
  --audio-file-path resources/today.wav
  
  python detect_intent_audio.py --session-id mysession \
  --audio-file-path resources/230pm.wav
  
  python detect_intent_audio.py --session-id mysession \
  --audio-file-path resources/half_an_hour.wav
  
  python detect_intent_audio.py --session-id mysession \
  --audio-file-path resources/two_people.wav
"""

# [START import_libraries]
import argparse
import os
import uuid

from google.cloud import dialogflow
from google.cloud.dialogflow import enums
from google.cloud.dialogflow import types
# [END import_libraries]


def detect_intent_audio(audio_file_path, project_id=None, session_id=None, language_code=None, audio_encoding=None, sample_rate_hertz=None):
    """Returns the result of DetectIntent() with a text input."""
    session_client = dialogflow.SessionsClient()

    project_id = project_id or os.getenv('GCLOUD_PROJECT') or os.getenv('GOOGLE_CLOUD_PROJECT')
    session_id = session_id or str(uuid.uuid4())
    language_code = language_code or 'en-US'
    audio_encoding = audio_encoding or enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate_hertz = sample_rate_hertz or 16000

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    with open(audio_file_path, 'rb') as audio_file:
        audio_config = types.InputAudioConfig(audio_encoding=audio_encoding, language_code=language_code, sample_rate_hertz=sample_rate_hertz)
        query_input = types.QueryInput(audio_config=audio_config)

        input_audio = audio_file.read()

        response = session_client.detect_intent(session=session, query_input=query_input, input_audio=input_audio)
        query_result = response.query_result

        print('=' * 20)
        print('Query text: {}'.format(query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(query_result.intent.display_name, query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(query_result.fulfillment_text))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--project-id',
        help='Project/agent id. Defaults to the value of the GCLOUD_PROJECT or '
        'GOOGLE_CLOUD_PROJECT environment variables.')
    parser.add_argument(
        '--session-id',
        help='Identifier of the DetectIntent session. '
             'Defaults to a random UUID.')
    parser.add_argument(
        '--language-code',
        help='Language code of the query. Defaults to "en-US".')
    parser.add_argument(
        '--audio-encoding',
        help='Encoding of the input audio. Defaults to '
            'AUDIO_ENCODING_LINEAR_16. See '
            'https://cloud.google.com/speech/docs/basics#audio-encodings.')
    parser.add_argument(
        '--sample-rate-hertz',
        help='Sample rate of the input audio. Only required if the input '
            'audio is in raw format. Defaults to 16000. See '
            'https://cloud.google.com/speech/docs/basics#sample-rates.',
        type=int)
    parser.add_argument(
        '--audio-file-path',
        help='Path to the audio file.',
        required=True)

    args = parser.parse_args()

    detect_intent_audio(args.audio_file_path, args.project_id, args.session_id, args.language_code, args.audio_encoding, args.sample_rate_hertz)

