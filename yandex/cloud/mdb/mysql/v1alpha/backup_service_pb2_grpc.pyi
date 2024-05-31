"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.mdb.mysql.v1alpha.backup_pb2
import yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class BackupServiceStub:
    """A set of methods for managing MySQL backups."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2.GetBackupRequest,
        yandex.cloud.mdb.mysql.v1alpha.backup_pb2.Backup,
    ]
    """Returns the specified MySQL backup.

    To get the list of available MySQL backups, make a [List] request.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2.ListBackupsRequest,
        yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2.ListBackupsResponse,
    ]
    """Retrieves the list of MySQL backups available for the specified folder."""

class BackupServiceAsyncStub:
    """A set of methods for managing MySQL backups."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2.GetBackupRequest,
        yandex.cloud.mdb.mysql.v1alpha.backup_pb2.Backup,
    ]
    """Returns the specified MySQL backup.

    To get the list of available MySQL backups, make a [List] request.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2.ListBackupsRequest,
        yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2.ListBackupsResponse,
    ]
    """Retrieves the list of MySQL backups available for the specified folder."""

class BackupServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing MySQL backups."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2.GetBackupRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mysql.v1alpha.backup_pb2.Backup, collections.abc.Awaitable[yandex.cloud.mdb.mysql.v1alpha.backup_pb2.Backup]]:
        """Returns the specified MySQL backup.

        To get the list of available MySQL backups, make a [List] request.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2.ListBackupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2.ListBackupsResponse, collections.abc.Awaitable[yandex.cloud.mdb.mysql.v1alpha.backup_service_pb2.ListBackupsResponse]]:
        """Retrieves the list of MySQL backups available for the specified folder."""

def add_BackupServiceServicer_to_server(servicer: BackupServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...