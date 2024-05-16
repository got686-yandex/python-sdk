# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dns/v1/dns_zone_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.dns.v1 import dns_zone_pb2 as yandex_dot_cloud_dot_dns_dot_v1_dot_dns__zone__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/dns/v1/dns_zone_service.proto\x12\x13yandex.cloud.dns.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a\"yandex/cloud/dns/v1/dns_zone.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"\x86\x01\n#UpdateDnsZonePrivateNetworksRequest\x12\x13\n\x0b\x64ns_zone_id\x18\x01 \x01(\t\x12$\n\x1cprivate_network_id_additions\x18\x02 \x03(\t\x12$\n\x1cprivate_network_id_deletions\x18\x03 \x03(\t\";\n$UpdateDnsZonePrivateNetworksMetadata\x12\x13\n\x0b\x64ns_zone_id\x18\x01 \x01(\t\".\n\x11GetDnsZoneRequest\x12\x19\n\x0b\x64ns_zone_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x89\x01\n\x13ListDnsZonesRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"`\n\x14ListDnsZonesResponse\x12/\n\tdns_zones\x18\x01 \x03(\x0b\x32\x1c.yandex.cloud.dns.v1.DnsZone\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa4\x04\n\x14\x43reateDnsZoneRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x32\n\x04name\x18\x02 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8a\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x35.yandex.cloud.dns.v1.CreateDnsZoneRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x38\n\x04zone\x18\x05 \x01(\tB*\xe8\xc7\x31\x01\xf2\xc7\x31\x19[.]|[a-z0-9][-a-z0-9.]*\\.\x8a\xc8\x31\x05<=255\x12\x42\n\x12private_visibility\x18\x06 \x01(\x0b\x32&.yandex.cloud.dns.v1.PrivateVisibility\x12@\n\x11public_visibility\x18\x07 \x01(\x0b\x32%.yandex.cloud.dns.v1.PublicVisibility\x12\x1b\n\x13\x64\x65letion_protection\x18\x08 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\",\n\x15\x43reateDnsZoneMetadata\x12\x13\n\x0b\x64ns_zone_id\x18\x01 \x01(\t\"\x97\x04\n\x14UpdateDnsZoneRequest\x12\x1b\n\x0b\x64ns_zone_id\x18\x01 \x01(\tB\x06\x8a\xc8\x31\x02\x32\x30\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8a\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x35.yandex.cloud.dns.v1.UpdateDnsZoneRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x42\n\x12private_visibility\x18\x06 \x01(\x0b\x32&.yandex.cloud.dns.v1.PrivateVisibility\x12@\n\x11public_visibility\x18\x07 \x01(\x0b\x32%.yandex.cloud.dns.v1.PublicVisibility\x12\x1b\n\x13\x64\x65letion_protection\x18\x08 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\",\n\x15UpdateDnsZoneMetadata\x12\x13\n\x0b\x64ns_zone_id\x18\x01 \x01(\t\"3\n\x14\x44\x65leteDnsZoneRequest\x12\x1b\n\x0b\x64ns_zone_id\x18\x01 \x01(\tB\x06\x8a\xc8\x31\x02\x32\x30\",\n\x15\x44\x65leteDnsZoneMetadata\x12\x13\n\x0b\x64ns_zone_id\x18\x01 \x01(\t\"r\n\x1aGetDnsZoneRecordSetRequest\x12\x1b\n\x0b\x64ns_zone_id\x18\x01 \x01(\tB\x06\x8a\xc8\x31\x02\x32\x30\x12\x1b\n\x04name\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05<=255\x12\x1a\n\x04type\x18\x03 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=10\"\x96\x01\n\x1cListDnsZoneRecordSetsRequest\x12\x1b\n\x0b\x64ns_zone_id\x18\x01 \x01(\tB\x06\x8a\xc8\x31\x02\x32\x30\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"m\n\x1dListDnsZoneRecordSetsResponse\x12\x33\n\x0brecord_sets\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.dns.v1.RecordSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xb4\x01\n\x17UpdateRecordSetsRequest\x12\x1b\n\x0b\x64ns_zone_id\x18\x01 \x01(\tB\x06\x8a\xc8\x31\x02\x32\x30\x12=\n\tdeletions\x18\x02 \x03(\x0b\x32\x1e.yandex.cloud.dns.v1.RecordSetB\n\x82\xc8\x31\x06<=1000\x12=\n\tadditions\x18\x03 \x03(\x0b\x32\x1e.yandex.cloud.dns.v1.RecordSetB\n\x82\xc8\x31\x06<=1000\"\x1a\n\x18UpdateRecordSetsMetadata\"\xf3\x01\n\x17UpsertRecordSetsRequest\x12\x1b\n\x0b\x64ns_zone_id\x18\x01 \x01(\tB\x06\x8a\xc8\x31\x02\x32\x30\x12=\n\tdeletions\x18\x02 \x03(\x0b\x32\x1e.yandex.cloud.dns.v1.RecordSetB\n\x82\xc8\x31\x06<=1000\x12@\n\x0creplacements\x18\x03 \x03(\x0b\x32\x1e.yandex.cloud.dns.v1.RecordSetB\n\x82\xc8\x31\x06<=1000\x12:\n\x06merges\x18\x04 \x03(\x0b\x32\x1e.yandex.cloud.dns.v1.RecordSetB\n\x82\xc8\x31\x06<=1000\"\x1a\n\x18UpsertRecordSetsMetadata\"u\n\rRecordSetDiff\x12\x31\n\tadditions\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.dns.v1.RecordSet\x12\x31\n\tdeletions\x18\x02 \x03(\x0b\x32\x1e.yandex.cloud.dns.v1.RecordSet\"\x96\x01\n\x1cListDnsZoneOperationsRequest\x12\x1b\n\x0b\x64ns_zone_id\x18\x01 \x01(\tB\x06\x8a\xc8\x31\x02\x32\x30\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"o\n\x1dListDnsZoneOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xc8\x13\n\x0e\x44nsZoneService\x12p\n\x03Get\x12&.yandex.cloud.dns.v1.GetDnsZoneRequest\x1a\x1c.yandex.cloud.dns.v1.DnsZone\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/dns/v1/zones/{dns_zone_id}\x12r\n\x04List\x12(.yandex.cloud.dns.v1.ListDnsZonesRequest\x1a).yandex.cloud.dns.v1.ListDnsZonesResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/dns/v1/zones\x12\x94\x01\n\x06\x43reate\x12).yandex.cloud.dns.v1.CreateDnsZoneRequest\x1a!.yandex.cloud.operation.Operation\"<\xb2\xd2* \n\x15\x43reateDnsZoneMetadata\x12\x07\x44nsZone\x82\xd3\xe4\x93\x02\x12\"\r/dns/v1/zones:\x01*\x12\xa2\x01\n\x06Update\x12).yandex.cloud.dns.v1.UpdateDnsZoneRequest\x1a!.yandex.cloud.operation.Operation\"J\xb2\xd2* \n\x15UpdateDnsZoneMetadata\x12\x07\x44nsZone\x82\xd3\xe4\x93\x02 2\x1b/dns/v1/zones/{dns_zone_id}:\x01*\x12\xad\x01\n\x06\x44\x65lete\x12).yandex.cloud.dns.v1.DeleteDnsZoneRequest\x1a!.yandex.cloud.operation.Operation\"U\xb2\xd2*.\n\x15\x44\x65leteDnsZoneMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1d*\x1b/dns/v1/zones/{dns_zone_id}\x12\x91\x01\n\x0cGetRecordSet\x12/.yandex.cloud.dns.v1.GetDnsZoneRecordSetRequest\x1a\x1e.yandex.cloud.dns.v1.RecordSet\"0\x82\xd3\xe4\x93\x02*\x12(/dns/v1/zones/{dns_zone_id}:getRecordSet\x12\xab\x01\n\x0eListRecordSets\x12\x31.yandex.cloud.dns.v1.ListDnsZoneRecordSetsRequest\x1a\x32.yandex.cloud.dns.v1.ListDnsZoneRecordSetsResponse\"2\x82\xd3\xe4\x93\x02,\x12*/dns/v1/zones/{dns_zone_id}:listRecordSets\x12\xc9\x01\n\x10UpdateRecordSets\x12,.yandex.cloud.dns.v1.UpdateRecordSetsRequest\x1a!.yandex.cloud.operation.Operation\"d\xb2\xd2*)\n\x18UpdateRecordSetsMetadata\x12\rRecordSetDiff\x82\xd3\xe4\x93\x02\x31\",/dns/v1/zones/{dns_zone_id}:updateRecordSets:\x01*\x12\xc9\x01\n\x10UpsertRecordSets\x12,.yandex.cloud.dns.v1.UpsertRecordSetsRequest\x1a!.yandex.cloud.operation.Operation\"d\xb2\xd2*)\n\x18UpsertRecordSetsMetadata\x12\rRecordSetDiff\x82\xd3\xe4\x93\x02\x31\",/dns/v1/zones/{dns_zone_id}:upsertRecordSets:\x01*\x12\xa7\x01\n\x0eListOperations\x12\x31.yandex.cloud.dns.v1.ListDnsZoneOperationsRequest\x1a\x32.yandex.cloud.dns.v1.ListDnsZoneOperationsResponse\".\x82\xd3\xe4\x93\x02(\x12&/dns/v1/zones/{dns_zone_id}/operations\x12\xad\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./dns/v1/zones/{resource_id}:listAccessBindings\x12\xdc\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"u\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x32\"-/dns/v1/zones/{resource_id}:setAccessBindings:\x01*\x12\xe8\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"{\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x35\"0/dns/v1/zones/{resource_id}:updateAccessBindings:\x01*\x12\xe5\x01\n\x15UpdatePrivateNetworks\x12\x38.yandex.cloud.dns.v1.UpdateDnsZonePrivateNetworksRequest\x1a!.yandex.cloud.operation.Operation\"o\xb2\xd2*/\n$UpdateDnsZonePrivateNetworksMetadata\x12\x07\x44nsZone\x82\xd3\xe4\x93\x02\x36\x32\x31/dns/v1/zones/{dns_zone_id}:updatePrivateNetworks:\x01*BV\n\x17yandex.cloud.api.dns.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/dns/v1;dnsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.dns.v1.dns_zone_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.dns.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/dns/v1;dns'
  _GETDNSZONEREQUEST.fields_by_name['dns_zone_id']._options = None
  _GETDNSZONEREQUEST.fields_by_name['dns_zone_id']._serialized_options = b'\350\3071\001'
  _LISTDNSZONESREQUEST.fields_by_name['folder_id']._options = None
  _LISTDNSZONESREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _LISTDNSZONESREQUEST.fields_by_name['page_size']._options = None
  _LISTDNSZONESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTDNSZONESREQUEST.fields_by_name['page_token']._options = None
  _LISTDNSZONESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=1000'
  _LISTDNSZONESREQUEST.fields_by_name['filter']._options = None
  _LISTDNSZONESREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _CREATEDNSZONEREQUEST_LABELSENTRY._options = None
  _CREATEDNSZONEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEDNSZONEREQUEST.fields_by_name['folder_id']._options = None
  _CREATEDNSZONEREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEDNSZONEREQUEST.fields_by_name['name']._options = None
  _CREATEDNSZONEREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _CREATEDNSZONEREQUEST.fields_by_name['description']._options = None
  _CREATEDNSZONEREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATEDNSZONEREQUEST.fields_by_name['labels']._options = None
  _CREATEDNSZONEREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _CREATEDNSZONEREQUEST.fields_by_name['zone']._options = None
  _CREATEDNSZONEREQUEST.fields_by_name['zone']._serialized_options = b'\350\3071\001\362\3071\031[.]|[a-z0-9][-a-z0-9.]*\\.\212\3101\005<=255'
  _UPDATEDNSZONEREQUEST_LABELSENTRY._options = None
  _UPDATEDNSZONEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEDNSZONEREQUEST.fields_by_name['dns_zone_id']._options = None
  _UPDATEDNSZONEREQUEST.fields_by_name['dns_zone_id']._serialized_options = b'\212\3101\00220'
  _UPDATEDNSZONEREQUEST.fields_by_name['name']._options = None
  _UPDATEDNSZONEREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _UPDATEDNSZONEREQUEST.fields_by_name['description']._options = None
  _UPDATEDNSZONEREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATEDNSZONEREQUEST.fields_by_name['labels']._options = None
  _UPDATEDNSZONEREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _DELETEDNSZONEREQUEST.fields_by_name['dns_zone_id']._options = None
  _DELETEDNSZONEREQUEST.fields_by_name['dns_zone_id']._serialized_options = b'\212\3101\00220'
  _GETDNSZONERECORDSETREQUEST.fields_by_name['dns_zone_id']._options = None
  _GETDNSZONERECORDSETREQUEST.fields_by_name['dns_zone_id']._serialized_options = b'\212\3101\00220'
  _GETDNSZONERECORDSETREQUEST.fields_by_name['name']._options = None
  _GETDNSZONERECORDSETREQUEST.fields_by_name['name']._serialized_options = b'\350\3071\001\212\3101\005<=255'
  _GETDNSZONERECORDSETREQUEST.fields_by_name['type']._options = None
  _GETDNSZONERECORDSETREQUEST.fields_by_name['type']._serialized_options = b'\350\3071\001\212\3101\004<=10'
  _LISTDNSZONERECORDSETSREQUEST.fields_by_name['dns_zone_id']._options = None
  _LISTDNSZONERECORDSETSREQUEST.fields_by_name['dns_zone_id']._serialized_options = b'\212\3101\00220'
  _LISTDNSZONERECORDSETSREQUEST.fields_by_name['page_size']._options = None
  _LISTDNSZONERECORDSETSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTDNSZONERECORDSETSREQUEST.fields_by_name['page_token']._options = None
  _LISTDNSZONERECORDSETSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=1000'
  _LISTDNSZONERECORDSETSREQUEST.fields_by_name['filter']._options = None
  _LISTDNSZONERECORDSETSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _UPDATERECORDSETSREQUEST.fields_by_name['dns_zone_id']._options = None
  _UPDATERECORDSETSREQUEST.fields_by_name['dns_zone_id']._serialized_options = b'\212\3101\00220'
  _UPDATERECORDSETSREQUEST.fields_by_name['deletions']._options = None
  _UPDATERECORDSETSREQUEST.fields_by_name['deletions']._serialized_options = b'\202\3101\006<=1000'
  _UPDATERECORDSETSREQUEST.fields_by_name['additions']._options = None
  _UPDATERECORDSETSREQUEST.fields_by_name['additions']._serialized_options = b'\202\3101\006<=1000'
  _UPSERTRECORDSETSREQUEST.fields_by_name['dns_zone_id']._options = None
  _UPSERTRECORDSETSREQUEST.fields_by_name['dns_zone_id']._serialized_options = b'\212\3101\00220'
  _UPSERTRECORDSETSREQUEST.fields_by_name['deletions']._options = None
  _UPSERTRECORDSETSREQUEST.fields_by_name['deletions']._serialized_options = b'\202\3101\006<=1000'
  _UPSERTRECORDSETSREQUEST.fields_by_name['replacements']._options = None
  _UPSERTRECORDSETSREQUEST.fields_by_name['replacements']._serialized_options = b'\202\3101\006<=1000'
  _UPSERTRECORDSETSREQUEST.fields_by_name['merges']._options = None
  _UPSERTRECORDSETSREQUEST.fields_by_name['merges']._serialized_options = b'\202\3101\006<=1000'
  _LISTDNSZONEOPERATIONSREQUEST.fields_by_name['dns_zone_id']._options = None
  _LISTDNSZONEOPERATIONSREQUEST.fields_by_name['dns_zone_id']._serialized_options = b'\212\3101\00220'
  _LISTDNSZONEOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTDNSZONEOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTDNSZONEOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTDNSZONEOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=1000'
  _LISTDNSZONEOPERATIONSREQUEST.fields_by_name['filter']._options = None
  _LISTDNSZONEOPERATIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _DNSZONESERVICE.methods_by_name['Get']._options = None
  _DNSZONESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\035\022\033/dns/v1/zones/{dns_zone_id}'
  _DNSZONESERVICE.methods_by_name['List']._options = None
  _DNSZONESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\017\022\r/dns/v1/zones'
  _DNSZONESERVICE.methods_by_name['Create']._options = None
  _DNSZONESERVICE.methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateDnsZoneMetadata\022\007DnsZone\202\323\344\223\002\022\"\r/dns/v1/zones:\001*'
  _DNSZONESERVICE.methods_by_name['Update']._options = None
  _DNSZONESERVICE.methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateDnsZoneMetadata\022\007DnsZone\202\323\344\223\002 2\033/dns/v1/zones/{dns_zone_id}:\001*'
  _DNSZONESERVICE.methods_by_name['Delete']._options = None
  _DNSZONESERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteDnsZoneMetadata\022\025google.protobuf.Empty\202\323\344\223\002\035*\033/dns/v1/zones/{dns_zone_id}'
  _DNSZONESERVICE.methods_by_name['GetRecordSet']._options = None
  _DNSZONESERVICE.methods_by_name['GetRecordSet']._serialized_options = b'\202\323\344\223\002*\022(/dns/v1/zones/{dns_zone_id}:getRecordSet'
  _DNSZONESERVICE.methods_by_name['ListRecordSets']._options = None
  _DNSZONESERVICE.methods_by_name['ListRecordSets']._serialized_options = b'\202\323\344\223\002,\022*/dns/v1/zones/{dns_zone_id}:listRecordSets'
  _DNSZONESERVICE.methods_by_name['UpdateRecordSets']._options = None
  _DNSZONESERVICE.methods_by_name['UpdateRecordSets']._serialized_options = b'\262\322*)\n\030UpdateRecordSetsMetadata\022\rRecordSetDiff\202\323\344\223\0021\",/dns/v1/zones/{dns_zone_id}:updateRecordSets:\001*'
  _DNSZONESERVICE.methods_by_name['UpsertRecordSets']._options = None
  _DNSZONESERVICE.methods_by_name['UpsertRecordSets']._serialized_options = b'\262\322*)\n\030UpsertRecordSetsMetadata\022\rRecordSetDiff\202\323\344\223\0021\",/dns/v1/zones/{dns_zone_id}:upsertRecordSets:\001*'
  _DNSZONESERVICE.methods_by_name['ListOperations']._options = None
  _DNSZONESERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002(\022&/dns/v1/zones/{dns_zone_id}/operations'
  _DNSZONESERVICE.methods_by_name['ListAccessBindings']._options = None
  _DNSZONESERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\0020\022./dns/v1/zones/{resource_id}:listAccessBindings'
  _DNSZONESERVICE.methods_by_name['SetAccessBindings']._options = None
  _DNSZONESERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\0022\"-/dns/v1/zones/{resource_id}:setAccessBindings:\001*'
  _DNSZONESERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _DNSZONESERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\0025\"0/dns/v1/zones/{resource_id}:updateAccessBindings:\001*'
  _DNSZONESERVICE.methods_by_name['UpdatePrivateNetworks']._options = None
  _DNSZONESERVICE.methods_by_name['UpdatePrivateNetworks']._serialized_options = b'\262\322*/\n$UpdateDnsZonePrivateNetworksMetadata\022\007DnsZone\202\323\344\223\002621/dns/v1/zones/{dns_zone_id}:updatePrivateNetworks:\001*'
  _globals['_UPDATEDNSZONEPRIVATENETWORKSREQUEST']._serialized_start=307
  _globals['_UPDATEDNSZONEPRIVATENETWORKSREQUEST']._serialized_end=441
  _globals['_UPDATEDNSZONEPRIVATENETWORKSMETADATA']._serialized_start=443
  _globals['_UPDATEDNSZONEPRIVATENETWORKSMETADATA']._serialized_end=502
  _globals['_GETDNSZONEREQUEST']._serialized_start=504
  _globals['_GETDNSZONEREQUEST']._serialized_end=550
  _globals['_LISTDNSZONESREQUEST']._serialized_start=553
  _globals['_LISTDNSZONESREQUEST']._serialized_end=690
  _globals['_LISTDNSZONESRESPONSE']._serialized_start=692
  _globals['_LISTDNSZONESRESPONSE']._serialized_end=788
  _globals['_CREATEDNSZONEREQUEST']._serialized_start=791
  _globals['_CREATEDNSZONEREQUEST']._serialized_end=1339
  _globals['_CREATEDNSZONEREQUEST_LABELSENTRY']._serialized_start=1294
  _globals['_CREATEDNSZONEREQUEST_LABELSENTRY']._serialized_end=1339
  _globals['_CREATEDNSZONEMETADATA']._serialized_start=1341
  _globals['_CREATEDNSZONEMETADATA']._serialized_end=1385
  _globals['_UPDATEDNSZONEREQUEST']._serialized_start=1388
  _globals['_UPDATEDNSZONEREQUEST']._serialized_end=1923
  _globals['_UPDATEDNSZONEREQUEST_LABELSENTRY']._serialized_start=1294
  _globals['_UPDATEDNSZONEREQUEST_LABELSENTRY']._serialized_end=1339
  _globals['_UPDATEDNSZONEMETADATA']._serialized_start=1925
  _globals['_UPDATEDNSZONEMETADATA']._serialized_end=1969
  _globals['_DELETEDNSZONEREQUEST']._serialized_start=1971
  _globals['_DELETEDNSZONEREQUEST']._serialized_end=2022
  _globals['_DELETEDNSZONEMETADATA']._serialized_start=2024
  _globals['_DELETEDNSZONEMETADATA']._serialized_end=2068
  _globals['_GETDNSZONERECORDSETREQUEST']._serialized_start=2070
  _globals['_GETDNSZONERECORDSETREQUEST']._serialized_end=2184
  _globals['_LISTDNSZONERECORDSETSREQUEST']._serialized_start=2187
  _globals['_LISTDNSZONERECORDSETSREQUEST']._serialized_end=2337
  _globals['_LISTDNSZONERECORDSETSRESPONSE']._serialized_start=2339
  _globals['_LISTDNSZONERECORDSETSRESPONSE']._serialized_end=2448
  _globals['_UPDATERECORDSETSREQUEST']._serialized_start=2451
  _globals['_UPDATERECORDSETSREQUEST']._serialized_end=2631
  _globals['_UPDATERECORDSETSMETADATA']._serialized_start=2633
  _globals['_UPDATERECORDSETSMETADATA']._serialized_end=2659
  _globals['_UPSERTRECORDSETSREQUEST']._serialized_start=2662
  _globals['_UPSERTRECORDSETSREQUEST']._serialized_end=2905
  _globals['_UPSERTRECORDSETSMETADATA']._serialized_start=2907
  _globals['_UPSERTRECORDSETSMETADATA']._serialized_end=2933
  _globals['_RECORDSETDIFF']._serialized_start=2935
  _globals['_RECORDSETDIFF']._serialized_end=3052
  _globals['_LISTDNSZONEOPERATIONSREQUEST']._serialized_start=3055
  _globals['_LISTDNSZONEOPERATIONSREQUEST']._serialized_end=3205
  _globals['_LISTDNSZONEOPERATIONSRESPONSE']._serialized_start=3207
  _globals['_LISTDNSZONEOPERATIONSRESPONSE']._serialized_end=3318
  _globals['_DNSZONESERVICE']._serialized_start=3321
  _globals['_DNSZONESERVICE']._serialized_end=5825
# @@protoc_insertion_point(module_scope)
