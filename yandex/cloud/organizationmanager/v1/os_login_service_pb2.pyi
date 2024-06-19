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

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetOsLoginSettingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id"]) -> None: ...

global___GetOsLoginSettingsRequest = GetOsLoginSettingsRequest

@typing.final
class OsLoginSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_SSH_KEY_SETTINGS_FIELD_NUMBER: builtins.int
    SSH_CERTIFICATE_SETTINGS_FIELD_NUMBER: builtins.int
    @property
    def user_ssh_key_settings(self) -> global___UserSshKeySettings: ...
    @property
    def ssh_certificate_settings(self) -> global___SshCertificateSettings: ...
    def __init__(
        self,
        *,
        user_ssh_key_settings: global___UserSshKeySettings | None = ...,
        ssh_certificate_settings: global___SshCertificateSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ssh_certificate_settings", b"ssh_certificate_settings", "user_ssh_key_settings", b"user_ssh_key_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ssh_certificate_settings", b"ssh_certificate_settings", "user_ssh_key_settings", b"user_ssh_key_settings"]) -> None: ...

global___OsLoginSettings = OsLoginSettings

@typing.final
class UserSshKeySettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLED_FIELD_NUMBER: builtins.int
    ALLOW_MANAGE_OWN_KEYS_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    allow_manage_own_keys: builtins.bool
    def __init__(
        self,
        *,
        enabled: builtins.bool = ...,
        allow_manage_own_keys: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["allow_manage_own_keys", b"allow_manage_own_keys", "enabled", b"enabled"]) -> None: ...

global___UserSshKeySettings = UserSshKeySettings

@typing.final
class SshCertificateSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLED_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    def __init__(
        self,
        *,
        enabled: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["enabled", b"enabled"]) -> None: ...

global___SshCertificateSettings = SshCertificateSettings

@typing.final
class UpdateOsLoginSettingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class UserSshKeySettings(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ENABLED_FIELD_NUMBER: builtins.int
        ALLOW_MANAGE_OWN_KEYS_FIELD_NUMBER: builtins.int
        enabled: builtins.bool
        allow_manage_own_keys: builtins.bool
        def __init__(
            self,
            *,
            enabled: builtins.bool = ...,
            allow_manage_own_keys: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["allow_manage_own_keys", b"allow_manage_own_keys", "enabled", b"enabled"]) -> None: ...

    @typing.final
    class SshCertificateSettings(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ENABLED_FIELD_NUMBER: builtins.int
        enabled: builtins.bool
        def __init__(
            self,
            *,
            enabled: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["enabled", b"enabled"]) -> None: ...

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    USER_SSH_KEY_SETTINGS_FIELD_NUMBER: builtins.int
    SSH_CERTIFICATE_SETTINGS_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    @property
    def user_ssh_key_settings(self) -> global___UpdateOsLoginSettingsRequest.UserSshKeySettings: ...
    @property
    def ssh_certificate_settings(self) -> global___UpdateOsLoginSettingsRequest.SshCertificateSettings: ...
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        user_ssh_key_settings: global___UpdateOsLoginSettingsRequest.UserSshKeySettings | None = ...,
        ssh_certificate_settings: global___UpdateOsLoginSettingsRequest.SshCertificateSettings | None = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ssh_certificate_settings", b"ssh_certificate_settings", "update_mask", b"update_mask", "user_ssh_key_settings", b"user_ssh_key_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id", "ssh_certificate_settings", b"ssh_certificate_settings", "update_mask", b"update_mask", "user_ssh_key_settings", b"user_ssh_key_settings"]) -> None: ...

global___UpdateOsLoginSettingsRequest = UpdateOsLoginSettingsRequest

@typing.final
class SetDefaultOsLoginProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OS_LOGIN_PROFILE_ID_FIELD_NUMBER: builtins.int
    os_login_profile_id: builtins.str
    def __init__(
        self,
        *,
        os_login_profile_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["os_login_profile_id", b"os_login_profile_id"]) -> None: ...

global___SetDefaultOsLoginProfileRequest = SetDefaultOsLoginProfileRequest

@typing.final
class GetOsLoginProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OS_LOGIN_PROFILE_ID_FIELD_NUMBER: builtins.int
    os_login_profile_id: builtins.str
    def __init__(
        self,
        *,
        os_login_profile_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["os_login_profile_id", b"os_login_profile_id"]) -> None: ...

global___GetOsLoginProfileRequest = GetOsLoginProfileRequest

@typing.final
class ListOsLoginProfilesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    page_size: builtins.int
    page_token: builtins.str
    filter: builtins.str
    """A filter expression that filters profiles listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering by subject_id, uid or login.
    2. An `=` operator.
    3. The value in double quotes (`"`).
    E.g. login="example-login"
    """
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "organization_id", b"organization_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListOsLoginProfilesRequest = ListOsLoginProfilesRequest

@typing.final
class ListOsLoginProfilesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROFILES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    @property
    def profiles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OsLoginProfile]: ...
    def __init__(
        self,
        *,
        profiles: collections.abc.Iterable[global___OsLoginProfile] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "profiles", b"profiles"]) -> None: ...

global___ListOsLoginProfilesResponse = ListOsLoginProfilesResponse

@typing.final
class OsLoginProfile(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    LOGIN_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    IS_DEFAULT_FIELD_NUMBER: builtins.int
    HOME_DIRECTORY_FIELD_NUMBER: builtins.int
    SHELL_FIELD_NUMBER: builtins.int
    id: builtins.str
    organization_id: builtins.str
    subject_id: builtins.str
    login: builtins.str
    uid: builtins.int
    is_default: builtins.bool
    home_directory: builtins.str
    shell: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        organization_id: builtins.str = ...,
        subject_id: builtins.str = ...,
        login: builtins.str = ...,
        uid: builtins.int = ...,
        is_default: builtins.bool = ...,
        home_directory: builtins.str = ...,
        shell: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["home_directory", b"home_directory", "id", b"id", "is_default", b"is_default", "login", b"login", "organization_id", b"organization_id", "shell", b"shell", "subject_id", b"subject_id", "uid", b"uid"]) -> None: ...

global___OsLoginProfile = OsLoginProfile

@typing.final
class UpdateOsLoginProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OS_LOGIN_PROFILE_ID_FIELD_NUMBER: builtins.int
    LOGIN_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    HOME_DIRECTORY_FIELD_NUMBER: builtins.int
    SHELL_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    os_login_profile_id: builtins.str
    login: builtins.str
    """must not contain . or end in ~"""
    uid: builtins.int
    """1000 - 2^63 - 1"""
    home_directory: builtins.str
    shell: builtins.str
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    def __init__(
        self,
        *,
        os_login_profile_id: builtins.str = ...,
        login: builtins.str = ...,
        uid: builtins.int = ...,
        home_directory: builtins.str = ...,
        shell: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["home_directory", b"home_directory", "login", b"login", "os_login_profile_id", b"os_login_profile_id", "shell", b"shell", "uid", b"uid", "update_mask", b"update_mask"]) -> None: ...

global___UpdateOsLoginProfileRequest = UpdateOsLoginProfileRequest

@typing.final
class DeleteOsLoginProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___DeleteOsLoginProfileRequest = DeleteOsLoginProfileRequest

@typing.final
class CreateOsLoginProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    LOGIN_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    HOME_DIRECTORY_FIELD_NUMBER: builtins.int
    SHELL_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    subject_id: builtins.str
    login: builtins.str
    """must not contain . or end in ~"""
    uid: builtins.int
    """1000 - 2^63 - 1"""
    home_directory: builtins.str
    shell: builtins.str
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        subject_id: builtins.str = ...,
        login: builtins.str = ...,
        uid: builtins.int = ...,
        home_directory: builtins.str = ...,
        shell: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["home_directory", b"home_directory", "login", b"login", "organization_id", b"organization_id", "shell", b"shell", "subject_id", b"subject_id", "uid", b"uid"]) -> None: ...

