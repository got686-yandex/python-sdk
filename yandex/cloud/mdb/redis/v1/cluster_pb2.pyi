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
import google.type.timeofday_pb2
import sys
import typing
import yandex.cloud.mdb.redis.v1.config.redis5_0_pb2
import yandex.cloud.mdb.redis.v1.config.redis6_0_pb2
import yandex.cloud.mdb.redis.v1.config.redis6_2_pb2
import yandex.cloud.mdb.redis.v1.config.redis7_0_pb2
import yandex.cloud.mdb.redis.v1.config.redis_pb2
import yandex.cloud.mdb.redis.v1.maintenance_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Cluster(google.protobuf.message.Message):
    """Description of a Redis cluster. For more information, see
    the Managed Service for Redis [documentation](/docs/managed-redis/concepts/).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Environment:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EnvironmentEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Environment.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ENVIRONMENT_UNSPECIFIED: Cluster._Environment.ValueType  # 0
        PRODUCTION: Cluster._Environment.ValueType  # 1
        """Stable environment with a conservative update policy:
        only hotfixes are applied during regular maintenance.
        """
        PRESTABLE: Cluster._Environment.ValueType  # 2
        """Environment with more aggressive update policy: new versions
        are rolled out irrespective of backward compatibility.
        """

    class Environment(_Environment, metaclass=_EnvironmentEnumTypeWrapper): ...
    ENVIRONMENT_UNSPECIFIED: Cluster.Environment.ValueType  # 0
    PRODUCTION: Cluster.Environment.ValueType  # 1
    """Stable environment with a conservative update policy:
    only hotfixes are applied during regular maintenance.
    """
    PRESTABLE: Cluster.Environment.ValueType  # 2
    """Environment with more aggressive update policy: new versions
    are rolled out irrespective of backward compatibility.
    """

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Cluster._Health.ValueType  # 0
        """Cluster is in unknown state (we have no data)"""
        ALIVE: Cluster._Health.ValueType  # 1
        """Cluster is alive and well (all hosts are alive)"""
        DEAD: Cluster._Health.ValueType  # 2
        """Cluster is inoperable (it cannot perform any of its essential functions)"""
        DEGRADED: Cluster._Health.ValueType  # 3
        """Cluster is partially alive (it can perform some of its essential functions)"""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    HEALTH_UNKNOWN: Cluster.Health.ValueType  # 0
    """Cluster is in unknown state (we have no data)"""
    ALIVE: Cluster.Health.ValueType  # 1
    """Cluster is alive and well (all hosts are alive)"""
    DEAD: Cluster.Health.ValueType  # 2
    """Cluster is inoperable (it cannot perform any of its essential functions)"""
    DEGRADED: Cluster.Health.ValueType  # 3
    """Cluster is partially alive (it can perform some of its essential functions)"""

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNKNOWN: Cluster._Status.ValueType  # 0
        """Cluster status is unknown"""
        CREATING: Cluster._Status.ValueType  # 1
        """Cluster is being created"""
        RUNNING: Cluster._Status.ValueType  # 2
        """Cluster is running"""
        ERROR: Cluster._Status.ValueType  # 3
        """Cluster failed"""
        UPDATING: Cluster._Status.ValueType  # 4
        """Cluster is being updated."""
        STOPPING: Cluster._Status.ValueType  # 5
        """Cluster is stopping."""
        STOPPED: Cluster._Status.ValueType  # 6
        """Cluster stopped."""
        STARTING: Cluster._Status.ValueType  # 7
        """Cluster is starting."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNKNOWN: Cluster.Status.ValueType  # 0
    """Cluster status is unknown"""
    CREATING: Cluster.Status.ValueType  # 1
    """Cluster is being created"""
    RUNNING: Cluster.Status.ValueType  # 2
    """Cluster is running"""
    ERROR: Cluster.Status.ValueType  # 3
    """Cluster failed"""
    UPDATING: Cluster.Status.ValueType  # 4
    """Cluster is being updated."""
    STOPPING: Cluster.Status.ValueType  # 5
    """Cluster is stopping."""
    STOPPED: Cluster.Status.ValueType  # 6
    """Cluster stopped."""
    STARTING: Cluster.Status.ValueType  # 7
    """Cluster is starting."""

    class _PersistenceMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PersistenceModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cluster._PersistenceMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ON: Cluster._PersistenceMode.ValueType  # 0
        """cluster persistence mode on"""
        OFF: Cluster._PersistenceMode.ValueType  # 1
        """cluster persistence mode off"""
        ON_REPLICAS: Cluster._PersistenceMode.ValueType  # 2
        """cluster persistence on replicas only"""

    class PersistenceMode(_PersistenceMode, metaclass=_PersistenceModeEnumTypeWrapper): ...
    ON: Cluster.PersistenceMode.ValueType  # 0
    """cluster persistence mode on"""
    OFF: Cluster.PersistenceMode.ValueType  # 1
    """cluster persistence mode off"""
    ON_REPLICAS: Cluster.PersistenceMode.ValueType  # 2
    """cluster persistence on replicas only"""

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
    FOLDER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    ENVIRONMENT_FIELD_NUMBER: builtins.int
    MONITORING_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    SHARDED_FIELD_NUMBER: builtins.int
    MAINTENANCE_WINDOW_FIELD_NUMBER: builtins.int
    PLANNED_OPERATION_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    TLS_ENABLED_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    PERSISTENCE_MODE_FIELD_NUMBER: builtins.int
    ANNOUNCE_HOSTNAMES_FIELD_NUMBER: builtins.int
    AUTH_SENTINEL_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the Redis cluster.
    This ID is assigned by MDB at creation time.
    """
    folder_id: builtins.str
    """ID of the folder that the Redis cluster belongs to."""
    name: builtins.str
    """Name of the Redis cluster.
    The name is unique within the folder. 3-63 characters long.
    """
    description: builtins.str
    """Description of the Redis cluster. 0-256 characters long."""
    environment: global___Cluster.Environment.ValueType
    """Deployment environment of the Redis cluster."""
    network_id: builtins.str
    health: global___Cluster.Health.ValueType
    """Aggregated cluster health."""
    status: global___Cluster.Status.ValueType
    """Cluster status."""
    sharded: builtins.bool
    """Redis cluster mode on/off."""
    tls_enabled: builtins.bool
    """TLS port and functionality on\\off"""
    deletion_protection: builtins.bool
    """Deletion Protection inhibits deletion of the cluster"""
    persistence_mode: global___Cluster.PersistenceMode.ValueType
    """Persistence mode"""
    announce_hostnames: builtins.bool
    """Enable FQDN instead of ip"""
    auth_sentinel: builtins.bool
    """Allows to use ACL users to auth in sentinel"""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Custom labels for the Redis cluster as `key:value` pairs.
        Maximum 64 per cluster.
        """

    @property
    def monitoring(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Monitoring]:
        """Description of monitoring systems relevant to the Redis cluster."""

    @property
    def config(self) -> global___ClusterConfig:
        """Configuration of the Redis cluster."""

    @property
    def maintenance_window(self) -> yandex.cloud.mdb.redis.v1.maintenance_pb2.MaintenanceWindow:
        """Maintenance window for the cluster."""

    @property
    def planned_operation(self) -> yandex.cloud.mdb.redis.v1.maintenance_pb2.MaintenanceOperation:
        """Planned maintenance operation to be started for the cluster within the nearest [maintenance_window]."""

    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """User security groups"""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        folder_id: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        environment: global___Cluster.Environment.ValueType = ...,
        monitoring: collections.abc.Iterable[global___Monitoring] | None = ...,
        config: global___ClusterConfig | None = ...,
        network_id: builtins.str = ...,
        health: global___Cluster.Health.ValueType = ...,
        status: global___Cluster.Status.ValueType = ...,
        sharded: builtins.bool = ...,
        maintenance_window: yandex.cloud.mdb.redis.v1.maintenance_pb2.MaintenanceWindow | None = ...,
        planned_operation: yandex.cloud.mdb.redis.v1.maintenance_pb2.MaintenanceOperation | None = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
        tls_enabled: builtins.bool = ...,
        deletion_protection: builtins.bool = ...,
        persistence_mode: global___Cluster.PersistenceMode.ValueType = ...,
        announce_hostnames: builtins.bool = ...,
        auth_sentinel: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["config", b"config", "created_at", b"created_at", "maintenance_window", b"maintenance_window", "planned_operation", b"planned_operation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["announce_hostnames", b"announce_hostnames", "auth_sentinel", b"auth_sentinel", "config", b"config", "created_at", b"created_at", "deletion_protection", b"deletion_protection", "description", b"description", "environment", b"environment", "folder_id", b"folder_id", "health", b"health", "id", b"id", "labels", b"labels", "maintenance_window", b"maintenance_window", "monitoring", b"monitoring", "name", b"name", "network_id", b"network_id", "persistence_mode", b"persistence_mode", "planned_operation", b"planned_operation", "security_group_ids", b"security_group_ids", "sharded", b"sharded", "status", b"status", "tls_enabled", b"tls_enabled"]) -> None: ...

global___Cluster = Cluster

@typing.final
class Monitoring(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LINK_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the monitoring system."""
    description: builtins.str
    """Description of the monitoring system."""
    link: builtins.str
    """Link to the monitoring system charts for the Redis cluster."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
        link: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "link", b"link", "name", b"name"]) -> None: ...

