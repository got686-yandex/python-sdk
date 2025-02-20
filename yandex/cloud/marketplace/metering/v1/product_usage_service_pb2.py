# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/marketplace/metering/v1/product_usage_service.proto
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
    'yandex/cloud/marketplace/metering/v1/product_usage_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.marketplace.metering.v1 import usage_record_pb2 as yandex_dot_cloud_dot_marketplace_dot_metering_dot_v1_dot_usage__record__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@yandex/cloud/marketplace/metering/v1/product_usage_service.proto\x12$yandex.cloud.marketplace.metering.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x37yandex/cloud/marketplace/metering/v1/usage_record.proto\"\xa3\x01\n\x11WriteUsageRequest\x12\x0f\n\x07\x64ry_run\x18\x01 \x01(\x08\x12)\n\x13product_instance_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12R\n\rusage_records\x18\x03 \x03(\x0b\x32\x31.yandex.cloud.marketplace.metering.v1.UsageRecordB\x08\x82\xc8\x31\x04\x31-25\"\xae\x01\n\x12WriteUsageResponse\x12K\n\x08\x61\x63\x63\x65pted\x18\x01 \x03(\x0b\x32\x39.yandex.cloud.marketplace.metering.v1.AcceptedUsageRecord\x12K\n\x08rejected\x18\x02 \x03(\x0b\x32\x39.yandex.cloud.marketplace.metering.v1.RejectedUsageRecord2\xca\x01\n\x13ProductUsageService\x12\xb2\x01\n\x05Write\x12\x37.yandex.cloud.marketplace.metering.v1.WriteUsageRequest\x1a\x38.yandex.cloud.marketplace.metering.v1.WriteUsageResponse\"6\x82\xd3\xe4\x93\x02\x30\"+/marketplace/metering/v1/productUsage/write:\x01*B}\n(yandex.cloud.api.marketplace.metering.v1ZQgithub.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/metering/v1;meteringb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.marketplace.metering.v1.product_usage_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.marketplace.metering.v1ZQgithub.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/metering/v1;metering'
  _globals['_WRITEUSAGEREQUEST'].fields_by_name['product_instance_id']._loaded_options = None
  _globals['_WRITEUSAGEREQUEST'].fields_by_name['product_instance_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_WRITEUSAGEREQUEST'].fields_by_name['usage_records']._loaded_options = None
  _globals['_WRITEUSAGEREQUEST'].fields_by_name['usage_records']._serialized_options = b'\202\3101\0041-25'
  _globals['_PRODUCTUSAGESERVICE'].methods_by_name['Write']._loaded_options = None
  _globals['_PRODUCTUSAGESERVICE'].methods_by_name['Write']._serialized_options = b'\202\323\344\223\0020\"+/marketplace/metering/v1/productUsage/write:\001*'
  _globals['_WRITEUSAGEREQUEST']._serialized_start=225
  _globals['_WRITEUSAGEREQUEST']._serialized_end=388
  _globals['_WRITEUSAGERESPONSE']._serialized_start=391
  _globals['_WRITEUSAGERESPONSE']._serialized_end=565
  _globals['_PRODUCTUSAGESERVICE']._serialized_start=568
  _globals['_PRODUCTUSAGESERVICE']._serialized_end=770
# @@protoc_insertion_point(module_scope)
