# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/vision/v1/face_detection.proto
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
    'yandex/cloud/ai/vision/v1/face_detection.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.vision.v1 import primitives_pb2 as yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_primitives__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/ai/vision/v1/face_detection.proto\x12\x19yandex.cloud.ai.vision.v1\x1a*yandex/cloud/ai/vision/v1/primitives.proto\"@\n\x0e\x46\x61\x63\x65\x41nnotation\x12.\n\x05\x66\x61\x63\x65s\x18\x01 \x03(\x0b\x32\x1f.yandex.cloud.ai.vision.v1.Face\"@\n\x04\x46\x61\x63\x65\x12\x38\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32\".yandex.cloud.ai.vision.v1.PolygonBe\n\x1dyandex.cloud.api.ai.vision.v1ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1;visionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.vision.v1.face_detection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035yandex.cloud.api.ai.vision.v1ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1;vision'
  _globals['_FACEANNOTATION']._serialized_start=121
  _globals['_FACEANNOTATION']._serialized_end=185
  _globals['_FACE']._serialized_start=187
  _globals['_FACE']._serialized_end=251
# @@protoc_insertion_point(module_scope)
