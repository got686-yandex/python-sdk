# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/marketplace/licensemanager/saas/v1/lock_service.proto
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
    'yandex/cloud/marketplace/licensemanager/saas/v1/lock_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.marketplace.licensemanager.v1 import lock_pb2 as yandex_dot_cloud_dot_marketplace_dot_licensemanager_dot_v1_dot_lock__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nByandex/cloud/marketplace/licensemanager/saas/v1/lock_service.proto\x12/yandex.cloud.marketplace.licensemanager.saas.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a\x35yandex/cloud/marketplace/licensemanager/v1/lock.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"L\n\x11\x45nsureLockRequest\x12\x1c\n\x0einstance_token\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x19\n\x0bresource_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"%\n\x12\x45nsureLockMetadata\x12\x0f\n\x07lock_id\x18\x01 \x01(\t\"\'\n\x0eGetLockRequest\x12\x15\n\x07lock_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x32\xa6\x03\n\x0bLockService\x12\xdd\x01\n\x06\x45nsure\x12\x42.yandex.cloud.marketplace.licensemanager.saas.v1.EnsureLockRequest\x1a!.yandex.cloud.operation.Operation\"l\xb2\xd2*,\n\x12\x45nsureLockMetadata\x12\x16licensemanager.v1.Lock\x82\xd3\xe4\x93\x02\x36\"1/marketplace/license-manager/saas/v1/locks/ensure:\x01*\x12\xb6\x01\n\x03Get\x12?.yandex.cloud.marketplace.licensemanager.saas.v1.GetLockRequest\x1a\x30.yandex.cloud.marketplace.licensemanager.v1.Lock\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/marketplace/license-manager/saas/v1/locks/{lock_id}B\x99\x01\n3yandex.cloud.api.marketplace.licensemanager.saas.v1Zbgithub.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/licensemanager/saas/v1;licensemanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.marketplace.licensemanager.saas.v1.lock_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n3yandex.cloud.api.marketplace.licensemanager.saas.v1Zbgithub.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/licensemanager/saas/v1;licensemanager'
  _globals['_ENSURELOCKREQUEST'].fields_by_name['instance_token']._loaded_options = None
  _globals['_ENSURELOCKREQUEST'].fields_by_name['instance_token']._serialized_options = b'\350\3071\001'
  _globals['_ENSURELOCKREQUEST'].fields_by_name['resource_id']._loaded_options = None
  _globals['_ENSURELOCKREQUEST'].fields_by_name['resource_id']._serialized_options = b'\350\3071\001'
  _globals['_GETLOCKREQUEST'].fields_by_name['lock_id']._loaded_options = None
  _globals['_GETLOCKREQUEST'].fields_by_name['lock_id']._serialized_options = b'\350\3071\001'
  _globals['_LOCKSERVICE'].methods_by_name['Ensure']._loaded_options = None
  _globals['_LOCKSERVICE'].methods_by_name['Ensure']._serialized_options = b'\262\322*,\n\022EnsureLockMetadata\022\026licensemanager.v1.Lock\202\323\344\223\0026\"1/marketplace/license-manager/saas/v1/locks/ensure:\001*'
  _globals['_LOCKSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_LOCKSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\0026\0224/marketplace/license-manager/saas/v1/locks/{lock_id}'
  _globals['_ENSURELOCKREQUEST']._serialized_start=309
  _globals['_ENSURELOCKREQUEST']._serialized_end=385
  _globals['_ENSURELOCKMETADATA']._serialized_start=387
  _globals['_ENSURELOCKMETADATA']._serialized_end=424
  _globals['_GETLOCKREQUEST']._serialized_start=426
  _globals['_GETLOCKREQUEST']._serialized_end=465
  _globals['_LOCKSERVICE']._serialized_start=468
  _globals['_LOCKSERVICE']._serialized_end=890
# @@protoc_insertion_point(module_scope)
