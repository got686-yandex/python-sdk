# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/vision/v1/classification.proto
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
    'yandex/cloud/ai/vision/v1/classification.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/ai/vision/v1/classification.proto\x12\x19yandex.cloud.ai.vision.v1\"J\n\x0f\x43lassAnnotation\x12\x37\n\nproperties\x18\x01 \x03(\x0b\x32#.yandex.cloud.ai.vision.v1.Property\"-\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bprobability\x18\x02 \x01(\x01\x42\x65\n\x1dyandex.cloud.api.ai.vision.v1ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1;visionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.vision.v1.classification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035yandex.cloud.api.ai.vision.v1ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1;vision'
  _globals['_CLASSANNOTATION']._serialized_start=77
  _globals['_CLASSANNOTATION']._serialized_end=151
  _globals['_PROPERTY']._serialized_start=153
  _globals['_PROPERTY']._serialized_end=198
# @@protoc_insertion_point(module_scope)
