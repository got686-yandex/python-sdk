# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/serverless/eventrouter/v1/event_service.proto
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
    'yandex/cloud/serverless/eventrouter/v1/event_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/serverless/eventrouter/v1/event_service.proto\x12&yandex.cloud.serverless.eventrouter.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1dyandex/cloud/validation.proto\"G\n\x0fPutEventRequest\x12\x14\n\x06\x62us_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1e\n\x04\x62ody\x18\x02 \x01(\tB\x10\xe8\xc7\x31\x01\x8a\xc8\x31\x08<=262144\"W\n\x11SendEventsRequest\x12\x1a\n\x0c\x63onnector_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12&\n\x07message\x18\x02 \x03(\tB\x15\x82\xc8\x31\x05\x31-100\x8a\xc8\x31\x08<=2621442\xaa\x02\n\x0c\x45ventService\x12\x86\x01\n\x03Put\x12\x37.yandex.cloud.serverless.eventrouter.v1.PutEventRequest\x1a\x16.google.protobuf.Empty\".\x82\xd3\xe4\x93\x02(\"#/eventrouter/v1/events/{bus_id}:put:\x01*\x12\x90\x01\n\x04Send\x12\x39.yandex.cloud.serverless.eventrouter.v1.SendEventsRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02/\"*/eventrouter/v1/events/{connector_id}:send:\x01*B\x8b\x01\n*yandex.cloud.api.serverless.eventrouter.v1B\x05PERESZVgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/eventrouter/v1;eventrouterb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.eventrouter.v1.event_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*yandex.cloud.api.serverless.eventrouter.v1B\005PERESZVgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/eventrouter/v1;eventrouter'
  _globals['_PUTEVENTREQUEST'].fields_by_name['bus_id']._loaded_options = None
  _globals['_PUTEVENTREQUEST'].fields_by_name['bus_id']._serialized_options = b'\350\3071\001'
  _globals['_PUTEVENTREQUEST'].fields_by_name['body']._loaded_options = None
  _globals['_PUTEVENTREQUEST'].fields_by_name['body']._serialized_options = b'\350\3071\001\212\3101\010<=262144'
  _globals['_SENDEVENTSREQUEST'].fields_by_name['connector_id']._loaded_options = None
  _globals['_SENDEVENTSREQUEST'].fields_by_name['connector_id']._serialized_options = b'\350\3071\001'
  _globals['_SENDEVENTSREQUEST'].fields_by_name['message']._loaded_options = None
  _globals['_SENDEVENTSREQUEST'].fields_by_name['message']._serialized_options = b'\202\3101\0051-100\212\3101\010<=262144'
  _globals['_EVENTSERVICE'].methods_by_name['Put']._loaded_options = None
  _globals['_EVENTSERVICE'].methods_by_name['Put']._serialized_options = b'\202\323\344\223\002(\"#/eventrouter/v1/events/{bus_id}:put:\001*'
  _globals['_EVENTSERVICE'].methods_by_name['Send']._loaded_options = None
  _globals['_EVENTSERVICE'].methods_by_name['Send']._serialized_options = b'\202\323\344\223\002/\"*/eventrouter/v1/events/{connector_id}:send:\001*'
  _globals['_PUTEVENTREQUEST']._serialized_start=192
  _globals['_PUTEVENTREQUEST']._serialized_end=263
  _globals['_SENDEVENTSREQUEST']._serialized_start=265
  _globals['_SENDEVENTSREQUEST']._serialized_end=352
  _globals['_EVENTSERVICE']._serialized_start=355
  _globals['_EVENTSERVICE']._serialized_end=653
# @@protoc_insertion_point(module_scope)
