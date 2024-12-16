# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/mysql/v1alpha/cluster_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'yandex/cloud/mdb/mysql/v1alpha/cluster_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.mdb.mysql.v1alpha import backup_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_backup__pb2
from yandex.cloud.mdb.mysql.v1alpha import cluster_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_cluster__pb2
from yandex.cloud.mdb.mysql.v1alpha.config import mysql5_7_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_config_dot_mysql5__7__pb2
from yandex.cloud.mdb.mysql.v1alpha import database_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_database__pb2
from yandex.cloud.mdb.mysql.v1alpha import user_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_user__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4yandex/cloud/mdb/mysql/v1alpha/cluster_service.proto\x12\x1eyandex.cloud.mdb.mysql.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/type/timeofday.proto\x1a yandex/cloud/api/operation.proto\x1a+yandex/cloud/mdb/mysql/v1alpha/backup.proto\x1a,yandex/cloud/mdb/mysql/v1alpha/cluster.proto\x1a\x34yandex/cloud/mdb/mysql/v1alpha/config/mysql5_7.proto\x1a-yandex/cloud/mdb/mysql/v1alpha/database.proto\x1a)yandex/cloud/mdb/mysql/v1alpha/user.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"5\n\x11GetClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x90\x01\n\x13ListClustersRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"j\n\x14ListClustersResponse\x12\x39\n\x08\x63lusters\x18\x01 \x03(\x0b\x32\'.yandex.cloud.mdb.mysql.v1alpha.Cluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xaf\x05\n\x14\x43reateClusterRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12,\n\x04name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8d\x01\n\x06labels\x18\x04 \x03(\x0b\x32@.yandex.cloud.mdb.mysql.v1alpha.CreateClusterRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12H\n\x0b\x65nvironment\x18\x05 \x01(\x0e\x32\x33.yandex.cloud.mdb.mysql.v1alpha.Cluster.Environment\x12?\n\x0b\x63onfig_spec\x18\x06 \x01(\x0b\x32*.yandex.cloud.mdb.mysql.v1alpha.ConfigSpec\x12\x44\n\x0e\x64\x61tabase_specs\x18\x07 \x03(\x0b\x32,.yandex.cloud.mdb.mysql.v1alpha.DatabaseSpec\x12<\n\nuser_specs\x18\x08 \x03(\x0b\x32(.yandex.cloud.mdb.mysql.v1alpha.UserSpec\x12<\n\nhost_specs\x18\t \x03(\x0b\x32(.yandex.cloud.mdb.mysql.v1alpha.HostSpec\x12\x1c\n\nnetwork_id\x18\n \x01(\tB\x08\x8a\xc8\x31\x04<=50\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15\x43reateClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\xb3\x03\n\x14UpdateClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8d\x01\n\x06labels\x18\x04 \x03(\x0b\x32@.yandex.cloud.mdb.mysql.v1alpha.UpdateClusterRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12?\n\x0b\x63onfig_spec\x18\x05 \x01(\x0b\x32*.yandex.cloud.mdb.mysql.v1alpha.ConfigSpec\x12(\n\x04name\x18\x06 \x01(\tB\x1a\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15UpdateClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"8\n\x14\x44\x65leteClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"+\n\x15\x44\x65leteClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"8\n\x14\x42\x61\x63kupClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"+\n\x15\x42\x61\x63kupClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\xd3\x04\n\x15RestoreClusterRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12.\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe8\xc7\x31\x01\x12$\n\x04name\x18\x04 \x01(\tB\x16\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12\x1e\n\x0b\x64\x65scription\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8e\x01\n\x06labels\x18\x06 \x03(\x0b\x32\x41.yandex.cloud.mdb.mysql.v1alpha.RestoreClusterRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12H\n\x0b\x65nvironment\x18\x07 \x01(\x0e\x32\x33.yandex.cloud.mdb.mysql.v1alpha.Cluster.Environment\x12?\n\x0b\x63onfig_spec\x18\x08 \x01(\x0b\x32*.yandex.cloud.mdb.mysql.v1alpha.ConfigSpec\x12<\n\nhost_specs\x18\t \x03(\x0b\x32(.yandex.cloud.mdb.mysql.v1alpha.HostSpec\x12\x1c\n\nnetwork_id\x18\n \x01(\tB\x08\x8a\xc8\x31\x04<=50\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x03\x10\x04\"?\n\x16RestoreClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tbackup_id\x18\x02 \x01(\t\"\xb3\x01\n\tLogRecord\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\x07message\x18\x02 \x03(\x0b\x32\x36.yandex.cloud.mdb.mysql.v1alpha.LogRecord.MessageEntry\x1a.\n\x0cMessageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9d\x03\n\x16ListClusterLogsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x15\n\rcolumn_filter\x18\x02 \x03(\t\x12X\n\x0cservice_type\x18\x03 \x01(\x0e\x32\x42.yandex.cloud.mdb.mysql.v1alpha.ListClusterLogsRequest.ServiceType\x12-\n\tfrom_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07to_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\tpage_size\x18\x06 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x07 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1e\n\x16\x61lways_next_page_token\x18\x08 \x01(\x08\"6\n\x0bServiceType\x12\x1c\n\x18SERVICE_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05MYSQL\x10\x01\"k\n\x17ListClusterLogsResponse\x12\x37\n\x04logs\x18\x01 \x03(\x0b\x32).yandex.cloud.mdb.mysql.v1alpha.LogRecord\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"~\n\x1cListClusterOperationsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"o\n\x1dListClusterOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"{\n\x19ListClusterBackupsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"n\n\x1aListClusterBackupsResponse\x12\x37\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32&.yandex.cloud.mdb.mysql.v1alpha.Backup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"y\n\x17ListClusterHostsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"h\n\x18ListClusterHostsResponse\x12\x33\n\x05hosts\x18\x01 \x03(\x0b\x32$.yandex.cloud.mdb.mysql.v1alpha.Host\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x80\x01\n\x16\x41\x64\x64\x43lusterHostsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x44\n\nhost_specs\x18\x02 \x03(\x0b\x32(.yandex.cloud.mdb.mysql.v1alpha.HostSpecB\x06\x82\xc8\x31\x02>0\"A\n\x17\x41\x64\x64\x43lusterHostsMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x12\n\nhost_names\x18\x02 \x03(\t\"b\n\x19\x44\x65leteClusterHostsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12#\n\nhost_names\x18\x02 \x03(\tB\x0f\x82\xc8\x31\x02>0\x8a\xc8\x31\x05<=253\"D\n\x1a\x44\x65leteClusterHostsMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x12\n\nhost_names\x18\x02 \x03(\t\"7\n\x13StartClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"*\n\x14StartClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"6\n\x12StopClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\")\n\x13StopClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"D\n\x1aUpdateClusterHostsMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x12\n\nhost_names\x18\x02 \x03(\t\"\\\n\x08HostSpec\x12\x19\n\x07zone_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1b\n\tsubnet_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x18\n\x10\x61ssign_public_ip\x18\x03 \x01(\x08\"\x84\x02\n\nConfigSpec\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x62\n\x10mysql_config_5_7\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.mdb.mysql.v1alpha.config.MysqlConfig5_7H\x00R\x0fmysqlConfig_5_7\x12<\n\tresources\x18\x03 \x01(\x0b\x32).yandex.cloud.mdb.mysql.v1alpha.Resources\x12\x33\n\x13\x62\x61\x63kup_window_start\x18\x04 \x01(\x0b\x32\x16.google.type.TimeOfDayB\x0e\n\x0cmysql_config2\xee\x16\n\x0e\x43lusterService\x12\x97\x01\n\x03Get\x12\x31.yandex.cloud.mdb.mysql.v1alpha.GetClusterRequest\x1a\'.yandex.cloud.mdb.mysql.v1alpha.Cluster\"4\x82\xd3\xe4\x93\x02.\x12,/managed-mysql/v1alpha/clusters/{cluster_id}\x12\x9a\x01\n\x04List\x12\x33.yandex.cloud.mdb.mysql.v1alpha.ListClustersRequest\x1a\x34.yandex.cloud.mdb.mysql.v1alpha.ListClustersResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/managed-mysql/v1alpha/clusters\x12\xb1\x01\n\x06\x43reate\x12\x34.yandex.cloud.mdb.mysql.v1alpha.CreateClusterRequest\x1a!.yandex.cloud.operation.Operation\"N\xb2\xd2* \n\x15\x43reateClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02$\"\x1f/managed-mysql/v1alpha/clusters:\x01*\x12\xbe\x01\n\x06Update\x12\x34.yandex.cloud.mdb.mysql.v1alpha.UpdateClusterRequest\x1a!.yandex.cloud.operation.Operation\"[\xb2\xd2* \n\x15UpdateClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x31\x32,/managed-mysql/v1alpha/clusters/{cluster_id}:\x01*\x12\xc9\x01\n\x06\x44\x65lete\x12\x34.yandex.cloud.mdb.mysql.v1alpha.DeleteClusterRequest\x1a!.yandex.cloud.operation.Operation\"f\xb2\xd2*.\n\x15\x44\x65leteClusterMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02.*,/managed-mysql/v1alpha/clusters/{cluster_id}\x12\xbe\x01\n\x05Start\x12\x33.yandex.cloud.mdb.mysql.v1alpha.StartClusterRequest\x1a!.yandex.cloud.operation.Operation\"]\xb2\xd2*\x1f\n\x14StartClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x34\"2/managed-mysql/v1alpha/clusters/{cluster_id}:start\x12\xba\x01\n\x04Stop\x12\x32.yandex.cloud.mdb.mysql.v1alpha.StopClusterRequest\x1a!.yandex.cloud.operation.Operation\"[\xb2\xd2*\x1e\n\x13StopClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x33\"1/managed-mysql/v1alpha/clusters/{cluster_id}:stop\x12\xc2\x01\n\x06\x42\x61\x63kup\x12\x34.yandex.cloud.mdb.mysql.v1alpha.BackupClusterRequest\x1a!.yandex.cloud.operation.Operation\"_\xb2\xd2* \n\x15\x42\x61\x63kupClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x35\"3/managed-mysql/v1alpha/clusters/{cluster_id}:backup\x12\xbc\x01\n\x07Restore\x12\x35.yandex.cloud.mdb.mysql.v1alpha.RestoreClusterRequest\x1a!.yandex.cloud.operation.Operation\"W\xb2\xd2*!\n\x16RestoreClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02,\"\'/managed-mysql/v1alpha/clusters:restore:\x01*\x12\xb6\x01\n\x08ListLogs\x12\x36.yandex.cloud.mdb.mysql.v1alpha.ListClusterLogsRequest\x1a\x37.yandex.cloud.mdb.mysql.v1alpha.ListClusterLogsResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/managed-mysql/v1alpha/clusters/{cluster_id}:logs\x12\xce\x01\n\x0eListOperations\x12<.yandex.cloud.mdb.mysql.v1alpha.ListClusterOperationsRequest\x1a=.yandex.cloud.mdb.mysql.v1alpha.ListClusterOperationsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/managed-mysql/v1alpha/clusters/{cluster_id}/operations\x12\xc2\x01\n\x0bListBackups\x12\x39.yandex.cloud.mdb.mysql.v1alpha.ListClusterBackupsRequest\x1a:.yandex.cloud.mdb.mysql.v1alpha.ListClusterBackupsResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/managed-mysql/v1alpha/clusters/{cluster_id}/backups\x12\xba\x01\n\tListHosts\x12\x37.yandex.cloud.mdb.mysql.v1alpha.ListClusterHostsRequest\x1a\x38.yandex.cloud.mdb.mysql.v1alpha.ListClusterHostsResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/managed-mysql/v1alpha/clusters/{cluster_id}/hosts\x12\xe4\x01\n\x08\x41\x64\x64Hosts\x12\x36.yandex.cloud.mdb.mysql.v1alpha.AddClusterHostsRequest\x1a!.yandex.cloud.operation.Operation\"}\xb2\xd2*0\n\x17\x41\x64\x64\x43lusterHostsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x43\">/managed-mysql/v1alpha/clusters/{cluster_id}/hosts:batchCreate:\x01*\x12\xee\x01\n\x0b\x44\x65leteHosts\x12\x39.yandex.cloud.mdb.mysql.v1alpha.DeleteClusterHostsRequest\x1a!.yandex.cloud.operation.Operation\"\x80\x01\xb2\xd2*3\n\x1a\x44\x65leteClusterHostsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x43\">/managed-mysql/v1alpha/clusters/{cluster_id}/hosts:batchDelete:\x01*Bn\n\"yandex.cloud.api.mdb.mysql.v1alphaZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha;mysqlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mysql.v1alpha.cluster_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.api.mdb.mysql.v1alphaZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha;mysql'
  _globals['_GETCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GETCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTCLUSTERSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_CREATECLUSTERREQUEST'].fields_by_name['network_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETECLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_BACKUPCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_BACKUPCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_RESTORECLUSTERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_RESTORECLUSTERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['backup_id']._loaded_options = None
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['time']._loaded_options = None
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['time']._serialized_options = b'\350\3071\001'
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*'
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_RESTORECLUSTERREQUEST'].fields_by_name['network_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LOGRECORD_MESSAGEENTRY']._loaded_options = None
  _globals['_LOGRECORD_MESSAGEENTRY']._serialized_options = b'8\001'
  _globals['_LISTCLUSTERLOGSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTCLUSTERLOGSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTCLUSTERLOGSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTERLOGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTCLUSTERLOGSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTERLOGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTEROPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTCLUSTERBACKUPSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTCLUSTERBACKUPSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTCLUSTERBACKUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTERBACKUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTCLUSTERBACKUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTERBACKUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTCLUSTERHOSTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_ADDCLUSTERHOSTSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_ADDCLUSTERHOSTSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ADDCLUSTERHOSTSREQUEST'].fields_by_name['host_specs']._loaded_options = None
  _globals['_ADDCLUSTERHOSTSREQUEST'].fields_by_name['host_specs']._serialized_options = b'\202\3101\002>0'
  _globals['_DELETECLUSTERHOSTSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETECLUSTERHOSTSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETECLUSTERHOSTSREQUEST'].fields_by_name['host_names']._loaded_options = None
  _globals['_DELETECLUSTERHOSTSREQUEST'].fields_by_name['host_names']._serialized_options = b'\202\3101\002>0\212\3101\005<=253'
  _globals['_STARTCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_STARTCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_STOPCLUSTERREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_STOPCLUSTERREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_HOSTSPEC'].fields_by_name['zone_id']._loaded_options = None
  _globals['_HOSTSPEC'].fields_by_name['zone_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_HOSTSPEC'].fields_by_name['subnet_id']._loaded_options = None
  _globals['_HOSTSPEC'].fields_by_name['subnet_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_CLUSTERSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002.\022,/managed-mysql/v1alpha/clusters/{cluster_id}'
  _globals['_CLUSTERSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/managed-mysql/v1alpha/clusters'
  _globals['_CLUSTERSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateClusterMetadata\022\007Cluster\202\323\344\223\002$\"\037/managed-mysql/v1alpha/clusters:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateClusterMetadata\022\007Cluster\202\323\344\223\00212,/managed-mysql/v1alpha/clusters/{cluster_id}:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteClusterMetadata\022\025google.protobuf.Empty\202\323\344\223\002.*,/managed-mysql/v1alpha/clusters/{cluster_id}'
  _globals['_CLUSTERSERVICE'].methods_by_name['Start']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Start']._serialized_options = b'\262\322*\037\n\024StartClusterMetadata\022\007Cluster\202\323\344\223\0024\"2/managed-mysql/v1alpha/clusters/{cluster_id}:start'
  _globals['_CLUSTERSERVICE'].methods_by_name['Stop']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Stop']._serialized_options = b'\262\322*\036\n\023StopClusterMetadata\022\007Cluster\202\323\344\223\0023\"1/managed-mysql/v1alpha/clusters/{cluster_id}:stop'
  _globals['_CLUSTERSERVICE'].methods_by_name['Backup']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Backup']._serialized_options = b'\262\322* \n\025BackupClusterMetadata\022\007Cluster\202\323\344\223\0025\"3/managed-mysql/v1alpha/clusters/{cluster_id}:backup'
  _globals['_CLUSTERSERVICE'].methods_by_name['Restore']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['Restore']._serialized_options = b'\262\322*!\n\026RestoreClusterMetadata\022\007Cluster\202\323\344\223\002,\"\'/managed-mysql/v1alpha/clusters:restore:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListLogs']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListLogs']._serialized_options = b'\202\323\344\223\0023\0221/managed-mysql/v1alpha/clusters/{cluster_id}:logs'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0029\0227/managed-mysql/v1alpha/clusters/{cluster_id}/operations'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListBackups']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListBackups']._serialized_options = b'\202\323\344\223\0026\0224/managed-mysql/v1alpha/clusters/{cluster_id}/backups'
  _globals['_CLUSTERSERVICE'].methods_by_name['ListHosts']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['ListHosts']._serialized_options = b'\202\323\344\223\0024\0222/managed-mysql/v1alpha/clusters/{cluster_id}/hosts'
  _globals['_CLUSTERSERVICE'].methods_by_name['AddHosts']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['AddHosts']._serialized_options = b'\262\322*0\n\027AddClusterHostsMetadata\022\025google.protobuf.Empty\202\323\344\223\002C\">/managed-mysql/v1alpha/clusters/{cluster_id}/hosts:batchCreate:\001*'
  _globals['_CLUSTERSERVICE'].methods_by_name['DeleteHosts']._loaded_options = None
  _globals['_CLUSTERSERVICE'].methods_by_name['DeleteHosts']._serialized_options = b'\262\322*3\n\032DeleteClusterHostsMetadata\022\025google.protobuf.Empty\202\323\344\223\002C\">/managed-mysql/v1alpha/clusters/{cluster_id}/hosts:batchDelete:\001*'
  _globals['_GETCLUSTERREQUEST']._serialized_start=554
  _globals['_GETCLUSTERREQUEST']._serialized_end=607
  _globals['_LISTCLUSTERSREQUEST']._serialized_start=610
  _globals['_LISTCLUSTERSREQUEST']._serialized_end=754
  _globals['_LISTCLUSTERSRESPONSE']._serialized_start=756
  _globals['_LISTCLUSTERSRESPONSE']._serialized_end=862
  _globals['_CREATECLUSTERREQUEST']._serialized_start=865
  _globals['_CREATECLUSTERREQUEST']._serialized_end=1552
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_start=1507
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_end=1552
  _globals['_CREATECLUSTERMETADATA']._serialized_start=1554
  _globals['_CREATECLUSTERMETADATA']._serialized_end=1597
  _globals['_UPDATECLUSTERREQUEST']._serialized_start=1600
  _globals['_UPDATECLUSTERREQUEST']._serialized_end=2035
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_start=1507
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_end=1552
  _globals['_UPDATECLUSTERMETADATA']._serialized_start=2037
  _globals['_UPDATECLUSTERMETADATA']._serialized_end=2080
  _globals['_DELETECLUSTERREQUEST']._serialized_start=2082
  _globals['_DELETECLUSTERREQUEST']._serialized_end=2138
  _globals['_DELETECLUSTERMETADATA']._serialized_start=2140
  _globals['_DELETECLUSTERMETADATA']._serialized_end=2183
  _globals['_BACKUPCLUSTERREQUEST']._serialized_start=2185
  _globals['_BACKUPCLUSTERREQUEST']._serialized_end=2241
  _globals['_BACKUPCLUSTERMETADATA']._serialized_start=2243
  _globals['_BACKUPCLUSTERMETADATA']._serialized_end=2286
  _globals['_RESTORECLUSTERREQUEST']._serialized_start=2289
  _globals['_RESTORECLUSTERREQUEST']._serialized_end=2884
  _globals['_RESTORECLUSTERREQUEST_LABELSENTRY']._serialized_start=1507
  _globals['_RESTORECLUSTERREQUEST_LABELSENTRY']._serialized_end=1552
  _globals['_RESTORECLUSTERMETADATA']._serialized_start=2886
  _globals['_RESTORECLUSTERMETADATA']._serialized_end=2949
  _globals['_LOGRECORD']._serialized_start=2952
  _globals['_LOGRECORD']._serialized_end=3131
  _globals['_LOGRECORD_MESSAGEENTRY']._serialized_start=3085
  _globals['_LOGRECORD_MESSAGEENTRY']._serialized_end=3131
  _globals['_LISTCLUSTERLOGSREQUEST']._serialized_start=3134
  _globals['_LISTCLUSTERLOGSREQUEST']._serialized_end=3547
  _globals['_LISTCLUSTERLOGSREQUEST_SERVICETYPE']._serialized_start=3493
  _globals['_LISTCLUSTERLOGSREQUEST_SERVICETYPE']._serialized_end=3547
  _globals['_LISTCLUSTERLOGSRESPONSE']._serialized_start=3549
  _globals['_LISTCLUSTERLOGSRESPONSE']._serialized_end=3656
  _globals['_LISTCLUSTEROPERATIONSREQUEST']._serialized_start=3658
  _globals['_LISTCLUSTEROPERATIONSREQUEST']._serialized_end=3784
  _globals['_LISTCLUSTEROPERATIONSRESPONSE']._serialized_start=3786
  _globals['_LISTCLUSTEROPERATIONSRESPONSE']._serialized_end=3897
  _globals['_LISTCLUSTERBACKUPSREQUEST']._serialized_start=3899
  _globals['_LISTCLUSTERBACKUPSREQUEST']._serialized_end=4022
  _globals['_LISTCLUSTERBACKUPSRESPONSE']._serialized_start=4024
  _globals['_LISTCLUSTERBACKUPSRESPONSE']._serialized_end=4134
  _globals['_LISTCLUSTERHOSTSREQUEST']._serialized_start=4136
  _globals['_LISTCLUSTERHOSTSREQUEST']._serialized_end=4257
  _globals['_LISTCLUSTERHOSTSRESPONSE']._serialized_start=4259
  _globals['_LISTCLUSTERHOSTSRESPONSE']._serialized_end=4363
  _globals['_ADDCLUSTERHOSTSREQUEST']._serialized_start=4366
  _globals['_ADDCLUSTERHOSTSREQUEST']._serialized_end=4494
  _globals['_ADDCLUSTERHOSTSMETADATA']._serialized_start=4496
  _globals['_ADDCLUSTERHOSTSMETADATA']._serialized_end=4561
  _globals['_DELETECLUSTERHOSTSREQUEST']._serialized_start=4563
  _globals['_DELETECLUSTERHOSTSREQUEST']._serialized_end=4661
  _globals['_DELETECLUSTERHOSTSMETADATA']._serialized_start=4663
  _globals['_DELETECLUSTERHOSTSMETADATA']._serialized_end=4731
  _globals['_STARTCLUSTERREQUEST']._serialized_start=4733
  _globals['_STARTCLUSTERREQUEST']._serialized_end=4788
  _globals['_STARTCLUSTERMETADATA']._serialized_start=4790
  _globals['_STARTCLUSTERMETADATA']._serialized_end=4832
  _globals['_STOPCLUSTERREQUEST']._serialized_start=4834
  _globals['_STOPCLUSTERREQUEST']._serialized_end=4888
  _globals['_STOPCLUSTERMETADATA']._serialized_start=4890
  _globals['_STOPCLUSTERMETADATA']._serialized_end=4931
  _globals['_UPDATECLUSTERHOSTSMETADATA']._serialized_start=4933
  _globals['_UPDATECLUSTERHOSTSMETADATA']._serialized_end=5001
  _globals['_HOSTSPEC']._serialized_start=5003
  _globals['_HOSTSPEC']._serialized_end=5095
  _globals['_CONFIGSPEC']._serialized_start=5098
  _globals['_CONFIGSPEC']._serialized_end=5358
  _globals['_CLUSTERSERVICE']._serialized_start=5361
  _globals['_CLUSTERSERVICE']._serialized_end=8287
# @@protoc_insertion_point(module_scope)
