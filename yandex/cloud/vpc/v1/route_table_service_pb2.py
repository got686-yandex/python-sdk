# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/vpc/v1/route_table_service.proto
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
    'yandex/cloud/vpc/v1/route_table_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.vpc.v1 import route_table_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/vpc/v1/route_table_service.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a%yandex/cloud/vpc/v1/route_table.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"<\n\x14GetRouteTableRequest\x12$\n\x0eroute_table_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x93\x01\n\x16ListRouteTablesRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"i\n\x17ListRouteTablesResponse\x12\x35\n\x0croute_tables\x18\x01 \x03(\x0b\x32\x1f.yandex.cloud.vpc.v1.RouteTable\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xaa\x03\n\x17\x43reateRouteTableRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12<\n\x04name\x18\x02 \x01(\tB.\xf2\xc7\x31*|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x85\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x38.yandex.cloud.vpc.v1.CreateRouteTableRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12 \n\nnetwork_id\x18\x05 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x37\n\rstatic_routes\x18\x06 \x03(\x0b\x32 .yandex.cloud.vpc.v1.StaticRoute\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"2\n\x18\x43reateRouteTableMetadata\x12\x16\n\x0eroute_table_id\x18\x01 \x01(\t\"\xbe\x03\n\x17UpdateRouteTableRequest\x12$\n\x0eroute_table_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12<\n\x04name\x18\x03 \x01(\tB.\xf2\xc7\x31*|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x85\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x38.yandex.cloud.vpc.v1.UpdateRouteTableRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x37\n\rstatic_routes\x18\x06 \x03(\x0b\x32 .yandex.cloud.vpc.v1.StaticRoute\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"2\n\x18UpdateRouteTableMetadata\x12\x16\n\x0eroute_table_id\x18\x01 \x01(\t\"?\n\x17\x44\x65leteRouteTableRequest\x12$\n\x0eroute_table_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"2\n\x18\x44\x65leteRouteTableMetadata\x12\x16\n\x0eroute_table_id\x18\x01 \x01(\t\"\x85\x01\n\x1fListRouteTableOperationsRequest\x12$\n\x0eroute_table_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"r\n ListRouteTableOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"j\n\x15MoveRouteTableRequest\x12$\n\x0eroute_table_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12+\n\x15\x64\x65stination_folder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"0\n\x16MoveRouteTableMetadata\x12\x16\n\x0eroute_table_id\x18\x01 \x01(\t2\x9f\t\n\x11RouteTableService\x12\x7f\n\x03Get\x12).yandex.cloud.vpc.v1.GetRouteTableRequest\x1a\x1f.yandex.cloud.vpc.v1.RouteTable\",\x82\xd3\xe4\x93\x02&\x12$/vpc/v1/routeTables/{route_table_id}\x12~\n\x04List\x12+.yandex.cloud.vpc.v1.ListRouteTablesRequest\x1a,.yandex.cloud.vpc.v1.ListRouteTablesResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/vpc/v1/routeTables\x12\xa3\x01\n\x06\x43reate\x12,.yandex.cloud.vpc.v1.CreateRouteTableRequest\x1a!.yandex.cloud.operation.Operation\"H\xb2\xd2*&\n\x18\x43reateRouteTableMetadata\x12\nRouteTable\x82\xd3\xe4\x93\x02\x18\"\x13/vpc/v1/routeTables:\x01*\x12\xb4\x01\n\x06Update\x12,.yandex.cloud.vpc.v1.UpdateRouteTableRequest\x1a!.yandex.cloud.operation.Operation\"Y\xb2\xd2*&\n\x18UpdateRouteTableMetadata\x12\nRouteTable\x82\xd3\xe4\x93\x02)2$/vpc/v1/routeTables/{route_table_id}:\x01*\x12\xbc\x01\n\x06\x44\x65lete\x12,.yandex.cloud.vpc.v1.DeleteRouteTableRequest\x1a!.yandex.cloud.operation.Operation\"a\xb2\xd2*1\n\x18\x44\x65leteRouteTableMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02&*$/vpc/v1/routeTables/{route_table_id}\x12\xb6\x01\n\x0eListOperations\x12\x34.yandex.cloud.vpc.v1.ListRouteTableOperationsRequest\x1a\x35.yandex.cloud.vpc.v1.ListRouteTableOperationsResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//vpc/v1/routeTables/{route_table_id}/operations\x12\xb3\x01\n\x04Move\x12*.yandex.cloud.vpc.v1.MoveRouteTableRequest\x1a!.yandex.cloud.operation.Operation\"\\\xb2\xd2*$\n\x16MoveRouteTableMetadata\x12\nRouteTable\x82\xd3\xe4\x93\x02.\")/vpc/v1/routeTables/{route_table_id}:move:\x01*BV\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.vpc.v1.route_table_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc'
  _globals['_GETROUTETABLEREQUEST'].fields_by_name['route_table_id']._loaded_options = None
  _globals['_GETROUTETABLEREQUEST'].fields_by_name['route_table_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTROUTETABLESREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTROUTETABLESREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTROUTETABLESREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTROUTETABLESREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTROUTETABLESREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTROUTETABLESREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTROUTETABLESREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTROUTETABLESREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATEROUTETABLEREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEROUTETABLEREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEROUTETABLEREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEROUTETABLEREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEROUTETABLEREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEROUTETABLEREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071*|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?'
  _globals['_CREATEROUTETABLEREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATEROUTETABLEREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATEROUTETABLEREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATEROUTETABLEREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_CREATEROUTETABLEREQUEST'].fields_by_name['network_id']._loaded_options = None
  _globals['_CREATEROUTETABLEREQUEST'].fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEROUTETABLEREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEROUTETABLEREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEROUTETABLEREQUEST'].fields_by_name['route_table_id']._loaded_options = None
  _globals['_UPDATEROUTETABLEREQUEST'].fields_by_name['route_table_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEROUTETABLEREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEROUTETABLEREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071*|[a-zA-Z]([-_a-zA-Z0-9]{0,61}[a-zA-Z0-9])?'
  _globals['_UPDATEROUTETABLEREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEROUTETABLEREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEROUTETABLEREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEROUTETABLEREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_DELETEROUTETABLEREQUEST'].fields_by_name['route_table_id']._loaded_options = None
  _globals['_DELETEROUTETABLEREQUEST'].fields_by_name['route_table_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTROUTETABLEOPERATIONSREQUEST'].fields_by_name['route_table_id']._loaded_options = None
  _globals['_LISTROUTETABLEOPERATIONSREQUEST'].fields_by_name['route_table_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTROUTETABLEOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTROUTETABLEOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTROUTETABLEOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTROUTETABLEOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_MOVEROUTETABLEREQUEST'].fields_by_name['route_table_id']._loaded_options = None
  _globals['_MOVEROUTETABLEREQUEST'].fields_by_name['route_table_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_MOVEROUTETABLEREQUEST'].fields_by_name['destination_folder_id']._loaded_options = None
  _globals['_MOVEROUTETABLEREQUEST'].fields_by_name['destination_folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ROUTETABLESERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_ROUTETABLESERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002&\022$/vpc/v1/routeTables/{route_table_id}'
  _globals['_ROUTETABLESERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_ROUTETABLESERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\025\022\023/vpc/v1/routeTables'
  _globals['_ROUTETABLESERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_ROUTETABLESERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*&\n\030CreateRouteTableMetadata\022\nRouteTable\202\323\344\223\002\030\"\023/vpc/v1/routeTables:\001*'
  _globals['_ROUTETABLESERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_ROUTETABLESERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*&\n\030UpdateRouteTableMetadata\022\nRouteTable\202\323\344\223\002)2$/vpc/v1/routeTables/{route_table_id}:\001*'
  _globals['_ROUTETABLESERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_ROUTETABLESERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*1\n\030DeleteRouteTableMetadata\022\025google.protobuf.Empty\202\323\344\223\002&*$/vpc/v1/routeTables/{route_table_id}'
  _globals['_ROUTETABLESERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_ROUTETABLESERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0021\022//vpc/v1/routeTables/{route_table_id}/operations'
  _globals['_ROUTETABLESERVICE'].methods_by_name['Move']._loaded_options = None
  _globals['_ROUTETABLESERVICE'].methods_by_name['Move']._serialized_options = b'\262\322*$\n\026MoveRouteTableMetadata\022\nRouteTable\202\323\344\223\002.\")/vpc/v1/routeTables/{route_table_id}:move:\001*'
  _globals['_GETROUTETABLEREQUEST']._serialized_start=278
  _globals['_GETROUTETABLEREQUEST']._serialized_end=338
  _globals['_LISTROUTETABLESREQUEST']._serialized_start=341
  _globals['_LISTROUTETABLESREQUEST']._serialized_end=488
  _globals['_LISTROUTETABLESRESPONSE']._serialized_start=490
  _globals['_LISTROUTETABLESRESPONSE']._serialized_end=595
  _globals['_CREATEROUTETABLEREQUEST']._serialized_start=598
  _globals['_CREATEROUTETABLEREQUEST']._serialized_end=1024
  _globals['_CREATEROUTETABLEREQUEST_LABELSENTRY']._serialized_start=979
  _globals['_CREATEROUTETABLEREQUEST_LABELSENTRY']._serialized_end=1024
  _globals['_CREATEROUTETABLEMETADATA']._serialized_start=1026
  _globals['_CREATEROUTETABLEMETADATA']._serialized_end=1076
  _globals['_UPDATEROUTETABLEREQUEST']._serialized_start=1079
  _globals['_UPDATEROUTETABLEREQUEST']._serialized_end=1525
  _globals['_UPDATEROUTETABLEREQUEST_LABELSENTRY']._serialized_start=979
  _globals['_UPDATEROUTETABLEREQUEST_LABELSENTRY']._serialized_end=1024
  _globals['_UPDATEROUTETABLEMETADATA']._serialized_start=1527
  _globals['_UPDATEROUTETABLEMETADATA']._serialized_end=1577
  _globals['_DELETEROUTETABLEREQUEST']._serialized_start=1579
  _globals['_DELETEROUTETABLEREQUEST']._serialized_end=1642
  _globals['_DELETEROUTETABLEMETADATA']._serialized_start=1644
  _globals['_DELETEROUTETABLEMETADATA']._serialized_end=1694
  _globals['_LISTROUTETABLEOPERATIONSREQUEST']._serialized_start=1697
  _globals['_LISTROUTETABLEOPERATIONSREQUEST']._serialized_end=1830
  _globals['_LISTROUTETABLEOPERATIONSRESPONSE']._serialized_start=1832
  _globals['_LISTROUTETABLEOPERATIONSRESPONSE']._serialized_end=1946
  _globals['_MOVEROUTETABLEREQUEST']._serialized_start=1948
  _globals['_MOVEROUTETABLEREQUEST']._serialized_end=2054
  _globals['_MOVEROUTETABLEMETADATA']._serialized_start=2056
  _globals['_MOVEROUTETABLEMETADATA']._serialized_end=2104
  _globals['_ROUTETABLESERVICE']._serialized_start=2107
  _globals['_ROUTETABLESERVICE']._serialized_end=3290
# @@protoc_insertion_point(module_scope)
