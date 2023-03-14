# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/mysql.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.datatransfer.v1.endpoint import common_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datatransfer/v1/endpoint/mysql.proto',
  package='yandex.cloud.datatransfer.v1.endpoint',
  syntax='proto3',
  serialized_options=b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\252\002%Yandex.Cloud.Datatransfer.V1.EndPoint',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1yandex/cloud/datatransfer/v1/endpoint/mysql.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x32yandex/cloud/datatransfer/v1/endpoint/common.proto\"\x82\x01\n\x0eOnPremiseMysql\x12\r\n\x05hosts\x18\x05 \x03(\t\x12\x0c\n\x04port\x18\x02 \x01(\x03\x12@\n\x08tls_mode\x18\x06 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.endpoint.TLSMode\x12\x11\n\tsubnet_id\x18\x04 \x01(\t\"\x86\x01\n\x0fMysqlConnection\x12\x18\n\x0emdb_cluster_id\x18\x01 \x01(\tH\x00\x12K\n\non_premise\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.datatransfer.v1.endpoint.OnPremiseMysqlH\x00\x42\x0c\n\nconnection\"\xcd\x02\n\x1bMysqlObjectTransferSettings\x12H\n\x04view\x18\x01 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12K\n\x07routine\x18\x02 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12K\n\x07trigger\x18\x03 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12J\n\x06tables\x18\x04 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\"\xa1\x03\n\x0bMysqlSource\x12J\n\nconnection\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.datatransfer.v1.endpoint.MysqlConnection\x12\x17\n\x0fsecurity_groups\x18\x0e \x03(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x18\n\x10service_database\x18\x0f \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12?\n\x08password\x18\x04 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12\x1c\n\x14include_tables_regex\x18\x0c \x03(\t\x12\x1c\n\x14\x65xclude_tables_regex\x18\r \x03(\t\x12\x10\n\x08timezone\x18\x08 \x01(\t\x12\x64\n\x18object_transfer_settings\x18\x0b \x01(\x0b\x32\x42.yandex.cloud.datatransfer.v1.endpoint.MysqlObjectTransferSettings\"\xff\x02\n\x0bMysqlTarget\x12J\n\nconnection\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.datatransfer.v1.endpoint.MysqlConnection\x12\x17\n\x0fsecurity_groups\x18\x10 \x03(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12?\n\x08password\x18\x04 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12\x10\n\x08sql_mode\x18\x05 \x01(\t\x12\x1e\n\x16skip_constraint_checks\x18\x06 \x01(\x08\x12\x10\n\x08timezone\x18\x07 \x01(\t\x12L\n\x0e\x63leanup_policy\x18\x08 \x01(\x0e\x32\x34.yandex.cloud.datatransfer.v1.endpoint.CleanupPolicy\x12\x18\n\x10service_database\x18\x0f \x01(\tB\xa7\x01\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\xaa\x02%Yandex.Cloud.Datatransfer.V1.EndPointb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2.DESCRIPTOR,])




_ONPREMISEMYSQL = _descriptor.Descriptor(
  name='OnPremiseMysql',
  full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremiseMysql',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hosts', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremiseMysql.hosts', index=0,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremiseMysql.port', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tls_mode', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremiseMysql.tls_mode', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremiseMysql.subnet_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=145,
  serialized_end=275,
)


_MYSQLCONNECTION = _descriptor.Descriptor(
  name='MysqlConnection',
  full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mdb_cluster_id', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlConnection.mdb_cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='on_premise', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlConnection.on_premise', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='connection', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlConnection.connection',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=278,
  serialized_end=412,
)


_MYSQLOBJECTTRANSFERSETTINGS = _descriptor.Descriptor(
  name='MysqlObjectTransferSettings',
  full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlObjectTransferSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='view', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlObjectTransferSettings.view', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='routine', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlObjectTransferSettings.routine', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlObjectTransferSettings.trigger', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tables', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlObjectTransferSettings.tables', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=415,
  serialized_end=748,
)


_MYSQLSOURCE = _descriptor.Descriptor(
  name='MysqlSource',
  full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource.connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security_groups', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource.security_groups', index=1,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource.database', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_database', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource.service_database', index=3,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource.user', index=4,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource.password', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='include_tables_regex', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource.include_tables_regex', index=6,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exclude_tables_regex', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource.exclude_tables_regex', index=7,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource.timezone', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object_transfer_settings', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlSource.object_transfer_settings', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_end=1168,
)


