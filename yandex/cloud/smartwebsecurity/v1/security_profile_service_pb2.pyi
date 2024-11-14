"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.smartwebsecurity.v1.security_profile_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetSecurityProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECURITY_PROFILE_ID_FIELD_NUMBER: builtins.int
    security_profile_id: builtins.str
    """ID of the SecurityProfile resource to return."""
    def __init__(
        self,
        *,
        security_profile_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["security_profile_id", b"security_profile_id"]) -> None: ...

global___GetSecurityProfileRequest = GetSecurityProfileRequest

@typing.final
class ListSecurityProfilesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder that the security profile belongs to.
    Currently page_size, page_token, filter and order_by are not supported and List method will return all security profiles in the folder.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id"]) -> None: ...

global___ListSecurityProfilesRequest = ListSecurityProfilesRequest

@typing.final
class ListSecurityProfilesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECURITY_PROFILES_FIELD_NUMBER: builtins.int
    @property
    def security_profiles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityProfile]:
        """List of SecurityProfile resources.
        Currently next_page_token is not supported and List method will return all security profiles in the folder.
        """

    def __init__(
        self,
        *,
        security_profiles: collections.abc.Iterable[yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityProfile] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["security_profiles", b"security_profiles"]) -> None: ...

global___ListSecurityProfilesResponse = ListSecurityProfilesResponse

@typing.final
class CreateSecurityProfileRequest(google.protobuf.message.Message):
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

    FOLDER_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DEFAULT_ACTION_FIELD_NUMBER: builtins.int
    SECURITY_RULES_FIELD_NUMBER: builtins.int
    CAPTCHA_ID_FIELD_NUMBER: builtins.int
    ADVANCED_RATE_LIMITER_PROFILE_ID_FIELD_NUMBER: builtins.int
    ANALYZE_REQUEST_BODY_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a security profile in."""
    name: builtins.str
    """Name of the security profile. The name is unique within the folder. 1-50 characters long."""
    description: builtins.str
    """Optional description of the security profile."""
    default_action: yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityProfile.DefaultAction.ValueType
    """Action to perform if none of rules matched."""
    captcha_id: builtins.str
    """Captcha ID to use with this security profile. Set empty to use default."""
    advanced_rate_limiter_profile_id: builtins.str
    """Advanced rate limiter profile ID to use with this security profile. Set empty to use default."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels as `` key:value `` pairs. Maximum of 64 per resource."""

    @property
    def security_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityRule]:
        """List of security rules."""

    @property
    def analyze_request_body(self) -> yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityProfile.AnalyzeRequestBody:
        """Parameters for request body analyzer."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        default_action: yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityProfile.DefaultAction.ValueType = ...,
        security_rules: collections.abc.Iterable[yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityRule] | None = ...,
        captcha_id: builtins.str = ...,
        advanced_rate_limiter_profile_id: builtins.str = ...,
        analyze_request_body: yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityProfile.AnalyzeRequestBody | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["analyze_request_body", b"analyze_request_body"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["advanced_rate_limiter_profile_id", b"advanced_rate_limiter_profile_id", "analyze_request_body", b"analyze_request_body", "captcha_id", b"captcha_id", "default_action", b"default_action", "description", b"description", "folder_id", b"folder_id", "labels", b"labels", "name", b"name", "security_rules", b"security_rules"]) -> None: ...

global___CreateSecurityProfileRequest = CreateSecurityProfileRequest

@typing.final
class CreateSecurityProfileMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECURITY_PROFILE_ID_FIELD_NUMBER: builtins.int
    security_profile_id: builtins.str
    """ID of the security profile that is being created."""
    def __init__(
        self,
        *,
        security_profile_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["security_profile_id", b"security_profile_id"]) -> None: ...

global___CreateSecurityProfileMetadata = CreateSecurityProfileMetadata

@typing.final
class UpdateSecurityProfileRequest(google.protobuf.message.Message):
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

    SECURITY_PROFILE_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DEFAULT_ACTION_FIELD_NUMBER: builtins.int
    SECURITY_RULES_FIELD_NUMBER: builtins.int
    CAPTCHA_ID_FIELD_NUMBER: builtins.int
    ADVANCED_RATE_LIMITER_PROFILE_ID_FIELD_NUMBER: builtins.int
    ANALYZE_REQUEST_BODY_FIELD_NUMBER: builtins.int
    security_profile_id: builtins.str
    """ID of the security profile to update."""
    name: builtins.str
    """Name of the security profile. The name is unique within the folder. 1-50 characters long."""
    description: builtins.str
    """Optional description of the security profile."""
    default_action: yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityProfile.DefaultAction.ValueType
    """Action to perform if none of rules matched."""
    captcha_id: builtins.str
    """Captcha ID to use with this security profile. Set empty to use default."""
    advanced_rate_limiter_profile_id: builtins.str
    """Advanced rate limiter profile ID to use with this security profile. Set empty to use default."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the SecurityProfile resource are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels as `` key:value `` pairs. Maximum of 64 per resource."""

    @property
    def security_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityRule]:
        """List of security rules."""

    @property
    def analyze_request_body(self) -> yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityProfile.AnalyzeRequestBody:
        """Parameters for request body analyzer."""

    def __init__(
        self,
        *,
        security_profile_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        default_action: yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityProfile.DefaultAction.ValueType = ...,
        security_rules: collections.abc.Iterable[yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityRule] | None = ...,
        captcha_id: builtins.str = ...,
        advanced_rate_limiter_profile_id: builtins.str = ...,
        analyze_request_body: yandex.cloud.smartwebsecurity.v1.security_profile_pb2.SecurityProfile.AnalyzeRequestBody | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["analyze_request_body", b"analyze_request_body", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["advanced_rate_limiter_profile_id", b"advanced_rate_limiter_profile_id", "analyze_request_body", b"analyze_request_body", "captcha_id", b"captcha_id", "default_action", b"default_action", "description", b"description", "labels", b"labels", "name", b"name", "security_profile_id", b"security_profile_id", "security_rules", b"security_rules", "update_mask", b"update_mask"]) -> None: ...

global___UpdateSecurityProfileRequest = UpdateSecurityProfileRequest

@typing.final
class UpdateSecurityProfileMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECURITY_PROFILE_ID_FIELD_NUMBER: builtins.int
    security_profile_id: builtins.str
    """ID of the SecurityProfile resource that is being updated."""
    def __init__(
        self,
        *,
        security_profile_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["security_profile_id", b"security_profile_id"]) -> None: ...

global___UpdateSecurityProfileMetadata = UpdateSecurityProfileMetadata

@typing.final
class DeleteSecurityProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECURITY_PROFILE_ID_FIELD_NUMBER: builtins.int
    security_profile_id: builtins.str
    """ID of the security profile to delete."""
    def __init__(
        self,
        *,
        security_profile_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["security_profile_id", b"security_profile_id"]) -> None: ...

global___DeleteSecurityProfileRequest = DeleteSecurityProfileRequest

@typing.final
class DeleteSecurityProfileMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECURITY_PROFILE_ID_FIELD_NUMBER: builtins.int
    security_profile_id: builtins.str
    """ID of the SecurityProfile resource that is being deleted."""
    def __init__(
        self,
        *,
        security_profile_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["security_profile_id", b"security_profile_id"]) -> None: ...

global___DeleteSecurityProfileMetadata = DeleteSecurityProfileMetadata
