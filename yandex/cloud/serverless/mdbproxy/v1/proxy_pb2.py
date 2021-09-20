# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/mdbproxy/v1/proxy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/serverless/mdbproxy/v1/proxy.proto',
  package='yandex.cloud.serverless.mdbproxy.v1',
  syntax='proto3',
  serialized_options=b'\n\'yandex.cloud.api.serverless.mdbproxy.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/mdbproxy/v1;proxy',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/yandex/cloud/serverless/mdbproxy/v1/proxy.proto\x12#yandex.cloud.serverless.mdbproxy.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xac\x03\n\x05Proxy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1f\n\tfolder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x04name\x18\x04 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x8f\x01\n\x06labels\x18\x06 \x03(\x0b\x32\x36.yandex.cloud.serverless.mdbproxy.v1.Proxy.LabelsEntryBG\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x16\x12\x14[a-z][-_./\\@0-9a-z]*\x12;\n\x06target\x18\x07 \x01(\x0b\x32+.yandex.cloud.serverless.mdbproxy.v1.Target\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8e\x04\n\x06Target\x12L\n\nclickhouse\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.serverless.mdbproxy.v1.Target.ClickHouseH\x00\x12L\n\npostgresql\x18\x02 \x01(\x0b\x32\x36.yandex.cloud.serverless.mdbproxy.v1.Target.PostgreSQLH\x00\x1a\xac\x01\n\nPostgreSQL\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12,\n\x04user\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12\x10\n\x08password\x18\x03 \x01(\t\x12*\n\x02\x64\x62\x18\x04 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12\x10\n\x08\x65ndpoint\x18\x05 \x01(\t\x1a\xab\x01\n\nClickHouse\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12+\n\x04user\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12\x10\n\x08password\x18\x03 \x01(\t\x12*\n\x02\x64\x62\x18\x04 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12\x10\n\x08\x65ndpoint\x18\x05 \x01(\tB\x0b\n\x03mdb\x12\x04\xc0\xc1\x31\x01\x42x\n\'yandex.cloud.api.serverless.mdbproxy.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/mdbproxy/v1;proxyb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_PROXY_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy.LabelsEntry.value', index=1,
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
  serialized_start=536,
  serialized_end=581,
)

_PROXY = _descriptor.Descriptor(
  name='Proxy',
  full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\004<=64\212\3101\004<=63\362\3071\017[-_./\\@0-9a-z]*\262\3101\006\032\0041-63\262\3101\026\022\024[a-z][-_./\\@0-9a-z]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='yandex.cloud.serverless.mdbproxy.v1.Proxy.target', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PROXY_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=581,
)


_TARGET_POSTGRESQL = _descriptor.Descriptor(
  name='PostgreSQL',
  full_name='yandex.cloud.serverless.mdbproxy.v1.Target.PostgreSQL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.PostgreSQL.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.PostgreSQL.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.PostgreSQL.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='db', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.PostgreSQL.db', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.PostgreSQL.endpoint', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=751,
  serialized_end=923,
)

_TARGET_CLICKHOUSE = _descriptor.Descriptor(
  name='ClickHouse',
  full_name='yandex.cloud.serverless.mdbproxy.v1.Target.ClickHouse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.ClickHouse.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.ClickHouse.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.ClickHouse.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='db', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.ClickHouse.db', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.ClickHouse.endpoint', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=926,
  serialized_end=1097,
)

_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='yandex.cloud.serverless.mdbproxy.v1.Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clickhouse', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.clickhouse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postgresql', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.postgresql', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TARGET_POSTGRESQL, _TARGET_CLICKHOUSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='mdb', full_name='yandex.cloud.serverless.mdbproxy.v1.Target.mdb',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=584,
  serialized_end=1110,
)

_PROXY_LABELSENTRY.containing_type = _PROXY
_PROXY.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PROXY.fields_by_name['labels'].message_type = _PROXY_LABELSENTRY
_PROXY.fields_by_name['target'].message_type = _TARGET
_TARGET_POSTGRESQL.containing_type = _TARGET
_TARGET_CLICKHOUSE.containing_type = _TARGET
_TARGET.fields_by_name['clickhouse'].message_type = _TARGET_CLICKHOUSE
_TARGET.fields_by_name['postgresql'].message_type = _TARGET_POSTGRESQL
_TARGET.oneofs_by_name['mdb'].fields.append(
  _TARGET.fields_by_name['clickhouse'])
_TARGET.fields_by_name['clickhouse'].containing_oneof = _TARGET.oneofs_by_name['mdb']
_TARGET.oneofs_by_name['mdb'].fields.append(
  _TARGET.fields_by_name['postgresql'])
_TARGET.fields_by_name['postgresql'].containing_oneof = _TARGET.oneofs_by_name['mdb']
DESCRIPTOR.message_types_by_name['Proxy'] = _PROXY
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Proxy = _reflection.GeneratedProtocolMessageType('Proxy', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROXY_LABELSENTRY,
    '__module__' : 'yandex.cloud.serverless.mdbproxy.v1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.mdbproxy.v1.Proxy.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _PROXY,
  '__module__' : 'yandex.cloud.serverless.mdbproxy.v1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.mdbproxy.v1.Proxy)
  })
_sym_db.RegisterMessage(Proxy)
_sym_db.RegisterMessage(Proxy.LabelsEntry)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {

  'PostgreSQL' : _reflection.GeneratedProtocolMessageType('PostgreSQL', (_message.Message,), {
    'DESCRIPTOR' : _TARGET_POSTGRESQL,
    '__module__' : 'yandex.cloud.serverless.mdbproxy.v1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.mdbproxy.v1.Target.PostgreSQL)
    })
  ,

  'ClickHouse' : _reflection.GeneratedProtocolMessageType('ClickHouse', (_message.Message,), {
    'DESCRIPTOR' : _TARGET_CLICKHOUSE,
    '__module__' : 'yandex.cloud.serverless.mdbproxy.v1.proxy_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.mdbproxy.v1.Target.ClickHouse)
    })
  ,
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'yandex.cloud.serverless.mdbproxy.v1.proxy_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.mdbproxy.v1.Target)
  })
_sym_db.RegisterMessage(Target)
_sym_db.RegisterMessage(Target.PostgreSQL)
_sym_db.RegisterMessage(Target.ClickHouse)


DESCRIPTOR._options = None
_PROXY_LABELSENTRY._options = None
_PROXY.fields_by_name['folder_id']._options = None
_PROXY.fields_by_name['name']._options = None
_PROXY.fields_by_name['labels']._options = None
_TARGET_POSTGRESQL.fields_by_name['cluster_id']._options = None
_TARGET_POSTGRESQL.fields_by_name['user']._options = None
_TARGET_POSTGRESQL.fields_by_name['db']._options = None
_TARGET_CLICKHOUSE.fields_by_name['cluster_id']._options = None
_TARGET_CLICKHOUSE.fields_by_name['user']._options = None
_TARGET_CLICKHOUSE.fields_by_name['db']._options = None
_TARGET.oneofs_by_name['mdb']._options = None
# @@protoc_insertion_point(module_scope)
