# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/vpc/v1/subnet_service.proto
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
from yandex.cloud.vpc.v1 import subnet_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_subnet__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.reference import reference_pb2 as yandex_dot_cloud_dot_reference_dot_reference__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/vpc/v1/subnet_service.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a yandex/cloud/vpc/v1/subnet.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a&yandex/cloud/reference/reference.proto\"3\n\x10GetSubnetRequest\x12\x1f\n\tsubnet_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x8f\x01\n\x12ListSubnetsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"\\\n\x13ListSubnetsResponse\x12,\n\x07subnets\x18\x01 \x03(\x0b\x32\x1b.yandex.cloud.vpc.v1.Subnet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xf3\x03\n\x13\x43reateSubnetRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x81\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x34.yandex.cloud.vpc.v1.CreateSubnetRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12 \n\nnetwork_id\x18\x05 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\x07zone_id\x18\x06 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\x0ev4_cidr_blocks\x18\x07 \x03(\tB\x04\xe8\xc7\x31\x01\x12 \n\x0eroute_table_id\x18\t \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x36\n\x0c\x64hcp_options\x18\n \x01(\x0b\x32 .yandex.cloud.vpc.v1.DhcpOptions\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\x14\x43reateSubnetMetadata\x12\x11\n\tsubnet_id\x18\x01 \x01(\t\"\xdd\x03\n\x13UpdateSubnetRequest\x12\x1f\n\tsubnet_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x81\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x34.yandex.cloud.vpc.v1.UpdateSubnetRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12 \n\x0eroute_table_id\x18\x06 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x36\n\x0c\x64hcp_options\x18\x07 \x01(\x0b\x32 .yandex.cloud.vpc.v1.DhcpOptions\x12\x16\n\x0ev4_cidr_blocks\x18\x08 \x03(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\x14UpdateSubnetMetadata\x12\x11\n\tsubnet_id\x18\x01 \x01(\t\"U\n\x1a\x41\x64\x64SubnetCidrBlocksRequest\x12\x1f\n\tsubnet_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x16\n\x0ev4_cidr_blocks\x18\x02 \x03(\t\"0\n\x1b\x41\x64\x64SubnetCidrBlocksMetadata\x12\x11\n\tsubnet_id\x18\x01 \x01(\t\"X\n\x1dRemoveSubnetCidrBlocksRequest\x12\x1f\n\tsubnet_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x16\n\x0ev4_cidr_blocks\x18\x02 \x03(\t\"3\n\x1eRemoveSubnetCidrBlocksMetadata\x12\x11\n\tsubnet_id\x18\x01 \x01(\t\"6\n\x13\x44\x65leteSubnetRequest\x12\x1f\n\tsubnet_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\")\n\x14\x44\x65leteSubnetMetadata\x12\x11\n\tsubnet_id\x18\x01 \x01(\t\"|\n\x1bListSubnetOperationsRequest\x12\x1f\n\tsubnet_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"n\n\x1cListSubnetOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"a\n\x11MoveSubnetRequest\x12\x1f\n\tsubnet_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12+\n\x15\x64\x65stination_folder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\'\n\x12MoveSubnetMetadata\x12\x11\n\tsubnet_id\x18\x01 \x01(\t\"j\n\x18ListUsedAddressesRequest\x12\x17\n\tsubnet_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\"i\n\x19ListUsedAddressesResponse\x12\x33\n\taddresses\x18\x01 \x03(\x0b\x32 .yandex.cloud.vpc.v1.UsedAddress\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x89\x01\n\x0bUsedAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x32\n\nip_version\x18\x02 \x01(\x0e\x32\x1e.yandex.cloud.vpc.v1.IpVersion\x12\x35\n\nreferences\x18\x03 \x03(\x0b\x32!.yandex.cloud.reference.Reference\"[\n\x15RelocateSubnetRequest\x12\x1f\n\tsubnet_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12!\n\x13\x64\x65stination_zone_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"+\n\x16RelocateSubnetMetadata\x12\x11\n\tsubnet_id\x18\x01 \x01(\t2\x80\x0e\n\rSubnetService\x12n\n\x03Get\x12%.yandex.cloud.vpc.v1.GetSubnetRequest\x1a\x1b.yandex.cloud.vpc.v1.Subnet\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/vpc/v1/subnets/{subnet_id}\x12r\n\x04List\x12\'.yandex.cloud.vpc.v1.ListSubnetsRequest\x1a(.yandex.cloud.vpc.v1.ListSubnetsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/vpc/v1/subnets\x12\x93\x01\n\x06\x43reate\x12(.yandex.cloud.vpc.v1.CreateSubnetRequest\x1a!.yandex.cloud.operation.Operation\"<\xb2\xd2*\x1e\n\x14\x43reateSubnetMetadata\x12\x06Subnet\x82\xd3\xe4\x93\x02\x14\"\x0f/vpc/v1/subnets:\x01*\x12\x9f\x01\n\x06Update\x12(.yandex.cloud.vpc.v1.UpdateSubnetRequest\x1a!.yandex.cloud.operation.Operation\"H\xb2\xd2*\x1e\n\x14UpdateSubnetMetadata\x12\x06Subnet\x82\xd3\xe4\x93\x02 2\x1b/vpc/v1/subnets/{subnet_id}:\x01*\x12\xbd\x01\n\rAddCidrBlocks\x12/.yandex.cloud.vpc.v1.AddSubnetCidrBlocksRequest\x1a!.yandex.cloud.operation.Operation\"X\xb2\xd2*\x1e\n\x14UpdateSubnetMetadata\x12\x06Subnet\x82\xd3\xe4\x93\x02\x30\"+/vpc/v1/subnets/{subnet_id}:add-cidr-blocks:\x01*\x12\xc6\x01\n\x10RemoveCidrBlocks\x12\x32.yandex.cloud.vpc.v1.RemoveSubnetCidrBlocksRequest\x1a!.yandex.cloud.operation.Operation\"[\xb2\xd2*\x1e\n\x14UpdateSubnetMetadata\x12\x06Subnet\x82\xd3\xe4\x93\x02\x33\"./vpc/v1/subnets/{subnet_id}:remove-cidr-blocks:\x01*\x12\xab\x01\n\x06\x44\x65lete\x12(.yandex.cloud.vpc.v1.DeleteSubnetRequest\x1a!.yandex.cloud.operation.Operation\"T\xb2\xd2*-\n\x14\x44\x65leteSubnetMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1d*\x1b/vpc/v1/subnets/{subnet_id}\x12\xa5\x01\n\x0eListOperations\x12\x30.yandex.cloud.vpc.v1.ListSubnetOperationsRequest\x1a\x31.yandex.cloud.vpc.v1.ListSubnetOperationsResponse\".\x82\xd3\xe4\x93\x02(\x12&/vpc/v1/subnets/{subnet_id}/operations\x12\x9e\x01\n\x04Move\x12&.yandex.cloud.vpc.v1.MoveSubnetRequest\x1a!.yandex.cloud.operation.Operation\"K\xb2\xd2*\x1c\n\x12MoveSubnetMetadata\x12\x06Subnet\x82\xd3\xe4\x93\x02%\" /vpc/v1/subnets/{subnet_id}:move:\x01*\x12\xae\x01\n\x08Relocate\x12*.yandex.cloud.vpc.v1.RelocateSubnetRequest\x1a!.yandex.cloud.operation.Operation\"S\xb2\xd2* \n\x16RelocateSubnetMetadata\x12\x06Subnet\x82\xd3\xe4\x93\x02)\"$/vpc/v1/subnets/{subnet_id}:relocate:\x01*\x12\xa1\x01\n\x11ListUsedAddresses\x12-.yandex.cloud.vpc.v1.ListUsedAddressesRequest\x1a..yandex.cloud.vpc.v1.ListUsedAddressesResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/vpc/v1/subnets/{subnet_id}/addressesBV\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.vpc.v1.subnet_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc'
  _GETSUBNETREQUEST.fields_by_name['subnet_id']._options = None
  _GETSUBNETREQUEST.fields_by_name['subnet_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSUBNETSREQUEST.fields_by_name['folder_id']._options = None
  _LISTSUBNETSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSUBNETSREQUEST.fields_by_name['page_size']._options = None
  _LISTSUBNETSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTSUBNETSREQUEST.fields_by_name['page_token']._options = None
  _LISTSUBNETSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTSUBNETSREQUEST.fields_by_name['filter']._options = None
  _LISTSUBNETSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _CREATESUBNETREQUEST_LABELSENTRY._options = None
  _CREATESUBNETREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATESUBNETREQUEST.fields_by_name['folder_id']._options = None
  _CREATESUBNETREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATESUBNETREQUEST.fields_by_name['name']._options = None
  _CREATESUBNETREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _CREATESUBNETREQUEST.fields_by_name['description']._options = None
  _CREATESUBNETREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATESUBNETREQUEST.fields_by_name['labels']._options = None
  _CREATESUBNETREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _CREATESUBNETREQUEST.fields_by_name['network_id']._options = None
  _CREATESUBNETREQUEST.fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATESUBNETREQUEST.fields_by_name['zone_id']._options = None
  _CREATESUBNETREQUEST.fields_by_name['zone_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATESUBNETREQUEST.fields_by_name['v4_cidr_blocks']._options = None
  _CREATESUBNETREQUEST.fields_by_name['v4_cidr_blocks']._serialized_options = b'\350\3071\001'
  _CREATESUBNETREQUEST.fields_by_name['route_table_id']._options = None
  _CREATESUBNETREQUEST.fields_by_name['route_table_id']._serialized_options = b'\212\3101\004<=50'
  _UPDATESUBNETREQUEST_LABELSENTRY._options = None
  _UPDATESUBNETREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATESUBNETREQUEST.fields_by_name['subnet_id']._options = None
  _UPDATESUBNETREQUEST.fields_by_name['subnet_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATESUBNETREQUEST.fields_by_name['name']._options = None
  _UPDATESUBNETREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _UPDATESUBNETREQUEST.fields_by_name['description']._options = None
  _UPDATESUBNETREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATESUBNETREQUEST.fields_by_name['labels']._options = None
  _UPDATESUBNETREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _UPDATESUBNETREQUEST.fields_by_name['route_table_id']._options = None
  _UPDATESUBNETREQUEST.fields_by_name['route_table_id']._serialized_options = b'\212\3101\004<=50'
  _ADDSUBNETCIDRBLOCKSREQUEST.fields_by_name['subnet_id']._options = None
  _ADDSUBNETCIDRBLOCKSREQUEST.fields_by_name['subnet_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _REMOVESUBNETCIDRBLOCKSREQUEST.fields_by_name['subnet_id']._options = None
  _REMOVESUBNETCIDRBLOCKSREQUEST.fields_by_name['subnet_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETESUBNETREQUEST.fields_by_name['subnet_id']._options = None
  _DELETESUBNETREQUEST.fields_by_name['subnet_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSUBNETOPERATIONSREQUEST.fields_by_name['subnet_id']._options = None
  _LISTSUBNETOPERATIONSREQUEST.fields_by_name['subnet_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSUBNETOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTSUBNETOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTSUBNETOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTSUBNETOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _MOVESUBNETREQUEST.fields_by_name['subnet_id']._options = None
  _MOVESUBNETREQUEST.fields_by_name['subnet_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _MOVESUBNETREQUEST.fields_by_name['destination_folder_id']._options = None
  _MOVESUBNETREQUEST.fields_by_name['destination_folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTUSEDADDRESSESREQUEST.fields_by_name['subnet_id']._options = None
  _LISTUSEDADDRESSESREQUEST.fields_by_name['subnet_id']._serialized_options = b'\350\3071\001'
  _RELOCATESUBNETREQUEST.fields_by_name['subnet_id']._options = None
  _RELOCATESUBNETREQUEST.fields_by_name['subnet_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _RELOCATESUBNETREQUEST.fields_by_name['destination_zone_id']._options = None
  _RELOCATESUBNETREQUEST.fields_by_name['destination_zone_id']._serialized_options = b'\350\3071\001'
  _SUBNETSERVICE.methods_by_name['Get']._options = None
  _SUBNETSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\035\022\033/vpc/v1/subnets/{subnet_id}'
  _SUBNETSERVICE.methods_by_name['List']._options = None
  _SUBNETSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\021\022\017/vpc/v1/subnets'
  _SUBNETSERVICE.methods_by_name['Create']._options = None
  _SUBNETSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*\036\n\024CreateSubnetMetadata\022\006Subnet\202\323\344\223\002\024\"\017/vpc/v1/subnets:\001*'
  _SUBNETSERVICE.methods_by_name['Update']._options = None
  _SUBNETSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\036\n\024UpdateSubnetMetadata\022\006Subnet\202\323\344\223\002 2\033/vpc/v1/subnets/{subnet_id}:\001*'
  _SUBNETSERVICE.methods_by_name['AddCidrBlocks']._options = None
  _SUBNETSERVICE.methods_by_name['AddCidrBlocks']._serialized_options = b'\262\322*\036\n\024UpdateSubnetMetadata\022\006Subnet\202\323\344\223\0020\"+/vpc/v1/subnets/{subnet_id}:add-cidr-blocks:\001*'
  _SUBNETSERVICE.methods_by_name['RemoveCidrBlocks']._options = None
  _SUBNETSERVICE.methods_by_name['RemoveCidrBlocks']._serialized_options = b'\262\322*\036\n\024UpdateSubnetMetadata\022\006Subnet\202\323\344\223\0023\"./vpc/v1/subnets/{subnet_id}:remove-cidr-blocks:\001*'
  _SUBNETSERVICE.methods_by_name['Delete']._options = None
  _SUBNETSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*-\n\024DeleteSubnetMetadata\022\025google.protobuf.Empty\202\323\344\223\002\035*\033/vpc/v1/subnets/{subnet_id}'
  _SUBNETSERVICE.methods_by_name['ListOperations']._options = None
  _SUBNETSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002(\022&/vpc/v1/subnets/{subnet_id}/operations'
  _SUBNETSERVICE.methods_by_name['Move']._options = None
  _SUBNETSERVICE.methods_by_name['Move']._serialized_options = b'\262\322*\034\n\022MoveSubnetMetadata\022\006Subnet\202\323\344\223\002%\" /vpc/v1/subnets/{subnet_id}:move:\001*'
  _SUBNETSERVICE.methods_by_name['Relocate']._options = None
  _SUBNETSERVICE.methods_by_name['Relocate']._serialized_options = b'\262\322* \n\026RelocateSubnetMetadata\022\006Subnet\202\323\344\223\002)\"$/vpc/v1/subnets/{subnet_id}:relocate:\001*'
  _SUBNETSERVICE.methods_by_name['ListUsedAddresses']._options = None
  _SUBNETSERVICE.methods_by_name['ListUsedAddresses']._serialized_options = b'\202\323\344\223\002\'\022%/vpc/v1/subnets/{subnet_id}/addresses'
  _globals['_GETSUBNETREQUEST']._serialized_start=308
  _globals['_GETSUBNETREQUEST']._serialized_end=359
  _globals['_LISTSUBNETSREQUEST']._serialized_start=362
  _globals['_LISTSUBNETSREQUEST']._serialized_end=505
  _globals['_LISTSUBNETSRESPONSE']._serialized_start=507
  _globals['_LISTSUBNETSRESPONSE']._serialized_end=599
  _globals['_CREATESUBNETREQUEST']._serialized_start=602
  _globals['_CREATESUBNETREQUEST']._serialized_end=1101
  _globals['_CREATESUBNETREQUEST_LABELSENTRY']._serialized_start=1056
  _globals['_CREATESUBNETREQUEST_LABELSENTRY']._serialized_end=1101
  _globals['_CREATESUBNETMETADATA']._serialized_start=1103
  _globals['_CREATESUBNETMETADATA']._serialized_end=1144
  _globals['_UPDATESUBNETREQUEST']._serialized_start=1147
  _globals['_UPDATESUBNETREQUEST']._serialized_end=1624
  _globals['_UPDATESUBNETREQUEST_LABELSENTRY']._serialized_start=1056
  _globals['_UPDATESUBNETREQUEST_LABELSENTRY']._serialized_end=1101
  _globals['_UPDATESUBNETMETADATA']._serialized_start=1626
  _globals['_UPDATESUBNETMETADATA']._serialized_end=1667
  _globals['_ADDSUBNETCIDRBLOCKSREQUEST']._serialized_start=1669
  _globals['_ADDSUBNETCIDRBLOCKSREQUEST']._serialized_end=1754
  _globals['_ADDSUBNETCIDRBLOCKSMETADATA']._serialized_start=1756
  _globals['_ADDSUBNETCIDRBLOCKSMETADATA']._serialized_end=1804
  _globals['_REMOVESUBNETCIDRBLOCKSREQUEST']._serialized_start=1806
  _globals['_REMOVESUBNETCIDRBLOCKSREQUEST']._serialized_end=1894
  _globals['_REMOVESUBNETCIDRBLOCKSMETADATA']._serialized_start=1896
  _globals['_REMOVESUBNETCIDRBLOCKSMETADATA']._serialized_end=1947
  _globals['_DELETESUBNETREQUEST']._serialized_start=1949
  _globals['_DELETESUBNETREQUEST']._serialized_end=2003
  _globals['_DELETESUBNETMETADATA']._serialized_start=2005
  _globals['_DELETESUBNETMETADATA']._serialized_end=2046
  _globals['_LISTSUBNETOPERATIONSREQUEST']._serialized_start=2048
  _globals['_LISTSUBNETOPERATIONSREQUEST']._serialized_end=2172
  _globals['_LISTSUBNETOPERATIONSRESPONSE']._serialized_start=2174
  _globals['_LISTSUBNETOPERATIONSRESPONSE']._serialized_end=2284
  _globals['_MOVESUBNETREQUEST']._serialized_start=2286
  _globals['_MOVESUBNETREQUEST']._serialized_end=2383
  _globals['_MOVESUBNETMETADATA']._serialized_start=2385
  _globals['_MOVESUBNETMETADATA']._serialized_end=2424
  _globals['_LISTUSEDADDRESSESREQUEST']._serialized_start=2426
  _globals['_LISTUSEDADDRESSESREQUEST']._serialized_end=2532
  _globals['_LISTUSEDADDRESSESRESPONSE']._serialized_start=2534
  _globals['_LISTUSEDADDRESSESRESPONSE']._serialized_end=2639
  _globals['_USEDADDRESS']._serialized_start=2642
  _globals['_USEDADDRESS']._serialized_end=2779
  _globals['_RELOCATESUBNETREQUEST']._serialized_start=2781
  _globals['_RELOCATESUBNETREQUEST']._serialized_end=2872
  _globals['_RELOCATESUBNETMETADATA']._serialized_start=2874
  _globals['_RELOCATESUBNETMETADATA']._serialized_end=2917
  _globals['_SUBNETSERVICE']._serialized_start=2920
  _globals['_SUBNETSERVICE']._serialized_end=4712
# @@protoc_insertion_point(module_scope)
