# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/k8s/v1/cluster_service.proto
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
from yandex.cloud.k8s.v1 import cluster_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_cluster__pb2
from yandex.cloud.k8s.v1 import node_group_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_node__group__pb2
from yandex.cloud.k8s.v1 import node_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_node__pb2
from yandex.cloud.k8s.v1 import version_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_version__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/k8s/v1/cluster_service.proto\x12\x13yandex.cloud.k8s.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a!yandex/cloud/k8s/v1/cluster.proto\x1a$yandex/cloud/k8s/v1/node_group.proto\x1a\x1eyandex/cloud/k8s/v1/node.proto\x1a!yandex/cloud/k8s/v1/version.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"-\n\x11GetClusterRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x88\x01\n\x13ListClustersRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"_\n\x14ListClustersResponse\x12.\n\x08\x63lusters\x18\x01 \x03(\x0b\x32\x1c.yandex.cloud.k8s.v1.Cluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"0\n\x14\x44\x65leteClusterRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"+\n\x15\x44\x65leteClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\".\n\x12StopClusterRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\")\n\x13StopClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"/\n\x13StartClusterRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"*\n\x14StartClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\xab\x05\n\x14UpdateClusterRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8a\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x35.yandex.cloud.k8s.v1.UpdateClusterRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12(\n\x14gateway_ipv4_address\x18\x06 \x01(\tB\x08\x8a\xc8\x31\x04<=15H\x00\x12:\n\x0bmaster_spec\x18\x07 \x01(\x0b\x32%.yandex.cloud.k8s.v1.MasterUpdateSpec\x12\x1a\n\x12service_account_id\x18\t \x01(\t\x12\x1f\n\x17node_service_account_id\x18\x08 \x01(\t\x12:\n\x0enetwork_policy\x18\n \x01(\x0b\x32\".yandex.cloud.k8s.v1.NetworkPolicy\x12\x45\n\x14ip_allocation_policy\x18\x0b \x01(\x0b\x32\'.yandex.cloud.k8s.v1.IPAllocationPolicy\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x12\n\x10internet_gateway\"\xa3\x02\n\x10MasterUpdateSpec\x12\x37\n\x07version\x18\x01 \x01(\x0b\x32&.yandex.cloud.k8s.v1.UpdateVersionSpec\x12H\n\x12maintenance_policy\x18\x02 \x01(\x0b\x32,.yandex.cloud.k8s.v1.MasterMaintenancePolicy\x12\x1a\n\x12security_group_ids\x18\x03 \x03(\t\x12:\n\x0emaster_logging\x18\x04 \x01(\x0b\x32\".yandex.cloud.k8s.v1.MasterLogging\x12\x34\n\tlocations\x18\x05 \x03(\x0b\x32!.yandex.cloud.k8s.v1.LocationSpec\"+\n\x15UpdateClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\xd4\x06\n\x14\x43reateClusterRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x32\n\x04name\x18\x02 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8a\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x35.yandex.cloud.k8s.v1.CreateClusterRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x18\n\nnetwork_id\x18\x05 \x01(\tB\x04\xe8\xc7\x31\x01\x12:\n\x0bmaster_spec\x18\x06 \x01(\x0b\x32\x1f.yandex.cloud.k8s.v1.MasterSpecB\x04\xe8\xc7\x31\x01\x12\x45\n\x14ip_allocation_policy\x18\x07 \x01(\x0b\x32\'.yandex.cloud.k8s.v1.IPAllocationPolicy\x12\x1e\n\x14gateway_ipv4_address\x18\x08 \x01(\tH\x00\x12 \n\x12service_account_id\x18\t \x01(\tB\x04\xe8\xc7\x31\x01\x12%\n\x17node_service_account_id\x18\n \x01(\tB\x04\xe8\xc7\x31\x01\x12<\n\x0frelease_channel\x18\x0b \x01(\x0e\x32#.yandex.cloud.k8s.v1.ReleaseChannel\x12:\n\x0enetwork_policy\x18\x0c \x01(\x0b\x32\".yandex.cloud.k8s.v1.NetworkPolicy\x12\x36\n\x0ckms_provider\x18\r \x01(\x0b\x32 .yandex.cloud.k8s.v1.KMSProvider\x12-\n\x06\x63ilium\x18\x0e \x01(\x0b\x32\x1b.yandex.cloud.k8s.v1.CiliumH\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x12\n\x10internet_gatewayB\x18\n\x16network_implementation\"+\n\x15\x43reateClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"/\n\x19\x41utoUpgradeMasterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\x92\x01\n\x1cListClusterOperationsRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"o\n\x1dListClusterOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x92\x01\n\x1cListClusterNodeGroupsRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"m\n\x1dListClusterNodeGroupsResponse\x12\x33\n\x0bnode_groups\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.k8s.v1.NodeGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"q\n\x17ListClusterNodesRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"]\n\x18ListClusterNodesResponse\x12(\n\x05nodes\x18\x01 \x03(\x0b\x32\x19.yandex.cloud.k8s.v1.Node\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xce\x04\n\nMasterSpec\x12\x41\n\x11zonal_master_spec\x18\x01 \x01(\x0b\x32$.yandex.cloud.k8s.v1.ZonalMasterSpecH\x00\x12G\n\x14regional_master_spec\x18\x02 \x01(\x0b\x32\'.yandex.cloud.k8s.v1.RegionalMasterSpecH\x00\x12\x34\n\tlocations\x18\x08 \x03(\x0b\x32!.yandex.cloud.k8s.v1.LocationSpec\x12$\n\x11\x65tcd_cluster_size\x18\t \x01(\x03\x42\t\xfa\xc7\x31\x05\x30,1,3\x12J\n\x18\x65xternal_v4_address_spec\x18\n \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\x12J\n\x18\x65xternal_v6_address_spec\x18\x0b \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\x12\x0f\n\x07version\x18\x03 \x01(\t\x12H\n\x12maintenance_policy\x18\x04 \x01(\x0b\x32,.yandex.cloud.k8s.v1.MasterMaintenancePolicy\x12\x1a\n\x12security_group_ids\x18\x06 \x03(\t\x12:\n\x0emaster_logging\x18\x07 \x01(\x0b\x32\".yandex.cloud.k8s.v1.MasterLoggingB\r\n\x0bmaster_type\"\xc0\x01\n\x0fZonalMasterSpec\x12\x15\n\x07zone_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12J\n\x18internal_v4_address_spec\x18\x02 \x01(\x0b\x32(.yandex.cloud.k8s.v1.InternalAddressSpec\x12J\n\x18\x65xternal_v4_address_spec\x18\x03 \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\"\xfd\x01\n\x12RegionalMasterSpec\x12\x17\n\tregion_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x36\n\tlocations\x18\x02 \x03(\x0b\x32#.yandex.cloud.k8s.v1.MasterLocation\x12J\n\x18\x65xternal_v4_address_spec\x18\x03 \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\x12J\n\x18\x65xternal_v6_address_spec\x18\x04 \x01(\x0b\x32(.yandex.cloud.k8s.v1.ExternalAddressSpec\"(\n\x13InternalAddressSpec\x12\x11\n\tsubnet_id\x18\x02 \x01(\t\"&\n\x13\x45xternalAddressSpec\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"s\n\x0eMasterLocation\x12\x15\n\x07zone_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12J\n\x18internal_v4_address_spec\x18\x02 \x01(\x0b\x32(.yandex.cloud.k8s.v1.InternalAddressSpec\"8\n\x0cLocationSpec\x12\x15\n\x07zone_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tsubnet_id\x18\x02 \x01(\t2\xc6\r\n\x0e\x43lusterService\x12\x81\x01\n\x03Get\x12&.yandex.cloud.k8s.v1.GetClusterRequest\x1a\x1c.yandex.cloud.k8s.v1.Cluster\"4\x82\xd3\xe4\x93\x02.\x12,/managed-kubernetes/v1/clusters/{cluster_id}\x12\x84\x01\n\x04List\x12(.yandex.cloud.k8s.v1.ListClustersRequest\x1a).yandex.cloud.k8s.v1.ListClustersResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/managed-kubernetes/v1/clusters\x12\xa6\x01\n\x06\x43reate\x12).yandex.cloud.k8s.v1.CreateClusterRequest\x1a!.yandex.cloud.operation.Operation\"N\xb2\xd2* \n\x15\x43reateClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02$\"\x1f/managed-kubernetes/v1/clusters:\x01*\x12\xb3\x01\n\x06Update\x12).yandex.cloud.k8s.v1.UpdateClusterRequest\x1a!.yandex.cloud.operation.Operation\"[\xb2\xd2* \n\x15UpdateClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x31\x32,/managed-kubernetes/v1/clusters/{cluster_id}:\x01*\x12\xbe\x01\n\x06\x44\x65lete\x12).yandex.cloud.k8s.v1.DeleteClusterRequest\x1a!.yandex.cloud.operation.Operation\"f\xb2\xd2*.\n\x15\x44\x65leteClusterMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02.*,/managed-kubernetes/v1/clusters/{cluster_id}\x12\xb2\x01\n\x04Stop\x12\'.yandex.cloud.k8s.v1.StopClusterRequest\x1a!.yandex.cloud.operation.Operation\"^\xb2\xd2*\x1e\n\x13StopClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x36\"1/managed-kubernetes/v1/clusters/{cluster_id}:stop:\x01*\x12\xb6\x01\n\x05Start\x12(.yandex.cloud.k8s.v1.StartClusterRequest\x1a!.yandex.cloud.operation.Operation\"`\xb2\xd2*\x1f\n\x14StartClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x37\"2/managed-kubernetes/v1/clusters/{cluster_id}:start:\x01*\x12\xb8\x01\n\x0eListNodeGroups\x12\x31.yandex.cloud.k8s.v1.ListClusterNodeGroupsRequest\x1a\x32.yandex.cloud.k8s.v1.ListClusterNodeGroupsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/managed-kubernetes/v1/clusters/{cluster_id}/nodeGroups\x12\xb8\x01\n\x0eListOperations\x12\x31.yandex.cloud.k8s.v1.ListClusterOperationsRequest\x1a\x32.yandex.cloud.k8s.v1.ListClusterOperationsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/managed-kubernetes/v1/clusters/{cluster_id}/operations\x12\xa4\x01\n\tListNodes\x12,.yandex.cloud.k8s.v1.ListClusterNodesRequest\x1a-.yandex.cloud.k8s.v1.ListClusterNodesResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/managed-kubernetes/v1/clusters/{cluster_id}/nodesBV\n\x17yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8sb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.k8s.v1.cluster_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8s'
  _GETCLUSTERREQUEST.fields_by_name['cluster_id']._options = None
  _GETCLUSTERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _LISTCLUSTERSREQUEST.fields_by_name['folder_id']._options = None
  _LISTCLUSTERSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _LISTCLUSTERSREQUEST.fields_by_name['page_size']._options = None
  _LISTCLUSTERSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTCLUSTERSREQUEST.fields_by_name['page_token']._options = None
  _LISTCLUSTERSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTCLUSTERSREQUEST.fields_by_name['filter']._options = None
  _LISTCLUSTERSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _DELETECLUSTERREQUEST.fields_by_name['cluster_id']._options = None
  _DELETECLUSTERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _STOPCLUSTERREQUEST.fields_by_name['cluster_id']._options = None
  _STOPCLUSTERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _STARTCLUSTERREQUEST.fields_by_name['cluster_id']._options = None
  _STARTCLUSTERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _UPDATECLUSTERREQUEST_LABELSENTRY._options = None
  _UPDATECLUSTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATECLUSTERREQUEST.fields_by_name['cluster_id']._options = None
  _UPDATECLUSTERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _UPDATECLUSTERREQUEST.fields_by_name['name']._options = None
  _UPDATECLUSTERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _UPDATECLUSTERREQUEST.fields_by_name['description']._options = None
  _UPDATECLUSTERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATECLUSTERREQUEST.fields_by_name['labels']._options = None
  _UPDATECLUSTERREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _UPDATECLUSTERREQUEST.fields_by_name['gateway_ipv4_address']._options = None
  _UPDATECLUSTERREQUEST.fields_by_name['gateway_ipv4_address']._serialized_options = b'\212\3101\004<=15'
  _CREATECLUSTERREQUEST_LABELSENTRY._options = None
  _CREATECLUSTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATECLUSTERREQUEST.fields_by_name['folder_id']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATECLUSTERREQUEST.fields_by_name['name']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _CREATECLUSTERREQUEST.fields_by_name['description']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATECLUSTERREQUEST.fields_by_name['labels']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _CREATECLUSTERREQUEST.fields_by_name['network_id']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['network_id']._serialized_options = b'\350\3071\001'
  _CREATECLUSTERREQUEST.fields_by_name['master_spec']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['master_spec']._serialized_options = b'\350\3071\001'
  _CREATECLUSTERREQUEST.fields_by_name['service_account_id']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['service_account_id']._serialized_options = b'\350\3071\001'
  _CREATECLUSTERREQUEST.fields_by_name['node_service_account_id']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['node_service_account_id']._serialized_options = b'\350\3071\001'
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['cluster_id']._options = None
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['filter']._options = None
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTCLUSTERNODEGROUPSREQUEST.fields_by_name['cluster_id']._options = None
  _LISTCLUSTERNODEGROUPSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _LISTCLUSTERNODEGROUPSREQUEST.fields_by_name['page_size']._options = None
  _LISTCLUSTERNODEGROUPSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTCLUSTERNODEGROUPSREQUEST.fields_by_name['page_token']._options = None
  _LISTCLUSTERNODEGROUPSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTCLUSTERNODEGROUPSREQUEST.fields_by_name['filter']._options = None
  _LISTCLUSTERNODEGROUPSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTCLUSTERNODESREQUEST.fields_by_name['cluster_id']._options = None
  _LISTCLUSTERNODESREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _LISTCLUSTERNODESREQUEST.fields_by_name['page_size']._options = None
  _LISTCLUSTERNODESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTCLUSTERNODESREQUEST.fields_by_name['page_token']._options = None
  _LISTCLUSTERNODESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _MASTERSPEC.fields_by_name['etcd_cluster_size']._options = None
  _MASTERSPEC.fields_by_name['etcd_cluster_size']._serialized_options = b'\372\3071\0050,1,3'
  _ZONALMASTERSPEC.fields_by_name['zone_id']._options = None
  _ZONALMASTERSPEC.fields_by_name['zone_id']._serialized_options = b'\350\3071\001'
  _REGIONALMASTERSPEC.fields_by_name['region_id']._options = None
  _REGIONALMASTERSPEC.fields_by_name['region_id']._serialized_options = b'\350\3071\001'
  _MASTERLOCATION.fields_by_name['zone_id']._options = None
  _MASTERLOCATION.fields_by_name['zone_id']._serialized_options = b'\350\3071\001'
  _LOCATIONSPEC.fields_by_name['zone_id']._options = None
  _LOCATIONSPEC.fields_by_name['zone_id']._serialized_options = b'\350\3071\001'
  _CLUSTERSERVICE.methods_by_name['Get']._options = None
  _CLUSTERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002.\022,/managed-kubernetes/v1/clusters/{cluster_id}'
  _CLUSTERSERVICE.methods_by_name['List']._options = None
  _CLUSTERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/managed-kubernetes/v1/clusters'
  _CLUSTERSERVICE.methods_by_name['Create']._options = None
  _CLUSTERSERVICE.methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateClusterMetadata\022\007Cluster\202\323\344\223\002$\"\037/managed-kubernetes/v1/clusters:\001*'
  _CLUSTERSERVICE.methods_by_name['Update']._options = None
  _CLUSTERSERVICE.methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateClusterMetadata\022\007Cluster\202\323\344\223\00212,/managed-kubernetes/v1/clusters/{cluster_id}:\001*'
  _CLUSTERSERVICE.methods_by_name['Delete']._options = None
  _CLUSTERSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteClusterMetadata\022\025google.protobuf.Empty\202\323\344\223\002.*,/managed-kubernetes/v1/clusters/{cluster_id}'
  _CLUSTERSERVICE.methods_by_name['Stop']._options = None
  _CLUSTERSERVICE.methods_by_name['Stop']._serialized_options = b'\262\322*\036\n\023StopClusterMetadata\022\007Cluster\202\323\344\223\0026\"1/managed-kubernetes/v1/clusters/{cluster_id}:stop:\001*'
  _CLUSTERSERVICE.methods_by_name['Start']._options = None
  _CLUSTERSERVICE.methods_by_name['Start']._serialized_options = b'\262\322*\037\n\024StartClusterMetadata\022\007Cluster\202\323\344\223\0027\"2/managed-kubernetes/v1/clusters/{cluster_id}:start:\001*'
  _CLUSTERSERVICE.methods_by_name['ListNodeGroups']._options = None
  _CLUSTERSERVICE.methods_by_name['ListNodeGroups']._serialized_options = b'\202\323\344\223\0029\0227/managed-kubernetes/v1/clusters/{cluster_id}/nodeGroups'
  _CLUSTERSERVICE.methods_by_name['ListOperations']._options = None
  _CLUSTERSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0029\0227/managed-kubernetes/v1/clusters/{cluster_id}/operations'
  _CLUSTERSERVICE.methods_by_name['ListNodes']._options = None
  _CLUSTERSERVICE.methods_by_name['ListNodes']._serialized_options = b'\202\323\344\223\0024\0222/managed-kubernetes/v1/clusters/{cluster_id}/nodes'
  _globals['_GETCLUSTERREQUEST']._serialized_start=375
  _globals['_GETCLUSTERREQUEST']._serialized_end=420
  _globals['_LISTCLUSTERSREQUEST']._serialized_start=423
  _globals['_LISTCLUSTERSREQUEST']._serialized_end=559
  _globals['_LISTCLUSTERSRESPONSE']._serialized_start=561
  _globals['_LISTCLUSTERSRESPONSE']._serialized_end=656
  _globals['_DELETECLUSTERREQUEST']._serialized_start=658
  _globals['_DELETECLUSTERREQUEST']._serialized_end=706
  _globals['_DELETECLUSTERMETADATA']._serialized_start=708
  _globals['_DELETECLUSTERMETADATA']._serialized_end=751
  _globals['_STOPCLUSTERREQUEST']._serialized_start=753
  _globals['_STOPCLUSTERREQUEST']._serialized_end=799
  _globals['_STOPCLUSTERMETADATA']._serialized_start=801
  _globals['_STOPCLUSTERMETADATA']._serialized_end=842
  _globals['_STARTCLUSTERREQUEST']._serialized_start=844
  _globals['_STARTCLUSTERREQUEST']._serialized_end=891
  _globals['_STARTCLUSTERMETADATA']._serialized_start=893
  _globals['_STARTCLUSTERMETADATA']._serialized_end=935
  _globals['_UPDATECLUSTERREQUEST']._serialized_start=938
  _globals['_UPDATECLUSTERREQUEST']._serialized_end=1621
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_start=1556
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_end=1601
  _globals['_MASTERUPDATESPEC']._serialized_start=1624
  _globals['_MASTERUPDATESPEC']._serialized_end=1915
  _globals['_UPDATECLUSTERMETADATA']._serialized_start=1917
  _globals['_UPDATECLUSTERMETADATA']._serialized_end=1960
  _globals['_CREATECLUSTERREQUEST']._serialized_start=1963
  _globals['_CREATECLUSTERREQUEST']._serialized_end=2815
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_start=1556
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_end=1601
  _globals['_CREATECLUSTERMETADATA']._serialized_start=2817
  _globals['_CREATECLUSTERMETADATA']._serialized_end=2860
  _globals['_AUTOUPGRADEMASTERMETADATA']._serialized_start=2862
  _globals['_AUTOUPGRADEMASTERMETADATA']._serialized_end=2909
  _globals['_LISTCLUSTEROPERATIONSREQUEST']._serialized_start=2912
  _globals['_LISTCLUSTEROPERATIONSREQUEST']._serialized_end=3058
  _globals['_LISTCLUSTEROPERATIONSRESPONSE']._serialized_start=3060
  _globals['_LISTCLUSTEROPERATIONSRESPONSE']._serialized_end=3171
  _globals['_LISTCLUSTERNODEGROUPSREQUEST']._serialized_start=3174
  _globals['_LISTCLUSTERNODEGROUPSREQUEST']._serialized_end=3320
  _globals['_LISTCLUSTERNODEGROUPSRESPONSE']._serialized_start=3322
  _globals['_LISTCLUSTERNODEGROUPSRESPONSE']._serialized_end=3431
  _globals['_LISTCLUSTERNODESREQUEST']._serialized_start=3433
  _globals['_LISTCLUSTERNODESREQUEST']._serialized_end=3546
  _globals['_LISTCLUSTERNODESRESPONSE']._serialized_start=3548
  _globals['_LISTCLUSTERNODESRESPONSE']._serialized_end=3641
  _globals['_MASTERSPEC']._serialized_start=3644
  _globals['_MASTERSPEC']._serialized_end=4234
  _globals['_ZONALMASTERSPEC']._serialized_start=4237
  _globals['_ZONALMASTERSPEC']._serialized_end=4429
  _globals['_REGIONALMASTERSPEC']._serialized_start=4432
  _globals['_REGIONALMASTERSPEC']._serialized_end=4685
  _globals['_INTERNALADDRESSSPEC']._serialized_start=4687
  _globals['_INTERNALADDRESSSPEC']._serialized_end=4727
  _globals['_EXTERNALADDRESSSPEC']._serialized_start=4729
  _globals['_EXTERNALADDRESSSPEC']._serialized_end=4767
  _globals['_MASTERLOCATION']._serialized_start=4769
  _globals['_MASTERLOCATION']._serialized_end=4884
  _globals['_LOCATIONSPEC']._serialized_start=4886
  _globals['_LOCATIONSPEC']._serialized_end=4942
  _globals['_CLUSTERSERVICE']._serialized_start=4945
  _globals['_CLUSTERSERVICE']._serialized_end=6679
# @@protoc_insertion_point(module_scope)
