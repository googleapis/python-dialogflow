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

import conversation_management
import conversation_profile_management
import participant_management

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
CONVERSATION_PROFILE_DISPLAY_NAME = "fake_conversation_profile"
AUDIO_FILE_PATH = "{0}/resources/book_a_room.wav".format(
    os.path.realpath(os.path.dirname(__file__)),
)

# Test live transcription with streaming_analyze_content.


def test_analyze_content_audio_stream(capsys):
    # Create conversation profile.
    conversation_profile_management.create_conversation_profile_article_faq(
        project_id=PROJECT_ID,
        display_name=CONVERSATION_PROFILE_DISPLAY_NAME
    )
    out, _ = capsys.readouterr()
    assert "Display Name: {}".format(CONVERSATION_PROFILE_DISPLAY_NAME) in out
    conversation_profile_id = out.split("conversationProfiles/")[1].rstrip()

    # Create conversation.
    conversation_management.create_conversation(
        project_id=PROJECT_ID, conversation_profile_id=conversation_profile_id
    )

    out, _ = capsys.readouterr()
    conversation_id = out.split("conversations/")[1].rstrip()

    # Create end user participant.
    participant_management.create_participant(
        project_id=PROJECT_ID, conversation_id=conversation_id, role="END_USER"
    )
    out, _ = capsys.readouterr()
    end_user_id = out.split("participants/")[1].rstrip()

    participant_management.analyze_content_audio_stream(
        project_id=PROJECT_ID,
        conversation_id=conversation_id,
        participant_id=end_user_id,
        audio_file_path=AUDIO_FILE_PATH,
        language_code="en-US",
    )

    out, _ = capsys.readouterr()
    assert "Transcript" in out
