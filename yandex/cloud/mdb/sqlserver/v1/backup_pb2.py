# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/sqlserver/v1/backup.proto
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
    'yandex/cloud/mdb/sqlserver/v1/backup.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/mdb/sqlserver/v1/backup.proto\x12\x1dyandex.cloud.mdb.sqlserver.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb5\x01\n\x06\x42\x61\x63kup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x11source_cluster_id\x18\x04 \x01(\t\x12.\n\nstarted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tdatabases\x18\x06 \x03(\tBu\n!yandex.cloud.api.mdb.sqlserver.v1B\x03PSBZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/sqlserver/v1;sqlserverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.sqlserver.v1.backup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!yandex.cloud.api.mdb.sqlserver.v1B\003PSBZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/sqlserver/v1;sqlserver'
  _globals['_BACKUP']._serialized_start=111
  _globals['_BACKUP']._serialized_end=292
# @@protoc_insertion_point(module_scope)
