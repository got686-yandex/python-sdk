# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.mdb.postgresql.v1 import backup_retention_policy_service_pb2 as yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2

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
        + f' but the generated code in yandex/cloud/mdb/postgresql/v1/backup_retention_policy_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class BackupRetentionPolicyServiceStub(object):
    """A set of methods for managing PostgreSQL Cluster backup retention policies.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.postgresql.v1.BackupRetentionPolicyService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.ListBackupRetentionPoliciesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.ListBackupRetentionPoliciesResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.mdb.postgresql.v1.BackupRetentionPolicyService/Create',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.CreateBackupRetentionPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.CreateBackupRetentionPolicyResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.mdb.postgresql.v1.BackupRetentionPolicyService/Delete',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.DeleteBackupRetentionPolicyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.DeleteBackupRetentionPolicyResponse.FromString,
                _registered_method=True)


class BackupRetentionPolicyServiceServicer(object):
    """A set of methods for managing PostgreSQL Cluster backup retention policies.
    """

    def List(self, request, context):
        """List all retention policies.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Add a new retention policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete retention policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BackupRetentionPolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.ListBackupRetentionPoliciesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.ListBackupRetentionPoliciesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.CreateBackupRetentionPolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.CreateBackupRetentionPolicyResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.DeleteBackupRetentionPolicyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.DeleteBackupRetentionPolicyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.postgresql.v1.BackupRetentionPolicyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.mdb.postgresql.v1.BackupRetentionPolicyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BackupRetentionPolicyService(object):
    """A set of methods for managing PostgreSQL Cluster backup retention policies.
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
            '/yandex.cloud.mdb.postgresql.v1.BackupRetentionPolicyService/List',
            yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.ListBackupRetentionPoliciesRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.ListBackupRetentionPoliciesResponse.FromString,
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
            '/yandex.cloud.mdb.postgresql.v1.BackupRetentionPolicyService/Create',
            yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.CreateBackupRetentionPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.CreateBackupRetentionPolicyResponse.FromString,
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
            '/yandex.cloud.mdb.postgresql.v1.BackupRetentionPolicyService/Delete',
            yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.DeleteBackupRetentionPolicyRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_backup__retention__policy__service__pb2.DeleteBackupRetentionPolicyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
