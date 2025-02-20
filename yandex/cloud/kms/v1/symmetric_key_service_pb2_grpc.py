# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.kms.v1 import symmetric_key_pb2 as yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__pb2
from yandex.cloud.kms.v1 import symmetric_key_service_pb2 as yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2
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
        + f' but the generated code in yandex/cloud/kms/v1/symmetric_key_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SymmetricKeyServiceStub(object):
    """Set of methods for managing symmetric KMS keys.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/Create',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.CreateSymmetricKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/Get',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.GetSymmetricKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__pb2.SymmetricKey.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/List',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeysRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeysResponse.FromString,
                _registered_method=True)
        self.ListVersions = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/ListVersions',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyVersionsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyVersionsResponse.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/Update',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.UpdateSymmetricKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/Delete',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.DeleteSymmetricKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.SetPrimaryVersion = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/SetPrimaryVersion',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.SetPrimarySymmetricKeyVersionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ScheduleVersionDestruction = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/ScheduleVersionDestruction',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ScheduleSymmetricKeyVersionDestructionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.CancelVersionDestruction = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/CancelVersionDestruction',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.CancelSymmetricKeyVersionDestructionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Rotate = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/Rotate',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.RotateSymmetricKeyRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyOperationsResponse.FromString,
                _registered_method=True)
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                _registered_method=True)
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.kms.v1.SymmetricKeyService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class SymmetricKeyServiceServicer(object):
    """Set of methods for managing symmetric KMS keys.
    """

    def Create(self, request, context):
        """--- control plane

        Creates a symmetric KMS key in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Returns the specified symmetric KMS key.

        To get the list of available symmetric KMS keys, make a [SymmetricKeyService.List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Returns the list of symmetric KMS keys in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListVersions(self, request, context):
        """Returns the list of versions of the specified symmetric KMS key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified symmetric KMS key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified symmetric KMS key. This action also automatically schedules
        the destruction of all of the key's versions in 72 hours.

        The key and its versions appear absent in [SymmetricKeyService.Get] and [SymmetricKeyService.List]
        requests, but can be restored within 72 hours with a request to tech support.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPrimaryVersion(self, request, context):
        """Sets the primary version for the specified key. The primary version is used
        by default for all encrypt/decrypt operations where no version ID is specified.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ScheduleVersionDestruction(self, request, context):
        """Schedules the specified key version for destruction.

        Scheduled destruction can be cancelled with the [SymmetricKeyService.CancelVersionDestruction] method.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelVersionDestruction(self, request, context):
        """Cancels previously scheduled version destruction, if the version hasn't been destroyed yet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Rotate(self, request, context):
        """Rotates the specified key: creates a new key version and makes it the primary version.
        The old version remains available for decryption of ciphertext encrypted with it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified symmetric KMS key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """Lists existing access bindings for the specified key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Sets access bindings for the key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Updates access bindings for the specified key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SymmetricKeyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.CreateSymmetricKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.GetSymmetricKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__pb2.SymmetricKey.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeysRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeysResponse.SerializeToString,
            ),
            'ListVersions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListVersions,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyVersionsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyVersionsResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.UpdateSymmetricKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.DeleteSymmetricKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'SetPrimaryVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPrimaryVersion,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.SetPrimarySymmetricKeyVersionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ScheduleVersionDestruction': grpc.unary_unary_rpc_method_handler(
                    servicer.ScheduleVersionDestruction,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ScheduleSymmetricKeyVersionDestructionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'CancelVersionDestruction': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelVersionDestruction,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.CancelSymmetricKeyVersionDestructionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Rotate': grpc.unary_unary_rpc_method_handler(
                    servicer.Rotate,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.RotateSymmetricKeyRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyOperationsResponse.SerializeToString,
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
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.kms.v1.SymmetricKeyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.kms.v1.SymmetricKeyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SymmetricKeyService(object):
    """Set of methods for managing symmetric KMS keys.
    """

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
            '/yandex.cloud.kms.v1.SymmetricKeyService/Create',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.CreateSymmetricKeyRequest.SerializeToString,
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
            '/yandex.cloud.kms.v1.SymmetricKeyService/Get',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.GetSymmetricKeyRequest.SerializeToString,
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__pb2.SymmetricKey.FromString,
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
            '/yandex.cloud.kms.v1.SymmetricKeyService/List',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeysRequest.SerializeToString,
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeysResponse.FromString,
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
    def ListVersions(request,
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
            '/yandex.cloud.kms.v1.SymmetricKeyService/ListVersions',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyVersionsRequest.SerializeToString,
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyVersionsResponse.FromString,
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
            '/yandex.cloud.kms.v1.SymmetricKeyService/Update',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.UpdateSymmetricKeyRequest.SerializeToString,
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
            '/yandex.cloud.kms.v1.SymmetricKeyService/Delete',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.DeleteSymmetricKeyRequest.SerializeToString,
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
    def SetPrimaryVersion(request,
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
            '/yandex.cloud.kms.v1.SymmetricKeyService/SetPrimaryVersion',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.SetPrimarySymmetricKeyVersionRequest.SerializeToString,
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
    def ScheduleVersionDestruction(request,
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
            '/yandex.cloud.kms.v1.SymmetricKeyService/ScheduleVersionDestruction',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ScheduleSymmetricKeyVersionDestructionRequest.SerializeToString,
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
    def CancelVersionDestruction(request,
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
            '/yandex.cloud.kms.v1.SymmetricKeyService/CancelVersionDestruction',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.CancelSymmetricKeyVersionDestructionRequest.SerializeToString,
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
    def Rotate(request,
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
            '/yandex.cloud.kms.v1.SymmetricKeyService/Rotate',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.RotateSymmetricKeyRequest.SerializeToString,
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
            '/yandex.cloud.kms.v1.SymmetricKeyService/ListOperations',
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__service__pb2.ListSymmetricKeyOperationsResponse.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.kms.v1.SymmetricKeyService/ListAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.kms.v1.SymmetricKeyService/SetAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.kms.v1.SymmetricKeyService/UpdateAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
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
