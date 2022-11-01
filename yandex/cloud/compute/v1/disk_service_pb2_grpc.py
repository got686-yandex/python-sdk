# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.compute.v1 import disk_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_disk__pb2
from yandex.cloud.compute.v1 import disk_service_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class DiskServiceStub(object):
    """A set of methods for managing Disk resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.compute.v1.DiskService/Get',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.GetDiskRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__pb2.Disk.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.compute.v1.DiskService/List',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDisksRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDisksResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.compute.v1.DiskService/Create',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.CreateDiskRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.compute.v1.DiskService/Update',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.UpdateDiskRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.compute.v1.DiskService/Delete',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.DeleteDiskRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.compute.v1.DiskService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskOperationsResponse.FromString,
                )
        self.Move = channel.unary_unary(
                '/yandex.cloud.compute.v1.DiskService/Move',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.MoveDiskRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListSnapshotSchedules = channel.unary_unary(
                '/yandex.cloud.compute.v1.DiskService/ListSnapshotSchedules',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskSnapshotSchedulesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskSnapshotSchedulesResponse.FromString,
                )


class DiskServiceServicer(object):
    """A set of methods for managing Disk resources.
    """

    def Get(self, request, context):
        """Returns the specified Disk resource.

        To get the list of available Disk resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Disk resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a disk in the specified folder.

        You can create an empty disk or restore it from a snapshot or an image.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified disk.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified disk.

        Deleting a disk removes its data permanently and is irreversible. However, deleting a disk does not delete
        any snapshots or images previously made from the disk. You must delete snapshots and images separately.

        It is not possible to delete a disk that is attached to an instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified disk.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Move(self, request, context):
        """Moves the specified disk to another folder of the same cloud.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSnapshotSchedules(self, request, context):
        """Retrieves the list of snapshot schedules the specified disk is attached to.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.GetDiskRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__pb2.Disk.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDisksRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDisksResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.CreateDiskRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.UpdateDiskRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.DeleteDiskRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskOperationsResponse.SerializeToString,
            ),
            'Move': grpc.unary_unary_rpc_method_handler(
                    servicer.Move,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.MoveDiskRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListSnapshotSchedules': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSnapshotSchedules,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskSnapshotSchedulesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskSnapshotSchedulesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.compute.v1.DiskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DiskService(object):
    """A set of methods for managing Disk resources.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.DiskService/Get',
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.GetDiskRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__pb2.Disk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.DiskService/List',
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDisksRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDisksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.DiskService/Create',
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.CreateDiskRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.DiskService/Update',
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.UpdateDiskRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.DiskService/Delete',
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.DeleteDiskRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.DiskService/ListOperations',
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Move(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.DiskService/Move',
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.MoveDiskRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSnapshotSchedules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.DiskService/ListSnapshotSchedules',
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskSnapshotSchedulesRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_disk__service__pb2.ListDiskSnapshotSchedulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
