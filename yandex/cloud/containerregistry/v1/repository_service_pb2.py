# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/containerregistry/v1/repository_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.containerregistry.v1 import repository_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_repository__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/containerregistry/v1/repository_service.proto\x12!yandex.cloud.containerregistry.v1\x1a yandex/cloud/api/operation.proto\x1a yandex/cloud/access/access.proto\x1a\x32yandex/cloud/containerregistry/v1/repository.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\";\n\x14GetRepositoryRequest\x12#\n\rrepository_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"}\n\x1aGetRepositoryByNameRequest\x12_\n\x0frepository_name\x18\x01 \x01(\tBF\xe8\xc7\x31\x01\xf2\xc7\x31>[a-z0-9]+(?:[._-][a-z0-9]+)*(/([a-z0-9]+(?:[._-][a-z0-9]+)*))*\"\xcc\x01\n\x17ListRepositoriesRequest\x12\x1d\n\x0bregistry_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1b\n\tfolder_id\x18\x06 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"x\n\x18ListRepositoriesResponse\x12\x43\n\x0crepositories\x18\x01 \x03(\x0b\x32-.yandex.cloud.containerregistry.v1.Repository\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"o\n\x17UpsertRepositoryRequest\x12T\n\x04name\x18\x01 \x01(\tBF\xe8\xc7\x31\x01\xf2\xc7\x31>[a-z0-9]+(?:[._-][a-z0-9]+)*(/([a-z0-9]+(?:[._-][a-z0-9]+)*))*\"1\n\x18UpsertRepositoryMetadata\x12\x15\n\rrepository_id\x18\x01 \x01(\t\">\n\x17\x44\x65leteRepositoryRequest\x12#\n\rrepository_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"1\n\x18\x44\x65leteRepositoryMetadata\x12\x15\n\rrepository_id\x18\x01 \x01(\t2\x8f\r\n\x11RepositoryService\x12\xaa\x01\n\x03Get\x12\x37.yandex.cloud.containerregistry.v1.GetRepositoryRequest\x1a-.yandex.cloud.containerregistry.v1.Repository\";\x82\xd3\xe4\x93\x02\x35\x12\x33/container-registry/v1/repositories/{repository_id}\x12\xbf\x01\n\tGetByName\x12=.yandex.cloud.containerregistry.v1.GetRepositoryByNameRequest\x1a-.yandex.cloud.containerregistry.v1.Repository\"D\x82\xd3\xe4\x93\x02>\x12</container-registry/v1/repositories/{repository_name}:byName\x12\xac\x01\n\x04List\x12:.yandex.cloud.containerregistry.v1.ListRepositoriesRequest\x1a;.yandex.cloud.containerregistry.v1.ListRepositoriesResponse\"+\x82\xd3\xe4\x93\x02%\x12#/container-registry/v1/repositories\x12\xc3\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"L\x82\xd3\xe4\x93\x02\x46\x12\x44/container-registry/v1/repositories/{resource_id}:listAccessBindings\x12\xc1\x01\n\x06Upsert\x12:.yandex.cloud.containerregistry.v1.UpsertRepositoryRequest\x1a!.yandex.cloud.operation.Operation\"X\xb2\xd2*&\n\x18UpsertRepositoryMetadata\x12\nRepository\x82\xd3\xe4\x93\x02(\"#/container-registry/v1/repositories:\x01*\x12\xd9\x01\n\x06\x44\x65lete\x12:.yandex.cloud.containerregistry.v1.DeleteRepositoryRequest\x1a!.yandex.cloud.operation.Operation\"p\xb2\xd2*1\n\x18\x44\x65leteRepositoryMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x35*3/container-registry/v1/repositories/{repository_id}\x12\xf3\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8b\x01\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02H\"C/container-registry/v1/repositories/{resource_id}:setAccessBindings:\x01*\x12\xff\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x91\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02K\"F/container-registry/v1/repositories/{resource_id}:updateAccessBindings:\x01*B\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.containerregistry.v1.repository_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry'
  _GETREPOSITORYREQUEST.fields_by_name['repository_id']._options = None
  _GETREPOSITORYREQUEST.fields_by_name['repository_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GETREPOSITORYBYNAMEREQUEST.fields_by_name['repository_name']._options = None
  _GETREPOSITORYBYNAMEREQUEST.fields_by_name['repository_name']._serialized_options = b'\350\3071\001\362\3071>[a-z0-9]+(?:[._-][a-z0-9]+)*(/([a-z0-9]+(?:[._-][a-z0-9]+)*))*'
  _LISTREPOSITORIESREQUEST.fields_by_name['registry_id']._options = None
  _LISTREPOSITORIESREQUEST.fields_by_name['registry_id']._serialized_options = b'\212\3101\004<=50'
  _LISTREPOSITORIESREQUEST.fields_by_name['folder_id']._options = None
  _LISTREPOSITORIESREQUEST.fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _LISTREPOSITORIESREQUEST.fields_by_name['page_size']._options = None
  _LISTREPOSITORIESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTREPOSITORIESREQUEST.fields_by_name['page_token']._options = None
  _LISTREPOSITORIESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTREPOSITORIESREQUEST.fields_by_name['filter']._options = None
  _LISTREPOSITORIESREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTREPOSITORIESREQUEST.fields_by_name['order_by']._options = None
  _LISTREPOSITORIESREQUEST.fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _UPSERTREPOSITORYREQUEST.fields_by_name['name']._options = None
  _UPSERTREPOSITORYREQUEST.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071>[a-z0-9]+(?:[._-][a-z0-9]+)*(/([a-z0-9]+(?:[._-][a-z0-9]+)*))*'
  _DELETEREPOSITORYREQUEST.fields_by_name['repository_id']._options = None
  _DELETEREPOSITORYREQUEST.fields_by_name['repository_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _REPOSITORYSERVICE.methods_by_name['Get']._options = None
  _REPOSITORYSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\0025\0223/container-registry/v1/repositories/{repository_id}'
  _REPOSITORYSERVICE.methods_by_name['GetByName']._options = None
  _REPOSITORYSERVICE.methods_by_name['GetByName']._serialized_options = b'\202\323\344\223\002>\022</container-registry/v1/repositories/{repository_name}:byName'
  _REPOSITORYSERVICE.methods_by_name['List']._options = None
  _REPOSITORYSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002%\022#/container-registry/v1/repositories'
  _REPOSITORYSERVICE.methods_by_name['ListAccessBindings']._options = None
  _REPOSITORYSERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002F\022D/container-registry/v1/repositories/{resource_id}:listAccessBindings'
  _REPOSITORYSERVICE.methods_by_name['Upsert']._options = None
  _REPOSITORYSERVICE.methods_by_name['Upsert']._serialized_options = b'\262\322*&\n\030UpsertRepositoryMetadata\022\nRepository\202\323\344\223\002(\"#/container-registry/v1/repositories:\001*'
  _REPOSITORYSERVICE.methods_by_name['Delete']._options = None
  _REPOSITORYSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*1\n\030DeleteRepositoryMetadata\022\025google.protobuf.Empty\202\323\344\223\0025*3/container-registry/v1/repositories/{repository_id}'
  _REPOSITORYSERVICE.methods_by_name['SetAccessBindings']._options = None
  _REPOSITORYSERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002H\"C/container-registry/v1/repositories/{resource_id}:setAccessBindings:\001*'
  _REPOSITORYSERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _REPOSITORYSERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002K\"F/container-registry/v1/repositories/{resource_id}:updateAccessBindings:\001*'
  _globals['_GETREPOSITORYREQUEST']._serialized_start=318
  _globals['_GETREPOSITORYREQUEST']._serialized_end=377
  _globals['_GETREPOSITORYBYNAMEREQUEST']._serialized_start=379
  _globals['_GETREPOSITORYBYNAMEREQUEST']._serialized_end=504
  _globals['_LISTREPOSITORIESREQUEST']._serialized_start=507
  _globals['_LISTREPOSITORIESREQUEST']._serialized_end=711
  _globals['_LISTREPOSITORIESRESPONSE']._serialized_start=713
  _globals['_LISTREPOSITORIESRESPONSE']._serialized_end=833
  _globals['_UPSERTREPOSITORYREQUEST']._serialized_start=835
  _globals['_UPSERTREPOSITORYREQUEST']._serialized_end=946
  _globals['_UPSERTREPOSITORYMETADATA']._serialized_start=948
  _globals['_UPSERTREPOSITORYMETADATA']._serialized_end=997
  _globals['_DELETEREPOSITORYREQUEST']._serialized_start=999
  _globals['_DELETEREPOSITORYREQUEST']._serialized_end=1061
  _globals['_DELETEREPOSITORYMETADATA']._serialized_start=1063
  _globals['_DELETEREPOSITORYMETADATA']._serialized_end=1112
  _globals['_REPOSITORYSERVICE']._serialized_start=1115
  _globals['_REPOSITORYSERVICE']._serialized_end=2794
# @@protoc_insertion_point(module_scope)
