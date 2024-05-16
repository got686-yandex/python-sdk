# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/service_account_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.iam.v1 import service_account_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_service__account__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/iam/v1/service_account_service.proto\x12\x13yandex.cloud.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a)yandex/cloud/iam/v1/service_account.proto\x1a yandex/cloud/access/access.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"D\n\x18GetServiceAccountRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x98\x01\n\x1aListServiceAccountsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"u\n\x1bListServiceAccountsResponse\x12=\n\x10service_accounts\x18\x01 \x03(\x0b\x32#.yandex.cloud.iam.v1.ServiceAccount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xce\x02\n\x1b\x43reateServiceAccountRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x33\n\x04name\x18\x02 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x89\x01\n\x06labels\x18\x04 \x03(\x0b\x32<.yandex.cloud.iam.v1.CreateServiceAccountRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\":\n\x1c\x43reateServiceAccountMetadata\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\"\x88\x03\n\x1bUpdateServiceAccountRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x33\n\x04name\x18\x03 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x89\x01\n\x06labels\x18\x05 \x03(\x0b\x32<.yandex.cloud.iam.v1.UpdateServiceAccountRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\":\n\x1cUpdateServiceAccountMetadata\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\"G\n\x1b\x44\x65leteServiceAccountRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\":\n\x1c\x44\x65leteServiceAccountMetadata\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\"\x8e\x01\n#ListServiceAccountOperationsRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"v\n$ListServiceAccountOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x87\x0e\n\x15ServiceAccountService\x12\x8f\x01\n\x03Get\x12-.yandex.cloud.iam.v1.GetServiceAccountRequest\x1a#.yandex.cloud.iam.v1.ServiceAccount\"4\x82\xd3\xe4\x93\x02.\x12,/iam/v1/serviceAccounts/{service_account_id}\x12\x8a\x01\n\x04List\x12/.yandex.cloud.iam.v1.ListServiceAccountsRequest\x1a\x30.yandex.cloud.iam.v1.ListServiceAccountsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/iam/v1/serviceAccounts\x12\xb3\x01\n\x06\x43reate\x12\x30.yandex.cloud.iam.v1.CreateServiceAccountRequest\x1a!.yandex.cloud.operation.Operation\"T\xb2\xd2*.\n\x1c\x43reateServiceAccountMetadata\x12\x0eServiceAccount\x82\xd3\xe4\x93\x02\x1c\"\x17/iam/v1/serviceAccounts:\x01*\x12\xc8\x01\n\x06Update\x12\x30.yandex.cloud.iam.v1.UpdateServiceAccountRequest\x1a!.yandex.cloud.operation.Operation\"i\xb2\xd2*.\n\x1cUpdateServiceAccountMetadata\x12\x0eServiceAccount\x82\xd3\xe4\x93\x02\x31\x32,/iam/v1/serviceAccounts/{service_account_id}:\x01*\x12\xcc\x01\n\x06\x44\x65lete\x12\x30.yandex.cloud.iam.v1.DeleteServiceAccountRequest\x1a!.yandex.cloud.operation.Operation\"m\xb2\xd2*5\n\x1c\x44\x65leteServiceAccountMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02.*,/iam/v1/serviceAccounts/{service_account_id}\x12\xb7\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/iam/v1/serviceAccounts/{resource_id}:listAccessBindings\x12\xf6\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8e\x01\xb2\xd2*H\n access.SetAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02<\"7/iam/v1/serviceAccounts/{resource_id}:setAccessBindings:\x01*\x12\x82\x02\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x94\x01\xb2\xd2*K\n#access.UpdateAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02?\":/iam/v1/serviceAccounts/{resource_id}:updateAccessBindings:\x01*\x12\xc6\x01\n\x0eListOperations\x12\x38.yandex.cloud.iam.v1.ListServiceAccountOperationsRequest\x1a\x39.yandex.cloud.iam.v1.ListServiceAccountOperationsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/iam/v1/serviceAccounts/{service_account_id}/operationsBV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iam.v1.service_account_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam'
  _GETSERVICEACCOUNTREQUEST.fields_by_name['service_account_id']._options = None
  _GETSERVICEACCOUNTREQUEST.fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSERVICEACCOUNTSREQUEST.fields_by_name['folder_id']._options = None
  _LISTSERVICEACCOUNTSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSERVICEACCOUNTSREQUEST.fields_by_name['page_size']._options = None
  _LISTSERVICEACCOUNTSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTSERVICEACCOUNTSREQUEST.fields_by_name['page_token']._options = None
  _LISTSERVICEACCOUNTSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _LISTSERVICEACCOUNTSREQUEST.fields_by_name['filter']._options = None
  _LISTSERVICEACCOUNTSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _CREATESERVICEACCOUNTREQUEST_LABELSENTRY._options = None
  _CREATESERVICEACCOUNTREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATESERVICEACCOUNTREQUEST.fields_by_name['folder_id']._options = None
  _CREATESERVICEACCOUNTREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATESERVICEACCOUNTREQUEST.fields_by_name['name']._options = None
  _CREATESERVICEACCOUNTREQUEST.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _CREATESERVICEACCOUNTREQUEST.fields_by_name['description']._options = None
  _CREATESERVICEACCOUNTREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATESERVICEACCOUNTREQUEST.fields_by_name['labels']._options = None
  _CREATESERVICEACCOUNTREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _UPDATESERVICEACCOUNTREQUEST_LABELSENTRY._options = None
  _UPDATESERVICEACCOUNTREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATESERVICEACCOUNTREQUEST.fields_by_name['service_account_id']._options = None
  _UPDATESERVICEACCOUNTREQUEST.fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATESERVICEACCOUNTREQUEST.fields_by_name['name']._options = None
  _UPDATESERVICEACCOUNTREQUEST.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _UPDATESERVICEACCOUNTREQUEST.fields_by_name['description']._options = None
  _UPDATESERVICEACCOUNTREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATESERVICEACCOUNTREQUEST.fields_by_name['labels']._options = None
  _UPDATESERVICEACCOUNTREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _DELETESERVICEACCOUNTREQUEST.fields_by_name['service_account_id']._options = None
  _DELETESERVICEACCOUNTREQUEST.fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSERVICEACCOUNTOPERATIONSREQUEST.fields_by_name['service_account_id']._options = None
  _LISTSERVICEACCOUNTOPERATIONSREQUEST.fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSERVICEACCOUNTOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTSERVICEACCOUNTOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTSERVICEACCOUNTOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTSERVICEACCOUNTOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _SERVICEACCOUNTSERVICE.methods_by_name['Get']._options = None
  _SERVICEACCOUNTSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002.\022,/iam/v1/serviceAccounts/{service_account_id}'
  _SERVICEACCOUNTSERVICE.methods_by_name['List']._options = None
  _SERVICEACCOUNTSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\031\022\027/iam/v1/serviceAccounts'
  _SERVICEACCOUNTSERVICE.methods_by_name['Create']._options = None
  _SERVICEACCOUNTSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*.\n\034CreateServiceAccountMetadata\022\016ServiceAccount\202\323\344\223\002\034\"\027/iam/v1/serviceAccounts:\001*'
  _SERVICEACCOUNTSERVICE.methods_by_name['Update']._options = None
  _SERVICEACCOUNTSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*.\n\034UpdateServiceAccountMetadata\022\016ServiceAccount\202\323\344\223\00212,/iam/v1/serviceAccounts/{service_account_id}:\001*'
  _SERVICEACCOUNTSERVICE.methods_by_name['Delete']._options = None
  _SERVICEACCOUNTSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*5\n\034DeleteServiceAccountMetadata\022\025google.protobuf.Empty\202\323\344\223\002.*,/iam/v1/serviceAccounts/{service_account_id}'
  _SERVICEACCOUNTSERVICE.methods_by_name['ListAccessBindings']._options = None
  _SERVICEACCOUNTSERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002:\0228/iam/v1/serviceAccounts/{resource_id}:listAccessBindings'
  _SERVICEACCOUNTSERVICE.methods_by_name['SetAccessBindings']._options = None
  _SERVICEACCOUNTSERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*H\n access.SetAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002<\"7/iam/v1/serviceAccounts/{resource_id}:setAccessBindings:\001*'
  _SERVICEACCOUNTSERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _SERVICEACCOUNTSERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*K\n#access.UpdateAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002?\":/iam/v1/serviceAccounts/{resource_id}:updateAccessBindings:\001*'
  _SERVICEACCOUNTSERVICE.methods_by_name['ListOperations']._options = None
  _SERVICEACCOUNTSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0029\0227/iam/v1/serviceAccounts/{service_account_id}/operations'
  _globals['_GETSERVICEACCOUNTREQUEST']._serialized_start=320
  _globals['_GETSERVICEACCOUNTREQUEST']._serialized_end=388
  _globals['_LISTSERVICEACCOUNTSREQUEST']._serialized_start=391
  _globals['_LISTSERVICEACCOUNTSREQUEST']._serialized_end=543
  _globals['_LISTSERVICEACCOUNTSRESPONSE']._serialized_start=545
  _globals['_LISTSERVICEACCOUNTSRESPONSE']._serialized_end=662
  _globals['_CREATESERVICEACCOUNTREQUEST']._serialized_start=665
  _globals['_CREATESERVICEACCOUNTREQUEST']._serialized_end=999
  _globals['_CREATESERVICEACCOUNTREQUEST_LABELSENTRY']._serialized_start=954
  _globals['_CREATESERVICEACCOUNTREQUEST_LABELSENTRY']._serialized_end=999
  _globals['_CREATESERVICEACCOUNTMETADATA']._serialized_start=1001
  _globals['_CREATESERVICEACCOUNTMETADATA']._serialized_end=1059
  _globals['_UPDATESERVICEACCOUNTREQUEST']._serialized_start=1062
  _globals['_UPDATESERVICEACCOUNTREQUEST']._serialized_end=1454
  _globals['_UPDATESERVICEACCOUNTREQUEST_LABELSENTRY']._serialized_start=954
  _globals['_UPDATESERVICEACCOUNTREQUEST_LABELSENTRY']._serialized_end=999
  _globals['_UPDATESERVICEACCOUNTMETADATA']._serialized_start=1456
  _globals['_UPDATESERVICEACCOUNTMETADATA']._serialized_end=1514
  _globals['_DELETESERVICEACCOUNTREQUEST']._serialized_start=1516
  _globals['_DELETESERVICEACCOUNTREQUEST']._serialized_end=1587
  _globals['_DELETESERVICEACCOUNTMETADATA']._serialized_start=1589
  _globals['_DELETESERVICEACCOUNTMETADATA']._serialized_end=1647
  _globals['_LISTSERVICEACCOUNTOPERATIONSREQUEST']._serialized_start=1650
  _globals['_LISTSERVICEACCOUNTOPERATIONSREQUEST']._serialized_end=1792
  _globals['_LISTSERVICEACCOUNTOPERATIONSRESPONSE']._serialized_start=1794
  _globals['_LISTSERVICEACCOUNTOPERATIONSRESPONSE']._serialized_end=1912
  _globals['_SERVICEACCOUNTSERVICE']._serialized_start=1915
  _globals['_SERVICEACCOUNTSERVICE']._serialized_end=3714
# @@protoc_insertion_point(module_scope)
