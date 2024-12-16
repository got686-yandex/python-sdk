# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/cic/v1/public_connection.proto
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
    'yandex/cloud/cic/v1/public_connection.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud.cic.v1 import peering_pb2 as yandex_dot_cloud_dot_cic_dot_v1_dot_peering__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/cic/v1/public_connection.proto\x12\x13yandex.cloud.cic.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a!yandex/cloud/cic/v1/peering.proto\"\xe5\x06\n\x10PublicConnection\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tfolder_id\x18\x05 \x01(\t\x12\x11\n\tregion_id\x18\x06 \x01(\t\x12\x1b\n\x13trunk_connection_id\x18\x07 \x01(\t\x12,\n\x07vlan_id\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x32\n\x0cipv4_peering\x18\t \x01(\x0b\x32\x1c.yandex.cloud.cic.v1.Peering\x12Z\n\x1aipv4_allowed_service_types\x18\x0b \x03(\x0e\x32\x36.yandex.cloud.cic.v1.PublicConnection.CloudServiceType\x12$\n\x1cipv4_peer_announced_prefixes\x18\r \x03(\t\x12\x41\n\x06labels\x18\x12 \x03(\x0b\x32\x31.yandex.cloud.cic.v1.PublicConnection.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf0\x02\n\x10\x43loudServiceType\x12\"\n\x1e\x43LOUD_SERVICE_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x14\x43LOUD_SERVICE_YANDEX\x10\x01\x1a\x02\x08\x01\x12\x1c\n\x18\x43LOUD_SERVICE_ALL_PUBLIC\x10\x02\x12\x14\n\x10\x43LOUD_SERVICE_S3\x10\x03\x12\x14\n\x10\x43LOUD_SERVICE_ML\x10\x04\x12\x17\n\x13\x43LOUD_SERVICE_APIGW\x10\x05\x12$\n CLOUD_SERVICE_CONTAINER_REGISTRY\x10\x06\x12\x19\n\x15\x43LOUD_SERVICE_CONSOLE\x10\x07\x12\x1c\n\x18\x43LOUD_SERVICE_MONITORING\x10\x08\x12\x1c\n\x18\x43LOUD_SERVICE_YANDEX_GPT\x10\t\x12#\n\x1f\x43LOUD_SERVICES_ALL_API_ENDPOINT\x10\n\x12\x15\n\x11\x43LOUD_SERVICE_YMQ\x10\x0bJ\x04\x08\x04\x10\x05J\x04\x08\n\x10\x0bJ\x04\x08\x0c\x10\rJ\x04\x08\x0e\x10\x12\x42V\n\x17yandex.cloud.api.cic.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cic/v1;cicb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cic.v1.public_connection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.cic.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cic/v1;cic'
  _globals['_PUBLICCONNECTION_LABELSENTRY']._loaded_options = None
  _globals['_PUBLICCONNECTION_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_PUBLICCONNECTION_CLOUDSERVICETYPE'].values_by_name["CLOUD_SERVICE_YANDEX"]._loaded_options = None
  _globals['_PUBLICCONNECTION_CLOUDSERVICETYPE'].values_by_name["CLOUD_SERVICE_YANDEX"]._serialized_options = b'\010\001'
  _globals['_PUBLICCONNECTION']._serialized_start=136
  _globals['_PUBLICCONNECTION']._serialized_end=1005
  _globals['_PUBLICCONNECTION_LABELSENTRY']._serialized_start=565
  _globals['_PUBLICCONNECTION_LABELSENTRY']._serialized_end=610
  _globals['_PUBLICCONNECTION_CLOUDSERVICETYPE']._serialized_start=613
  _globals['_PUBLICCONNECTION_CLOUDSERVICETYPE']._serialized_end=981
# @@protoc_insertion_point(module_scope)
