"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.airflow.v1.cluster_pb2
import yandex.cloud.airflow.v1.cluster_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ClusterServiceStub:
    """A set of methods for managing Apache Airflow Cluster resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.airflow.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified Apache Airflow Cluster resource."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.airflow.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves a list of Apache Airflow Cluster resources."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates an Apache Airflow cluster."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified Apache Airflow cluster."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified Apache Airflow cluster."""

    Start: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified Apache Airflow cluster."""

    Stop: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified Apache Airflow cluster."""

    ListOperations: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.airflow.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of Operation resources for the specified cluster."""

class ClusterServiceAsyncStub:
    """A set of methods for managing Apache Airflow Cluster resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.GetClusterRequest,
        yandex.cloud.airflow.v1.cluster_pb2.Cluster,
    ]
    """Returns the specified Apache Airflow Cluster resource."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.ListClustersRequest,
        yandex.cloud.airflow.v1.cluster_service_pb2.ListClustersResponse,
    ]
    """Retrieves a list of Apache Airflow Cluster resources."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.CreateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates an Apache Airflow cluster."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.UpdateClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified Apache Airflow cluster."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.DeleteClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified Apache Airflow cluster."""

    Start: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.StartClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Starts the specified Apache Airflow cluster."""

    Stop: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.StopClusterRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Stops the specified Apache Airflow cluster."""

    ListOperations: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.airflow.v1.cluster_service_pb2.ListClusterOperationsRequest,
        yandex.cloud.airflow.v1.cluster_service_pb2.ListClusterOperationsResponse,
    ]
    """Retrieves the list of Operation resources for the specified cluster."""

class ClusterServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Apache Airflow Cluster resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.airflow.v1.cluster_service_pb2.GetClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.airflow.v1.cluster_pb2.Cluster, collections.abc.Awaitable[yandex.cloud.airflow.v1.cluster_pb2.Cluster]]:
        """Returns the specified Apache Airflow Cluster resource."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.airflow.v1.cluster_service_pb2.ListClustersRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.airflow.v1.cluster_service_pb2.ListClustersResponse, collections.abc.Awaitable[yandex.cloud.airflow.v1.cluster_service_pb2.ListClustersResponse]]:
        """Retrieves a list of Apache Airflow Cluster resources."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.airflow.v1.cluster_service_pb2.CreateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates an Apache Airflow cluster."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.airflow.v1.cluster_service_pb2.UpdateClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified Apache Airflow cluster."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.airflow.v1.cluster_service_pb2.DeleteClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified Apache Airflow cluster."""

    @abc.abstractmethod
    def Start(
        self,
        request: yandex.cloud.airflow.v1.cluster_service_pb2.StartClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Starts the specified Apache Airflow cluster."""

    @abc.abstractmethod
    def Stop(
        self,
        request: yandex.cloud.airflow.v1.cluster_service_pb2.StopClusterRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Stops the specified Apache Airflow cluster."""

    @abc.abstractmethod
    def ListOperations(
        self,
        request: yandex.cloud.airflow.v1.cluster_service_pb2.ListClusterOperationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.airflow.v1.cluster_service_pb2.ListClusterOperationsResponse, collections.abc.Awaitable[yandex.cloud.airflow.v1.cluster_service_pb2.ListClusterOperationsResponse]]:
        """Retrieves the list of Operation resources for the specified cluster."""

def add_ClusterServiceServicer_to_server(servicer: ClusterServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...