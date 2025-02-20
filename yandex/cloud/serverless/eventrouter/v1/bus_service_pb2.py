# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/serverless/eventrouter/v1/bus_service.proto
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
    'yandex/cloud/serverless/eventrouter/v1/bus_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.serverless.eventrouter.v1 import bus_pb2 as yandex_dot_cloud_dot_serverless_dot_eventrouter_dot_v1_dot_bus__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8yandex/cloud/serverless/eventrouter/v1/bus_service.proto\x12&yandex.cloud.serverless.eventrouter.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a yandex/cloud/access/access.proto\x1a\x30yandex/cloud/serverless/eventrouter/v1/bus.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"%\n\rGetBusRequest\x12\x14\n\x06\x62us_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"b\n\x10ListBusesRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\"h\n\x11ListBusesResponse\x12:\n\x05\x62uses\x18\x01 \x03(\x0b\x32+.yandex.cloud.serverless.eventrouter.v1.Bus\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xdc\x02\n\x10\x43reateBusRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x91\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x44.yandex.cloud.serverless.eventrouter.v1.CreateBusRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x1b\n\x13\x64\x65letion_protection\x18\x05 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n\x11\x43reateBusMetadata\x12\x0e\n\x06\x62us_id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\"\x8a\x03\n\x10UpdateBusRequest\x12\x14\n\x06\x62us_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x91\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x44.yandex.cloud.serverless.eventrouter.v1.UpdateBusRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x1b\n\x13\x64\x65letion_protection\x18\x06 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\x11UpdateBusMetadata\x12\x14\n\x06\x62us_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"(\n\x10\x44\x65leteBusRequest\x12\x14\n\x06\x62us_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\")\n\x11\x44\x65leteBusMetadata\x12\x14\n\x06\x62us_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x8a\x01\n\x18ListBusOperationsRequest\x12\x14\n\x06\x62us_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"k\n\x19ListBusOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xae\r\n\nBusService\x12\x91\x01\n\x03Get\x12\x35.yandex.cloud.serverless.eventrouter.v1.GetBusRequest\x1a+.yandex.cloud.serverless.eventrouter.v1.Bus\"&\x82\xd3\xe4\x93\x02 \x12\x1e/eventrouter/v1/buses/{bus_id}\x12\x9a\x01\n\x04List\x12\x38.yandex.cloud.serverless.eventrouter.v1.ListBusesRequest\x1a\x39.yandex.cloud.serverless.eventrouter.v1.ListBusesResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/eventrouter/v1/buses\x12\xa3\x01\n\x06\x43reate\x12\x38.yandex.cloud.serverless.eventrouter.v1.CreateBusRequest\x1a!.yandex.cloud.operation.Operation\"<\xb2\xd2*\x18\n\x11\x43reateBusMetadata\x12\x03\x42us\x82\xd3\xe4\x93\x02\x1a\"\x15/eventrouter/v1/buses:\x01*\x12\xac\x01\n\x06Update\x12\x38.yandex.cloud.serverless.eventrouter.v1.UpdateBusRequest\x1a!.yandex.cloud.operation.Operation\"E\xb2\xd2*\x18\n\x11UpdateBusMetadata\x12\x03\x42us\x82\xd3\xe4\x93\x02#2\x1e/eventrouter/v1/buses/{bus_id}:\x01*\x12\xbb\x01\n\x06\x44\x65lete\x12\x38.yandex.cloud.serverless.eventrouter.v1.DeleteBusRequest\x1a!.yandex.cloud.operation.Operation\"T\xb2\xd2**\n\x11\x44\x65leteBusMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02 *\x1e/eventrouter/v1/buses/{bus_id}\x12\xc8\x01\n\x0eListOperations\x12@.yandex.cloud.serverless.eventrouter.v1.ListBusOperationsRequest\x1a\x41.yandex.cloud.serverless.eventrouter.v1.ListBusOperationsResponse\"1\x82\xd3\xe4\x93\x02+\x12)/eventrouter/v1/buses/{bus_id}/operations\x12\xb5\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/eventrouter/v1/buses/{resource_id}:listAccessBindings\x12\xe4\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"}\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02:\"5/eventrouter/v1/buses/{resource_id}:setAccessBindings:\x01*\x12\xf1\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x83\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02=28/eventrouter/v1/buses/{resource_id}:updateAccessBindings:\x01*B\x8b\x01\n*yandex.cloud.api.serverless.eventrouter.v1B\x05PERBSZVgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/eventrouter/v1;eventrouterb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.eventrouter.v1.bus_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*yandex.cloud.api.serverless.eventrouter.v1B\005PERBSZVgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/eventrouter/v1;eventrouter'
  _globals['_GETBUSREQUEST'].fields_by_name['bus_id']._loaded_options = None
  _globals['_GETBUSREQUEST'].fields_by_name['bus_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTBUSESREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTBUSESREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _globals['_CREATEBUSREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEBUSREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEBUSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEBUSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _globals['_CREATEBUSREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEBUSREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_CREATEBUSREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATEBUSREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATEBUSREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATEBUSREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_UPDATEBUSREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEBUSREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEBUSREQUEST'].fields_by_name['bus_id']._loaded_options = None
  _globals['_UPDATEBUSREQUEST'].fields_by_name['bus_id']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEBUSREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEBUSREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_UPDATEBUSREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEBUSREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEBUSREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEBUSREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_UPDATEBUSMETADATA'].fields_by_name['bus_id']._loaded_options = None
  _globals['_UPDATEBUSMETADATA'].fields_by_name['bus_id']._serialized_options = b'\350\3071\001'
  _globals['_DELETEBUSREQUEST'].fields_by_name['bus_id']._loaded_options = None
  _globals['_DELETEBUSREQUEST'].fields_by_name['bus_id']._serialized_options = b'\350\3071\001'
  _globals['_DELETEBUSMETADATA'].fields_by_name['bus_id']._loaded_options = None
  _globals['_DELETEBUSMETADATA'].fields_by_name['bus_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTBUSOPERATIONSREQUEST'].fields_by_name['bus_id']._loaded_options = None
  _globals['_LISTBUSOPERATIONSREQUEST'].fields_by_name['bus_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTBUSOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTBUSOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTBUSOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTBUSOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTBUSOPERATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTBUSOPERATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_BUSSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_BUSSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002 \022\036/eventrouter/v1/buses/{bus_id}'
  _globals['_BUSSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_BUSSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\027\022\025/eventrouter/v1/buses'
  _globals['_BUSSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_BUSSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*\030\n\021CreateBusMetadata\022\003Bus\202\323\344\223\002\032\"\025/eventrouter/v1/buses:\001*'
  _globals['_BUSSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_BUSSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*\030\n\021UpdateBusMetadata\022\003Bus\202\323\344\223\002#2\036/eventrouter/v1/buses/{bus_id}:\001*'
  _globals['_BUSSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_BUSSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322**\n\021DeleteBusMetadata\022\025google.protobuf.Empty\202\323\344\223\002 *\036/eventrouter/v1/buses/{bus_id}'
  _globals['_BUSSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_BUSSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002+\022)/eventrouter/v1/buses/{bus_id}/operations'
  _globals['_BUSSERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_BUSSERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\0028\0226/eventrouter/v1/buses/{resource_id}:listAccessBindings'
  _globals['_BUSSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_BUSSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002:\"5/eventrouter/v1/buses/{resource_id}:setAccessBindings:\001*'
  _globals['_BUSSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_BUSSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002=28/eventrouter/v1/buses/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETBUSREQUEST']._serialized_start=353
  _globals['_GETBUSREQUEST']._serialized_end=390
  _globals['_LISTBUSESREQUEST']._serialized_start=392
  _globals['_LISTBUSESREQUEST']._serialized_end=490
  _globals['_LISTBUSESRESPONSE']._serialized_start=492
  _globals['_LISTBUSESRESPONSE']._serialized_end=596
  _globals['_CREATEBUSREQUEST']._serialized_start=599
  _globals['_CREATEBUSREQUEST']._serialized_end=947
  _globals['_CREATEBUSREQUEST_LABELSENTRY']._serialized_start=902
  _globals['_CREATEBUSREQUEST_LABELSENTRY']._serialized_end=947
  _globals['_CREATEBUSMETADATA']._serialized_start=949
  _globals['_CREATEBUSMETADATA']._serialized_end=1003
  _globals['_UPDATEBUSREQUEST']._serialized_start=1006
  _globals['_UPDATEBUSREQUEST']._serialized_end=1400
  _globals['_UPDATEBUSREQUEST_LABELSENTRY']._serialized_start=902
  _globals['_UPDATEBUSREQUEST_LABELSENTRY']._serialized_end=947
  _globals['_UPDATEBUSMETADATA']._serialized_start=1402
  _globals['_UPDATEBUSMETADATA']._serialized_end=1443
  _globals['_DELETEBUSREQUEST']._serialized_start=1445
  _globals['_DELETEBUSREQUEST']._serialized_end=1485
  _globals['_DELETEBUSMETADATA']._serialized_start=1487
  _globals['_DELETEBUSMETADATA']._serialized_end=1528
  _globals['_LISTBUSOPERATIONSREQUEST']._serialized_start=1531
  _globals['_LISTBUSOPERATIONSREQUEST']._serialized_end=1669
  _globals['_LISTBUSOPERATIONSRESPONSE']._serialized_start=1671
  _globals['_LISTBUSOPERATIONSRESPONSE']._serialized_end=1778
  _globals['_BUSSERVICE']._serialized_start=1781
  _globals['_BUSSERVICE']._serialized_end=3491
# @@protoc_insertion_point(module_scope)
