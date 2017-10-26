# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow_v2beta1/proto/tier.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dialogflow_v2beta1/proto/tier.proto',
  package='google.cloud.dialogflow.v2beta1',
  syntax='proto3',
  serialized_pb=_b('\n0google/cloud/dialogflow_v2beta1/proto/tier.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"@\n\tAgentTier\x12\x33\n\x04tier\x18\x01 \x01(\x0e\x32%.google.cloud.dialogflow.v2beta1.Tier\"#\n\x13GetAgentTierRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x97\x01\n\x16UpdateAgentTierRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\nagent_tier\x18\x02 \x01(\x0b\x32*.google.cloud.dialogflow.v2beta1.AgentTier\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask*D\n\x04Tier\x12\x14\n\x10TIER_UNSPECIFIED\x10\x00\x12\x11\n\rTIER_STANDARD\x10\x01\x12\x13\n\x0fTIER_ENTERPRISE\x10\x02\x32\xdd\x02\n\x05Tiers\x12\x9f\x01\n\x0cGetAgentTier\x12\x34.google.cloud.dialogflow.v2beta1.GetAgentTierRequest\x1a*.google.cloud.dialogflow.v2beta1.AgentTier\"-\x82\xd3\xe4\x93\x02\'\x12%/v2beta1/{name=projects/*/agent/tier}\x12\xb1\x01\n\x0fUpdateAgentTier\x12\x37.google.cloud.dialogflow.v2beta1.UpdateAgentTierRequest\x1a*.google.cloud.dialogflow.v2beta1.AgentTier\"9\x82\xd3\xe4\x93\x02\x33\"%/v2beta1/{name=projects/*/agent/tier}:\nagent_tierB\x80\x01\n#com.google.cloud.dialogflow.v2beta1B\tTierProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])

_TIER = _descriptor.EnumDescriptor(
  name='Tier',
  full_name='google.cloud.dialogflow.v2beta1.Tier',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TIER_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIER_STANDARD', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIER_ENTERPRISE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=406,
  serialized_end=474,
)
_sym_db.RegisterEnumDescriptor(_TIER)

Tier = enum_type_wrapper.EnumTypeWrapper(_TIER)
TIER_UNSPECIFIED = 0
TIER_STANDARD = 1
TIER_ENTERPRISE = 2



_AGENTTIER = _descriptor.Descriptor(
  name='AgentTier',
  full_name='google.cloud.dialogflow.v2beta1.AgentTier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tier', full_name='google.cloud.dialogflow.v2beta1.AgentTier.tier', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=213,
)


_GETAGENTTIERREQUEST = _descriptor.Descriptor(
  name='GetAgentTierRequest',
  full_name='google.cloud.dialogflow.v2beta1.GetAgentTierRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.GetAgentTierRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=250,
)


_UPDATEAGENTTIERREQUEST = _descriptor.Descriptor(
  name='UpdateAgentTierRequest',
  full_name='google.cloud.dialogflow.v2beta1.UpdateAgentTierRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.UpdateAgentTierRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agent_tier', full_name='google.cloud.dialogflow.v2beta1.UpdateAgentTierRequest.agent_tier', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.dialogflow.v2beta1.UpdateAgentTierRequest.update_mask', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=404,
)

_AGENTTIER.fields_by_name['tier'].enum_type = _TIER
_UPDATEAGENTTIERREQUEST.fields_by_name['agent_tier'].message_type = _AGENTTIER
_UPDATEAGENTTIERREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['AgentTier'] = _AGENTTIER
DESCRIPTOR.message_types_by_name['GetAgentTierRequest'] = _GETAGENTTIERREQUEST
DESCRIPTOR.message_types_by_name['UpdateAgentTierRequest'] = _UPDATEAGENTTIERREQUEST
DESCRIPTOR.enum_types_by_name['Tier'] = _TIER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgentTier = _reflection.GeneratedProtocolMessageType('AgentTier', (_message.Message,), dict(
  DESCRIPTOR = _AGENTTIER,
  __module__ = 'google.cloud.dialogflow_v2beta1.proto.tier_pb2'
  ,
  __doc__ = """Represents the agent tier.
  
  
  Attributes:
      tier:
          Required. The agent tier.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.AgentTier)
  ))
_sym_db.RegisterMessage(AgentTier)

GetAgentTierRequest = _reflection.GeneratedProtocolMessageType('GetAgentTierRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETAGENTTIERREQUEST,
  __module__ = 'google.cloud.dialogflow_v2beta1.proto.tier_pb2'
  ,
  __doc__ = """The request message for [Tiers.GetAgentTier].
  
  
  Attributes:
      name:
          Required. The project to retrieve the tier of. Format:
          ``projects/<Project ID>``.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.GetAgentTierRequest)
  ))