_MYSQLTARGET = _descriptor.Descriptor(
  name='MysqlTarget',
  full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget.connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security_groups', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget.security_groups', index=1,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget.database', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget.user', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget.password', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sql_mode', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget.sql_mode', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skip_constraint_checks', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget.skip_constraint_checks', index=6,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget.timezone', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cleanup_policy', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget.cleanup_policy', index=8,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_database', full_name='yandex.cloud.datatransfer.v1.endpoint.MysqlTarget.service_database', index=9,
      number=15, type=9, cpp_type=9, label=1,
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
  serialized_start=1171,
  serialized_end=1554,
)

_ONPREMISEMYSQL.fields_by_name['tls_mode'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._TLSMODE
_MYSQLCONNECTION.fields_by_name['on_premise'].message_type = _ONPREMISEMYSQL
_MYSQLCONNECTION.oneofs_by_name['connection'].fields.append(
  _MYSQLCONNECTION.fields_by_name['mdb_cluster_id'])
_MYSQLCONNECTION.fields_by_name['mdb_cluster_id'].containing_oneof = _MYSQLCONNECTION.oneofs_by_name['connection']
_MYSQLCONNECTION.oneofs_by_name['connection'].fields.append(
  _MYSQLCONNECTION.fields_by_name['on_premise'])
_MYSQLCONNECTION.fields_by_name['on_premise'].containing_oneof = _MYSQLCONNECTION.oneofs_by_name['connection']
_MYSQLOBJECTTRANSFERSETTINGS.fields_by_name['view'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_MYSQLOBJECTTRANSFERSETTINGS.fields_by_name['routine'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_MYSQLOBJECTTRANSFERSETTINGS.fields_by_name['trigger'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_MYSQLOBJECTTRANSFERSETTINGS.fields_by_name['tables'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_MYSQLSOURCE.fields_by_name['connection'].message_type = _MYSQLCONNECTION
_MYSQLSOURCE.fields_by_name['password'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._SECRET
_MYSQLSOURCE.fields_by_name['object_transfer_settings'].message_type = _MYSQLOBJECTTRANSFERSETTINGS
_MYSQLTARGET.fields_by_name['connection'].message_type = _MYSQLCONNECTION
_MYSQLTARGET.fields_by_name['password'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._SECRET
_MYSQLTARGET.fields_by_name['cleanup_policy'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._CLEANUPPOLICY
DESCRIPTOR.message_types_by_name['OnPremiseMysql'] = _ONPREMISEMYSQL
DESCRIPTOR.message_types_by_name['MysqlConnection'] = _MYSQLCONNECTION
DESCRIPTOR.message_types_by_name['MysqlObjectTransferSettings'] = _MYSQLOBJECTTRANSFERSETTINGS
DESCRIPTOR.message_types_by_name['MysqlSource'] = _MYSQLSOURCE
DESCRIPTOR.message_types_by_name['MysqlTarget'] = _MYSQLTARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OnPremiseMysql = _reflection.GeneratedProtocolMessageType('OnPremiseMysql', (_message.Message,), {
  'DESCRIPTOR' : _ONPREMISEMYSQL,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.mysql_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.OnPremiseMysql)
  })
_sym_db.RegisterMessage(OnPremiseMysql)

MysqlConnection = _reflection.GeneratedProtocolMessageType('MysqlConnection', (_message.Message,), {
  'DESCRIPTOR' : _MYSQLCONNECTION,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.mysql_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.MysqlConnection)
  })
_sym_db.RegisterMessage(MysqlConnection)

MysqlObjectTransferSettings = _reflection.GeneratedProtocolMessageType('MysqlObjectTransferSettings', (_message.Message,), {
  'DESCRIPTOR' : _MYSQLOBJECTTRANSFERSETTINGS,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.mysql_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.MysqlObjectTransferSettings)
  })
_sym_db.RegisterMessage(MysqlObjectTransferSettings)

MysqlSource = _reflection.GeneratedProtocolMessageType('MysqlSource', (_message.Message,), {
  'DESCRIPTOR' : _MYSQLSOURCE,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.mysql_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.MysqlSource)
  })
_sym_db.RegisterMessage(MysqlSource)

MysqlTarget = _reflection.GeneratedProtocolMessageType('MysqlTarget', (_message.Message,), {
  'DESCRIPTOR' : _MYSQLTARGET,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.mysql_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.MysqlTarget)
  })
_sym_db.RegisterMessage(MysqlTarget)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
