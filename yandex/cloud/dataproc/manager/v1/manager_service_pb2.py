# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dataproc/manager/v1/manager_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/dataproc/manager/v1/manager_service.proto',
  package='yandex.cloud.dataproc.manager.v1',
  syntax='proto3',
  serialized_options=_b('\n$yandex.cloud.api.dataproc.manager.v1ZUgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/manager/v1;dataproc_manager'),
  serialized_pb=_b('\n6yandex/cloud/dataproc/manager/v1/manager_service.proto\x12 yandex.cloud.dataproc.manager.v1\"_\n\rHbaseNodeInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08requests\x18\x02 \x01(\x03\x12\x14\n\x0cheap_size_mb\x18\x03 \x01(\x03\x12\x18\n\x10max_heap_size_mb\x18\x04 \x01(\x03\"\xe1\x01\n\tHbaseInfo\x12\x11\n\tavailable\x18\x01 \x01(\x08\x12\x0f\n\x07regions\x18\x02 \x01(\x03\x12\x10\n\x08requests\x18\x03 \x01(\x03\x12\x14\n\x0c\x61verage_load\x18\x04 \x01(\x01\x12\x43\n\nlive_nodes\x18\x05 \x03(\x0b\x32/.yandex.cloud.dataproc.manager.v1.HbaseNodeInfo\x12\x43\n\ndead_nodes\x18\x06 \x03(\x0b\x32/.yandex.cloud.dataproc.manager.v1.HbaseNodeInfo\"r\n\x0cHDFSNodeInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04used\x18\x02 \x01(\x03\x12\x11\n\tremaining\x18\x03 \x01(\x03\x12\x10\n\x08\x63\x61pacity\x18\x04 \x01(\x03\x12\x12\n\nnum_blocks\x18\x05 \x01(\x03\x12\r\n\x05state\x18\x06 \x01(\t\"\xf3\x02\n\x08HDFSInfo\x12\x11\n\tavailable\x18\x01 \x01(\x08\x12\x19\n\x11percent_remaining\x18\x02 \x01(\x01\x12\x0c\n\x04used\x18\x03 \x01(\x03\x12\x0c\n\x04\x66ree\x18\x04 \x01(\x03\x12\x14\n\x0ctotal_blocks\x18\x05 \x01(\x03\x12\x16\n\x0emissing_blocks\x18\x06 \x01(\x03\x12\"\n\x1amissing_blocks_replica_one\x18\x07 \x01(\x03\x12\x42\n\nlive_nodes\x18\x08 \x03(\x0b\x32..yandex.cloud.dataproc.manager.v1.HDFSNodeInfo\x12\x42\n\ndead_nodes\x18\t \x03(\x0b\x32..yandex.cloud.dataproc.manager.v1.HDFSNodeInfo\x12\x43\n\x0b\x64\x65\x63om_nodes\x18\n \x03(\x0b\x32..yandex.cloud.dataproc.manager.v1.HDFSNodeInfo\"\x9b\x01\n\x08HiveInfo\x12\x11\n\tavailable\x18\x01 \x01(\x08\x12\x19\n\x11queries_succeeded\x18\x02 \x01(\x03\x12\x16\n\x0equeries_failed\x18\x03 \x01(\x03\x12\x19\n\x11queries_executing\x18\x04 \x01(\x03\x12\x15\n\rsessions_open\x18\x05 \x01(\x03\x12\x17\n\x0fsessions_active\x18\x06 \x01(\x03\"x\n\x0cYarnNodeInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x16\n\x0enum_containers\x18\x03 \x01(\x03\x12\x16\n\x0eused_memory_mb\x18\x04 \x01(\x03\x12\x1b\n\x13\x61vailable_memory_mb\x18\x05 \x01(\x03\"a\n\x08YarnInfo\x12\x11\n\tavailable\x18\x01 \x01(\x08\x12\x42\n\nlive_nodes\x18\x02 \x03(\x0b\x32..yandex.cloud.dataproc.manager.v1.YarnNodeInfo\"\x1e\n\rZookeeperInfo\x12\r\n\x05\x61live\x18\x01 \x01(\x08\"\x1a\n\tOozieInfo\x12\r\n\x05\x61live\x18\x01 \x01(\x08\"\xf0\x02\n\x04Info\x12\x38\n\x04hdfs\x18\x01 \x01(\x0b\x32*.yandex.cloud.dataproc.manager.v1.HDFSInfo\x12\x38\n\x04yarn\x18\x02 \x01(\x0b\x32*.yandex.cloud.dataproc.manager.v1.YarnInfo\x12\x38\n\x04hive\x18\x03 \x01(\x0b\x32*.yandex.cloud.dataproc.manager.v1.HiveInfo\x12\x42\n\tzookeeper\x18\x04 \x01(\x0b\x32/.yandex.cloud.dataproc.manager.v1.ZookeeperInfo\x12:\n\x05hbase\x18\x05 \x01(\x0b\x32+.yandex.cloud.dataproc.manager.v1.HbaseInfo\x12:\n\x05oozie\x18\x06 \x01(\x0b\x32+.yandex.cloud.dataproc.manager.v1.OozieInfo\"m\n\rReportRequest\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x19\n\x11topology_revision\x18\x02 \x01(\x03\x12\x34\n\x04info\x18\x03 \x01(\x0b\x32&.yandex.cloud.dataproc.manager.v1.Info\"\r\n\x0bReportReply2\x84\x01\n\x16\x44\x61taprocManagerService\x12j\n\x06Report\x12/.yandex.cloud.dataproc.manager.v1.ReportRequest\x1a-.yandex.cloud.dataproc.manager.v1.ReportReply\"\x00\x42}\n$yandex.cloud.api.dataproc.manager.v1ZUgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/manager/v1;dataproc_managerb\x06proto3')
)




