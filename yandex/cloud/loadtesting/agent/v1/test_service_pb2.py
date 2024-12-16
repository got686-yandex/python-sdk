# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/loadtesting/agent/v1/test_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'yandex/cloud/loadtesting/agent/v1/test_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.loadtesting.agent.v1 import test_pb2 as yandex_dot_cloud_dot_loadtesting_dot_agent_dot_v1_dot_test__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4yandex/cloud/loadtesting/agent/v1/test_service.proto\x12!yandex.cloud.loadtesting.agent.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1dyandex/cloud/validation.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a,yandex/cloud/loadtesting/agent/v1/test.proto\"/\n\x0eGetTestRequest\x12\x1d\n\x07test_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x8f\x03\n\x11UpdateTestRequest\x12\x1d\n\x07test_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x10\n\x04name\x18\x03 \x01(\tB\x02\x18\x01\x12\x17\n\x0b\x64\x65scription\x18\x04 \x01(\tB\x02\x18\x01\x12T\n\x06labels\x18\x05 \x03(\x0b\x32@.yandex.cloud.loadtesting.agent.v1.UpdateTestRequest.LabelsEntryB\x02\x18\x01\x12\x14\n\x08\x66\x61vorite\x18\x06 \x01(\x08\x42\x02\x18\x01\x12\x1a\n\x0etarget_version\x18\x07 \x01(\tB\x02\x18\x01\x12\x17\n\x0fimbalance_point\x18\x08 \x01(\x03\x12\x14\n\x0cimbalance_ts\x18\t \x01(\x03\x12\x19\n\x11imbalance_comment\x18\n \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"%\n\x12UpdateTestMetadata\x12\x0f\n\x07test_id\x18\x01 \x01(\t2\xd4\x02\n\x0bTestService\x12\x90\x01\n\x03Get\x12\x31.yandex.cloud.loadtesting.agent.v1.GetTestRequest\x1a\'.yandex.cloud.loadtesting.agent.v1.Test\"-\x82\xd3\xe4\x93\x02\'\x12%/loadtesting/agent/v1/tests/{test_id}\x12\xb1\x01\n\x06Update\x12\x34.yandex.cloud.loadtesting.agent.v1.UpdateTestRequest\x1a!.yandex.cloud.operation.Operation\"N\xb2\xd2*\x1a\n\x12UpdateTestMetadata\x12\x04Test\x82\xd3\xe4\x93\x02*2%/loadtesting/agent/v1/tests/{test_id}:\x01*Bt\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.loadtesting.agent.v1.test_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agent'
  _globals['_GETTESTREQUEST'].fields_by_name['test_id']._loaded_options = None
  _globals['_GETTESTREQUEST'].fields_by_name['test_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATETESTREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATETESTREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATETESTREQUEST'].fields_by_name['test_id']._loaded_options = None
  _globals['_UPDATETESTREQUEST'].fields_by_name['test_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATETESTREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATETESTREQUEST'].fields_by_name['name']._serialized_options = b'\030\001'
  _globals['_UPDATETESTREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATETESTREQUEST'].fields_by_name['description']._serialized_options = b'\030\001'
  _globals['_UPDATETESTREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATETESTREQUEST'].fields_by_name['labels']._serialized_options = b'\030\001'
  _globals['_UPDATETESTREQUEST'].fields_by_name['favorite']._loaded_options = None
  _globals['_UPDATETESTREQUEST'].fields_by_name['favorite']._serialized_options = b'\030\001'
  _globals['_UPDATETESTREQUEST'].fields_by_name['target_version']._loaded_options = None
  _globals['_UPDATETESTREQUEST'].fields_by_name['target_version']._serialized_options = b'\030\001'
  _globals['_TESTSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_TESTSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\'\022%/loadtesting/agent/v1/tests/{test_id}'
  _globals['_TESTSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_TESTSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*\032\n\022UpdateTestMetadata\022\004Test\202\323\344\223\002*2%/loadtesting/agent/v1/tests/{test_id}:\001*'
  _globals['_GETTESTREQUEST']._serialized_start=306
  _globals['_GETTESTREQUEST']._serialized_end=353
  _globals['_UPDATETESTREQUEST']._serialized_start=356
  _globals['_UPDATETESTREQUEST']._serialized_end=755
  _globals['_UPDATETESTREQUEST_LABELSENTRY']._serialized_start=710
  _globals['_UPDATETESTREQUEST_LABELSENTRY']._serialized_end=755
  _globals['_UPDATETESTMETADATA']._serialized_start=757
  _globals['_UPDATETESTMETADATA']._serialized_end=794
  _globals['_TESTSERVICE']._serialized_start=797
  _globals['_TESTSERVICE']._serialized_end=1137
# @@protoc_insertion_point(module_scope)
