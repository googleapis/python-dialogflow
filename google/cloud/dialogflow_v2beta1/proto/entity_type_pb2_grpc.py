# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.dialogflow_v2beta1.proto import entity_type_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class EntityTypesStub(object):
  """Manages agent entity types.


  Refer to [documentation](https://dialogflow.com/docs/entities) for more
  # details about entity types.

  Standard methods.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListEntityTypes = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.EntityTypes/ListEntityTypes',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.ListEntityTypesRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.ListEntityTypesResponse.FromString,
        )
    self.GetEntityType = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.EntityTypes/GetEntityType',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.GetEntityTypeRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.EntityType.FromString,
        )
    self.CreateEntityType = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.EntityTypes/CreateEntityType',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.CreateEntityTypeRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.EntityType.FromString,
        )
    self.UpdateEntityType = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.EntityTypes/UpdateEntityType',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.UpdateEntityTypeRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.EntityType.FromString,
        )
    self.DeleteEntityType = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.EntityTypes/DeleteEntityType',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.DeleteEntityTypeRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.BatchUpdateEntityTypes = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.EntityTypes/BatchUpdateEntityTypes',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.BatchUpdateEntityTypesRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.BatchDeleteEntityTypes = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.EntityTypes/BatchDeleteEntityTypes',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.BatchDeleteEntityTypesRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.BatchCreateEntities = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.EntityTypes/BatchCreateEntities',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.BatchCreateEntitiesRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.BatchUpdateEntities = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.EntityTypes/BatchUpdateEntities',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.BatchUpdateEntitiesRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.BatchDeleteEntities = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.EntityTypes/BatchDeleteEntities',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.BatchDeleteEntitiesRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class EntityTypesServicer(object):
  """Manages agent entity types.


  Refer to [documentation](https://dialogflow.com/docs/entities) for more
  # details about entity types.

  Standard methods.
  """

  def ListEntityTypes(self, request, context):
    """Returns the list of all entity types in the specified agent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEntityType(self, request, context):
    """Retrieves the specified entity type.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateEntityType(self, request, context):
    """Creates an entity type in the specified agent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateEntityType(self, request, context):
    """Updates the specified entity type.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteEntityType(self, request, context):
    """Deletes the specified entity type.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchUpdateEntityTypes(self, request, context):
    """Updates/Creates multiple entity types in the specified agent.

    Operation<response: BatchUpdateEntityTypesResponse,
    metadata: google.protobuf.Struct>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchDeleteEntityTypes(self, request, context):
    """Deletes entity types in the specified agent.

    Operation<response: google.protobuf.Empty,
    metadata: google.protobuf.Struct>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchCreateEntities(self, request, context):
    """Creates multiple new entities in the specified entity type (extends the
    existing collection of entries).

    Operation<response: google.protobuf.Empty>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchUpdateEntities(self, request, context):
    """Updates entities in the specified entity type (replaces the existing
    collection of entries).

    Operation<response: google.protobuf.Empty,
    metadata: google.protobuf.Struct>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchDeleteEntities(self, request, context):
    """Deletes entities in the specified entity type.

    Operation<response: google.protobuf.Empty,
    metadata: google.protobuf.Struct>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EntityTypesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListEntityTypes': grpc.unary_unary_rpc_method_handler(
          servicer.ListEntityTypes,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.ListEntityTypesRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.ListEntityTypesResponse.SerializeToString,
      ),
      'GetEntityType': grpc.unary_unary_rpc_method_handler(
          servicer.GetEntityType,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.GetEntityTypeRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.EntityType.SerializeToString,
      ),
      'CreateEntityType': grpc.unary_unary_rpc_method_handler(
          servicer.CreateEntityType,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.CreateEntityTypeRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.EntityType.SerializeToString,
      ),
      'UpdateEntityType': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateEntityType,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.UpdateEntityTypeRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.EntityType.SerializeToString,
      ),
      'DeleteEntityType': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteEntityType,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.DeleteEntityTypeRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'BatchUpdateEntityTypes': grpc.unary_unary_rpc_method_handler(
          servicer.BatchUpdateEntityTypes,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.BatchUpdateEntityTypesRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'BatchDeleteEntityTypes': grpc.unary_unary_rpc_method_handler(
          servicer.BatchDeleteEntityTypes,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.BatchDeleteEntityTypesRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'BatchCreateEntities': grpc.unary_unary_rpc_method_handler(
          servicer.BatchCreateEntities,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.BatchCreateEntitiesRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'BatchUpdateEntities': grpc.unary_unary_rpc_method_handler(
          servicer.BatchUpdateEntities,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.BatchUpdateEntitiesRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'BatchDeleteEntities': grpc.unary_unary_rpc_method_handler(
          servicer.BatchDeleteEntities,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_entity__type__pb2.BatchDeleteEntitiesRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.dialogflow.v2beta1.EntityTypes', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
