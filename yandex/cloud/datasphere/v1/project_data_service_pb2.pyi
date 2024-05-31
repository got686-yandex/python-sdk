"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class FileMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    SIZE_BYTES_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the Project resource associated with the file."""
    path: builtins.str
    """File path."""
    size_bytes: builtins.int
    """File size in bytes."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        path: builtins.str = ...,
        size_bytes: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["path", b"path", "project_id", b"project_id", "size_bytes", b"size_bytes"]) -> None: ...

global___FileMetadata = FileMetadata

@typing.final
class UploadFileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    CHUNK_FIELD_NUMBER: builtins.int
    chunk: builtins.bytes
    """Byte chunk of the file to upload."""
    @property
    def metadata(self) -> global___FileMetadata:
        """Metadata of the file to upload."""

    def __init__(
        self,
        *,
        metadata: global___FileMetadata | None = ...,
        chunk: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["chunk", b"chunk", "message", b"message", "metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["chunk", b"chunk", "message", b"message", "metadata", b"metadata"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["message", b"message"]) -> typing.Literal["metadata", "chunk"] | None: ...

global___UploadFileRequest = UploadFileRequest

@typing.final
class UploadFileResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> global___FileMetadata:
        """Metadata of the uploaded file."""

    def __init__(
        self,
        *,
        metadata: global___FileMetadata | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["metadata", b"metadata"]) -> None: ...

global___UploadFileResponse = UploadFileResponse

@typing.final
class DownloadFileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    FILE_PATH_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the Project resource to download the file from."""
    file_path: builtins.str
    """Path of the file to download."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        file_path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["file_path", b"file_path", "project_id", b"project_id"]) -> None: ...

global___DownloadFileRequest = DownloadFileRequest

@typing.final
class DownloadFileResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METADATA_FIELD_NUMBER: builtins.int
    CHUNK_FIELD_NUMBER: builtins.int
    chunk: builtins.bytes
    """Byte chunk of the downloaded file."""
    @property
    def metadata(self) -> global___FileMetadata:
        """Metadata of the downloaded file."""

    def __init__(
        self,
        *,
        metadata: global___FileMetadata | None = ...,
        chunk: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["chunk", b"chunk", "message", b"message", "metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["chunk", b"chunk", "message", b"message", "metadata", b"metadata"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["message", b"message"]) -> typing.Literal["metadata", "chunk"] | None: ...

global___DownloadFileResponse = DownloadFileResponse