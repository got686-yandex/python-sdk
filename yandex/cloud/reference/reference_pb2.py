# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/reference/reference.proto
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
    'yandex/cloud/reference/reference.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&yandex/cloud/reference/reference.proto\x12\x16yandex.cloud.reference\"\xb0\x01\n\tReference\x12\x32\n\x08referrer\x18\x01 \x01(\x0b\x32 .yandex.cloud.reference.Referrer\x12\x34\n\x04type\x18\x02 \x01(\x0e\x32&.yandex.cloud.reference.Reference.Type\"9\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nMANAGED_BY\x10\x01\x12\x0b\n\x07USED_BY\x10\x02\"$\n\x08Referrer\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\tBb\n\x1ayandex.cloud.api.referenceZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/reference;referenceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.reference.reference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032yandex.cloud.api.referenceZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/reference;reference'
  _globals['_REFERENCE']._serialized_start=67
  _globals['_REFERENCE']._serialized_end=243
  _globals['_REFERENCE_TYPE']._serialized_start=186
  _globals['_REFERENCE_TYPE']._serialized_end=243
  _globals['_REFERRER']._serialized_start=245
  _globals['_REFERRER']._serialized_end=281
# @@protoc_insertion_point(module_scope)
