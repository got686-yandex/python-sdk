# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadtesting/api/v1/report/table/report.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.loadtesting.api.v1.common import quantiles_pb2 as yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_common_dot_quantiles__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9yandex/cloud/loadtesting/api/v1/report/table/report.proto\x12,yandex.cloud.loadtesting.api.v1.report.table\x1a\x36yandex/cloud/loadtesting/api/v1/common/quantiles.proto\"\xe1\x02\n\x06Report\x12W\n\nhttp_codes\x18\x01 \x03(\x0b\x32\x43.yandex.cloud.loadtesting.api.v1.report.table.Report.HttpCodesEntry\x12U\n\tnet_codes\x18\x02 \x03(\x0b\x32\x42.yandex.cloud.loadtesting.api.v1.report.table.Report.NetCodesEntry\x12\x44\n\tquantiles\x18\x03 \x01(\x0b\x32\x31.yandex.cloud.loadtesting.api.v1.common.Quantiles\x1a\x30\n\x0eHttpCodesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a/\n\rNetCodesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x42\x8a\x01\n0yandex.cloud.api.loadtesting.api.v1.report.tableZVgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/api/v1/report/table;tableb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.loadtesting.api.v1.report.table.report_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n0yandex.cloud.api.loadtesting.api.v1.report.tableZVgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/api/v1/report/table;table'
  _REPORT_HTTPCODESENTRY._options = None
  _REPORT_HTTPCODESENTRY._serialized_options = b'8\001'
  _REPORT_NETCODESENTRY._options = None
  _REPORT_NETCODESENTRY._serialized_options = b'8\001'
  _globals['_REPORT']._serialized_start=164
  _globals['_REPORT']._serialized_end=517
  _globals['_REPORT_HTTPCODESENTRY']._serialized_start=420
  _globals['_REPORT_HTTPCODESENTRY']._serialized_end=468
  _globals['_REPORT_NETCODESENTRY']._serialized_start=470
  _globals['_REPORT_NETCODESENTRY']._serialized_end=517
# @@protoc_insertion_point(module_scope)
