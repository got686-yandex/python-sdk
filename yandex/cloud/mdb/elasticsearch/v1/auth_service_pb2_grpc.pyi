"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.elasticsearch.v1.auth_pb2
import yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class AuthServiceStub:
    """A set of methods for managing Elasticsearch Authentication resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    ListProviders: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.ListAuthProvidersRequest,
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.ListAuthProvidersResponse,
    ]
    """Retrieves the list of registered auth providers for Elasticsearch cluster."""

    GetProvider: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.GetAuthProviderRequest,
        yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider,
    ]
    """Returns registered auth provider by name."""

    AddProviders: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.AddAuthProvidersRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds new auth providers to Elasticsearch cluster."""

    UpdateProviders: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.UpdateAuthProvidersRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Replase the list of auth providers."""

    DeleteProviders: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.DeleteAuthProvidersRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Removes auth providers from Elasticsearch cluster by name."""

    UpdateProvider: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.UpdateAuthProviderRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates registered auth provider."""

    DeleteProvider: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.DeleteAuthProviderRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Removes auth provider from Elasticsearch cluster by name."""

class AuthServiceAsyncStub:
    """A set of methods for managing Elasticsearch Authentication resources."""

    ListProviders: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.ListAuthProvidersRequest,
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.ListAuthProvidersResponse,
    ]
    """Retrieves the list of registered auth providers for Elasticsearch cluster."""

    GetProvider: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.GetAuthProviderRequest,
        yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider,
    ]
    """Returns registered auth provider by name."""

    AddProviders: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.AddAuthProvidersRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Adds new auth providers to Elasticsearch cluster."""

    UpdateProviders: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.UpdateAuthProvidersRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Replase the list of auth providers."""

    DeleteProviders: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.DeleteAuthProvidersRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Removes auth providers from Elasticsearch cluster by name."""

    UpdateProvider: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.UpdateAuthProviderRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates registered auth provider."""

    DeleteProvider: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.DeleteAuthProviderRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Removes auth provider from Elasticsearch cluster by name."""

class AuthServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Elasticsearch Authentication resources."""

    @abc.abstractmethod
    def ListProviders(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.ListAuthProvidersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.ListAuthProvidersResponse, collections.abc.Awaitable[yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.ListAuthProvidersResponse]]:
        """Retrieves the list of registered auth providers for Elasticsearch cluster."""

    @abc.abstractmethod
    def GetProvider(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.GetAuthProviderRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider, collections.abc.Awaitable[yandex.cloud.mdb.elasticsearch.v1.auth_pb2.AuthProvider]]:
        """Returns registered auth provider by name."""

    @abc.abstractmethod
    def AddProviders(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.AddAuthProvidersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Adds new auth providers to Elasticsearch cluster."""

    @abc.abstractmethod
    def UpdateProviders(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.UpdateAuthProvidersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Replase the list of auth providers."""

    @abc.abstractmethod
    def DeleteProviders(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.DeleteAuthProvidersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Removes auth providers from Elasticsearch cluster by name."""

    @abc.abstractmethod
    def UpdateProvider(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.UpdateAuthProviderRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates registered auth provider."""

    @abc.abstractmethod
    def DeleteProvider(
        self,
        request: yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2.DeleteAuthProviderRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Removes auth provider from Elasticsearch cluster by name."""

def add_AuthServiceServicer_to_server(servicer: AuthServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...