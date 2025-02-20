# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/greenplum/v1/resource_groups_service.proto
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
    'yandex/cloud/mdb/greenplum/v1/resource_groups_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.mdb.greenplum.v1 import resource_groups_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_resource__groups__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;yandex/cloud/mdb/greenplum/v1/resource_groups_service.proto\x12\x1dyandex.cloud.mdb.greenplum.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x33yandex/cloud/mdb/greenplum/v1/resource_groups.proto\"\x81\x01\n\x1b\x43reateResourceGroupMetadata\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12@\n\x13resource_group_name\x18\x02 \x01(\tB#\xe8\xc7\x31\x01\xf2\xc7\x31\x12^[^\\|/*?.,;\"\'<>]+$\x8a\xc8\x31\x05\x33-200\"\x81\x01\n\x1bUpdateResourceGroupMetadata\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12@\n\x13resource_group_name\x18\x02 \x01(\tB#\xe8\xc7\x31\x01\xf2\xc7\x31\x12^[^\\|/*?.,;\"\'<>]+$\x8a\xc8\x31\x05\x33-200\"\x81\x01\n\x1b\x44\x65leteResourceGroupMetadata\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12@\n\x13resource_group_name\x18\x02 \x01(\tB#\xe8\xc7\x31\x01\xf2\xc7\x31\x12^[^\\|/*?.,;\"\'<>]+$\x8a\xc8\x31\x05\x33-200\"=\n\x19ListResourceGroupsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"c\n\x1aListResourceGroupsResponse\x12\x45\n\x0fresource_groups\x18\x01 \x03(\x0b\x32,.yandex.cloud.mdb.greenplum.v1.ResourceGroup\"\xa1\x01\n!GetResourceGroupAtRevisionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x18\n\x08revision\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12@\n\x13resource_group_name\x18\x03 \x01(\tB#\xe8\xc7\x31\x01\xf2\xc7\x31\x12^[^\\|/*?.,;\"\'<>]+$\x8a\xc8\x31\x05\x33-200\"\x84\x01\n\x1a\x43reateResourceGroupRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x44\n\x0eresource_group\x18\x02 \x01(\x0b\x32,.yandex.cloud.mdb.greenplum.v1.ResourceGroup\"\xb5\x01\n\x1aUpdateResourceGroupRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x44\n\x0eresource_group\x18\x03 \x01(\x0b\x32,.yandex.cloud.mdb.greenplum.v1.ResourceGroup\"\x80\x01\n\x1a\x44\x65leteResourceGroupRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12@\n\x13resource_group_name\x18\x02 \x01(\tB#\xe8\xc7\x31\x01\xf2\xc7\x31\x12^[^\\|/*?.,;\"\'<>]+$\x8a\xc8\x31\x05\x33-2002\xe6\x08\n\x14ResourceGroupService\x12\xc0\x01\n\x04List\x12\x38.yandex.cloud.mdb.greenplum.v1.ListResourceGroupsRequest\x1a\x39.yandex.cloud.mdb.greenplum.v1.ListResourceGroupsResponse\"C\x82\xd3\xe4\x93\x02=\x12;/managed-greenplum/v1/clusters/{cluster_id}/resource_groups\x12\xcb\x01\n\rGetAtRevision\x12@.yandex.cloud.mdb.greenplum.v1.GetResourceGroupAtRevisionRequest\x1a,.yandex.cloud.mdb.greenplum.v1.ResourceGroup\"J\x82\xd3\xe4\x93\x02\x44\x12\x42/managed-greenplum/v1/clusters/{cluster_id}/resource_groups/at_rev\x12\xde\x01\n\x06\x43reate\x12\x39.yandex.cloud.mdb.greenplum.v1.CreateResourceGroupRequest\x1a!.yandex.cloud.operation.Operation\"v\xb2\xd2*,\n\x1b\x43reateResourceGroupMetadata\x12\rResourceGroup\x82\xd3\xe4\x93\x02@\";/managed-greenplum/v1/clusters/{cluster_id}/resource_groups:\x01*\x12\xde\x01\n\x06Update\x12\x39.yandex.cloud.mdb.greenplum.v1.UpdateResourceGroupRequest\x1a!.yandex.cloud.operation.Operation\"v\xb2\xd2*,\n\x1bUpdateResourceGroupMetadata\x12\rResourceGroup\x82\xd3\xe4\x93\x02@2;/managed-greenplum/v1/clusters/{cluster_id}/resource_groups:\x01*\x12\xfa\x01\n\x06\x44\x65lete\x12\x39.yandex.cloud.mdb.greenplum.v1.DeleteResourceGroupRequest\x1a!.yandex.cloud.operation.Operation\"\x91\x01\xb2\xd2*4\n\x1b\x44\x65leteResourceGroupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02S*Q/managed-greenplum/v1/clusters/{cluster_id}/resource_groups/{resource_group_name}Bp\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplumb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.greenplum.v1.resource_groups_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplum'
  _globals['_CREATERESOURCEGROUPMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CREATERESOURCEGROUPMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATERESOURCEGROUPMETADATA'].fields_by_name['resource_group_name']._loaded_options = None
  _globals['_CREATERESOURCEGROUPMETADATA'].fields_by_name['resource_group_name']._serialized_options = b'\350\3071\001\362\3071\022^[^\\|/*?.,;\"\'<>]+$\212\3101\0053-200'
  _globals['_UPDATERESOURCEGROUPMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATERESOURCEGROUPMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATERESOURCEGROUPMETADATA'].fields_by_name['resource_group_name']._loaded_options = None
  _globals['_UPDATERESOURCEGROUPMETADATA'].fields_by_name['resource_group_name']._serialized_options = b'\350\3071\001\362\3071\022^[^\\|/*?.,;\"\'<>]+$\212\3101\0053-200'
  _globals['_DELETERESOURCEGROUPMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETERESOURCEGROUPMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETERESOURCEGROUPMETADATA'].fields_by_name['resource_group_name']._loaded_options = None
  _globals['_DELETERESOURCEGROUPMETADATA'].fields_by_name['resource_group_name']._serialized_options = b'\350\3071\001\362\3071\022^[^\\|/*?.,;\"\'<>]+$\212\3101\0053-200'
  _globals['_LISTRESOURCEGROUPSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTRESOURCEGROUPSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETRESOURCEGROUPATREVISIONREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_GETRESOURCEGROUPATREVISIONREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETRESOURCEGROUPATREVISIONREQUEST'].fields_by_name['revision']._loaded_options = None
  _globals['_GETRESOURCEGROUPATREVISIONREQUEST'].fields_by_name['revision']._serialized_options = b'\372\3071\002>0'
  _globals['_GETRESOURCEGROUPATREVISIONREQUEST'].fields_by_name['resource_group_name']._loaded_options = None
  _globals['_GETRESOURCEGROUPATREVISIONREQUEST'].fields_by_name['resource_group_name']._serialized_options = b'\350\3071\001\362\3071\022^[^\\|/*?.,;\"\'<>]+$\212\3101\0053-200'
  _globals['_CREATERESOURCEGROUPREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_CREATERESOURCEGROUPREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATERESOURCEGROUPREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATERESOURCEGROUPREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETERESOURCEGROUPREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_DELETERESOURCEGROUPREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_DELETERESOURCEGROUPREQUEST'].fields_by_name['resource_group_name']._loaded_options = None
  _globals['_DELETERESOURCEGROUPREQUEST'].fields_by_name['resource_group_name']._serialized_options = b'\350\3071\001\362\3071\022^[^\\|/*?.,;\"\'<>]+$\212\3101\0053-200'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002=\022;/managed-greenplum/v1/clusters/{cluster_id}/resource_groups'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['GetAtRevision']._loaded_options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['GetAtRevision']._serialized_options = b'\202\323\344\223\002D\022B/managed-greenplum/v1/clusters/{cluster_id}/resource_groups/at_rev'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*,\n\033CreateResourceGroupMetadata\022\rResourceGroup\202\323\344\223\002@\";/managed-greenplum/v1/clusters/{cluster_id}/resource_groups:\001*'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*,\n\033UpdateResourceGroupMetadata\022\rResourceGroup\202\323\344\223\002@2;/managed-greenplum/v1/clusters/{cluster_id}/resource_groups:\001*'
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_RESOURCEGROUPSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*4\n\033DeleteResourceGroupMetadata\022\025google.protobuf.Empty\202\323\344\223\002S*Q/managed-greenplum/v1/clusters/{cluster_id}/resource_groups/{resource_group_name}'
  _globals['_CREATERESOURCEGROUPMETADATA']._serialized_start=317
  _globals['_CREATERESOURCEGROUPMETADATA']._serialized_end=446
  _globals['_UPDATERESOURCEGROUPMETADATA']._serialized_start=449
  _globals['_UPDATERESOURCEGROUPMETADATA']._serialized_end=578
  _globals['_DELETERESOURCEGROUPMETADATA']._serialized_start=581
  _globals['_DELETERESOURCEGROUPMETADATA']._serialized_end=710
  _globals['_LISTRESOURCEGROUPSREQUEST']._serialized_start=712
  _globals['_LISTRESOURCEGROUPSREQUEST']._serialized_end=773
  _globals['_LISTRESOURCEGROUPSRESPONSE']._serialized_start=775
  _globals['_LISTRESOURCEGROUPSRESPONSE']._serialized_end=874
  _globals['_GETRESOURCEGROUPATREVISIONREQUEST']._serialized_start=877
  _globals['_GETRESOURCEGROUPATREVISIONREQUEST']._serialized_end=1038
  _globals['_CREATERESOURCEGROUPREQUEST']._serialized_start=1041
  _globals['_CREATERESOURCEGROUPREQUEST']._serialized_end=1173
  _globals['_UPDATERESOURCEGROUPREQUEST']._serialized_start=1176
  _globals['_UPDATERESOURCEGROUPREQUEST']._serialized_end=1357
  _globals['_DELETERESOURCEGROUPREQUEST']._serialized_start=1360
  _globals['_DELETERESOURCEGROUPREQUEST']._serialized_end=1488
  _globals['_RESOURCEGROUPSERVICE']._serialized_start=1491
  _globals['_RESOURCEGROUPSERVICE']._serialized_end=2617
# @@protoc_insertion_point(module_scope)
