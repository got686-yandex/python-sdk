# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/logging/v1/log_ingestion_service.proto
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
    'yandex/cloud/logging/v1/log_ingestion_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from yandex.cloud.logging.v1 import log_entry_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2
from yandex.cloud.logging.v1 import log_resource_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__resource__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/logging/v1/log_ingestion_service.proto\x12\x17yandex.cloud.logging.v1\x1a\x17google/rpc/status.proto\x1a\'yandex/cloud/logging/v1/log_entry.proto\x1a*yandex/cloud/logging/v1/log_resource.proto\x1a\x1dyandex/cloud/validation.proto\"\x90\x02\n\x0cWriteRequest\x12?\n\x0b\x64\x65stination\x18\x01 \x01(\x0b\x32$.yandex.cloud.logging.v1.DestinationB\x04\xe8\xc7\x31\x01\x12;\n\x08resource\x18\x02 \x01(\x0b\x32).yandex.cloud.logging.v1.LogEntryResource\x12\x45\n\x07\x65ntries\x18\x03 \x03(\x0b\x32).yandex.cloud.logging.v1.IncomingLogEntryB\t\x82\xc8\x31\x05\x31-100\x12;\n\x08\x64\x65\x66\x61ults\x18\x04 \x01(\x0b\x32).yandex.cloud.logging.v1.LogEntryDefaults\"\x96\x01\n\rWriteResponse\x12\x42\n\x06\x65rrors\x18\x01 \x03(\x0b\x32\x32.yandex.cloud.logging.v1.WriteResponse.ErrorsEntry\x1a\x41\n\x0b\x45rrorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.google.rpc.Status:\x02\x38\x01\x32m\n\x13LogIngestionService\x12V\n\x05Write\x12%.yandex.cloud.logging.v1.WriteRequest\x1a&.yandex.cloud.logging.v1.WriteResponseBb\n\x1byandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;loggingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.logging.v1.log_ingestion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;logging'
  _globals['_WRITEREQUEST'].fields_by_name['destination']._loaded_options = None
  _globals['_WRITEREQUEST'].fields_by_name['destination']._serialized_options = b'\350\3071\001'
  _globals['_WRITEREQUEST'].fields_by_name['entries']._loaded_options = None
  _globals['_WRITEREQUEST'].fields_by_name['entries']._serialized_options = b'\202\3101\0051-100'
  _globals['_WRITERESPONSE_ERRORSENTRY']._loaded_options = None
  _globals['_WRITERESPONSE_ERRORSENTRY']._serialized_options = b'8\001'
  _globals['_WRITEREQUEST']._serialized_start=222
  _globals['_WRITEREQUEST']._serialized_end=494
  _globals['_WRITERESPONSE']._serialized_start=497
  _globals['_WRITERESPONSE']._serialized_end=647
  _globals['_WRITERESPONSE_ERRORSENTRY']._serialized_start=582
  _globals['_WRITERESPONSE_ERRORSENTRY']._serialized_end=647
  _globals['_LOGINGESTIONSERVICE']._serialized_start=649
  _globals['_LOGINGESTIONSERVICE']._serialized_end=758
# @@protoc_insertion_point(module_scope)
