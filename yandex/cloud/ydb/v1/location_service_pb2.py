# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ydb/v1/location_service.proto
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
    'yandex/cloud/ydb/v1/location_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.ydb.v1 import location_pb2 as yandex_dot_cloud_dot_ydb_dot_v1_dot_location__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/ydb/v1/location_service.proto\x12\x13yandex.cloud.ydb.v1\x1a\x1cgoogle/api/annotations.proto\x1a\"yandex/cloud/ydb/v1/location.proto\x1a\x1dyandex/cloud/validation.proto\"/\n\x12GetLocationRequest\x12\x19\n\x0blocation_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"T\n\x14ListLocationsRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\"b\n\x15ListLocationsResponse\x12\x30\n\tlocations\x18\x01 \x03(\x0b\x32\x1d.yandex.cloud.ydb.v1.Location\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x83\x02\n\x0fLocationService\x12v\n\x03Get\x12\'.yandex.cloud.ydb.v1.GetLocationRequest\x1a\x1d.yandex.cloud.ydb.v1.Location\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/ydb/v1/locations/{location_id}\x12x\n\x04List\x12).yandex.cloud.ydb.v1.ListLocationsRequest\x1a*.yandex.cloud.ydb.v1.ListLocationsResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/ydb/v1/locationsBV\n\x17yandex.cloud.api.ydb.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1;ydbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ydb.v1.location_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.ydb.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1;ydb'
  _globals['_GETLOCATIONREQUEST'].fields_by_name['location_id']._loaded_options = None
  _globals['_GETLOCATIONREQUEST'].fields_by_name['location_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTLOCATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTLOCATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTLOCATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTLOCATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LOCATIONSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_LOCATIONSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002!\022\037/ydb/v1/locations/{location_id}'
  _globals['_LOCATIONSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_LOCATIONSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\023\022\021/ydb/v1/locations'
  _globals['_GETLOCATIONREQUEST']._serialized_start=164
  _globals['_GETLOCATIONREQUEST']._serialized_end=211
  _globals['_LISTLOCATIONSREQUEST']._serialized_start=213
  _globals['_LISTLOCATIONSREQUEST']._serialized_end=297
  _globals['_LISTLOCATIONSRESPONSE']._serialized_start=299
  _globals['_LISTLOCATIONSRESPONSE']._serialized_end=397
  _globals['_LOCATIONSERVICE']._serialized_start=400
  _globals['_LOCATIONSERVICE']._serialized_end=659
# @@protoc_insertion_point(module_scope)
