"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.operation.operation_pb2
import yandex.cloud.organizationmanager.v1.os_login_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class OsLoginServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetSettings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.GetOsLoginSettingsRequest,
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.OsLoginSettings,
    ]
    """OsLogin settings"""

    UpdateSettings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.UpdateOsLoginSettingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

    GetProfile: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.GetOsLoginProfileRequest,
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.OsLoginProfile,
    ]
    """OsLogin Profiles"""

    ListProfiles: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.ListOsLoginProfilesRequest,
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.ListOsLoginProfilesResponse,
    ]

    CreateProfile: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.CreateOsLoginProfileRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

    UpdateProfile: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.UpdateOsLoginProfileRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

    SetDefaultProfile: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.SetDefaultOsLoginProfileRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets a profile as a default for the subject assigned to this profile"""

    DeleteProfile: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.DeleteOsLoginProfileRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

class OsLoginServiceAsyncStub:
    GetSettings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.GetOsLoginSettingsRequest,
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.OsLoginSettings,
    ]
    """OsLogin settings"""

    UpdateSettings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.UpdateOsLoginSettingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

    GetProfile: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.GetOsLoginProfileRequest,
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.OsLoginProfile,
    ]
    """OsLogin Profiles"""

    ListProfiles: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.ListOsLoginProfilesRequest,
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.ListOsLoginProfilesResponse,
    ]

    CreateProfile: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.CreateOsLoginProfileRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

    UpdateProfile: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.UpdateOsLoginProfileRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

    SetDefaultProfile: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.SetDefaultOsLoginProfileRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets a profile as a default for the subject assigned to this profile"""

    DeleteProfile: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.organizationmanager.v1.os_login_service_pb2.DeleteOsLoginProfileRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]

class OsLoginServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetSettings(
        self,
        request: yandex.cloud.organizationmanager.v1.os_login_service_pb2.GetOsLoginSettingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.organizationmanager.v1.os_login_service_pb2.OsLoginSettings, collections.abc.Awaitable[yandex.cloud.organizationmanager.v1.os_login_service_pb2.OsLoginSettings]]:
        """OsLogin settings"""

    @abc.abstractmethod
    def UpdateSettings(
        self,
        request: yandex.cloud.organizationmanager.v1.os_login_service_pb2.UpdateOsLoginSettingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def GetProfile(
        self,
        request: yandex.cloud.organizationmanager.v1.os_login_service_pb2.GetOsLoginProfileRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.organizationmanager.v1.os_login_service_pb2.OsLoginProfile, collections.abc.Awaitable[yandex.cloud.organizationmanager.v1.os_login_service_pb2.OsLoginProfile]]:
        """OsLogin Profiles"""

    @abc.abstractmethod
    def ListProfiles(
        self,
        request: yandex.cloud.organizationmanager.v1.os_login_service_pb2.ListOsLoginProfilesRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.organizationmanager.v1.os_login_service_pb2.ListOsLoginProfilesResponse, collections.abc.Awaitable[yandex.cloud.organizationmanager.v1.os_login_service_pb2.ListOsLoginProfilesResponse]]: ...

    @abc.abstractmethod
    def CreateProfile(
        self,
        request: yandex.cloud.organizationmanager.v1.os_login_service_pb2.CreateOsLoginProfileRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def UpdateProfile(
        self,
        request: yandex.cloud.organizationmanager.v1.os_login_service_pb2.UpdateOsLoginProfileRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]: ...

    @abc.abstractmethod
    def SetDefaultProfile(
        self,
        request: yandex.cloud.organizationmanager.v1.os_login_service_pb2.SetDefaultOsLoginProfileRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets a profile as a default for the subject assigned to this profile"""

    @abc.abstractmethod
    def DeleteProfile(
        self,
        request: yandex.cloud.organizationmanager.v1.os_login_service_pb2.DeleteOsLoginProfileRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]: ...

def add_OsLoginServiceServicer_to_server(servicer: OsLoginServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...