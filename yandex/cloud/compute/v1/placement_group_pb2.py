# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/compute/v1/placement_group.proto
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
    'yandex/cloud/compute/v1/placement_group.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/compute/v1/placement_group.proto\x12\x17yandex.cloud.compute.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xc6\x03\n\x0ePlacementGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x43\n\x06labels\x18\x06 \x03(\x0b\x32\x33.yandex.cloud.compute.v1.PlacementGroup.LabelsEntry\x12U\n\x19spread_placement_strategy\x18\x07 \x01(\x0b\x32\x30.yandex.cloud.compute.v1.SpreadPlacementStrategyH\x00\x12[\n\x1cpartition_placement_strategy\x18\x08 \x01(\x0b\x32\x33.yandex.cloud.compute.v1.PartitionPlacementStrategyH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x1a\n\x12placement_strategy\x12\x04\xc0\xc1\x31\x01\"\x19\n\x17SpreadPlacementStrategy\"9\n\x1aPartitionPlacementStrategy\x12\x1b\n\npartitions\x18\x01 \x01(\x03\x42\x07\xfa\xc7\x31\x03\x32-5Bb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.placement_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _globals['_PLACEMENTGROUP_LABELSENTRY']._loaded_options = None
  _globals['_PLACEMENTGROUP_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_PLACEMENTGROUP'].oneofs_by_name['placement_strategy']._loaded_options = None
  _globals['_PLACEMENTGROUP'].oneofs_by_name['placement_strategy']._serialized_options = b'\300\3011\001'
  _globals['_PARTITIONPLACEMENTSTRATEGY'].fields_by_name['partitions']._loaded_options = None
  _globals['_PARTITIONPLACEMENTSTRATEGY'].fields_by_name['partitions']._serialized_options = b'\372\3071\0032-5'
  _globals['_PLACEMENTGROUP']._serialized_start=139
  _globals['_PLACEMENTGROUP']._serialized_end=593
  _globals['_PLACEMENTGROUP_LABELSENTRY']._serialized_start=520
  _globals['_PLACEMENTGROUP_LABELSENTRY']._serialized_end=565
  _globals['_SPREADPLACEMENTSTRATEGY']._serialized_start=595
  _globals['_SPREADPLACEMENTSTRATEGY']._serialized_end=620
  _globals['_PARTITIONPLACEMENTSTRATEGY']._serialized_start=622
  _globals['_PARTITIONPLACEMENTSTRATEGY']._serialized_end=679
# @@protoc_insertion_point(module_scope)
