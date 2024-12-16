# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/containerregistry/v1/scanner_service.proto
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
    'yandex/cloud/containerregistry/v1/scanner_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.containerregistry.v1 import scanner_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_scanner__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7yandex/cloud/containerregistry/v1/scanner_service.proto\x12!yandex.cloud.containerregistry.v1\x1a yandex/cloud/api/operation.proto\x1a/yandex/cloud/containerregistry/v1/scanner.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\"-\n\x0bScanRequest\x12\x1e\n\x08image_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"&\n\x0cScanMetadata\x12\x16\n\x0escan_result_id\x18\x01 \x01(\t\"<\n\x14GetScanResultRequest\x12$\n\x0escan_result_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"6\n\x18GetLastScanResultRequest\x12\x1a\n\x08image_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"\xdc\x01\n\x16ListScanResultsRequest\x12\x1c\n\x08image_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12!\n\rrepository_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x1d\n\tpage_size\x18\x03 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x05 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x06 \x01(\tB\t\x8a\xc8\x31\x05<=100B\n\n\x02id\x12\x04\xc0\xc1\x31\x01\"w\n\x17ListScanResultsResponse\x12\x43\n\x0cscan_results\x18\x01 \x03(\x0b\x32-.yandex.cloud.containerregistry.v1.ScanResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xb9\x01\n\x1aListVulnerabilitiesRequest\x12$\n\x0escan_result_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x81\x01\n\x1bListVulnerabilitiesResponse\x12I\n\x0fvulnerabilities\x18\x01 \x03(\x0b\x32\x30.yandex.cloud.containerregistry.v1.Vulnerability\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x9b\x07\n\x0eScannerService\x12\xa0\x01\n\x04Scan\x12..yandex.cloud.containerregistry.v1.ScanRequest\x1a!.yandex.cloud.operation.Operation\"E\xb2\xd2*\x1a\n\x0cScanMetadata\x12\nScanResult\x82\xd3\xe4\x93\x02!\"\x1c/container-registry/v1/scans:\x01*\x12\xa4\x01\n\x03Get\x12\x37.yandex.cloud.containerregistry.v1.GetScanResultRequest\x1a-.yandex.cloud.containerregistry.v1.ScanResult\"5\x82\xd3\xe4\x93\x02/\x12-/container-registry/v1/scans/{scan_result_id}\x12\xb6\x01\n\x07GetLast\x12;.yandex.cloud.containerregistry.v1.GetLastScanResultRequest\x1a-.yandex.cloud.containerregistry.v1.ScanResult\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/container-registry/v1/images/{image_id}:lastScanResult\x12\xa3\x01\n\x04List\x12\x39.yandex.cloud.containerregistry.v1.ListScanResultsRequest\x1a:.yandex.cloud.containerregistry.v1.ListScanResultsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/container-registry/v1/scans\x12\xdf\x01\n\x13ListVulnerabilities\x12=.yandex.cloud.containerregistry.v1.ListVulnerabilitiesRequest\x1a>.yandex.cloud.containerregistry.v1.ListVulnerabilitiesResponse\"I\x82\xd3\xe4\x93\x02\x43\x12\x41/container-registry/v1/scans/{scan_result_id}:listVulnerabilitiesB\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.containerregistry.v1.scanner_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry'
  _globals['_SCANREQUEST'].fields_by_name['image_id']._loaded_options = None
  _globals['_SCANREQUEST'].fields_by_name['image_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETSCANRESULTREQUEST'].fields_by_name['scan_result_id']._loaded_options = None
  _globals['_GETSCANRESULTREQUEST'].fields_by_name['scan_result_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_GETLASTSCANRESULTREQUEST'].fields_by_name['image_id']._loaded_options = None
  _globals['_GETLASTSCANRESULTREQUEST'].fields_by_name['image_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTSCANRESULTSREQUEST'].oneofs_by_name['id']._loaded_options = None
  _globals['_LISTSCANRESULTSREQUEST'].oneofs_by_name['id']._serialized_options = b'\300\3011\001'
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['image_id']._loaded_options = None
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['image_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['repository_id']._loaded_options = None
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['repository_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTSCANRESULTSREQUEST'].fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTVULNERABILITIESREQUEST'].fields_by_name['scan_result_id']._loaded_options = None
  _globals['_LISTVULNERABILITIESREQUEST'].fields_by_name['scan_result_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTVULNERABILITIESREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTVULNERABILITIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTVULNERABILITIESREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTVULNERABILITIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTVULNERABILITIESREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTVULNERABILITIESREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_LISTVULNERABILITIESREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTVULNERABILITIESREQUEST'].fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _globals['_SCANNERSERVICE'].methods_by_name['Scan']._loaded_options = None
  _globals['_SCANNERSERVICE'].methods_by_name['Scan']._serialized_options = b'\262\322*\032\n\014ScanMetadata\022\nScanResult\202\323\344\223\002!\"\034/container-registry/v1/scans:\001*'
  _globals['_SCANNERSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_SCANNERSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002/\022-/container-registry/v1/scans/{scan_result_id}'
  _globals['_SCANNERSERVICE'].methods_by_name['GetLast']._loaded_options = None
  _globals['_SCANNERSERVICE'].methods_by_name['GetLast']._serialized_options = b'\202\323\344\223\0029\0227/container-registry/v1/images/{image_id}:lastScanResult'
  _globals['_SCANNERSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_SCANNERSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\036\022\034/container-registry/v1/scans'
  _globals['_SCANNERSERVICE'].methods_by_name['ListVulnerabilities']._loaded_options = None
  _globals['_SCANNERSERVICE'].methods_by_name['ListVulnerabilities']._serialized_options = b'\202\323\344\223\002C\022A/container-registry/v1/scans/{scan_result_id}:listVulnerabilities'
  _globals['_SCANREQUEST']._serialized_start=278
  _globals['_SCANREQUEST']._serialized_end=323
  _globals['_SCANMETADATA']._serialized_start=325
  _globals['_SCANMETADATA']._serialized_end=363
  _globals['_GETSCANRESULTREQUEST']._serialized_start=365
  _globals['_GETSCANRESULTREQUEST']._serialized_end=425
  _globals['_GETLASTSCANRESULTREQUEST']._serialized_start=427
  _globals['_GETLASTSCANRESULTREQUEST']._serialized_end=481
  _globals['_LISTSCANRESULTSREQUEST']._serialized_start=484
  _globals['_LISTSCANRESULTSREQUEST']._serialized_end=704
  _globals['_LISTSCANRESULTSRESPONSE']._serialized_start=706
  _globals['_LISTSCANRESULTSRESPONSE']._serialized_end=825
  _globals['_LISTVULNERABILITIESREQUEST']._serialized_start=828
  _globals['_LISTVULNERABILITIESREQUEST']._serialized_end=1013
  _globals['_LISTVULNERABILITIESRESPONSE']._serialized_start=1016
  _globals['_LISTVULNERABILITIESRESPONSE']._serialized_end=1145
  _globals['_SCANNERSERVICE']._serialized_start=1148
  _globals['_SCANNERSERVICE']._serialized_end=2071
# @@protoc_insertion_point(module_scope)
