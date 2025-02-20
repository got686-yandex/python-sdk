# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/backup/v1/resource.proto
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
    'yandex/cloud/backup/v1/resource.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%yandex/cloud/backup/v1/resource.proto\x12\x16yandex.cloud.backup.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x81\x06\n\x08Resource\x12\x1b\n\x13\x63ompute_instance_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06online\x18\x04 \x01(\x08\x12\x0f\n\x07\x65nabled\x18\x05 \x01(\x08\x12\x37\n\x06status\x18\x06 \x01(\x0e\x32\'.yandex.cloud.backup.v1.Resource.Status\x12\x16\n\x0estatus_details\x18\x07 \x01(\t\x12\x17\n\x0fstatus_progress\x18\x08 \x01(\x03\x12\x34\n\x10last_backup_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10next_backup_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bresource_id\x18\x0b \x01(\t\x12\x11\n\tis_active\x18\x0c \x01(\x08\x12@\n\x0binit_status\x18\r \x01(\x0e\x32+.yandex.cloud.backup.v1.Resource.InitStatus\x12\x10\n\x08metadata\x18\x0e \x01(\t\x12\x32\n\x04type\x18\x0f \x01(\x0e\x32$.yandex.cloud.backup.v1.ResourceType\"`\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x08\n\x04IDLE\x10\x01\x12\r\n\tBACKUPING\x10\x02\x12\x0e\n\nRECOVERING\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\t\n\x05OTHER\x10\x05\"o\n\nInitStatus\x12\x1b\n\x17INIT_STATUS_UNSPECIFIED\x10\x00\x12\x0f\n\x0bREGISTERING\x10\x01\x12\r\n\tREGISTRED\x10\x02\x12\x17\n\x13\x46\x41ILED_REGISTRATION\x10\x03\x12\x0b\n\x07\x44\x45LETED\x10\x04\"*\n\x08Progress\x12\x0f\n\x07\x63urrent\x18\x01 \x01(\x03\x12\r\n\x05total\x18\x02 \x01(\x03\"\xb7\x06\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0b\x63\x61ncellable\x18\x02 \x01(\x08\x12\x11\n\tpolicy_id\x18\x03 \x01(\t\x12/\n\x04type\x18\x04 \x01(\x0e\x32!.yandex.cloud.backup.v1.Task.Type\x12\x32\n\x08progress\x18\x05 \x01(\x0b\x32 .yandex.cloud.backup.v1.Progress\x12\x33\n\x06status\x18\x06 \x01(\x0e\x32#.yandex.cloud.backup.v1.Task.Status\x12/\n\x0b\x65nqueued_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstarted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x63ompleted_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13\x63ompute_instance_id\x18\x0b \x01(\t\x12\x36\n\x0bresult_code\x18\x0c \x01(\x0e\x32!.yandex.cloud.backup.v1.Task.Code\x12\r\n\x05\x65rror\x18\r \x01(\t\"j\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06\x42\x41\x43KUP\x10\x01\x12\r\n\tRETENTION\x10\x02\x12\x0c\n\x08RECOVERY\x10\x03\x12\x10\n\x0c\x41PPLY_POLICY\x10\x04\x12\x11\n\rREVOKE_POLICY\x10\x05\"d\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x45NQUEUED\x10\x01\x12\x0c\n\x08\x41SSIGNED\x10\x02\x12\x0b\n\x07STARTED\x10\x03\x12\n\n\x06PAUSED\x10\x04\x12\r\n\tCOMPLETED\x10\x05\"h\n\x04\x43ode\x12\x14\n\x10\x43ODE_UNSPECIFIED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x0b\n\x07WARNING\x10\x03\x12\r\n\tCANCELLED\x10\x04\x12\r\n\tABANDONED\x10\x05\x12\x0c\n\x08TIMEDOUT\x10\x06*C\n\x0cResourceType\x12\x1d\n\x19RESOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x43OMPUTE\x10\x01\x12\x07\n\x03\x42MS\x10\x02\x42_\n\x1ayandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.backup.v1.resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032yandex.cloud.api.backup.v1ZAgithub.com/yandex-cloud/go-genproto/yandex/cloud/backup/v1;backup'
  _globals['_RESOURCETYPE']._serialized_start=1740
  _globals['_RESOURCETYPE']._serialized_end=1807
  _globals['_RESOURCE']._serialized_start=99
  _globals['_RESOURCE']._serialized_end=868
  _globals['_RESOURCE_STATUS']._serialized_start=659
  _globals['_RESOURCE_STATUS']._serialized_end=755
  _globals['_RESOURCE_INITSTATUS']._serialized_start=757
  _globals['_RESOURCE_INITSTATUS']._serialized_end=868
  _globals['_PROGRESS']._serialized_start=870
  _globals['_PROGRESS']._serialized_end=912
  _globals['_TASK']._serialized_start=915
  _globals['_TASK']._serialized_end=1738
  _globals['_TASK_TYPE']._serialized_start=1424
  _globals['_TASK_TYPE']._serialized_end=1530
  _globals['_TASK_STATUS']._serialized_start=1532
  _globals['_TASK_STATUS']._serialized_end=1632
  _globals['_TASK_CODE']._serialized_start=1634
  _globals['_TASK_CODE']._serialized_end=1738
# @@protoc_insertion_point(module_scope)
