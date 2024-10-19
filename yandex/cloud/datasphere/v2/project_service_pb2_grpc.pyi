"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import typing
import yandex.cloud.access.access_pb2
import yandex.cloud.datasphere.v2.project_pb2
import yandex.cloud.datasphere.v2.project_service_pb2
import yandex.cloud.datasphere.v2.restrictions_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ProjectServiceStub:
    """A set of methods for managing Project resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.CreateProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a project in the specified folder."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.UpdateProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified project."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.DeleteProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified project."""

    Open: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.OpenProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Opens the specified project."""

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.GetProjectRequest,
        yandex.cloud.datasphere.v2.project_pb2.Project,
    ]
    """Returns the specified project."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.ListProjectsRequest,
        yandex.cloud.datasphere.v2.project_service_pb2.ListProjectsResponse,
    ]
    """Lists projects for the specified community."""

    GetUnitBalance: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.GetUnitBalanceRequest,
        yandex.cloud.datasphere.v2.project_service_pb2.GetUnitBalanceResponse,
    ]
    """Returns the unit balance of the specified project."""

    SetUnitBalance: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.SetUnitBalanceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets the unit balance of the specified project."""

    Execute: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.ProjectExecutionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Executes code of the specified notebook using configuration defined in the project settings. If the default project configuration is not specified, `c1.4` is used."""

    ListAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists access bindings for the project."""

    SetAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the project."""

    UpdateAccessBindings: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the project."""

    AddResource: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.AddResourceToProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds shared resource to project"""

    RemoveResource: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.RemoveResourceFromProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Removes shared resource from project"""

    ResizeDisk: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.ResizeProjectDiskRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Resizes project disk"""

    GetRestrictionsMeta: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        yandex.cloud.datasphere.v2.restrictions_pb2.GetRestrictionsMetaResponse,
    ]
    """Get meta information about available restrictions."""

    GetRestrictions: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.GetProjectRestrictionsRequest,
        yandex.cloud.datasphere.v2.restrictions_pb2.RestrictionsResponse,
    ]
    """Get current project restrictions."""

    SetRestrictions: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.SetProjectRestrictionsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Set project restrictions."""

class ProjectServiceAsyncStub:
    """A set of methods for managing Project resources."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.CreateProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a project in the specified folder."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.UpdateProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified project."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.DeleteProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified project."""

    Open: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.OpenProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Opens the specified project."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.GetProjectRequest,
        yandex.cloud.datasphere.v2.project_pb2.Project,
    ]
    """Returns the specified project."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.ListProjectsRequest,
        yandex.cloud.datasphere.v2.project_service_pb2.ListProjectsResponse,
    ]
    """Lists projects for the specified community."""

    GetUnitBalance: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.GetUnitBalanceRequest,
        yandex.cloud.datasphere.v2.project_service_pb2.GetUnitBalanceResponse,
    ]
    """Returns the unit balance of the specified project."""

    SetUnitBalance: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.SetUnitBalanceRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets the unit balance of the specified project."""

    Execute: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.ProjectExecutionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Executes code of the specified notebook using configuration defined in the project settings. If the default project configuration is not specified, `c1.4` is used."""

    ListAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        yandex.cloud.access.access_pb2.ListAccessBindingsResponse,
    ]
    """Lists access bindings for the project."""

    SetAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Sets access bindings for the project."""

    UpdateAccessBindings: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates access bindings for the project."""

    AddResource: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.AddResourceToProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds shared resource to project"""

    RemoveResource: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.RemoveResourceFromProjectRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Removes shared resource from project"""

    ResizeDisk: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.ResizeProjectDiskRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Resizes project disk"""

    GetRestrictionsMeta: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        yandex.cloud.datasphere.v2.restrictions_pb2.GetRestrictionsMetaResponse,
    ]
    """Get meta information about available restrictions."""

    GetRestrictions: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.GetProjectRestrictionsRequest,
        yandex.cloud.datasphere.v2.restrictions_pb2.RestrictionsResponse,
    ]
    """Get current project restrictions."""

    SetRestrictions: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.datasphere.v2.project_service_pb2.SetProjectRestrictionsRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Set project restrictions."""

class ProjectServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Project resources."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.CreateProjectRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a project in the specified folder."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.UpdateProjectRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified project."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.DeleteProjectRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified project."""

    @abc.abstractmethod
    def Open(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.OpenProjectRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Opens the specified project."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.GetProjectRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.datasphere.v2.project_pb2.Project, collections.abc.Awaitable[yandex.cloud.datasphere.v2.project_pb2.Project]]:
        """Returns the specified project."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.ListProjectsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.datasphere.v2.project_service_pb2.ListProjectsResponse, collections.abc.Awaitable[yandex.cloud.datasphere.v2.project_service_pb2.ListProjectsResponse]]:
        """Lists projects for the specified community."""

    @abc.abstractmethod
    def GetUnitBalance(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.GetUnitBalanceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.datasphere.v2.project_service_pb2.GetUnitBalanceResponse, collections.abc.Awaitable[yandex.cloud.datasphere.v2.project_service_pb2.GetUnitBalanceResponse]]:
        """Returns the unit balance of the specified project."""

    @abc.abstractmethod
    def SetUnitBalance(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.SetUnitBalanceRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets the unit balance of the specified project."""

    @abc.abstractmethod
    def Execute(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.ProjectExecutionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Executes code of the specified notebook using configuration defined in the project settings. If the default project configuration is not specified, `c1.4` is used."""

    @abc.abstractmethod
    def ListAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.ListAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.access.access_pb2.ListAccessBindingsResponse, collections.abc.Awaitable[yandex.cloud.access.access_pb2.ListAccessBindingsResponse]]:
        """Lists access bindings for the project."""

    @abc.abstractmethod
    def SetAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.SetAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Sets access bindings for the project."""

    @abc.abstractmethod
    def UpdateAccessBindings(
        self,
        request: yandex.cloud.access.access_pb2.UpdateAccessBindingsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates access bindings for the project."""

    @abc.abstractmethod
    def AddResource(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.AddResourceToProjectRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Adds shared resource to project"""

    @abc.abstractmethod
    def RemoveResource(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.RemoveResourceFromProjectRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Removes shared resource from project"""

    @abc.abstractmethod
    def ResizeDisk(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.ResizeProjectDiskRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Resizes project disk"""

    @abc.abstractmethod
    def GetRestrictionsMeta(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.datasphere.v2.restrictions_pb2.GetRestrictionsMetaResponse, collections.abc.Awaitable[yandex.cloud.datasphere.v2.restrictions_pb2.GetRestrictionsMetaResponse]]:
        """Get meta information about available restrictions."""

    @abc.abstractmethod
    def GetRestrictions(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.GetProjectRestrictionsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.datasphere.v2.restrictions_pb2.RestrictionsResponse, collections.abc.Awaitable[yandex.cloud.datasphere.v2.restrictions_pb2.RestrictionsResponse]]:
        """Get current project restrictions."""

    @abc.abstractmethod
    def SetRestrictions(
        self,
        request: yandex.cloud.datasphere.v2.project_service_pb2.SetProjectRestrictionsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Set project restrictions."""

def add_ProjectServiceServicer_to_server(servicer: ProjectServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
