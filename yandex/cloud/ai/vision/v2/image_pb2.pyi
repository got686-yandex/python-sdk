"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Image(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ImageType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ImageTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Image._ImageType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        IMAGE_TYPE_UNSPECIFIED: Image._ImageType.ValueType  # 0
        JPEG: Image._ImageType.ValueType  # 1
        PNG: Image._ImageType.ValueType  # 2

    class ImageType(_ImageType, metaclass=_ImageTypeEnumTypeWrapper):
        """   type of image"""

    IMAGE_TYPE_UNSPECIFIED: Image.ImageType.ValueType  # 0
    JPEG: Image.ImageType.ValueType  # 1
    PNG: Image.ImageType.ValueType  # 2

    CONTENT_FIELD_NUMBER: builtins.int
    IMAGE_TYPE_FIELD_NUMBER: builtins.int
    content: builtins.bytes
    """       bytes with data"""
    image_type: global___Image.ImageType.ValueType
    """   type of data"""
    def __init__(
        self,
        *,
        content: builtins.bytes = ...,
        image_type: global___Image.ImageType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ImageSource", b"ImageSource", "content", b"content"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ImageSource", b"ImageSource", "content", b"content", "image_type", b"image_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["ImageSource", b"ImageSource"]) -> typing.Literal["content"] | None: ...

global___Image = Image