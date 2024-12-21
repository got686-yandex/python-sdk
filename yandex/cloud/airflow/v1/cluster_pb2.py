# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/airflow/v1/cluster.proto
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
    'yandex/cloud/airflow/v1/cluster.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.airflow.v1 import common_pb2 as yandex_dot_cloud_dot_airflow_dot_v1_dot_common__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.logging.v1 import log_entry_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%yandex/cloud/airflow/v1/cluster.proto\x12\x17yandex.cloud.airflow.v1\x1a$yandex/cloud/airflow/v1/common.proto\x1a\x1dyandex/cloud/validation.proto\x1a\'yandex/cloud/logging/v1/log_entry.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcc\x06\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12<\n\x06labels\x18\x06 \x03(\x0b\x32,.yandex.cloud.airflow.v1.Cluster.LabelsEntry\x12\x37\n\nmonitoring\x18\x08 \x03(\x0b\x32#.yandex.cloud.airflow.v1.Monitoring\x12\x36\n\x06\x63onfig\x18\t \x01(\x0b\x32&.yandex.cloud.airflow.v1.ClusterConfig\x12/\n\x06health\x18\n \x01(\x0e\x32\x1f.yandex.cloud.airflow.v1.Health\x12\x37\n\x06status\x18\x0b \x01(\x0e\x32\'.yandex.cloud.airflow.v1.Cluster.Status\x12\x37\n\x07network\x18\x0c \x01(\x0b\x32&.yandex.cloud.airflow.v1.NetworkConfig\x12:\n\tcode_sync\x18\r \x01(\x0b\x32\'.yandex.cloud.airflow.v1.CodeSyncConfig\x12\x1b\n\x13\x64\x65letion_protection\x18\x0e \x01(\x08\x12\x15\n\rwebserver_url\x18\x0f \x01(\t\x12$\n\x12service_account_id\x18\x10 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x37\n\x07logging\x18\x11 \x01(\x0b\x32&.yandex.cloud.airflow.v1.LoggingConfig\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"y\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\x0c\n\x08STARTING\x10\x06\x12\x0c\n\x08UPDATING\x10\x07J\x04\x08\x07\x10\x08\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\x87\x04\n\rClusterConfig\x12\x16\n\nversion_id\x18\x01 \x01(\tB\x02\x18\x01\x12\x37\n\x07\x61irflow\x18\x02 \x01(\x0b\x32&.yandex.cloud.airflow.v1.AirflowConfig\x12\x41\n\twebserver\x18\x03 \x01(\x0b\x32(.yandex.cloud.airflow.v1.WebserverConfigB\x04\xe8\xc7\x31\x01\x12\x41\n\tscheduler\x18\x04 \x01(\x0b\x32(.yandex.cloud.airflow.v1.SchedulerConfigB\x04\xe8\xc7\x31\x01\x12;\n\ttriggerer\x18\x05 \x01(\x0b\x32(.yandex.cloud.airflow.v1.TriggererConfig\x12;\n\x06worker\x18\x06 \x01(\x0b\x32%.yandex.cloud.airflow.v1.WorkerConfigB\x04\xe8\xc7\x31\x01\x12;\n\x0c\x64\x65pendencies\x18\x07 \x01(\x0b\x32%.yandex.cloud.airflow.v1.Dependencies\x12\x37\n\x07lockbox\x18\x08 \x01(\x0b\x32&.yandex.cloud.airflow.v1.LockboxConfig\x12\x17\n\x0f\x61irflow_version\x18\t \x01(\t\x12\x16\n\x0epython_version\x18\n \x01(\t\"\x82\x01\n\rAirflowConfig\x12\x42\n\x06\x63onfig\x18\x01 \x03(\x0b\x32\x32.yandex.cloud.airflow.v1.AirflowConfig.ConfigEntry\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"b\n\x0fWebserverConfig\x12\x18\n\x05\x63ount\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x31-512\x12\x35\n\tresources\x18\x02 \x01(\x0b\x32\".yandex.cloud.airflow.v1.Resources\"b\n\x0fSchedulerConfig\x12\x18\n\x05\x63ount\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x31-512\x12\x35\n\tresources\x18\x02 \x01(\x0b\x32\".yandex.cloud.airflow.v1.Resources\"b\n\x0fTriggererConfig\x12\x18\n\x05\x63ount\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-512\x12\x35\n\tresources\x18\x02 \x01(\x0b\x32\".yandex.cloud.airflow.v1.Resources\"\x81\x01\n\x0cWorkerConfig\x12\x1c\n\tmin_count\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-512\x12\x1c\n\tmax_count\x18\x02 \x01(\x03\x42\t\xfa\xc7\x31\x05\x31-512\x12\x35\n\tresources\x18\x03 \x01(\x0b\x32\".yandex.cloud.airflow.v1.Resources\":\n\x0c\x44\x65pendencies\x12\x14\n\x0cpip_packages\x18\x01 \x03(\t\x12\x14\n\x0c\x64\x65\x62_packages\x18\x02 \x03(\t\"?\n\rNetworkConfig\x12\x12\n\nsubnet_ids\x18\x01 \x03(\t\x12\x1a\n\x12security_group_ids\x18\x02 \x03(\t\"\x1a\n\x08S3Config\x12\x0e\n\x06\x62ucket\x18\x03 \x01(\t\"Q\n\x0e\x43odeSyncConfig\x12/\n\x02s3\x18\x01 \x01(\x0b\x32!.yandex.cloud.airflow.v1.S3ConfigH\x00\x42\x0e\n\x06source\x12\x04\xc0\xc1\x31\x01\"\xe2\x01\n\rLoggingConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x38\n\tfolder_id\x18\x02 \x01(\tB#\xf2\xc7\x31\x1f([a-zA-Z][-a-zA-Z0-9_.]{0,63})?H\x00\x12;\n\x0clog_group_id\x18\x03 \x01(\tB#\xf2\xc7\x31\x1f([a-zA-Z][-a-zA-Z0-9_.]{0,63})?H\x00\x12:\n\tmin_level\x18\x04 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.LevelB\r\n\x0b\x64\x65stination\" \n\rLockboxConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x42\x62\n\x1byandex.cloud.api.airflow.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/airflow/v1;airflowb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.airflow.v1.cluster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.airflow.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/airflow/v1;airflow'
  _globals['_CLUSTER_LABELSENTRY']._loaded_options = None
  _globals['_CLUSTER_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CLUSTER'].fields_by_name['service_account_id']._loaded_options = None
  _globals['_CLUSTER'].fields_by_name['service_account_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_CLUSTERCONFIG'].fields_by_name['version_id']._loaded_options = None
  _globals['_CLUSTERCONFIG'].fields_by_name['version_id']._serialized_options = b'\030\001'
  _globals['_CLUSTERCONFIG'].fields_by_name['webserver']._loaded_options = None
  _globals['_CLUSTERCONFIG'].fields_by_name['webserver']._serialized_options = b'\350\3071\001'
  _globals['_CLUSTERCONFIG'].fields_by_name['scheduler']._loaded_options = None
  _globals['_CLUSTERCONFIG'].fields_by_name['scheduler']._serialized_options = b'\350\3071\001'
  _globals['_CLUSTERCONFIG'].fields_by_name['worker']._loaded_options = None
  _globals['_CLUSTERCONFIG'].fields_by_name['worker']._serialized_options = b'\350\3071\001'
  _globals['_AIRFLOWCONFIG_CONFIGENTRY']._loaded_options = None
  _globals['_AIRFLOWCONFIG_CONFIGENTRY']._serialized_options = b'8\001'
  _globals['_WEBSERVERCONFIG'].fields_by_name['count']._loaded_options = None
  _globals['_WEBSERVERCONFIG'].fields_by_name['count']._serialized_options = b'\372\3071\0051-512'
  _globals['_SCHEDULERCONFIG'].fields_by_name['count']._loaded_options = None
  _globals['_SCHEDULERCONFIG'].fields_by_name['count']._serialized_options = b'\372\3071\0051-512'
  _globals['_TRIGGERERCONFIG'].fields_by_name['count']._loaded_options = None
  _globals['_TRIGGERERCONFIG'].fields_by_name['count']._serialized_options = b'\372\3071\0050-512'
  _globals['_WORKERCONFIG'].fields_by_name['min_count']._loaded_options = None
  _globals['_WORKERCONFIG'].fields_by_name['min_count']._serialized_options = b'\372\3071\0050-512'
  _globals['_WORKERCONFIG'].fields_by_name['max_count']._loaded_options = None
  _globals['_WORKERCONFIG'].fields_by_name['max_count']._serialized_options = b'\372\3071\0051-512'
  _globals['_CODESYNCCONFIG'].oneofs_by_name['source']._loaded_options = None
  _globals['_CODESYNCCONFIG'].oneofs_by_name['source']._serialized_options = b'\300\3011\001'
  _globals['_LOGGINGCONFIG'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LOGGINGCONFIG'].fields_by_name['folder_id']._serialized_options = b'\362\3071\037([a-zA-Z][-a-zA-Z0-9_.]{0,63})?'
  _globals['_LOGGINGCONFIG'].fields_by_name['log_group_id']._loaded_options = None
  _globals['_LOGGINGCONFIG'].fields_by_name['log_group_id']._serialized_options = b'\362\3071\037([a-zA-Z][-a-zA-Z0-9_.]{0,63})?'
  _globals['_CLUSTER']._serialized_start=210
  _globals['_CLUSTER']._serialized_end=1054
  _globals['_CLUSTER_LABELSENTRY']._serialized_start=880
  _globals['_CLUSTER_LABELSENTRY']._serialized_end=925
  _globals['_CLUSTER_STATUS']._serialized_start=927
  _globals['_CLUSTER_STATUS']._serialized_end=1048
  _globals['_MONITORING']._serialized_start=1056
  _globals['_MONITORING']._serialized_end=1117
  _globals['_CLUSTERCONFIG']._serialized_start=1120
  _globals['_CLUSTERCONFIG']._serialized_end=1639
  _globals['_AIRFLOWCONFIG']._serialized_start=1642
  _globals['_AIRFLOWCONFIG']._serialized_end=1772
  _globals['_AIRFLOWCONFIG_CONFIGENTRY']._serialized_start=1727
  _globals['_AIRFLOWCONFIG_CONFIGENTRY']._serialized_end=1772
  _globals['_WEBSERVERCONFIG']._serialized_start=1774
  _globals['_WEBSERVERCONFIG']._serialized_end=1872
  _globals['_SCHEDULERCONFIG']._serialized_start=1874
  _globals['_SCHEDULERCONFIG']._serialized_end=1972
  _globals['_TRIGGERERCONFIG']._serialized_start=1974
  _globals['_TRIGGERERCONFIG']._serialized_end=2072
  _globals['_WORKERCONFIG']._serialized_start=2075
  _globals['_WORKERCONFIG']._serialized_end=2204
  _globals['_DEPENDENCIES']._serialized_start=2206
  _globals['_DEPENDENCIES']._serialized_end=2264
  _globals['_NETWORKCONFIG']._serialized_start=2266
  _globals['_NETWORKCONFIG']._serialized_end=2329
  _globals['_S3CONFIG']._serialized_start=2331
  _globals['_S3CONFIG']._serialized_end=2357
  _globals['_CODESYNCCONFIG']._serialized_start=2359
  _globals['_CODESYNCCONFIG']._serialized_end=2440
  _globals['_LOGGINGCONFIG']._serialized_start=2443
  _globals['_LOGGINGCONFIG']._serialized_end=2669
  _globals['_LOCKBOXCONFIG']._serialized_start=2671
  _globals['_LOCKBOXCONFIG']._serialized_end=2703
# @@protoc_insertion_point(module_scope)