_sym_db.RegisterMessage(GetAgentTierRequest)

UpdateAgentTierRequest = _reflection.GeneratedProtocolMessageType('UpdateAgentTierRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEAGENTTIERREQUEST,
  __module__ = 'google.cloud.dialogflow_v2beta1.proto.tier_pb2'
  ,
  __doc__ = """The request message for [Tiers.UpdateAgentTier].
  
  
  Attributes:
      name:
          Required. The project to update the tier of. Format:
          ``projects/<Project ID>``.
      agent_tier:
          Required. The agent tier.
      update_mask:
          Optional. The mask to control which fields get updated.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.UpdateAgentTierRequest)
  ))
_sym_db.RegisterMessage(UpdateAgentTierRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#com.google.cloud.dialogflow.v2beta1B\tTierProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class TiersStub(object):
    """# Manages agent tier.

    Standard methods.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetAgentTier = channel.unary_unary(
          '/google.cloud.dialogflow.v2beta1.Tiers/GetAgentTier',
          request_serializer=GetAgentTierRequest.SerializeToString,
          response_deserializer=AgentTier.FromString,
          )
      self.UpdateAgentTier = channel.unary_unary(
          '/google.cloud.dialogflow.v2beta1.Tiers/UpdateAgentTier',
          request_serializer=UpdateAgentTierRequest.SerializeToString,
          response_deserializer=AgentTier.FromString,
          )


  class TiersServicer(object):
    """# Manages agent tier.

    Standard methods.
    """

    def GetAgentTier(self, request, context):
      """Retrieves the tier of the specified agent.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def UpdateAgentTier(self, request, context):
      """Updates the tier of the specified agent.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_TiersServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAgentTier': grpc.unary_unary_rpc_method_handler(
            servicer.GetAgentTier,
            request_deserializer=GetAgentTierRequest.FromString,
            response_serializer=AgentTier.SerializeToString,
        ),
        'UpdateAgentTier': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateAgentTier,
            request_deserializer=UpdateAgentTierRequest.FromString,
            response_serializer=AgentTier.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'google.cloud.dialogflow.v2beta1.Tiers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTiersServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """# Manages agent tier.

    Standard methods.
    """
    def GetAgentTier(self, request, context):
      """Retrieves the tier of the specified agent.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def UpdateAgentTier(self, request, context):
      """Updates the tier of the specified agent.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTiersStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """# Manages agent tier.

    Standard methods.
    """
    def GetAgentTier(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Retrieves the tier of the specified agent.
      """
      raise NotImplementedError()
    GetAgentTier.future = None
    def UpdateAgentTier(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Updates the tier of the specified agent.
      """
      raise NotImplementedError()
    UpdateAgentTier.future = None


  def beta_create_Tiers_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('google.cloud.dialogflow.v2beta1.Tiers', 'GetAgentTier'): GetAgentTierRequest.FromString,
      ('google.cloud.dialogflow.v2beta1.Tiers', 'UpdateAgentTier'): UpdateAgentTierRequest.FromString,
    }
    response_serializers = {
      ('google.cloud.dialogflow.v2beta1.Tiers', 'GetAgentTier'): AgentTier.SerializeToString,
      ('google.cloud.dialogflow.v2beta1.Tiers', 'UpdateAgentTier'): AgentTier.SerializeToString,
    }
    method_implementations = {
      ('google.cloud.dialogflow.v2beta1.Tiers', 'GetAgentTier'): face_utilities.unary_unary_inline(servicer.GetAgentTier),
      ('google.cloud.dialogflow.v2beta1.Tiers', 'UpdateAgentTier'): face_utilities.unary_unary_inline(servicer.UpdateAgentTier),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Tiers_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('google.cloud.dialogflow.v2beta1.Tiers', 'GetAgentTier'): GetAgentTierRequest.SerializeToString,
      ('google.cloud.dialogflow.v2beta1.Tiers', 'UpdateAgentTier'): UpdateAgentTierRequest.SerializeToString,
    }
    response_deserializers = {
      ('google.cloud.dialogflow.v2beta1.Tiers', 'GetAgentTier'): AgentTier.FromString,
      ('google.cloud.dialogflow.v2beta1.Tiers', 'UpdateAgentTier'): AgentTier.FromString,
    }
    cardinalities = {
      'GetAgentTier': cardinality.Cardinality.UNARY_UNARY,
      'UpdateAgentTier': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'google.cloud.dialogflow.v2beta1.Tiers', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)