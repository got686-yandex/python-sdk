# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/workflows/v1/history_entry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8yandex/cloud/serverless/workflows/v1/history_entry.proto\x12$yandex.cloud.serverless.workflows.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xee\x06\n\x0cHistoryEntry\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\nstarted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x64uration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x46\n\x05input\x18\x06 \x01(\x0b\x32\x37.yandex.cloud.serverless.workflows.v1.HistoryEntryInput\x12H\n\x06output\x18\x07 \x01(\x0b\x32\x38.yandex.cloud.serverless.workflows.v1.HistoryEntryOutput\x12\x46\n\x05\x65rror\x18\x08 \x01(\x0b\x32\x37.yandex.cloud.serverless.workflows.v1.HistoryEntryError\x12I\n\x06status\x18\t \x01(\x0e\x32\x39.yandex.cloud.serverless.workflows.v1.HistoryEntry.Status\x12\x0c\n\x04type\x18\n \x01(\t\x12\x10\n\x08\x61ttempts\x18\x0c \x01(\x03\x12K\n\nlast_error\x18\r \x01(\x0b\x32\x37.yandex.cloud.serverless.workflows.v1.HistoryEntryError\x1a\xba\x01\n\rFailedAttempt\x12\x34\n\nstarted_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe8\xc7\x31\x01\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x46\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x37.yandex.cloud.serverless.workflows.v1.HistoryEntryError\"|\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\r\n\tSCHEDULED\x10\x01\x12\x0b\n\x07STARTED\x10\x02\x12\r\n\tCOMPLETED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x14\n\x10\x43\x41NCEL_REQUESTED\x10\x05\x12\r\n\tCANCELLED\x10\x06J\x04\x08\x0b\x10\x0c\"8\n\x11HistoryEntryInput\x12\x14\n\ninput_json\x18\x01 \x01(\tH\x00\x42\r\n\x05input\x12\x04\xc0\xc1\x31\x01\";\n\x12HistoryEntryOutput\x12\x15\n\x0boutput_json\x18\x01 \x01(\tH\x00\x42\x0e\n\x06output\x12\x04\xc0\xc1\x31\x01\"8\n\x11HistoryEntryError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x12\n\nerror_code\x18\x02 \x01(\tB~\n(yandex.cloud.api.serverless.workflows.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/workflows/v1;workflowsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.workflows.v1.history_entry_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(yandex.cloud.api.serverless.workflows.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/workflows/v1;workflows'
  _HISTORYENTRY_FAILEDATTEMPT.fields_by_name['started_at']._options = None
  _HISTORYENTRY_FAILEDATTEMPT.fields_by_name['started_at']._serialized_options = b'\350\3071\001'
  _HISTORYENTRYINPUT.oneofs_by_name['input']._options = None
  _HISTORYENTRYINPUT.oneofs_by_name['input']._serialized_options = b'\300\3011\001'
  _HISTORYENTRYOUTPUT.oneofs_by_name['output']._options = None
  _HISTORYENTRYOUTPUT.oneofs_by_name['output']._serialized_options = b'\300\3011\001'
  _globals['_HISTORYENTRY']._serialized_start=195
  _globals['_HISTORYENTRY']._serialized_end=1073
  _globals['_HISTORYENTRY_FAILEDATTEMPT']._serialized_start=755
  _globals['_HISTORYENTRY_FAILEDATTEMPT']._serialized_end=941
  _globals['_HISTORYENTRY_STATUS']._serialized_start=943
  _globals['_HISTORYENTRY_STATUS']._serialized_end=1067
  _globals['_HISTORYENTRYINPUT']._serialized_start=1075
  _globals['_HISTORYENTRYINPUT']._serialized_end=1131
  _globals['_HISTORYENTRYOUTPUT']._serialized_start=1133
  _globals['_HISTORYENTRYOUTPUT']._serialized_end=1192
  _globals['_HISTORYENTRYERROR']._serialized_start=1194
  _globals['_HISTORYENTRYERROR']._serialized_end=1250
# @@protoc_insertion_point(module_scope)