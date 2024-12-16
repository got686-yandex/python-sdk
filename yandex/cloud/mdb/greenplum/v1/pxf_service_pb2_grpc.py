# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.mdb.greenplum.v1 import pxf_service_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

GRPC_GENERATED_VERSION = '1.68.1'
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
        + f' but the generated code in yandex/cloud/mdb/greenplum/v1/pxf_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PXFDatasourceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.PXFDatasourceService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.ListPXFDatasourcesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.ListPXFDatasourcesResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.PXFDatasourceService/Create',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.CreatePXFDatasourceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.PXFDatasourceService/Update',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.UpdatePXFDatasourceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.PXFDatasourceService/Delete',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.DeletePXFDatasourceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class PXFDatasourceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """List all PXF datasources
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates PXF datasource
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update PXF datasource
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete PXF datasource
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PXFDatasourceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.ListPXFDatasourcesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.ListPXFDatasourcesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.CreatePXFDatasourceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.UpdatePXFDatasourceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.DeletePXFDatasourceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.greenplum.v1.PXFDatasourceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.mdb.greenplum.v1.PXFDatasourceService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PXFDatasourceService(object):
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.mdb.greenplum.v1.PXFDatasourceService/List',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.ListPXFDatasourcesRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.ListPXFDatasourcesResponse.FromString,
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
            '/yandex.cloud.mdb.greenplum.v1.PXFDatasourceService/Create',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.CreatePXFDatasourceRequest.SerializeToString,
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
            '/yandex.cloud.mdb.greenplum.v1.PXFDatasourceService/Update',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.UpdatePXFDatasourceRequest.SerializeToString,
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
            '/yandex.cloud.mdb.greenplum.v1.PXFDatasourceService/Delete',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__service__pb2.DeletePXFDatasourceRequest.SerializeToString,
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
