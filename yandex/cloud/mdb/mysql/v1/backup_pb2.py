# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/mysql/v1/backup.proto
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
    'yandex/cloud/mdb/mysql/v1/backup.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&yandex/cloud/mdb/mysql/v1/backup.proto\x12\x19yandex.cloud.mdb.mysql.v1\x1a\x1dyandex/cloud/validation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd8\x03\n\x06\x42\x61\x63kup\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x11source_cluster_id\x18\x04 \x01(\t\x12.\n\nstarted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04size\x18\x06 \x01(\x03\x12\x42\n\x04type\x18\x07 \x01(\x0e\x32\x34.yandex.cloud.mdb.mysql.v1.Backup.BackupCreationType\x12>\n\x06status\x18\x08 \x01(\x0e\x32..yandex.cloud.mdb.mysql.v1.Backup.BackupStatus\"U\n\x12\x42\x61\x63kupCreationType\x12$\n BACKUP_CREATION_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tAUTOMATED\x10\x01\x12\n\n\x06MANUAL\x10\x02\"E\n\x0c\x42\x61\x63kupStatus\x12\x1d\n\x19\x42\x41\x43KUP_STATUS_UNSPECIFIED\x10\x00\x12\x08\n\x04\x44ONE\x10\x01\x12\x0c\n\x08\x43REATING\x10\x02\x42\x64\n\x1dyandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysqlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mysql.v1.backup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035yandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysql'
  _globals['_BACKUP'].fields_by_name['id']._loaded_options = None
  _globals['_BACKUP'].fields_by_name['id']._serialized_options = b'\350\3071\001'
  _globals['_BACKUP']._serialized_start=134
  _globals['_BACKUP']._serialized_end=606
  _globals['_BACKUP_BACKUPCREATIONTYPE']._serialized_start=450
  _globals['_BACKUP_BACKUPCREATIONTYPE']._serialized_end=535
  _globals['_BACKUP_BACKUPSTATUS']._serialized_start=537
  _globals['_BACKUP_BACKUPSTATUS']._serialized_end=606
# @@protoc_insertion_point(module_scope)
