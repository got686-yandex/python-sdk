# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.datasphere.v1 import node_service_pb2 as yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2


class NodeServiceStub(object):
    """A set of methods for managing Node resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Execute = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.NodeService/Execute',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.NodeExecutionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.NodeExecutionResponse.FromString,
                )
        self.ExecuteAlias = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.NodeService/ExecuteAlias',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.AliasExecutionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.AliasExecutionResponse.FromString,
                )


class NodeServiceServicer(object):
    """A set of methods for managing Node resources.
    """

    def Execute(self, request, context):
        """Executes deployed Node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteAlias(self, request, context):
        """Executes NodeAlias requests.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Execute': grpc.unary_unary_rpc_method_handler(
                    servicer.Execute,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.NodeExecutionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.NodeExecutionResponse.SerializeToString,
            ),
            'ExecuteAlias': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteAlias,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.AliasExecutionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.AliasExecutionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.datasphere.v1.NodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NodeService(object):
    """A set of methods for managing Node resources.
    """

    @staticmethod
    def Execute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.NodeService/Execute',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.NodeExecutionRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.NodeExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecuteAlias(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.NodeService/ExecuteAlias',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.AliasExecutionRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_node__service__pb2.AliasExecutionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