global___CreateOsLoginProfileRequest = CreateOsLoginProfileRequest

@typing.final
class UpdateOsLoginProfileMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OS_LOGIN_PROFILE_ID_FIELD_NUMBER: builtins.int
    os_login_profile_id: builtins.str
    def __init__(
        self,
        *,
        os_login_profile_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["os_login_profile_id", b"os_login_profile_id"]) -> None: ...

global___UpdateOsLoginProfileMetadata = UpdateOsLoginProfileMetadata

@typing.final
class DeleteOsLoginProfileMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OS_LOGIN_PROFILE_ID_FIELD_NUMBER: builtins.int
    os_login_profile_id: builtins.str
    def __init__(
        self,
        *,
        os_login_profile_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["os_login_profile_id", b"os_login_profile_id"]) -> None: ...

global___DeleteOsLoginProfileMetadata = DeleteOsLoginProfileMetadata

@typing.final
class CreateOsLoginProfileMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OS_LOGIN_PROFILE_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    os_login_profile_id: builtins.str
    organization_id: builtins.str
    subject_id: builtins.str
    def __init__(
        self,
        *,
        os_login_profile_id: builtins.str = ...,
        organization_id: builtins.str = ...,
        subject_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id", "os_login_profile_id", b"os_login_profile_id", "subject_id", b"subject_id"]) -> None: ...

global___CreateOsLoginProfileMetadata = CreateOsLoginProfileMetadata

@typing.final
class UpdateOsLoginSettingsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id"]) -> None: ...

global___UpdateOsLoginSettingsMetadata = UpdateOsLoginSettingsMetadata

@typing.final
class SetDefaultOsLoginProfileMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREVIOUS_DEFAULT_PROFILE_ID_FIELD_NUMBER: builtins.int
    CURRENT_DEFAULT_PROFILE_ID_FIELD_NUMBER: builtins.int
    previous_default_profile_id: builtins.str
    current_default_profile_id: builtins.str
    def __init__(
        self,
        *,
        previous_default_profile_id: builtins.str = ...,
        current_default_profile_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["current_default_profile_id", b"current_default_profile_id", "previous_default_profile_id", b"previous_default_profile_id"]) -> None: ...

global___SetDefaultOsLoginProfileMetadata = SetDefaultOsLoginProfileMetadata
