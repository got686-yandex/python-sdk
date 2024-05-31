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
class AuthSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SAML_FIELD_NUMBER: builtins.int
    @property
    def saml(self) -> global___SAMLSettings:
        """SAML settings"""

    def __init__(
        self,
        *,
        saml: global___SAMLSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["saml", b"saml"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["saml", b"saml"]) -> None: ...

global___AuthSettings = AuthSettings

@typing.final
class SAMLSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLED_FIELD_NUMBER: builtins.int
    IDP_ENTITY_ID_FIELD_NUMBER: builtins.int
    IDP_METADATA_FILE_FIELD_NUMBER: builtins.int
    SP_ENTITY_ID_FIELD_NUMBER: builtins.int
    DASHBOARDS_URL_FIELD_NUMBER: builtins.int
    ROLES_KEY_FIELD_NUMBER: builtins.int
    SUBJECT_KEY_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    idp_entity_id: builtins.str
    """Required. The entity ID of your IdP."""
    idp_metadata_file: builtins.bytes
    """Required. The SAML 2.0 metadata file of your IdP."""
    sp_entity_id: builtins.str
    """Required. The entity ID of the service provider."""
    dashboards_url: builtins.str
    """Required. The OpenSearch Dashboards base URL."""
    roles_key: builtins.str
    """Optional. The attribute in the SAML response where the roles are stored. If not configured, no roles are used."""
    subject_key: builtins.str
    """Optional. The attribute in the SAML response where the subject is stored. If not configured, the NameID attribute is used."""
    def __init__(
        self,
        *,
        enabled: builtins.bool = ...,
        idp_entity_id: builtins.str = ...,
        idp_metadata_file: builtins.bytes = ...,
        sp_entity_id: builtins.str = ...,
        dashboards_url: builtins.str = ...,
        roles_key: builtins.str = ...,
        subject_key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dashboards_url", b"dashboards_url", "enabled", b"enabled", "idp_entity_id", b"idp_entity_id", "idp_metadata_file", b"idp_metadata_file", "roles_key", b"roles_key", "sp_entity_id", b"sp_entity_id", "subject_key", b"subject_key"]) -> None: ...

global___SAMLSettings = SAMLSettings