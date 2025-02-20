# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ydb/v1/backup_service.proto
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
    'yandex/cloud/ydb/v1/backup_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.ydb.v1 import backup_pb2 as yandex_dot_cloud_dot_ydb_dot_v1_dot_backup__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/ydb/v1/backup_service.proto\x12\x13yandex.cloud.ydb.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a yandex/cloud/access/access.proto\x1a\x1dyandex/cloud/validation.proto\x1a yandex/cloud/ydb/v1/backup.proto\"q\n\x10ListPathsRequest\x12\x1f\n\tbackup_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\";\n\x11ListPathsResponse\x12\r\n\x05paths\x18\x01 \x03(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"3\n\x10GetBackupRequest\x12\x1f\n\tbackup_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"e\n\x12ListBackupsRequest\x12\x11\n\tfolder_id\x18\x01 \x01(\t\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\\\n\x13ListBackupsResponse\x12,\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32\x1b.yandex.cloud.ydb.v1.Backup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"(\n\x13\x44\x65leteBackupRequest\x12\x11\n\tbackup_id\x18\x01 \x01(\t\">\n\x14\x44\x65leteBackupMetadata\x12\x11\n\tbackup_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x61tabase_id\x18\x02 \x01(\t2\xf7\x07\n\rBackupService\x12n\n\x03Get\x12%.yandex.cloud.ydb.v1.GetBackupRequest\x1a\x1b.yandex.cloud.ydb.v1.Backup\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/ydb/v1/backups/{backup_id}\x12\x85\x01\n\tListPaths\x12%.yandex.cloud.ydb.v1.ListPathsRequest\x1a&.yandex.cloud.ydb.v1.ListPathsResponse\")\x82\xd3\xe4\x93\x02#\x12!/ydb/v1/backups/{backup_id}/paths\x12r\n\x04List\x12\'.yandex.cloud.ydb.v1.ListBackupsRequest\x1a(.yandex.cloud.ydb.v1.ListBackupsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/ydb/v1/backups\x12u\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\x12\xa4\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"=\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x12\xad\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"@\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x12\xab\x01\n\x06\x44\x65lete\x12(.yandex.cloud.ydb.v1.DeleteBackupRequest\x1a!.yandex.cloud.operation.Operation\"T\xb2\xd2*-\n\x14\x44\x65leteBackupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1d*\x1b/ydb/v1/backups/{backup_id}BV\n\x17yandex.cloud.api.ydb.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1;ydbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ydb.v1.backup_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.ydb.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1;ydb'
  _globals['_LISTPATHSREQUEST'].fields_by_name['backup_id']._loaded_options = None
  _globals['_LISTPATHSREQUEST'].fields_by_name['backup_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTPATHSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTPATHSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTPATHSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTPATHSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_GETBACKUPREQUEST'].fields_by_name['backup_id']._loaded_options = None
  _globals['_GETBACKUPREQUEST'].fields_by_name['backup_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_BACKUPSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\035\022\033/ydb/v1/backups/{backup_id}'
  _globals['_BACKUPSERVICE'].methods_by_name['ListPaths']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['ListPaths']._serialized_options = b'\202\323\344\223\002#\022!/ydb/v1/backups/{backup_id}/paths'
  _globals['_BACKUPSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\021\022\017/ydb/v1/backups'
  _globals['_BACKUPSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty'
  _globals['_BACKUPSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty'
  _globals['_BACKUPSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*-\n\024DeleteBackupMetadata\022\025google.protobuf.Empty\202\323\344\223\002\035*\033/ydb/v1/backups/{backup_id}'
  _globals['_LISTPATHSREQUEST']._serialized_start=268
  _globals['_LISTPATHSREQUEST']._serialized_end=381
  _globals['_LISTPATHSRESPONSE']._serialized_start=383
  _globals['_LISTPATHSRESPONSE']._serialized_end=442
  _globals['_GETBACKUPREQUEST']._serialized_start=444
  _globals['_GETBACKUPREQUEST']._serialized_end=495
  _globals['_LISTBACKUPSREQUEST']._serialized_start=497
  _globals['_LISTBACKUPSREQUEST']._serialized_end=598
  _globals['_LISTBACKUPSRESPONSE']._serialized_start=600
  _globals['_LISTBACKUPSRESPONSE']._serialized_end=692
  _globals['_DELETEBACKUPREQUEST']._serialized_start=694
  _globals['_DELETEBACKUPREQUEST']._serialized_end=734
  _globals['_DELETEBACKUPMETADATA']._serialized_start=736
  _globals['_DELETEBACKUPMETADATA']._serialized_end=798
  _globals['_BACKUPSERVICE']._serialized_start=801
  _globals['_BACKUPSERVICE']._serialized_end=1816
# @@protoc_insertion_point(module_scope)
