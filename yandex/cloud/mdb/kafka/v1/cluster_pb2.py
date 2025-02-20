# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/kafka/v1/cluster.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'yandex/cloud/mdb/kafka/v1/cluster.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud.mdb.kafka.v1 import common_pb2 as yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_common__pb2
from yandex.cloud.mdb.kafka.v1 import maintenance_pb2 as yandex_dot_cloud_dot_mdb_dot_kafka_dot_v1_dot_maintenance__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'yandex/cloud/mdb/kafka/v1/cluster.proto\x12\x19yandex.cloud.mdb.kafka.v1\x1a google/protobuf/descriptor.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a&yandex/cloud/mdb/kafka/v1/common.proto\x1a+yandex/cloud/mdb/kafka/v1/maintenance.proto\x1a\x1dyandex/cloud/validation.proto\"\x99\x08\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.mdb.kafka.v1.Cluster.LabelsEntry\x12\x43\n\x0b\x65nvironment\x18\x07 \x01(\x0e\x32..yandex.cloud.mdb.kafka.v1.Cluster.Environment\x12\x39\n\nmonitoring\x18\x08 \x03(\x0b\x32%.yandex.cloud.mdb.kafka.v1.Monitoring\x12\x35\n\x06\x63onfig\x18\t \x01(\x0b\x32%.yandex.cloud.mdb.kafka.v1.ConfigSpec\x12\x12\n\nnetwork_id\x18\n \x01(\t\x12\x39\n\x06health\x18\x0b \x01(\x0e\x32).yandex.cloud.mdb.kafka.v1.Cluster.Health\x12\x39\n\x06status\x18\x0c \x01(\x0e\x32).yandex.cloud.mdb.kafka.v1.Cluster.Status\x12\x1a\n\x12security_group_ids\x18\r \x03(\t\x12\x16\n\x0ehost_group_ids\x18\x0e \x03(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x0f \x01(\x08\x12H\n\x12maintenance_window\x18\x10 \x01(\x0b\x32,.yandex.cloud.mdb.kafka.v1.MaintenanceWindow\x12J\n\x11planned_operation\x18\x11 \x01(\x0b\x32/.yandex.cloud.mdb.kafka.v1.MaintenanceOperation\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0b\x45nvironment\x12\x1b\n\x17\x45NVIRONMENT_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\r\n\tPRESTABLE\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"y\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08STARTING\x10\x07\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\xec\x07\n\nConfigSpec\x12\x0f\n\x07version\x18\x01 \x01(\t\x12:\n\x05kafka\x18\x02 \x01(\x0b\x32+.yandex.cloud.mdb.kafka.v1.ConfigSpec.Kafka\x12\x42\n\tzookeeper\x18\x03 \x01(\x0b\x32/.yandex.cloud.mdb.kafka.v1.ConfigSpec.Zookeeper\x12\x0f\n\x07zone_id\x18\x04 \x03(\t\x12\x32\n\rbrokers_count\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x18\n\x10\x61ssign_public_ip\x18\x06 \x01(\x08\x12\x1c\n\x10unmanaged_topics\x18\x07 \x01(\x08\x42\x02\x18\x01\x12\x17\n\x0fschema_registry\x18\x08 \x01(\x08\x12\x31\n\x06\x61\x63\x63\x65ss\x18\t \x01(\x0b\x32!.yandex.cloud.mdb.kafka.v1.Access\x12L\n\x0frest_api_config\x18\n \x01(\x0b\x32\x33.yandex.cloud.mdb.kafka.v1.ConfigSpec.RestAPIConfig\x12M\n\x15\x64isk_size_autoscaling\x18\x0b \x01(\x0b\x32..yandex.cloud.mdb.kafka.v1.DiskSizeAutoscaling\x12:\n\x05kraft\x18\x0c \x01(\x0b\x32+.yandex.cloud.mdb.kafka.v1.ConfigSpec.KRaft\x1a\x80\x02\n\x05Kafka\x12\x37\n\tresources\x18\x01 \x01(\x0b\x32$.yandex.cloud.mdb.kafka.v1.Resources\x12V\n\x10kafka_config_2_8\x18\x04 \x01(\x0b\x32).yandex.cloud.mdb.kafka.v1.KafkaConfig2_8H\x00R\x0fkafkaConfig_2_8\x12P\n\x0ekafka_config_3\x18\x05 \x01(\x0b\x32\'.yandex.cloud.mdb.kafka.v1.KafkaConfig3H\x00R\rkafkaConfig_3B\x0e\n\x0ckafka_configJ\x04\x08\x02\x10\x04\x1a\x44\n\tZookeeper\x12\x37\n\tresources\x18\x01 \x01(\x0b\x32$.yandex.cloud.mdb.kafka.v1.Resources\x1a@\n\x05KRaft\x12\x37\n\tresources\x18\x01 \x01(\x0b\x32$.yandex.cloud.mdb.kafka.v1.Resources\x1a \n\rRestAPIConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\"P\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\x12\x14\n\x0c\x64isk_type_id\x18\x03 \x01(\t\"\xc0\t\n\x0eKafkaConfig2_8\x12\x44\n\x10\x63ompression_type\x18\x01 \x01(\x0e\x32*.yandex.cloud.mdb.kafka.v1.CompressionType\x12@\n\x1blog_flush_interval_messages\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\x15log_flush_interval_ms\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x44\n\x1flog_flush_scheduler_interval_ms\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x13log_retention_bytes\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x13log_retention_hours\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\x15log_retention_minutes\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x35\n\x10log_retention_ms\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11log_segment_bytes\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0flog_preallocate\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12=\n\x18socket_send_buffer_bytes\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bsocket_receive_buffer_bytes\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12=\n\x19\x61uto_create_topics_enable\x18\r \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0enum_partitions\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12?\n\x1a\x64\x65\x66\x61ult_replication_factor\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11message_max_bytes\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\x17replica_fetch_max_bytes\x18\x11 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x19\n\x11ssl_cipher_suites\x18\x12 \x03(\t\x12>\n\x19offsets_retention_minutes\x18\x13 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12I\n\x17sasl_enabled_mechanisms\x18\x14 \x03(\x0e\x32(.yandex.cloud.mdb.kafka.v1.SaslMechanism\"\xbe\t\n\x0cKafkaConfig3\x12\x44\n\x10\x63ompression_type\x18\x01 \x01(\x0e\x32*.yandex.cloud.mdb.kafka.v1.CompressionType\x12@\n\x1blog_flush_interval_messages\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\x15log_flush_interval_ms\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x44\n\x1flog_flush_scheduler_interval_ms\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x13log_retention_bytes\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x13log_retention_hours\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\x15log_retention_minutes\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x35\n\x10log_retention_ms\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11log_segment_bytes\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0flog_preallocate\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12=\n\x18socket_send_buffer_bytes\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bsocket_receive_buffer_bytes\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12=\n\x19\x61uto_create_topics_enable\x18\r \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0enum_partitions\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12?\n\x1a\x64\x65\x66\x61ult_replication_factor\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11message_max_bytes\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12<\n\x17replica_fetch_max_bytes\x18\x11 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x19\n\x11ssl_cipher_suites\x18\x12 \x03(\t\x12>\n\x19offsets_retention_minutes\x18\x13 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12I\n\x17sasl_enabled_mechanisms\x18\x14 \x03(\x0e\x32(.yandex.cloud.mdb.kafka.v1.SaslMechanism\"\x83\x03\n\x04Host\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\t\x12\x32\n\x04role\x18\x04 \x01(\x0e\x32$.yandex.cloud.mdb.kafka.v1.Host.Role\x12\x37\n\tresources\x18\x05 \x01(\x0b\x32$.yandex.cloud.mdb.kafka.v1.Resources\x12\x36\n\x06health\x18\x06 \x01(\x0e\x32&.yandex.cloud.mdb.kafka.v1.Host.Health\x12\x11\n\tsubnet_id\x18\x08 \x01(\t\x12\x18\n\x10\x61ssign_public_ip\x18\t \x01(\x08\"6\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\t\n\x05KAFKA\x10\x01\x12\r\n\tZOOKEEPER\x10\x02\"8\n\x06Health\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03J\x04\x08\x07\x10\x08\"\x1f\n\x06\x41\x63\x63\x65ss\x12\x15\n\rdata_transfer\x18\x01 \x01(\x08\"\x90\x01\n\x13\x44iskSizeAutoscaling\x12.\n\x17planned_usage_threshold\x18\x01 \x01(\x03\x42\r\xe8\xc7\x31\x00\xfa\xc7\x31\x05\x30-100\x12\x30\n\x19\x65mergency_usage_threshold\x18\x02 \x01(\x03\x42\r\xe8\xc7\x31\x00\xfa\xc7\x31\x05\x30-100\x12\x17\n\x0f\x64isk_size_limit\x18\x03 \x01(\x03\x42\x64\n\x1dyandex.cloud.api.mdb.kafka.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/kafka/v1;kafkab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.kafka.v1.cluster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035yandex.cloud.api.mdb.kafka.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/kafka/v1;kafka'
  _globals['_CLUSTER_LABELSENTRY']._loaded_options = None
  _globals['_CLUSTER_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CONFIGSPEC'].fields_by_name['unmanaged_topics']._loaded_options = None
  _globals['_CONFIGSPEC'].fields_by_name['unmanaged_topics']._serialized_options = b'\030\001'
  _globals['_DISKSIZEAUTOSCALING'].fields_by_name['planned_usage_threshold']._loaded_options = None
  _globals['_DISKSIZEAUTOSCALING'].fields_by_name['planned_usage_threshold']._serialized_options = b'\350\3071\000\372\3071\0050-100'
  _globals['_DISKSIZEAUTOSCALING'].fields_by_name['emergency_usage_threshold']._loaded_options = None
  _globals['_DISKSIZEAUTOSCALING'].fields_by_name['emergency_usage_threshold']._serialized_options = b'\350\3071\000\372\3071\0050-100'
  _globals['_CLUSTER']._serialized_start=286
  _globals['_CLUSTER']._serialized_end=1335
  _globals['_CLUSTER_LABELSENTRY']._serialized_start=1027
  _globals['_CLUSTER_LABELSENTRY']._serialized_end=1072
  _globals['_CLUSTER_ENVIRONMENT']._serialized_start=1074
  _globals['_CLUSTER_ENVIRONMENT']._serialized_end=1147
  _globals['_CLUSTER_HEALTH']._serialized_start=1149
  _globals['_CLUSTER_HEALTH']._serialized_end=1212
  _globals['_CLUSTER_STATUS']._serialized_start=1214
  _globals['_CLUSTER_STATUS']._serialized_end=1335
  _globals['_MONITORING']._serialized_start=1337
  _globals['_MONITORING']._serialized_end=1398
  _globals['_CONFIGSPEC']._serialized_start=1401
  _globals['_CONFIGSPEC']._serialized_end=2405
  _globals['_CONFIGSPEC_KAFKA']._serialized_start=1979
  _globals['_CONFIGSPEC_KAFKA']._serialized_end=2235
  _globals['_CONFIGSPEC_ZOOKEEPER']._serialized_start=2237
  _globals['_CONFIGSPEC_ZOOKEEPER']._serialized_end=2305
  _globals['_CONFIGSPEC_KRAFT']._serialized_start=2307
  _globals['_CONFIGSPEC_KRAFT']._serialized_end=2371
  _globals['_CONFIGSPEC_RESTAPICONFIG']._serialized_start=2373
  _globals['_CONFIGSPEC_RESTAPICONFIG']._serialized_end=2405
  _globals['_RESOURCES']._serialized_start=2407
  _globals['_RESOURCES']._serialized_end=2487
  _globals['_KAFKACONFIG2_8']._serialized_start=2490
  _globals['_KAFKACONFIG2_8']._serialized_end=3706
  _globals['_KAFKACONFIG3']._serialized_start=3709
  _globals['_KAFKACONFIG3']._serialized_end=4923
  _globals['_HOST']._serialized_start=4926
  _globals['_HOST']._serialized_end=5313
  _globals['_HOST_ROLE']._serialized_start=5195
  _globals['_HOST_ROLE']._serialized_end=5249
  _globals['_HOST_HEALTH']._serialized_start=5251
  _globals['_HOST_HEALTH']._serialized_end=5307
  _globals['_ACCESS']._serialized_start=5315
  _globals['_ACCESS']._serialized_end=5346
  _globals['_DISKSIZEAUTOSCALING']._serialized_start=5349
  _globals['_DISKSIZEAUTOSCALING']._serialized_end=5493
# @@protoc_insertion_point(module_scope)
