# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow_v2beta1/proto/version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dialogflow_v2beta1/proto/version.proto',
  package='google.cloud.dialogflow.v2beta1',
  syntax='proto3',
  serialized_pb=_b('\n3google/cloud/dialogflow_v2beta1/proto/version.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"u\n\x07Version\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x16\n\x0eversion_number\x18\x03 \x01(\x05\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"L\n\x13ListVersionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"k\n\x14ListVersionsResponse\x12:\n\x08versions\x18\x01 \x03(\x0b\x32(.google.cloud.dialogflow.v2beta1.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"!\n\x11GetVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"a\n\x14\x43reateVersionRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x39\n\x07version\x18\x02 \x01(\x0b\x32(.google.cloud.dialogflow.v2beta1.Version\"\x82\x01\n\x14UpdateVersionRequest\x12\x39\n\x07version\x18\x01 \x01(\x0b\x32(.google.cloud.dialogflow.v2beta1.Version\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"$\n\x14\x44\x65leteVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xdf\x06\n\x08Versions\x12\xb0\x01\n\x0cListVersions\x12\x34.google.cloud.dialogflow.v2beta1.ListVersionsRequest\x1a\x35.google.cloud.dialogflow.v2beta1.ListVersionsResponse\"3\x82\xd3\xe4\x93\x02-\x12+/v2beta1/{parent=projects/*/agent}/versions\x12\x9f\x01\n\nGetVersion\x12\x32.google.cloud.dialogflow.v2beta1.GetVersionRequest\x1a(.google.cloud.dialogflow.v2beta1.Version\"3\x82\xd3\xe4\x93\x02-\x12+/v2beta1/{name=projects/*/agent/versions/*}\x12\xae\x01\n\rCreateVersion\x12\x35.google.cloud.dialogflow.v2beta1.CreateVersionRequest\x1a(.google.cloud.dialogflow.v2beta1.Version\"<\x82\xd3\xe4\x93\x02\x36\"+/v2beta1/{parent=projects/*/agent}/versions:\x07version\x12\xb6\x01\n\rUpdateVersion\x12\x35.google.cloud.dialogflow.v2beta1.UpdateVersionRequest\x1a(.google.cloud.dialogflow.v2beta1.Version\"D\x82\xd3\xe4\x93\x02>23/v2beta1/{version.name=projects/*/agent/versions/*}:\x07version\x12\x93\x01\n\rDeleteVersion\x12\x35.google.cloud.dialogflow.v2beta1.DeleteVersionRequest\x1a\x16.google.protobuf.Empty\"3\x82\xd3\xe4\x93\x02-*+/v2beta1/{name=projects/*/agent/versions/*}B\x83\x01\n#com.google.cloud.dialogflow.v2beta1B\x0cVersionProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='google.cloud.dialogflow.v2beta1.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.Version.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.dialogflow.v2beta1.Version.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version_number', full_name='google.cloud.dialogflow.v2beta1.Version.version_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.dialogflow.v2beta1.Version.create_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=214,
  serialized_end=331,
)


_LISTVERSIONSREQUEST = _descriptor.Descriptor(
  name='ListVersionsRequest',
  full_name='google.cloud.dialogflow.v2beta1.ListVersionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2beta1.ListVersionsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.dialogflow.v2beta1.ListVersionsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.dialogflow.v2beta1.ListVersionsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=333,
  serialized_end=409,
)


_LISTVERSIONSRESPONSE = _descriptor.Descriptor(
  name='ListVersionsResponse',
  full_name='google.cloud.dialogflow.v2beta1.ListVersionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='versions', full_name='google.cloud.dialogflow.v2beta1.ListVersionsResponse.versions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.dialogflow.v2beta1.ListVersionsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=411,
  serialized_end=518,
)


_GETVERSIONREQUEST = _descriptor.Descriptor(
  name='GetVersionRequest',
  full_name='google.cloud.dialogflow.v2beta1.GetVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.GetVersionRequest.name', index=0,
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
  serialized_start=520,
  serialized_end=553,
)


_CREATEVERSIONREQUEST = _descriptor.Descriptor(
  name='CreateVersionRequest',
  full_name='google.cloud.dialogflow.v2beta1.CreateVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2beta1.CreateVersionRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='google.cloud.dialogflow.v2beta1.CreateVersionRequest.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=555,
  serialized_end=652,
)


