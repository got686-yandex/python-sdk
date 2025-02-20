# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.backup.v1 import resource_service_pb2 as yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2
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
        + f' but the generated code in yandex/cloud/backup/v1/resource_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ResourceServiceStub(object):
    """A set of methods for managing backup resources: [Compute Cloud instances](/docs/backup/concepts/vm-connection#os).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.backup.v1.ResourceService/List',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourcesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourcesResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/yandex.cloud.backup.v1.ResourceService/Get',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.GetResourceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.GetResourceResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.backup.v1.ResourceService/Delete',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.DeleteResourceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListTasks = channel.unary_unary(
                '/yandex.cloud.backup.v1.ResourceService/ListTasks',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListTasksRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListTasksResponse.FromString,
                _registered_method=True)
        self.ListDirectory = channel.unary_unary(
                '/yandex.cloud.backup.v1.ResourceService/ListDirectory',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListDirectoryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListDirectoryResponse.FromString,
                _registered_method=True)
        self.CreateDirectory = channel.unary_unary(
                '/yandex.cloud.backup.v1.ResourceService/CreateDirectory',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.CreateDirectoryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.backup.v1.ResourceService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourceOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourceOperationsResponse.FromString,
                _registered_method=True)


class ResourceServiceServicer(object):
    """A set of methods for managing backup resources: [Compute Cloud instances](/docs/backup/concepts/vm-connection#os).
    """

    def List(self, request, context):
        """List resources: Compute Cloud instances.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get specific Compute Cloud instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete specific Compute Cloud instance from Cloud Backup. It does not delete
        instance from Cloud Compute service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTasks(self, request, context):
        """List tasks of resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDirectory(self, request, context):
        """ListDirectory returns all subdirectories found in requested directory identified
        by the id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDirectory(self, request, context):
        """CreateDirectory creates new directory by requested path.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """ListOperations return all operations in backup service for given instance
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResourceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourcesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourcesResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.GetResourceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.GetResourceResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.DeleteResourceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTasks,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListTasksRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListTasksResponse.SerializeToString,
            ),
            'ListDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDirectory,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListDirectoryRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListDirectoryResponse.SerializeToString,
            ),
            'CreateDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDirectory,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.CreateDirectoryRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourceOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourceOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.backup.v1.ResourceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.backup.v1.ResourceService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ResourceService(object):
    """A set of methods for managing backup resources: [Compute Cloud instances](/docs/backup/concepts/vm-connection#os).
    """

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
            '/yandex.cloud.backup.v1.ResourceService/List',
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourcesRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourcesResponse.FromString,
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
            '/yandex.cloud.backup.v1.ResourceService/Get',
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.GetResourceRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.GetResourceResponse.FromString,
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
            '/yandex.cloud.backup.v1.ResourceService/Delete',
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.DeleteResourceRequest.SerializeToString,
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
    def ListTasks(request,
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
            '/yandex.cloud.backup.v1.ResourceService/ListTasks',
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListTasksRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListTasksResponse.FromString,
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
    def ListDirectory(request,
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
            '/yandex.cloud.backup.v1.ResourceService/ListDirectory',
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListDirectoryRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListDirectoryResponse.FromString,
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
    def CreateDirectory(request,
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
            '/yandex.cloud.backup.v1.ResourceService/CreateDirectory',
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.CreateDirectoryRequest.SerializeToString,
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
            '/yandex.cloud.backup.v1.ResourceService/ListOperations',
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourceOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_resource__service__pb2.ListResourceOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
