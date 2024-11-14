"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Backup(google.protobuf.message.Message):
    """Description of a Redis backup. For more information, see
    the Managed Service for Redis [documentation](/docs/managed-redis/concepts/backup).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _BackupType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _BackupTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Backup._BackupType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        BACKUP_TYPE_UNSPECIFIED: Backup._BackupType.ValueType  # 0
        AUTOMATED: Backup._BackupType.ValueType  # 1
        """Backup created by automated daily schedule"""
        MANUAL: Backup._BackupType.ValueType  # 2
        """Backup created by user request"""

    class BackupType(_BackupType, metaclass=_BackupTypeEnumTypeWrapper): ...
    BACKUP_TYPE_UNSPECIFIED: Backup.BackupType.ValueType  # 0
    AUTOMATED: Backup.BackupType.ValueType  # 1
    """Backup created by automated daily schedule"""
    MANUAL: Backup.BackupType.ValueType  # 2
    """Backup created by user request"""

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    SOURCE_CLUSTER_ID_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    SOURCE_SHARD_NAMES_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the backup."""
    folder_id: builtins.str
    """ID of the folder that the backup belongs to."""
    source_cluster_id: builtins.str
    """ID of the Redis cluster that the backup was created for."""
    type: global___Backup.BackupType.ValueType
    """How this backup was created (manual/automatic/etc...)"""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format
        (i.e. when the backup operation was completed).
        """

    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Start timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format
        (i.e. when the backup operation was started).
        """

    @property
    def source_shard_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Shard names used as a source for backup."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        source_cluster_id: builtins.str = ...,
        started_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        source_shard_names: collections.abc.Iterable[builtins.str] | None = ...,
        type: global___Backup.BackupType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "started_at", b"started_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "folder_id", b"folder_id", "id", b"id", "source_cluster_id", b"source_cluster_id", "source_shard_names", b"source_shard_names", "started_at", b"started_at", "type", b"type"]) -> None: ...

global___Backup = Backup
