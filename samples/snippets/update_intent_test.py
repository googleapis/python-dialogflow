import os
import unittest
from datetime import date
from google.cloud.dialogflow_v2.services.agents.client import AgentsClient
from google.cloud.dialogflow_v2.services.intents.client import IntentsClient
from google.cloud.dialogflow_v2 import Agent
from google.cloud.dialogflow_v2.types.agent import (
    DeleteAgentRequest,
    SearchAgentsRequest,
)

from update_intent_ES import updateIntent


os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = "/Users/galzahavi/Documents/Dialogflow Snippets/valiant-marker-319718-a597e6688ab0.json"
os.environ["GOOGLE_CLOUD_PROJECT"] = "valiant-marker-319718"

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")


def create_agent(project_id, display_name):
    parent = "projects/" + project_id
    agents_client = AgentsClient()
    agent = Agent(
        parent=parent,
        display_name=display_name,
        default_language_code="en",
        time_zone="America/Los_Angeles",
    )

    response = agents_client.set_agent(request={"agent": agent})


def list_agent(self, project_id):
    parent = "projects/" + project_id
    agents_client = AgentsClient()
    agent = SearchAgentsRequest(parent=parent)
    response = agents_client.search_agents(agent)
    return len(response._response.agents)


def delete_agent(self, project_id):
    parent = "projects/" + project_id
    agents_client = AgentsClient()
    agent = DeleteAgentRequest(parent=parent)
    agents_client.delete_agent(agent)


def list_intent(self, project_id):
    intents_client = IntentsClient()

    parent = AgentsClient.agent_path(project_id)

    intents = intents_client.list_intents(request={"parent": parent})

    for intent in intents:
        return intent.name.split("/")[4]


class fieldmaskTest(unittest.TestCase):
    def setUp(self):
        parent_id = PROJECT_ID or ""
        if self.list_agent(parent_id) > 0:
            self.delete_agent(parent_id)
            print("Deleted in setUp")
            today = date.today()
            agentName = "tempAgent." + today.strftime("%d.%m.%Y")
            create_agent(PROJECT_ID or "", agentName)
            print("Created Agent in setUp")
            self.intent_id = self.list_intent(project_id=PROJECT_ID or "")
            print("Created Intent in setUp")
        else:
            today = date.today()
            agentName = "tempAgent." + today.strftime("%d.%m.%Y")
            create_agent(PROJECT_ID or "", agentName)
            print("Created Agent in setUp")
            self.intent_id = self.list_intent(project_id=PROJECT_ID or "")
            print("Created Intent in setUp")

    def test_update_intent(self):
        actualResponse = updateIntent(
            PROJECT_ID or "", self.intent_id, "Updated Intent"
        )
        expectedResponse = "Updated Intent"
        self.assertEqual(actualResponse.display_name, expectedResponse)

    def tearDown(self):
        parent_id = PROJECT_ID or ""
        if self.list_agent(parent_id) > 0:
            self.delete_agent(parent_id)
            print("Deleted in tearDown")


if __name__ == "__main__":
    unittest.main()
