# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.speechsense.v1 import classifiers_service_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_classifiers__service__pb2


class ClassifiersServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.speechsense.v1.ClassifiersService/List',
                request_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_classifiers__service__pb2.ListClassifiersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_classifiers__service__pb2.ListClassifiersResponse.FromString,
                )


class ClassifiersServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Rpc for listing classifiers in a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClassifiersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_classifiers__service__pb2.ListClassifiersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_speechsense_dot_v1_dot_classifiers__service__pb2.ListClassifiersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.speechsense.v1.ClassifiersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClassifiersService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.speechsense.v1.ClassifiersService/List',
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_classifiers__service__pb2.ListClassifiersRequest.SerializeToString,
            yandex_dot_cloud_dot_speechsense_dot_v1_dot_classifiers__service__pb2.ListClassifiersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)