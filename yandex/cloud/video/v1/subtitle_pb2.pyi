"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
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
class Subtitle(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _SubtitleStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SubtitleStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Subtitle._SubtitleStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SUBTITLE_STATUS_UNSPECIFIED: Subtitle._SubtitleStatus.ValueType  # 0
        """Subtitle status unspecified."""
        WAIT_UPLOADING: Subtitle._SubtitleStatus.ValueType  # 1
        """Waiting for all the bytes to be loaded."""
        UPLOADED: Subtitle._SubtitleStatus.ValueType  # 2
        """Uploading is complete."""

    class SubtitleStatus(_SubtitleStatus, metaclass=_SubtitleStatusEnumTypeWrapper): ...
    SUBTITLE_STATUS_UNSPECIFIED: Subtitle.SubtitleStatus.ValueType  # 0
    """Subtitle status unspecified."""
    WAIT_UPLOADING: Subtitle.SubtitleStatus.ValueType  # 1
    """Waiting for all the bytes to be loaded."""
    UPLOADED: Subtitle.SubtitleStatus.ValueType  # 2
    """Uploading is complete."""

    ID_FIELD_NUMBER: builtins.int
    LANGUAGE_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    FILENAME_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    VIDEO_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the subtitle."""
    language: builtins.str
    """Subtitle language represented as a three-letter ISO 639-3 code."""
    label: builtins.str
    """Subtitle caption to be displayed on screen during video playback."""
    status: global___Subtitle.SubtitleStatus.ValueType
    """Subtitle status."""
    filename: builtins.str
    """Subtitle filename."""
    video_id: builtins.str
    """ID of the video."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when subtitle was created."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of last subtitle update."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        language: builtins.str = ...,
        label: builtins.str = ...,
        status: global___Subtitle.SubtitleStatus.ValueType = ...,
        filename: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        video_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "parent_id", b"parent_id", "updated_at", b"updated_at", "video_id", b"video_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "filename", b"filename", "id", b"id", "label", b"label", "language", b"language", "parent_id", b"parent_id", "status", b"status", "updated_at", b"updated_at", "video_id", b"video_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["parent_id", b"parent_id"]) -> typing.Literal["video_id"] | None: ...

global___Subtitle = Subtitle