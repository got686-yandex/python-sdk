# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/backup/v1/backup.proto
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
    'yandex/cloud/backup/v1/backup.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.backup.v1 import policy_pb2 as yandex_dot_cloud_dot_backup_dot_v1_dot_policy__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#yandex/cloud/backup/v1/backup.proto\x12\x16yandex.cloud.backup.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\x1a#yandex/cloud/backup/v1/policy.proto\"\xc1\x08\n\x07\x41rchive\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08vault_id\x18\x03 \x01(\t\x12\x45\n\nattributes\x18\x04 \x01(\x0b\x32\x31.yandex.cloud.backup.v1.Archive.ArchiveAttributes\x12\x0c\n\x04size\x18\x05 \x01(\x03\x12\x1c\n\x14\x63ompressed_data_size\x18\x06 \x01(\x03\x12\x11\n\tdata_size\x18\x07 \x01(\x03\x12\x1a\n\x12original_data_size\x18\x08 \x01(\x03\x12\x14\n\x0clogical_size\x18\t \x01(\x03\x12.\n\x06\x66ormat\x18\n \x01(\x0e\x32\x1e.yandex.cloud.backup.v1.Format\x12.\n\ncreated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16last_backup_created_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_seen_at\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\x15protected_by_password\x18\x0f \x01(\x08\x12Q\n\x14\x65ncryption_algorithm\x18\x10 \x01(\x0e\x32\x33.yandex.cloud.backup.v1.Archive.EncryptionAlgorithm\x12\x37\n\x07\x61\x63tions\x18\x14 \x03(\x0e\x32&.yandex.cloud.backup.v1.Archive.Action\x12\x16\n\x0e\x62\x61\x63kup_plan_id\x18\x16 \x01(\t\x12\x18\n\x10\x62\x61\x63kup_plan_name\x18\x17 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x18 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x19 \x01(\t\x12\x1b\n\x13\x63ompute_instance_id\x18\x1a \x01(\t\x12\x12\n\nconsistent\x18\x1b \x01(\x08\x12\x0f\n\x07\x64\x65leted\x18\x1e \x01(\x08\x12\x13\n\x0bresource_id\x18\x1f \x01(\t\x1a.\n\x11\x41rchiveAttributes\x12\x0c\n\x04\x61\x61ib\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\"i\n\x13\x45ncryptionAlgorithm\x12$\n ENCRYPTION_ALGORITHM_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\n\n\x06\x41\x45S128\x10\x02\x12\n\n\x06\x41\x45S192\x10\x03\x12\n\n\x06\x41\x45S256\x10\x04\"B\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\x0b\n\x07REFRESH\x10\x01\x12\x13\n\x0f\x44\x45LETE_BY_AGENT\x10\x02J\x04\x08\x11\x10\x14J\x04\x08\x15\x10\x16J\x04\x08\x1c\x10\x1dJ\x04\x08\x1d\x10\x1e\"u\n\x06Volume\x12\x12\n\nfree_space\x18\x01 \x01(\x03\x12\x13\n\x0bis_bootable\x18\x02 \x01(\x08\x12\x11\n\tis_system\x18\x03 \x01(\x08\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\x03\x12\x13\n\x0bmount_strid\x18\x06 \x01(\t\"i\n\x04\x44isk\x12\x14\n\x0c\x64\x65vice_model\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x03\x12/\n\x07volumes\x18\x04 \x03(\x0b\x32\x1e.yandex.cloud.backup.v1.Volume\"\xfa\x04\n\x06\x42\x61\x63kup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08vault_id\x18\x02 \x01(\t\x12\x12\n\narchive_id\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_seen_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04size\x18\x06 \x01(\x03\x12\x19\n\x11\x64\x65\x64uplicated_size\x18\x07 \x01(\x03\x12\x1b\n\x13\x62\x61\x63ked_up_data_size\x18\x08 \x01(\x03\x12\x1a\n\x12original_data_size\x18\t \x01(\x03\x12\x43\n\nattributes\x18\n \x01(\x0b\x32/.yandex.cloud.backup.v1.Backup.BackupAttributes\x12\x1b\n\x13\x63ompute_instance_id\x18\x0b \x01(\t\x12+\n\x05\x64isks\x18\x0e \x03(\x0b\x32\x1c.yandex.cloud.backup.v1.Disk\x12\x31\n\x04type\x18\x0f \x01(\x0e\x32#.yandex.cloud.backup.v1.Backup.Type\x12\x0f\n\x07\x64\x65leted\x18\x15 \x01(\x08\x12\x11\n\tpolicy_id\x18\x16 \x01(\t\x12\x13\n\x0bresource_id\x18\x17 \x01(\t\x1a\x34\n\x10\x42\x61\x63kupAttributes\x12\x13\n\x0bstream_name\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\"7\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\x12\x0f\n\x0bINCREMENTAL\x10\x02J\x04\x08\x0c\x10\rJ\x04\x08\r\x10\x0eJ\x04\x08\x10\x10\x15\"\xc4\x03\n\nBackupFile\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x35\n\tparent_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x04\xe8\xc7\x31\x00\x12;\n\x04type\x18\x03 \x01(\x0e\x32\'.yandex.cloud.backup.v1.BackupFile.TypeB\x04\xe8\xc7\x31\x01\x12\x17\n\tfull_path\x18\x04 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x12\n\x04name\x18\x05 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x0c\n\x04size\x18\x06 \x01(\x03\x12\x41\n\x07\x61\x63tions\x18\x07 \x01(\x0b\x32*.yandex.cloud.backup.v1.BackupFile.ActionsB\x04\xe8\xc7\x31\x01\x12\x35\n\x0bmodified_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe8\xc7\x31\x01\x1a@\n\x07\x41\x63tions\x12\x17\n\x0frestore_to_disk\x18\x01 \x01(\x08\x12\x16\n\x0ego_to_location\x18\x02 \x01(\x08J\x04\x08\x03\x10\x04\"9\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08TYPE_DIR\x10\x01\x12\r\n\tTYPE_FILE\x10\x02\x42_\n\x1ayandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.backup.v1.backup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032yandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backup'
  _globals['_BACKUPFILE'].fields_by_name['id']._loaded_options = None
  _globals['_BACKUPFILE'].fields_by_name['id']._serialized_options = b'\350\3071\001'
  _globals['_BACKUPFILE'].fields_by_name['parent_id']._loaded_options = None
  _globals['_BACKUPFILE'].fields_by_name['parent_id']._serialized_options = b'\350\3071\000'
  _globals['_BACKUPFILE'].fields_by_name['type']._loaded_options = None
  _globals['_BACKUPFILE'].fields_by_name['type']._serialized_options = b'\350\3071\001'
  _globals['_BACKUPFILE'].fields_by_name['full_path']._loaded_options = None
  _globals['_BACKUPFILE'].fields_by_name['full_path']._serialized_options = b'\350\3071\001'
  _globals['_BACKUPFILE'].fields_by_name['name']._loaded_options = None
  _globals['_BACKUPFILE'].fields_by_name['name']._serialized_options = b'\350\3071\001'
  _globals['_BACKUPFILE'].fields_by_name['actions']._loaded_options = None
  _globals['_BACKUPFILE'].fields_by_name['actions']._serialized_options = b'\350\3071\001'
  _globals['_BACKUPFILE'].fields_by_name['modified_at']._loaded_options = None
  _globals['_BACKUPFILE'].fields_by_name['modified_at']._serialized_options = b'\350\3071\001'
  _globals['_ARCHIVE']._serialized_start=197
  _globals['_ARCHIVE']._serialized_end=1286
  _globals['_ARCHIVE_ARCHIVEATTRIBUTES']._serialized_start=1041
  _globals['_ARCHIVE_ARCHIVEATTRIBUTES']._serialized_end=1087
  _globals['_ARCHIVE_ENCRYPTIONALGORITHM']._serialized_start=1089
  _globals['_ARCHIVE_ENCRYPTIONALGORITHM']._serialized_end=1194
  _globals['_ARCHIVE_ACTION']._serialized_start=1196
  _globals['_ARCHIVE_ACTION']._serialized_end=1262
  _globals['_VOLUME']._serialized_start=1288
  _globals['_VOLUME']._serialized_end=1405
  _globals['_DISK']._serialized_start=1407
  _globals['_DISK']._serialized_end=1512
  _globals['_BACKUP']._serialized_start=1515
  _globals['_BACKUP']._serialized_end=2149
  _globals['_BACKUP_BACKUPATTRIBUTES']._serialized_start=2022
  _globals['_BACKUP_BACKUPATTRIBUTES']._serialized_end=2074
  _globals['_BACKUP_TYPE']._serialized_start=2076
  _globals['_BACKUP_TYPE']._serialized_end=2131
  _globals['_BACKUPFILE']._serialized_start=2152
  _globals['_BACKUPFILE']._serialized_end=2604
  _globals['_BACKUPFILE_ACTIONS']._serialized_start=2481
  _globals['_BACKUPFILE_ACTIONS']._serialized_end=2545
  _globals['_BACKUPFILE_TYPE']._serialized_start=2547
  _globals['_BACKUPFILE_TYPE']._serialized_end=2604
# @@protoc_insertion_point(module_scope)
