# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/billing/v1/billable_object.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/billing/v1/billable_object.proto\x12\x17yandex.cloud.billing.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"*\n\x0e\x42illableObject\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"\x8d\x01\n\x15\x42illableObjectBinding\x12\x32\n\x0e\x65\x66\x66\x65\x63tive_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12@\n\x0f\x62illable_object\x18\x02 \x01(\x0b\x32\'.yandex.cloud.billing.v1.BillableObjectBb\n\x1byandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.billing.v1.billable_object_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billing'
  _globals['_BILLABLEOBJECT']._serialized_start=107
  _globals['_BILLABLEOBJECT']._serialized_end=149
  _globals['_BILLABLEOBJECTBINDING']._serialized_start=152
  _globals['_BILLABLEOBJECTBINDING']._serialized_end=293
# @@protoc_insertion_point(module_scope)
