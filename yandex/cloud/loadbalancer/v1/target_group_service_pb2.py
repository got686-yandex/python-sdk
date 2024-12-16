# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/loadbalancer/v1/target_group_service.proto
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
    'yandex/cloud/loadbalancer/v1/target_group_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.loadbalancer.v1 import target_group_pb2 as yandex_dot_cloud_dot_loadbalancer_dot_v1_dot_target__group__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7yandex/cloud/loadbalancer/v1/target_group_service.proto\x12\x1cyandex.cloud.loadbalancer.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a/yandex/cloud/loadbalancer/v1/target_group.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\">\n\x15GetTargetGroupRequest\x12%\n\x0ftarget_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x94\x01\n\x17ListTargetGroupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"u\n\x18ListTargetGroupsResponse\x12@\n\rtarget_groups\x18\x01 \x03(\x0b\x32).yandex.cloud.loadbalancer.v1.TargetGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa7\x03\n\x18\x43reateTargetGroupRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8f\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x42.yandex.cloud.loadbalancer.v1.CreateTargetGroupRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x1b\n\tregion_id\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x35\n\x07targets\x18\x07 \x03(\x0b\x32$.yandex.cloud.loadbalancer.v1.Target\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x06\x10\x07\"4\n\x19\x43reateTargetGroupMetadata\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\"\xbb\x03\n\x18UpdateTargetGroupRequest\x12%\n\x0ftarget_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8f\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x42.yandex.cloud.loadbalancer.v1.UpdateTargetGroupRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x35\n\x07targets\x18\x06 \x03(\x0b\x32$.yandex.cloud.loadbalancer.v1.Target\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\x19UpdateTargetGroupMetadata\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\"A\n\x18\x44\x65leteTargetGroupRequest\x12%\n\x0ftarget_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"4\n\x19\x44\x65leteTargetGroupMetadata\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\"z\n\x11\x41\x64\x64TargetsRequest\x12%\n\x0ftarget_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12>\n\x07targets\x18\x02 \x03(\x0b\x32$.yandex.cloud.loadbalancer.v1.TargetB\x07\x82\xc8\x31\x03>=1\"-\n\x12\x41\x64\x64TargetsMetadata\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\"}\n\x14RemoveTargetsRequest\x12%\n\x0ftarget_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12>\n\x07targets\x18\x02 \x03(\x0b\x32$.yandex.cloud.loadbalancer.v1.TargetB\x07\x82\xc8\x31\x03>=1\"0\n\x15RemoveTargetsMetadata\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\"\x87\x01\n ListTargetGroupOperationsRequest\x12%\n\x0ftarget_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"s\n!ListTargetGroupOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xbd\x0c\n\x12TargetGroupService\x12\x9f\x01\n\x03Get\x12\x33.yandex.cloud.loadbalancer.v1.GetTargetGroupRequest\x1a).yandex.cloud.loadbalancer.v1.TargetGroup\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/load-balancer/v1/targetGroups/{target_group_id}\x12\x9d\x01\n\x04List\x12\x35.yandex.cloud.loadbalancer.v1.ListTargetGroupsRequest\x1a\x36.yandex.cloud.loadbalancer.v1.ListTargetGroupsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/load-balancer/v1/targetGroups\x12\xba\x01\n\x06\x43reate\x12\x36.yandex.cloud.loadbalancer.v1.CreateTargetGroupRequest\x1a!.yandex.cloud.operation.Operation\"U\xb2\xd2*(\n\x19\x43reateTargetGroupMetadata\x12\x0bTargetGroup\x82\xd3\xe4\x93\x02#\"\x1e/load-balancer/v1/targetGroups:\x01*\x12\xcc\x01\n\x06Update\x12\x36.yandex.cloud.loadbalancer.v1.UpdateTargetGroupRequest\x1a!.yandex.cloud.operation.Operation\"g\xb2\xd2*(\n\x19UpdateTargetGroupMetadata\x12\x0bTargetGroup\x82\xd3\xe4\x93\x02\x35\x32\x30/load-balancer/v1/targetGroups/{target_group_id}:\x01*\x12\xd3\x01\n\x06\x44\x65lete\x12\x36.yandex.cloud.loadbalancer.v1.DeleteTargetGroupRequest\x1a!.yandex.cloud.operation.Operation\"n\xb2\xd2*2\n\x19\x44\x65leteTargetGroupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x32*0/load-balancer/v1/targetGroups/{target_group_id}\x12\xcd\x01\n\nAddTargets\x12/.yandex.cloud.loadbalancer.v1.AddTargetsRequest\x1a!.yandex.cloud.operation.Operation\"k\xb2\xd2*!\n\x12\x41\x64\x64TargetsMetadata\x12\x0bTargetGroup\x82\xd3\xe4\x93\x02@\";/load-balancer/v1/targetGroups/{target_group_id}:addTargets:\x01*\x12\xd9\x01\n\rRemoveTargets\x12\x32.yandex.cloud.loadbalancer.v1.RemoveTargetsRequest\x1a!.yandex.cloud.operation.Operation\"q\xb2\xd2*$\n\x15RemoveTargetsMetadata\x12\x0bTargetGroup\x82\xd3\xe4\x93\x02\x43\">/load-balancer/v1/targetGroups/{target_group_id}:removeTargets:\x01*\x12\xd6\x01\n\x0eListOperations\x12>.yandex.cloud.loadbalancer.v1.ListTargetGroupOperationsRequest\x1a?.yandex.cloud.loadbalancer.v1.ListTargetGroupOperationsResponse\"C\x82\xd3\xe4\x93\x02=\x12;/load-balancer/v1/targetGroups/{target_group_id}/operationsBq\n yandex.cloud.api.loadbalancer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1;loadbalancerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.loadbalancer.v1.target_group_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n yandex.cloud.api.loadbalancer.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1;loadbalancer'
  _globals['_GETTARGETGROUPREQUEST'].fields_by_name['target_group_id']._loaded_options = None
  _globals['_GETTARGETGROUPREQUEST'].fields_by_name['target_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTTARGETGROUPSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTTARGETGROUPSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTTARGETGROUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTTARGETGROUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTTARGETGROUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTTARGETGROUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTTARGETGROUPSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTTARGETGROUPSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATETARGETGROUPREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATETARGETGROUPREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATETARGETGROUPREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATETARGETGROUPREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATETARGETGROUPREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATETARGETGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_CREATETARGETGROUPREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATETARGETGROUPREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATETARGETGROUPREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATETARGETGROUPREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_CREATETARGETGROUPREQUEST'].fields_by_name['region_id']._loaded_options = None
  _globals['_CREATETARGETGROUPREQUEST'].fields_by_name['region_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_UPDATETARGETGROUPREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATETARGETGROUPREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATETARGETGROUPREQUEST'].fields_by_name['target_group_id']._loaded_options = None
  _globals['_UPDATETARGETGROUPREQUEST'].fields_by_name['target_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATETARGETGROUPREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATETARGETGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_UPDATETARGETGROUPREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATETARGETGROUPREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATETARGETGROUPREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATETARGETGROUPREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_DELETETARGETGROUPREQUEST'].fields_by_name['target_group_id']._loaded_options = None
  _globals['_DELETETARGETGROUPREQUEST'].fields_by_name['target_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ADDTARGETSREQUEST'].fields_by_name['target_group_id']._loaded_options = None
  _globals['_ADDTARGETSREQUEST'].fields_by_name['target_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ADDTARGETSREQUEST'].fields_by_name['targets']._loaded_options = None
  _globals['_ADDTARGETSREQUEST'].fields_by_name['targets']._serialized_options = b'\202\3101\003>=1'
  _globals['_REMOVETARGETSREQUEST'].fields_by_name['target_group_id']._loaded_options = None
  _globals['_REMOVETARGETSREQUEST'].fields_by_name['target_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_REMOVETARGETSREQUEST'].fields_by_name['targets']._loaded_options = None
  _globals['_REMOVETARGETSREQUEST'].fields_by_name['targets']._serialized_options = b'\202\3101\003>=1'
  _globals['_LISTTARGETGROUPOPERATIONSREQUEST'].fields_by_name['target_group_id']._loaded_options = None
  _globals['_LISTTARGETGROUPOPERATIONSREQUEST'].fields_by_name['target_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTTARGETGROUPOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTTARGETGROUPOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTTARGETGROUPOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTTARGETGROUPOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_TARGETGROUPSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_TARGETGROUPSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\0022\0220/load-balancer/v1/targetGroups/{target_group_id}'
  _globals['_TARGETGROUPSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_TARGETGROUPSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002 \022\036/load-balancer/v1/targetGroups'
  _globals['_TARGETGROUPSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_TARGETGROUPSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*(\n\031CreateTargetGroupMetadata\022\013TargetGroup\202\323\344\223\002#\"\036/load-balancer/v1/targetGroups:\001*'
  _globals['_TARGETGROUPSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_TARGETGROUPSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*(\n\031UpdateTargetGroupMetadata\022\013TargetGroup\202\323\344\223\002520/load-balancer/v1/targetGroups/{target_group_id}:\001*'
  _globals['_TARGETGROUPSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_TARGETGROUPSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*2\n\031DeleteTargetGroupMetadata\022\025google.protobuf.Empty\202\323\344\223\0022*0/load-balancer/v1/targetGroups/{target_group_id}'
  _globals['_TARGETGROUPSERVICE'].methods_by_name['AddTargets']._loaded_options = None
  _globals['_TARGETGROUPSERVICE'].methods_by_name['AddTargets']._serialized_options = b'\262\322*!\n\022AddTargetsMetadata\022\013TargetGroup\202\323\344\223\002@\";/load-balancer/v1/targetGroups/{target_group_id}:addTargets:\001*'
  _globals['_TARGETGROUPSERVICE'].methods_by_name['RemoveTargets']._loaded_options = None
  _globals['_TARGETGROUPSERVICE'].methods_by_name['RemoveTargets']._serialized_options = b'\262\322*$\n\025RemoveTargetsMetadata\022\013TargetGroup\202\323\344\223\002C\">/load-balancer/v1/targetGroups/{target_group_id}:removeTargets:\001*'
  _globals['_TARGETGROUPSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_TARGETGROUPSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002=\022;/load-balancer/v1/targetGroups/{target_group_id}/operations'
  _globals['_GETTARGETGROUPREQUEST']._serialized_start=307
  _globals['_GETTARGETGROUPREQUEST']._serialized_end=369
  _globals['_LISTTARGETGROUPSREQUEST']._serialized_start=372
  _globals['_LISTTARGETGROUPSREQUEST']._serialized_end=520
  _globals['_LISTTARGETGROUPSRESPONSE']._serialized_start=522
  _globals['_LISTTARGETGROUPSRESPONSE']._serialized_end=639
  _globals['_CREATETARGETGROUPREQUEST']._serialized_start=642
  _globals['_CREATETARGETGROUPREQUEST']._serialized_end=1065
  _globals['_CREATETARGETGROUPREQUEST_LABELSENTRY']._serialized_start=1014
  _globals['_CREATETARGETGROUPREQUEST_LABELSENTRY']._serialized_end=1059
  _globals['_CREATETARGETGROUPMETADATA']._serialized_start=1067
  _globals['_CREATETARGETGROUPMETADATA']._serialized_end=1119
  _globals['_UPDATETARGETGROUPREQUEST']._serialized_start=1122
  _globals['_UPDATETARGETGROUPREQUEST']._serialized_end=1565
  _globals['_UPDATETARGETGROUPREQUEST_LABELSENTRY']._serialized_start=1014
  _globals['_UPDATETARGETGROUPREQUEST_LABELSENTRY']._serialized_end=1059
  _globals['_UPDATETARGETGROUPMETADATA']._serialized_start=1567
  _globals['_UPDATETARGETGROUPMETADATA']._serialized_end=1619
  _globals['_DELETETARGETGROUPREQUEST']._serialized_start=1621
  _globals['_DELETETARGETGROUPREQUEST']._serialized_end=1686
  _globals['_DELETETARGETGROUPMETADATA']._serialized_start=1688
  _globals['_DELETETARGETGROUPMETADATA']._serialized_end=1740
  _globals['_ADDTARGETSREQUEST']._serialized_start=1742
  _globals['_ADDTARGETSREQUEST']._serialized_end=1864
  _globals['_ADDTARGETSMETADATA']._serialized_start=1866
  _globals['_ADDTARGETSMETADATA']._serialized_end=1911
  _globals['_REMOVETARGETSREQUEST']._serialized_start=1913
  _globals['_REMOVETARGETSREQUEST']._serialized_end=2038
  _globals['_REMOVETARGETSMETADATA']._serialized_start=2040
  _globals['_REMOVETARGETSMETADATA']._serialized_end=2088
  _globals['_LISTTARGETGROUPOPERATIONSREQUEST']._serialized_start=2091
  _globals['_LISTTARGETGROUPOPERATIONSREQUEST']._serialized_end=2226
  _globals['_LISTTARGETGROUPOPERATIONSRESPONSE']._serialized_start=2228
  _globals['_LISTTARGETGROUPOPERATIONSRESPONSE']._serialized_end=2343
  _globals['_TARGETGROUPSERVICE']._serialized_start=2346
  _globals['_TARGETGROUPSERVICE']._serialized_end=3943
# @@protoc_insertion_point(module_scope)
