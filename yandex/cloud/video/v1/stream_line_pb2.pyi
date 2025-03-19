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
class StreamLine(google.protobuf.message.Message):
    """Entity that is responsible for the incoming video signal settings."""

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
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    RTMP_PUSH_FIELD_NUMBER: builtins.int
    RTMP_PULL_FIELD_NUMBER: builtins.int
    MANUAL_LINE_FIELD_NUMBER: builtins.int
    AUTO_LINE_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the line."""
    channel_id: builtins.str
    """ID of the channel to which this stream line belongs."""
    title: builtins.str
    """Title of the stream line."""
    thumbnail_id: builtins.str
    """ID of the thumbnail image associated with the stream line.."""
    @property
    def rtmp_push(self) -> global___RTMPPushInput:
        """Real-Time Messaging Protocol (RTMP) push input settings."""

    @property
    def rtmp_pull(self) -> global___RTMPPullInput:
        """Real-Time Messaging Protocol (RTMP) pull input type."""

    @property
    def manual_line(self) -> global___ManualLine:
        """Manual control of stream."""

    @property
    def auto_line(self) -> global___AutoLine:
        """Automatic control of stream."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the stream line was created."""

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the stream line was last updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels as `` key:value `` pairs. Maximum 64 per resource."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        channel_id: builtins.str = ...,
        title: builtins.str = ...,
        thumbnail_id: builtins.str = ...,
        rtmp_push: global___RTMPPushInput | None = ...,
        rtmp_pull: global___RTMPPullInput | None = ...,
        manual_line: global___ManualLine | None = ...,
        auto_line: global___AutoLine | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        updated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["auto_line", b"auto_line", "created_at", b"created_at", "input_type", b"input_type", "line_type", b"line_type", "manual_line", b"manual_line", "rtmp_pull", b"rtmp_pull", "rtmp_push", b"rtmp_push", "updated_at", b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auto_line", b"auto_line", "channel_id", b"channel_id", "created_at", b"created_at", "id", b"id", "input_type", b"input_type", "labels", b"labels", "line_type", b"line_type", "manual_line", b"manual_line", "rtmp_pull", b"rtmp_pull", "rtmp_push", b"rtmp_push", "thumbnail_id", b"thumbnail_id", "title", b"title", "updated_at", b"updated_at"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["input_type", b"input_type"]) -> typing.Literal["rtmp_push", "rtmp_pull"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["line_type", b"line_type"]) -> typing.Literal["manual_line", "auto_line"] | None: ...

global___StreamLine = StreamLine

@typing.final
class PushStreamKey(google.protobuf.message.Message):
    """Represents the stream key used for pushing video streams."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    key: builtins.str
    """The unique stream key."""
    def __init__(
        self,
        *,
        key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key", b"key"]) -> None: ...

global___PushStreamKey = PushStreamKey

@typing.final
class RTMPPushInput(google.protobuf.message.Message):
    """Settings for an RTMP (Real-Time Messaging Protocol) push input.
    Used when the video stream is pushed to an RTMP server.
    @see https://en.wikipedia.org/wiki/Real-Time_Messaging_Protocol
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    url: builtins.str
    """RTMP server url."""
    def __init__(
        self,
        *,
        url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["url", b"url"]) -> None: ...

global___RTMPPushInput = RTMPPushInput

@typing.final
class RTMPPullInput(google.protobuf.message.Message):
    """Settings for an RTMP pull input.
    Used when the service pulls the video stream from an RTMP source.
    @see https://en.wikipedia.org/wiki/Real-Time_Messaging_Protocol
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    url: builtins.str
    """RTMP url for receiving video signal."""
    def __init__(
        self,
        *,
        url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["url", b"url"]) -> None: ...

global___RTMPPullInput = RTMPPullInput

@typing.final
class ManualLine(google.protobuf.message.Message):
    """Represents a manual line type where the stream control is handled manually.
    This means that stream start/stop actions are performed by the user.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ManualLine = ManualLine

@typing.final
class AutoLine(google.protobuf.message.Message):
    """Represents an automatic line type where the stream control is handled automatically."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _AutoLineStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _AutoLineStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AutoLine._AutoLineStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        AUTO_LINE_STATUS_UNSPECIFIED: AutoLine._AutoLineStatus.ValueType  # 0
        """Auto line status unspecified."""
        DEACTIVATED: AutoLine._AutoLineStatus.ValueType  # 1
        """The automatic line is deactivated and not currently active."""
        ACTIVE: AutoLine._AutoLineStatus.ValueType  # 2
        """The automatic line is active and operational."""

    class AutoLineStatus(_AutoLineStatus, metaclass=_AutoLineStatusEnumTypeWrapper):
        """Enum representing the status of an automatic stream line.
        Indicates whether the automatic line is active or deactivated.
        """

    AUTO_LINE_STATUS_UNSPECIFIED: AutoLine.AutoLineStatus.ValueType  # 0
    """Auto line status unspecified."""
    DEACTIVATED: AutoLine.AutoLineStatus.ValueType  # 1
    """The automatic line is deactivated and not currently active."""
    ACTIVE: AutoLine.AutoLineStatus.ValueType  # 2
    """The automatic line is active and operational."""

    STATUS_FIELD_NUMBER: builtins.int
    status: global___AutoLine.AutoLineStatus.ValueType
    """The status of the automatic line."""
    def __init__(
        self,
        *,
        status: global___AutoLine.AutoLineStatus.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["status", b"status"]) -> None: ...

global___AutoLine = AutoLine
