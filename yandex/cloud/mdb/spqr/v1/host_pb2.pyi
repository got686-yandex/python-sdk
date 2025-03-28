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
import yandex.cloud.mdb.spqr.v1.config_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Host(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Host._Type.ValueType  # 0
        ROUTER: Host._Type.ValueType  # 2
        """A SPQR Router host."""
        COORDINATOR: Host._Type.ValueType  # 3
        """A SPQR Coordinator host."""
        INFRA: Host._Type.ValueType  # 4
        """A SPQR Infra host (router+coordinator)"""
        POSTGRESQL: Host._Type.ValueType  # 5
        """A PostgreSQL host."""
        EXTERNAL_POSTGRESQL: Host._Type.ValueType  # 6
        """An External PostgreSQL host."""
        MDB_POSTGRESQL: Host._Type.ValueType  # 7
        """A Managed PostgreSQL host"""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    TYPE_UNSPECIFIED: Host.Type.ValueType  # 0
    ROUTER: Host.Type.ValueType  # 2
    """A SPQR Router host."""
    COORDINATOR: Host.Type.ValueType  # 3
    """A SPQR Coordinator host."""
    INFRA: Host.Type.ValueType  # 4
    """A SPQR Infra host (router+coordinator)"""
    POSTGRESQL: Host.Type.ValueType  # 5
    """A PostgreSQL host."""
    EXTERNAL_POSTGRESQL: Host.Type.ValueType  # 6
    """An External PostgreSQL host."""
    MDB_POSTGRESQL: Host.Type.ValueType  # 7
    """A Managed PostgreSQL host"""

    class _Role:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Role.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ROLE_UNKNOWN: Host._Role.ValueType  # 0
        """Role of the host in the cluster is unknown."""
        PRIMARY: Host._Role.ValueType  # 1
        """Host is the primary SPQR server in the cluster."""
        SECONDARY: Host._Role.ValueType  # 2
        """Host is a secondary SPQR server in the cluster."""
        MASTER: Host._Role.ValueType  # 3
        """Host is the master PostgreSQL server in the cluster."""
        REPLICA: Host._Role.ValueType  # 4
        """Host is a replica (standby) PostgreSQL server in the cluster."""

    class Role(_Role, metaclass=_RoleEnumTypeWrapper): ...
    ROLE_UNKNOWN: Host.Role.ValueType  # 0
    """Role of the host in the cluster is unknown."""
    PRIMARY: Host.Role.ValueType  # 1
    """Host is the primary SPQR server in the cluster."""
    SECONDARY: Host.Role.ValueType  # 2
    """Host is a secondary SPQR server in the cluster."""
    MASTER: Host.Role.ValueType  # 3
    """Host is the master PostgreSQL server in the cluster."""
    REPLICA: Host.Role.ValueType  # 4
    """Host is a replica (standby) PostgreSQL server in the cluster."""

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Host._Health.ValueType  # 0
        """Health of the host is unknown."""
        ALIVE: Host._Health.ValueType  # 1
        """The host is performing all its functions normally."""
        DEAD: Host._Health.ValueType  # 2
        """The host is inoperable, and cannot perform any of its essential functions."""
        DEGRADED: Host._Health.ValueType  # 3
        """The host is degraded, and can perform only some of its essential functions."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    HEALTH_UNKNOWN: Host.Health.ValueType  # 0
    """Health of the host is unknown."""
    ALIVE: Host.Health.ValueType  # 1
    """The host is performing all its functions normally."""
    DEAD: Host.Health.ValueType  # 2
    """The host is inoperable, and cannot perform any of its essential functions."""
    DEGRADED: Host.Health.ValueType  # 3
    """The host is degraded, and can perform only some of its essential functions."""

    @typing.final
    class CPUMetric(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        USED_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        used: builtins.float
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            used: builtins.float = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["timestamp", b"timestamp", "used", b"used"]) -> None: ...

    @typing.final
    class MemoryMetric(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        USED_FIELD_NUMBER: builtins.int
        TOTAL_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        used: builtins.int
        total: builtins.int
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            used: builtins.int = ...,
            total: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["timestamp", b"timestamp", "total", b"total", "used", b"used"]) -> None: ...

    @typing.final
    class DiskMetric(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TIMESTAMP_FIELD_NUMBER: builtins.int
        USED_FIELD_NUMBER: builtins.int
        TOTAL_FIELD_NUMBER: builtins.int
        timestamp: builtins.int
        used: builtins.int
        total: builtins.int
        def __init__(
            self,
            *,
            timestamp: builtins.int = ...,
            used: builtins.int = ...,
            total: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["timestamp", b"timestamp", "total", b"total", "used", b"used"]) -> None: ...

    @typing.final
    class SystemMetrics(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CPU_FIELD_NUMBER: builtins.int
        MEMORY_FIELD_NUMBER: builtins.int
        DISK_FIELD_NUMBER: builtins.int
        @property
        def cpu(self) -> global___Host.CPUMetric: ...
        @property
        def memory(self) -> global___Host.MemoryMetric: ...
        @property
        def disk(self) -> global___Host.DiskMetric: ...
        def __init__(
            self,
            *,
            cpu: global___Host.CPUMetric | None = ...,
            memory: global___Host.MemoryMetric | None = ...,
            disk: global___Host.DiskMetric | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["cpu", b"cpu", "disk", b"disk", "memory", b"memory"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["cpu", b"cpu", "disk", b"disk", "memory", b"memory"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    WALLE_LINK_FIELD_NUMBER: builtins.int
    STATE_REASON_FIELD_NUMBER: builtins.int
    SYSTEM_FIELD_NUMBER: builtins.int
    SHARD_NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the SPQR host. The host name is assigned by MDB at creation time, and cannot be changed.
    1-63 characters long.

    The name is unique across all MDB hosts that exist on the platform, as it defines the FQDN of the host.
    """
    cluster_id: builtins.str
    """The ID of the SPQR cluster that the host belongs to."""
    zone_id: builtins.str
    """ID of the availability zone where the SPQR host resides."""
    role: global___Host.Role.ValueType
    """Role of the host in the cluster."""
    health: global___Host.Health.ValueType
    """Status code of the aggregated health of the host."""
    subnet_id: builtins.str
    """ID of the subnet that the host belongs to."""
    assign_public_ip: builtins.bool
    """Flag showing public IP assignment status to this host."""
    type: global___Host.Type.ValueType
    """Host type"""
    walle_link: builtins.str
    """link to wall-e (porto only)"""
    state_reason: builtins.str
    """host state reason from cms (porto only)"""
    shard_name: builtins.str
    """Shard which this host belongs to."""
    @property
    def resources(self) -> yandex.cloud.mdb.spqr.v1.config_pb2.Resources:
        """Resources allocated to the SPQR host."""

    @property
    def services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Service]:
        """Services provided by the host."""

    @property
    def system(self) -> global___Host.SystemMetrics:
        """System metrics"""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        cluster_id: builtins.str = ...,
        zone_id: builtins.str = ...,
        resources: yandex.cloud.mdb.spqr.v1.config_pb2.Resources | None = ...,
        role: global___Host.Role.ValueType = ...,
        health: global___Host.Health.ValueType = ...,
        services: collections.abc.Iterable[global___Service] | None = ...,
        subnet_id: builtins.str = ...,
        assign_public_ip: builtins.bool = ...,
        type: global___Host.Type.ValueType = ...,
        walle_link: builtins.str = ...,
        state_reason: builtins.str = ...,
        system: global___Host.SystemMetrics | None = ...,
        shard_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["resources", b"resources", "system", b"system"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assign_public_ip", b"assign_public_ip", "cluster_id", b"cluster_id", "health", b"health", "name", b"name", "resources", b"resources", "role", b"role", "services", b"services", "shard_name", b"shard_name", "state_reason", b"state_reason", "subnet_id", b"subnet_id", "system", b"system", "type", b"type", "walle_link", b"walle_link", "zone_id", b"zone_id"]) -> None: ...

global___Host = Host

@typing.final
class Service(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: Service._Type.ValueType  # 0
        ROUTER: Service._Type.ValueType  # 2
        """The host is running a SPQR Router."""
        COORDINATOR: Service._Type.ValueType  # 3
        """The host is running a SPQR Coordinator."""
        INFRA: Service._Type.ValueType  # 4
        """The host is running a SPQR router and coordinator"""
        POSTGRESQL: Service._Type.ValueType  # 5
        """The host is running a PostgreSQL."""
        EXTERNAL_POSTGRESQL: Service._Type.ValueType  # 6
        """The host is running a PostgreSQL."""
        MDB_POSTGRESQL: Service._Type.ValueType  # 7
        """The host is running a PostgreSQL"""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    TYPE_UNSPECIFIED: Service.Type.ValueType  # 0
    ROUTER: Service.Type.ValueType  # 2
    """The host is running a SPQR Router."""
    COORDINATOR: Service.Type.ValueType  # 3
    """The host is running a SPQR Coordinator."""
    INFRA: Service.Type.ValueType  # 4
    """The host is running a SPQR router and coordinator"""
    POSTGRESQL: Service.Type.ValueType  # 5
    """The host is running a PostgreSQL."""
    EXTERNAL_POSTGRESQL: Service.Type.ValueType  # 6
    """The host is running a PostgreSQL."""
    MDB_POSTGRESQL: Service.Type.ValueType  # 7
    """The host is running a PostgreSQL"""

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Service._Health.ValueType  # 0
        """Health of the server is unknown."""
        ALIVE: Service._Health.ValueType  # 1
        """The server is working normally."""
        DEAD: Service._Health.ValueType  # 2
        """The server is dead or unresponsive."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    HEALTH_UNKNOWN: Service.Health.ValueType  # 0
    """Health of the server is unknown."""
    ALIVE: Service.Health.ValueType  # 1
    """The server is working normally."""
    DEAD: Service.Health.ValueType  # 2
    """The server is dead or unresponsive."""

    TYPE_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    type: global___Service.Type.ValueType
    """Type of the service provided by the host."""
    health: global___Service.Health.ValueType
    """Status code of server availability."""
    def __init__(
        self,
        *,
        type: global___Service.Type.ValueType = ...,
        health: global___Service.Health.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["health", b"health", "type", b"type"]) -> None: ...

global___Service = Service

@typing.final
class HostSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ZONE_ID_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    SHARD_NAME_FIELD_NUMBER: builtins.int
    MDB_POSTGRESQL_FIELD_NUMBER: builtins.int
    zone_id: builtins.str
    """ID of the availability zone where the host resides.
    To get a list of available zones, use the [yandex.cloud.compute.v1.ZoneService.List] request.
    """
    subnet_id: builtins.str
    """ID of the subnet that the host should belong to. This subnet should be a part
    of the network that the cluster belongs to.
    The network ID is set in the [Cluster.network_id] field.
    """
    assign_public_ip: builtins.bool
    """Whether the host should get a public IP address on creation.

    After a host has been created, this setting cannot be changed. To remove an assigned public IP, or to assign
    a public IP to a host without one, recreate the host with [assign_public_ip] set as needed.

    Possible values:
    * false - don't assign a public IP to the host.
    * true - the host should have a public IP address.
    """
    type: global___Host.Type.ValueType
    """Type of the host to be deployed."""
    shard_name: builtins.str
    """Name of the shard that the host belongs to.
    If empty, host doesn't belong to any shard
    """
    @property
    def mdb_postgresql(self) -> yandex.cloud.mdb.spqr.v1.config_pb2.MDBPostgreSQL: ...
    def __init__(
        self,
        *,
        zone_id: builtins.str = ...,
        subnet_id: builtins.str = ...,
        assign_public_ip: builtins.bool = ...,
        type: global___Host.Type.ValueType = ...,
        shard_name: builtins.str = ...,
        mdb_postgresql: yandex.cloud.mdb.spqr.v1.config_pb2.MDBPostgreSQL | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["mdb_postgresql", b"mdb_postgresql"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assign_public_ip", b"assign_public_ip", "mdb_postgresql", b"mdb_postgresql", "shard_name", b"shard_name", "subnet_id", b"subnet_id", "type", b"type", "zone_id", b"zone_id"]) -> None: ...

global___HostSpec = HostSpec
