"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.ai.assistants.v1.threads.message_pb2
import yandex.cloud.ai.assistants.v1.threads.thread_pb2
import yandex.cloud.ai.common.common_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CreateThreadRequest(google.protobuf.message.Message):
    """Request message for creating a new thread."""

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

    FOLDER_ID_FIELD_NUMBER: builtins.int
    MESSAGES_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DEFAULT_MESSAGE_AUTHOR_ID_FIELD_NUMBER: builtins.int
    EXPIRATION_CONFIG_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    name: builtins.str
    """Name of the thread."""
    description: builtins.str
    """Description of the thread."""
    default_message_author_id: builtins.str
    """Default user ID that will be used as the author for thread messages if no other author is specified."""
    @property
    def messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ai.assistants.v1.threads.message_pb2.MessageData]:
        """List of messages to initialize the thread."""

    @property
    def expiration_config(self) -> yandex.cloud.ai.common.common_pb2.ExpirationConfig:
        """Expiration configuration for the thread."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Set of key-value pairs to label the thread."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        messages: collections.abc.Iterable[yandex.cloud.ai.assistants.v1.threads.message_pb2.MessageData] | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        default_message_author_id: builtins.str = ...,
        expiration_config: yandex.cloud.ai.common.common_pb2.ExpirationConfig | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["expiration_config", b"expiration_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["default_message_author_id", b"default_message_author_id", "description", b"description", "expiration_config", b"expiration_config", "folder_id", b"folder_id", "labels", b"labels", "messages", b"messages", "name", b"name"]) -> None: ...

global___CreateThreadRequest = CreateThreadRequest

@typing.final
class GetThreadRequest(google.protobuf.message.Message):
    """Request message for retrieving a thread by ID."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    THREAD_ID_FIELD_NUMBER: builtins.int
    thread_id: builtins.str
    """ID of the thread to retrieve."""
    def __init__(
        self,
        *,
        thread_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["thread_id", b"thread_id"]) -> None: ...

global___GetThreadRequest = GetThreadRequest

@typing.final
class UpdateThreadRequest(google.protobuf.message.Message):
    """Request message for updating an existing thread."""

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

    THREAD_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPIRATION_CONFIG_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    thread_id: builtins.str
    """ID of the thread to update."""
    name: builtins.str
    """New name for the thread."""
    description: builtins.str
    """New description for the thread."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask specifying which fields to update."""

    @property
    def expiration_config(self) -> yandex.cloud.ai.common.common_pb2.ExpirationConfig:
        """New expiration configuration for the thread."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """New set of labels for the thread."""

    def __init__(
        self,
        *,
        thread_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        expiration_config: yandex.cloud.ai.common.common_pb2.ExpirationConfig | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["expiration_config", b"expiration_config", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "expiration_config", b"expiration_config", "labels", b"labels", "name", b"name", "thread_id", b"thread_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateThreadRequest = UpdateThreadRequest

@typing.final
class DeleteThreadRequest(google.protobuf.message.Message):
    """Request message for deleting a thread by ID."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    THREAD_ID_FIELD_NUMBER: builtins.int
    thread_id: builtins.str
    """ID of the thread to delete."""
    def __init__(
        self,
        *,
        thread_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["thread_id", b"thread_id"]) -> None: ...

global___DeleteThreadRequest = DeleteThreadRequest

@typing.final
class DeleteThreadResponse(google.protobuf.message.Message):
    """Response message for the delete operation."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteThreadResponse = DeleteThreadResponse

@typing.final
class ListThreadsRequest(google.protobuf.message.Message):
    """Request message for listing threads in a specific folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Folder ID from which to list threads."""
    page_size: builtins.int
    """Maximum number of threads to return per page."""
    page_token: builtins.str
    """Token to retrieve the next page of results."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListThreadsRequest = ListThreadsRequest

@typing.final
class ListThreadsResponse(google.protobuf.message.Message):
    """Response message for the list operation."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    THREADS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token to retrieve the next page of results."""
    @property
    def threads(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ai.assistants.v1.threads.thread_pb2.Thread]:
        """List of threads in the specified folder."""

    def __init__(
        self,
        *,
        threads: collections.abc.Iterable[yandex.cloud.ai.assistants.v1.threads.thread_pb2.Thread] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "threads", b"threads"]) -> None: ...

global___ListThreadsResponse = ListThreadsResponse
