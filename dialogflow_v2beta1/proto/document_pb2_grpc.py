# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dialogflow_v2beta1.proto import (
    document_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


class DocumentsStub(object):
    """Service for managing knowledge [Documents][google.cloud.dialogflow.v2beta1.Document]."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListDocuments = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.Documents/ListDocuments",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.ListDocumentsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.ListDocumentsResponse.FromString,
        )
        self.GetDocument = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.Documents/GetDocument",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.GetDocumentRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.Document.FromString,
        )
        self.CreateDocument = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.Documents/CreateDocument",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.CreateDocumentRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.DeleteDocument = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.Documents/DeleteDocument",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.DeleteDocumentRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.UpdateDocument = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.Documents/UpdateDocument",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.UpdateDocumentRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.ReloadDocument = channel.unary_unary(
            "/google.cloud.dialogflow.v2beta1.Documents/ReloadDocument",
            request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.ReloadDocumentRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class DocumentsServicer(object):
    """Service for managing knowledge [Documents][google.cloud.dialogflow.v2beta1.Document]."""

    def ListDocuments(self, request, context):
        """Returns the list of all documents of the knowledge base.

        Note: The `projects.agent.knowledgeBases.documents` resource is deprecated;
        only use `projects.knowledgeBases.documents`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetDocument(self, request, context):
        """Retrieves the specified document.

        Note: The `projects.agent.knowledgeBases.documents` resource is deprecated;
        only use `projects.knowledgeBases.documents`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateDocument(self, request, context):
        """Creates a new document.

        Note: The `projects.agent.knowledgeBases.documents` resource is deprecated;
        only use `projects.knowledgeBases.documents`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteDocument(self, request, context):
        """Deletes the specified document.

        Note: The `projects.agent.knowledgeBases.documents` resource is deprecated;
        only use `projects.knowledgeBases.documents`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateDocument(self, request, context):
        """Updates the specified document.

        Note: The `projects.agent.knowledgeBases.documents` resource is deprecated;
        only use `projects.knowledgeBases.documents`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ReloadDocument(self, request, context):
        """Reloads the specified document from its specified source, content_uri or
        content. The previously loaded content of the document will be deleted.
        Note: Even when the content of the document has not changed, there still
        may be side effects because of internal implementation changes.

        Note: The `projects.agent.knowledgeBases.documents` resource is deprecated;
        only use `projects.knowledgeBases.documents`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DocumentsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListDocuments": grpc.unary_unary_rpc_method_handler(
            servicer.ListDocuments,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.ListDocumentsRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.ListDocumentsResponse.SerializeToString,
        ),
        "GetDocument": grpc.unary_unary_rpc_method_handler(
            servicer.GetDocument,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.GetDocumentRequest.FromString,
            response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.Document.SerializeToString,
        ),
        "CreateDocument": grpc.unary_unary_rpc_method_handler(
            servicer.CreateDocument,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.CreateDocumentRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "DeleteDocument": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteDocument,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.DeleteDocumentRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "UpdateDocument": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateDocument,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.UpdateDocumentRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "ReloadDocument": grpc.unary_unary_rpc_method_handler(
            servicer.ReloadDocument,
            request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.ReloadDocumentRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.dialogflow.v2beta1.Documents", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Documents(object):
    """Service for managing knowledge [Documents][google.cloud.dialogflow.v2beta1.Document]."""

    @staticmethod
    def ListDocuments(
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
            "/google.cloud.dialogflow.v2beta1.Documents/ListDocuments",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.ListDocumentsRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.ListDocumentsResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetDocument(
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
            "/google.cloud.dialogflow.v2beta1.Documents/GetDocument",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.GetDocumentRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.Document.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateDocument(
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
            "/google.cloud.dialogflow.v2beta1.Documents/CreateDocument",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.CreateDocumentRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteDocument(
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
            "/google.cloud.dialogflow.v2beta1.Documents/DeleteDocument",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.DeleteDocumentRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateDocument(
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
            "/google.cloud.dialogflow.v2beta1.Documents/UpdateDocument",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.UpdateDocumentRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ReloadDocument(
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
            "/google.cloud.dialogflow.v2beta1.Documents/ReloadDocument",
            google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_document__pb2.ReloadDocumentRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
