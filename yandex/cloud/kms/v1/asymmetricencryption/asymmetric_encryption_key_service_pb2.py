# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_key_service.proto
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
    'yandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_key_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.kms.v1.asymmetricencryption import asymmetric_encryption_key_pb2 as yandex_dot_cloud_dot_kms_dot_v1_dot_asymmetricencryption_dot_asymmetric__encryption__key__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nPyandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_key_service.proto\x12(yandex.cloud.kms.v1.asymmetricencryption\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1aHyandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_key.proto\"\xde\x03\n$CreateAsymmetricEncryptionKeyRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x17\n\x04name\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1f\n\x0b\x64\x65scription\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12\xa7\x01\n\x06labels\x18\x04 \x03(\x0b\x32Z.yandex.cloud.kms.v1.asymmetricencryption.CreateAsymmetricEncryptionKeyRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12\x65\n\x14\x65ncryption_algorithm\x18\x05 \x01(\x0e\x32G.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionAlgorithm\x12\x1b\n\x13\x64\x65letion_protection\x18\x06 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"7\n%CreateAsymmetricEncryptionKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"A\n!GetAsymmetricEncryptionKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x84\x01\n#ListAsymmetricEncryptionKeysRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x90\x01\n$ListAsymmetricEncryptionKeysResponse\x12O\n\x04keys\x18\x01 \x03(\x0b\x32\x41.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x85\x04\n$UpdateAsymmetricEncryptionKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x35\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe8\xc7\x31\x01\x12\x17\n\x04name\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1f\n\x0b\x64\x65scription\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12X\n\x06status\x18\x05 \x01(\x0e\x32H.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.Status\x12\xa7\x01\n\x06labels\x18\x06 \x03(\x0b\x32Z.yandex.cloud.kms.v1.asymmetricencryption.UpdateAsymmetricEncryptionKeyRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12\x1b\n\x13\x64\x65letion_protection\x18\x07 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"7\n%UpdateAsymmetricEncryptionKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"D\n$DeleteAsymmetricEncryptionKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"7\n%DeleteAsymmetricEncryptionKeyMetadata\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"\x8a\x01\n,ListAsymmetricEncryptionKeyOperationsRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x7f\n-ListAsymmetricEncryptionKeyOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd0\x10\n\x1e\x41symmetricEncryptionKeyService\x12\xec\x01\n\x06\x43reate\x12N.yandex.cloud.kms.v1.asymmetricencryption.CreateAsymmetricEncryptionKeyRequest\x1a!.yandex.cloud.operation.Operation\"o\xb2\xd2*@\n%CreateAsymmetricEncryptionKeyMetadata\x12\x17\x41symmetricEncryptionKey\x82\xd3\xe4\x93\x02%\" /kms/v1/asymmetricEncryptionKeys:\x01*\x12\xc8\x01\n\x03Get\x12K.yandex.cloud.kms.v1.asymmetricencryption.GetAsymmetricEncryptionKeyRequest\x1a\x41.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey\"1\x82\xd3\xe4\x93\x02+\x12)/kms/v1/asymmetricEncryptionKeys/{key_id}\x12\xcf\x01\n\x04List\x12M.yandex.cloud.kms.v1.asymmetricencryption.ListAsymmetricEncryptionKeysRequest\x1aN.yandex.cloud.kms.v1.asymmetricencryption.ListAsymmetricEncryptionKeysResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /kms/v1/asymmetricEncryptionKeys\x12\xf5\x01\n\x06Update\x12N.yandex.cloud.kms.v1.asymmetricencryption.UpdateAsymmetricEncryptionKeyRequest\x1a!.yandex.cloud.operation.Operation\"x\xb2\xd2*@\n%UpdateAsymmetricEncryptionKeyMetadata\x12\x17\x41symmetricEncryptionKey\x82\xd3\xe4\x93\x02.2)/kms/v1/asymmetricEncryptionKeys/{key_id}:\x01*\x12\xf2\x01\n\x06\x44\x65lete\x12N.yandex.cloud.kms.v1.asymmetricencryption.DeleteAsymmetricEncryptionKeyRequest\x1a!.yandex.cloud.operation.Operation\"u\xb2\xd2*@\n%DeleteAsymmetricEncryptionKeyMetadata\x12\x17\x41symmetricEncryptionKey\x82\xd3\xe4\x93\x02+*)/kms/v1/asymmetricEncryptionKeys/{key_id}\x12\xff\x01\n\x0eListOperations\x12V.yandex.cloud.kms.v1.asymmetricencryption.ListAsymmetricEncryptionKeyOperationsRequest\x1aW.yandex.cloud.kms.v1.asymmetricencryption.ListAsymmetricEncryptionKeyOperationsResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/kms/v1/asymmetricEncryptionKeys/{key_id}/operations\x12\xc0\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"I\x82\xd3\xe4\x93\x02\x43\x12\x41/kms/v1/asymmetricEncryptionKeys/{resource_id}:listAccessBindings\x12\xf0\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x88\x01\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x45\"@/kms/v1/asymmetricEncryptionKeys/{resource_id}:setAccessBindings:\x01*\x12\xfc\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8e\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02H\"C/kms/v1/asymmetricEncryptionKeys/{resource_id}:updateAccessBindings:\x01*Bk\n\x17yandex.cloud.api.kms.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricencryption;kmsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.kms.v1.asymmetricencryption.asymmetric_encryption_key_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.kms.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricencryption;kms'
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['name']._serialized_options = b'\212\3101\005<=100'
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\006<=1024'
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _globals['_GETASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['key_id']._loaded_options = None
  _globals['_GETASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTASYMMETRICENCRYPTIONKEYSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTASYMMETRICENCRYPTIONKEYSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTASYMMETRICENCRYPTIONKEYSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTASYMMETRICENCRYPTIONKEYSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTASYMMETRICENCRYPTIONKEYSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTASYMMETRICENCRYPTIONKEYSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['key_id']._loaded_options = None
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['update_mask']._loaded_options = None
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['name']._serialized_options = b'\212\3101\005<=100'
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\006<=1024'
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _globals['_DELETEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['key_id']._loaded_options = None
  _globals['_DELETEASYMMETRICENCRYPTIONKEYREQUEST'].fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTASYMMETRICENCRYPTIONKEYOPERATIONSREQUEST'].fields_by_name['key_id']._loaded_options = None
  _globals['_LISTASYMMETRICENCRYPTIONKEYOPERATIONSREQUEST'].fields_by_name['key_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTASYMMETRICENCRYPTIONKEYOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTASYMMETRICENCRYPTIONKEYOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTASYMMETRICENCRYPTIONKEYOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTASYMMETRICENCRYPTIONKEYOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*@\n%CreateAsymmetricEncryptionKeyMetadata\022\027AsymmetricEncryptionKey\202\323\344\223\002%\" /kms/v1/asymmetricEncryptionKeys:\001*'
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002+\022)/kms/v1/asymmetricEncryptionKeys/{key_id}'
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\"\022 /kms/v1/asymmetricEncryptionKeys'
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*@\n%UpdateAsymmetricEncryptionKeyMetadata\022\027AsymmetricEncryptionKey\202\323\344\223\002.2)/kms/v1/asymmetricEncryptionKeys/{key_id}:\001*'
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*@\n%DeleteAsymmetricEncryptionKeyMetadata\022\027AsymmetricEncryptionKey\202\323\344\223\002+*)/kms/v1/asymmetricEncryptionKeys/{key_id}'
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0026\0224/kms/v1/asymmetricEncryptionKeys/{key_id}/operations'
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002C\022A/kms/v1/asymmetricEncryptionKeys/{resource_id}:listAccessBindings'
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002E\"@/kms/v1/asymmetricEncryptionKeys/{resource_id}:setAccessBindings:\001*'
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002H\"C/kms/v1/asymmetricEncryptionKeys/{resource_id}:updateAccessBindings:\001*'
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST']._serialized_start=404
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST']._serialized_end=882
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST_LABELSENTRY']._serialized_start=837
  _globals['_CREATEASYMMETRICENCRYPTIONKEYREQUEST_LABELSENTRY']._serialized_end=882
  _globals['_CREATEASYMMETRICENCRYPTIONKEYMETADATA']._serialized_start=884
  _globals['_CREATEASYMMETRICENCRYPTIONKEYMETADATA']._serialized_end=939
  _globals['_GETASYMMETRICENCRYPTIONKEYREQUEST']._serialized_start=941
  _globals['_GETASYMMETRICENCRYPTIONKEYREQUEST']._serialized_end=1006
  _globals['_LISTASYMMETRICENCRYPTIONKEYSREQUEST']._serialized_start=1009
  _globals['_LISTASYMMETRICENCRYPTIONKEYSREQUEST']._serialized_end=1141
  _globals['_LISTASYMMETRICENCRYPTIONKEYSRESPONSE']._serialized_start=1144
  _globals['_LISTASYMMETRICENCRYPTIONKEYSRESPONSE']._serialized_end=1288
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST']._serialized_start=1291
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST']._serialized_end=1808
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST_LABELSENTRY']._serialized_start=837
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYREQUEST_LABELSENTRY']._serialized_end=882
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYMETADATA']._serialized_start=1810
  _globals['_UPDATEASYMMETRICENCRYPTIONKEYMETADATA']._serialized_end=1865
  _globals['_DELETEASYMMETRICENCRYPTIONKEYREQUEST']._serialized_start=1867
  _globals['_DELETEASYMMETRICENCRYPTIONKEYREQUEST']._serialized_end=1935
  _globals['_DELETEASYMMETRICENCRYPTIONKEYMETADATA']._serialized_start=1937
  _globals['_DELETEASYMMETRICENCRYPTIONKEYMETADATA']._serialized_end=1992
  _globals['_LISTASYMMETRICENCRYPTIONKEYOPERATIONSREQUEST']._serialized_start=1995
  _globals['_LISTASYMMETRICENCRYPTIONKEYOPERATIONSREQUEST']._serialized_end=2133
  _globals['_LISTASYMMETRICENCRYPTIONKEYOPERATIONSRESPONSE']._serialized_start=2135
  _globals['_LISTASYMMETRICENCRYPTIONKEYOPERATIONSRESPONSE']._serialized_end=2262
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE']._serialized_start=2265
  _globals['_ASYMMETRICENCRYPTIONKEYSERVICE']._serialized_end=4393
# @@protoc_insertion_point(module_scope)
