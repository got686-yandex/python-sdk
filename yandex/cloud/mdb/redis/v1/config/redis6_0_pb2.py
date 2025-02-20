# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/redis/v1/config/redis6_0.proto
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
    'yandex/cloud/mdb/redis/v1/config/redis6_0.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/mdb/redis/v1/config/redis6_0.proto\x12 yandex.cloud.mdb.redis.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xd6\x08\n\x0eRedisConfig6_0\x12Z\n\x10maxmemory_policy\x18\x01 \x01(\x0e\x32@.yandex.cloud.mdb.redis.v1.config.RedisConfig6_0.MaxmemoryPolicy\x12,\n\x07timeout\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x08password\x18\x03 \x01(\tB&\xf2\xc7\x31\"[a-zA-Z0-9@=+?*.,!&#$^<>_-]{8,128}\x12\x36\n\tdatabases\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12\x45\n\x17slowlog_log_slower_than\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12=\n\x0fslowlog_max_len\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x39\n\x16notify_keyspace_events\x18\x07 \x01(\tB\x19\xf2\xc7\x31\x15[KEg$lshzxeAtm]{0,13}\x12s\n!client_output_buffer_limit_pubsub\x18\x08 \x01(\x0b\x32H.yandex.cloud.mdb.redis.v1.config.RedisConfig6_0.ClientOutputBufferLimit\x12s\n!client_output_buffer_limit_normal\x18\t \x01(\x0b\x32H.yandex.cloud.mdb.redis.v1.config.RedisConfig6_0.ClientOutputBufferLimit\x1a\xd5\x01\n\x17\x43lientOutputBufferLimit\x12\x38\n\nhard_limit\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x38\n\nsoft_limit\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12:\n\x0csoft_seconds\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0J\x04\x08\x04\x10\x05J\x04\x08\x02\x10\x03\"\xc4\x01\n\x0fMaxmemoryPolicy\x12 \n\x1cMAXMEMORY_POLICY_UNSPECIFIED\x10\x00\x12\x10\n\x0cVOLATILE_LRU\x10\x01\x12\x0f\n\x0b\x41LLKEYS_LRU\x10\x02\x12\x10\n\x0cVOLATILE_LFU\x10\x03\x12\x0f\n\x0b\x41LLKEYS_LFU\x10\x04\x12\x13\n\x0fVOLATILE_RANDOM\x10\x05\x12\x12\n\x0e\x41LLKEYS_RANDOM\x10\x06\x12\x10\n\x0cVOLATILE_TTL\x10\x07\x12\x0e\n\nNOEVICTION\x10\x08\"\xf0\x01\n\x11RedisConfigSet6_0\x12J\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x30.yandex.cloud.mdb.redis.v1.config.RedisConfig6_0\x12\x45\n\x0buser_config\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.redis.v1.config.RedisConfig6_0\x12H\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.redis.v1.config.RedisConfig6_0Br\n$yandex.cloud.api.mdb.redis.v1.configZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1/config;redisb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.redis.v1.config.redis6_0_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$yandex.cloud.api.mdb.redis.v1.configZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1/config;redis'
  _globals['_REDISCONFIG6_0_CLIENTOUTPUTBUFFERLIMIT'].fields_by_name['hard_limit']._loaded_options = None
  _globals['_REDISCONFIG6_0_CLIENTOUTPUTBUFFERLIMIT'].fields_by_name['hard_limit']._serialized_options = b'\372\3071\003>=0'
  _globals['_REDISCONFIG6_0_CLIENTOUTPUTBUFFERLIMIT'].fields_by_name['soft_limit']._loaded_options = None
  _globals['_REDISCONFIG6_0_CLIENTOUTPUTBUFFERLIMIT'].fields_by_name['soft_limit']._serialized_options = b'\372\3071\003>=0'
  _globals['_REDISCONFIG6_0_CLIENTOUTPUTBUFFERLIMIT'].fields_by_name['soft_seconds']._loaded_options = None
  _globals['_REDISCONFIG6_0_CLIENTOUTPUTBUFFERLIMIT'].fields_by_name['soft_seconds']._serialized_options = b'\372\3071\003>=0'
  _globals['_REDISCONFIG6_0'].fields_by_name['password']._loaded_options = None
  _globals['_REDISCONFIG6_0'].fields_by_name['password']._serialized_options = b'\362\3071\"[a-zA-Z0-9@=+?*.,!&#$^<>_-]{8,128}'
  _globals['_REDISCONFIG6_0'].fields_by_name['databases']._loaded_options = None
  _globals['_REDISCONFIG6_0'].fields_by_name['databases']._serialized_options = b'\372\3071\002>0'
  _globals['_REDISCONFIG6_0'].fields_by_name['slowlog_log_slower_than']._loaded_options = None
  _globals['_REDISCONFIG6_0'].fields_by_name['slowlog_log_slower_than']._serialized_options = b'\372\3071\003>=0'
  _globals['_REDISCONFIG6_0'].fields_by_name['slowlog_max_len']._loaded_options = None
  _globals['_REDISCONFIG6_0'].fields_by_name['slowlog_max_len']._serialized_options = b'\372\3071\003>=0'
  _globals['_REDISCONFIG6_0'].fields_by_name['notify_keyspace_events']._loaded_options = None
  _globals['_REDISCONFIG6_0'].fields_by_name['notify_keyspace_events']._serialized_options = b'\362\3071\025[KEg$lshzxeAtm]{0,13}'
  _globals['_REDISCONFIG6_0']._serialized_start=149
  _globals['_REDISCONFIG6_0']._serialized_end=1259
  _globals['_REDISCONFIG6_0_CLIENTOUTPUTBUFFERLIMIT']._serialized_start=847
  _globals['_REDISCONFIG6_0_CLIENTOUTPUTBUFFERLIMIT']._serialized_end=1060
  _globals['_REDISCONFIG6_0_MAXMEMORYPOLICY']._serialized_start=1063
  _globals['_REDISCONFIG6_0_MAXMEMORYPOLICY']._serialized_end=1259
  _globals['_REDISCONFIGSET6_0']._serialized_start=1262
  _globals['_REDISCONFIGSET6_0']._serialized_end=1502
# @@protoc_insertion_point(module_scope)
