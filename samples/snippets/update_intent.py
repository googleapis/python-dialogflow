from google.cloud.dialogflow_v2 import IntentsClient
from google.protobuf import field_mask_pb2


def update_intent(project_id, intent_id, display_name):
    intents_client = IntentsClient()

    intent_name = intents_client.intent_path(project_id, intent_id)
    intent = intents_client.get_intent(request={"name": intent_name})

    intent.display_name = display_name
    update_mask = field_mask_pb2.FieldMask(paths=["display_name"])
    response = intents_client.update_intent(
        intent=intent, update_mask=update_mask, language_code="en"
    )
    return response
