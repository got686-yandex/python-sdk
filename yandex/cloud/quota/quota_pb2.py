# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/quota/quota.proto
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
    'yandex/cloud/quota/quota.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eyandex/cloud/quota/quota.proto\x12\x12yandex.cloud.quota\"?\n\x0bQuotaMetric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x03\x12\r\n\x05usage\x18\x04 \x01(\x01J\x04\x08\x02\x10\x03\"*\n\x0bMetricLimit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x03\"\x9e\x01\n\x0cQuotaFailure\x12>\n\nviolations\x18\x02 \x03(\x0b\x32*.yandex.cloud.quota.QuotaFailure.Violation\x1aN\n\tViolation\x12/\n\x06metric\x18\x01 \x01(\x0b\x32\x1f.yandex.cloud.quota.QuotaMetric\x12\x10\n\x08required\x18\x02 \x01(\x03\x42V\n\x16yandex.cloud.api.quotaZ<github.com/yandex-cloud/go-genproto/yandex/cloud/quota;quotab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.quota.quota_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026yandex.cloud.api.quotaZ<github.com/yandex-cloud/go-genproto/yandex/cloud/quota;quota'
  _globals['_QUOTAMETRIC']._serialized_start=54
  _globals['_QUOTAMETRIC']._serialized_end=117
  _globals['_METRICLIMIT']._serialized_start=119
  _globals['_METRICLIMIT']._serialized_end=161
  _globals['_QUOTAFAILURE']._serialized_start=164
  _globals['_QUOTAFAILURE']._serialized_end=322
  _globals['_QUOTAFAILURE_VIOLATION']._serialized_start=244
  _globals['_QUOTAFAILURE_VIOLATION']._serialized_end=322
# @@protoc_insertion_point(module_scope)
