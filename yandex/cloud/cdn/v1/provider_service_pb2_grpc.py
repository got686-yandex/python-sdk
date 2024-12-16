# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.cdn.v1 import provider_service_pb2 as yandex_dot_cloud_dot_cdn_dot_v1_dot_provider__service__pb2
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
        + f' but the generated code in yandex/cloud/cdn/v1/provider_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ProviderServiceStub(object):
    """A set of methods for managing Provider Service resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Activate = channel.unary_unary(
                '/yandex.cloud.cdn.v1.ProviderService/Activate',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_provider__service__pb2.ActivateProviderRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListActivated = channel.unary_unary(
                '/yandex.cloud.cdn.v1.ProviderService/ListActivated',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_provider__service__pb2.ListActivatedProvidersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_provider__service__pb2.ListActivatedProvidersResponse.FromString,
                _registered_method=True)


class ProviderServiceServicer(object):
    """A set of methods for managing Provider Service resources.
    """

    def Activate(self, request, context):
        """Activate provider for specified client.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListActivated(self, request, context):
        """List activated providers for specified client.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProviderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Activate': grpc.unary_unary_rpc_method_handler(
                    servicer.Activate,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_provider__service__pb2.ActivateProviderRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListActivated': grpc.unary_unary_rpc_method_handler(
                    servicer.ListActivated,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_provider__service__pb2.ListActivatedProvidersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_provider__service__pb2.ListActivatedProvidersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.cdn.v1.ProviderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.cdn.v1.ProviderService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ProviderService(object):
    """A set of methods for managing Provider Service resources.
    """

    @staticmethod
    def Activate(request,
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
            '/yandex.cloud.cdn.v1.ProviderService/Activate',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_provider__service__pb2.ActivateProviderRequest.SerializeToString,
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
    def ListActivated(request,
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
            '/yandex.cloud.cdn.v1.ProviderService/ListActivated',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_provider__service__pb2.ListActivatedProvidersRequest.SerializeToString,
            yandex_dot_cloud_dot_cdn_dot_v1_dot_provider__service__pb2.ListActivatedProvidersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
