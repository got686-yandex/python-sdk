# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/cdn/v1/origin.proto
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
    'yandex/cloud/cdn/v1/origin.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n yandex/cloud/cdn/v1/origin.proto\x12\x13yandex.cloud.cdn.v1\"\x8d\x01\n\x06Origin\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x17\n\x0forigin_group_id\x18\x02 \x01(\x03\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x0e\n\x06\x62\x61\x63kup\x18\x05 \x01(\x08\x12-\n\x04meta\x18\x06 \x01(\x0b\x32\x1f.yandex.cloud.cdn.v1.OriginMeta\"n\n\x0cOriginParams\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x0e\n\x06\x62\x61\x63kup\x18\x03 \x01(\x08\x12-\n\x04meta\x18\x04 \x01(\x0b\x32\x1f.yandex.cloud.cdn.v1.OriginMeta\"\x89\x02\n\nOriginMeta\x12\x36\n\x06\x63ommon\x18\x01 \x01(\x0b\x32$.yandex.cloud.cdn.v1.OriginNamedMetaH\x00\x12\x36\n\x06\x62ucket\x18\x02 \x01(\x0b\x32$.yandex.cloud.cdn.v1.OriginNamedMetaH\x00\x12\x37\n\x07website\x18\x03 \x01(\x0b\x32$.yandex.cloud.cdn.v1.OriginNamedMetaH\x00\x12;\n\x08\x62\x61lancer\x18\x04 \x01(\x0b\x32\'.yandex.cloud.cdn.v1.OriginBalancerMetaH\x00\x42\x15\n\x13origin_meta_variant\"\x1f\n\x0fOriginNamedMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\x12OriginBalancerMeta\x12\n\n\x02id\x18\x01 \x01(\tBV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cdn.v1.origin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn'
  _globals['_ORIGIN']._serialized_start=58
  _globals['_ORIGIN']._serialized_end=199
  _globals['_ORIGINPARAMS']._serialized_start=201
  _globals['_ORIGINPARAMS']._serialized_end=311
  _globals['_ORIGINMETA']._serialized_start=314
  _globals['_ORIGINMETA']._serialized_end=579
  _globals['_ORIGINNAMEDMETA']._serialized_start=581
  _globals['_ORIGINNAMEDMETA']._serialized_end=612
  _globals['_ORIGINBALANCERMETA']._serialized_start=614
  _globals['_ORIGINBALANCERMETA']._serialized_end=646
# @@protoc_insertion_point(module_scope)
