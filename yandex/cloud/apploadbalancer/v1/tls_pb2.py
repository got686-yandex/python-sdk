# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/apploadbalancer/v1/tls.proto
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
    'yandex/cloud/apploadbalancer/v1/tls.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/apploadbalancer/v1/tls.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1dyandex/cloud/validation.proto\"\\\n\x11ValidationContext\x12\x17\n\rtrusted_ca_id\x18\x01 \x01(\tH\x00\x12\x1a\n\x10trusted_ca_bytes\x18\x02 \x01(\tH\x00\x42\x12\n\ntrusted_ca\x12\x04\xc0\xc1\x31\x01\x42z\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.apploadbalancer.v1.tls_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer'
  _globals['_VALIDATIONCONTEXT'].oneofs_by_name['trusted_ca']._loaded_options = None
  _globals['_VALIDATIONCONTEXT'].oneofs_by_name['trusted_ca']._serialized_options = b'\300\3011\001'
  _globals['_VALIDATIONCONTEXT']._serialized_start=109
  _globals['_VALIDATIONCONTEXT']._serialized_end=201
# @@protoc_insertion_point(module_scope)
