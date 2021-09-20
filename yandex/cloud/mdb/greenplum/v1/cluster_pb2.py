# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/greenplum/v1/cluster.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.greenplum.v1 import config_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_config__pb2
from yandex.cloud.mdb.greenplum.v1 import maintenance_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_maintenance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/greenplum/v1/cluster.proto',
  package='yandex.cloud.mdb.greenplum.v1',
  syntax='proto3',
  serialized_options=b'\n!yandex.cloud.api.mdb.greenplum.v1B\003GPCZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplum',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+yandex/cloud/mdb/greenplum/v1/cluster.proto\x12\x1dyandex.cloud.mdb.greenplum.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/type/timeofday.proto\x1a\x1dyandex/cloud/validation.proto\x1a*yandex/cloud/mdb/greenplum/v1/config.proto\x1a/yandex/cloud/mdb/greenplum/v1/maintenance.proto\"\xcd\n\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x04name\x18\x04 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\x12>\n\x06\x63onfig\x18\x05 \x01(\x0b\x32..yandex.cloud.mdb.greenplum.v1.GreenplumConfig\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x42\n\x06labels\x18\x07 \x03(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.Cluster.LabelsEntry\x12G\n\x0b\x65nvironment\x18\x08 \x01(\x0e\x32\x32.yandex.cloud.mdb.greenplum.v1.Cluster.Environment\x12=\n\nmonitoring\x18\t \x03(\x0b\x32).yandex.cloud.mdb.greenplum.v1.Monitoring\x12L\n\rmaster_config\x18\n \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.MasterSubclusterConfig\x12N\n\x0esegment_config\x18\x0b \x01(\x0b\x32\x36.yandex.cloud.mdb.greenplum.v1.SegmentSubclusterConfig\x12\x19\n\x11master_host_count\x18\x0c \x01(\x03\x12\x1a\n\x12segment_host_count\x18\r \x01(\x03\x12\x17\n\x0fsegment_in_host\x18\x0e \x01(\x03\x12\x12\n\nnetwork_id\x18\x0f \x01(\t\x12=\n\x06health\x18\x10 \x01(\x0e\x32-.yandex.cloud.mdb.greenplum.v1.Cluster.Health\x12=\n\x06status\x18\x11 \x01(\x0e\x32-.yandex.cloud.mdb.greenplum.v1.Cluster.Status\x12L\n\x12maintenance_window\x18\x12 \x01(\x0b\x32\x30.yandex.cloud.mdb.greenplum.v1.MaintenanceWindow\x12N\n\x11planned_operation\x18\x13 \x01(\x0b\x32\x33.yandex.cloud.mdb.greenplum.v1.MaintenanceOperation\x12\x1a\n\x12security_group_ids\x18\x14 \x03(\t\x12\x11\n\tuser_name\x18\x15 \x01(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x16 \x01(\x08\x12\x16\n\x0ehost_group_ids\x18\x17 \x03(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0b\x45nvironment\x12\x1b\n\x17\x45NVIRONMENT_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\r\n\tPRESTABLE\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"y\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08STARTING\x10\x07\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\xe0\x01\n\x0fGreenplumConfig\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x33\n\x13\x62\x61\x63kup_window_start\x18\x02 \x01(\x0b\x32\x16.google.type.TimeOfDay\x12\x35\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0b\x32%.yandex.cloud.mdb.greenplum.v1.Access\x12\x19\n\x07zone_id\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1b\n\tsubnet_id\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x18\n\x10\x61ssign_public_ip\x18\x06 \x01(\x08\",\n\x06\x41\x63\x63\x65ss\x12\x11\n\tdata_lens\x18\x01 \x01(\x08\x12\x0f\n\x07web_sql\x18\x02 \x01(\x08\x42u\n!yandex.cloud.api.mdb.greenplum.v1B\x03GPCZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplumb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_type_dot_timeofday__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_config__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_maintenance__pb2.DESCRIPTOR,])



_CLUSTER_ENVIRONMENT = _descriptor.EnumDescriptor(
  name='Environment',
  full_name='yandex.cloud.mdb.greenplum.v1.Cluster.Environment',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENVIRONMENT_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRODUCTION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRESTABLE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1361,
  serialized_end=1434,
)
_sym_db.RegisterEnumDescriptor(_CLUSTER_ENVIRONMENT)

_CLUSTER_HEALTH = _descriptor.EnumDescriptor(
  name='Health',
  full_name='yandex.cloud.mdb.greenplum.v1.Cluster.Health',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HEALTH_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEAD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEGRADED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1436,
  serialized_end=1499,
)
_sym_db.RegisterEnumDescriptor(_CLUSTER_HEALTH)

_CLUSTER_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.mdb.greenplum.v1.Cluster.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPING', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STARTING', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1501,
  serialized_end=1622,
)
_sym_db.RegisterEnumDescriptor(_CLUSTER_STATUS)


_CLUSTER_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.mdb.greenplum.v1.Cluster.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1314,
  serialized_end=1359,
)

