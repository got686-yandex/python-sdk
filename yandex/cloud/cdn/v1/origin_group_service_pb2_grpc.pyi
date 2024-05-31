"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.cdn.v1.origin_group_pb2
import yandex.cloud.cdn.v1.origin_group_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class OriginGroupServiceStub:
    """
    Origin Groups management service.
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.origin_group_service_pb2.GetOriginGroupRequest,
        yandex.cloud.cdn.v1.origin_group_pb2.OriginGroup,
    ]
    """Gets origin group with specified origin group id."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.origin_group_service_pb2.ListOriginGroupsRequest,
        yandex.cloud.cdn.v1.origin_group_service_pb2.ListOriginGroupsResponse,
    ]
    """Lists origins of origin group."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.origin_group_service_pb2.CreateOriginGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates origin group."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.origin_group_service_pb2.UpdateOriginGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified origin group.

    Changes may take up to 15 minutes to apply. Afterwards, it is recommended to purge cache of the resources that
    use the origin group via a [CacheService.Purge] request.
    """

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.origin_group_service_pb2.DeleteOriginGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes origin group with specified origin group id."""

class OriginGroupServiceAsyncStub:
    """
    Origin Groups management service.
    """

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.origin_group_service_pb2.GetOriginGroupRequest,
        yandex.cloud.cdn.v1.origin_group_pb2.OriginGroup,
    ]
    """Gets origin group with specified origin group id."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.origin_group_service_pb2.ListOriginGroupsRequest,
        yandex.cloud.cdn.v1.origin_group_service_pb2.ListOriginGroupsResponse,
    ]
    """Lists origins of origin group."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.origin_group_service_pb2.CreateOriginGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates origin group."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.origin_group_service_pb2.UpdateOriginGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified origin group.

    Changes may take up to 15 minutes to apply. Afterwards, it is recommended to purge cache of the resources that
    use the origin group via a [CacheService.Purge] request.
    """

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.cdn.v1.origin_group_service_pb2.DeleteOriginGroupRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes origin group with specified origin group id."""

class OriginGroupServiceServicer(metaclass=abc.ABCMeta):
    """
    Origin Groups management service.
    """

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.cdn.v1.origin_group_service_pb2.GetOriginGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cdn.v1.origin_group_pb2.OriginGroup, collections.abc.Awaitable[yandex.cloud.cdn.v1.origin_group_pb2.OriginGroup]]:
        """Gets origin group with specified origin group id."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.cdn.v1.origin_group_service_pb2.ListOriginGroupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.cdn.v1.origin_group_service_pb2.ListOriginGroupsResponse, collections.abc.Awaitable[yandex.cloud.cdn.v1.origin_group_service_pb2.ListOriginGroupsResponse]]:
        """Lists origins of origin group."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.cdn.v1.origin_group_service_pb2.CreateOriginGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates origin group."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.cdn.v1.origin_group_service_pb2.UpdateOriginGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified origin group.

        Changes may take up to 15 minutes to apply. Afterwards, it is recommended to purge cache of the resources that
        use the origin group via a [CacheService.Purge] request.
        """

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.cdn.v1.origin_group_service_pb2.DeleteOriginGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes origin group with specified origin group id."""

def add_OriginGroupServiceServicer_to_server(servicer: OriginGroupServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...