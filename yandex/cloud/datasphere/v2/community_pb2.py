# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/datasphere/v2/community.proto
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
    'yandex/cloud/datasphere/v2/community.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/datasphere/v2/community.proto\x12\x1ayandex.cloud.datasphere.v2\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa3\x02\n\tCommunity\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x41\n\x06labels\x18\x05 \x03(\x0b\x32\x31.yandex.cloud.datasphere.v2.Community.LabelsEntry\x12\x15\n\rcreated_by_id\x18\x06 \x01(\t\x12\x17\n\x0forganization_id\x18\n \x01(\t\x12\x0f\n\x07zone_id\x18\x0b \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x07\x10\nBk\n\x1eyandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.community_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphere'
  _globals['_COMMUNITY_LABELSENTRY']._loaded_options = None
  _globals['_COMMUNITY_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_COMMUNITY']._serialized_start=108
  _globals['_COMMUNITY']._serialized_end=399
  _globals['_COMMUNITY_LABELSENTRY']._serialized_start=348
  _globals['_COMMUNITY_LABELSENTRY']._serialized_end=393
# @@protoc_insertion_point(module_scope)
