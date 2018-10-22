# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from dialogflow_v2.proto import agent_pb2 as google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


class AgentsStub(object):
  """Agents are best described as Natural Language Understanding (NLU) modules
  that transform user requests into actionable data. You can include agents
  in your app, product, or service to determine user intent and respond to the
  user in a natural way.

  After you create an agent, you can add [Intents][google.cloud.dialogflow.v2.Intents], [Contexts][google.cloud.dialogflow.v2.Contexts],
  [Entity Types][google.cloud.dialogflow.v2.EntityTypes], [Webhooks][google.cloud.dialogflow.v2.WebhookRequest], and so on to
  manage the flow of a conversation and match user input to predefined intents
  and actions.

  You can create an agent using both Dialogflow Standard Edition and
  Dialogflow Enterprise Edition. For details, see
  [Dialogflow Editions](/dialogflow-enterprise/docs/editions).

  You can save your agent for backup or versioning by exporting the agent by
  using the [ExportAgent][google.cloud.dialogflow.v2.Agents.ExportAgent] method. You can import a saved
  agent by using the [ImportAgent][google.cloud.dialogflow.v2.Agents.ImportAgent] method.

  Dialogflow provides several
  [prebuilt agents](https://dialogflow.com/docs/prebuilt-agents) for common
  conversation scenarios such as determining a date and time, converting
  currency, and so on.

  For more information about agents, see the
  [Dialogflow documentation](https://dialogflow.com/docs/agents).
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Agents/GetAgent',
        request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.GetAgentRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.Agent.FromString,
        )
    self.SearchAgents = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Agents/SearchAgents',
        request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.SearchAgentsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.SearchAgentsResponse.FromString,
        )
    self.TrainAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Agents/TrainAgent',
        request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.TrainAgentRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.ExportAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Agents/ExportAgent',
        request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.ExportAgentRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.ImportAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Agents/ImportAgent',
        request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.ImportAgentRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.RestoreAgent = channel.unary_unary(
        '/google.cloud.dialogflow.v2.Agents/RestoreAgent',
        request_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.RestoreAgentRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class AgentsServicer(object):
  """Agents are best described as Natural Language Understanding (NLU) modules
  that transform user requests into actionable data. You can include agents
  in your app, product, or service to determine user intent and respond to the
  user in a natural way.

  After you create an agent, you can add [Intents][google.cloud.dialogflow.v2.Intents], [Contexts][google.cloud.dialogflow.v2.Contexts],
  [Entity Types][google.cloud.dialogflow.v2.EntityTypes], [Webhooks][google.cloud.dialogflow.v2.WebhookRequest], and so on to
  manage the flow of a conversation and match user input to predefined intents
  and actions.

  You can create an agent using both Dialogflow Standard Edition and
  Dialogflow Enterprise Edition. For details, see
  [Dialogflow Editions](/dialogflow-enterprise/docs/editions).

  You can save your agent for backup or versioning by exporting the agent by
  using the [ExportAgent][google.cloud.dialogflow.v2.Agents.ExportAgent] method. You can import a saved
  agent by using the [ImportAgent][google.cloud.dialogflow.v2.Agents.ImportAgent] method.

  Dialogflow provides several
  [prebuilt agents](https://dialogflow.com/docs/prebuilt-agents) for common
  conversation scenarios such as determining a date and time, converting
  currency, and so on.

  For more information about agents, see the
  [Dialogflow documentation](https://dialogflow.com/docs/agents).
  """

  def GetAgent(self, request, context):
    """Retrieves the specified agent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchAgents(self, request, context):
    """Returns the list of agents.

    Since there is at most one conversational agent per project, this method is
    useful primarily for listing all agents across projects the caller has
    access to. One can achieve that with a wildcard project collection id "-".
    Refer to [List
    Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TrainAgent(self, request, context):
    """Trains the specified agent.

    Operation <response: [google.protobuf.Empty][google.protobuf.Empty],
    metadata: [google.protobuf.Struct][google.protobuf.Struct]>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExportAgent(self, request, context):
    """Exports the specified agent to a ZIP file.

    Operation <response: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse],
    metadata: [google.protobuf.Struct][google.protobuf.Struct]>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ImportAgent(self, request, context):
    """Imports the specified agent from a ZIP file.

    Uploads new intents and entity types without deleting the existing ones.
    Intents and entity types with the same name are replaced with the new
    versions from ImportAgentRequest.

    Operation <response: [google.protobuf.Empty][google.protobuf.Empty],
    metadata: [google.protobuf.Struct][google.protobuf.Struct]>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestoreAgent(self, request, context):
    """Restores the specified agent from a ZIP file.

    Replaces the current agent version with a new one. All the intents and
    entity types in the older version are deleted.

    Operation <response: [google.protobuf.Empty][google.protobuf.Empty],
    metadata: [google.protobuf.Struct][google.protobuf.Struct]>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AgentsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAgent': grpc.unary_unary_rpc_method_handler(
          servicer.GetAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.GetAgentRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.Agent.SerializeToString,
      ),
      'SearchAgents': grpc.unary_unary_rpc_method_handler(
          servicer.SearchAgents,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.SearchAgentsRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.SearchAgentsResponse.SerializeToString,
      ),
      'TrainAgent': grpc.unary_unary_rpc_method_handler(
          servicer.TrainAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.TrainAgentRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'ExportAgent': grpc.unary_unary_rpc_method_handler(
          servicer.ExportAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.ExportAgentRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'ImportAgent': grpc.unary_unary_rpc_method_handler(
          servicer.ImportAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.ImportAgentRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'RestoreAgent': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreAgent,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_agent__pb2.RestoreAgentRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.dialogflow.v2.Agents', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
