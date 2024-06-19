# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/api_key_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.iam.v1 import api_key_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_api__key__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/iam/v1/api_key_service.proto\x12\x13yandex.cloud.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a yandex/cloud/api/operation.proto\x1a!yandex/cloud/iam/v1/api_key.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"4\n\x10GetApiKeyRequest\x12 \n\napi_key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"y\n\x12ListApiKeysRequest\x12$\n\x12service_account_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"]\n\x13ListApiKeysResponse\x12-\n\x08\x61pi_keys\x18\x01 \x03(\x0b\x32\x1b.yandex.cloud.iam.v1.ApiKey\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa5\x01\n\x13\x43reateApiKeyRequest\x12$\n\x12service_account_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1e\n\x0b\x64\x65scription\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x18\n\x05scope\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12.\n\nexpires_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"T\n\x14\x43reateApiKeyResponse\x12,\n\x07\x61pi_key\x18\x01 \x01(\x0b\x32\x1b.yandex.cloud.iam.v1.ApiKey\x12\x0e\n\x06secret\x18\x02 \x01(\t\"\x88\x01\n\x13UpdateApiKeyRequest\x12 \n\napi_key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\"*\n\x14UpdateApiKeyMetadata\x12\x12\n\napi_key_id\x18\x01 \x01(\t\"7\n\x13\x44\x65leteApiKeyRequest\x12 \n\napi_key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"*\n\x14\x44\x65leteApiKeyMetadata\x12\x12\n\napi_key_id\x18\x01 \x01(\t\"~\n\x1bListApiKeyOperationsRequest\x12 \n\napi_key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"n\n\x1cListApiKeyOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"X\n\x17ListApiKeyScopesRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x02 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"C\n\x18ListApiKeyScopesResponse\x12\x0e\n\x06scopes\x18\x01 \x03(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xf6\x07\n\rApiKeyService\x12r\n\x04List\x12\'.yandex.cloud.iam.v1.ListApiKeysRequest\x1a(.yandex.cloud.iam.v1.ListApiKeysResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/iam/v1/apiKeys\x12o\n\x03Get\x12%.yandex.cloud.iam.v1.GetApiKeyRequest\x1a\x1b.yandex.cloud.iam.v1.ApiKey\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/iam/v1/apiKeys/{api_key_id}\x12y\n\x06\x43reate\x12(.yandex.cloud.iam.v1.CreateApiKeyRequest\x1a).yandex.cloud.iam.v1.CreateApiKeyResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/iam/v1/apiKeys:\x01*\x12\xa0\x01\n\x06Update\x12(.yandex.cloud.iam.v1.UpdateApiKeyRequest\x1a!.yandex.cloud.operation.Operation\"I\xb2\xd2*\x1e\n\x14UpdateApiKeyMetadata\x12\x06\x41piKey\x82\xd3\xe4\x93\x02!2\x1c/iam/v1/apiKeys/{api_key_id}:\x01*\x12\xac\x01\n\x06\x44\x65lete\x12(.yandex.cloud.iam.v1.DeleteApiKeyRequest\x1a!.yandex.cloud.operation.Operation\"U\xb2\xd2*-\n\x14\x44\x65leteApiKeyMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1e*\x1c/iam/v1/apiKeys/{api_key_id}\x12\xa6\x01\n\x0eListOperations\x12\x30.yandex.cloud.iam.v1.ListApiKeyOperationsRequest\x1a\x31.yandex.cloud.iam.v1.ListApiKeyOperationsResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/iam/v1/apiKeys/{api_key_id}/operations\x12\x89\x01\n\nListScopes\x12,.yandex.cloud.iam.v1.ListApiKeyScopesRequest\x1a-.yandex.cloud.iam.v1.ListApiKeyScopesResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/iam/v1/apiKeys/scopesBV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iam.v1.api_key_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam'
  _GETAPIKEYREQUEST.fields_by_name['api_key_id']._options = None
  _GETAPIKEYREQUEST.fields_by_name['api_key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTAPIKEYSREQUEST.fields_by_name['service_account_id']._options = None
  _LISTAPIKEYSREQUEST.fields_by_name['service_account_id']._serialized_options = b'\212\3101\004<=50'
  _LISTAPIKEYSREQUEST.fields_by_name['page_size']._options = None
  _LISTAPIKEYSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTAPIKEYSREQUEST.fields_by_name['page_token']._options = None
  _LISTAPIKEYSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _CREATEAPIKEYREQUEST.fields_by_name['service_account_id']._options = None
  _CREATEAPIKEYREQUEST.fields_by_name['service_account_id']._serialized_options = b'\212\3101\004<=50'
  _CREATEAPIKEYREQUEST.fields_by_name['description']._options = None
  _CREATEAPIKEYREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATEAPIKEYREQUEST.fields_by_name['scope']._options = None
  _CREATEAPIKEYREQUEST.fields_by_name['scope']._serialized_options = b'\212\3101\005<=256'
  _UPDATEAPIKEYREQUEST.fields_by_name['api_key_id']._options = None
  _UPDATEAPIKEYREQUEST.fields_by_name['api_key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEAPIKEYREQUEST.fields_by_name['description']._options = None
  _UPDATEAPIKEYREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _DELETEAPIKEYREQUEST.fields_by_name['api_key_id']._options = None
  _DELETEAPIKEYREQUEST.fields_by_name['api_key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTAPIKEYOPERATIONSREQUEST.fields_by_name['api_key_id']._options = None
  _LISTAPIKEYOPERATIONSREQUEST.fields_by_name['api_key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTAPIKEYOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTAPIKEYOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTAPIKEYOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTAPIKEYOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _LISTAPIKEYSCOPESREQUEST.fields_by_name['page_size']._options = None
  _LISTAPIKEYSCOPESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTAPIKEYSCOPESREQUEST.fields_by_name['page_token']._options = None
  _LISTAPIKEYSCOPESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _APIKEYSERVICE.methods_by_name['List']._options = None
  _APIKEYSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\021\022\017/iam/v1/apiKeys'
  _APIKEYSERVICE.methods_by_name['Get']._options = None
  _APIKEYSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\036\022\034/iam/v1/apiKeys/{api_key_id}'
  _APIKEYSERVICE.methods_by_name['Create']._options = None
  _APIKEYSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\024\"\017/iam/v1/apiKeys:\001*'
  _APIKEYSERVICE.methods_by_name['Update']._options = None
  _APIKEYSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\036\n\024UpdateApiKeyMetadata\022\006ApiKey\202\323\344\223\002!2\034/iam/v1/apiKeys/{api_key_id}:\001*'
  _APIKEYSERVICE.methods_by_name['Delete']._options = None
  _APIKEYSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*-\n\024DeleteApiKeyMetadata\022\025google.protobuf.Empty\202\323\344\223\002\036*\034/iam/v1/apiKeys/{api_key_id}'
  _APIKEYSERVICE.methods_by_name['ListOperations']._options = None
  _APIKEYSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002)\022\'/iam/v1/apiKeys/{api_key_id}/operations'
  _APIKEYSERVICE.methods_by_name['ListScopes']._options = None
  _APIKEYSERVICE.methods_by_name['ListScopes']._serialized_options = b'\202\323\344\223\002\030\022\026/iam/v1/apiKeys/scopes'
  _globals['_GETAPIKEYREQUEST']._serialized_start=303
  _globals['_GETAPIKEYREQUEST']._serialized_end=355
  _globals['_LISTAPIKEYSREQUEST']._serialized_start=357
  _globals['_LISTAPIKEYSREQUEST']._serialized_end=478
  _globals['_LISTAPIKEYSRESPONSE']._serialized_start=480
  _globals['_LISTAPIKEYSRESPONSE']._serialized_end=573
  _globals['_CREATEAPIKEYREQUEST']._serialized_start=576
  _globals['_CREATEAPIKEYREQUEST']._serialized_end=741
  _globals['_CREATEAPIKEYRESPONSE']._serialized_start=743
  _globals['_CREATEAPIKEYRESPONSE']._serialized_end=827
  _globals['_UPDATEAPIKEYREQUEST']._serialized_start=830
  _globals['_UPDATEAPIKEYREQUEST']._serialized_end=966
  _globals['_UPDATEAPIKEYMETADATA']._serialized_start=968
  _globals['_UPDATEAPIKEYMETADATA']._serialized_end=1010
  _globals['_DELETEAPIKEYREQUEST']._serialized_start=1012
  _globals['_DELETEAPIKEYREQUEST']._serialized_end=1067
  _globals['_DELETEAPIKEYMETADATA']._serialized_start=1069
  _globals['_DELETEAPIKEYMETADATA']._serialized_end=1111
  _globals['_LISTAPIKEYOPERATIONSREQUEST']._serialized_start=1113
  _globals['_LISTAPIKEYOPERATIONSREQUEST']._serialized_end=1239
  _globals['_LISTAPIKEYOPERATIONSRESPONSE']._serialized_start=1241
  _globals['_LISTAPIKEYOPERATIONSRESPONSE']._serialized_end=1351
  _globals['_LISTAPIKEYSCOPESREQUEST']._serialized_start=1353
  _globals['_LISTAPIKEYSCOPESREQUEST']._serialized_end=1441
  _globals['_LISTAPIKEYSCOPESRESPONSE']._serialized_start=1443
  _globals['_LISTAPIKEYSCOPESRESPONSE']._serialized_end=1510
  _globals['_APIKEYSERVICE']._serialized_start=1513
  _globals['_APIKEYSERVICE']._serialized_end=2527
# @@protoc_insertion_point(module_scope)