_HBASENODEINFO = _descriptor.Descriptor(
  name='HbaseNodeInfo',
  full_name='yandex.cloud.dataproc.manager.v1.HbaseNodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.dataproc.manager.v1.HbaseNodeInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requests', full_name='yandex.cloud.dataproc.manager.v1.HbaseNodeInfo.requests', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heap_size_mb', full_name='yandex.cloud.dataproc.manager.v1.HbaseNodeInfo.heap_size_mb', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_heap_size_mb', full_name='yandex.cloud.dataproc.manager.v1.HbaseNodeInfo.max_heap_size_mb', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=92,
  serialized_end=187,
)


_HBASEINFO = _descriptor.Descriptor(
  name='HbaseInfo',
  full_name='yandex.cloud.dataproc.manager.v1.HbaseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='available', full_name='yandex.cloud.dataproc.manager.v1.HbaseInfo.available', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regions', full_name='yandex.cloud.dataproc.manager.v1.HbaseInfo.regions', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requests', full_name='yandex.cloud.dataproc.manager.v1.HbaseInfo.requests', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_load', full_name='yandex.cloud.dataproc.manager.v1.HbaseInfo.average_load', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='live_nodes', full_name='yandex.cloud.dataproc.manager.v1.HbaseInfo.live_nodes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dead_nodes', full_name='yandex.cloud.dataproc.manager.v1.HbaseInfo.dead_nodes', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=190,
  serialized_end=415,
)


_HDFSNODEINFO = _descriptor.Descriptor(
  name='HDFSNodeInfo',
  full_name='yandex.cloud.dataproc.manager.v1.HDFSNodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.dataproc.manager.v1.HDFSNodeInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='used', full_name='yandex.cloud.dataproc.manager.v1.HDFSNodeInfo.used', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remaining', full_name='yandex.cloud.dataproc.manager.v1.HDFSNodeInfo.remaining', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='yandex.cloud.dataproc.manager.v1.HDFSNodeInfo.capacity', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_blocks', full_name='yandex.cloud.dataproc.manager.v1.HDFSNodeInfo.num_blocks', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='yandex.cloud.dataproc.manager.v1.HDFSNodeInfo.state', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=417,
  serialized_end=531,
)


_HDFSINFO = _descriptor.Descriptor(
  name='HDFSInfo',
  full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='available', full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo.available', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percent_remaining', full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo.percent_remaining', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='used', full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo.used', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free', full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo.free', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_blocks', full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo.total_blocks', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing_blocks', full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo.missing_blocks', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing_blocks_replica_one', full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo.missing_blocks_replica_one', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='live_nodes', full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo.live_nodes', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dead_nodes', full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo.dead_nodes', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decom_nodes', full_name='yandex.cloud.dataproc.manager.v1.HDFSInfo.decom_nodes', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=534,
  serialized_end=905,
)


_HIVEINFO = _descriptor.Descriptor(
  name='HiveInfo',
  full_name='yandex.cloud.dataproc.manager.v1.HiveInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='available', full_name='yandex.cloud.dataproc.manager.v1.HiveInfo.available', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queries_succeeded', full_name='yandex.cloud.dataproc.manager.v1.HiveInfo.queries_succeeded', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queries_failed', full_name='yandex.cloud.dataproc.manager.v1.HiveInfo.queries_failed', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queries_executing', full_name='yandex.cloud.dataproc.manager.v1.HiveInfo.queries_executing', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessions_open', full_name='yandex.cloud.dataproc.manager.v1.HiveInfo.sessions_open', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessions_active', full_name='yandex.cloud.dataproc.manager.v1.HiveInfo.sessions_active', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=908,
  serialized_end=1063,
)


