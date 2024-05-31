"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.message
import typing
import yandex.cloud.containerregistry.v1.scan_policy_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetScanPolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCAN_POLICY_ID_FIELD_NUMBER: builtins.int
    scan_policy_id: builtins.str
    """ID of the scan policy."""
    def __init__(
        self,
        *,
        scan_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["scan_policy_id", b"scan_policy_id"]) -> None: ...

global___GetScanPolicyRequest = GetScanPolicyRequest

@typing.final
class GetScanPolicyByRegistryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the registry with scan policy."""
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["registry_id", b"registry_id"]) -> None: ...

global___GetScanPolicyByRegistryRequest = GetScanPolicyByRegistryRequest

@typing.final
class CreateScanPolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RULES_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the scan policy registry."""
    name: builtins.str
    """Name of the scan policy."""
    description: builtins.str
    """Description of the scan policy."""
    @property
    def rules(self) -> yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanRules:
        """Rules of the scan policy."""

    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        rules: yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanRules | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["rules", b"rules"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "name", b"name", "registry_id", b"registry_id", "rules", b"rules"]) -> None: ...

global___CreateScanPolicyRequest = CreateScanPolicyRequest

@typing.final
class UpdateScanPolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCAN_POLICY_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RULES_FIELD_NUMBER: builtins.int
    scan_policy_id: builtins.str
    """ID of the scan policy."""
    name: builtins.str
    """Name of the scan policy."""
    description: builtins.str
    """Description of the scan policy."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the scan policy resource are going to be updated."""

    @property
    def rules(self) -> yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanRules:
        """Rules of the scan policy."""

    def __init__(
        self,
        *,
        scan_policy_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        rules: yandex.cloud.containerregistry.v1.scan_policy_pb2.ScanRules | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["rules", b"rules", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "name", b"name", "rules", b"rules", "scan_policy_id", b"scan_policy_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateScanPolicyRequest = UpdateScanPolicyRequest

@typing.final
class DeleteScanPolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCAN_POLICY_ID_FIELD_NUMBER: builtins.int
    scan_policy_id: builtins.str
    """ID of the scan policy."""
    def __init__(
        self,
        *,
        scan_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["scan_policy_id", b"scan_policy_id"]) -> None: ...

global___DeleteScanPolicyRequest = DeleteScanPolicyRequest

@typing.final
class CreateScanPolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCAN_POLICY_ID_FIELD_NUMBER: builtins.int
    scan_policy_id: builtins.str
    """ID of created scan policy resource."""
    def __init__(
        self,
        *,
        scan_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["scan_policy_id", b"scan_policy_id"]) -> None: ...

global___CreateScanPolicyMetadata = CreateScanPolicyMetadata

@typing.final
class UpdateScanPolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCAN_POLICY_ID_FIELD_NUMBER: builtins.int
    scan_policy_id: builtins.str
    """ID of the scan policy resource that is updated."""
    def __init__(
        self,
        *,
        scan_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["scan_policy_id", b"scan_policy_id"]) -> None: ...

global___UpdateScanPolicyMetadata = UpdateScanPolicyMetadata

@typing.final
class DeleteScanPolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCAN_POLICY_ID_FIELD_NUMBER: builtins.int
    scan_policy_id: builtins.str
    """ID of the scan policy resource that is deleted."""
    def __init__(
        self,
        *,
        scan_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["scan_policy_id", b"scan_policy_id"]) -> None: ...

global___DeleteScanPolicyMetadata = DeleteScanPolicyMetadata