import os

from google.cloud.dialogflow_v2.services.agents.client import AgentsClient
from google.cloud.dialogflow_v2.services.intents.client import IntentsClient

import pytest

from update_intent import update_intent

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
pytest.INTENT_ID = None


def list_intent(project_id):
    intents_client = IntentsClient()

    parent = AgentsClient.agent_path(project_id)

    intents = intents_client.list_intents(request={"parent": parent})

    for intent in intents:
        return intent.name.split("/")[4]


@pytest.fixture(scope="function", autouse=True)
def setup_teardown():
    pytest.INTENT_ID = list_intent(project_id=PROJECT_ID)
    print("Created Intent in setUp")


def test_update_intent():
    actualResponse = update_intent(PROJECT_ID, pytest.INTENT_ID, "Updated Intent")
    expectedResponse = "Updated Intent"
    assert actualResponse.display_name == expectedResponse
