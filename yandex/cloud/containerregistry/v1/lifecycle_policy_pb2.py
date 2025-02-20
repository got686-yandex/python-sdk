# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/containerregistry/v1/lifecycle_policy.proto
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
    'yandex/cloud/containerregistry/v1/lifecycle_policy.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8yandex/cloud/containerregistry/v1/lifecycle_policy.proto\x12!yandex.cloud.containerregistry.v1\x1a\x1dyandex/cloud/validation.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcf\x02\n\x0fLifecyclePolicy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rrepository_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12I\n\x06status\x18\x05 \x01(\x0e\x32\x39.yandex.cloud.containerregistry.v1.LifecyclePolicy.Status\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12?\n\x05rules\x18\x07 \x03(\x0b\x32\x30.yandex.cloud.containerregistry.v1.LifecycleRule\":\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\xbc\x01\n\rLifecycleRule\x12\x1e\n\x0b\x64\x65scription\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12;\n\rexpire_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05>=24h\x12\x1d\n\ntag_regexp\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x10\n\x08untagged\x18\x04 \x01(\x08\x12\x1d\n\x0cretained_top\x18\x05 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=0B\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.containerregistry.v1.lifecycle_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry'
  _globals['_LIFECYCLERULE'].fields_by_name['description']._loaded_options = None
  _globals['_LIFECYCLERULE'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_LIFECYCLERULE'].fields_by_name['expire_period']._loaded_options = None
  _globals['_LIFECYCLERULE'].fields_by_name['expire_period']._serialized_options = b'\372\3071\005>=24h'
  _globals['_LIFECYCLERULE'].fields_by_name['tag_regexp']._loaded_options = None
  _globals['_LIFECYCLERULE'].fields_by_name['tag_regexp']._serialized_options = b'\212\3101\005<=256'
  _globals['_LIFECYCLERULE'].fields_by_name['retained_top']._loaded_options = None
  _globals['_LIFECYCLERULE'].fields_by_name['retained_top']._serialized_options = b'\372\3071\003>=0'
  _globals['_LIFECYCLEPOLICY']._serialized_start=192
  _globals['_LIFECYCLEPOLICY']._serialized_end=527
  _globals['_LIFECYCLEPOLICY_STATUS']._serialized_start=469
  _globals['_LIFECYCLEPOLICY_STATUS']._serialized_end=527
  _globals['_LIFECYCLERULE']._serialized_start=530
  _globals['_LIFECYCLERULE']._serialized_end=718
# @@protoc_insertion_point(module_scope)
