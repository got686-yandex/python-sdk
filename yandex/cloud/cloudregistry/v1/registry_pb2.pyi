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
class Registry(google.protobuf.message.Message):
    """A Registry resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Registry._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: Registry._Status.ValueType  # 0
        CREATING: Registry._Status.ValueType  # 1
        """Registry is being created."""
        ACTIVE: Registry._Status.ValueType  # 2
        """Registry is ready to use."""
        DELETING: Registry._Status.ValueType  # 3
        """Registry is being deleted."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: Registry.Status.ValueType  # 0
    CREATING: Registry.Status.ValueType  # 1
    """Registry is being created."""
    ACTIVE: Registry.Status.ValueType  # 2
    """Registry is ready to use."""
    DELETING: Registry.Status.ValueType  # 3
    """Registry is being deleted."""

    class _Kind:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _KindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Registry._Kind.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        KIND_UNSPECIFIED: Registry._Kind.ValueType  # 0
        MAVEN: Registry._Kind.ValueType  # 1
        """Registry kind is maven."""
        NPM: Registry._Kind.ValueType  # 2
        """Registry kind is npm."""
        DOCKER: Registry._Kind.ValueType  # 3
        """Registry kind is docker."""

    class Kind(_Kind, metaclass=_KindEnumTypeWrapper): ...
    KIND_UNSPECIFIED: Registry.Kind.ValueType  # 0
    MAVEN: Registry.Kind.ValueType  # 1
    """Registry kind is maven."""
    NPM: Registry.Kind.ValueType  # 2
    """Registry kind is npm."""
    DOCKER: Registry.Kind.ValueType  # 3
    """Registry kind is docker."""

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Registry._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Registry._Type.ValueType  # 0
        LOCAL: Registry._Type.ValueType  # 1
        """Registry type is local."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    TYPE_UNSPECIFIED: Registry.Type.ValueType  # 0
    LOCAL: Registry.Type.ValueType  # 1
    """Registry type is local."""

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

    @typing.final
    class PropertiesEntry(google.protobuf.message.Message):
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
    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Output only. ID of the registry."""
    folder_id: builtins.str
    """ID of the folder that the registry belongs to."""
    name: builtins.str
    """Name of the registry."""
    kind: global___Registry.Kind.ValueType
    """Kind of the registry."""
    type: global___Registry.Type.ValueType
    """Type of the registry."""
    status: global___Registry.Status.ValueType
    """Output only. Status of the registry."""
    description: builtins.str
    """Description of the registry."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs. Maximum of 64 per resource."""

    @property
    def properties(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource properties as `key:value` pairs. Maximum of 64 per resource."""

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""

    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Modification timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        kind: global___Registry.Kind.ValueType = ...,
        type: global___Registry.Type.ValueType = ...,
        status: global___Registry.Status.ValueType = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        properties: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "modified_at", b"modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "kind", b"kind", "labels", b"labels", "modified_at", b"modified_at", "name", b"name", "properties", b"properties", "status", b"status", "type", b"type"]) -> None: ...

global___Registry = Registry