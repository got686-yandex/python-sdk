# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.vpc.v1 import security_group_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__pb2
from yandex.cloud.vpc.v1 import security_group_service_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2

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
        + f' but the generated code in yandex/cloud/vpc/v1/security_group_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SecurityGroupServiceStub(object):
    """A set of methods for managing SecurityGroup resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SecurityGroupService/Get',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.GetSecurityGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__pb2.SecurityGroup.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SecurityGroupService/List',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupsResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SecurityGroupService/Create',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.CreateSecurityGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SecurityGroupService/Update',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.UpdateRules = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SecurityGroupService/UpdateRules',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRulesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.UpdateRule = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SecurityGroupService/UpdateRule',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRuleRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SecurityGroupService/Delete',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.DeleteSecurityGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Move = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SecurityGroupService/Move',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.MoveSecurityGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.vpc.v1.SecurityGroupService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupOperationsResponse.FromString,
                _registered_method=True)


class SecurityGroupServiceServicer(object):
    """A set of methods for managing SecurityGroup resources.
    """

    def Get(self, request, context):
        """Returns the specified SecurityGroup resource.

        To get the list of all available SecurityGroup resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of SecurityGroup resources in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a security group in the specified folder and network.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified security group.
        Method starts an asynchronous operation that can be cancelled while it is in progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRules(self, request, context):
        """Updates the rules of the specified security group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRule(self, request, context):
        """Updates the specified rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified security group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Move(self, request, context):
        """Moves security groups to another folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified security groups.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SecurityGroupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.GetSecurityGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__pb2.SecurityGroup.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.CreateSecurityGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateRules': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRules,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRulesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateRule': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRule,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRuleRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.DeleteSecurityGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Move': grpc.unary_unary_rpc_method_handler(
                    servicer.Move,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.MoveSecurityGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.vpc.v1.SecurityGroupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.vpc.v1.SecurityGroupService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SecurityGroupService(object):
    """A set of methods for managing SecurityGroup resources.
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
            '/yandex.cloud.vpc.v1.SecurityGroupService/Get',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.GetSecurityGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__pb2.SecurityGroup.FromString,
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
            '/yandex.cloud.vpc.v1.SecurityGroupService/List',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupsRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupsResponse.FromString,
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
            '/yandex.cloud.vpc.v1.SecurityGroupService/Create',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.CreateSecurityGroupRequest.SerializeToString,
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
            '/yandex.cloud.vpc.v1.SecurityGroupService/Update',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRequest.SerializeToString,
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
    def UpdateRules(request,
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
            '/yandex.cloud.vpc.v1.SecurityGroupService/UpdateRules',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRulesRequest.SerializeToString,
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
    def UpdateRule(request,
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
            '/yandex.cloud.vpc.v1.SecurityGroupService/UpdateRule',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.UpdateSecurityGroupRuleRequest.SerializeToString,
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
            '/yandex.cloud.vpc.v1.SecurityGroupService/Delete',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.DeleteSecurityGroupRequest.SerializeToString,
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
    def Move(request,
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
            '/yandex.cloud.vpc.v1.SecurityGroupService/Move',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.MoveSecurityGroupRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.vpc.v1.SecurityGroupService/ListOperations',
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_vpc_dot_v1_dot_security__group__service__pb2.ListSecurityGroupOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
