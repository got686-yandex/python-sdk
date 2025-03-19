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
import yandex.cloud.ydb.v1.backup_pb2
import yandex.cloud.ydb.v1.database_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MoveDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FOLDER_ID_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    """ID of the YDB instance to move."""
    destination_folder_id: builtins.str
    """ID of the destination folder."""
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
        destination_folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id", "destination_folder_id", b"destination_folder_id"]) -> None: ...

global___MoveDatabaseRequest = MoveDatabaseRequest

@typing.final
class MoveDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    database_name: builtins.str
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
        database_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id", "database_name", b"database_name"]) -> None: ...

global___MoveDatabaseMetadata = MoveDatabaseMetadata

@typing.final
class RestoreBackupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUP_ID_FIELD_NUMBER: builtins.int
    DATABASE_ID_FIELD_NUMBER: builtins.int
    PATHS_TO_RESTORE_FIELD_NUMBER: builtins.int
    TARGET_PATH_FIELD_NUMBER: builtins.int
    backup_id: builtins.str
    """Required. ID of the YDB backup."""
    database_id: builtins.str
    """Required. ID of the YDB database."""
    target_path: builtins.str
    """Specify target path."""
    @property
    def paths_to_restore(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Specify paths to restore.
        If empty, all paths will restored by default.
        """

    def __init__(
        self,
        *,
        backup_id: builtins.str = ...,
        database_id: builtins.str = ...,
        paths_to_restore: collections.abc.Iterable[builtins.str] | None = ...,
        target_path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["backup_id", b"backup_id", "database_id", b"database_id", "paths_to_restore", b"paths_to_restore", "target_path", b"target_path"]) -> None: ...

global___RestoreBackupRequest = RestoreBackupRequest

@typing.final
class RestoreBackupMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUP_ID_FIELD_NUMBER: builtins.int
    DATABASE_ID_FIELD_NUMBER: builtins.int
    backup_id: builtins.str
    database_id: builtins.str
    def __init__(
        self,
        *,
        backup_id: builtins.str = ...,
        database_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["backup_id", b"backup_id", "database_id", b"database_id"]) -> None: ...

global___RestoreBackupMetadata = RestoreBackupMetadata

@typing.final
class BackupDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    BACKUP_SETTINGS_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    @property
    def backup_settings(self) -> yandex.cloud.ydb.v1.backup_pb2.BackupSettings:
        """custom backup options, if required."""

    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
        backup_settings: yandex.cloud.ydb.v1.backup_pb2.BackupSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["backup_settings", b"backup_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["backup_settings", b"backup_settings", "database_id", b"database_id"]) -> None: ...

global___BackupDatabaseRequest = BackupDatabaseRequest

@typing.final
class BackupDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUP_ID_FIELD_NUMBER: builtins.int
    DATABASE_ID_FIELD_NUMBER: builtins.int
    backup_id: builtins.str
    database_id: builtins.str
    def __init__(
        self,
        *,
        backup_id: builtins.str = ...,
        database_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["backup_id", b"backup_id", "database_id", b"database_id"]) -> None: ...

global___BackupDatabaseMetadata = BackupDatabaseMetadata

@typing.final
class StartDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id"]) -> None: ...

global___StartDatabaseRequest = StartDatabaseRequest

@typing.final
class StartDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    database_name: builtins.str
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
        database_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id", "database_name", b"database_name"]) -> None: ...

global___StartDatabaseMetadata = StartDatabaseMetadata

@typing.final
class StopDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id"]) -> None: ...

global___StopDatabaseRequest = StopDatabaseRequest

@typing.final
class StopDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    database_name: builtins.str
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
        database_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id", "database_name", b"database_name"]) -> None: ...

global___StopDatabaseMetadata = StopDatabaseMetadata

@typing.final
class GetDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    """Required. ID of the YDB cluster."""
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id"]) -> None: ...

global___GetDatabaseRequest = GetDatabaseRequest

@typing.final
class ListDatabasesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a `next_page_token` that can be used
    to get the next page of results in subsequent ListDatabases requests.
    Acceptable values are 0 to 1000, inclusive. Default value: 100.
    """
    page_token: builtins.str
    """Page token. Set `page_token` to the `next_page_token` returned by a previous ListDatabases
    request to get the next page of results.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListDatabasesRequest = ListDatabasesRequest

@typing.final
class ListDatabasesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for ListDatabases requests,
    if the number of results is larger than `page_size` specified in the request.
    To get the next page, specify the value of `next_page_token` as a value for
    the `page_token` parameter in the next ListDatabases request. Subsequent ListDatabases
    requests will have their own `next_page_token` to continue paging through the results.
    """
    @property
    def databases(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ydb.v1.database_pb2.Database]: ...
    def __init__(
        self,
        *,
        databases: collections.abc.Iterable[yandex.cloud.ydb.v1.database_pb2.Database] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["databases", b"databases", "next_page_token", b"next_page_token"]) -> None: ...

global___ListDatabasesResponse = ListDatabasesResponse

@typing.final
class CreateDatabaseRequest(google.protobuf.message.Message):
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
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    STORAGE_CONFIG_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    ZONAL_DATABASE_FIELD_NUMBER: builtins.int
    REGIONAL_DATABASE_FIELD_NUMBER: builtins.int
    DEDICATED_DATABASE_FIELD_NUMBER: builtins.int
    SERVERLESS_DATABASE_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IPS_FIELD_NUMBER: builtins.int
    LOCATION_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    BACKUP_CONFIG_FIELD_NUMBER: builtins.int
    MONITORING_CONFIG_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    name: builtins.str
    description: builtins.str
    resource_preset_id: builtins.str
    network_id: builtins.str
    assign_public_ips: builtins.bool
    location_id: builtins.str
    deletion_protection: builtins.bool
    @property
    def storage_config(self) -> yandex.cloud.ydb.v1.database_pb2.StorageConfig: ...
    @property
    def scale_policy(self) -> yandex.cloud.ydb.v1.database_pb2.ScalePolicy: ...
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def zonal_database(self) -> yandex.cloud.ydb.v1.database_pb2.ZonalDatabase:
        """deprecated field"""

    @property
    def regional_database(self) -> yandex.cloud.ydb.v1.database_pb2.RegionalDatabase:
        """deprecated field"""

    @property
    def dedicated_database(self) -> yandex.cloud.ydb.v1.database_pb2.DedicatedDatabase: ...
    @property
    def serverless_database(self) -> yandex.cloud.ydb.v1.database_pb2.ServerlessDatabase: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def backup_config(self) -> yandex.cloud.ydb.v1.backup_pb2.BackupConfig: ...
    @property
    def monitoring_config(self) -> yandex.cloud.ydb.v1.database_pb2.MonitoringConfig: ...
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        resource_preset_id: builtins.str = ...,
        storage_config: yandex.cloud.ydb.v1.database_pb2.StorageConfig | None = ...,
        scale_policy: yandex.cloud.ydb.v1.database_pb2.ScalePolicy | None = ...,
        network_id: builtins.str = ...,
        subnet_ids: collections.abc.Iterable[builtins.str] | None = ...,
        zonal_database: yandex.cloud.ydb.v1.database_pb2.ZonalDatabase | None = ...,
        regional_database: yandex.cloud.ydb.v1.database_pb2.RegionalDatabase | None = ...,
        dedicated_database: yandex.cloud.ydb.v1.database_pb2.DedicatedDatabase | None = ...,
        serverless_database: yandex.cloud.ydb.v1.database_pb2.ServerlessDatabase | None = ...,
        assign_public_ips: builtins.bool = ...,
        location_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        backup_config: yandex.cloud.ydb.v1.backup_pb2.BackupConfig | None = ...,
        monitoring_config: yandex.cloud.ydb.v1.database_pb2.MonitoringConfig | None = ...,
        deletion_protection: builtins.bool = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["backup_config", b"backup_config", "database_type", b"database_type", "dedicated_database", b"dedicated_database", "monitoring_config", b"monitoring_config", "regional_database", b"regional_database", "scale_policy", b"scale_policy", "serverless_database", b"serverless_database", "storage_config", b"storage_config", "zonal_database", b"zonal_database"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assign_public_ips", b"assign_public_ips", "backup_config", b"backup_config", "database_type", b"database_type", "dedicated_database", b"dedicated_database", "deletion_protection", b"deletion_protection", "description", b"description", "folder_id", b"folder_id", "labels", b"labels", "location_id", b"location_id", "monitoring_config", b"monitoring_config", "name", b"name", "network_id", b"network_id", "regional_database", b"regional_database", "resource_preset_id", b"resource_preset_id", "scale_policy", b"scale_policy", "security_group_ids", b"security_group_ids", "serverless_database", b"serverless_database", "storage_config", b"storage_config", "subnet_ids", b"subnet_ids", "zonal_database", b"zonal_database"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["database_type", b"database_type"]) -> typing.Literal["zonal_database", "regional_database", "dedicated_database", "serverless_database"] | None: ...

global___CreateDatabaseRequest = CreateDatabaseRequest

@typing.final
class CreateDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    """Required. ID of the YDB cluster."""
    database_name: builtins.str
    """Required. Name of the creating database."""
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
        database_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id", "database_name", b"database_name"]) -> None: ...

global___CreateDatabaseMetadata = CreateDatabaseMetadata

@typing.final
class UpdateDatabaseRequest(google.protobuf.message.Message):
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
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    DATABASE_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RESOURCE_PRESET_ID_FIELD_NUMBER: builtins.int
    STORAGE_CONFIG_FIELD_NUMBER: builtins.int
    SCALE_POLICY_FIELD_NUMBER: builtins.int
    NETWORK_ID_FIELD_NUMBER: builtins.int
    SUBNET_IDS_FIELD_NUMBER: builtins.int
    ZONAL_DATABASE_FIELD_NUMBER: builtins.int
    REGIONAL_DATABASE_FIELD_NUMBER: builtins.int
    DEDICATED_DATABASE_FIELD_NUMBER: builtins.int
    SERVERLESS_DATABASE_FIELD_NUMBER: builtins.int
    ASSIGN_PUBLIC_IPS_FIELD_NUMBER: builtins.int
    LOCATION_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    BACKUP_CONFIG_FIELD_NUMBER: builtins.int
    MONITORING_CONFIG_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    SECURITY_GROUP_IDS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    database_id: builtins.str
    name: builtins.str
    description: builtins.str
    resource_preset_id: builtins.str
    network_id: builtins.str
    assign_public_ips: builtins.bool
    location_id: builtins.str
    deletion_protection: builtins.bool
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def storage_config(self) -> yandex.cloud.ydb.v1.database_pb2.StorageConfig: ...
    @property
    def scale_policy(self) -> yandex.cloud.ydb.v1.database_pb2.ScalePolicy: ...
    @property
    def subnet_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def zonal_database(self) -> yandex.cloud.ydb.v1.database_pb2.ZonalDatabase: ...
    @property
    def regional_database(self) -> yandex.cloud.ydb.v1.database_pb2.RegionalDatabase: ...
    @property
    def dedicated_database(self) -> yandex.cloud.ydb.v1.database_pb2.DedicatedDatabase: ...
    @property
    def serverless_database(self) -> yandex.cloud.ydb.v1.database_pb2.ServerlessDatabase: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    @property
    def backup_config(self) -> yandex.cloud.ydb.v1.backup_pb2.BackupConfig: ...
    @property
    def monitoring_config(self) -> yandex.cloud.ydb.v1.database_pb2.MonitoringConfig: ...
    @property
    def security_group_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        database_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        resource_preset_id: builtins.str = ...,
        storage_config: yandex.cloud.ydb.v1.database_pb2.StorageConfig | None = ...,
        scale_policy: yandex.cloud.ydb.v1.database_pb2.ScalePolicy | None = ...,
        network_id: builtins.str = ...,
        subnet_ids: collections.abc.Iterable[builtins.str] | None = ...,
        zonal_database: yandex.cloud.ydb.v1.database_pb2.ZonalDatabase | None = ...,
        regional_database: yandex.cloud.ydb.v1.database_pb2.RegionalDatabase | None = ...,
        dedicated_database: yandex.cloud.ydb.v1.database_pb2.DedicatedDatabase | None = ...,
        serverless_database: yandex.cloud.ydb.v1.database_pb2.ServerlessDatabase | None = ...,
        assign_public_ips: builtins.bool = ...,
        location_id: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        backup_config: yandex.cloud.ydb.v1.backup_pb2.BackupConfig | None = ...,
        monitoring_config: yandex.cloud.ydb.v1.database_pb2.MonitoringConfig | None = ...,
        deletion_protection: builtins.bool = ...,
        security_group_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["backup_config", b"backup_config", "database_type", b"database_type", "dedicated_database", b"dedicated_database", "monitoring_config", b"monitoring_config", "regional_database", b"regional_database", "scale_policy", b"scale_policy", "serverless_database", b"serverless_database", "storage_config", b"storage_config", "update_mask", b"update_mask", "zonal_database", b"zonal_database"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["assign_public_ips", b"assign_public_ips", "backup_config", b"backup_config", "database_id", b"database_id", "database_type", b"database_type", "dedicated_database", b"dedicated_database", "deletion_protection", b"deletion_protection", "description", b"description", "folder_id", b"folder_id", "labels", b"labels", "location_id", b"location_id", "monitoring_config", b"monitoring_config", "name", b"name", "network_id", b"network_id", "regional_database", b"regional_database", "resource_preset_id", b"resource_preset_id", "scale_policy", b"scale_policy", "security_group_ids", b"security_group_ids", "serverless_database", b"serverless_database", "storage_config", b"storage_config", "subnet_ids", b"subnet_ids", "update_mask", b"update_mask", "zonal_database", b"zonal_database"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["database_type", b"database_type"]) -> typing.Literal["zonal_database", "regional_database", "dedicated_database", "serverless_database"] | None: ...

global___UpdateDatabaseRequest = UpdateDatabaseRequest

@typing.final
class UpdateDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    database_name: builtins.str
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
        database_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id", "database_name", b"database_name"]) -> None: ...

global___UpdateDatabaseMetadata = UpdateDatabaseMetadata

@typing.final
class DeleteDatabaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id"]) -> None: ...

global___DeleteDatabaseRequest = DeleteDatabaseRequest

@typing.final
class DeleteDatabaseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_ID_FIELD_NUMBER: builtins.int
    DATABASE_NAME_FIELD_NUMBER: builtins.int
    database_id: builtins.str
    database_name: builtins.str
    def __init__(
        self,
        *,
        database_id: builtins.str = ...,
        database_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database_id", b"database_id", "database_name", b"database_name"]) -> None: ...

global___DeleteDatabaseMetadata = DeleteDatabaseMetadata
