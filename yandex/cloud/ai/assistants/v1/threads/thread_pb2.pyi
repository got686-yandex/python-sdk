"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import yandex.cloud.ai.common.common_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Thread(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

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
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DEFAULT_MESSAGE_AUTHOR_ID_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_BY_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    EXPIRATION_CONFIG_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Unique identifier of the thread."""
    folder_id: builtins.str
    """ID of the folder that the thread belongs to."""
    name: builtins.str
    """Name of the thread."""
    description: builtins.str
    """Description of the thread."""
    default_message_author_id: builtins.str
    """Default user ID that will be used as the author for thread messages if no other author is specified."""
    created_by: builtins.str
    """Identifier of the subject who created this thread."""
    updated_by: builtins.str
    """Identifier of the subject who last updated this thread."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp representing when the thread was created."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp representing the last time this thread was updated."""

    @property
    def expiration_config(self) -> yandex.cloud.ai.common.common_pb2.ExpirationConfig:
        """Configuration for the expiration of the thread, defining when and how the thread will expire."""

    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp representing when the thread will expire."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Set of key-value pairs that can be used to organize and categorize the thread."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        default_message_author_id: builtins.str = ...,
        created_by: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_by: builtins.str = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        expiration_config: yandex.cloud.ai.common.common_pb2.ExpirationConfig | None = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "expiration_config", b"expiration_config", "expires_at", b"expires_at", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "created_by", b"created_by", "default_message_author_id", b"default_message_author_id", "description", b"description", "expiration_config", b"expiration_config", "expires_at", b"expires_at", "folder_id", b"folder_id", "id", b"id", "labels", b"labels", "name", b"name", "updated_at", b"updated_at", "updated_by", b"updated_by"]) -> None: ...

global___Thread = Thread