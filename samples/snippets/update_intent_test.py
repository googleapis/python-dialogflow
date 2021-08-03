from datetime import date
import os
import pytest

from google.cloud.dialogflow_v2 import Agent
from google.cloud.dialogflow_v2.services.agents.client import AgentsClient
from google.cloud.dialogflow_v2.services.intents.client import IntentsClient
from google.cloud.dialogflow_v2.types.agent import (
    DeleteAgentRequest,
    SearchAgentsRequest,
)

from update_intent import update_intent

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
pytest.INTENT_ID = None

def create_agent(project_id, display_name):
    parent = "projects/" + project_id
    agents_client = AgentsClient()
    agent = Agent(
        parent=parent,
        display_name=display_name,
        default_language_code="en",
        time_zone="America/Los_Angeles",
    )

    agents_client.set_agent(request={"agent": agent})


def list_agent(project_id):
    parent = "projects/" + project_id
    agents_client = AgentsClient()
    agent = SearchAgentsRequest(parent=parent)
    response = agents_client.search_agents(agent)
    return len(response._response.agents)


def delete_agent(project_id):
    parent = "projects/" + project_id
    agents_client = AgentsClient()
    agent = DeleteAgentRequest(parent=parent)
    agents_client.delete_agent(agent)


def list_intent(project_id):
    intents_client = IntentsClient()

    parent = AgentsClient.agent_path(project_id)

    intents = intents_client.list_intents(request={"parent": parent})

    for intent in intents:
        return intent.name.split("/")[4]

@pytest.fixture(scope="function", autouse=True)
def setup_teardown():
    if list_agent(PROJECT_ID) > 0:
        delete_agent(PROJECT_ID)
        print("Deleted in setUp")
        today = date.today()
        agentName = "tempAgent." + today.strftime("%d.%m.%Y")
        create_agent(PROJECT_ID, agentName)
        print("Created Agent in setUp")
        pytest.INTENT_ID = list_intent(project_id=PROJECT_ID or "")
        print("Created Intent in setUp")
    else:
        today = date.today()
        agentName = "tempAgent." + today.strftime("%d.%m.%Y")
        create_agent(PROJECT_ID, agentName)
        print("Created Agent in setUp")
        pytest.INTENT_ID = list_intent(project_id=PROJECT_ID or "")
        print("Created Intent in setUp")
    
    yield

    delete_agent(PROJECT_ID)
    print("Deleted in tearDown")
    
def test_update_intent():
        actualResponse = update_intent(
            PROJECT_ID or "", pytest.INTENT_ID, "Updated Intent"
        )
        expectedResponse = "Updated Intent"
        assert actualResponse.display_name == expectedResponse


