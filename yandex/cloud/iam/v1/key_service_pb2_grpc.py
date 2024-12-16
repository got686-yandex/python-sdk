# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.iam.v1 import key_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_key__pb2
from yandex.cloud.iam.v1 import key_service_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2
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
        + f' but the generated code in yandex/cloud/iam/v1/key_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class KeyServiceStub(object):
    """A set of methods for managing Key resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.iam.v1.KeyService/Get',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.GetKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__pb2.Key.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.iam.v1.KeyService/List',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeysRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeysResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.iam.v1.KeyService/Create',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.CreateKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.CreateKeyResponse.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.iam.v1.KeyService/Update',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.UpdateKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.iam.v1.KeyService/Delete',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.DeleteKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.iam.v1.KeyService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeyOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeyOperationsResponse.FromString,
                _registered_method=True)


class KeyServiceServicer(object):
    """A set of methods for managing Key resources.
    """

    def Get(self, request, context):
        """Returns the specified Key resource.

        To get the list of available Key resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Key resources for the specified service account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a key pair for the specified service account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified key pair.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified key pair.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.GetKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__pb2.Key.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeysRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeysResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.CreateKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.CreateKeyResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.UpdateKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.DeleteKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeyOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeyOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.iam.v1.KeyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.iam.v1.KeyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class KeyService(object):
    """A set of methods for managing Key resources.
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
            '/yandex.cloud.iam.v1.KeyService/Get',
            yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.GetKeyRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_key__pb2.Key.FromString,
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
            '/yandex.cloud.iam.v1.KeyService/List',
            yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeysRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeysResponse.FromString,
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
            '/yandex.cloud.iam.v1.KeyService/Create',
            yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.CreateKeyRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.CreateKeyResponse.FromString,
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
            '/yandex.cloud.iam.v1.KeyService/Update',
            yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.UpdateKeyRequest.SerializeToString,
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
            '/yandex.cloud.iam.v1.KeyService/Delete',
            yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.DeleteKeyRequest.SerializeToString,
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
            '/yandex.cloud.iam.v1.KeyService/ListOperations',
            yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeyOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_key__service__pb2.ListKeyOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
