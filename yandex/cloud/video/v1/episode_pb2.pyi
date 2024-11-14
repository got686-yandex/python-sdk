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
class Episode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _VisibilityStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _VisibilityStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Episode._VisibilityStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        VISIBILITY_STATUS_UNSPECIFIED: Episode._VisibilityStatus.ValueType  # 0
        PUBLISHED: Episode._VisibilityStatus.ValueType  # 1
        UNPUBLISHED: Episode._VisibilityStatus.ValueType  # 2

    class VisibilityStatus(_VisibilityStatus, metaclass=_VisibilityStatusEnumTypeWrapper): ...
    VISIBILITY_STATUS_UNSPECIFIED: Episode.VisibilityStatus.ValueType  # 0
    PUBLISHED: Episode.VisibilityStatus.ValueType  # 1
    UNPUBLISHED: Episode.VisibilityStatus.ValueType  # 2

    ID_FIELD_NUMBER: builtins.int
    STREAM_ID_FIELD_NUMBER: builtins.int
    LINE_ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    FINISH_TIME_FIELD_NUMBER: builtins.int
    DVR_SECONDS_FIELD_NUMBER: builtins.int
    VISIBILITY_STATUS_FIELD_NUMBER: builtins.int
    PUBLIC_ACCESS_FIELD_NUMBER: builtins.int
    AUTH_SYSTEM_ACCESS_FIELD_NUMBER: builtins.int
    SIGN_URL_ACCESS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the episode."""
    stream_id: builtins.str
    """ID of the stream. Optional, empty if the episode is linked to the line"""
    line_id: builtins.str
    """ID of the line. Optional, empty if the episode is linked to the stream"""
    title: builtins.str
    """Channel title."""
    description: builtins.str
    """Channel description."""
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    dvr_seconds: builtins.int
    """Enables episode DVR mode. DVR seconds determines how many last seconds of the stream are available.

    possible values:
     * `0`: infinite dvr size, the full length of the stream allowed to display
     * `>0`: size of dvr window in seconds, the minimum value is 30s
    """
    visibility_status: global___Episode.VisibilityStatus.ValueType
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Episode start time."""

    @property
    def finish_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Episode finish time."""

    @property
    def public_access(self) -> global___EpisodePublicAccessRights:
        """Episode is available to everyone."""

    @property
    def auth_system_access(self) -> global___EpisodeAuthSystemAccessRights:
        """Checking access rights using the authorization system."""

    @property
    def sign_url_access(self) -> global___EpisodeSignURLAccessRights:
        """Checking access rights using url's signature."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when episode was created."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of last episode update."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        stream_id: builtins.str = ...,
        line_id: builtins.str = ...,
        title: builtins.str = ...,
        description: builtins.str = ...,
        thumbnail_id: builtins.str = ...,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finish_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        dvr_seconds: builtins.int = ...,
        visibility_status: global___Episode.VisibilityStatus.ValueType = ...,
        public_access: global___EpisodePublicAccessRights | None = ...,
        auth_system_access: global___EpisodeAuthSystemAccessRights | None = ...,
        sign_url_access: global___EpisodeSignURLAccessRights | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["access_rights", b"access_rights", "auth_system_access", b"auth_system_access", "created_at", b"created_at", "finish_time", b"finish_time", "public_access", b"public_access", "sign_url_access", b"sign_url_access", "start_time", b"start_time", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["access_rights", b"access_rights", "auth_system_access", b"auth_system_access", "created_at", b"created_at", "description", b"description", "dvr_seconds", b"dvr_seconds", "finish_time", b"finish_time", "id", b"id", "line_id", b"line_id", "public_access", b"public_access", "sign_url_access", b"sign_url_access", "start_time", b"start_time", "stream_id", b"stream_id", "thumbnail_id", b"thumbnail_id", "title", b"title", "updated_at", b"updated_at", "visibility_status", b"visibility_status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["access_rights", b"access_rights"]) -> typing.Literal["public_access", "auth_system_access", "sign_url_access"] | None: ...

global___Episode = Episode

@typing.final
class EpisodePublicAccessRights(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___EpisodePublicAccessRights = EpisodePublicAccessRights

@typing.final
class EpisodeAuthSystemAccessRights(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___EpisodeAuthSystemAccessRights = EpisodeAuthSystemAccessRights

@typing.final
class EpisodeSignURLAccessRights(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___EpisodeSignURLAccessRights = EpisodeSignURLAccessRights
