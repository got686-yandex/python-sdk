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
import sys
import typing
import yandex.cloud.video.v1.thumbnail_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetThumbnailRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    def __init__(
        self,
        *,
        thumbnail_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["thumbnail_id", b"thumbnail_id"]) -> None: ...

global___GetThumbnailRequest = GetThumbnailRequest

@typing.final
class ListThumbnailRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel."""
    page_size: builtins.int
    """The maximum number of the results per page to return.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token for getting the next page of the result."""
    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListThumbnailRequest = ListThumbnailRequest

@typing.final
class ListThumbnailResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    THUMBNAILS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page."""
    @property
    def thumbnails(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.video.v1.thumbnail_pb2.Thumbnail]:
        """List of thumbnails."""

    def __init__(
        self,
        *,
        thumbnails: collections.abc.Iterable[yandex.cloud.video.v1.thumbnail_pb2.Thumbnail] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "thumbnails", b"thumbnails"]) -> None: ...

global___ListThumbnailResponse = ListThumbnailResponse

@typing.final
class CreateThumbnailRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel."""
    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id"]) -> None: ...

global___CreateThumbnailRequest = CreateThumbnailRequest

@typing.final
class CreateThumbnailMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    def __init__(
        self,
        *,
        thumbnail_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["thumbnail_id", b"thumbnail_id"]) -> None: ...

global___CreateThumbnailMetadata = CreateThumbnailMetadata

@typing.final
class BatchGenerateDownloadURLsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHANNEL_ID_FIELD_NUMBER: builtins.int
    THUMBNAIL_IDS_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """ID of the channel."""
    @property
    def thumbnail_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of thumbnails IDs."""

    def __init__(
        self,
        *,
        channel_id: builtins.str = ...,
        thumbnail_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id", "thumbnail_ids", b"thumbnail_ids"]) -> None: ...

global___BatchGenerateDownloadURLsRequest = BatchGenerateDownloadURLsRequest

@typing.final
class BatchGenerateDownloadURLsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOWNLOAD_URLS_FIELD_NUMBER: builtins.int
    @property
    def download_urls(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ThumbnailDownloadURL]:
        """List of download urls."""

    def __init__(
        self,
        *,
        download_urls: collections.abc.Iterable[global___ThumbnailDownloadURL] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["download_urls", b"download_urls"]) -> None: ...

global___BatchGenerateDownloadURLsResponse = BatchGenerateDownloadURLsResponse

@typing.final
class ThumbnailDownloadURL(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ImageFormat:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ImageFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ThumbnailDownloadURL._ImageFormat.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        IMAGE_FORMAT_UNSPECIFIED: ThumbnailDownloadURL._ImageFormat.ValueType  # 0
        """Image format unspecified."""
        JPEG: ThumbnailDownloadURL._ImageFormat.ValueType  # 1
        """JPEG image format."""
        WEBP: ThumbnailDownloadURL._ImageFormat.ValueType  # 2
        """WebP image format."""

    class ImageFormat(_ImageFormat, metaclass=_ImageFormatEnumTypeWrapper): ...
    IMAGE_FORMAT_UNSPECIFIED: ThumbnailDownloadURL.ImageFormat.ValueType  # 0
    """Image format unspecified."""
    JPEG: ThumbnailDownloadURL.ImageFormat.ValueType  # 1
    """JPEG image format."""
    WEBP: ThumbnailDownloadURL.ImageFormat.ValueType  # 2
    """WebP image format."""

    @typing.final
    class ScaledURL(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        URL_FIELD_NUMBER: builtins.int
        MAX_WIDTH_FIELD_NUMBER: builtins.int
        MAX_HEIGHT_FIELD_NUMBER: builtins.int
        IMAGE_FORMAT_FIELD_NUMBER: builtins.int
        url: builtins.str
        """Download url."""
        max_width: builtins.int
        """Maximum width of the rectangle to inscribe the thumbnail into."""
        max_height: builtins.int
        """Maximum height of the rectangle to inscribe the thumbnail into."""
        image_format: global___ThumbnailDownloadURL.ImageFormat.ValueType
        """Image format."""
        def __init__(
            self,
            *,
            url: builtins.str = ...,
            max_width: builtins.int = ...,
            max_height: builtins.int = ...,
            image_format: global___ThumbnailDownloadURL.ImageFormat.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["image_format", b"image_format", "max_height", b"max_height", "max_width", b"max_width", "url", b"url"]) -> None: ...

    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    ORIGINAL_URL_FIELD_NUMBER: builtins.int
    SCALED_URLS_FIELD_NUMBER: builtins.int
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    original_url: builtins.str
    """Original download url."""
    @property
    def scaled_urls(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ThumbnailDownloadURL.ScaledURL]:
        """List of download urls, one per each available image size."""

    def __init__(
        self,
        *,
        thumbnail_id: builtins.str = ...,
        original_url: builtins.str = ...,
        scaled_urls: collections.abc.Iterable[global___ThumbnailDownloadURL.ScaledURL] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["original_url", b"original_url", "scaled_urls", b"scaled_urls", "thumbnail_id", b"thumbnail_id"]) -> None: ...

global___ThumbnailDownloadURL = ThumbnailDownloadURL

@typing.final
class GenerateThumbnailUploadURLRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    def __init__(
        self,
        *,
        thumbnail_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["thumbnail_id", b"thumbnail_id"]) -> None: ...

global___GenerateThumbnailUploadURLRequest = GenerateThumbnailUploadURLRequest

@typing.final
class GenerateThumbnailUploadURLResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPLOAD_URL_FIELD_NUMBER: builtins.int
    upload_url: builtins.str
    """Upload url."""
    def __init__(
        self,
        *,
        upload_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["upload_url", b"upload_url"]) -> None: ...

global___GenerateThumbnailUploadURLResponse = GenerateThumbnailUploadURLResponse

@typing.final
class DeleteThumbnailRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    def __init__(
        self,
        *,
        thumbnail_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["thumbnail_id", b"thumbnail_id"]) -> None: ...

global___DeleteThumbnailRequest = DeleteThumbnailRequest

@typing.final
class DeleteThumbnailMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    THUMBNAIL_ID_FIELD_NUMBER: builtins.int
    thumbnail_id: builtins.str
    """ID of the thumbnail."""
    def __init__(
        self,
        *,
        thumbnail_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["thumbnail_id", b"thumbnail_id"]) -> None: ...

global___DeleteThumbnailMetadata = DeleteThumbnailMetadata