global___Monitoring = Monitoring

@typing.final
class ClusterConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    REDIS_CONFIG_5_0_FIELD_NUMBER: builtins.int
    REDIS_CONFIG_6_0_FIELD_NUMBER: builtins.int
    REDIS_CONFIG_6_2_FIELD_NUMBER: builtins.int
    REDIS_CONFIG_7_0_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    BACKUP_WINDOW_START_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    REDIS_FIELD_NUMBER: builtins.int
    DISK_SIZE_AUTOSCALING_FIELD_NUMBER: builtins.int
    BACKUP_RETAIN_PERIOD_DAYS_FIELD_NUMBER: builtins.int
    version: builtins.str
    """Version of Redis server software."""
    @property
    def redis_config_5_0(self) -> yandex.cloud.mdb.redis.v1.config.redis5_0_pb2.RedisConfigSet5_0:
        """Configuration of a Redis 5.0 server."""

    @property
    def redis_config_6_0(self) -> yandex.cloud.mdb.redis.v1.config.redis6_0_pb2.RedisConfigSet6_0:
        """Configuration of a Redis 6.0 server."""

    @property
    def redis_config_6_2(self) -> yandex.cloud.mdb.redis.v1.config.redis6_2_pb2.RedisConfigSet6_2:
        """Configuration of a Redis 6.2 server."""

    @property
    def redis_config_7_0(self) -> yandex.cloud.mdb.redis.v1.config.redis7_0_pb2.RedisConfigSet7_0:
        """Configuration of a Redis 7.0 server."""

    @property
    def resources(self) -> global___Resources:
        """Resources allocated to Redis hosts."""

    @property
    def backup_window_start(self) -> google.type.timeofday_pb2.TimeOfDay:
        """Time to start the daily backup, in the UTC timezone."""

    @property
    def access(self) -> global___Access:
        """Access policy to DB"""

    @property
    def redis(self) -> yandex.cloud.mdb.redis.v1.config.redis_pb2.RedisConfigSet:
        """Unified configuration of a Redis cluster."""

    @property
    def disk_size_autoscaling(self) -> global___DiskSizeAutoscaling:
        """Disk size autoscaling settings"""

    @property
    def backup_retain_period_days(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Retain period of automatically created backup in days"""

    def __init__(
        self,
        *,
        version: builtins.str = ...,
        redis_config_5_0: yandex.cloud.mdb.redis.v1.config.redis5_0_pb2.RedisConfigSet5_0 | None = ...,
        redis_config_6_0: yandex.cloud.mdb.redis.v1.config.redis6_0_pb2.RedisConfigSet6_0 | None = ...,
        redis_config_6_2: yandex.cloud.mdb.redis.v1.config.redis6_2_pb2.RedisConfigSet6_2 | None = ...,
        redis_config_7_0: yandex.cloud.mdb.redis.v1.config.redis7_0_pb2.RedisConfigSet7_0 | None = ...,
        resources: global___Resources | None = ...,
        backup_window_start: google.type.timeofday_pb2.TimeOfDay | None = ...,
        access: global___Access | None = ...,
        redis: yandex.cloud.mdb.redis.v1.config.redis_pb2.RedisConfigSet | None = ...,
        disk_size_autoscaling: global___DiskSizeAutoscaling | None = ...,
        backup_retain_period_days: google.protobuf.wrappers_pb2.Int64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["access", b"access", "backup_retain_period_days", b"backup_retain_period_days", "backup_window_start", b"backup_window_start", "disk_size_autoscaling", b"disk_size_autoscaling", "redis", b"redis", "redis_config", b"redis_config", "redis_config_5_0", b"redis_config_5_0", "redis_config_6_0", b"redis_config_6_0", "redis_config_6_2", b"redis_config_6_2", "redis_config_7_0", b"redis_config_7_0", "resources", b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["access", b"access", "backup_retain_period_days", b"backup_retain_period_days", "backup_window_start", b"backup_window_start", "disk_size_autoscaling", b"disk_size_autoscaling", "redis", b"redis", "redis_config", b"redis_config", "redis_config_5_0", b"redis_config_5_0", "redis_config_6_0", b"redis_config_6_0", "redis_config_6_2", b"redis_config_6_2", "redis_config_7_0", b"redis_config_7_0", "resources", b"resources", "version", b"version"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["redis_config", b"redis_config"]) -> typing.Literal["redis_config_5_0", "redis_config_6_0", "redis_config_6_2", "redis_config_7_0"] | None: ...

global___ClusterConfig = ClusterConfig

@typing.final
class Shard(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the Redis shard. The shard name is assigned by user at creation time, and cannot be changed.
    1-63 characters long.
    """
    cluster_id: builtins.str
    """ID of the Redis cluster the shard belongs to. The ID is assigned by MDB at creation time."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "name", b"name"]) -> None: ...

global___Shard = Shard

@typing.final
class Host(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Role:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Role.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ROLE_UNKNOWN: Host._Role.ValueType  # 0
        """Role of the host in the cluster is unknown. Default value."""
        MASTER: Host._Role.ValueType  # 1
        """Host is the master Redis server in the cluster."""
        REPLICA: Host._Role.ValueType  # 2
        """Host is a replica (standby) Redis server in the cluster."""

    class Role(_Role, metaclass=_RoleEnumTypeWrapper): ...
    ROLE_UNKNOWN: Host.Role.ValueType  # 0
    """Role of the host in the cluster is unknown. Default value."""
    MASTER: Host.Role.ValueType  # 1
    """Host is the master Redis server in the cluster."""
    REPLICA: Host.Role.ValueType  # 2
    """Host is a replica (standby) Redis server in the cluster."""

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Host._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Host._Health.ValueType  # 0
        """Health of the host is unknown. Default value."""
        ALIVE: Host._Health.ValueType  # 1
        """The host is performing all its functions normally."""
        DEAD: Host._Health.ValueType  # 2
        """The host is inoperable, and cannot perform any of its essential functions."""
        DEGRADED: Host._Health.ValueType  # 3
        """The host is degraded, and can perform only some of its essential functions."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    HEALTH_UNKNOWN: Host.Health.ValueType  # 0
    """Health of the host is unknown. Default value."""
    ALIVE: Host.Health.ValueType  # 1
    """The host is performing all its functions normally."""
    DEAD: Host.Health.ValueType  # 2
    """The host is inoperable, and cannot perform any of its essential functions."""
    DEGRADED: Host.Health.ValueType  # 3
    """The host is degraded, and can perform only some of its essential functions."""

    NAME_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    SUBNET_ID_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    SHARD_NAME_FIELD_NUMBER: builtins.int
    REPLICA_PRIORITY_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IP_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the Redis host. The host name is assigned by MDB at creation time, and cannot be changed.
    1-63 characters long.

    The name is unique across all MDB hosts that exist on the platform, as it defines the FQDN of the host.
    """
    cluster_id: builtins.str
    """ID of the Redis cluster. The ID is assigned by MDB at creation time."""
    zone_id: builtins.str
    """ID of the availability zone where the Redis host resides."""
    subnet_id: builtins.str
    """ID of the subnet that the host belongs to."""
    role: global___Host.Role.ValueType
    """Role of the host in the cluster. If the field has default value, it is not returned in the response."""
    health: global___Host.Health.ValueType
    """Aggregated health of the host. If the field has default value, it is not returned in the response."""
    shard_name: builtins.str
    assign_public_ip: builtins.bool
    """Flag showing public IP assignment status to this host."""
    @property
    def resources(self) -> global___Resources:
        """Resources allocated to the Redis host."""

    @property
    def services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Service]:
        """Services provided by the host."""

    @property
    def replica_priority(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """A replica with a low priority number is considered better for promotion.
        A replica with priority of 0 will never be selected by Redis Sentinel for promotion.
        Works only for non-sharded clusters. Default value is 100.
        """

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        cluster_id: builtins.str = ...,
        zone_id: builtins.str = ...,
        subnet_id: builtins.str = ...,
        resources: global___Resources | None = ...,
        role: global___Host.Role.ValueType = ...,
        health: global___Host.Health.ValueType = ...,
        services: collections.abc.Iterable[global___Service] | None = ...,
        shard_name: builtins.str = ...,
        replica_priority: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        assign_public_ip: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["replica_priority", b"replica_priority", "resources", b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assign_public_ip", b"assign_public_ip", "cluster_id", b"cluster_id", "health", b"health", "name", b"name", "replica_priority", b"replica_priority", "resources", b"resources", "role", b"role", "services", b"services", "shard_name", b"shard_name", "subnet_id", b"subnet_id", "zone_id", b"zone_id"]) -> None: ...

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
        """Service type of the host is unspecified. Default value."""
        REDIS: Service._Type.ValueType  # 1
        """The host is a Redis server."""
        ARBITER: Service._Type.ValueType  # 2
        """The host provides a Sentinel-only service (a quorum node)."""
        REDIS_CLUSTER: Service._Type.ValueType  # 3
        """The host is a Redis Cluster node."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    TYPE_UNSPECIFIED: Service.Type.ValueType  # 0
    """Service type of the host is unspecified. Default value."""
    REDIS: Service.Type.ValueType  # 1
    """The host is a Redis server."""
    ARBITER: Service.Type.ValueType  # 2
    """The host provides a Sentinel-only service (a quorum node)."""
    REDIS_CLUSTER: Service.Type.ValueType  # 3
    """The host is a Redis Cluster node."""

    class _Health:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _HealthEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Service._Health.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        HEALTH_UNKNOWN: Service._Health.ValueType  # 0
        """Health of the server is unknown. Default value."""
        ALIVE: Service._Health.ValueType  # 1
        """The server is working normally."""
        DEAD: Service._Health.ValueType  # 2
        """The server is dead or unresponsive."""

    class Health(_Health, metaclass=_HealthEnumTypeWrapper): ...
    HEALTH_UNKNOWN: Service.Health.ValueType  # 0
    """Health of the server is unknown. Default value."""
    ALIVE: Service.Health.ValueType  # 1
    """The server is working normally."""
    DEAD: Service.Health.ValueType  # 2
    """The server is dead or unresponsive."""

    TYPE_FIELD_NUMBER: builtins.int
    HEALTH_FIELD_NUMBER: builtins.int
    type: global___Service.Type.ValueType
    """Type of the service provided by the host. If the field has default value, it is not returned in the response."""
    health: global___Service.Health.ValueType
    """Aggregated health of the service. If the field has default value, it is not returned in the response."""
    def __init__(
        self,
        *,
        type: global___Service.Type.ValueType = ...,
        health: global___Service.Health.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["health", b"health", "type", b"type"]) -> None: ...

global___Service = Service

@typing.final
class Resources(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    DISK_SIZE_FIELD_NUMBER: builtins.int
    DISK_TYPE_ID_FIELD_NUMBER: builtins.int
    resource_preset_id: builtins.str
    """ID of the preset for computational resources available to a host (CPU, memory etc.).
    All available presets are listed in the [documentation](/docs/managed-redis/concepts/instance-types).
    """
    disk_size: builtins.int
    """Volume of the storage available to a host, in bytes."""
    disk_type_id: builtins.str
    """Type of the storage environment for the host.
    Possible values:
    * network-ssd - network SSD drive,
    * local-ssd - local SSD storage.
    """
    def __init__(
        self,
        *,
        resource_preset_id: builtins.str = ...,
        disk_size: builtins.int = ...,
        disk_type_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["disk_size", b"disk_size", "disk_type_id", b"disk_type_id", "resource_preset_id", b"resource_preset_id"]) -> None: ...

global___Resources = Resources

@typing.final
class Access(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_LENS_FIELD_NUMBER: builtins.int
    WEB_SQL_FIELD_NUMBER: builtins.int
    data_lens: builtins.bool
    """Allow access for DataLens"""
    web_sql: builtins.bool
    """Allow access for Web SQL."""
    def __init__(
        self,
        *,
        data_lens: builtins.bool = ...,
        web_sql: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_lens", b"data_lens", "web_sql", b"web_sql"]) -> None: ...

global___Access = Access

@typing.final
class DiskSizeAutoscaling(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLANNED_USAGE_THRESHOLD_FIELD_NUMBER: builtins.int
    EMERGENCY_USAGE_THRESHOLD_FIELD_NUMBER: builtins.int
    DISK_SIZE_LIMIT_FIELD_NUMBER: builtins.int
    @property
    def planned_usage_threshold(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Amount of used storage for automatic disk scaling in the maintenance window, 0 means disabled, in percent."""

    @property
    def emergency_usage_threshold(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Amount of used storage for immediately  automatic disk scaling, 0 means disabled, in percent."""

    @property
    def disk_size_limit(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """Limit on how large the storage for database instances can automatically grow, in bytes."""

    def __init__(
        self,
        *,
        planned_usage_threshold: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        emergency_usage_threshold: google.protobuf.wrappers_pb2.Int64Value | None = ...,
        disk_size_limit: google.protobuf.wrappers_pb2.Int64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["disk_size_limit", b"disk_size_limit", "emergency_usage_threshold", b"emergency_usage_threshold", "planned_usage_threshold", b"planned_usage_threshold"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["disk_size_limit", b"disk_size_limit", "emergency_usage_threshold", b"emergency_usage_threshold", "planned_usage_threshold", b"planned_usage_threshold"]) -> None: ...

global___DiskSizeAutoscaling = DiskSizeAutoscaling
