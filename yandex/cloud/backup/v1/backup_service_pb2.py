# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/backup/v1/backup_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.backup.v1 import backup_pb2 as yandex_dot_cloud_dot_backup_dot_v1_dot_backup__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/backup/v1/backup_service.proto\x12\x16yandex.cloud.backup.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a#yandex/cloud/backup/v1/backup.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"U\n\x13ListArchivesRequest\x12\x13\n\tfolder_id\x18\x01 \x01(\tH\x00\x12\x1d\n\x13\x63ompute_instance_id\x18\x02 \x01(\tH\x00\x42\n\n\x02id\x12\x04\xc0\xc1\x31\x01\"I\n\x14ListArchivesResponse\x12\x31\n\x08\x61rchives\x18\x01 \x03(\x0b\x32\x1f.yandex.cloud.backup.v1.Archive\"\xd3\x03\n\x12ListBackupsRequest\x12\x1d\n\x13\x63ompute_instance_id\x18\x01 \x01(\tH\x00\x12O\n\x07\x61rchive\x18\x02 \x01(\x0b\x32<.yandex.cloud.backup.v1.ListBackupsRequest.ArchiveParametersH\x00\x12\x13\n\tfolder_id\x18\x03 \x01(\tH\x00\x12T\n\x0finstance_policy\x18\x04 \x01(\x0b\x32\x39.yandex.cloud.backup.v1.ListBackupsRequest.InstancePolicyH\x00\x12\x15\n\x0bresource_id\x18\x06 \x01(\tH\x00\x12\x13\n\tpolicy_id\x18\x07 \x01(\tH\x00\x12\x10\n\x08order_by\x18\x05 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x08 \x01(\t\x1a\x46\n\x11\x41rchiveParameters\x12\x18\n\narchive_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x17\n\tfolder_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x1a@\n\x0eInstancePolicy\x12\x1b\n\x13\x63ompute_instance_id\x18\x01 \x01(\t\x12\x11\n\tpolicy_id\x18\x02 \x01(\tB\n\n\x02id\x12\x04\xc0\xc1\x31\x01\"F\n\x13ListBackupsResponse\x12/\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.backup.v1.Backup\"]\n\x10ListFilesRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x17\n\tbackup_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x17\n\tsource_id\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x00\"F\n\x11ListFilesResponse\x12\x31\n\x05\x66iles\x18\x01 \x03(\x0b\x32\".yandex.cloud.backup.v1.BackupFile\"D\n\x10GetBackupRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x17\n\tfolder_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"Z\n\x14StartRecoveryRequest\x12)\n\x13\x63ompute_instance_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x17\n\tbackup_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"l\n\x15StartRecoveryMetadata\x12\x1b\n\x13progress_percentage\x18\x01 \x01(\x01\x12\x15\n\rsrc_backup_id\x18\x02 \x01(\t\x12\x1f\n\x17\x64st_compute_instance_id\x18\x03 \x01(\t\"\x14\n\x12TargetPathOriginal\" \n\x10TargetPathCustom\x12\x0c\n\x04path\x18\x01 \x01(\t\"\xf5\x02\n\x14\x46ilesRecoveryOptions\x12O\n\toverwrite\x18\x01 \x01(\x0e\x32\x36.yandex.cloud.backup.v1.FilesRecoveryOptions.OverwriteB\x04\xe8\xc7\x31\x00\x12\x1e\n\x10reboot_if_needed\x18\x02 \x01(\x08\x42\x04\xe8\xc7\x31\x00\x12>\n\x08original\x18\x64 \x01(\x0b\x32*.yandex.cloud.backup.v1.TargetPathOriginalH\x00\x12:\n\x06\x63ustom\x18\x65 \x01(\x0b\x32(.yandex.cloud.backup.v1.TargetPathCustomH\x00\"b\n\tOverwrite\x12\x19\n\x15OVERWRITE_UNSPECIFIED\x10\x00\x12\x11\n\rOVERWRITE_ALL\x10\x01\x12\x13\n\x0fOVERWRITE_OLDER\x10\x02\x12\x12\n\x0eOVERWRITE_NONE\x10\x03\x42\x0c\n\x04type\x12\x04\xc0\xc1\x31\x01\"\xb5\x01\n\x19StartFilesRecoveryRequest\x12!\n\x13\x63ompute_instance_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x17\n\tbackup_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12@\n\x04opts\x18\x03 \x01(\x0b\x32,.yandex.cloud.backup.v1.FilesRecoveryOptionsB\x04\xe8\xc7\x31\x01\x12\x1a\n\nsource_ids\x18\x04 \x03(\tB\x06\x82\xc8\x31\x02>0\"\x91\x01\n\x1aStartFilesRecoveryMetadata\x12\x1b\n\x13progress_percentage\x18\x01 \x01(\x01\x12!\n\x13\x63ompute_instance_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x17\n\tbackup_id\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1a\n\nsource_ids\x18\x04 \x03(\tB\x06\x82\xc8\x31\x02>0\"Y\n\x13\x44\x65leteBackupRequest\x12)\n\x13\x63ompute_instance_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x17\n\tbackup_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"F\n\x14\x44\x65leteBackupMetadata\x12\x1b\n\x13\x63ompute_instance_id\x18\x01 \x01(\t\x12\x11\n\tbackup_id\x18\x02 \x01(\t2\xfb\x08\n\rBackupService\x12{\n\x04List\x12*.yandex.cloud.backup.v1.ListBackupsRequest\x1a+.yandex.cloud.backup.v1.ListBackupsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/backup/v1/backups\x12\xa4\x01\n\x0cListArchives\x12+.yandex.cloud.backup.v1.ListArchivesRequest\x1a,.yandex.cloud.backup.v1.ListArchivesResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/backup/v1/backups/{compute_instance_id}/archives\x12\x8e\x01\n\tListFiles\x12(.yandex.cloud.backup.v1.ListFilesRequest\x1a).yandex.cloud.backup.v1.ListFilesResponse\",\x82\xd3\xe4\x93\x02&\x12$/backup/v1/backups/{backup_id}/files\x12w\n\x03Get\x12(.yandex.cloud.backup.v1.GetBackupRequest\x1a\x1e.yandex.cloud.backup.v1.Backup\"&\x82\xd3\xe4\x93\x02 \x12\x1e/backup/v1/backups/{backup_id}\x12\xcb\x01\n\rStartRecovery\x12,.yandex.cloud.backup.v1.StartRecoveryRequest\x1a!.yandex.cloud.operation.Operation\"i\xb2\xd2*.\n\x15StartRecoveryMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x31\",/backup/v1/backups/{backup_id}:startRecovery:\x01*\x12\xa3\x01\n\x12StartFilesRecovery\x12\x31.yandex.cloud.backup.v1.StartFilesRecoveryRequest\x1a!.yandex.cloud.operation.Operation\"7\xb2\xd2*3\n\x1aStartFilesRecoveryMetadata\x12\x15google.protobuf.Empty\x12\xc7\x01\n\x06\x44\x65lete\x12+.yandex.cloud.backup.v1.DeleteBackupRequest\x1a!.yandex.cloud.operation.Operation\"m\xb2\xd2*-\n\x14\x44\x65leteBackupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x36*4/backup/v1/backups/{compute_instance_id}/{backup_id}B_\n\x1ayandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.backup.v1.backup_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032yandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backup'
  _LISTARCHIVESREQUEST.oneofs_by_name['id']._options = None
  _LISTARCHIVESREQUEST.oneofs_by_name['id']._serialized_options = b'\300\3011\001'
  _LISTBACKUPSREQUEST_ARCHIVEPARAMETERS.fields_by_name['archive_id']._options = None
  _LISTBACKUPSREQUEST_ARCHIVEPARAMETERS.fields_by_name['archive_id']._serialized_options = b'\350\3071\001'
  _LISTBACKUPSREQUEST_ARCHIVEPARAMETERS.fields_by_name['folder_id']._options = None
  _LISTBACKUPSREQUEST_ARCHIVEPARAMETERS.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _LISTBACKUPSREQUEST.oneofs_by_name['id']._options = None
  _LISTBACKUPSREQUEST.oneofs_by_name['id']._serialized_options = b'\300\3011\001'
  _LISTFILESREQUEST.fields_by_name['folder_id']._options = None
  _LISTFILESREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _LISTFILESREQUEST.fields_by_name['backup_id']._options = None
  _LISTFILESREQUEST.fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _LISTFILESREQUEST.fields_by_name['source_id']._options = None
  _LISTFILESREQUEST.fields_by_name['source_id']._serialized_options = b'\350\3071\000'
  _GETBACKUPREQUEST.fields_by_name['backup_id']._options = None
  _GETBACKUPREQUEST.fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _GETBACKUPREQUEST.fields_by_name['folder_id']._options = None
  _GETBACKUPREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _STARTRECOVERYREQUEST.fields_by_name['compute_instance_id']._options = None
  _STARTRECOVERYREQUEST.fields_by_name['compute_instance_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _STARTRECOVERYREQUEST.fields_by_name['backup_id']._options = None
  _STARTRECOVERYREQUEST.fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _FILESRECOVERYOPTIONS.oneofs_by_name['type']._options = None
  _FILESRECOVERYOPTIONS.oneofs_by_name['type']._serialized_options = b'\300\3011\001'
  _FILESRECOVERYOPTIONS.fields_by_name['overwrite']._options = None
  _FILESRECOVERYOPTIONS.fields_by_name['overwrite']._serialized_options = b'\350\3071\000'
  _FILESRECOVERYOPTIONS.fields_by_name['reboot_if_needed']._options = None
  _FILESRECOVERYOPTIONS.fields_by_name['reboot_if_needed']._serialized_options = b'\350\3071\000'
  _STARTFILESRECOVERYREQUEST.fields_by_name['compute_instance_id']._options = None
  _STARTFILESRECOVERYREQUEST.fields_by_name['compute_instance_id']._serialized_options = b'\350\3071\001'
  _STARTFILESRECOVERYREQUEST.fields_by_name['backup_id']._options = None
  _STARTFILESRECOVERYREQUEST.fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _STARTFILESRECOVERYREQUEST.fields_by_name['opts']._options = None
  _STARTFILESRECOVERYREQUEST.fields_by_name['opts']._serialized_options = b'\350\3071\001'
  _STARTFILESRECOVERYREQUEST.fields_by_name['source_ids']._options = None
  _STARTFILESRECOVERYREQUEST.fields_by_name['source_ids']._serialized_options = b'\202\3101\002>0'
  _STARTFILESRECOVERYMETADATA.fields_by_name['compute_instance_id']._options = None
  _STARTFILESRECOVERYMETADATA.fields_by_name['compute_instance_id']._serialized_options = b'\350\3071\001'
  _STARTFILESRECOVERYMETADATA.fields_by_name['backup_id']._options = None
  _STARTFILESRECOVERYMETADATA.fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _STARTFILESRECOVERYMETADATA.fields_by_name['source_ids']._options = None
  _STARTFILESRECOVERYMETADATA.fields_by_name['source_ids']._serialized_options = b'\202\3101\002>0'
  _DELETEBACKUPREQUEST.fields_by_name['compute_instance_id']._options = None
  _DELETEBACKUPREQUEST.fields_by_name['compute_instance_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEBACKUPREQUEST.fields_by_name['backup_id']._options = None
  _DELETEBACKUPREQUEST.fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _BACKUPSERVICE.methods_by_name['List']._options = None
  _BACKUPSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\024\022\022/backup/v1/backups'
  _BACKUPSERVICE.methods_by_name['ListArchives']._options = None
  _BACKUPSERVICE.methods_by_name['ListArchives']._serialized_options = b'\202\323\344\223\0023\0221/backup/v1/backups/{compute_instance_id}/archives'
  _BACKUPSERVICE.methods_by_name['ListFiles']._options = None
  _BACKUPSERVICE.methods_by_name['ListFiles']._serialized_options = b'\202\323\344\223\002&\022$/backup/v1/backups/{backup_id}/files'
  _BACKUPSERVICE.methods_by_name['Get']._options = None
  _BACKUPSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002 \022\036/backup/v1/backups/{backup_id}'
  _BACKUPSERVICE.methods_by_name['StartRecovery']._options = None
  _BACKUPSERVICE.methods_by_name['StartRecovery']._serialized_options = b'\262\322*.\n\025StartRecoveryMetadata\022\025google.protobuf.Empty\202\323\344\223\0021\",/backup/v1/backups/{backup_id}:startRecovery:\001*'
  _BACKUPSERVICE.methods_by_name['StartFilesRecovery']._options = None
  _BACKUPSERVICE.methods_by_name['StartFilesRecovery']._serialized_options = b'\262\322*3\n\032StartFilesRecoveryMetadata\022\025google.protobuf.Empty'
  _BACKUPSERVICE.methods_by_name['Delete']._options = None
  _BACKUPSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*-\n\024DeleteBackupMetadata\022\025google.protobuf.Empty\202\323\344\223\0026*4/backup/v1/backups/{compute_instance_id}/{backup_id}'
  _globals['_LISTARCHIVESREQUEST']._serialized_start=243
  _globals['_LISTARCHIVESREQUEST']._serialized_end=328
  _globals['_LISTARCHIVESRESPONSE']._serialized_start=330
  _globals['_LISTARCHIVESRESPONSE']._serialized_end=403
  _globals['_LISTBACKUPSREQUEST']._serialized_start=406
  _globals['_LISTBACKUPSREQUEST']._serialized_end=873
  _globals['_LISTBACKUPSREQUEST_ARCHIVEPARAMETERS']._serialized_start=725
  _globals['_LISTBACKUPSREQUEST_ARCHIVEPARAMETERS']._serialized_end=795
  _globals['_LISTBACKUPSREQUEST_INSTANCEPOLICY']._serialized_start=797
  _globals['_LISTBACKUPSREQUEST_INSTANCEPOLICY']._serialized_end=861
  _globals['_LISTBACKUPSRESPONSE']._serialized_start=875
  _globals['_LISTBACKUPSRESPONSE']._serialized_end=945
  _globals['_LISTFILESREQUEST']._serialized_start=947
  _globals['_LISTFILESREQUEST']._serialized_end=1040
  _globals['_LISTFILESRESPONSE']._serialized_start=1042
  _globals['_LISTFILESRESPONSE']._serialized_end=1112
  _globals['_GETBACKUPREQUEST']._serialized_start=1114
  _globals['_GETBACKUPREQUEST']._serialized_end=1182
  _globals['_STARTRECOVERYREQUEST']._serialized_start=1184
  _globals['_STARTRECOVERYREQUEST']._serialized_end=1274
  _globals['_STARTRECOVERYMETADATA']._serialized_start=1276
  _globals['_STARTRECOVERYMETADATA']._serialized_end=1384
  _globals['_TARGETPATHORIGINAL']._serialized_start=1386
  _globals['_TARGETPATHORIGINAL']._serialized_end=1406
  _globals['_TARGETPATHCUSTOM']._serialized_start=1408
  _globals['_TARGETPATHCUSTOM']._serialized_end=1440
  _globals['_FILESRECOVERYOPTIONS']._serialized_start=1443
  _globals['_FILESRECOVERYOPTIONS']._serialized_end=1816
  _globals['_FILESRECOVERYOPTIONS_OVERWRITE']._serialized_start=1704
  _globals['_FILESRECOVERYOPTIONS_OVERWRITE']._serialized_end=1802
  _globals['_STARTFILESRECOVERYREQUEST']._serialized_start=1819
  _globals['_STARTFILESRECOVERYREQUEST']._serialized_end=2000
  _globals['_STARTFILESRECOVERYMETADATA']._serialized_start=2003
  _globals['_STARTFILESRECOVERYMETADATA']._serialized_end=2148
  _globals['_DELETEBACKUPREQUEST']._serialized_start=2150
  _globals['_DELETEBACKUPREQUEST']._serialized_end=2239
  _globals['_DELETEBACKUPMETADATA']._serialized_start=2241
  _globals['_DELETEBACKUPMETADATA']._serialized_end=2311
  _globals['_BACKUPSERVICE']._serialized_start=2314
  _globals['_BACKUPSERVICE']._serialized_end=3461
# @@protoc_insertion_point(module_scope)