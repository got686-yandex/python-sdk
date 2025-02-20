# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.mdb.redis.v1 import user_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__pb2
from yandex.cloud.mdb.redis.v1 import user_service_pb2 as yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

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
        + f' but the generated code in yandex/cloud/mdb/redis/v1/user_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class UserServiceStub(object):
    """A set of methods for managing Redis User resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.mdb.redis.v1.UserService/Get',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.GetUserRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__pb2.User.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.redis.v1.UserService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.ListUsersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.ListUsersResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.mdb.redis.v1.UserService/Create',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.mdb.redis.v1.UserService/Update',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.mdb.redis.v1.UserService/Delete',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class UserServiceServicer(object):
    """A set of methods for managing Redis User resources.
    """

    def Get(self, request, context):
        """Returns the specified Redis User resource.

        To get the list of available Redis User resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Redis User resources in the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a Redis user in the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified Redis user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified Redis user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.GetUserRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__pb2.User.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.ListUsersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.ListUsersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.CreateUserRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.UpdateUserRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.DeleteUserRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.redis.v1.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.mdb.redis.v1.UserService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """A set of methods for managing Redis User resources.
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
            '/yandex.cloud.mdb.redis.v1.UserService/Get',
            yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.GetUserRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__pb2.User.FromString,
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
            '/yandex.cloud.mdb.redis.v1.UserService/List',
            yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.ListUsersRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.ListUsersResponse.FromString,
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
            '/yandex.cloud.mdb.redis.v1.UserService/Create',
            yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.CreateUserRequest.SerializeToString,
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
            '/yandex.cloud.mdb.redis.v1.UserService/Update',
            yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.UpdateUserRequest.SerializeToString,
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
            '/yandex.cloud.mdb.redis.v1.UserService/Delete',
            yandex_dot_cloud_dot_mdb_dot_redis_dot_v1_dot_user__service__pb2.DeleteUserRequest.SerializeToString,
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