_UPDATEVERSIONREQUEST = _descriptor.Descriptor(
  name='UpdateVersionRequest',
  full_name='google.cloud.dialogflow.v2beta1.UpdateVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='google.cloud.dialogflow.v2beta1.UpdateVersionRequest.version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.dialogflow.v2beta1.UpdateVersionRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=655,
  serialized_end=785,
)


_DELETEVERSIONREQUEST = _descriptor.Descriptor(
  name='DeleteVersionRequest',
  full_name='google.cloud.dialogflow.v2beta1.DeleteVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.DeleteVersionRequest.name', index=0,
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
  serialized_start=787,
  serialized_end=823,
)

_VERSION.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTVERSIONSRESPONSE.fields_by_name['versions'].message_type = _VERSION
_CREATEVERSIONREQUEST.fields_by_name['version'].message_type = _VERSION
_UPDATEVERSIONREQUEST.fields_by_name['version'].message_type = _VERSION
_UPDATEVERSIONREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['ListVersionsRequest'] = _LISTVERSIONSREQUEST
DESCRIPTOR.message_types_by_name['ListVersionsResponse'] = _LISTVERSIONSRESPONSE
DESCRIPTOR.message_types_by_name['GetVersionRequest'] = _GETVERSIONREQUEST
DESCRIPTOR.message_types_by_name['CreateVersionRequest'] = _CREATEVERSIONREQUEST
DESCRIPTOR.message_types_by_name['UpdateVersionRequest'] = _UPDATEVERSIONREQUEST
DESCRIPTOR.message_types_by_name['DeleteVersionRequest'] = _DELETEVERSIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), dict(
  DESCRIPTOR = _VERSION,
  __module__ = 'google.cloud.dialogflow_v2beta1.proto.version_pb2'
  ,
  __doc__ = """Represents an agent version.
  
  
  Attributes:
      name:
          Required. The unique identifier of this agent version. Format:
          ``projects/<Project ID>/agent/versions/<Version ID>``.
      description:
          Optional. The developer-provided description of this version.
      version_number:
          The sequential number of this version. This field is read-
          only, i.e., it cannot be set by create and update methods.
      create_time:
          The creation time of this version. This field is read-only,
          i.e., it cannot be set by create and update methods.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.Version)
  ))
_sym_db.RegisterMessage(Version)

ListVersionsRequest = _reflection.GeneratedProtocolMessageType('ListVersionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTVERSIONSREQUEST,
  __module__ = 'google.cloud.dialogflow_v2beta1.proto.version_pb2'
  ,
  __doc__ = """The request message for [Versions.ListVersions].
  
  
  Attributes:
      parent:
          Required. The agent to list all versions from. Format:
          ``projects/<Project ID>/agent``.
      page_size:
          Optional. The maximum number of items to return in a single
          page. By default 100 and at most 1000.
      page_token:
          Optional. The next\_page\_token value returned from a previous
          list request.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListVersionsRequest)
  ))
_sym_db.RegisterMessage(ListVersionsRequest)

ListVersionsResponse = _reflection.GeneratedProtocolMessageType('ListVersionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTVERSIONSRESPONSE,
  __module__ = 'google.cloud.dialogflow_v2beta1.proto.version_pb2'
  ,
  __doc__ = """The response message for [Versions.ListVersions].
  
  
  Attributes:
      versions:
          The list of agent versions. There will be a maximum number of
          items returned based on the page\_size field in the request.
      next_page_token:
          Token to retrieve the next page of results, or empty if there
          are no more results in the list.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListVersionsResponse)
  ))
_sym_db.RegisterMessage(ListVersionsResponse)

GetVersionRequest = _reflection.GeneratedProtocolMessageType('GetVersionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVERSIONREQUEST,
  __module__ = 'google.cloud.dialogflow_v2beta1.proto.version_pb2'
  ,
  __doc__ = """The request message for [Versions.GetVersion].
  
  
  Attributes:
      name:
          Required. The name of the version. Format: ``projects/<Project
          ID>/agent/versions/<Version ID>``.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.GetVersionRequest)
  ))
_sym_db.RegisterMessage(GetVersionRequest)