_CLUSTER = _descriptor.Descriptor(
  name='Cluster',
  full_name='yandex.cloud.mdb.greenplum.v1.Cluster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.labels', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environment', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.environment', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monitoring', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.monitoring', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='master_config', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.master_config', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='segment_config', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.segment_config', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='master_host_count', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.master_host_count', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='segment_host_count', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.segment_host_count', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='segment_in_host', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.segment_in_host', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_id', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.network_id', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='health', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.health', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.status', index=16,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maintenance_window', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.maintenance_window', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='planned_operation', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.planned_operation', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security_group_ids', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.security_group_ids', index=19,
      number=20, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.user_name', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deletion_protection', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.deletion_protection', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_group_ids', full_name='yandex.cloud.mdb.greenplum.v1.Cluster.host_group_ids', index=22,
      number=23, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CLUSTER_LABELSENTRY, ],
  enum_types=[
    _CLUSTER_ENVIRONMENT,
    _CLUSTER_HEALTH,
    _CLUSTER_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=1622,
)


_MONITORING = _descriptor.Descriptor(
  name='Monitoring',
  full_name='yandex.cloud.mdb.greenplum.v1.Monitoring',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.greenplum.v1.Monitoring.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.mdb.greenplum.v1.Monitoring.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='link', full_name='yandex.cloud.mdb.greenplum.v1.Monitoring.link', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1624,
  serialized_end=1685,
)


_GREENPLUMCONFIG = _descriptor.Descriptor(
  name='GreenplumConfig',
  full_name='yandex.cloud.mdb.greenplum.v1.GreenplumConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='yandex.cloud.mdb.greenplum.v1.GreenplumConfig.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup_window_start', full_name='yandex.cloud.mdb.greenplum.v1.GreenplumConfig.backup_window_start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access', full_name='yandex.cloud.mdb.greenplum.v1.GreenplumConfig.access', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='yandex.cloud.mdb.greenplum.v1.GreenplumConfig.zone_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.mdb.greenplum.v1.GreenplumConfig.subnet_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assign_public_ip', full_name='yandex.cloud.mdb.greenplum.v1.GreenplumConfig.assign_public_ip', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1688,
  serialized_end=1912,
)


_ACCESS = _descriptor.Descriptor(
  name='Access',
  full_name='yandex.cloud.mdb.greenplum.v1.Access',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_lens', full_name='yandex.cloud.mdb.greenplum.v1.Access.data_lens', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='web_sql', full_name='yandex.cloud.mdb.greenplum.v1.Access.web_sql', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1914,
  serialized_end=1958,
)

_CLUSTER_LABELSENTRY.containing_type = _CLUSTER
_CLUSTER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLUSTER.fields_by_name['config'].message_type = _GREENPLUMCONFIG
_CLUSTER.fields_by_name['labels'].message_type = _CLUSTER_LABELSENTRY
_CLUSTER.fields_by_name['environment'].enum_type = _CLUSTER_ENVIRONMENT
_CLUSTER.fields_by_name['monitoring'].message_type = _MONITORING
_CLUSTER.fields_by_name['master_config'].message_type = yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_config__pb2._MASTERSUBCLUSTERCONFIG
_CLUSTER.fields_by_name['segment_config'].message_type = yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_config__pb2._SEGMENTSUBCLUSTERCONFIG
_CLUSTER.fields_by_name['health'].enum_type = _CLUSTER_HEALTH
_CLUSTER.fields_by_name['status'].enum_type = _CLUSTER_STATUS
_CLUSTER.fields_by_name['maintenance_window'].message_type = yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_maintenance__pb2._MAINTENANCEWINDOW
_CLUSTER.fields_by_name['planned_operation'].message_type = yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_maintenance__pb2._MAINTENANCEOPERATION
_CLUSTER_ENVIRONMENT.containing_type = _CLUSTER
_CLUSTER_HEALTH.containing_type = _CLUSTER
_CLUSTER_STATUS.containing_type = _CLUSTER
_GREENPLUMCONFIG.fields_by_name['backup_window_start'].message_type = google_dot_type_dot_timeofday__pb2._TIMEOFDAY
_GREENPLUMCONFIG.fields_by_name['access'].message_type = _ACCESS
DESCRIPTOR.message_types_by_name['Cluster'] = _CLUSTER
DESCRIPTOR.message_types_by_name['Monitoring'] = _MONITORING
DESCRIPTOR.message_types_by_name['GreenplumConfig'] = _GREENPLUMCONFIG
DESCRIPTOR.message_types_by_name['Access'] = _ACCESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cluster = _reflection.GeneratedProtocolMessageType('Cluster', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLUSTER_LABELSENTRY,
    '__module__' : 'yandex.cloud.mdb.greenplum.v1.cluster_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.Cluster.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CLUSTER,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.Cluster)
  })
_sym_db.RegisterMessage(Cluster)
_sym_db.RegisterMessage(Cluster.LabelsEntry)

Monitoring = _reflection.GeneratedProtocolMessageType('Monitoring', (_message.Message,), {
  'DESCRIPTOR' : _MONITORING,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.Monitoring)
  })
_sym_db.RegisterMessage(Monitoring)

GreenplumConfig = _reflection.GeneratedProtocolMessageType('GreenplumConfig', (_message.Message,), {
  'DESCRIPTOR' : _GREENPLUMCONFIG,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.GreenplumConfig)
  })
_sym_db.RegisterMessage(GreenplumConfig)

Access = _reflection.GeneratedProtocolMessageType('Access', (_message.Message,), {
  'DESCRIPTOR' : _ACCESS,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.Access)
  })
_sym_db.RegisterMessage(Access)


DESCRIPTOR._options = None
_CLUSTER_LABELSENTRY._options = None
_CLUSTER.fields_by_name['name']._options = None
_GREENPLUMCONFIG.fields_by_name['zone_id']._options = None
_GREENPLUMCONFIG.fields_by_name['subnet_id']._options = None
# @@protoc_insertion_point(module_scope)
