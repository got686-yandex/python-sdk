# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.ydb.v1 import storage_type_pb2 as yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__pb2
from yandex.cloud.ydb.v1 import storage_type_service_pb2 as yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__service__pb2

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
        + f' but the generated code in yandex/cloud/ydb/v1/storage_type_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class StorageTypeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.ydb.v1.StorageTypeService/Get',
                request_serializer=yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__service__pb2.GetStorageTypeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__pb2.StorageType.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.ydb.v1.StorageTypeService/List',
                request_serializer=yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__service__pb2.ListStorageTypesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__service__pb2.ListStorageTypesResponse.FromString,
                _registered_method=True)


class StorageTypeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Returns the specified storage types.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Returns the list of available storage types.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StorageTypeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__service__pb2.GetStorageTypeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__pb2.StorageType.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__service__pb2.ListStorageTypesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__service__pb2.ListStorageTypesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ydb.v1.StorageTypeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.ydb.v1.StorageTypeService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class StorageTypeService(object):
    """Missing associated documentation comment in .proto file."""

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
            '/yandex.cloud.ydb.v1.StorageTypeService/Get',
            yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__service__pb2.GetStorageTypeRequest.SerializeToString,
            yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__pb2.StorageType.FromString,
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
            '/yandex.cloud.ydb.v1.StorageTypeService/List',
            yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__service__pb2.ListStorageTypesRequest.SerializeToString,
            yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__service__pb2.ListStorageTypesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
