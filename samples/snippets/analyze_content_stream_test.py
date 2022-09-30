# Copyright 2022 Google LLC
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
import uuid

import conversation_management
import conversation_profile_management
import participant_management

import pytest

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
CONVERSATION_PROFILE_DISPLAY_NAME = "sample_conversation_profile_{}".format(uuid.uuid4())
AUDIO_FILE_PATH = "{0}/resources/book_a_room.wav".format(
    os.path.realpath(os.path.dirname(__file__)),
)


@pytest.fixture(scope="function", autouse=True)
def setup_teardown():
    # Create conversation profile.
    response = conversation_profile_management.create_conversation_profile_article_faq(
        project_id=PROJECT_ID,
        display_name=CONVERSATION_PROFILE_DISPLAY_NAME
    )
    conversation_profile_id = response.name.split("conversationProfiles/")[1].rstrip()

    # Create conversation.
    response = conversation_management.create_conversation(
        project_id=PROJECT_ID, conversation_profile_id=conversation_profile_id
    )
    pytest.CONVERSATION_ID = response.name.split("conversations/")[1].rstrip()

    # Create end user participant.
    response = participant_management.create_participant(
        project_id=PROJECT_ID, conversation_id=pytest.CONVERSATION_ID, role="END_USER"
    )
    pytest.END_USER_ID = response.name.split("participants/")[1].rstrip()

    yield

    # Complete the conversation.
    conversation_management.complete_conversation(project_id=PROJECT_ID, conversation_id=pytest.CONVERSATION_ID)

    # Delete the conversation profile.
    conversation_profile_management.delete_conversation_profile(
        PROJECT_ID, conversation_profile_id
    )


# Test live transcription with streaming_analyze_content.
def test_analyze_content_audio_stream(capsys):
    # Call StreamingAnalyzeContent to transcribe the audio.
    participant_management.analyze_content_audio_stream(
        project_id=PROJECT_ID,
        conversation_id=pytest.CONVERSATION_ID,
        participant_id=pytest.END_USER_ID ,
        audio_file_path=AUDIO_FILE_PATH,
        language_code="en-US",
    )
    out, _ = capsys.readouterr()
    assert "book a room" in out
