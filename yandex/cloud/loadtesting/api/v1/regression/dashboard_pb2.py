# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/loadtesting/api/v1/regression/dashboard.proto
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
    'yandex/cloud/loadtesting/api/v1/regression/dashboard.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.loadtesting.api.v1.regression import widget_pb2 as yandex_dot_cloud_dot_loadtesting_dot_api_dot_v1_dot_regression_dot_widget__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/loadtesting/api/v1/regression/dashboard.proto\x12*yandex.cloud.loadtesting.api.v1.regression\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x37yandex/cloud/loadtesting/api/v1/regression/widget.proto\"\xf0\x02\n\tDashboard\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x06 \x01(\t\x12\x12\n\nupdated_by\x18\x07 \x01(\t\x12\x0c\n\x04\x65tag\x18\x08 \x01(\t\x12N\n\x07\x63ontent\x18\t \x01(\x0b\x32=.yandex.cloud.loadtesting.api.v1.regression.Dashboard.Content\x1aN\n\x07\x43ontent\x12\x43\n\x07widgets\x18\x01 \x03(\x0b\x32\x32.yandex.cloud.loadtesting.api.v1.regression.WidgetB\x8b\x01\n.yandex.cloud.api.loadtesting.api.v1.regressionZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/api/v1/regression;regressionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.loadtesting.api.v1.regression.dashboard_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n.yandex.cloud.api.loadtesting.api.v1.regressionZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/api/v1/regression;regression'
  _globals['_DASHBOARD']._serialized_start=197
  _globals['_DASHBOARD']._serialized_end=565
  _globals['_DASHBOARD_CONTENT']._serialized_start=487
  _globals['_DASHBOARD_CONTENT']._serialized_end=565
# @@protoc_insertion_point(module_scope)
