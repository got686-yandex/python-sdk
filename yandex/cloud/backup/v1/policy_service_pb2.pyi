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
import yandex.cloud.backup.v1.policy_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListPoliciesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    COMPUTE_INSTANCE_ID_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Folder ID. Either Folder ID or Compute Cloud instance ID should be set."""
    compute_instance_id: builtins.str
    """Compute Cloud instance ID. Either Folder ID or Compute Cloud instance ID should be set."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        compute_instance_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["compute_instance_id", b"compute_instance_id", "folder_id", b"folder_id"]) -> None: ...

global___ListPoliciesRequest = ListPoliciesRequest

@typing.final
class ListPoliciesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICIES_FIELD_NUMBER: builtins.int
    @property
    def policies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.backup.v1.policy_pb2.Policy]: ...
    def __init__(
        self,
        *,
        policies: collections.abc.Iterable[yandex.cloud.backup.v1.policy_pb2.Policy] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["policies", b"policies"]) -> None: ...

global___ListPoliciesResponse = ListPoliciesResponse

@typing.final
class CreatePolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Folder ID."""
    name: builtins.str
    """Policy name."""
    @property
    def settings(self) -> yandex.cloud.backup.v1.policy_pb2.PolicySettings: ...
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        settings: yandex.cloud.backup.v1.policy_pb2.PolicySettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "name", b"name", "settings", b"settings"]) -> None: ...

global___CreatePolicyRequest = CreatePolicyRequest

@typing.final
class CreatePolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["policy_id", b"policy_id"]) -> None: ...

global___CreatePolicyMetadata = CreatePolicyMetadata

@typing.final
class GetPolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["policy_id", b"policy_id"]) -> None: ...

global___GetPolicyRequest = GetPolicyRequest

@typing.final
class UpdatePolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    @property
    def settings(self) -> yandex.cloud.backup.v1.policy_pb2.PolicySettings: ...
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
        settings: yandex.cloud.backup.v1.policy_pb2.PolicySettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["policy_id", b"policy_id", "settings", b"settings"]) -> None: ...

global___UpdatePolicyRequest = UpdatePolicyRequest

@typing.final
class UpdatePolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["policy_id", b"policy_id"]) -> None: ...

global___UpdatePolicyMetadata = UpdatePolicyMetadata

@typing.final
class DeletePolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["policy_id", b"policy_id"]) -> None: ...

global___DeletePolicyRequest = DeletePolicyRequest

@typing.final
class DeletePolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["policy_id", b"policy_id"]) -> None: ...

global___DeletePolicyMetadata = DeletePolicyMetadata

@typing.final
class ApplyPolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    COMPUTE_INSTANCE_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    compute_instance_id: builtins.str
    """Compute Cloud instance ID."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
        compute_instance_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["compute_instance_id", b"compute_instance_id", "policy_id", b"policy_id"]) -> None: ...

global___ApplyPolicyRequest = ApplyPolicyRequest

@typing.final
class ApplyPolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    COMPUTE_INSTANCE_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    compute_instance_id: builtins.str
    """Compute Cloud instance ID."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
        compute_instance_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["compute_instance_id", b"compute_instance_id", "policy_id", b"policy_id"]) -> None: ...

global___ApplyPolicyMetadata = ApplyPolicyMetadata

@typing.final
class ListApplicationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    POLICY_ID_FIELD_NUMBER: builtins.int
    COMPUTE_INSTANCE_ID_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Folder ID."""
    policy_id: builtins.str
    """Policy ID."""
    compute_instance_id: builtins.str
    """Compute Cloud instance ID."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        policy_id: builtins.str = ...,
        compute_instance_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["compute_instance_id", b"compute_instance_id", "folder_id", b"folder_id", "id", b"id", "policy_id", b"policy_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["compute_instance_id", b"compute_instance_id", "folder_id", b"folder_id", "id", b"id", "policy_id", b"policy_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["id", b"id"]) -> typing.Literal["folder_id", "policy_id", "compute_instance_id"] | None: ...

global___ListApplicationsRequest = ListApplicationsRequest

@typing.final
class ListApplicationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    APPLICATIONS_FIELD_NUMBER: builtins.int
    @property
    def applications(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.backup.v1.policy_pb2.PolicyApplication]: ...
    def __init__(
        self,
        *,
        applications: collections.abc.Iterable[yandex.cloud.backup.v1.policy_pb2.PolicyApplication] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["applications", b"applications"]) -> None: ...

global___ListApplicationsResponse = ListApplicationsResponse

@typing.final
class ExecuteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    COMPUTE_INSTANCE_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    compute_instance_id: builtins.str
    """Compute Cloud instance ID."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
        compute_instance_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["compute_instance_id", b"compute_instance_id", "policy_id", b"policy_id"]) -> None: ...

global___ExecuteRequest = ExecuteRequest

@typing.final
class ExecuteMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    COMPUTE_INSTANCE_ID_FIELD_NUMBER: builtins.int
    PROGRESS_PERCENTAGE_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    compute_instance_id: builtins.str
    """Compute Cloud instance ID."""
    progress_percentage: builtins.float
    """Progress of the backup process."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
        compute_instance_id: builtins.str = ...,
        progress_percentage: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["compute_instance_id", b"compute_instance_id", "policy_id", b"policy_id", "progress_percentage", b"progress_percentage"]) -> None: ...

global___ExecuteMetadata = ExecuteMetadata

@typing.final
class RevokeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    COMPUTE_INSTANCE_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    compute_instance_id: builtins.str
    """Compute Cloud instance ID."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
        compute_instance_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["compute_instance_id", b"compute_instance_id", "policy_id", b"policy_id"]) -> None: ...

global___RevokeRequest = RevokeRequest

@typing.final
class RevokeMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    COMPUTE_INSTANCE_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Policy ID."""
    compute_instance_id: builtins.str
    """Compute Cloud instance ID."""
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
        compute_instance_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["compute_instance_id", b"compute_instance_id", "policy_id", b"policy_id"]) -> None: ...

global___RevokeMetadata = RevokeMetadata