# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/tuning/v1/tuning_error.proto
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
    'yandex/cloud/ai/tuning/v1/tuning_error.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,yandex/cloud/ai/tuning/v1/tuning_error.proto\x12\x19yandex.cloud.ai.tuning.v1\"\xa9\x01\n\x0bTuningError\x12\x16\n\x0etuning_task_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x39\n\x04type\x18\x03 \x01(\x0e\x32+.yandex.cloud.ai.tuning.v1.TuningError.Type\"6\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\x0c\n\x08INTERNAL\x10\x02\x42\x63\n\x1dyandex.cloud.api.ai.tuning.v1ZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/tuning/v1;fomob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.tuning.v1.tuning_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035yandex.cloud.api.ai.tuning.v1ZBgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/tuning/v1;fomo'
  _globals['_TUNINGERROR']._serialized_start=76
  _globals['_TUNINGERROR']._serialized_end=245
  _globals['_TUNINGERROR_TYPE']._serialized_start=191
  _globals['_TUNINGERROR_TYPE']._serialized_end=245
# @@protoc_insertion_point(module_scope)
