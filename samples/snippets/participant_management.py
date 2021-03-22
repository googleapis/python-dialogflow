#!/usr/bin/env python

# Copyright 2019 Google LLC
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
"""Dialogflow API Python sample showing how to manage Participants.
"""

import time

from google.cloud import dialogflow_v2beta1 as dialogflow
from google.api_core import client_options

ROLES = ['HUMAN_AGENT', 'AUTOMATED_AGENT', 'END_USER']


# [START dialogflow_list_participants]
def list_participants(project_id, conversation_id):
    """Lists the participants belonging to a conversation.

    Args:
        project_id: The GCP project linked with the conversation profile.
        conversation_id: Id of the conversation."""
    client = dialogflow.ParticipantsClient()
    conversation_path = dialogflow.ConversationsClient.conversation_path(
        project_id, conversation_id)
    response = client.list_participants(parent=conversation_path)
    for participant in response:
        print('Role: {}'.format(participant.role))
        print('Name: {}'.format(participant.name))


# [END dialogflow_list_participants]


# [START dialogflow_create_participant]
def create_participant(project_id, conversation_id, role):
    """Creates a participant in a given conversation.

    Args:
        project_id: The GCP project linked with the conversation profile.
        conversation_id: Id of the conversation.
        participant: participant to be created."""
    client = dialogflow.ParticipantsClient()
    conversation_path = dialogflow.ConversationsClient.conversation_path(
        project_id, conversation_id)
    if role in ROLES:
        response = client.create_participant(parent=conversation_path,
                                             participant={'role': role})
        print('Participant Created.')
        print('Role: {}'.format(response.role))
        print('Name: {}'.format(response.name))

        return response


# [END dialogflow_create_participant]


# [START dialogflow_update_participant]
def update_participant(participant, update_mask=None):
    """Update the participant.

    Args:
        participant: participant to be created.
        update_mask: the mask to specify which fields to update."""
    client = dialogflow.ParticipantsClient()
    response = client.update_participant(participant=participant,
                                         update_mask=update_mask)
    print('Participant Updated.')
    print('Role: {}'.format(response.role))
    print('Name: {}'.format(response.name))

    return response


# [END dialogflow_update_participant]


# [START dialogflow_analyze_content_text]
def analyze_content_text(project_id, conversation_id, participant_id, text):
    """Analyze text message content from a participant.

    Args:
        project_id: The GCP project linked with the conversation profile.
        conversation_id: Id of the conversation.
        participant_id: Id of the participant.
        text: the text message that participant typed.
    """
    client = dialogflow.ParticipantsClient()
    participant_path = client.participant_path(project_id, conversation_id,
                                               participant_id)
    text_input = {'text': text, 'language_code': 'en-US'}
    response = client.analyze_content(participant=participant_path,
                                      text_input=text_input)
    print('AnalyzeContent Response:')
    print('Reply Text: {}'.format(response.reply_text))

    for suggestion_result in response.human_agent_suggestion_results:
        if suggestion_result.error is None:
            print('Error: {}'.format(suggestion_result.error.message))
        if suggestion_result.suggest_articles_response:
            for answer in suggestion_result.suggest_articles_response.article_answers:
                print('Article Suggestion Answer: {}'.format(answer.title))
                print('Answer Record: {}'.format(answer.answer_record))
        if suggestion_result.suggest_faq_answers_response:
            for answer in suggestion_result.suggest_faq_answers_response.faq_answers:
                print('Faq Answer: {}'.format(answer.answer))
                print('Answer Record: {}'.format(answer.answer_record))
        if suggestion_result.suggest_smart_replies_response:
            for answer in suggestion_result.suggest_smart_replies_response.smart_reply_answers:
                print('Smart Reply: {}'.format(answer.reply))
                print('Answer Record: {}'.format(answer.answer_record))

    for suggestion_result in response.end_user_suggestion_results:
        if suggestion_result.error:
            print('Error: {}'.format(suggestion_result.error.message))
        if suggestion_result.suggest_articles_response:
            for answer in suggestion_result.suggest_articles_response.article_answers:
                print('Article Suggestion Answer: {}'.format(answer.title))
                print('Answer Record: {}'.format(answer.answer_record))
        if suggestion_result.suggest_faq_answers_response:
            for answer in suggestion_result.suggest_faq_answers_response.faq_answers:
                print('Faq Answer: {}'.format(answer.answer))
                print('Answer Record: {}'.format(answer.answer_record))
        if suggestion_result.suggest_smart_replies_response:
            for answer in suggestion_result.suggest_smart_replies_response.smart_reply_answers:
                print('Smart Reply: {}'.format(answer.reply))
                print('Answer Record: {}'.format(answer.answer_record))

    return response


# [END dialogflow_analyze_content_text]


# [START dialogflow_streaming_analyze_content_audio]
def streaming_analyze_content_audio(participant_name,
                                    sample_rate_herz,
                                    stream,
                                    timeout,
                                    enable_extended_streaming=False):
    """Stream audio to Dialogflow and receive transcripts and suggestions.

    Args:
        participant_name: resource name of the participant.
        sample_rate_herz: herz rate of the sample.
        audio_generator: a sequence of audio data.
    """
    from google.cloud import dialogflow_v2beta1 as dialogflow_beta
    client = dialogflow_beta.ParticipantsClient()

    audio_config = dialogflow_beta.types.audio_config.InputAudioConfig(
        audio_encoding=dialogflow_beta.types.audio_config.AudioEncoding.
        AUDIO_ENCODING_LINEAR_16,
        sample_rate_hertz=sample_rate_herz,
        language_code='en-Us')

    def gen_requests(participant_name, audio_config, stream):
        """Generates requests for streaming.
        """
        audio_generator = stream.generator()
        while not stream.closed:
            print("Yield config to streaming analyze content.")
            yield dialogflow_beta.types.participant.StreamingAnalyzeContentRequest(
                participant=participant_name,
                enable_extended_streaming=enable_extended_streaming,
                audio_config=audio_config)
            print("Yield audios to streaming analyze content.")
            for content in audio_generator:
                # print('Yield audio to streaming analyze content')
                yield dialogflow_beta.types.participant.StreamingAnalyzeContentRequest(
                    input_audio=content)

    return client.streaming_analyze_content(gen_requests(
        participant_name, audio_config, stream),
                                            timeout=timeout)


# [END dialogflow_streaming_analyze_content_audio]
