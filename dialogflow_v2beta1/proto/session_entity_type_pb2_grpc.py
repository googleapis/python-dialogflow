# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dialogflow_v2beta1.proto import (
    session_entity_type_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class SessionEntityTypesStub(object):
    """Entities are extracted from user input and represent parameters that are
    meaningful to your application. For example, a date range, a proper name
    such as a geographic location or landmark, and so on. Entities represent
    actionable data for your application.

    Session entity types are referred to as **User** entity types and are
    entities that are built for an individual user such as
    favorites, preferences, playlists, and so on. You can redefine a session
    entity type at the session level.

    Session entity methods do not work with Google Assistant integration.
    Contact Dialogflow support if you need to use session entities
    with Google Assistant integration.

    For more information about entity types, see the
    [Dialogflow
    documentation](https://cloud.google.com/dialogflow/docs/entities-overview).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListSessionEntityTypes = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.SessionEntityTypes/ListSessionEntityTypes",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.ListSessionEntityTypesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.ListSessionEntityTypesResponse.FromString,
        )
        self.GetSessionEntityType = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.SessionEntityTypes/GetSessionEntityType",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.GetSessionEntityTypeRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.SessionEntityType.FromString,
        )
        self.CreateSessionEntityType = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.SessionEntityTypes/CreateSessionEntityType",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.CreateSessionEntityTypeRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.SessionEntityType.FromString,
        )
        self.UpdateSessionEntityType = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.SessionEntityTypes/UpdateSessionEntityType",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.UpdateSessionEntityTypeRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.SessionEntityType.FromString,
        )
        self.DeleteSessionEntityType = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.SessionEntityTypes/DeleteSessionEntityType",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.DeleteSessionEntityTypeRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class SessionEntityTypesServicer(object):
    """Entities are extracted from user input and represent parameters that are
    meaningful to your application. For example, a date range, a proper name
    such as a geographic location or landmark, and so on. Entities represent
    actionable data for your application.

    Session entity types are referred to as **User** entity types and are
    entities that are built for an individual user such as
    favorites, preferences, playlists, and so on. You can redefine a session
    entity type at the session level.

    Session entity methods do not work with Google Assistant integration.
    Contact Dialogflow support if you need to use session entities
    with Google Assistant integration.

    For more information about entity types, see the
    [Dialogflow
    documentation](https://cloud.google.com/dialogflow/docs/entities-overview).
    """

    def ListSessionEntityTypes(self, request, context):
        """Returns the list of all session entity types in the specified session.

        This method doesn't work with Google Assistant integration.
        Contact Dialogflow support if you need to use session entities
        with Google Assistant integration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetSessionEntityType(self, request, context):
        """Retrieves the specified session entity type.

        This method doesn't work with Google Assistant integration.
        Contact Dialogflow support if you need to use session entities
        with Google Assistant integration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateSessionEntityType(self, request, context):
        """Creates a session entity type.

        If the specified session entity type already exists, overrides the
        session entity type.

        This method doesn't work with Google Assistant integration.
        Contact Dialogflow support if you need to use session entities
        with Google Assistant integration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateSessionEntityType(self, request, context):
        """Updates the specified session entity type.

        This method doesn't work with Google Assistant integration.
        Contact Dialogflow support if you need to use session entities
        with Google Assistant integration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteSessionEntityType(self, request, context):
        """Deletes the specified session entity type.

        This method doesn't work with Google Assistant integration.
        Contact Dialogflow support if you need to use session entities
        with Google Assistant integration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SessionEntityTypesServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListSessionEntityTypes": grpc.unary_unary_rpc_method_handler(
            servicer.ListSessionEntityTypes,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.ListSessionEntityTypesRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.ListSessionEntityTypesResponse.SerializeToString,
        ),
        "GetSessionEntityType": grpc.unary_unary_rpc_method_handler(
            servicer.GetSessionEntityType,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.GetSessionEntityTypeRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.SessionEntityType.SerializeToString,
        ),
        "CreateSessionEntityType": grpc.unary_unary_rpc_method_handler(
            servicer.CreateSessionEntityType,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.CreateSessionEntityTypeRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.SessionEntityType.SerializeToString,
        ),
        "UpdateSessionEntityType": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateSessionEntityType,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.UpdateSessionEntityTypeRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.SessionEntityType.SerializeToString,
        ),
        "DeleteSessionEntityType": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteSessionEntityType,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.DeleteSessionEntityTypeRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.dialogflow.v2beta1.SessionEntityTypes", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SessionEntityTypes(object):
    """Entities are extracted from user input and represent parameters that are
    meaningful to your application. For example, a date range, a proper name
    such as a geographic location or landmark, and so on. Entities represent
    actionable data for your application.

    Session entity types are referred to as **User** entity types and are
    entities that are built for an individual user such as
    favorites, preferences, playlists, and so on. You can redefine a session
    entity type at the session level.

    Session entity methods do not work with Google Assistant integration.
    Contact Dialogflow support if you need to use session entities
    with Google Assistant integration.

    For more information about entity types, see the
    [Dialogflow
    documentation](https://cloud.google.com/dialogflow/docs/entities-overview).
    """

    @staticmethod
    def ListSessionEntityTypes(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.v2beta1.SessionEntityTypes/ListSessionEntityTypes",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.ListSessionEntityTypesRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.ListSessionEntityTypesResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetSessionEntityType(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.v2beta1.SessionEntityTypes/GetSessionEntityType",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.GetSessionEntityTypeRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.SessionEntityType.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateSessionEntityType(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.v2beta1.SessionEntityTypes/CreateSessionEntityType",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.CreateSessionEntityTypeRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.SessionEntityType.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateSessionEntityType(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.v2beta1.SessionEntityTypes/UpdateSessionEntityType",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.UpdateSessionEntityTypeRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.SessionEntityType.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteSessionEntityType(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.dialogflow.v2beta1.SessionEntityTypes/DeleteSessionEntityType",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__entity__type__pb2.DeleteSessionEntityTypeRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
