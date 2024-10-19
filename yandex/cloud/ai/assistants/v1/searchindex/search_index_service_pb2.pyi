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
import yandex.cloud.ai.assistants.v1.searchindex.search_index_pb2
import yandex.cloud.ai.common.common_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CreateSearchIndexRequest(google.protobuf.message.Message):
    """Request to create a new search index."""

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
    FILE_IDS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPIRATION_CONFIG_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    TEXT_SEARCH_INDEX_FIELD_NUMBER: builtins.int
    VECTOR_SEARCH_INDEX_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    name: builtins.str
    """Name of the search index."""
    description: builtins.str
    """Description of the search index."""
    @property
    def file_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of file IDs to be indexed."""

    @property
    def expiration_config(self) -> yandex.cloud.ai.common.common_pb2.ExpirationConfig:
        """Expiration configuration for the search index."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Set of key-value pairs to label the search index."""

    @property
    def text_search_index(self) -> yandex.cloud.ai.assistants.v1.searchindex.search_index_pb2.TextSearchIndex:
        """Configuration for a traditional keyword-based text search index."""

    @property
    def vector_search_index(self) -> yandex.cloud.ai.assistants.v1.searchindex.search_index_pb2.VectorSearchIndex:
        """Configuration for a vector-based search index using embeddings."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        file_ids: collections.abc.Iterable[builtins.str] | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        expiration_config: yandex.cloud.ai.common.common_pb2.ExpirationConfig | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        text_search_index: yandex.cloud.ai.assistants.v1.searchindex.search_index_pb2.TextSearchIndex | None = ...,
        vector_search_index: yandex.cloud.ai.assistants.v1.searchindex.search_index_pb2.VectorSearchIndex | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["IndexType", b"IndexType", "expiration_config", b"expiration_config", "text_search_index", b"text_search_index", "vector_search_index", b"vector_search_index"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["IndexType", b"IndexType", "description", b"description", "expiration_config", b"expiration_config", "file_ids", b"file_ids", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "text_search_index", b"text_search_index", "vector_search_index", b"vector_search_index"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["IndexType", b"IndexType"]) -> typing.Literal["text_search_index", "vector_search_index"] | None: ...

global___CreateSearchIndexRequest = CreateSearchIndexRequest

@typing.final
class GetSearchIndexRequest(google.protobuf.message.Message):
    """Request message for retrieving a search index by ID."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEARCH_INDEX_ID_FIELD_NUMBER: builtins.int
    search_index_id: builtins.str
    """ID of the search index to retrieve."""
    def __init__(
        self,
        *,
        search_index_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["search_index_id", b"search_index_id"]) -> None: ...

global___GetSearchIndexRequest = GetSearchIndexRequest

@typing.final
class UpdateSearchIndexRequest(google.protobuf.message.Message):
    """Request message for updating an existing search index."""

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

    SEARCH_INDEX_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPIRATION_CONFIG_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    search_index_id: builtins.str
    """ID of the search index to update."""
    name: builtins.str
    """New name for the search index."""
    description: builtins.str
    """New description for the search index."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask specifying which fields to update."""

    @property
    def expiration_config(self) -> yandex.cloud.ai.common.common_pb2.ExpirationConfig:
        """New expiration configuration for the search index."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """New set of labels for the search index."""

    def __init__(
        self,
        *,
        search_index_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        expiration_config: yandex.cloud.ai.common.common_pb2.ExpirationConfig | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["expiration_config", b"expiration_config", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "expiration_config", b"expiration_config", "labels", b"labels", "name", b"name", "search_index_id", b"search_index_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateSearchIndexRequest = UpdateSearchIndexRequest

@typing.final
class DeleteSearchIndexRequest(google.protobuf.message.Message):
    """Request message for deleting a search index by ID."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEARCH_INDEX_ID_FIELD_NUMBER: builtins.int
    search_index_id: builtins.str
    """ID of the search index to delete."""
    def __init__(
        self,
        *,
        search_index_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["search_index_id", b"search_index_id"]) -> None: ...

global___DeleteSearchIndexRequest = DeleteSearchIndexRequest

@typing.final
class DeleteSearchIndexResponse(google.protobuf.message.Message):
    """Response message for the delete operation."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteSearchIndexResponse = DeleteSearchIndexResponse

@typing.final
class ListSearchIndicesRequest(google.protobuf.message.Message):
    """Request message for listing search indexes in a specific folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Folder ID from which to list search indexes."""
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

global___ListSearchIndicesRequest = ListSearchIndicesRequest

@typing.final
class ListSearchIndicesResponse(google.protobuf.message.Message):
    """Response message for the list operation."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INDICES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token to retrieve the next page of results."""
    @property
    def indices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ai.assistants.v1.searchindex.search_index_pb2.SearchIndex]:
        """List of search indexes in the specified folder."""

    def __init__(
        self,
        *,
        indices: collections.abc.Iterable[yandex.cloud.ai.assistants.v1.searchindex.search_index_pb2.SearchIndex] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["indices", b"indices", "next_page_token", b"next_page_token"]) -> None: ...

global___ListSearchIndicesResponse = ListSearchIndicesResponse
