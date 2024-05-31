"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
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
class LogGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LogGroup._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: LogGroup._Status.ValueType  # 0
        """Unknown status.

        Should never occur.
        """
        CREATING: LogGroup._Status.ValueType  # 1
        """Log group is creating."""
        ACTIVE: LogGroup._Status.ValueType  # 2
        """Log group is ready to accept messages,"""
        DELETING: LogGroup._Status.ValueType  # 3
        """Log group is being deleted.

        No messages will be accepted.
        """
        ERROR: LogGroup._Status.ValueType  # 4
        """Log group is in failed state."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper):
        """Possible log group statuses."""

    STATUS_UNSPECIFIED: LogGroup.Status.ValueType  # 0
    """Unknown status.

    Should never occur.
    """
    CREATING: LogGroup.Status.ValueType  # 1
    """Log group is creating."""
    ACTIVE: LogGroup.Status.ValueType  # 2
    """Log group is ready to accept messages,"""
    DELETING: LogGroup.Status.ValueType  # 3
    """Log group is being deleted.

    No messages will be accepted.
    """
    ERROR: LogGroup.Status.ValueType  # 4
    """Log group is in failed state."""

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CLOUD_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    RETENTION_PERIOD_FIELD_NUMBER: builtins.int
    DATA_STREAM_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Log group ID."""
    folder_id: builtins.str
    """Log group folder ID."""
    cloud_id: builtins.str
    """Log group cloud ID."""
    name: builtins.str
    """Log group name."""
    description: builtins.str
    """Log group description."""
    status: global___LogGroup.Status.ValueType
    """Status of the log group."""
    data_stream: builtins.str
    """Data stream name"""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Log group creation time."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Log group labels."""

    @property
    def retention_period(self) -> google.protobuf.duration_pb2.Duration:
        """Log group entry retention period.

        Entries will be present in group during this period.
        """

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        cloud_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        status: global___LogGroup.Status.ValueType = ...,
        retention_period: google.protobuf.duration_pb2.Duration | None = ...,
        data_stream: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "retention_period", b"retention_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_id", b"cloud_id", "created_at", b"created_at", "data_stream", b"data_stream", "description", b"description", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "retention_period", b"retention_period", "status", b"status"]) -> None: ...

global___LogGroup = LogGroup