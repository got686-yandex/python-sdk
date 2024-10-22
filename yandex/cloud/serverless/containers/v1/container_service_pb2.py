# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/containers/v1/container_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.serverless.containers.v1 import container_pb2 as yandex_dot_cloud_dot_serverless_dot_containers_dot_v1_dot_container__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=yandex/cloud/serverless/containers/v1/container_service.proto\x12%yandex.cloud.serverless.containers.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x35yandex/cloud/serverless/containers/v1/container.proto\x1a\x1dyandex/cloud/validation.proto\"1\n\x13GetContainerRequest\x12\x1a\n\x0c\x63ontainer_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"g\n\x15ListContainersRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\"w\n\x16ListContainersResponse\x12\x44\n\ncontainers\x18\x01 \x03(\x0b\x32\x30.yandex.cloud.serverless.containers.v1.Container\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xd2\x02\n\x16\x43reateContainerRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x9e\x01\n\x06labels\x18\x04 \x03(\x0b\x32I.yandex.cloud.serverless.containers.v1.CreateContainerRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"/\n\x17\x43reateContainerMetadata\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\"\x86\x03\n\x16UpdateContainerRequest\x12\x1a\n\x0c\x63ontainer_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x9e\x01\n\x06labels\x18\x05 \x03(\x0b\x32I.yandex.cloud.serverless.containers.v1.UpdateContainerRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"/\n\x17UpdateContainerMetadata\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\"4\n\x16\x44\x65leteContainerRequest\x12\x1a\n\x0c\x63ontainer_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"/\n\x17\x44\x65leteContainerMetadata\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\"B\n\x1bGetContainerRevisionRequest\x12#\n\x15\x63ontainer_revision_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\xb3\x01\n\x1eListContainersRevisionsRequest\x12\x13\n\tfolder_id\x18\x01 \x01(\tH\x00\x12\x16\n\x0c\x63ontainer_id\x18\x02 \x01(\tH\x00\x12\x1d\n\tpage_size\x18\x03 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x05 \x01(\tB\n\x8a\xc8\x31\x06<=1000B\n\n\x02id\x12\x04\xc0\xc1\x31\x01\"~\n\x1fListContainersRevisionsResponse\x12\x42\n\trevisions\x18\x01 \x03(\x0b\x32/.yandex.cloud.serverless.containers.v1.Revision\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xe7\x06\n\x1e\x44\x65ployContainerRevisionRequest\x12\x1a\n\x0c\x63ontainer_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12I\n\tresources\x18\x05 \x01(\x0b\x32\x30.yandex.cloud.serverless.containers.v1.ResourcesB\x04\xe8\xc7\x31\x01\x12\x42\n\x11\x65xecution_timeout\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xfa\xc7\x31\x08\x30s-3600s\x12\x1a\n\x12service_account_id\x18\x07 \x01(\t\x12J\n\nimage_spec\x18\x08 \x01(\x0b\x32\x30.yandex.cloud.serverless.containers.v1.ImageSpecB\x04\xe8\xc7\x31\x01\x12\x13\n\x0b\x63oncurrency\x18\t \x01(\x03\x12>\n\x07secrets\x18\n \x03(\x0b\x32-.yandex.cloud.serverless.containers.v1.Secret\x12I\n\x0c\x63onnectivity\x18\x0b \x01(\x0b\x32\x33.yandex.cloud.serverless.containers.v1.Connectivity\x12P\n\x10provision_policy\x18\x0c \x01(\x0b\x32\x36.yandex.cloud.serverless.containers.v1.ProvisionPolicy\x12L\n\x0escaling_policy\x18\r \x01(\x0b\x32\x34.yandex.cloud.serverless.containers.v1.ScalingPolicy\x12\x46\n\x0blog_options\x18\x0e \x01(\x0b\x32\x31.yandex.cloud.serverless.containers.v1.LogOptions\x12K\n\x0estorage_mounts\x18\x0f \x03(\x0b\x32\x33.yandex.cloud.serverless.containers.v1.StorageMount\x12<\n\x06mounts\x18\x10 \x03(\x0b\x32,.yandex.cloud.serverless.containers.v1.MountJ\x04\x08\x04\x10\x05J\x04\x08\x02\x10\x03\"\xe8\x02\n\tImageSpec\x12\x17\n\timage_url\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12?\n\x07\x63ommand\x18\x02 \x01(\x0b\x32..yandex.cloud.serverless.containers.v1.Command\x12\x39\n\x04\x61rgs\x18\x03 \x01(\x0b\x32+.yandex.cloud.serverless.containers.v1.Args\x12}\n\x0b\x65nvironment\x18\x04 \x03(\x0b\x32\x41.yandex.cloud.serverless.containers.v1.ImageSpec.EnvironmentEntryB%\x8a\xc8\x31\x06<=4096\xb2\xc8\x31\x17\x12\x15[a-zA-Z][a-zA-Z0-9_]*\x12\x13\n\x0bworking_dir\x18\x05 \x01(\t\x1a\x32\n\x10\x45nvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"@\n\x1f\x44\x65ployContainerRevisionMetadata\x12\x1d\n\x15\x63ontainer_revision_id\x18\x01 \x01(\t\"Q\n\x18RollbackContainerRequest\x12\x1a\n\x0c\x63ontainer_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x19\n\x0brevision_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"F\n\x19RollbackContainerMetadata\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\t\x12\x13\n\x0brevision_id\x18\x02 \x01(\t\"\x96\x01\n\x1eListContainerOperationsRequest\x12\x1a\n\x0c\x63ontainer_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"q\n\x1fListContainerOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xed\x14\n\x10\x43ontainerService\x12\xa5\x01\n\x03Get\x12:.yandex.cloud.serverless.containers.v1.GetContainerRequest\x1a\x30.yandex.cloud.serverless.containers.v1.Container\"0\x82\xd3\xe4\x93\x02*\x12(/containers/v1/containers/{container_id}\x12\xa6\x01\n\x04List\x12<.yandex.cloud.serverless.containers.v1.ListContainersRequest\x1a=.yandex.cloud.serverless.containers.v1.ListContainersResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/containers/v1/containers\x12\xb8\x01\n\x06\x43reate\x12=.yandex.cloud.serverless.containers.v1.CreateContainerRequest\x1a!.yandex.cloud.operation.Operation\"L\xb2\xd2*$\n\x17\x43reateContainerMetadata\x12\tContainer\x82\xd3\xe4\x93\x02\x1e\"\x19/containers/v1/containers:\x01*\x12\xc7\x01\n\x06Update\x12=.yandex.cloud.serverless.containers.v1.UpdateContainerRequest\x1a!.yandex.cloud.operation.Operation\"[\xb2\xd2*$\n\x17UpdateContainerMetadata\x12\tContainer\x82\xd3\xe4\x93\x02-2(/containers/v1/containers/{container_id}:\x01*\x12\xd0\x01\n\x06\x44\x65lete\x12=.yandex.cloud.serverless.containers.v1.DeleteContainerRequest\x1a!.yandex.cloud.operation.Operation\"d\xb2\xd2*0\n\x17\x44\x65leteContainerMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02**(/containers/v1/containers/{container_id}\x12\xd5\x01\n\x0e\x44\x65ployRevision\x12\x45.yandex.cloud.serverless.containers.v1.DeployContainerRevisionRequest\x1a!.yandex.cloud.operation.Operation\"Y\xb2\xd2*+\n\x1f\x44\x65ployContainerRevisionMetadata\x12\x08Revision\x82\xd3\xe4\x93\x02$\"\x1f/containers/v1/revisions:deploy:\x01*\x12\xd6\x01\n\x08Rollback\x12?.yandex.cloud.serverless.containers.v1.RollbackContainerRequest\x1a!.yandex.cloud.operation.Operation\"f\xb2\xd2*&\n\x19RollbackContainerMetadata\x12\tContainer\x82\xd3\xe4\x93\x02\x36\"1/containers/v1/containers/{container_id}:rollback:\x01*\x12\xbc\x01\n\x0bGetRevision\x12\x42.yandex.cloud.serverless.containers.v1.GetContainerRevisionRequest\x1a/.yandex.cloud.serverless.containers.v1.Revision\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/containers/v1/revisions/{container_revision_id}\x12\xc0\x01\n\rListRevisions\x12\x45.yandex.cloud.serverless.containers.v1.ListContainersRevisionsRequest\x1a\x46.yandex.cloud.serverless.containers.v1.ListContainersRevisionsResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/containers/v1/revisions\x12\xdc\x01\n\x0eListOperations\x12\x45.yandex.cloud.serverless.containers.v1.ListContainerOperationsRequest\x1a\x46.yandex.cloud.serverless.containers.v1.ListContainerOperationsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/containers/v1/containers/{container_id}/operations\x12\xb9\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"B\x82\xd3\xe4\x93\x02<\x12:/containers/v1/containers/{resource_id}:listAccessBindings\x12\xe9\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x81\x01\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02>\"9/containers/v1/containers/{resource_id}:setAccessBindings:\x01*\x12\xf5\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x87\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x41\"</containers/v1/containers/{resource_id}:updateAccessBindings:\x01*B\x81\x01\n)yandex.cloud.api.serverless.containers.v1ZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/containers/v1;containersb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.containers.v1.container_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.serverless.containers.v1ZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/containers/v1;containers'
  _GETCONTAINERREQUEST.fields_by_name['container_id']._options = None
  _GETCONTAINERREQUEST.fields_by_name['container_id']._serialized_options = b'\350\3071\001'
  _LISTCONTAINERSREQUEST.fields_by_name['folder_id']._options = None
  _LISTCONTAINERSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATECONTAINERREQUEST_LABELSENTRY._options = None
  _CREATECONTAINERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATECONTAINERREQUEST.fields_by_name['folder_id']._options = None
  _CREATECONTAINERREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATECONTAINERREQUEST.fields_by_name['name']._options = None
  _CREATECONTAINERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _CREATECONTAINERREQUEST.fields_by_name['description']._options = None
  _CREATECONTAINERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATECONTAINERREQUEST.fields_by_name['labels']._options = None
  _CREATECONTAINERREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _UPDATECONTAINERREQUEST_LABELSENTRY._options = None
  _UPDATECONTAINERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATECONTAINERREQUEST.fields_by_name['container_id']._options = None
  _UPDATECONTAINERREQUEST.fields_by_name['container_id']._serialized_options = b'\350\3071\001'
  _UPDATECONTAINERREQUEST.fields_by_name['name']._options = None
  _UPDATECONTAINERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _UPDATECONTAINERREQUEST.fields_by_name['description']._options = None
  _UPDATECONTAINERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATECONTAINERREQUEST.fields_by_name['labels']._options = None
  _UPDATECONTAINERREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _DELETECONTAINERREQUEST.fields_by_name['container_id']._options = None
  _DELETECONTAINERREQUEST.fields_by_name['container_id']._serialized_options = b'\350\3071\001'
  _GETCONTAINERREVISIONREQUEST.fields_by_name['container_revision_id']._options = None
  _GETCONTAINERREVISIONREQUEST.fields_by_name['container_revision_id']._serialized_options = b'\350\3071\001'
  _LISTCONTAINERSREVISIONSREQUEST.oneofs_by_name['id']._options = None
  _LISTCONTAINERSREVISIONSREQUEST.oneofs_by_name['id']._serialized_options = b'\300\3011\001'
  _LISTCONTAINERSREVISIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTCONTAINERSREVISIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTCONTAINERSREVISIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTCONTAINERSREVISIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTCONTAINERSREVISIONSREQUEST.fields_by_name['filter']._options = None
  _LISTCONTAINERSREVISIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _DEPLOYCONTAINERREVISIONREQUEST.fields_by_name['container_id']._options = None
  _DEPLOYCONTAINERREVISIONREQUEST.fields_by_name['container_id']._serialized_options = b'\350\3071\001'
  _DEPLOYCONTAINERREVISIONREQUEST.fields_by_name['resources']._options = None
  _DEPLOYCONTAINERREVISIONREQUEST.fields_by_name['resources']._serialized_options = b'\350\3071\001'
  _DEPLOYCONTAINERREVISIONREQUEST.fields_by_name['execution_timeout']._options = None
  _DEPLOYCONTAINERREVISIONREQUEST.fields_by_name['execution_timeout']._serialized_options = b'\372\3071\0100s-3600s'
  _DEPLOYCONTAINERREVISIONREQUEST.fields_by_name['image_spec']._options = None
  _DEPLOYCONTAINERREVISIONREQUEST.fields_by_name['image_spec']._serialized_options = b'\350\3071\001'
  _IMAGESPEC_ENVIRONMENTENTRY._options = None
  _IMAGESPEC_ENVIRONMENTENTRY._serialized_options = b'8\001'
  _IMAGESPEC.fields_by_name['image_url']._options = None
  _IMAGESPEC.fields_by_name['image_url']._serialized_options = b'\350\3071\001'
  _IMAGESPEC.fields_by_name['environment']._options = None
  _IMAGESPEC.fields_by_name['environment']._serialized_options = b'\212\3101\006<=4096\262\3101\027\022\025[a-zA-Z][a-zA-Z0-9_]*'
  _ROLLBACKCONTAINERREQUEST.fields_by_name['container_id']._options = None
  _ROLLBACKCONTAINERREQUEST.fields_by_name['container_id']._serialized_options = b'\350\3071\001'
  _ROLLBACKCONTAINERREQUEST.fields_by_name['revision_id']._options = None
  _ROLLBACKCONTAINERREQUEST.fields_by_name['revision_id']._serialized_options = b'\350\3071\001'
  _LISTCONTAINEROPERATIONSREQUEST.fields_by_name['container_id']._options = None
  _LISTCONTAINEROPERATIONSREQUEST.fields_by_name['container_id']._serialized_options = b'\350\3071\001'
  _LISTCONTAINEROPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTCONTAINEROPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTCONTAINEROPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTCONTAINEROPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTCONTAINEROPERATIONSREQUEST.fields_by_name['filter']._options = None
  _LISTCONTAINEROPERATIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _CONTAINERSERVICE.methods_by_name['Get']._options = None
  _CONTAINERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002*\022(/containers/v1/containers/{container_id}'
  _CONTAINERSERVICE.methods_by_name['List']._options = None
  _CONTAINERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\033\022\031/containers/v1/containers'
  _CONTAINERSERVICE.methods_by_name['Create']._options = None
  _CONTAINERSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*$\n\027CreateContainerMetadata\022\tContainer\202\323\344\223\002\036\"\031/containers/v1/containers:\001*'
  _CONTAINERSERVICE.methods_by_name['Update']._options = None
  _CONTAINERSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*$\n\027UpdateContainerMetadata\022\tContainer\202\323\344\223\002-2(/containers/v1/containers/{container_id}:\001*'
  _CONTAINERSERVICE.methods_by_name['Delete']._options = None
  _CONTAINERSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*0\n\027DeleteContainerMetadata\022\025google.protobuf.Empty\202\323\344\223\002**(/containers/v1/containers/{container_id}'
  _CONTAINERSERVICE.methods_by_name['DeployRevision']._options = None
  _CONTAINERSERVICE.methods_by_name['DeployRevision']._serialized_options = b'\262\322*+\n\037DeployContainerRevisionMetadata\022\010Revision\202\323\344\223\002$\"\037/containers/v1/revisions:deploy:\001*'
  _CONTAINERSERVICE.methods_by_name['Rollback']._options = None
  _CONTAINERSERVICE.methods_by_name['Rollback']._serialized_options = b'\262\322*&\n\031RollbackContainerMetadata\022\tContainer\202\323\344\223\0026\"1/containers/v1/containers/{container_id}:rollback:\001*'
  _CONTAINERSERVICE.methods_by_name['GetRevision']._options = None
  _CONTAINERSERVICE.methods_by_name['GetRevision']._serialized_options = b'\202\323\344\223\0022\0220/containers/v1/revisions/{container_revision_id}'
  _CONTAINERSERVICE.methods_by_name['ListRevisions']._options = None
  _CONTAINERSERVICE.methods_by_name['ListRevisions']._serialized_options = b'\202\323\344\223\002\032\022\030/containers/v1/revisions'
  _CONTAINERSERVICE.methods_by_name['ListOperations']._options = None
  _CONTAINERSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0025\0223/containers/v1/containers/{container_id}/operations'
  _CONTAINERSERVICE.methods_by_name['ListAccessBindings']._options = None
  _CONTAINERSERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002<\022:/containers/v1/containers/{resource_id}:listAccessBindings'
  _CONTAINERSERVICE.methods_by_name['SetAccessBindings']._options = None
  _CONTAINERSERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002>\"9/containers/v1/containers/{resource_id}:setAccessBindings:\001*'
  _CONTAINERSERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _CONTAINERSERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002A\"</containers/v1/containers/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETCONTAINERREQUEST']._serialized_start=394
  _globals['_GETCONTAINERREQUEST']._serialized_end=443
  _globals['_LISTCONTAINERSREQUEST']._serialized_start=445
  _globals['_LISTCONTAINERSREQUEST']._serialized_end=548
  _globals['_LISTCONTAINERSRESPONSE']._serialized_start=550
  _globals['_LISTCONTAINERSRESPONSE']._serialized_end=669
  _globals['_CREATECONTAINERREQUEST']._serialized_start=672
  _globals['_CREATECONTAINERREQUEST']._serialized_end=1010
  _globals['_CREATECONTAINERREQUEST_LABELSENTRY']._serialized_start=965
  _globals['_CREATECONTAINERREQUEST_LABELSENTRY']._serialized_end=1010
  _globals['_CREATECONTAINERMETADATA']._serialized_start=1012
  _globals['_CREATECONTAINERMETADATA']._serialized_end=1059
  _globals['_UPDATECONTAINERREQUEST']._serialized_start=1062
  _globals['_UPDATECONTAINERREQUEST']._serialized_end=1452
  _globals['_UPDATECONTAINERREQUEST_LABELSENTRY']._serialized_start=965
  _globals['_UPDATECONTAINERREQUEST_LABELSENTRY']._serialized_end=1010
  _globals['_UPDATECONTAINERMETADATA']._serialized_start=1454
  _globals['_UPDATECONTAINERMETADATA']._serialized_end=1501
  _globals['_DELETECONTAINERREQUEST']._serialized_start=1503
  _globals['_DELETECONTAINERREQUEST']._serialized_end=1555
  _globals['_DELETECONTAINERMETADATA']._serialized_start=1557
  _globals['_DELETECONTAINERMETADATA']._serialized_end=1604
  _globals['_GETCONTAINERREVISIONREQUEST']._serialized_start=1606
  _globals['_GETCONTAINERREVISIONREQUEST']._serialized_end=1672
  _globals['_LISTCONTAINERSREVISIONSREQUEST']._serialized_start=1675
  _globals['_LISTCONTAINERSREVISIONSREQUEST']._serialized_end=1854
  _globals['_LISTCONTAINERSREVISIONSRESPONSE']._serialized_start=1856
  _globals['_LISTCONTAINERSREVISIONSRESPONSE']._serialized_end=1982
  _globals['_DEPLOYCONTAINERREVISIONREQUEST']._serialized_start=1985
  _globals['_DEPLOYCONTAINERREVISIONREQUEST']._serialized_end=2856
  _globals['_IMAGESPEC']._serialized_start=2859
  _globals['_IMAGESPEC']._serialized_end=3219
  _globals['_IMAGESPEC_ENVIRONMENTENTRY']._serialized_start=3169
  _globals['_IMAGESPEC_ENVIRONMENTENTRY']._serialized_end=3219
  _globals['_DEPLOYCONTAINERREVISIONMETADATA']._serialized_start=3221
  _globals['_DEPLOYCONTAINERREVISIONMETADATA']._serialized_end=3285
  _globals['_ROLLBACKCONTAINERREQUEST']._serialized_start=3287
  _globals['_ROLLBACKCONTAINERREQUEST']._serialized_end=3368
  _globals['_ROLLBACKCONTAINERMETADATA']._serialized_start=3370
  _globals['_ROLLBACKCONTAINERMETADATA']._serialized_end=3440
  _globals['_LISTCONTAINEROPERATIONSREQUEST']._serialized_start=3443
  _globals['_LISTCONTAINEROPERATIONSREQUEST']._serialized_end=3593
  _globals['_LISTCONTAINEROPERATIONSRESPONSE']._serialized_start=3595
  _globals['_LISTCONTAINEROPERATIONSRESPONSE']._serialized_end=3708
  _globals['_CONTAINERSERVICE']._serialized_start=3711
  _globals['_CONTAINERSERVICE']._serialized_end=6380
# @@protoc_insertion_point(module_scope)
