# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/datatransfer/v1/endpoint/clickhouse.proto
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
    'yandex/cloud/datatransfer/v1/endpoint/clickhouse.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yandex.cloud.datatransfer.v1.endpoint import common_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6yandex/cloud/datatransfer/v1/endpoint/clickhouse.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x1bgoogle/protobuf/empty.proto\x1a\x32yandex/cloud/datatransfer/v1/endpoint/common.proto\".\n\x0f\x43lickhouseShard\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05hosts\x18\x02 \x03(\t\"\xd3\x01\n\x13OnPremiseClickhouse\x12\x46\n\x06shards\x18\x01 \x03(\x0b\x32\x36.yandex.cloud.datatransfer.v1.endpoint.ClickhouseShard\x12\x11\n\thttp_port\x18\x03 \x01(\x03\x12\x13\n\x0bnative_port\x18\x04 \x01(\x03\x12@\n\x08tls_mode\x18\x08 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.endpoint.TLSModeJ\x04\x08\x02\x10\x03J\x04\x08\x05\x10\x08\"\x81\x02\n\x1b\x43lickhouseConnectionOptions\x12P\n\non_premise\x18\x02 \x01(\x0b\x32:.yandex.cloud.datatransfer.v1.endpoint.OnPremiseClickhouseH\x00\x12\x18\n\x0emdb_cluster_id\x18\x05 \x01(\tH\x00\x12\x0c\n\x04user\x18\x06 \x01(\t\x12?\n\x08password\x18\x07 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12\x10\n\x08\x64\x61tabase\x18\x08 \x01(\tB\t\n\x07\x61\x64\x64ressJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x05\"\x86\x01\n\x14\x43lickhouseConnection\x12`\n\x12\x63onnection_options\x18\x01 \x01(\x0b\x32\x42.yandex.cloud.datatransfer.v1.endpoint.ClickhouseConnectionOptionsH\x00\x42\x0c\n\nconnection\"\xfc\x04\n\x12\x43lickhouseSharding\x12\x66\n\x11\x63olumn_value_hash\x18\x01 \x01(\x0b\x32I.yandex.cloud.datatransfer.v1.endpoint.ClickhouseSharding.ColumnValueHashH\x00\x12\x66\n\x0e\x63ustom_mapping\x18\x02 \x01(\x0b\x32L.yandex.cloud.datatransfer.v1.endpoint.ClickhouseSharding.ColumnValueMappingH\x00\x12-\n\x0btransfer_id\x18\x03 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12-\n\x0bround_robin\x18\x04 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x1a&\n\x0f\x43olumnValueHash\x12\x13\n\x0b\x63olumn_name\x18\x01 \x01(\t\x1a\x83\x02\n\x12\x43olumnValueMapping\x12\x13\n\x0b\x63olumn_name\x18\x01 \x01(\t\x12j\n\x07mapping\x18\x02 \x03(\x0b\x32Y.yandex.cloud.datatransfer.v1.endpoint.ClickhouseSharding.ColumnValueMapping.ValueToShard\x1al\n\x0cValueToShard\x12H\n\x0c\x63olumn_value\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.datatransfer.v1.endpoint.ColumnValue\x12\x12\n\nshard_name\x18\x02 \x01(\tB\n\n\x08sharding\"\xe6\x01\n\x10\x43lickhouseSource\x12O\n\nconnection\x18\x01 \x01(\x0b\x32;.yandex.cloud.datatransfer.v1.endpoint.ClickhouseConnection\x12\x16\n\x0einclude_tables\x18\x07 \x03(\t\x12\x16\n\x0e\x65xclude_tables\x18\x08 \x03(\t\x12\x11\n\tsubnet_id\x18\t \x01(\t\x12\x17\n\x0fsecurity_groups\x18\n \x03(\t\x12\x1f\n\x17\x63lickhouse_cluster_name\x18\x0b \x01(\tJ\x04\x08\x02\x10\x07\"\xb6\x03\n\x10\x43lickhouseTarget\x12O\n\nconnection\x18\x02 \x01(\x0b\x32;.yandex.cloud.datatransfer.v1.endpoint.ClickhouseConnection\x12\x11\n\tsubnet_id\x18\x0c \x01(\t\x12\x41\n\talt_names\x18\x11 \x03(\x0b\x32..yandex.cloud.datatransfer.v1.endpoint.AltName\x12V\n\x0e\x63leanup_policy\x18\x15 \x01(\x0e\x32>.yandex.cloud.datatransfer.v1.endpoint.ClickhouseCleanupPolicy\x12K\n\x08sharding\x18\x16 \x01(\x0b\x32\x39.yandex.cloud.datatransfer.v1.endpoint.ClickhouseSharding\x12\x1f\n\x17\x63lickhouse_cluster_name\x18\x32 \x01(\t\x12\x17\n\x0fsecurity_groups\x18\x33 \x03(\tJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x0cJ\x04\x08\r\x10\x11J\x04\x08\x12\x10\x15J\x04\x08\x17\x10\x32*\xb8\x01\n\x17\x43lickhouseCleanupPolicy\x12)\n%CLICKHOUSE_CLEANUP_POLICY_UNSPECIFIED\x10\x00\x12&\n\"CLICKHOUSE_CLEANUP_POLICY_DISABLED\x10\x01\x12\"\n\x1e\x43LICKHOUSE_CLEANUP_POLICY_DROP\x10\x02\x12&\n\"CLICKHOUSE_CLEANUP_POLICY_TRUNCATE\x10\x03\x42\xa7\x01\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\xaa\x02%Yandex.Cloud.Datatransfer.V1.EndPointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datatransfer.v1.endpoint.clickhouse_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\252\002%Yandex.Cloud.Datatransfer.V1.EndPoint'
  _globals['_CLICKHOUSECLEANUPPOLICY']._serialized_start=2151
  _globals['_CLICKHOUSECLEANUPPOLICY']._serialized_end=2335
  _globals['_CLICKHOUSESHARD']._serialized_start=178
  _globals['_CLICKHOUSESHARD']._serialized_end=224
  _globals['_ONPREMISECLICKHOUSE']._serialized_start=227
  _globals['_ONPREMISECLICKHOUSE']._serialized_end=438
  _globals['_CLICKHOUSECONNECTIONOPTIONS']._serialized_start=441
  _globals['_CLICKHOUSECONNECTIONOPTIONS']._serialized_end=698
  _globals['_CLICKHOUSECONNECTION']._serialized_start=701
  _globals['_CLICKHOUSECONNECTION']._serialized_end=835
  _globals['_CLICKHOUSESHARDING']._serialized_start=838
  _globals['_CLICKHOUSESHARDING']._serialized_end=1474
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEHASH']._serialized_start=1162
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEHASH']._serialized_end=1200
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEMAPPING']._serialized_start=1203
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEMAPPING']._serialized_end=1462
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEMAPPING_VALUETOSHARD']._serialized_start=1354
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEMAPPING_VALUETOSHARD']._serialized_end=1462
  _globals['_CLICKHOUSESOURCE']._serialized_start=1477
  _globals['_CLICKHOUSESOURCE']._serialized_end=1707
  _globals['_CLICKHOUSETARGET']._serialized_start=1710
  _globals['_CLICKHOUSETARGET']._serialized_end=2148
# @@protoc_insertion_point(module_scope)
