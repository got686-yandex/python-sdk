# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ydb/v1/storage_type_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.ydb.v1 import storage_type_pb2 as yandex_dot_cloud_dot_ydb_dot_v1_dot_storage__type__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/ydb/v1/storage_type_service.proto\x12\x13yandex.cloud.ydb.v1\x1a\x1cgoogle/api/annotations.proto\x1a&yandex/cloud/ydb/v1/storage_type.proto\x1a\x1dyandex/cloud/validation.proto\"6\n\x15GetStorageTypeRequest\x12\x1d\n\x0fstorage_type_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"W\n\x17ListStorageTypesRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\"l\n\x18ListStorageTypesResponse\x12\x37\n\rstorage_types\x18\x01 \x03(\x0b\x32 .yandex.cloud.ydb.v1.StorageType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x9e\x02\n\x12StorageTypeService\x12\x83\x01\n\x03Get\x12*.yandex.cloud.ydb.v1.GetStorageTypeRequest\x1a .yandex.cloud.ydb.v1.StorageType\".\x82\xd3\xe4\x93\x02(\x12&/ydb/v1/storageTypes/{storage_type_id}\x12\x81\x01\n\x04List\x12,.yandex.cloud.ydb.v1.ListStorageTypesRequest\x1a-.yandex.cloud.ydb.v1.ListStorageTypesResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/ydb/v1/storageTypesBV\n\x17yandex.cloud.api.ydb.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1;ydbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ydb.v1.storage_type_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.ydb.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1;ydb'
  _GETSTORAGETYPEREQUEST.fields_by_name['storage_type_id']._options = None
  _GETSTORAGETYPEREQUEST.fields_by_name['storage_type_id']._serialized_options = b'\350\3071\001'
  _LISTSTORAGETYPESREQUEST.fields_by_name['page_size']._options = None
  _LISTSTORAGETYPESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTSTORAGETYPESREQUEST.fields_by_name['page_token']._options = None
  _LISTSTORAGETYPESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _STORAGETYPESERVICE.methods_by_name['Get']._options = None
  _STORAGETYPESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002(\022&/ydb/v1/storageTypes/{storage_type_id}'
  _STORAGETYPESERVICE.methods_by_name['List']._options = None
  _STORAGETYPESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\026\022\024/ydb/v1/storageTypes'
  _globals['_GETSTORAGETYPEREQUEST']._serialized_start=172
  _globals['_GETSTORAGETYPEREQUEST']._serialized_end=226
  _globals['_LISTSTORAGETYPESREQUEST']._serialized_start=228
  _globals['_LISTSTORAGETYPESREQUEST']._serialized_end=315
  _globals['_LISTSTORAGETYPESRESPONSE']._serialized_start=317
  _globals['_LISTSTORAGETYPESRESPONSE']._serialized_end=425
  _globals['_STORAGETYPESERVICE']._serialized_start=428
  _globals['_STORAGETYPESERVICE']._serialized_end=714
# @@protoc_insertion_point(module_scope)
