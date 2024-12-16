# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.mdb.postgresql.v1 import perf_diag_service_pb2 as yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2

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
        + f' but the generated code in yandex/cloud/mdb/postgresql/v1/perf_diag_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PerformanceDiagnosticsServiceStub(object):
    """A set of methods for PostgreSQL performance diagnostics.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListRawSessionStates = channel.unary_unary(
                '/yandex.cloud.mdb.postgresql.v1.PerformanceDiagnosticsService/ListRawSessionStates',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawSessionStatesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawSessionStatesResponse.FromString,
                _registered_method=True)
        self.ListRawStatements = channel.unary_unary(
                '/yandex.cloud.mdb.postgresql.v1.PerformanceDiagnosticsService/ListRawStatements',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawStatementsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawStatementsResponse.FromString,
                _registered_method=True)


class PerformanceDiagnosticsServiceServicer(object):
    """A set of methods for PostgreSQL performance diagnostics.
    """

    def ListRawSessionStates(self, request, context):
        """Retrieves raw statistics on sessions. Corresponds to the [pg_stat_activity view](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRawStatements(self, request, context):
        """Retrieves statistics on planning and execution of SQL statements (queries).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PerformanceDiagnosticsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListRawSessionStates': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRawSessionStates,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawSessionStatesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawSessionStatesResponse.SerializeToString,
            ),
            'ListRawStatements': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRawStatements,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawStatementsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawStatementsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.postgresql.v1.PerformanceDiagnosticsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.mdb.postgresql.v1.PerformanceDiagnosticsService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PerformanceDiagnosticsService(object):
    """A set of methods for PostgreSQL performance diagnostics.
    """

    @staticmethod
    def ListRawSessionStates(request,
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
            '/yandex.cloud.mdb.postgresql.v1.PerformanceDiagnosticsService/ListRawSessionStates',
            yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawSessionStatesRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawSessionStatesResponse.FromString,
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
    def ListRawStatements(request,
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
            '/yandex.cloud.mdb.postgresql.v1.PerformanceDiagnosticsService/ListRawStatements',
            yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawStatementsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_postgresql_dot_v1_dot_perf__diag__service__pb2.ListRawStatementsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
