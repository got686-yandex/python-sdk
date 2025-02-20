# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/mysql/v1/backup_service.proto
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
    'yandex/cloud/mdb/mysql/v1/backup_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.mdb.mysql.v1 import backup_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_backup__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/mdb/mysql/v1/backup_service.proto\x12\x19yandex.cloud.mdb.mysql.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a&yandex/cloud/mdb/mysql/v1/backup.proto\"+\n\x10GetBackupRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"s\n\x12ListBackupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"m\n\x13ListBackupsResponse\x12\x32\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32!.yandex.cloud.mdb.mysql.v1.Backup\x12\"\n\x0fnext_page_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\".\n\x13\x44\x65leteBackupRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"=\n\x14\x44\x65leteBackupMetadata\x12\x11\n\tbackup_id\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t2\xdf\x03\n\rBackupService\x12\x84\x01\n\x03Get\x12+.yandex.cloud.mdb.mysql.v1.GetBackupRequest\x1a!.yandex.cloud.mdb.mysql.v1.Backup\"-\x82\xd3\xe4\x93\x02\'\x12%/managed-mysql/v1/backups/{backup_id}\x12\x88\x01\n\x04List\x12-.yandex.cloud.mdb.mysql.v1.ListBackupsRequest\x1a..yandex.cloud.mdb.mysql.v1.ListBackupsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/managed-mysql/v1/backups\x12\xbb\x01\n\x06\x44\x65lete\x12..yandex.cloud.mdb.mysql.v1.DeleteBackupRequest\x1a!.yandex.cloud.operation.Operation\"^\xb2\xd2*-\n\x14\x44\x65leteBackupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\'*%/managed-mysql/v1/backups/{backup_id}Bd\n\x1dyandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysqlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mysql.v1.backup_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035yandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysql'
  _globals['_GETBACKUPREQUEST'].fields_by_name['backup_id']._loaded_options = None
  _globals['_GETBACKUPREQUEST'].fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTBACKUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTBACKUPSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
  _globals['_LISTBACKUPSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_DELETEBACKUPREQUEST'].fields_by_name['backup_id']._loaded_options = None
  _globals['_DELETEBACKUPREQUEST'].fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _globals['_BACKUPSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\'\022%/managed-mysql/v1/backups/{backup_id}'
  _globals['_BACKUPSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\033\022\031/managed-mysql/v1/backups'
  _globals['_BACKUPSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_BACKUPSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*-\n\024DeleteBackupMetadata\022\025google.protobuf.Empty\202\323\344\223\002\'*%/managed-mysql/v1/backups/{backup_id}'
  _globals['_GETBACKUPREQUEST']._serialized_start=252
  _globals['_GETBACKUPREQUEST']._serialized_end=295
  _globals['_LISTBACKUPSREQUEST']._serialized_start=297
  _globals['_LISTBACKUPSREQUEST']._serialized_end=412
  _globals['_LISTBACKUPSRESPONSE']._serialized_start=414
  _globals['_LISTBACKUPSRESPONSE']._serialized_end=523
  _globals['_DELETEBACKUPREQUEST']._serialized_start=525
  _globals['_DELETEBACKUPREQUEST']._serialized_end=571
  _globals['_DELETEBACKUPMETADATA']._serialized_start=573
  _globals['_DELETEBACKUPMETADATA']._serialized_end=634
  _globals['_BACKUPSERVICE']._serialized_start=637
  _globals['_BACKUPSERVICE']._serialized_end=1116
# @@protoc_insertion_point(module_scope)
