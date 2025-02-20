# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/vpc/v1/route_table.proto
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
    'yandex/cloud/vpc/v1/route_table.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%yandex/cloud/vpc/v1/route_table.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb7\x02\n\nRouteTable\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12;\n\x06labels\x18\x06 \x03(\x0b\x32+.yandex.cloud.vpc.v1.RouteTable.LabelsEntry\x12\x12\n\nnetwork_id\x18\x07 \x01(\t\x12\x37\n\rstatic_routes\x18\x08 \x03(\x0b\x32 .yandex.cloud.vpc.v1.StaticRoute\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe5\x01\n\x0bStaticRoute\x12\x1c\n\x12\x64\x65stination_prefix\x18\x01 \x01(\tH\x00\x12\x1a\n\x10next_hop_address\x18\x02 \x01(\tH\x01\x12\x14\n\ngateway_id\x18\x04 \x01(\tH\x01\x12<\n\x06labels\x18\x03 \x03(\x0b\x32,.yandex.cloud.vpc.v1.StaticRoute.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\r\n\x0b\x64\x65stinationB\n\n\x08next_hopBV\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.vpc.v1.route_table_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc'
  _globals['_ROUTETABLE_LABELSENTRY']._loaded_options = None
  _globals['_ROUTETABLE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_STATICROUTE_LABELSENTRY']._loaded_options = None
  _globals['_STATICROUTE_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_ROUTETABLE']._serialized_start=96
  _globals['_ROUTETABLE']._serialized_end=407
  _globals['_ROUTETABLE_LABELSENTRY']._serialized_start=362
  _globals['_ROUTETABLE_LABELSENTRY']._serialized_end=407
  _globals['_STATICROUTE']._serialized_start=410
  _globals['_STATICROUTE']._serialized_end=639
  _globals['_STATICROUTE_LABELSENTRY']._serialized_start=362
  _globals['_STATICROUTE_LABELSENTRY']._serialized_end=407
# @@protoc_insertion_point(module_scope)