CreateVersionRequest = _reflection.GeneratedProtocolMessageType('CreateVersionRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEVERSIONREQUEST,
  __module__ = 'google.cloud.dialogflow_v2beta1.proto.version_pb2'
  ,
  __doc__ = """The request message for [Versions.CreateVersion].
  
  
  Attributes:
      parent:
          Required. The agent to create a version for. Format:
          ``projects/<Project ID>/agent``.
      version:
          Required. The version to create.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.CreateVersionRequest)
  ))
_sym_db.RegisterMessage(CreateVersionRequest)

UpdateVersionRequest = _reflection.GeneratedProtocolMessageType('UpdateVersionRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEVERSIONREQUEST,
  __module__ = 'google.cloud.dialogflow_v2beta1.proto.version_pb2'
  ,
  __doc__ = """The request message for [Versions.UpdateVersion].
  
  
  Attributes:
      version:
          Required. The version to update. Format: ``projects/<Project
          ID>/agent/versions/<Version ID>``.
      update_mask:
          Optional. The mask to control which fields get updated.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.UpdateVersionRequest)
  ))
_sym_db.RegisterMessage(UpdateVersionRequest)

DeleteVersionRequest = _reflection.GeneratedProtocolMessageType('DeleteVersionRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEVERSIONREQUEST,
  __module__ = 'google.cloud.dialogflow_v2beta1.proto.version_pb2'
  ,
  __doc__ = """The request message for [Versions.DeleteVersion].
  
  
  Attributes:
      name:
          Required. The name of the version to delete. Format:
          ``projects/<Project ID>/agent/versions/<Version ID>``.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.DeleteVersionRequest)
  ))
_sym_db.RegisterMessage(DeleteVersionRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#com.google.cloud.dialogflow.v2beta1B\014VersionProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class VersionsStub(object):
    """Manages agent versions.


    Standard methods.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.ListVersions = channel.unary_unary(
          '/google.cloud.dialogflow.v2beta1.Versions/ListVersions',
          request_serializer=ListVersionsRequest.SerializeToString,
          response_deserializer=ListVersionsResponse.FromString,
          )
      self.GetVersion = channel.unary_unary(
          '/google.cloud.dialogflow.v2beta1.Versions/GetVersion',
          request_serializer=GetVersionRequest.SerializeToString,
          response_deserializer=Version.FromString,
          )
      self.CreateVersion = channel.unary_unary(
          '/google.cloud.dialogflow.v2beta1.Versions/CreateVersion',
          request_serializer=CreateVersionRequest.SerializeToString,
          response_deserializer=Version.FromString,
          )
      self.UpdateVersion = channel.unary_unary(
          '/google.cloud.dialogflow.v2beta1.Versions/UpdateVersion',
          request_serializer=UpdateVersionRequest.SerializeToString,
          response_deserializer=Version.FromString,
          )
      self.DeleteVersion = channel.unary_unary(
          '/google.cloud.dialogflow.v2beta1.Versions/DeleteVersion',
          request_serializer=DeleteVersionRequest.SerializeToString,
          response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          )


  class VersionsServicer(object):
    """Manages agent versions.


    Standard methods.
    """

    def ListVersions(self, request, context):
      """Returns the list of all versions of the specified agent.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetVersion(self, request, context):
      """Retrieves the specified agent version.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def CreateVersion(self, request, context):
      """Creates an agent version.

      The new version points to the agent instance in the "default" runtime.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def UpdateVersion(self, request, context):
      """Updates the specified agent version.

      Note that this method does not allow you to update the state of the agent
      the given version points to. It allows you to update only mutable
      properties of the version resource.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def DeleteVersion(self, request, context):
      """Deletes the specified agent version.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_VersionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ListVersions': grpc.unary_unary_rpc_method_handler(
            servicer.ListVersions,
            request_deserializer=ListVersionsRequest.FromString,
            response_serializer=ListVersionsResponse.SerializeToString,
        ),
        'GetVersion': grpc.unary_unary_rpc_method_handler(
            servicer.GetVersion,
            request_deserializer=GetVersionRequest.FromString,
            response_serializer=Version.SerializeToString,
        ),
        'CreateVersion': grpc.unary_unary_rpc_method_handler(
            servicer.CreateVersion,
            request_deserializer=CreateVersionRequest.FromString,
            response_serializer=Version.SerializeToString,
        ),
        'UpdateVersion': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateVersion,
            request_deserializer=UpdateVersionRequest.FromString,
            response_serializer=Version.SerializeToString,
        ),
        'DeleteVersion': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteVersion,
            request_deserializer=DeleteVersionRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'google.cloud.dialogflow.v2beta1.Versions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaVersionsServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """Manages agent versions.


    Standard methods.
    """
    def ListVersions(self, request, context):
      """Returns the list of all versions of the specified agent.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetVersion(self, request, context):
      """Retrieves the specified agent version.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def CreateVersion(self, request, context):
      """Creates an agent version.

      The new version points to the agent instance in the "default" runtime.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def UpdateVersion(self, request, context):
      """Updates the specified agent version.

      Note that this method does not allow you to update the state of the agent
      the given version points to. It allows you to update only mutable
      properties of the version resource.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def DeleteVersion(self, request, context):
      """Deletes the specified agent version.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaVersionsStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """Manages agent versions.


    Standard methods.
    """
    def ListVersions(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Returns the list of all versions of the specified agent.
      """
      raise NotImplementedError()
    ListVersions.future = None
    def GetVersion(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Retrieves the specified agent version.
      """
      raise NotImplementedError()
    GetVersion.future = None
    def CreateVersion(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Creates an agent version.

      The new version points to the agent instance in the "default" runtime.
      """
      raise NotImplementedError()
    CreateVersion.future = None
    def UpdateVersion(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Updates the specified agent version.

      Note that this method does not allow you to update the state of the agent
      the given version points to. It allows you to update only mutable
      properties of the version resource.
      """
      raise NotImplementedError()
    UpdateVersion.future = None
    def DeleteVersion(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """Deletes the specified agent version.
      """
      raise NotImplementedError()
    DeleteVersion.future = None


  def beta_create_Versions_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('google.cloud.dialogflow.v2beta1.Versions', 'CreateVersion'): CreateVersionRequest.FromString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'DeleteVersion'): DeleteVersionRequest.FromString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'GetVersion'): GetVersionRequest.FromString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'ListVersions'): ListVersionsRequest.FromString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'UpdateVersion'): UpdateVersionRequest.FromString,
    }
    response_serializers = {
      ('google.cloud.dialogflow.v2beta1.Versions', 'CreateVersion'): Version.SerializeToString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'DeleteVersion'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'GetVersion'): Version.SerializeToString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'ListVersions'): ListVersionsResponse.SerializeToString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'UpdateVersion'): Version.SerializeToString,
    }
    method_implementations = {
      ('google.cloud.dialogflow.v2beta1.Versions', 'CreateVersion'): face_utilities.unary_unary_inline(servicer.CreateVersion),
      ('google.cloud.dialogflow.v2beta1.Versions', 'DeleteVersion'): face_utilities.unary_unary_inline(servicer.DeleteVersion),
      ('google.cloud.dialogflow.v2beta1.Versions', 'GetVersion'): face_utilities.unary_unary_inline(servicer.GetVersion),
      ('google.cloud.dialogflow.v2beta1.Versions', 'ListVersions'): face_utilities.unary_unary_inline(servicer.ListVersions),
      ('google.cloud.dialogflow.v2beta1.Versions', 'UpdateVersion'): face_utilities.unary_unary_inline(servicer.UpdateVersion),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Versions_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('google.cloud.dialogflow.v2beta1.Versions', 'CreateVersion'): CreateVersionRequest.SerializeToString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'DeleteVersion'): DeleteVersionRequest.SerializeToString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'GetVersion'): GetVersionRequest.SerializeToString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'ListVersions'): ListVersionsRequest.SerializeToString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'UpdateVersion'): UpdateVersionRequest.SerializeToString,
    }
    response_deserializers = {
      ('google.cloud.dialogflow.v2beta1.Versions', 'CreateVersion'): Version.FromString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'DeleteVersion'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'GetVersion'): Version.FromString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'ListVersions'): ListVersionsResponse.FromString,
      ('google.cloud.dialogflow.v2beta1.Versions', 'UpdateVersion'): Version.FromString,
    }
    cardinalities = {
      'CreateVersion': cardinality.Cardinality.UNARY_UNARY,
      'DeleteVersion': cardinality.Cardinality.UNARY_UNARY,
      'GetVersion': cardinality.Cardinality.UNARY_UNARY,
      'ListVersions': cardinality.Cardinality.UNARY_UNARY,
      'UpdateVersion': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'google.cloud.dialogflow.v2beta1.Versions', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)