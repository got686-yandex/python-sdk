"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.ai.assistants.v1.searchindex.search_index_file_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetSearchIndexFileRequest(google.protobuf.message.Message):
    """Request message for retrieving a file from a search index."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_ID_FIELD_NUMBER: builtins.int
    SEARCH_INDEX_ID_FIELD_NUMBER: builtins.int
    file_id: builtins.str
    """ID of the file to retrieve."""
    search_index_id: builtins.str
    """ID of the search index that contains the file."""
    def __init__(
        self,
        *,
        file_id: builtins.str = ...,
        search_index_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["file_id", b"file_id", "search_index_id", b"search_index_id"]) -> None: ...

global___GetSearchIndexFileRequest = GetSearchIndexFileRequest

@typing.final
class ListSearchIndexFilesRequest(google.protobuf.message.Message):
    """Request message for listing files in a specific search index."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEARCH_INDEX_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    search_index_id: builtins.str
    """ID of the search index whose files will be listed."""
    page_size: builtins.int
    """Maximum number of files to return per page."""
    page_token: builtins.str
    """Token to retrieve the next page of results."""
    def __init__(
        self,
        *,
        search_index_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "page_token", b"page_token", "search_index_id", b"search_index_id"]) -> None: ...

global___ListSearchIndexFilesRequest = ListSearchIndexFilesRequest

@typing.final
class ListSearchIndexFilesResponse(google.protobuf.message.Message):
    """Response message for the list operation."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token to retrieve the next page of results."""
    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ai.assistants.v1.searchindex.search_index_file_pb2.SearchIndexFile]:
        """List of files in the specified search index."""

    def __init__(
        self,
        *,
        files: collections.abc.Iterable[yandex.cloud.ai.assistants.v1.searchindex.search_index_file_pb2.SearchIndexFile] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["files", b"files", "next_page_token", b"next_page_token"]) -> None: ...

global___ListSearchIndexFilesResponse = ListSearchIndexFilesResponse
