# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.serverless.eventrouter.v1 import connector_pb2 as yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__pb2
from yandex.cloud.serverless.eventrouter.v1 import connector_service_pb2 as yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2


class ConnectorServiceStub(object):
    """A set of methods for managing connectors for serverless eventrouter.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Get',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.GetConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__pb2.Connector.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/List',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Create',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.CreateConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Update',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.UpdateConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Delete',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.DeleteConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Start = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Start',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.StartConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Stop = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Stop',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.StopConnectorRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                )
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorOperationsResponse.FromString,
                )


class ConnectorServiceServicer(object):
    """A set of methods for managing connectors for serverless eventrouter.
    """

    def Get(self, request, context):
        """Returns the specified bus.
        To get the list of all available connectors, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of connectors in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a connector in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Start(self, request, context):
        """Starts the specified connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Stops the specified connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """Lists existing access bindings for the specified bus.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Sets access bindings for the connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Updates access bindings for the specified connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConnectorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.GetConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__pb2.Connector.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.CreateConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.UpdateConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.DeleteConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.StartConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.StopConnectorRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.SerializeToString,
            ),
            'SetAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.serverless.eventrouter.v1.ConnectorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ConnectorService(object):
    """A set of methods for managing connectors for serverless eventrouter.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Get',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.GetConnectorRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__pb2.Connector.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/List',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorsRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Create',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.CreateConnectorRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Update',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.UpdateConnectorRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Delete',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.DeleteConnectorRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Start',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.StartConnectorRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/Stop',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.StopConnectorRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/ListAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/SetAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/UpdateAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.serverless.eventrouter.v1.ConnectorService/ListOperations',
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_connector__service__pb2.ListConnectorOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)