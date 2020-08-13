# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow_v2beta1/proto/validation_result.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/dialogflow_v2beta1/proto/validation_result.proto",
    package="google.cloud.dialogflow.v2beta1",
    syntax="proto3",
    serialized_options=b"\n#com.google.cloud.dialogflow.v2beta1B\025ValidationResultProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001\242\002\002DF\252\002\037Google.Cloud.Dialogflow.V2beta1",
    serialized_pb=b'\n=google/cloud/dialogflow_v2beta1/proto/validation_result.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto"\xdc\x01\n\x0fValidationError\x12K\n\x08severity\x18\x01 \x01(\x0e\x32\x39.google.cloud.dialogflow.v2beta1.ValidationError.Severity\x12\x0f\n\x07\x65ntries\x18\x03 \x03(\t\x12\x15\n\rerror_message\x18\x04 \x01(\t"T\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08\x43RITICAL\x10\x04"_\n\x10ValidationResult\x12K\n\x11validation_errors\x18\x01 \x03(\x0b\x32\x30.google.cloud.dialogflow.v2beta1.ValidationErrorB\xb3\x01\n#com.google.cloud.dialogflow.v2beta1B\x15ValidationResultProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2beta1b\x06proto3',
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)


_VALIDATIONERROR_SEVERITY = _descriptor.EnumDescriptor(
    name="Severity",
    full_name="google.cloud.dialogflow.v2beta1.ValidationError.Severity",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SEVERITY_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="INFO", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="WARNING", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CRITICAL", index=4, number=4, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=265,
    serialized_end=349,
)
_sym_db.RegisterEnumDescriptor(_VALIDATIONERROR_SEVERITY)


_VALIDATIONERROR = _descriptor.Descriptor(
    name="ValidationError",
    full_name="google.cloud.dialogflow.v2beta1.ValidationError",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="severity",
            full_name="google.cloud.dialogflow.v2beta1.ValidationError.severity",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="entries",
            full_name="google.cloud.dialogflow.v2beta1.ValidationError.entries",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="error_message",
            full_name="google.cloud.dialogflow.v2beta1.ValidationError.error_message",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_VALIDATIONERROR_SEVERITY],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=129,
    serialized_end=349,
)


_VALIDATIONRESULT = _descriptor.Descriptor(
    name="ValidationResult",
    full_name="google.cloud.dialogflow.v2beta1.ValidationResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="validation_errors",
            full_name="google.cloud.dialogflow.v2beta1.ValidationResult.validation_errors",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=351,
    serialized_end=446,
)

_VALIDATIONERROR.fields_by_name["severity"].enum_type = _VALIDATIONERROR_SEVERITY
_VALIDATIONERROR_SEVERITY.containing_type = _VALIDATIONERROR
_VALIDATIONRESULT.fields_by_name["validation_errors"].message_type = _VALIDATIONERROR
DESCRIPTOR.message_types_by_name["ValidationError"] = _VALIDATIONERROR
DESCRIPTOR.message_types_by_name["ValidationResult"] = _VALIDATIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValidationError = _reflection.GeneratedProtocolMessageType(
    "ValidationError",
    (_message.Message,),
    {
        "DESCRIPTOR": _VALIDATIONERROR,
        "__module__": "google.cloud.dialogflow_v2beta1.proto.validation_result_pb2",
        "__doc__": """Represents a single validation error.
  Attributes:
      severity:
          The severity of the error.
      entries:
          The names of the entries that the error is associated with.
          Format:  -  “projects//agent”, if the error is associated with
          the entire agent. -  “projects//agent/intents/”, if the error
          is associated with certain    intents. -
          “projects//agent/intents//trainingPhrases/”, if the error is
          associated with certain intent training phrases. -
          “projects//agent/intents//parameters/”, if the error is
          associated    with certain intent parameters. -
          “projects//agent/entities/”, if the error is associated with
          certain    entities.
      error_message:
          The detailed error messsage.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ValidationError)
    },
)
_sym_db.RegisterMessage(ValidationError)

ValidationResult = _reflection.GeneratedProtocolMessageType(
    "ValidationResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _VALIDATIONRESULT,
        "__module__": "google.cloud.dialogflow_v2beta1.proto.validation_result_pb2",
        "__doc__": """Represents the output of agent validation.
  Attributes:
      validation_errors:
          Contains all validation errors.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ValidationResult)
    },
)
_sym_db.RegisterMessage(ValidationResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
