# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/speechsense/v1/classifiers_service.proto
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
    'yandex/cloud/speechsense/v1/classifiers_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.speechsense.v1 import classifier_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_classifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/speechsense/v1/classifiers_service.proto\x12\x1byandex.cloud.speechsense.v1\x1a\x1cgoogle/api/annotations.proto\x1a,yandex/cloud/speechsense/v1/classifier.proto\",\n\x16ListClassifiersRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\"W\n\x17ListClassifiersResponse\x12<\n\x0b\x63lassifiers\x18\x01 \x03(\x0b\x32\'.yandex.cloud.speechsense.v1.Classifier2\xb5\x01\n\x12\x43lassifiersService\x12\x9e\x01\n\x04List\x12\x33.yandex.cloud.speechsense.v1.ListClassifiersRequest\x1a\x34.yandex.cloud.speechsense.v1.ListClassifiersResponse\"+\x82\xd3\xe4\x93\x02%\" /speechsense/v1/classifiers/list:\x01*B\x87\x01\n\x1fyandex.cloud.api.speechsense.v1B\x17\x43lassifiersServiceProtoZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1;speechsenseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.speechsense.v1.classifiers_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037yandex.cloud.api.speechsense.v1B\027ClassifiersServiceProtoZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1;speechsense'
  _globals['_CLASSIFIERSSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_CLASSIFIERSSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002%\" /speechsense/v1/classifiers/list:\001*'
  _globals['_LISTCLASSIFIERSREQUEST']._serialized_start=162
  _globals['_LISTCLASSIFIERSREQUEST']._serialized_end=206
  _globals['_LISTCLASSIFIERSRESPONSE']._serialized_start=208
  _globals['_LISTCLASSIFIERSRESPONSE']._serialized_end=295
  _globals['_CLASSIFIERSSERVICE']._serialized_start=298
  _globals['_CLASSIFIERSSERVICE']._serialized_end=479
# @@protoc_insertion_point(module_scope)
