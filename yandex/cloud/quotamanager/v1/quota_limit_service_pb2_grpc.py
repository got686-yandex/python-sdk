# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.quotamanager.v1 import quota_limit_service_pb2 as yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2

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
        + f' but the generated code in yandex/cloud/quotamanager/v1/quota_limit_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class QuotaLimitServiceStub(object):
    """A set of methods for managing quota limits.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.quotamanager.v1.QuotaLimitService/Get',
                request_serializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.GetQuotaLimitRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.QuotaLimit.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.quotamanager.v1.QuotaLimitService/List',
                request_serializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListQuotaLimitsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListQuotaLimitsResponse.FromString,
                _registered_method=True)
        self.ListServices = channel.unary_unary(
                '/yandex.cloud.quotamanager.v1.QuotaLimitService/ListServices',
                request_serializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListServicesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListServicesResponse.FromString,
                _registered_method=True)


class QuotaLimitServiceServicer(object):
    """A set of methods for managing quota limits.
    """

    def Get(self, request, context):
        """Returns the specified quota limit.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of quota limits for a given service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListServices(self, request, context):
        """Retrieves the list of services available for quota management.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QuotaLimitServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.GetQuotaLimitRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.QuotaLimit.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListQuotaLimitsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListQuotaLimitsResponse.SerializeToString,
            ),
            'ListServices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListServices,
                    request_deserializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListServicesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListServicesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.quotamanager.v1.QuotaLimitService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.quotamanager.v1.QuotaLimitService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class QuotaLimitService(object):
    """A set of methods for managing quota limits.
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
            '/yandex.cloud.quotamanager.v1.QuotaLimitService/Get',
            yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.GetQuotaLimitRequest.SerializeToString,
            yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.QuotaLimit.FromString,
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
            '/yandex.cloud.quotamanager.v1.QuotaLimitService/List',
            yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListQuotaLimitsRequest.SerializeToString,
            yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListQuotaLimitsResponse.FromString,
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
    def ListServices(request,
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
            '/yandex.cloud.quotamanager.v1.QuotaLimitService/ListServices',
            yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListServicesRequest.SerializeToString,
            yandex_dot_cloud_dot_quotamanager_dot_v1_dot_quota__limit__service__pb2.ListServicesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
