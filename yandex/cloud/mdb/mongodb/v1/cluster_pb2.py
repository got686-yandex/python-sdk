# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/mongodb/v1/cluster.proto
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
    'yandex/cloud/mdb/mongodb/v1/cluster.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
from yandex.cloud.mdb.mongodb.v1.config import mongodb_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_config_dot_mongodb__pb2
from yandex.cloud.mdb.mongodb.v1.config import mongodb3_6_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_config_dot_mongodb3__6__pb2
from yandex.cloud.mdb.mongodb.v1.config import mongodb4_0_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_config_dot_mongodb4__0__pb2
from yandex.cloud.mdb.mongodb.v1.config import mongodb4_2_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_config_dot_mongodb4__2__pb2
from yandex.cloud.mdb.mongodb.v1.config import mongodb4_4_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_config_dot_mongodb4__4__pb2
from yandex.cloud.mdb.mongodb.v1.config import mongodb4_4_enterprise_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_config_dot_mongodb4__4__enterprise__pb2
from yandex.cloud.mdb.mongodb.v1.config import mongodb5_0_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_config_dot_mongodb5__0__pb2
from yandex.cloud.mdb.mongodb.v1.config import mongodb5_0_enterprise_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_config_dot_mongodb5__0__enterprise__pb2
from yandex.cloud.mdb.mongodb.v1.config import mongodb6_0_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_config_dot_mongodb6__0__pb2
from yandex.cloud.mdb.mongodb.v1.config import mongodb6_0_enterprise_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_config_dot_mongodb6__0__enterprise__pb2
from yandex.cloud.mdb.mongodb.v1 import maintenance_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_maintenance__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/mdb/mongodb/v1/cluster.proto\x12\x1byandex.cloud.mdb.mongodb.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/type/timeofday.proto\x1a\x30yandex/cloud/mdb/mongodb/v1/config/mongodb.proto\x1a\x33yandex/cloud/mdb/mongodb/v1/config/mongodb3_6.proto\x1a\x33yandex/cloud/mdb/mongodb/v1/config/mongodb4_0.proto\x1a\x33yandex/cloud/mdb/mongodb/v1/config/mongodb4_2.proto\x1a\x33yandex/cloud/mdb/mongodb/v1/config/mongodb4_4.proto\x1a>yandex/cloud/mdb/mongodb/v1/config/mongodb4_4_enterprise.proto\x1a\x33yandex/cloud/mdb/mongodb/v1/config/mongodb5_0.proto\x1a>yandex/cloud/mdb/mongodb/v1/config/mongodb5_0_enterprise.proto\x1a\x33yandex/cloud/mdb/mongodb/v1/config/mongodb6_0.proto\x1a>yandex/cloud/mdb/mongodb/v1/config/mongodb6_0_enterprise.proto\x1a-yandex/cloud/mdb/mongodb/v1/maintenance.proto\x1a\x1dyandex/cloud/validation.proto\"\xa5\x08\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12@\n\x06labels\x18\x06 \x03(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.Cluster.LabelsEntry\x12\x45\n\x0b\x65nvironment\x18\x07 \x01(\x0e\x32\x30.yandex.cloud.mdb.mongodb.v1.Cluster.Environment\x12;\n\nmonitoring\x18\x08 \x03(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.Monitoring\x12:\n\x06\x63onfig\x18\t \x01(\x0b\x32*.yandex.cloud.mdb.mongodb.v1.ClusterConfig\x12\x12\n\nnetwork_id\x18\n \x01(\t\x12;\n\x06health\x18\x0b \x01(\x0e\x32+.yandex.cloud.mdb.mongodb.v1.Cluster.Health\x12;\n\x06status\x18\x0c \x01(\x0e\x32+.yandex.cloud.mdb.mongodb.v1.Cluster.Status\x12\x0f\n\x07sharded\x18\r \x01(\x08\x12J\n\x12maintenance_window\x18\x0e \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.MaintenanceWindow\x12L\n\x11planned_operation\x18\x0f \x01(\x0b\x32\x31.yandex.cloud.mdb.mongodb.v1.MaintenanceOperation\x12\x1a\n\x12security_group_ids\x18\x10 \x03(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x11 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0b\x45nvironment\x12\x1b\n\x17\x45NVIRONMENT_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\r\n\tPRESTABLE\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"y\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08STARTING\x10\x07\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\xb4\t\n\rClusterConfig\x12\x0f\n\x07version\x18\x01 \x01(\t\x12%\n\x1d\x66\x65\x61ture_compatibility_version\x18\x05 \x01(\t\x12K\n\x0bmongodb_3_6\x18\x02 \x01(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.Mongodb3_6H\x00R\x0bmongodb_3_6\x12K\n\x0bmongodb_4_0\x18\x04 \x01(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.Mongodb4_0H\x00R\x0bmongodb_4_0\x12K\n\x0bmongodb_4_2\x18\x07 \x01(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.Mongodb4_2H\x00R\x0bmongodb_4_2\x12K\n\x0bmongodb_4_4\x18\x08 \x01(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.Mongodb4_4H\x00R\x0bmongodb_4_4\x12K\n\x0bmongodb_5_0\x18\n \x01(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.Mongodb5_0H\x00R\x0bmongodb_5_0\x12K\n\x0bmongodb_6_0\x18\x0e \x01(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.Mongodb6_0H\x00R\x0bmongodb_6_0\x12l\n\x16mongodb_4_4_enterprise\x18\x0b \x01(\x0b\x32\x32.yandex.cloud.mdb.mongodb.v1.Mongodb4_4_enterpriseH\x00R\x16mongodb_4_4_enterprise\x12l\n\x16mongodb_5_0_enterprise\x18\x0c \x01(\x0b\x32\x32.yandex.cloud.mdb.mongodb.v1.Mongodb5_0_enterpriseH\x00R\x16mongodb_5_0_enterprise\x12l\n\x16mongodb_6_0_enterprise\x18\x0f \x01(\x0b\x32\x32.yandex.cloud.mdb.mongodb.v1.Mongodb6_0_enterpriseH\x00R\x16mongodb_6_0_enterprise\x12\x33\n\x13\x62\x61\x63kup_window_start\x18\x03 \x01(\x0b\x32\x16.google.type.TimeOfDay\x12>\n\x19\x62\x61\x63kup_retain_period_days\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12Z\n\x17performance_diagnostics\x18\r \x01(\x0b\x32\x39.yandex.cloud.mdb.mongodb.v1.PerformanceDiagnosticsConfig\x12\x33\n\x06\x61\x63\x63\x65ss\x18\x06 \x01(\x0b\x32#.yandex.cloud.mdb.mongodb.v1.Access\x12<\n\x0emongodb_config\x18\x13 \x01(\x0b\x32$.yandex.cloud.mdb.mongodb.v1.MongodbB\t\n\x07mongodbJ\x04\x08\x10\x10\x13\"\xf6\t\n\nMongodb3_6\x12>\n\x06mongod\x18\x01 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb3_6.Mongod\x12\x42\n\x08mongocfg\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.Mongodb3_6.MongoCfg\x12>\n\x06mongos\x18\x03 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb3_6.Mongos\x12\x46\n\nmongoinfra\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.mdb.mongodb.v1.Mongodb3_6.MongoInfra\x1a\xdc\x01\n\x06Mongod\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet3_6\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xe0\x01\n\x08MongoCfg\x12H\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet3_6\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xdc\x01\n\x06Mongos\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet3_6\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xba\x02\n\nMongoInfra\x12M\n\rconfig_mongos\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet3_6\x12Q\n\x0f\x63onfig_mongocfg\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet3_6\x12\x39\n\tresources\x18\x03 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\"\xf6\t\n\nMongodb4_0\x12>\n\x06mongod\x18\x01 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb4_0.Mongod\x12\x42\n\x08mongocfg\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.Mongodb4_0.MongoCfg\x12>\n\x06mongos\x18\x03 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb4_0.Mongos\x12\x46\n\nmongoinfra\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.mdb.mongodb.v1.Mongodb4_0.MongoInfra\x1a\xdc\x01\n\x06Mongod\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet4_0\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xe0\x01\n\x08MongoCfg\x12H\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet4_0\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xdc\x01\n\x06Mongos\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet4_0\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xba\x02\n\nMongoInfra\x12M\n\rconfig_mongos\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet4_0\x12Q\n\x0f\x63onfig_mongocfg\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet4_0\x12\x39\n\tresources\x18\x03 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\"\xf6\t\n\nMongodb4_2\x12>\n\x06mongod\x18\x01 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb4_2.Mongod\x12\x42\n\x08mongocfg\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.Mongodb4_2.MongoCfg\x12>\n\x06mongos\x18\x03 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb4_2.Mongos\x12\x46\n\nmongoinfra\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.mdb.mongodb.v1.Mongodb4_2.MongoInfra\x1a\xdc\x01\n\x06Mongod\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet4_2\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xe0\x01\n\x08MongoCfg\x12H\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet4_2\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xdc\x01\n\x06Mongos\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet4_2\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xba\x02\n\nMongoInfra\x12M\n\rconfig_mongos\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet4_2\x12Q\n\x0f\x63onfig_mongocfg\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet4_2\x12\x39\n\tresources\x18\x03 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\"\xf6\t\n\nMongodb4_4\x12>\n\x06mongod\x18\x01 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb4_4.Mongod\x12\x42\n\x08mongocfg\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.Mongodb4_4.MongoCfg\x12>\n\x06mongos\x18\x03 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb4_4.Mongos\x12\x46\n\nmongoinfra\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.mdb.mongodb.v1.Mongodb4_4.MongoInfra\x1a\xdc\x01\n\x06Mongod\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet4_4\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xe0\x01\n\x08MongoCfg\x12H\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet4_4\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xdc\x01\n\x06Mongos\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet4_4\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xba\x02\n\nMongoInfra\x12M\n\rconfig_mongos\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet4_4\x12Q\n\x0f\x63onfig_mongocfg\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet4_4\x12\x39\n\tresources\x18\x03 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\"\xe4\n\n\x15Mongodb4_4_enterprise\x12I\n\x06mongod\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.mdb.mongodb.v1.Mongodb4_4_enterprise.Mongod\x12M\n\x08mongocfg\x18\x02 \x01(\x0b\x32;.yandex.cloud.mdb.mongodb.v1.Mongodb4_4_enterprise.MongoCfg\x12I\n\x06mongos\x18\x03 \x01(\x0b\x32\x39.yandex.cloud.mdb.mongodb.v1.Mongodb4_4_enterprise.Mongos\x12Q\n\nmongoinfra\x18\x04 \x01(\x0b\x32=.yandex.cloud.mdb.mongodb.v1.Mongodb4_4_enterprise.MongoInfra\x1a\xe7\x01\n\x06Mongod\x12Q\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x41.yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet4_4_enterprise\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xeb\x01\n\x08MongoCfg\x12S\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x43.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet4_4_enterprise\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xe7\x01\n\x06Mongos\x12Q\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x41.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet4_4_enterprise\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xd0\x02\n\nMongoInfra\x12X\n\rconfig_mongos\x18\x01 \x01(\x0b\x32\x41.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet4_4_enterprise\x12\\\n\x0f\x63onfig_mongocfg\x18\x02 \x01(\x0b\x32\x43.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet4_4_enterprise\x12\x39\n\tresources\x18\x03 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\"\xf6\t\n\nMongodb5_0\x12>\n\x06mongod\x18\x01 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb5_0.Mongod\x12\x42\n\x08mongocfg\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.Mongodb5_0.MongoCfg\x12>\n\x06mongos\x18\x03 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb5_0.Mongos\x12\x46\n\nmongoinfra\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.mdb.mongodb.v1.Mongodb5_0.MongoInfra\x1a\xdc\x01\n\x06Mongod\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet5_0\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xe0\x01\n\x08MongoCfg\x12H\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet5_0\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xdc\x01\n\x06Mongos\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet5_0\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xba\x02\n\nMongoInfra\x12M\n\rconfig_mongos\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet5_0\x12Q\n\x0f\x63onfig_mongocfg\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet5_0\x12\x39\n\tresources\x18\x03 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\"\xe4\n\n\x15Mongodb5_0_enterprise\x12I\n\x06mongod\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.mdb.mongodb.v1.Mongodb5_0_enterprise.Mongod\x12M\n\x08mongocfg\x18\x02 \x01(\x0b\x32;.yandex.cloud.mdb.mongodb.v1.Mongodb5_0_enterprise.MongoCfg\x12I\n\x06mongos\x18\x03 \x01(\x0b\x32\x39.yandex.cloud.mdb.mongodb.v1.Mongodb5_0_enterprise.Mongos\x12Q\n\nmongoinfra\x18\x04 \x01(\x0b\x32=.yandex.cloud.mdb.mongodb.v1.Mongodb5_0_enterprise.MongoInfra\x1a\xe7\x01\n\x06Mongod\x12Q\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x41.yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet5_0_enterprise\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xeb\x01\n\x08MongoCfg\x12S\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x43.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet5_0_enterprise\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xe7\x01\n\x06Mongos\x12Q\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x41.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet5_0_enterprise\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xd0\x02\n\nMongoInfra\x12X\n\rconfig_mongos\x18\x01 \x01(\x0b\x32\x41.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet5_0_enterprise\x12\\\n\x0f\x63onfig_mongocfg\x18\x02 \x01(\x0b\x32\x43.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet5_0_enterprise\x12\x39\n\tresources\x18\x03 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\"\xf6\t\n\nMongodb6_0\x12>\n\x06mongod\x18\x01 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb6_0.Mongod\x12\x42\n\x08mongocfg\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.Mongodb6_0.MongoCfg\x12>\n\x06mongos\x18\x03 \x01(\x0b\x32..yandex.cloud.mdb.mongodb.v1.Mongodb6_0.Mongos\x12\x46\n\nmongoinfra\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.mdb.mongodb.v1.Mongodb6_0.MongoInfra\x1a\xdc\x01\n\x06Mongod\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet6_0\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xe0\x01\n\x08MongoCfg\x12H\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet6_0\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xdc\x01\n\x06Mongos\x12\x46\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet6_0\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xba\x02\n\nMongoInfra\x12M\n\rconfig_mongos\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet6_0\x12Q\n\x0f\x63onfig_mongocfg\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet6_0\x12\x39\n\tresources\x18\x03 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\"\xe4\n\n\x15Mongodb6_0_enterprise\x12I\n\x06mongod\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.mdb.mongodb.v1.Mongodb6_0_enterprise.Mongod\x12M\n\x08mongocfg\x18\x02 \x01(\x0b\x32;.yandex.cloud.mdb.mongodb.v1.Mongodb6_0_enterprise.MongoCfg\x12I\n\x06mongos\x18\x03 \x01(\x0b\x32\x39.yandex.cloud.mdb.mongodb.v1.Mongodb6_0_enterprise.Mongos\x12Q\n\nmongoinfra\x18\x04 \x01(\x0b\x32=.yandex.cloud.mdb.mongodb.v1.Mongodb6_0_enterprise.MongoInfra\x1a\xe7\x01\n\x06Mongod\x12Q\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x41.yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet6_0_enterprise\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xeb\x01\n\x08MongoCfg\x12S\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x43.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet6_0_enterprise\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xe7\x01\n\x06Mongos\x12Q\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x41.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet6_0_enterprise\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xd0\x02\n\nMongoInfra\x12X\n\rconfig_mongos\x18\x01 \x01(\x0b\x32\x41.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet6_0_enterprise\x12\\\n\x0f\x63onfig_mongocfg\x18\x02 \x01(\x0b\x32\x43.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet6_0_enterprise\x12\x39\n\tresources\x18\x03 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\"\xd8\t\n\x07Mongodb\x12;\n\x06mongod\x18\x01 \x01(\x0b\x32+.yandex.cloud.mdb.mongodb.v1.Mongodb.Mongod\x12?\n\x08mongocfg\x18\x02 \x01(\x0b\x32-.yandex.cloud.mdb.mongodb.v1.Mongodb.MongoCfg\x12;\n\x06mongos\x18\x03 \x01(\x0b\x32+.yandex.cloud.mdb.mongodb.v1.Mongodb.Mongos\x12\x43\n\nmongoinfra\x18\x04 \x01(\x0b\x32/.yandex.cloud.mdb.mongodb.v1.Mongodb.MongoInfra\x1a\xd9\x01\n\x06Mongod\x12\x43\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xdd\x01\n\x08MongoCfg\x12\x45\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x35.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xd9\x01\n\x06Mongos\x12\x43\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet\x12\x39\n\tresources\x18\x02 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\x1a\xb4\x02\n\nMongoInfra\x12J\n\rconfig_mongos\x18\x01 \x01(\x0b\x32\x33.yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet\x12N\n\x0f\x63onfig_mongocfg\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet\x12\x39\n\tresources\x18\x03 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12O\n\x15\x64isk_size_autoscaling\x18\x04 \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.DiskSizeAutoscaling\")\n\x05Shard\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\"\xf3\x06\n\x04Host\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\t\x12\x39\n\tresources\x18\x04 \x01(\x0b\x32&.yandex.cloud.mdb.mongodb.v1.Resources\x12\x34\n\x04role\x18\x05 \x01(\x0e\x32&.yandex.cloud.mdb.mongodb.v1.Host.Role\x12\x38\n\x06health\x18\x06 \x01(\x0e\x32(.yandex.cloud.mdb.mongodb.v1.Host.Health\x12\x36\n\x08services\x18\x07 \x03(\x0b\x32$.yandex.cloud.mdb.mongodb.v1.Service\x12\x11\n\tsubnet_id\x18\x08 \x01(\t\x12\x18\n\x10\x61ssign_public_ip\x18\t \x01(\x08\x12\x12\n\nshard_name\x18\n \x01(\t\x12\x34\n\x04type\x18\x0b \x01(\x0e\x32&.yandex.cloud.mdb.mongodb.v1.Host.Type\x12I\n\x0fhost_parameters\x18\x0c \x01(\x0b\x32\x30.yandex.cloud.mdb.mongodb.v1.Host.HostParameters\x1a\xc7\x01\n\x0eHostParameters\x12\x0e\n\x06hidden\x18\x01 \x01(\x08\x12\x1c\n\x14secondary_delay_secs\x18\x02 \x01(\x03\x12\x10\n\x08priority\x18\x03 \x01(\x01\x12H\n\x04tags\x18\x04 \x03(\x0b\x32:.yandex.cloud.mdb.mongodb.v1.Host.HostParameters.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"R\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06MONGOD\x10\x01\x12\n\n\x06MONGOS\x10\x02\x12\x0c\n\x08MONGOCFG\x10\x03\x12\x0e\n\nMONGOINFRA\x10\x04\"4\n\x04Role\x12\x10\n\x0cROLE_UNKNOWN\x10\x00\x12\x0b\n\x07PRIMARY\x10\x01\x12\r\n\tSECONDARY\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"\xf6\x01\n\x07Service\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32).yandex.cloud.mdb.mongodb.v1.Service.Type\x12;\n\x06health\x18\x02 \x01(\x0e\x32+.yandex.cloud.mdb.mongodb.v1.Service.Health\"B\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06MONGOD\x10\x01\x12\n\n\x06MONGOS\x10\x02\x12\x0c\n\x08MONGOCFG\x10\x03\"1\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\"P\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\x12\x14\n\x0c\x64isk_type_id\x18\x03 \x01(\t\"C\n\x06\x41\x63\x63\x65ss\x12\x11\n\tdata_lens\x18\x01 \x01(\x08\x12\x0f\n\x07web_sql\x18\x02 \x01(\x08\x12\x15\n\rdata_transfer\x18\x03 \x01(\x08\"9\n\x1cPerformanceDiagnosticsConfig\x12\x19\n\x11profiling_enabled\x18\x01 \x01(\x08\"\xe7\x01\n\x13\x44iskSizeAutoscaling\x12K\n\x17planned_usage_threshold\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xe8\xc7\x31\x00\xfa\xc7\x31\x05\x30-100\x12M\n\x19\x65mergency_usage_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xe8\xc7\x31\x00\xfa\xc7\x31\x05\x30-100\x12\x34\n\x0f\x64isk_size_limit\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueBj\n\x1fyandex.cloud.api.mdb.mongodb.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1;mongodbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mongodb.v1.cluster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037yandex.cloud.api.mdb.mongodb.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1;mongodb'
  _globals['_CLUSTER_LABELSENTRY']._loaded_options = None
  _globals['_CLUSTER_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_HOST_HOSTPARAMETERS_TAGSENTRY']._loaded_options = None
  _globals['_HOST_HOSTPARAMETERS_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_DISKSIZEAUTOSCALING'].fields_by_name['planned_usage_threshold']._loaded_options = None
  _globals['_DISKSIZEAUTOSCALING'].fields_by_name['planned_usage_threshold']._serialized_options = b'\350\3071\000\372\3071\0050-100'
  _globals['_DISKSIZEAUTOSCALING'].fields_by_name['emergency_usage_threshold']._loaded_options = None
  _globals['_DISKSIZEAUTOSCALING'].fields_by_name['emergency_usage_threshold']._serialized_options = b'\350\3071\000\372\3071\0050-100'
  _globals['_CLUSTER']._serialized_start=807
  _globals['_CLUSTER']._serialized_end=1868
  _globals['_CLUSTER_LABELSENTRY']._serialized_start=1560
  _globals['_CLUSTER_LABELSENTRY']._serialized_end=1605
  _globals['_CLUSTER_ENVIRONMENT']._serialized_start=1607
  _globals['_CLUSTER_ENVIRONMENT']._serialized_end=1680
  _globals['_CLUSTER_HEALTH']._serialized_start=1682
  _globals['_CLUSTER_HEALTH']._serialized_end=1745
  _globals['_CLUSTER_STATUS']._serialized_start=1747
  _globals['_CLUSTER_STATUS']._serialized_end=1868
  _globals['_MONITORING']._serialized_start=1870
  _globals['_MONITORING']._serialized_end=1931
  _globals['_CLUSTERCONFIG']._serialized_start=1934
  _globals['_CLUSTERCONFIG']._serialized_end=3138
  _globals['_MONGODB3_6']._serialized_start=3141
  _globals['_MONGODB3_6']._serialized_end=4411
  _globals['_MONGODB3_6_MONGOD']._serialized_start=3424
  _globals['_MONGODB3_6_MONGOD']._serialized_end=3644
  _globals['_MONGODB3_6_MONGOCFG']._serialized_start=3647
  _globals['_MONGODB3_6_MONGOCFG']._serialized_end=3871
  _globals['_MONGODB3_6_MONGOS']._serialized_start=3874
  _globals['_MONGODB3_6_MONGOS']._serialized_end=4094
  _globals['_MONGODB3_6_MONGOINFRA']._serialized_start=4097
  _globals['_MONGODB3_6_MONGOINFRA']._serialized_end=4411
  _globals['_MONGODB4_0']._serialized_start=4414
  _globals['_MONGODB4_0']._serialized_end=5684
  _globals['_MONGODB4_0_MONGOD']._serialized_start=4697
  _globals['_MONGODB4_0_MONGOD']._serialized_end=4917
  _globals['_MONGODB4_0_MONGOCFG']._serialized_start=4920
  _globals['_MONGODB4_0_MONGOCFG']._serialized_end=5144
  _globals['_MONGODB4_0_MONGOS']._serialized_start=5147
  _globals['_MONGODB4_0_MONGOS']._serialized_end=5367
  _globals['_MONGODB4_0_MONGOINFRA']._serialized_start=5370
  _globals['_MONGODB4_0_MONGOINFRA']._serialized_end=5684
  _globals['_MONGODB4_2']._serialized_start=5687
  _globals['_MONGODB4_2']._serialized_end=6957
  _globals['_MONGODB4_2_MONGOD']._serialized_start=5970
  _globals['_MONGODB4_2_MONGOD']._serialized_end=6190
  _globals['_MONGODB4_2_MONGOCFG']._serialized_start=6193
  _globals['_MONGODB4_2_MONGOCFG']._serialized_end=6417
  _globals['_MONGODB4_2_MONGOS']._serialized_start=6420
  _globals['_MONGODB4_2_MONGOS']._serialized_end=6640
  _globals['_MONGODB4_2_MONGOINFRA']._serialized_start=6643
  _globals['_MONGODB4_2_MONGOINFRA']._serialized_end=6957
  _globals['_MONGODB4_4']._serialized_start=6960
  _globals['_MONGODB4_4']._serialized_end=8230
  _globals['_MONGODB4_4_MONGOD']._serialized_start=7243
  _globals['_MONGODB4_4_MONGOD']._serialized_end=7463
  _globals['_MONGODB4_4_MONGOCFG']._serialized_start=7466
  _globals['_MONGODB4_4_MONGOCFG']._serialized_end=7690
  _globals['_MONGODB4_4_MONGOS']._serialized_start=7693
  _globals['_MONGODB4_4_MONGOS']._serialized_end=7913
  _globals['_MONGODB4_4_MONGOINFRA']._serialized_start=7916
  _globals['_MONGODB4_4_MONGOINFRA']._serialized_end=8230
  _globals['_MONGODB4_4_ENTERPRISE']._serialized_start=8233
  _globals['_MONGODB4_4_ENTERPRISE']._serialized_end=9613
  _globals['_MONGODB4_4_ENTERPRISE_MONGOD']._serialized_start=8571
  _globals['_MONGODB4_4_ENTERPRISE_MONGOD']._serialized_end=8802
  _globals['_MONGODB4_4_ENTERPRISE_MONGOCFG']._serialized_start=8805
  _globals['_MONGODB4_4_ENTERPRISE_MONGOCFG']._serialized_end=9040
  _globals['_MONGODB4_4_ENTERPRISE_MONGOS']._serialized_start=9043
  _globals['_MONGODB4_4_ENTERPRISE_MONGOS']._serialized_end=9274
  _globals['_MONGODB4_4_ENTERPRISE_MONGOINFRA']._serialized_start=9277
  _globals['_MONGODB4_4_ENTERPRISE_MONGOINFRA']._serialized_end=9613
  _globals['_MONGODB5_0']._serialized_start=9616
  _globals['_MONGODB5_0']._serialized_end=10886
  _globals['_MONGODB5_0_MONGOD']._serialized_start=9899
  _globals['_MONGODB5_0_MONGOD']._serialized_end=10119
  _globals['_MONGODB5_0_MONGOCFG']._serialized_start=10122
  _globals['_MONGODB5_0_MONGOCFG']._serialized_end=10346
  _globals['_MONGODB5_0_MONGOS']._serialized_start=10349
  _globals['_MONGODB5_0_MONGOS']._serialized_end=10569
  _globals['_MONGODB5_0_MONGOINFRA']._serialized_start=10572
  _globals['_MONGODB5_0_MONGOINFRA']._serialized_end=10886
  _globals['_MONGODB5_0_ENTERPRISE']._serialized_start=10889
  _globals['_MONGODB5_0_ENTERPRISE']._serialized_end=12269
  _globals['_MONGODB5_0_ENTERPRISE_MONGOD']._serialized_start=11227
  _globals['_MONGODB5_0_ENTERPRISE_MONGOD']._serialized_end=11458
  _globals['_MONGODB5_0_ENTERPRISE_MONGOCFG']._serialized_start=11461
  _globals['_MONGODB5_0_ENTERPRISE_MONGOCFG']._serialized_end=11696
  _globals['_MONGODB5_0_ENTERPRISE_MONGOS']._serialized_start=11699
  _globals['_MONGODB5_0_ENTERPRISE_MONGOS']._serialized_end=11930
  _globals['_MONGODB5_0_ENTERPRISE_MONGOINFRA']._serialized_start=11933
  _globals['_MONGODB5_0_ENTERPRISE_MONGOINFRA']._serialized_end=12269
  _globals['_MONGODB6_0']._serialized_start=12272
  _globals['_MONGODB6_0']._serialized_end=13542
  _globals['_MONGODB6_0_MONGOD']._serialized_start=12555
  _globals['_MONGODB6_0_MONGOD']._serialized_end=12775
  _globals['_MONGODB6_0_MONGOCFG']._serialized_start=12778
  _globals['_MONGODB6_0_MONGOCFG']._serialized_end=13002
  _globals['_MONGODB6_0_MONGOS']._serialized_start=13005
  _globals['_MONGODB6_0_MONGOS']._serialized_end=13225
  _globals['_MONGODB6_0_MONGOINFRA']._serialized_start=13228
  _globals['_MONGODB6_0_MONGOINFRA']._serialized_end=13542
  _globals['_MONGODB6_0_ENTERPRISE']._serialized_start=13545
  _globals['_MONGODB6_0_ENTERPRISE']._serialized_end=14925
  _globals['_MONGODB6_0_ENTERPRISE_MONGOD']._serialized_start=13883
  _globals['_MONGODB6_0_ENTERPRISE_MONGOD']._serialized_end=14114
  _globals['_MONGODB6_0_ENTERPRISE_MONGOCFG']._serialized_start=14117
  _globals['_MONGODB6_0_ENTERPRISE_MONGOCFG']._serialized_end=14352
  _globals['_MONGODB6_0_ENTERPRISE_MONGOS']._serialized_start=14355
  _globals['_MONGODB6_0_ENTERPRISE_MONGOS']._serialized_end=14586
  _globals['_MONGODB6_0_ENTERPRISE_MONGOINFRA']._serialized_start=14589
  _globals['_MONGODB6_0_ENTERPRISE_MONGOINFRA']._serialized_end=14925
  _globals['_MONGODB']._serialized_start=14928
  _globals['_MONGODB']._serialized_end=16168
  _globals['_MONGODB_MONGOD']._serialized_start=15196
  _globals['_MONGODB_MONGOD']._serialized_end=15413
  _globals['_MONGODB_MONGOCFG']._serialized_start=15416
  _globals['_MONGODB_MONGOCFG']._serialized_end=15637
  _globals['_MONGODB_MONGOS']._serialized_start=15640
  _globals['_MONGODB_MONGOS']._serialized_end=15857
  _globals['_MONGODB_MONGOINFRA']._serialized_start=15860
  _globals['_MONGODB_MONGOINFRA']._serialized_end=16168
  _globals['_SHARD']._serialized_start=16170
  _globals['_SHARD']._serialized_end=16211
  _globals['_HOST']._serialized_start=16214
  _globals['_HOST']._serialized_end=17097
  _globals['_HOST_HOSTPARAMETERS']._serialized_start=16695
  _globals['_HOST_HOSTPARAMETERS']._serialized_end=16894
  _globals['_HOST_HOSTPARAMETERS_TAGSENTRY']._serialized_start=16851
  _globals['_HOST_HOSTPARAMETERS_TAGSENTRY']._serialized_end=16894
  _globals['_HOST_TYPE']._serialized_start=16896
  _globals['_HOST_TYPE']._serialized_end=16978
  _globals['_HOST_ROLE']._serialized_start=16980
  _globals['_HOST_ROLE']._serialized_end=17032
  _globals['_HOST_HEALTH']._serialized_start=1682
  _globals['_HOST_HEALTH']._serialized_end=1745
  _globals['_SERVICE']._serialized_start=17100
  _globals['_SERVICE']._serialized_end=17346
  _globals['_SERVICE_TYPE']._serialized_start=16896
  _globals['_SERVICE_TYPE']._serialized_end=16962
  _globals['_SERVICE_HEALTH']._serialized_start=1682
  _globals['_SERVICE_HEALTH']._serialized_end=1731
  _globals['_RESOURCES']._serialized_start=17348
  _globals['_RESOURCES']._serialized_end=17428
  _globals['_ACCESS']._serialized_start=17430
  _globals['_ACCESS']._serialized_end=17497
  _globals['_PERFORMANCEDIAGNOSTICSCONFIG']._serialized_start=17499
  _globals['_PERFORMANCEDIAGNOSTICSCONFIG']._serialized_end=17556
  _globals['_DISKSIZEAUTOSCALING']._serialized_start=17559
  _globals['_DISKSIZEAUTOSCALING']._serialized_end=17790
# @@protoc_insertion_point(module_scope)
