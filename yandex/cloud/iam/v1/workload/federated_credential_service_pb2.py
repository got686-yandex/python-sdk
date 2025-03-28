# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/iam/v1/workload/federated_credential_service.proto
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
    'yandex/cloud/iam/v1/workload/federated_credential_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.iam.v1.workload import federated_credential_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_workload_dot_federated__credential__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?yandex/cloud/iam/v1/workload/federated_credential_service.proto\x12\x1cyandex.cloud.iam.v1.workload\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a\x37yandex/cloud/iam/v1/workload/federated_credential.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"N\n\x1dGetFederatedCredentialRequest\x12-\n\x17\x66\x65\x64\x65rated_credential_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x8a\x01\n\x1fListFederatedCredentialsRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"\x8d\x01\n ListFederatedCredentialsResponse\x12P\n\x15\x66\x65\x64\x65rated_credentials\x18\x01 \x03(\x0b\x32\x31.yandex.cloud.iam.v1.workload.FederatedCredential\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x9c\x01\n CreateFederatedCredentialRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12#\n\rfederation_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12)\n\x13\x65xternal_subject_id\x18\x03 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"D\n!CreateFederatedCredentialMetadata\x12\x1f\n\x17\x66\x65\x64\x65rated_credential_id\x18\x01 \x01(\t\"Q\n DeleteFederatedCredentialRequest\x12-\n\x17\x66\x65\x64\x65rated_credential_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"D\n!DeleteFederatedCredentialMetadata\x12\x1f\n\x17\x66\x65\x64\x65rated_credential_id\x18\x01 \x01(\t2\xe6\x06\n\x1a\x46\x65\x64\x65ratedCredentialService\x12\xbe\x01\n\x03Get\x12;.yandex.cloud.iam.v1.workload.GetFederatedCredentialRequest\x1a\x31.yandex.cloud.iam.v1.workload.FederatedCredential\"G\x82\xd3\xe4\x93\x02\x41\x12?/iam/v1/workload/federatedCredentials/{federated_credential_id}\x12\xb4\x01\n\x04List\x12=.yandex.cloud.iam.v1.workload.ListFederatedCredentialsRequest\x1a>.yandex.cloud.iam.v1.workload.ListFederatedCredentialsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/iam/v1/workload/federatedCredentials\x12\xd9\x01\n\x06\x43reate\x12>.yandex.cloud.iam.v1.workload.CreateFederatedCredentialRequest\x1a!.yandex.cloud.operation.Operation\"l\xb2\xd2*8\n!CreateFederatedCredentialMetadata\x12\x13\x46\x65\x64\x65ratedCredential\x82\xd3\xe4\x93\x02*\"%/iam/v1/workload/federatedCredentials:\x01*\x12\xf3\x01\n\x06\x44\x65lete\x12>.yandex.cloud.iam.v1.workload.DeleteFederatedCredentialRequest\x1a!.yandex.cloud.operation.Operation\"\x85\x01\xb2\xd2*:\n!DeleteFederatedCredentialMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x41*?/iam/v1/workload/federatedCredentials/{federated_credential_id}Bm\n yandex.cloud.api.iam.v1.workloadZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1/workload;workloadb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iam.v1.workload.federated_credential_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n yandex.cloud.api.iam.v1.workloadZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1/workload;workload'
  _globals['_GETFEDERATEDCREDENTIALREQUEST'].fields_by_name['federated_credential_id']._loaded_options = None
  _globals['_GETFEDERATEDCREDENTIALREQUEST'].fields_by_name['federated_credential_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTFEDERATEDCREDENTIALSREQUEST'].fields_by_name['service_account_id']._loaded_options = None
  _globals['_LISTFEDERATEDCREDENTIALSREQUEST'].fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTFEDERATEDCREDENTIALSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTFEDERATEDCREDENTIALSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTFEDERATEDCREDENTIALSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTFEDERATEDCREDENTIALSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _globals['_CREATEFEDERATEDCREDENTIALREQUEST'].fields_by_name['service_account_id']._loaded_options = None
  _globals['_CREATEFEDERATEDCREDENTIALREQUEST'].fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEFEDERATEDCREDENTIALREQUEST'].fields_by_name['federation_id']._loaded_options = None
  _globals['_CREATEFEDERATEDCREDENTIALREQUEST'].fields_by_name['federation_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEFEDERATEDCREDENTIALREQUEST'].fields_by_name['external_subject_id']._loaded_options = None
  _globals['_CREATEFEDERATEDCREDENTIALREQUEST'].fields_by_name['external_subject_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETEFEDERATEDCREDENTIALREQUEST'].fields_by_name['federated_credential_id']._loaded_options = None
  _globals['_DELETEFEDERATEDCREDENTIALREQUEST'].fields_by_name['federated_credential_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_FEDERATEDCREDENTIALSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_FEDERATEDCREDENTIALSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002A\022?/iam/v1/workload/federatedCredentials/{federated_credential_id}'
  _globals['_FEDERATEDCREDENTIALSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_FEDERATEDCREDENTIALSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\'\022%/iam/v1/workload/federatedCredentials'
  _globals['_FEDERATEDCREDENTIALSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_FEDERATEDCREDENTIALSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*8\n!CreateFederatedCredentialMetadata\022\023FederatedCredential\202\323\344\223\002*\"%/iam/v1/workload/federatedCredentials:\001*'
  _globals['_FEDERATEDCREDENTIALSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_FEDERATEDCREDENTIALSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*:\n!DeleteFederatedCredentialMetadata\022\025google.protobuf.Empty\202\323\344\223\002A*?/iam/v1/workload/federatedCredentials/{federated_credential_id}'
  _globals['_GETFEDERATEDCREDENTIALREQUEST']._serialized_start=289
  _globals['_GETFEDERATEDCREDENTIALREQUEST']._serialized_end=367
  _globals['_LISTFEDERATEDCREDENTIALSREQUEST']._serialized_start=370
  _globals['_LISTFEDERATEDCREDENTIALSREQUEST']._serialized_end=508
  _globals['_LISTFEDERATEDCREDENTIALSRESPONSE']._serialized_start=511
  _globals['_LISTFEDERATEDCREDENTIALSRESPONSE']._serialized_end=652
  _globals['_CREATEFEDERATEDCREDENTIALREQUEST']._serialized_start=655
  _globals['_CREATEFEDERATEDCREDENTIALREQUEST']._serialized_end=811
  _globals['_CREATEFEDERATEDCREDENTIALMETADATA']._serialized_start=813
  _globals['_CREATEFEDERATEDCREDENTIALMETADATA']._serialized_end=881
  _globals['_DELETEFEDERATEDCREDENTIALREQUEST']._serialized_start=883
  _globals['_DELETEFEDERATEDCREDENTIALREQUEST']._serialized_end=964
  _globals['_DELETEFEDERATEDCREDENTIALMETADATA']._serialized_start=966
  _globals['_DELETEFEDERATEDCREDENTIALMETADATA']._serialized_end=1034
  _globals['_FEDERATEDCREDENTIALSERVICE']._serialized_start=1037
  _globals['_FEDERATEDCREDENTIALSERVICE']._serialized_end=1907
# @@protoc_insertion_point(module_scope)