_YARNNODEINFO = _descriptor.Descriptor(
  name='YarnNodeInfo',
  full_name='yandex.cloud.dataproc.manager.v1.YarnNodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.dataproc.manager.v1.YarnNodeInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='yandex.cloud.dataproc.manager.v1.YarnNodeInfo.state', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_containers', full_name='yandex.cloud.dataproc.manager.v1.YarnNodeInfo.num_containers', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='used_memory_mb', full_name='yandex.cloud.dataproc.manager.v1.YarnNodeInfo.used_memory_mb', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_memory_mb', full_name='yandex.cloud.dataproc.manager.v1.YarnNodeInfo.available_memory_mb', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1065,
  serialized_end=1185,
)


_YARNINFO = _descriptor.Descriptor(
  name='YarnInfo',
  full_name='yandex.cloud.dataproc.manager.v1.YarnInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='available', full_name='yandex.cloud.dataproc.manager.v1.YarnInfo.available', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='live_nodes', full_name='yandex.cloud.dataproc.manager.v1.YarnInfo.live_nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1187,
  serialized_end=1284,
)


_ZOOKEEPERINFO = _descriptor.Descriptor(
  name='ZookeeperInfo',
  full_name='yandex.cloud.dataproc.manager.v1.ZookeeperInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alive', full_name='yandex.cloud.dataproc.manager.v1.ZookeeperInfo.alive', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1286,
  serialized_end=1316,
)


_OOZIEINFO = _descriptor.Descriptor(
  name='OozieInfo',
  full_name='yandex.cloud.dataproc.manager.v1.OozieInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alive', full_name='yandex.cloud.dataproc.manager.v1.OozieInfo.alive', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1318,
  serialized_end=1344,
)


_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='yandex.cloud.dataproc.manager.v1.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hdfs', full_name='yandex.cloud.dataproc.manager.v1.Info.hdfs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yarn', full_name='yandex.cloud.dataproc.manager.v1.Info.yarn', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hive', full_name='yandex.cloud.dataproc.manager.v1.Info.hive', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zookeeper', full_name='yandex.cloud.dataproc.manager.v1.Info.zookeeper', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hbase', full_name='yandex.cloud.dataproc.manager.v1.Info.hbase', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oozie', full_name='yandex.cloud.dataproc.manager.v1.Info.oozie', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1347,
  serialized_end=1715,
)


_REPORTREQUEST = _descriptor.Descriptor(
  name='ReportRequest',
  full_name='yandex.cloud.dataproc.manager.v1.ReportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cid', full_name='yandex.cloud.dataproc.manager.v1.ReportRequest.cid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topology_revision', full_name='yandex.cloud.dataproc.manager.v1.ReportRequest.topology_revision', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='yandex.cloud.dataproc.manager.v1.ReportRequest.info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1717,
  serialized_end=1826,
)


_REPORTREPLY = _descriptor.Descriptor(
  name='ReportReply',
  full_name='yandex.cloud.dataproc.manager.v1.ReportReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1828,
  serialized_end=1841,
)

_HBASEINFO.fields_by_name['live_nodes'].message_type = _HBASENODEINFO
_HBASEINFO.fields_by_name['dead_nodes'].message_type = _HBASENODEINFO
_HDFSINFO.fields_by_name['live_nodes'].message_type = _HDFSNODEINFO
_HDFSINFO.fields_by_name['dead_nodes'].message_type = _HDFSNODEINFO
_HDFSINFO.fields_by_name['decom_nodes'].message_type = _HDFSNODEINFO
_YARNINFO.fields_by_name['live_nodes'].message_type = _YARNNODEINFO
_INFO.fields_by_name['hdfs'].message_type = _HDFSINFO
_INFO.fields_by_name['yarn'].message_type = _YARNINFO
_INFO.fields_by_name['hive'].message_type = _HIVEINFO
_INFO.fields_by_name['zookeeper'].message_type = _ZOOKEEPERINFO
_INFO.fields_by_name['hbase'].message_type = _HBASEINFO
_INFO.fields_by_name['oozie'].message_type = _OOZIEINFO
_REPORTREQUEST.fields_by_name['info'].message_type = _INFO
DESCRIPTOR.message_types_by_name['HbaseNodeInfo'] = _HBASENODEINFO
DESCRIPTOR.message_types_by_name['HbaseInfo'] = _HBASEINFO
DESCRIPTOR.message_types_by_name['HDFSNodeInfo'] = _HDFSNODEINFO
DESCRIPTOR.message_types_by_name['HDFSInfo'] = _HDFSINFO
DESCRIPTOR.message_types_by_name['HiveInfo'] = _HIVEINFO
DESCRIPTOR.message_types_by_name['YarnNodeInfo'] = _YARNNODEINFO
DESCRIPTOR.message_types_by_name['YarnInfo'] = _YARNINFO
DESCRIPTOR.message_types_by_name['ZookeeperInfo'] = _ZOOKEEPERINFO
DESCRIPTOR.message_types_by_name['OozieInfo'] = _OOZIEINFO
DESCRIPTOR.message_types_by_name['Info'] = _INFO
DESCRIPTOR.message_types_by_name['ReportRequest'] = _REPORTREQUEST
DESCRIPTOR.message_types_by_name['ReportReply'] = _REPORTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HbaseNodeInfo = _reflection.GeneratedProtocolMessageType('HbaseNodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _HBASENODEINFO,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.HbaseNodeInfo)
  })
