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
import google.protobuf.wrappers_pb2
import sys
import typing
import yandex.cloud.cic.v1.peering_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class PublicConnection(google.protobuf.message.Message):
    """A PublicConnection resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _CloudServiceType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CloudServiceTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PublicConnection._CloudServiceType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CLOUD_SERVICE_TYPE_UNSPECIFIED: PublicConnection._CloudServiceType.ValueType  # 0
        CLOUD_SERVICE_YANDEX: PublicConnection._CloudServiceType.ValueType  # 1
        CLOUD_SERVICE_ALL_PUBLIC: PublicConnection._CloudServiceType.ValueType  # 2
        CLOUD_SERVICE_S3: PublicConnection._CloudServiceType.ValueType  # 3
        CLOUD_SERVICE_ML: PublicConnection._CloudServiceType.ValueType  # 4
        CLOUD_SERVICE_APIGW: PublicConnection._CloudServiceType.ValueType  # 5
        CLOUD_SERVICE_CONTAINER_REGISTRY: PublicConnection._CloudServiceType.ValueType  # 6
        CLOUD_SERVICE_CONSOLE: PublicConnection._CloudServiceType.ValueType  # 7
        CLOUD_SERVICE_MONITORING: PublicConnection._CloudServiceType.ValueType  # 8
        CLOUD_SERVICE_YANDEX_GPT: PublicConnection._CloudServiceType.ValueType  # 9
        CLOUD_SERVICES_ALL_API_ENDPOINT: PublicConnection._CloudServiceType.ValueType  # 10
        CLOUD_SERVICE_YMQ: PublicConnection._CloudServiceType.ValueType  # 11

    class CloudServiceType(_CloudServiceType, metaclass=_CloudServiceTypeEnumTypeWrapper): ...
    CLOUD_SERVICE_TYPE_UNSPECIFIED: PublicConnection.CloudServiceType.ValueType  # 0
    CLOUD_SERVICE_YANDEX: PublicConnection.CloudServiceType.ValueType  # 1
    CLOUD_SERVICE_ALL_PUBLIC: PublicConnection.CloudServiceType.ValueType  # 2
    CLOUD_SERVICE_S3: PublicConnection.CloudServiceType.ValueType  # 3
    CLOUD_SERVICE_ML: PublicConnection.CloudServiceType.ValueType  # 4
    CLOUD_SERVICE_APIGW: PublicConnection.CloudServiceType.ValueType  # 5
    CLOUD_SERVICE_CONTAINER_REGISTRY: PublicConnection.CloudServiceType.ValueType  # 6
    CLOUD_SERVICE_CONSOLE: PublicConnection.CloudServiceType.ValueType  # 7
    CLOUD_SERVICE_MONITORING: PublicConnection.CloudServiceType.ValueType  # 8
    CLOUD_SERVICE_YANDEX_GPT: PublicConnection.CloudServiceType.ValueType  # 9
    CLOUD_SERVICES_ALL_API_ENDPOINT: PublicConnection.CloudServiceType.ValueType  # 10
    CLOUD_SERVICE_YMQ: PublicConnection.CloudServiceType.ValueType  # 11

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PublicConnection._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: PublicConnection._Status.ValueType  # 0
        CREATING: PublicConnection._Status.ValueType  # 1
        UPDATING: PublicConnection._Status.ValueType  # 2
        DELETING: PublicConnection._Status.ValueType  # 3
        ACTIVE: PublicConnection._Status.ValueType  # 4

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: PublicConnection.Status.ValueType  # 0
    CREATING: PublicConnection.Status.ValueType  # 1
    UPDATING: PublicConnection.Status.ValueType  # 2
    DELETING: PublicConnection.Status.ValueType  # 3
    ACTIVE: PublicConnection.Status.ValueType  # 4

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
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    REGION_ID_FIELD_NUMBER: builtins.int
    TRUNK_CONNECTION_ID_FIELD_NUMBER: builtins.int
    VLAN_ID_FIELD_NUMBER: builtins.int
    IPV4_PEERING_FIELD_NUMBER: builtins.int
    IPV4_ALLOWED_SERVICE_TYPES_FIELD_NUMBER: builtins.int
    IPV4_PEER_ANNOUNCED_PREFIXES_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the publicConnection."""
    name: builtins.str
    """Name of the publicConnection.
    The name must be unique within the folder.
    Value must match the regular expression ``\\|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?``.
    """
    description: builtins.str
    """Optional description of the publicConnection. 0-256 characters long."""
    folder_id: builtins.str
    """ID of the folder that the publicConnection belongs to."""
    region_id: builtins.str
    """ID of the region that the publicConnection belongs to."""
    trunk_connection_id: builtins.str
    """ID of the trunk_connection that the publicConnection belongs to."""
    status: global___PublicConnection.Status.ValueType
    """Status of the publicConnection."""
    @property
    def vlan_id(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """VLAN_ID that the privateConnection uses in multiplexing.
        Not used in connections over partners-II
        Value range: [1, 4095]
        """

    @property
    def ipv4_peering(self) -> yandex.cloud.cic.v1.peering_pb2.Peering:
        """IPv4 peering config of connection"""

    @property
    def ipv4_allowed_service_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___PublicConnection.CloudServiceType.ValueType]:
        """Cloud services that the publicConnection connects to."""

    @property
    def ipv4_peer_announced_prefixes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """IPv4 Peer Announced Prefixes
        It's an list of ip with format ipPrefix/length where address part of ipPrefix is 0
        """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels, `key:value` pairs.
        No more than 64 per resource.
        The maximum string length in characters for each value is 63.
        Each value must match the regular expression `[-_0-9a-z]*`.
        The string length in characters for each key must be 1-63.
        Each key must match the regular expression `[a-z][-_0-9a-z]*`.
        """

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        folder_id: builtins.str = ...,
        region_id: builtins.str = ...,
        trunk_connection_id: builtins.str = ...,
        vlan_id: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        ipv4_peering: yandex.cloud.cic.v1.peering_pb2.Peering | None = ...,
        ipv4_allowed_service_types: collections.abc.Iterable[global___PublicConnection.CloudServiceType.ValueType] | None = ...,
        ipv4_peer_announced_prefixes: collections.abc.Iterable[builtins.str] | None = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        status: global___PublicConnection.Status.ValueType = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "ipv4_peering", b"ipv4_peering", "vlan_id", b"vlan_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "description", b"description", "folder_id", b"folder_id", "id", b"id", "ipv4_allowed_service_types", b"ipv4_allowed_service_types", "ipv4_peer_announced_prefixes", b"ipv4_peer_announced_prefixes", "ipv4_peering", b"ipv4_peering", "labels", b"labels", "name", b"name", "region_id", b"region_id", "status", b"status", "trunk_connection_id", b"trunk_connection_id", "vlan_id", b"vlan_id"]) -> None: ...

global___PublicConnection = PublicConnection
