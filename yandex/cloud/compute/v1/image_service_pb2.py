# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/image_service.proto
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
from yandex.cloud.compute.v1 import hardware_generation_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_hardware__generation__pb2
from yandex.cloud.compute.v1 import image_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_image__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/compute/v1/image_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a\x31yandex/cloud/compute/v1/hardware_generation.proto\x1a#yandex/cloud/compute/v1/image.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"1\n\x0fGetImageRequest\x12\x1e\n\x08image_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"s\n\x1dGetImageLatestByFamilyRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x31\n\x06\x66\x61mily\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\"\xab\x01\n\x11ListImagesRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"]\n\x12ListImagesResponse\x12.\n\x06images\x18\x01 \x03(\x0b\x32\x1e.yandex.cloud.compute.v1.Image\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xcf\x05\n\x12\x43reateImageRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x32\n\x04name\x18\x02 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8c\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x37.yandex.cloud.compute.v1.CreateImageRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\x31\n\x06\x66\x61mily\x18\x05 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x30\n\rmin_disk_size\x18\x06 \x01(\x03\x42\x19\xfa\xc7\x31\x15\x34\x31\x39\x34\x33\x30\x34-4398046511104\x12\x1d\n\x0bproduct_ids\x18\x07 \x03(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1c\n\x08image_id\x18\x08 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x1b\n\x07\x64isk_id\x18\t \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x1f\n\x0bsnapshot_id\x18\n \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\r\n\x03uri\x18\x0b \x01(\tH\x00\x12\'\n\x02os\x18\x0c \x01(\x0b\x32\x1b.yandex.cloud.compute.v1.Os\x12\x0e\n\x06pooled\x18\x11 \x01(\x08\x12H\n\x13hardware_generation\x18\x12 \x01(\x0b\x32+.yandex.cloud.compute.v1.HardwareGeneration\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0e\n\x06source\x12\x04\xc0\xc1\x31\x01J\x04\x08\r\x10\x11\"\'\n\x13\x43reateImageMetadata\x12\x10\n\x08image_id\x18\x01 \x01(\t\"\xa9\x03\n\x12UpdateImageRequest\x12\x1e\n\x08image_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x30\n\rmin_disk_size\x18\x05 \x01(\x03\x42\x19\xfa\xc7\x31\x15\x34\x31\x39\x34\x33\x30\x34-4398046511104\x12\x8c\x01\n\x06labels\x18\x06 \x03(\x0b\x32\x37.yandex.cloud.compute.v1.UpdateImageRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\'\n\x13UpdateImageMetadata\x12\x10\n\x08image_id\x18\x01 \x01(\t\"4\n\x12\x44\x65leteImageRequest\x12\x1e\n\x08image_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\'\n\x13\x44\x65leteImageMetadata\x12\x10\n\x08image_id\x18\x01 \x01(\t\"z\n\x1aListImageOperationsRequest\x12\x1e\n\x08image_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"m\n\x1bListImageOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe6\r\n\x0cImageService\x12v\n\x03Get\x12(.yandex.cloud.compute.v1.GetImageRequest\x1a\x1e.yandex.cloud.compute.v1.Image\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/compute/v1/images/{image_id}\x12\x96\x01\n\x11GetLatestByFamily\x12\x36.yandex.cloud.compute.v1.GetImageLatestByFamilyRequest\x1a\x1e.yandex.cloud.compute.v1.Image\")\x82\xd3\xe4\x93\x02#\x12!/compute/v1/images:latestByFamily\x12{\n\x04List\x12*.yandex.cloud.compute.v1.ListImagesRequest\x1a+.yandex.cloud.compute.v1.ListImagesResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/compute/v1/images\x12\x97\x01\n\x06\x43reate\x12+.yandex.cloud.compute.v1.CreateImageRequest\x1a!.yandex.cloud.operation.Operation\"=\xb2\xd2*\x1c\n\x13\x43reateImageMetadata\x12\x05Image\x82\xd3\xe4\x93\x02\x17\"\x12/compute/v1/images:\x01*\x12\xa2\x01\n\x06Update\x12+.yandex.cloud.compute.v1.UpdateImageRequest\x1a!.yandex.cloud.operation.Operation\"H\xb2\xd2*\x1c\n\x13UpdateImageMetadata\x12\x05Image\x82\xd3\xe4\x93\x02\"2\x1d/compute/v1/images/{image_id}:\x01*\x12\xaf\x01\n\x06\x44\x65lete\x12+.yandex.cloud.compute.v1.DeleteImageRequest\x1a!.yandex.cloud.operation.Operation\"U\xb2\xd2*,\n\x13\x44\x65leteImageMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1f*\x1d/compute/v1/images/{image_id}\x12\xad\x01\n\x0eListOperations\x12\x33.yandex.cloud.compute.v1.ListImageOperationsRequest\x1a\x34.yandex.cloud.compute.v1.ListImageOperationsResponse\"0\x82\xd3\xe4\x93\x02*\x12(/compute/v1/images/{image_id}/operations\x12\xb2\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/compute/v1/images/{resource_id}:listAccessBindings\x12\xf1\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x89\x01\xb2\xd2*H\n access.SetAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02\x37\"2/compute/v1/images/{resource_id}:setAccessBindings:\x01*\x12\xfd\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8f\x01\xb2\xd2*K\n#access.UpdateAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02:\"5/compute/v1/images/{resource_id}:updateAccessBindings:\x01*Bb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.image_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _GETIMAGEREQUEST.fields_by_name['image_id']._options = None
  _GETIMAGEREQUEST.fields_by_name['image_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GETIMAGELATESTBYFAMILYREQUEST.fields_by_name['folder_id']._options = None
  _GETIMAGELATESTBYFAMILYREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GETIMAGELATESTBYFAMILYREQUEST.fields_by_name['family']._options = None
  _GETIMAGELATESTBYFAMILYREQUEST.fields_by_name['family']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _LISTIMAGESREQUEST.fields_by_name['folder_id']._options = None
  _LISTIMAGESREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTIMAGESREQUEST.fields_by_name['page_size']._options = None
  _LISTIMAGESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTIMAGESREQUEST.fields_by_name['page_token']._options = None
  _LISTIMAGESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTIMAGESREQUEST.fields_by_name['filter']._options = None
  _LISTIMAGESREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTIMAGESREQUEST.fields_by_name['order_by']._options = None
  _LISTIMAGESREQUEST.fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _CREATEIMAGEREQUEST_LABELSENTRY._options = None
  _CREATEIMAGEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEIMAGEREQUEST.oneofs_by_name['source']._options = None
  _CREATEIMAGEREQUEST.oneofs_by_name['source']._serialized_options = b'\300\3011\001'
  _CREATEIMAGEREQUEST.fields_by_name['folder_id']._options = None
  _CREATEIMAGEREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEIMAGEREQUEST.fields_by_name['name']._options = None
  _CREATEIMAGEREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _CREATEIMAGEREQUEST.fields_by_name['description']._options = None
  _CREATEIMAGEREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATEIMAGEREQUEST.fields_by_name['labels']._options = None
  _CREATEIMAGEREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _CREATEIMAGEREQUEST.fields_by_name['family']._options = None
  _CREATEIMAGEREQUEST.fields_by_name['family']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _CREATEIMAGEREQUEST.fields_by_name['min_disk_size']._options = None
  _CREATEIMAGEREQUEST.fields_by_name['min_disk_size']._serialized_options = b'\372\3071\0254194304-4398046511104'
  _CREATEIMAGEREQUEST.fields_by_name['product_ids']._options = None
  _CREATEIMAGEREQUEST.fields_by_name['product_ids']._serialized_options = b'\212\3101\004<=50'
  _CREATEIMAGEREQUEST.fields_by_name['image_id']._options = None
  _CREATEIMAGEREQUEST.fields_by_name['image_id']._serialized_options = b'\212\3101\004<=50'
  _CREATEIMAGEREQUEST.fields_by_name['disk_id']._options = None
  _CREATEIMAGEREQUEST.fields_by_name['disk_id']._serialized_options = b'\212\3101\004<=50'
  _CREATEIMAGEREQUEST.fields_by_name['snapshot_id']._options = None
  _CREATEIMAGEREQUEST.fields_by_name['snapshot_id']._serialized_options = b'\212\3101\004<=50'
  _UPDATEIMAGEREQUEST_LABELSENTRY._options = None
  _UPDATEIMAGEREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEIMAGEREQUEST.fields_by_name['image_id']._options = None
  _UPDATEIMAGEREQUEST.fields_by_name['image_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEIMAGEREQUEST.fields_by_name['name']._options = None
  _UPDATEIMAGEREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _UPDATEIMAGEREQUEST.fields_by_name['description']._options = None
  _UPDATEIMAGEREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATEIMAGEREQUEST.fields_by_name['min_disk_size']._options = None
  _UPDATEIMAGEREQUEST.fields_by_name['min_disk_size']._serialized_options = b'\372\3071\0254194304-4398046511104'
  _UPDATEIMAGEREQUEST.fields_by_name['labels']._options = None
  _UPDATEIMAGEREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _DELETEIMAGEREQUEST.fields_by_name['image_id']._options = None
  _DELETEIMAGEREQUEST.fields_by_name['image_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTIMAGEOPERATIONSREQUEST.fields_by_name['image_id']._options = None
  _LISTIMAGEOPERATIONSREQUEST.fields_by_name['image_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTIMAGEOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTIMAGEOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTIMAGEOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTIMAGEOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _IMAGESERVICE.methods_by_name['Get']._options = None
  _IMAGESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\037\022\035/compute/v1/images/{image_id}'
  _IMAGESERVICE.methods_by_name['GetLatestByFamily']._options = None
  _IMAGESERVICE.methods_by_name['GetLatestByFamily']._serialized_options = b'\202\323\344\223\002#\022!/compute/v1/images:latestByFamily'
  _IMAGESERVICE.methods_by_name['List']._options = None
  _IMAGESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\024\022\022/compute/v1/images'
  _IMAGESERVICE.methods_by_name['Create']._options = None
  _IMAGESERVICE.methods_by_name['Create']._serialized_options = b'\262\322*\034\n\023CreateImageMetadata\022\005Image\202\323\344\223\002\027\"\022/compute/v1/images:\001*'
  _IMAGESERVICE.methods_by_name['Update']._options = None
  _IMAGESERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\034\n\023UpdateImageMetadata\022\005Image\202\323\344\223\002\"2\035/compute/v1/images/{image_id}:\001*'
  _IMAGESERVICE.methods_by_name['Delete']._options = None
  _IMAGESERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*,\n\023DeleteImageMetadata\022\025google.protobuf.Empty\202\323\344\223\002\037*\035/compute/v1/images/{image_id}'
  _IMAGESERVICE.methods_by_name['ListOperations']._options = None
  _IMAGESERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002*\022(/compute/v1/images/{image_id}/operations'
  _IMAGESERVICE.methods_by_name['ListAccessBindings']._options = None
  _IMAGESERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\0025\0223/compute/v1/images/{resource_id}:listAccessBindings'
  _IMAGESERVICE.methods_by_name['SetAccessBindings']._options = None
  _IMAGESERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*H\n access.SetAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\0027\"2/compute/v1/images/{resource_id}:setAccessBindings:\001*'
  _IMAGESERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _IMAGESERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*K\n#access.UpdateAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002:\"5/compute/v1/images/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETIMAGEREQUEST']._serialized_start=363
  _globals['_GETIMAGEREQUEST']._serialized_end=412
  _globals['_GETIMAGELATESTBYFAMILYREQUEST']._serialized_start=414
  _globals['_GETIMAGELATESTBYFAMILYREQUEST']._serialized_end=529
  _globals['_LISTIMAGESREQUEST']._serialized_start=532
  _globals['_LISTIMAGESREQUEST']._serialized_end=703
  _globals['_LISTIMAGESRESPONSE']._serialized_start=705
  _globals['_LISTIMAGESRESPONSE']._serialized_end=798
  _globals['_CREATEIMAGEREQUEST']._serialized_start=801
  _globals['_CREATEIMAGEREQUEST']._serialized_end=1520
  _globals['_CREATEIMAGEREQUEST_LABELSENTRY']._serialized_start=1453
  _globals['_CREATEIMAGEREQUEST_LABELSENTRY']._serialized_end=1498
  _globals['_CREATEIMAGEMETADATA']._serialized_start=1522
  _globals['_CREATEIMAGEMETADATA']._serialized_end=1561
  _globals['_UPDATEIMAGEREQUEST']._serialized_start=1564
  _globals['_UPDATEIMAGEREQUEST']._serialized_end=1989
  _globals['_UPDATEIMAGEREQUEST_LABELSENTRY']._serialized_start=1453
  _globals['_UPDATEIMAGEREQUEST_LABELSENTRY']._serialized_end=1498
  _globals['_UPDATEIMAGEMETADATA']._serialized_start=1991
  _globals['_UPDATEIMAGEMETADATA']._serialized_end=2030
  _globals['_DELETEIMAGEREQUEST']._serialized_start=2032
  _globals['_DELETEIMAGEREQUEST']._serialized_end=2084
  _globals['_DELETEIMAGEMETADATA']._serialized_start=2086
  _globals['_DELETEIMAGEMETADATA']._serialized_end=2125
  _globals['_LISTIMAGEOPERATIONSREQUEST']._serialized_start=2127
  _globals['_LISTIMAGEOPERATIONSREQUEST']._serialized_end=2249
  _globals['_LISTIMAGEOPERATIONSRESPONSE']._serialized_start=2251
  _globals['_LISTIMAGEOPERATIONSRESPONSE']._serialized_end=2360
  _globals['_IMAGESERVICE']._serialized_start=2363
  _globals['_IMAGESERVICE']._serialized_end=4129
# @@protoc_insertion_point(module_scope)
