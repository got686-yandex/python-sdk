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

class _AutoTranscode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AutoTranscodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AutoTranscode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    AUTO_TRANSCODE_UNSPECIFIED: _AutoTranscode.ValueType  # 0
    """Unspecified auto transcoding value."""
    ENABLE: _AutoTranscode.ValueType  # 1
    """Enable auto transcoding."""
    DISABLE: _AutoTranscode.ValueType  # 2
    """Disable auto transcoding."""

class AutoTranscode(_AutoTranscode, metaclass=_AutoTranscodeEnumTypeWrapper): ...

AUTO_TRANSCODE_UNSPECIFIED: AutoTranscode.ValueType  # 0
"""Unspecified auto transcoding value."""
ENABLE: AutoTranscode.ValueType  # 1
"""Enable auto transcoding."""
DISABLE: AutoTranscode.ValueType  # 2
"""Disable auto transcoding."""
global___AutoTranscode = AutoTranscode

@typing.final
class Video(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _VideoStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _VideoStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Video._VideoStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        VIDEO_STATUS_UNSPECIFIED: Video._VideoStatus.ValueType  # 0
        """Video status unspecified."""
        WAIT_UPLOADING: Video._VideoStatus.ValueType  # 1
        """Waiting for the whole number of bytes to be loaded."""
        PROCESSING: Video._VideoStatus.ValueType  # 4
        """Video processing."""
        READY: Video._VideoStatus.ValueType  # 5
        """Video is ready, processing is completed."""
        ERROR: Video._VideoStatus.ValueType  # 7
        """An error occurred during video processing."""

    class VideoStatus(_VideoStatus, metaclass=_VideoStatusEnumTypeWrapper): ...
    VIDEO_STATUS_UNSPECIFIED: Video.VideoStatus.ValueType  # 0
    """Video status unspecified."""
    WAIT_UPLOADING: Video.VideoStatus.ValueType  # 1
    """Waiting for the whole number of bytes to be loaded."""
    PROCESSING: Video.VideoStatus.ValueType  # 4
    """Video processing."""
    READY: Video.VideoStatus.ValueType  # 5
    """Video is ready, processing is completed."""
    ERROR: Video.VideoStatus.ValueType  # 7
    """An error occurred during video processing."""

    class _VisibilityStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _VisibilityStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Video._VisibilityStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        VISIBILITY_STATUS_UNSPECIFIED: Video._VisibilityStatus.ValueType  # 0
        """Visibility status unspecified."""
        PUBLISHED: Video._VisibilityStatus.ValueType  # 1
        """Video is published and available for viewing."""
        UNPUBLISHED: Video._VisibilityStatus.ValueType  # 2
        """Video is unpublished, only admin can watch."""

    class VisibilityStatus(_VisibilityStatus, metaclass=_VisibilityStatusEnumTypeWrapper): ...
    VISIBILITY_STATUS_UNSPECIFIED: Video.VisibilityStatus.ValueType  # 0
    """Visibility status unspecified."""
    PUBLISHED: Video.VisibilityStatus.ValueType  # 1
    """Video is published and available for viewing."""
    UNPUBLISHED: Video.VisibilityStatus.ValueType  # 2
    """Video is unpublished, only admin can watch."""

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
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    VISIBILITY_STATUS_FIELD_NUMBER: builtins.int
    AUTO_TRANSCODE_FIELD_NUMBER: builtins.int
    SUBTITLE_IDS_FIELD_NUMBER: builtins.int
    TUSD_FIELD_NUMBER: builtins.int
    PUBLIC_ACCESS_FIELD_NUMBER: builtins.int
    AUTH_SYSTEM_ACCESS_FIELD_NUMBER: builtins.int
    SIGN_URL_ACCESS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the video."""
    channel_id: builtins.str
    """ID of the channel where the video was created."""
    title: builtins.str
    """Video title."""
    description: builtins.str
    """Video description."""
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    status: global___Video.VideoStatus.ValueType
    """Video status."""
    visibility_status: global___Video.VisibilityStatus.ValueType
    """Video visibility status."""
    auto_transcode: global___AutoTranscode.ValueType
    """Auto start transcoding.
    If set to ENABLE, transcoding process is initiated automatically after video upload.
    If set to DISABLE, manual "Transcode()" call is required instead.
    """
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration:
        """Video duration. Optional, may be empty until the transcoding result is ready."""

    @property
    def subtitle_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """IDs of active video subtitles."""

    @property
    def tusd(self) -> global___VideoTUSDSource:
        """Upload video using the tus protocol."""

    @property
    def public_access(self) -> global___VideoPublicAccessRights:
        """Video is available to everyone."""

    @property
    def auth_system_access(self) -> global___VideoAuthSystemAccessRights:
        """Checking access rights using the authorization system."""

    @property
    def sign_url_access(self) -> global___VideoSignURLAccessRights:
        """Checking access rights using url's signature."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when video was created."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of last video update."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels as `` key:value `` pairs. Maximum 64 per resource."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        channel_id: builtins.str = ...,
        title: builtins.str = ...,
        description: builtins.str = ...,
        thumbnail_id: builtins.str = ...,
        status: global___Video.VideoStatus.ValueType = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
        visibility_status: global___Video.VisibilityStatus.ValueType = ...,
        auto_transcode: global___AutoTranscode.ValueType = ...,
        subtitle_ids: collections.abc.Iterable[builtins.str] | None = ...,
        tusd: global___VideoTUSDSource | None = ...,
        public_access: global___VideoPublicAccessRights | None = ...,
        auth_system_access: global___VideoAuthSystemAccessRights | None = ...,
        sign_url_access: global___VideoSignURLAccessRights | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["access_rights", b"access_rights", "auth_system_access", b"auth_system_access", "created_at", b"created_at", "duration", b"duration", "public_access", b"public_access", "sign_url_access", b"sign_url_access", "source", b"source", "tusd", b"tusd", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["access_rights", b"access_rights", "auth_system_access", b"auth_system_access", "auto_transcode", b"auto_transcode", "channel_id", b"channel_id", "created_at", b"created_at", "description", b"description", "duration", b"duration", "id", b"id", "labels", b"labels", "public_access", b"public_access", "sign_url_access", b"sign_url_access", "source", b"source", "status", b"status", "subtitle_ids", b"subtitle_ids", "thumbnail_id", b"thumbnail_id", "title", b"title", "tusd", b"tusd", "updated_at", b"updated_at", "visibility_status", b"visibility_status"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["access_rights", b"access_rights"]) -> typing.Literal["public_access", "auth_system_access", "sign_url_access"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["source", b"source"]) -> typing.Literal["tusd"] | None: ...

global___Video = Video

@typing.final
class VideoTUSDSource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    url: builtins.str
    """URL for uploading video via the tus protocol."""
    def __init__(
        self,
        *,
        url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["url", b"url"]) -> None: ...

global___VideoTUSDSource = VideoTUSDSource

@typing.final
class VideoPublicAccessRights(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___VideoPublicAccessRights = VideoPublicAccessRights

@typing.final
class VideoAuthSystemAccessRights(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___VideoAuthSystemAccessRights = VideoAuthSystemAccessRights

@typing.final
class VideoSignURLAccessRights(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___VideoSignURLAccessRights = VideoSignURLAccessRights
