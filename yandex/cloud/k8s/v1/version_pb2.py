# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/k8s/v1/version.proto
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
    'yandex/cloud/k8s/v1/version.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!yandex/cloud/k8s/v1/version.proto\x12\x13yandex.cloud.k8s.v1\x1a\x1dyandex/cloud/validation.proto\"\x80\x01\n\x0bVersionInfo\x12\x17\n\x0f\x63urrent_version\x18\x01 \x01(\t\x12\x1e\n\x16new_revision_available\x18\x02 \x01(\x08\x12\x1c\n\x14new_revision_summary\x18\x03 \x01(\t\x12\x1a\n\x12version_deprecated\x18\x04 \x01(\x08\"T\n\x11UpdateVersionSpec\x12\x11\n\x07version\x18\x01 \x01(\tH\x00\x12\x19\n\x0flatest_revision\x18\x02 \x01(\x08H\x00\x42\x11\n\tspecifier\x12\x04\xc0\xc1\x31\x01\x42V\n\x17yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8sb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.k8s.v1.version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8s'
  _globals['_UPDATEVERSIONSPEC'].oneofs_by_name['specifier']._loaded_options = None
  _globals['_UPDATEVERSIONSPEC'].oneofs_by_name['specifier']._serialized_options = b'\300\3011\001'
  _globals['_VERSIONINFO']._serialized_start=90
  _globals['_VERSIONINFO']._serialized_end=218
  _globals['_UPDATEVERSIONSPEC']._serialized_start=220
  _globals['_UPDATEVERSIONSPEC']._serialized_end=304
# @@protoc_insertion_point(module_scope)
