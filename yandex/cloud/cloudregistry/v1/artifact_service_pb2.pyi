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
class GetArtifactRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARTIFACT_ID_FIELD_NUMBER: builtins.int
    artifact_id: builtins.str
    """ID of the artifact resource to return."""
    def __init__(
        self,
        *,
        artifact_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["artifact_id", b"artifact_id"]) -> None: ...

global___GetArtifactRequest = GetArtifactRequest

@typing.final
class DeleteArtifactRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARTIFACT_ID_FIELD_NUMBER: builtins.int
    artifact_id: builtins.str
    """ID of the artifact to delete."""
    def __init__(
        self,
        *,
        artifact_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["artifact_id", b"artifact_id"]) -> None: ...

global___DeleteArtifactRequest = DeleteArtifactRequest

@typing.final
class DeleteArtifactMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARTIFACT_ID_FIELD_NUMBER: builtins.int
    artifact_id: builtins.str
    """ID of the artifact to delete."""
    def __init__(
        self,
        *,
        artifact_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["artifact_id", b"artifact_id"]) -> None: ...

global___DeleteArtifactMetadata = DeleteArtifactMetadata