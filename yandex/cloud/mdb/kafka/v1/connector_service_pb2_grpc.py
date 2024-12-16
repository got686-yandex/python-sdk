# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.mdb.kafka.v1 import connector_pb2 as yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__pb2
from yandex.cloud.mdb.kafka.v1 import connector_service_pb2 as yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2
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
        + f' but the generated code in yandex/cloud/mdb/kafka/v1/connector_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ConnectorServiceStub(object):
    """A set of methods for managing Apache Kafka® connectors.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.ConnectorService/Get',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.GetConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__pb2.Connector.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.ConnectorService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.ConnectorService/Create',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.CreateConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.ConnectorService/Update',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.UpdateConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.ConnectorService/Delete',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.DeleteConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Resume = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.ConnectorService/Resume',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.ResumeConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Pause = channel.unary_unary(
                '/yandex.cloud.mdb.kafka.v1.ConnectorService/Pause',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.PauseConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class ConnectorServiceServicer(object):
    """A set of methods for managing Apache Kafka® connectors.
    """

    def Get(self, request, context):
        """Returns information about an Apache Kafka® connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Apache Kafka® connectors in a cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a new Apache Kafka® connector in a cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates an Apache Kafka® connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes an Apache Kafka® connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Resume(self, request, context):
        """Resumes an Apache Kafka® connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pause(self, request, context):
        """Pauses an Apache Kafka® connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConnectorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.GetConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__pb2.Connector.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.CreateConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.UpdateConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.DeleteConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Resume': grpc.unary_unary_rpc_method_handler(
                    servicer.Resume,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.ResumeConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Pause': grpc.unary_unary_rpc_method_handler(
                    servicer.Pause,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.PauseConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.kafka.v1.ConnectorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.mdb.kafka.v1.ConnectorService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ConnectorService(object):
    """A set of methods for managing Apache Kafka® connectors.
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
            '/yandex.cloud.mdb.kafka.v1.ConnectorService/Get',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.GetConnectorRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__pb2.Connector.FromString,
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
            '/yandex.cloud.mdb.kafka.v1.ConnectorService/List',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsResponse.FromString,
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
            '/yandex.cloud.mdb.kafka.v1.ConnectorService/Create',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.CreateConnectorRequest.SerializeToString,
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
            '/yandex.cloud.mdb.kafka.v1.ConnectorService/Update',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.UpdateConnectorRequest.SerializeToString,
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
            '/yandex.cloud.mdb.kafka.v1.ConnectorService/Delete',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.DeleteConnectorRequest.SerializeToString,
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
    def Resume(request,
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
            '/yandex.cloud.mdb.kafka.v1.ConnectorService/Resume',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.ResumeConnectorRequest.SerializeToString,
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
    def Pause(request,
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
            '/yandex.cloud.mdb.kafka.v1.ConnectorService/Pause',
            yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_connector__service__pb2.PauseConnectorRequest.SerializeToString,
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
