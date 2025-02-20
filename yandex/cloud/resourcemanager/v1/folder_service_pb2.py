# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/resourcemanager/v1/folder_service.proto
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
    'yandex/cloud/resourcemanager/v1/folder_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.resourcemanager.v1 import folder_pb2 as yandex_dot_cloud_dot_resourcemanager_dot_v1_dot_folder__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4yandex/cloud/resourcemanager/v1/folder_service.proto\x12\x1fyandex.cloud.resourcemanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a yandex/cloud/api/operation.proto\x1a,yandex/cloud/resourcemanager/v1/folder.proto\x1a yandex/cloud/access/access.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"3\n\x10GetFolderRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x8f\x01\n\x12ListFoldersRequest\x12\x1e\n\x08\x63loud_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"h\n\x13ListFoldersResponse\x12\x38\n\x07\x66olders\x18\x01 \x03(\x0b\x32\'.yandex.cloud.resourcemanager.v1.Folder\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc9\x02\n\x13\x43reateFolderRequest\x12\x1e\n\x08\x63loud_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x33\n\x04name\x18\x02 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8d\x01\n\x06labels\x18\x04 \x03(\x0b\x32@.yandex.cloud.resourcemanager.v1.CreateFolderRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\x14\x43reateFolderMetadata\x12\x11\n\tfolder_id\x18\x01 \x01(\t\"\xfb\x02\n\x13UpdateFolderRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x33\n\x04name\x18\x03 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8d\x01\n\x06labels\x18\x05 \x03(\x0b\x32@.yandex.cloud.resourcemanager.v1.UpdateFolderRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\x14UpdateFolderMetadata\x12\x11\n\tfolder_id\x18\x01 \x01(\t\"h\n\x13\x44\x65leteFolderRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\x0c\x64\x65lete_after\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa3\x01\n\x14\x44\x65leteFolderMetadata\x12\x11\n\tfolder_id\x18\x01 \x01(\t\x12\x30\n\x0c\x64\x65lete_after\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0c\x63\x61ncelled_by\x18\x03 \x01(\t\x12\x30\n\x0c\x63\x61ncelled_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"}\n\x1bListFolderOperationsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=2000\"n\n\x1cListFolderOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x84\x0e\n\rFolderService\x12\x93\x01\n\x03Get\x12\x31.yandex.cloud.resourcemanager.v1.GetFolderRequest\x1a\'.yandex.cloud.resourcemanager.v1.Folder\"0\x82\xd3\xe4\x93\x02*\x12(/resource-manager/v1/folders/{folder_id}\x12\x97\x01\n\x04List\x12\x33.yandex.cloud.resourcemanager.v1.ListFoldersRequest\x1a\x34.yandex.cloud.resourcemanager.v1.ListFoldersResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/resource-manager/v1/folders\x12\xac\x01\n\x06\x43reate\x12\x34.yandex.cloud.resourcemanager.v1.CreateFolderRequest\x1a!.yandex.cloud.operation.Operation\"I\xb2\xd2*\x1e\n\x14\x43reateFolderMetadata\x12\x06\x46older\x82\xd3\xe4\x93\x02!\"\x1c/resource-manager/v1/folders:\x01*\x12\xb8\x01\n\x06Update\x12\x34.yandex.cloud.resourcemanager.v1.UpdateFolderRequest\x1a!.yandex.cloud.operation.Operation\"U\xb2\xd2*\x1e\n\x14UpdateFolderMetadata\x12\x06\x46older\x82\xd3\xe4\x93\x02-2(/resource-manager/v1/folders/{folder_id}:\x01*\x12\xc4\x01\n\x06\x44\x65lete\x12\x34.yandex.cloud.resourcemanager.v1.DeleteFolderRequest\x1a!.yandex.cloud.operation.Operation\"a\xb2\xd2*-\n\x14\x44\x65leteFolderMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02**(/resource-manager/v1/folders/{folder_id}\x12\xca\x01\n\x0eListOperations\x12<.yandex.cloud.resourcemanager.v1.ListFolderOperationsRequest\x1a=.yandex.cloud.resourcemanager.v1.ListFolderOperationsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/resource-manager/v1/folders/{folder_id}/operations\x12\xbc\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"E\x82\xd3\xe4\x93\x02?\x12=/resource-manager/v1/folders/{resource_id}:listAccessBindings\x12\xfb\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x93\x01\xb2\xd2*H\n access.SetAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02\x41\"</resource-manager/v1/folders/{resource_id}:setAccessBindings:\x01*\x12\x87\x02\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x99\x01\xb2\xd2*K\n#access.UpdateAccessBindingsMetadata\x12$access.AccessBindingsOperationResult\x82\xd3\xe4\x93\x02\x44\"?/resource-manager/v1/folders/{resource_id}:updateAccessBindings:\x01*Bz\n#yandex.cloud.api.resourcemanager.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1;resourcemanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.resourcemanager.v1.folder_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#yandex.cloud.api.resourcemanager.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1;resourcemanager'
  _globals['_GETFOLDERREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_GETFOLDERREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTFOLDERSREQUEST'].fields_by_name['cloud_id']._loaded_options = None
  _globals['_LISTFOLDERSREQUEST'].fields_by_name['cloud_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTFOLDERSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTFOLDERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTFOLDERSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTFOLDERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _globals['_LISTFOLDERSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTFOLDERSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATEFOLDERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEFOLDERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEFOLDERREQUEST'].fields_by_name['cloud_id']._loaded_options = None
  _globals['_CREATEFOLDERREQUEST'].fields_by_name['cloud_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEFOLDERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEFOLDERREQUEST'].fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_CREATEFOLDERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATEFOLDERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATEFOLDERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATEFOLDERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_UPDATEFOLDERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEFOLDERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEFOLDERREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_UPDATEFOLDERREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEFOLDERREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEFOLDERREQUEST'].fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _globals['_UPDATEFOLDERREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEFOLDERREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEFOLDERREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEFOLDERREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _globals['_DELETEFOLDERREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_DELETEFOLDERREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTFOLDEROPERATIONSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTFOLDEROPERATIONSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTFOLDEROPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTFOLDEROPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTFOLDEROPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTFOLDEROPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\006<=2000'
  _globals['_FOLDERSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_FOLDERSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002*\022(/resource-manager/v1/folders/{folder_id}'
  _globals['_FOLDERSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_FOLDERSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\036\022\034/resource-manager/v1/folders'
  _globals['_FOLDERSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_FOLDERSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*\036\n\024CreateFolderMetadata\022\006Folder\202\323\344\223\002!\"\034/resource-manager/v1/folders:\001*'
  _globals['_FOLDERSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_FOLDERSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*\036\n\024UpdateFolderMetadata\022\006Folder\202\323\344\223\002-2(/resource-manager/v1/folders/{folder_id}:\001*'
  _globals['_FOLDERSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_FOLDERSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*-\n\024DeleteFolderMetadata\022\025google.protobuf.Empty\202\323\344\223\002**(/resource-manager/v1/folders/{folder_id}'
  _globals['_FOLDERSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_FOLDERSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0025\0223/resource-manager/v1/folders/{folder_id}/operations'
  _globals['_FOLDERSERVICE'].methods_by_name['ListAccessBindings']._loaded_options = None
  _globals['_FOLDERSERVICE'].methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002?\022=/resource-manager/v1/folders/{resource_id}:listAccessBindings'
  _globals['_FOLDERSERVICE'].methods_by_name['SetAccessBindings']._loaded_options = None
  _globals['_FOLDERSERVICE'].methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*H\n access.SetAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002A\"</resource-manager/v1/folders/{resource_id}:setAccessBindings:\001*'
  _globals['_FOLDERSERVICE'].methods_by_name['UpdateAccessBindings']._loaded_options = None
  _globals['_FOLDERSERVICE'].methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*K\n#access.UpdateAccessBindingsMetadata\022$access.AccessBindingsOperationResult\202\323\344\223\002D\"?/resource-manager/v1/folders/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETFOLDERREQUEST']._serialized_start=371
  _globals['_GETFOLDERREQUEST']._serialized_end=422
  _globals['_LISTFOLDERSREQUEST']._serialized_start=425
  _globals['_LISTFOLDERSREQUEST']._serialized_end=568
  _globals['_LISTFOLDERSRESPONSE']._serialized_start=570
  _globals['_LISTFOLDERSRESPONSE']._serialized_end=674
  _globals['_CREATEFOLDERREQUEST']._serialized_start=677
  _globals['_CREATEFOLDERREQUEST']._serialized_end=1006
  _globals['_CREATEFOLDERREQUEST_LABELSENTRY']._serialized_start=961
  _globals['_CREATEFOLDERREQUEST_LABELSENTRY']._serialized_end=1006
  _globals['_CREATEFOLDERMETADATA']._serialized_start=1008
  _globals['_CREATEFOLDERMETADATA']._serialized_end=1049
  _globals['_UPDATEFOLDERREQUEST']._serialized_start=1052
  _globals['_UPDATEFOLDERREQUEST']._serialized_end=1431
  _globals['_UPDATEFOLDERREQUEST_LABELSENTRY']._serialized_start=961
  _globals['_UPDATEFOLDERREQUEST_LABELSENTRY']._serialized_end=1006
  _globals['_UPDATEFOLDERMETADATA']._serialized_start=1433
  _globals['_UPDATEFOLDERMETADATA']._serialized_end=1474
  _globals['_DELETEFOLDERREQUEST']._serialized_start=1476
  _globals['_DELETEFOLDERREQUEST']._serialized_end=1580
  _globals['_DELETEFOLDERMETADATA']._serialized_start=1583
  _globals['_DELETEFOLDERMETADATA']._serialized_end=1746
  _globals['_LISTFOLDEROPERATIONSREQUEST']._serialized_start=1748
  _globals['_LISTFOLDEROPERATIONSREQUEST']._serialized_end=1873
  _globals['_LISTFOLDEROPERATIONSRESPONSE']._serialized_start=1875
  _globals['_LISTFOLDEROPERATIONSRESPONSE']._serialized_end=1985
  _globals['_FOLDERSERVICE']._serialized_start=1988
  _globals['_FOLDERSERVICE']._serialized_end=3784
# @@protoc_insertion_point(module_scope)
