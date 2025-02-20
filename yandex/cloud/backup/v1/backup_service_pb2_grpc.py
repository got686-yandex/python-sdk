# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.backup.v1 import backup_pb2 as yandex_dot_cloud_dot_backup_dot_v1_dot_backup__pb2
from yandex.cloud.backup.v1 import backup_service_pb2 as yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2
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
        + f' but the generated code in yandex/cloud/backup/v1/backup_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class BackupServiceStub(object):
    """A set of methods for managing [backups](/docs/backup/concepts/backup).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.backup.v1.BackupService/List',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListBackupsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListBackupsResponse.FromString,
                _registered_method=True)
        self.ListArchives = channel.unary_unary(
                '/yandex.cloud.backup.v1.BackupService/ListArchives',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListArchivesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListArchivesResponse.FromString,
                _registered_method=True)
        self.ListFiles = channel.unary_unary(
                '/yandex.cloud.backup.v1.BackupService/ListFiles',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListFilesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListFilesResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/yandex.cloud.backup.v1.BackupService/Get',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.GetBackupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__pb2.Backup.FromString,
                _registered_method=True)
        self.StartRecovery = channel.unary_unary(
                '/yandex.cloud.backup.v1.BackupService/StartRecovery',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.StartRecoveryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.StartFilesRecovery = channel.unary_unary(
                '/yandex.cloud.backup.v1.BackupService/StartFilesRecovery',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.StartFilesRecoveryRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.backup.v1.BackupService/Delete',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.DeleteBackupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.DeleteArchive = channel.unary_unary(
                '/yandex.cloud.backup.v1.BackupService/DeleteArchive',
                request_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.DeleteArchiveRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class BackupServiceServicer(object):
    """A set of methods for managing [backups](/docs/backup/concepts/backup).
    """

    def List(self, request, context):
        """List backups using filters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListArchives(self, request, context):
        """List archives that holds backups for specified folder or
        specified [Compute Cloud instance](/docs/backup/concepts/vm-connection#os).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFiles(self, request, context):
        """ListFiles of the backup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get backup by its id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartRecovery(self, request, context):
        """Start recovery process of specified backup to specific Compute Cloud instance.

        For details, see [Restoring a VM from a backup](/docs/backup/operations/backup-vm/recover).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartFilesRecovery(self, request, context):
        """StartFilesRecovery runs recovery process of selected files to specific Compute Cloud instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete specific backup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteArchive(self, request, context):
        """Delete specific archive.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BackupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListBackupsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListBackupsResponse.SerializeToString,
            ),
            'ListArchives': grpc.unary_unary_rpc_method_handler(
                    servicer.ListArchives,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListArchivesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListArchivesResponse.SerializeToString,
            ),
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListFilesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListFilesResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.GetBackupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__pb2.Backup.SerializeToString,
            ),
            'StartRecovery': grpc.unary_unary_rpc_method_handler(
                    servicer.StartRecovery,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.StartRecoveryRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'StartFilesRecovery': grpc.unary_unary_rpc_method_handler(
                    servicer.StartFilesRecovery,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.StartFilesRecoveryRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.DeleteBackupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteArchive': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteArchive,
                    request_deserializer=yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.DeleteArchiveRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.backup.v1.BackupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.backup.v1.BackupService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BackupService(object):
    """A set of methods for managing [backups](/docs/backup/concepts/backup).
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
            '/yandex.cloud.backup.v1.BackupService/List',
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListBackupsRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListBackupsResponse.FromString,
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
    def ListArchives(request,
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
            '/yandex.cloud.backup.v1.BackupService/ListArchives',
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListArchivesRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListArchivesResponse.FromString,
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
    def ListFiles(request,
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
            '/yandex.cloud.backup.v1.BackupService/ListFiles',
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListFilesRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.ListFilesResponse.FromString,
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
            '/yandex.cloud.backup.v1.BackupService/Get',
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.GetBackupRequest.SerializeToString,
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__pb2.Backup.FromString,
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
    def StartRecovery(request,
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
            '/yandex.cloud.backup.v1.BackupService/StartRecovery',
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.StartRecoveryRequest.SerializeToString,
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
    def StartFilesRecovery(request,
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
            '/yandex.cloud.backup.v1.BackupService/StartFilesRecovery',
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.StartFilesRecoveryRequest.SerializeToString,
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
            '/yandex.cloud.backup.v1.BackupService/Delete',
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.DeleteBackupRequest.SerializeToString,
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
    def DeleteArchive(request,
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
            '/yandex.cloud.backup.v1.BackupService/DeleteArchive',
            yandex_dot_cloud_dot_backup_dot_v1_dot_backup__service__pb2.DeleteArchiveRequest.SerializeToString,
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
