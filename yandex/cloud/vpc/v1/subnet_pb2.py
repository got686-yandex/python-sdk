# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/vpc/v1/subnet.proto
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
    'yandex/cloud/vpc/v1/subnet.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n yandex/cloud/vpc/v1/subnet.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8d\x03\n\x06Subnet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x37\n\x06labels\x18\x06 \x03(\x0b\x32\'.yandex.cloud.vpc.v1.Subnet.LabelsEntry\x12\x12\n\nnetwork_id\x18\x07 \x01(\t\x12\x0f\n\x07zone_id\x18\x08 \x01(\t\x12\x16\n\x0ev4_cidr_blocks\x18\n \x03(\t\x12\x16\n\x0ev6_cidr_blocks\x18\x0b \x03(\t\x12\x16\n\x0eroute_table_id\x18\x0c \x01(\t\x12\x36\n\x0c\x64hcp_options\x18\r \x01(\x0b\x32 .yandex.cloud.vpc.v1.DhcpOptions\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\t\x10\n\"T\n\x0b\x44hcpOptions\x12\x1b\n\x13\x64omain_name_servers\x18\x01 \x03(\t\x12\x13\n\x0b\x64omain_name\x18\x02 \x01(\t\x12\x13\n\x0bntp_servers\x18\x03 \x03(\t*;\n\tIpVersion\x12\x1a\n\x16IP_VERSION_UNSPECIFIED\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02\x42V\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.vpc.v1.subnet_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc'
  _globals['_SUBNET_LABELSENTRY']._loaded_options = None
  _globals['_SUBNET_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_IPVERSION']._serialized_start=576
  _globals['_IPVERSION']._serialized_end=635
  _globals['_SUBNET']._serialized_start=91
  _globals['_SUBNET']._serialized_end=488
  _globals['_SUBNET_LABELSENTRY']._serialized_start=437
  _globals['_SUBNET_LABELSENTRY']._serialized_end=482
  _globals['_DHCPOPTIONS']._serialized_start=490
  _globals['_DHCPOPTIONS']._serialized_end=574
# @@protoc_insertion_point(module_scope)
