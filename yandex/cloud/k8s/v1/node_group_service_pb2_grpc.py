# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.k8s.v1 import node_group_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__pb2
from yandex.cloud.k8s.v1 import node_group_service_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in yandex/cloud/k8s/v1/node_group_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NodeGroupServiceStub(object):
    """A set of methods for managing node groups.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.k8s.v1.NodeGroupService/Get',
                request_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.GetNodeGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__pb2.NodeGroup.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.k8s.v1.NodeGroupService/List',
                request_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupsResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.k8s.v1.NodeGroupService/Create',
                request_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.CreateNodeGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.k8s.v1.NodeGroupService/Update',
                request_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.UpdateNodeGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.k8s.v1.NodeGroupService/Delete',
                request_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.DeleteNodeGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.k8s.v1.NodeGroupService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupOperationsResponse.FromString,
                _registered_method=True)
        self.ListNodes = channel.unary_unary(
                '/yandex.cloud.k8s.v1.NodeGroupService/ListNodes',
                request_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupNodesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupNodesResponse.FromString,
                _registered_method=True)


class NodeGroupServiceServicer(object):
    """A set of methods for managing node groups.
    """

    def Get(self, request, context):
        """Returns the specified node group.

        To get the list of available node group, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of node group in the specified Kubernetes cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a node group in the specified Kubernetes cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified node group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified node group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified node group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNodes(self, request, context):
        """Retrieves the list of nodes in the specified Kubernetes cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeGroupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.GetNodeGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__pb2.NodeGroup.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.CreateNodeGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.UpdateNodeGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.DeleteNodeGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupOperationsResponse.SerializeToString,
            ),
            'ListNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNodes,
                    request_deserializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupNodesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupNodesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.k8s.v1.NodeGroupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.k8s.v1.NodeGroupService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class NodeGroupService(object):
    """A set of methods for managing node groups.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.k8s.v1.NodeGroupService/Get',
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.GetNodeGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__pb2.NodeGroup.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.k8s.v1.NodeGroupService/List',
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupsRequest.SerializeToString,
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.k8s.v1.NodeGroupService/Create',
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.CreateNodeGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.k8s.v1.NodeGroupService/Update',
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.UpdateNodeGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.k8s.v1.NodeGroupService/Delete',
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.DeleteNodeGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.k8s.v1.NodeGroupService/ListOperations',
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.k8s.v1.NodeGroupService/ListNodes',
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupNodesRequest.SerializeToString,
            yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__service__pb2.ListNodeGroupNodesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
