# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.cdn.v1 import rule_pb2 as yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__pb2
from yandex.cloud.cdn.v1 import rule_service_pb2 as yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2
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
        + f' but the generated code in yandex/cloud/cdn/v1/rule_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ResourceRulesServiceStub(object):
    """
    Rules management service.

    Used for Resources Rules management.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/yandex.cloud.cdn.v1.ResourceRulesService/List',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.ListResourceRulesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.ListResourceRulesResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.cdn.v1.ResourceRulesService/Create',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.CreateResourceRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/yandex.cloud.cdn.v1.ResourceRulesService/Get',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.GetResourceRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__pb2.Rule.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.cdn.v1.ResourceRulesService/Update',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.UpdateResourceRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.cdn.v1.ResourceRulesService/Delete',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.DeleteResourceRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class ResourceRulesServiceServicer(object):
    """
    Rules management service.

    Used for Resources Rules management.

    """

    def List(self, request, context):
        """List all rules for specified resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Create new resource rule with specified unique name and rule patter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get specified by id resource rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update specified by id resource rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete specified by id resource rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResourceRulesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.ListResourceRulesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.ListResourceRulesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.CreateResourceRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.GetResourceRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__pb2.Rule.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.UpdateResourceRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.DeleteResourceRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.cdn.v1.ResourceRulesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.cdn.v1.ResourceRulesService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ResourceRulesService(object):
    """
    Rules management service.

    Used for Resources Rules management.

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
            '/yandex.cloud.cdn.v1.ResourceRulesService/List',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.ListResourceRulesRequest.SerializeToString,
            yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.ListResourceRulesResponse.FromString,
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
            '/yandex.cloud.cdn.v1.ResourceRulesService/Create',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.CreateResourceRuleRequest.SerializeToString,
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
            '/yandex.cloud.cdn.v1.ResourceRulesService/Get',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.GetResourceRuleRequest.SerializeToString,
            yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__pb2.Rule.FromString,
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
            '/yandex.cloud.cdn.v1.ResourceRulesService/Update',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.UpdateResourceRuleRequest.SerializeToString,
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
            '/yandex.cloud.cdn.v1.ResourceRulesService/Delete',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_rule__service__pb2.DeleteResourceRuleRequest.SerializeToString,
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