_sym_db.RegisterMessage(HbaseNodeInfo)

HbaseInfo = _reflection.GeneratedProtocolMessageType('HbaseInfo', (_message.Message,), {
  'DESCRIPTOR' : _HBASEINFO,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.HbaseInfo)
  })
_sym_db.RegisterMessage(HbaseInfo)

HDFSNodeInfo = _reflection.GeneratedProtocolMessageType('HDFSNodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _HDFSNODEINFO,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.HDFSNodeInfo)
  })
_sym_db.RegisterMessage(HDFSNodeInfo)

HDFSInfo = _reflection.GeneratedProtocolMessageType('HDFSInfo', (_message.Message,), {
  'DESCRIPTOR' : _HDFSINFO,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.HDFSInfo)
  })
_sym_db.RegisterMessage(HDFSInfo)

HiveInfo = _reflection.GeneratedProtocolMessageType('HiveInfo', (_message.Message,), {
  'DESCRIPTOR' : _HIVEINFO,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.HiveInfo)
  })
_sym_db.RegisterMessage(HiveInfo)

YarnNodeInfo = _reflection.GeneratedProtocolMessageType('YarnNodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _YARNNODEINFO,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.YarnNodeInfo)
  })
_sym_db.RegisterMessage(YarnNodeInfo)

YarnInfo = _reflection.GeneratedProtocolMessageType('YarnInfo', (_message.Message,), {
  'DESCRIPTOR' : _YARNINFO,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.YarnInfo)
  })
_sym_db.RegisterMessage(YarnInfo)

ZookeeperInfo = _reflection.GeneratedProtocolMessageType('ZookeeperInfo', (_message.Message,), {
  'DESCRIPTOR' : _ZOOKEEPERINFO,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.ZookeeperInfo)
  })
_sym_db.RegisterMessage(ZookeeperInfo)

OozieInfo = _reflection.GeneratedProtocolMessageType('OozieInfo', (_message.Message,), {
  'DESCRIPTOR' : _OOZIEINFO,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.OozieInfo)
  })
_sym_db.RegisterMessage(OozieInfo)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), {
  'DESCRIPTOR' : _INFO,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.Info)
  })
_sym_db.RegisterMessage(Info)

ReportRequest = _reflection.GeneratedProtocolMessageType('ReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTREQUEST,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.ReportRequest)
  })
_sym_db.RegisterMessage(ReportRequest)

ReportReply = _reflection.GeneratedProtocolMessageType('ReportReply', (_message.Message,), {
  'DESCRIPTOR' : _REPORTREPLY,
  '__module__' : 'yandex.cloud.dataproc.manager.v1.manager_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.manager.v1.ReportReply)
  })
_sym_db.RegisterMessage(ReportReply)


DESCRIPTOR._options = None

_DATAPROCMANAGERSERVICE = _descriptor.ServiceDescriptor(
  name='DataprocManagerService',
  full_name='yandex.cloud.dataproc.manager.v1.DataprocManagerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1844,
  serialized_end=1976,
  methods=[
  _descriptor.MethodDescriptor(
    name='Report',
    full_name='yandex.cloud.dataproc.manager.v1.DataprocManagerService.Report',
    index=0,
    containing_service=None,
    input_type=_REPORTREQUEST,
    output_type=_REPORTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAPROCMANAGERSERVICE)

DESCRIPTOR.services_by_name['DataprocManagerService'] = _DATAPROCMANAGERSERVICE

# @@protoc_insertion_point(module_scope)