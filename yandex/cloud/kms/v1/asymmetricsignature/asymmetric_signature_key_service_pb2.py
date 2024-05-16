# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/kms/v1/asymmetricsignature/asymmetric_signature_key_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.kms.v1.asymmetricsignature import asymmetric_signature_key_pb2 as yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricsignature_dot_asymmetric__signature__key__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNyandex/cloud/kms/v1/asymmetricsignature/asymmetric_signature_key_service.proto\x12\'yandex.cloud.kms.v1.asymmetricsignature\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x46yandex/cloud/kms/v1/asymmetricsignature/asymmetric_signature_key.proto\"\xd8\x03\n#CreateAsymmetricSignatureKeyRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x17\n\x04name\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1f\n\x0b\x64\x65scription\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12\xa5\x01\n\x06labels\x18\x04 \x03(\x0b\x32X.yandex.cloud.kms.v1.asymmetricsignature.CreateAsymmetricSignatureKeyRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12\x62\n\x13signature_algorithm\x18\x05 \x01(\x0e\x32\x45.yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignatureAlgorithm\x12\x1b\n\x13\x64\x65letion_protection\x18\x06 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n$CreateAsymmetricSignatureKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"@\n GetAsymmetricSignatureKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x83\x01\n\"ListAsymmetricSignatureKeysRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x8d\x01\n#ListAsymmetricSignatureKeysResponse\x12M\n\x04keys\x18\x01 \x03(\x0b\x32?.yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignatureKey\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x80\x04\n#UpdateAsymmetricSignatureKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe8\xc7\x31\x01\x12\x17\n\x04name\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1f\n\x0b\x64\x65scription\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12V\n\x06status\x18\x05 \x01(\x0e\x32\x46.yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignatureKey.Status\x12\xa5\x01\n\x06labels\x18\x06 \x03(\x0b\x32X.yandex.cloud.kms.v1.asymmetricsignature.UpdateAsymmetricSignatureKeyRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12\x1b\n\x13\x64\x65letion_protection\x18\x07 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n$UpdateAsymmetricSignatureKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"C\n#DeleteAsymmetricSignatureKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"6\n$DeleteAsymmetricSignatureKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"\x89\x01\n+ListAsymmetricSignatureKeyOperationsRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"~\n,ListAsymmetricSignatureKeyOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xae\x10\n\x1d\x41symmetricSignatureKeyService\x12\xe7\x01\n\x06\x43reate\x12L.yandex.cloud.kms.v1.asymmetricsignature.CreateAsymmetricSignatureKeyRequest\x1a!.yandex.cloud.operation.Operation\"l\xb2\xd2*>\n$CreateAsymmetricSignatureKeyMetadata\x12\x16\x41symmetricSignatureKey\x82\xd3\xe4\x93\x02$\"\x1f/kms/v1/asymmetricSignatureKeys:\x01*\x12\xc3\x01\n\x03Get\x12I.yandex.cloud.kms.v1.asymmetricsignature.GetAsymmetricSignatureKeyRequest\x1a?.yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignatureKey\"0\x82\xd3\xe4\x93\x02*\x12(/kms/v1/asymmetricSignatureKeys/{key_id}\x12\xca\x01\n\x04List\x12K.yandex.cloud.kms.v1.asymmetricsignature.ListAsymmetricSignatureKeysRequest\x1aL.yandex.cloud.kms.v1.asymmetricsignature.ListAsymmetricSignatureKeysResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/kms/v1/asymmetricSignatureKeys\x12\xf0\x01\n\x06Update\x12L.yandex.cloud.kms.v1.asymmetricsignature.UpdateAsymmetricSignatureKeyRequest\x1a!.yandex.cloud.operation.Operation\"u\xb2\xd2*>\n$UpdateAsymmetricSignatureKeyMetadata\x12\x16\x41symmetricSignatureKey\x82\xd3\xe4\x93\x02-2(/kms/v1/asymmetricSignatureKeys/{key_id}:\x01*\x12\xed\x01\n\x06\x44\x65lete\x12L.yandex.cloud.kms.v1.asymmetricsignature.DeleteAsymmetricSignatureKeyRequest\x1a!.yandex.cloud.operation.Operation\"r\xb2\xd2*>\n$DeleteAsymmetricSignatureKeyMetadata\x12\x16\x41symmetricSignatureKey\x82\xd3\xe4\x93\x02**(/kms/v1/asymmetricSignatureKeys/{key_id}\x12\xfa\x01\n\x0eListOperations\x12T.yandex.cloud.kms.v1.asymmetricsignature.ListAsymmetricSignatureKeyOperationsRequest\x1aU.yandex.cloud.kms.v1.asymmetricsignature.ListAsymmetricSignatureKeyOperationsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/kms/v1/asymmetricSignatureKeys/{key_id}/operations\x12\xbf\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"H\x82\xd3\xe4\x93\x02\x42\x12@/kms/v1/asymmetricSignatureKeys/{resource_id}:listAccessBindings\x12\xef\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x87\x01\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x44\"?/kms/v1/asymmetricSignatureKeys/{resource_id}:setAccessBindings:\x01*\x12\xfb\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8d\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02G\"B/kms/v1/asymmetricSignatureKeys/{resource_id}:updateAccessBindings:\x01*Bj\n\x17yandex.cloud.api.kms.v1ZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricsignature;kmsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.kms.v1.asymmetricsignature.asymmetric_signature_key_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.kms.v1ZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricsignature;kms'
  _CREATEASYMMETRICSIGNATUREKEYREQUEST_LABELSENTRY._options = None
  _CREATEASYMMETRICSIGNATUREKEYREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['folder_id']._options = None
  _CREATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['name']._options = None
  _CREATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['name']._serialized_options = b'\212\3101\005<=100'
  _CREATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['description']._options = None
  _CREATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\006<=1024'
  _CREATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['labels']._options = None
  _CREATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _GETASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['key_id']._options = None
  _GETASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTASYMMETRICSIGNATUREKEYSREQUEST.fields_by_name['folder_id']._options = None
  _LISTASYMMETRICSIGNATUREKEYSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTASYMMETRICSIGNATUREKEYSREQUEST.fields_by_name['page_size']._options = None
  _LISTASYMMETRICSIGNATUREKEYSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTASYMMETRICSIGNATUREKEYSREQUEST.fields_by_name['page_token']._options = None
  _LISTASYMMETRICSIGNATUREKEYSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST_LABELSENTRY._options = None
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['key_id']._options = None
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['update_mask']._serialized_options = b'\350\3071\001'
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['name']._options = None
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['name']._serialized_options = b'\212\3101\005<=100'
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['description']._options = None
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\006<=1024'
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['labels']._options = None
  _UPDATEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _DELETEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['key_id']._options = None
  _DELETEASYMMETRICSIGNATUREKEYREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTASYMMETRICSIGNATUREKEYOPERATIONSREQUEST.fields_by_name['key_id']._options = None
  _LISTASYMMETRICSIGNATUREKEYOPERATIONSREQUEST.fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTASYMMETRICSIGNATUREKEYOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTASYMMETRICSIGNATUREKEYOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTASYMMETRICSIGNATUREKEYOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTASYMMETRICSIGNATUREKEYOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['Create']._options = None
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*>\n$CreateAsymmetricSignatureKeyMetadata\022\026AsymmetricSignatureKey\202\323\344\223\002$\"\037/kms/v1/asymmetricSignatureKeys:\001*'
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['Get']._options = None
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002*\022(/kms/v1/asymmetricSignatureKeys/{key_id}'
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['List']._options = None
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/kms/v1/asymmetricSignatureKeys'
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['Update']._options = None
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*>\n$UpdateAsymmetricSignatureKeyMetadata\022\026AsymmetricSignatureKey\202\323\344\223\002-2(/kms/v1/asymmetricSignatureKeys/{key_id}:\001*'
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['Delete']._options = None
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*>\n$DeleteAsymmetricSignatureKeyMetadata\022\026AsymmetricSignatureKey\202\323\344\223\002**(/kms/v1/asymmetricSignatureKeys/{key_id}'
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['ListOperations']._options = None
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0025\0223/kms/v1/asymmetricSignatureKeys/{key_id}/operations'
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['ListAccessBindings']._options = None
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002B\022@/kms/v1/asymmetricSignatureKeys/{resource_id}:listAccessBindings'
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['SetAccessBindings']._options = None
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002D\"?/kms/v1/asymmetricSignatureKeys/{resource_id}:setAccessBindings:\001*'
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _ASYMMETRICSIGNATUREKEYSERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002G\"B/kms/v1/asymmetricSignatureKeys/{resource_id}:updateAccessBindings:\001*'
  _globals['_CREATEASYMMETRICSIGNATUREKEYREQUEST']._serialized_start=399
  _globals['_CREATEASYMMETRICSIGNATUREKEYREQUEST']._serialized_end=871
  _globals['_CREATEASYMMETRICSIGNATUREKEYREQUEST_LABELSENTRY']._serialized_start=826
  _globals['_CREATEASYMMETRICSIGNATUREKEYREQUEST_LABELSENTRY']._serialized_end=871
  _globals['_CREATEASYMMETRICSIGNATUREKEYMETADATA']._serialized_start=873
  _globals['_CREATEASYMMETRICSIGNATUREKEYMETADATA']._serialized_end=927
  _globals['_GETASYMMETRICSIGNATUREKEYREQUEST']._serialized_start=929
  _globals['_GETASYMMETRICSIGNATUREKEYREQUEST']._serialized_end=993
  _globals['_LISTASYMMETRICSIGNATUREKEYSREQUEST']._serialized_start=996
  _globals['_LISTASYMMETRICSIGNATUREKEYSREQUEST']._serialized_end=1127
  _globals['_LISTASYMMETRICSIGNATUREKEYSRESPONSE']._serialized_start=1130
  _globals['_LISTASYMMETRICSIGNATUREKEYSRESPONSE']._serialized_end=1271
  _globals['_UPDATEASYMMETRICSIGNATUREKEYREQUEST']._serialized_start=1274
  _globals['_UPDATEASYMMETRICSIGNATUREKEYREQUEST']._serialized_end=1786
  _globals['_UPDATEASYMMETRICSIGNATUREKEYREQUEST_LABELSENTRY']._serialized_start=826
  _globals['_UPDATEASYMMETRICSIGNATUREKEYREQUEST_LABELSENTRY']._serialized_end=871
  _globals['_UPDATEASYMMETRICSIGNATUREKEYMETADATA']._serialized_start=1788
  _globals['_UPDATEASYMMETRICSIGNATUREKEYMETADATA']._serialized_end=1842
  _globals['_DELETEASYMMETRICSIGNATUREKEYREQUEST']._serialized_start=1844
  _globals['_DELETEASYMMETRICSIGNATUREKEYREQUEST']._serialized_end=1911
  _globals['_DELETEASYMMETRICSIGNATUREKEYMETADATA']._serialized_start=1913
  _globals['_DELETEASYMMETRICSIGNATUREKEYMETADATA']._serialized_end=1967
  _globals['_LISTASYMMETRICSIGNATUREKEYOPERATIONSREQUEST']._serialized_start=1970
  _globals['_LISTASYMMETRICSIGNATUREKEYOPERATIONSREQUEST']._serialized_end=2107
  _globals['_LISTASYMMETRICSIGNATUREKEYOPERATIONSRESPONSE']._serialized_start=2109
  _globals['_LISTASYMMETRICSIGNATUREKEYOPERATIONSRESPONSE']._serialized_end=2235
  _globals['_ASYMMETRICSIGNATUREKEYSERVICE']._serialized_start=2238
  _globals['_ASYMMETRICSIGNATUREKEYSERVICE']._serialized_end=4332
# @@protoc_insertion_point(module_scope)
