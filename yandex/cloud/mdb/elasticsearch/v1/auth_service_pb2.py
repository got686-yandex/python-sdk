# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/elasticsearch/v1/auth_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.elasticsearch.v1 import auth_pb2 as yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/elasticsearch/v1/auth_service.proto',
  package='yandex.cloud.mdb.elasticsearch.v1',
  syntax='proto3',
  serialized_options=b'\n%yandex.cloud.api.mdb.elasticsearch.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1;elasticsearch',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4yandex/cloud/mdb/elasticsearch/v1/auth_service.proto\x12!yandex.cloud.mdb.elasticsearch.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a,yandex/cloud/mdb/elasticsearch/v1/auth.proto\"<\n\x18ListAuthProvidersRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"_\n\x19ListAuthProvidersResponse\x12\x42\n\tproviders\x18\x01 \x03(\x0b\x32/.yandex.cloud.mdb.elasticsearch.v1.AuthProvider\"j\n\x16GetAuthProviderRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\x04name\x18\x02 \x01(\tB \xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\xf2\xc7\x31\x10[a-z][a-z0-9_-]*\"\x89\x01\n\x17\x41\x64\x64\x41uthProvidersRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12L\n\tproviders\x18\x02 \x03(\x0b\x32/.yandex.cloud.mdb.elasticsearch.v1.AuthProviderB\x08\x82\xc8\x31\x04<=10\"\x8c\x01\n\x1aUpdateAuthProvidersRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12L\n\tproviders\x18\x02 \x03(\x0b\x32/.yandex.cloud.mdb.elasticsearch.v1.AuthProviderB\x08\x82\xc8\x31\x04<=10\"|\n\x1a\x44\x65leteAuthProvidersRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12<\n\x0eprovider_names\x18\x02 \x03(\tB$\x82\xc8\x31\x04<=10\x8a\xc8\x31\x04<=50\xf2\xc7\x31\x10[a-z][a-z0-9_-]*\"\xb6\x01\n\x19UpdateAuthProviderRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\x04name\x18\x02 \x01(\tB \xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\xf2\xc7\x31\x10[a-z][a-z0-9_-]*\x12G\n\x08provider\x18\x03 \x01(\x0b\x32/.yandex.cloud.mdb.elasticsearch.v1.AuthProviderB\x04\xe8\xc7\x31\x01\"m\n\x19\x44\x65leteAuthProviderRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\x04name\x18\x02 \x01(\tB \xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\xf2\xc7\x31\x10[a-z][a-z0-9_-]*\"=\n\x18\x41\x64\x64\x41uthProvidersMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x03(\t\"@\n\x1bUpdateAuthProvidersMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x03(\t\"@\n\x1b\x44\x65leteAuthProvidersMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x03(\t2\xef\x0c\n\x0b\x41uthService\x12\xd2\x01\n\rListProviders\x12;.yandex.cloud.mdb.elasticsearch.v1.ListAuthProvidersRequest\x1a<.yandex.cloud.mdb.elasticsearch.v1.ListAuthProvidersResponse\"F\x82\xd3\xe4\x93\x02@\x12>/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers\x12\xc8\x01\n\x0bGetProvider\x12\x39.yandex.cloud.mdb.elasticsearch.v1.GetAuthProviderRequest\x1a/.yandex.cloud.mdb.elasticsearch.v1.AuthProvider\"M\x82\xd3\xe4\x93\x02G\x12\x45/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers/{name}\x12\xe5\x01\n\x0c\x41\x64\x64Providers\x12:.yandex.cloud.mdb.elasticsearch.v1.AddAuthProvidersRequest\x1a!.yandex.cloud.operation.Operation\"v\x82\xd3\xe4\x93\x02\x43\">/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers:\x01*\xb2\xd2*)\n\x18\x41\x64\x64\x41uthProvidersMetadata\x12\rAuthProviders\x12\xee\x01\n\x0fUpdateProviders\x12=.yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProvidersRequest\x1a!.yandex.cloud.operation.Operation\"y\x82\xd3\xe4\x93\x02\x43\x1a>/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers:\x01*\xb2\xd2*,\n\x1bUpdateAuthProvidersMetadata\x12\rAuthProviders\x12\xf3\x01\n\x0f\x44\x65leteProviders\x12=.yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProvidersRequest\x1a!.yandex.cloud.operation.Operation\"~\x82\xd3\xe4\x93\x02@*>/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers\xb2\xd2*4\n\x1b\x44\x65leteAuthProvidersMetadata\x12\x15google.protobuf.Empty\x12\xf4\x01\n\x0eUpdateProvider\x12<.yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProviderRequest\x1a!.yandex.cloud.operation.Operation\"\x80\x01\x82\xd3\xe4\x93\x02J\x1a\x45/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers/{name}:\x01*\xb2\xd2*,\n\x1bUpdateAuthProvidersMetadata\x12\rAuthProviders\x12\xf9\x01\n\x0e\x44\x65leteProvider\x12<.yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProviderRequest\x1a!.yandex.cloud.operation.Operation\"\x85\x01\x82\xd3\xe4\x93\x02G*E/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers/{name}\xb2\xd2*4\n\x1b\x44\x65leteAuthProvidersMetadata\x12\x15google.protobuf.EmptyB|\n%yandex.cloud.api.mdb.elasticsearch.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1;elasticsearchb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2.DESCRIPTOR,])




_LISTAUTHPROVIDERSREQUEST = _descriptor.Descriptor(
  name='ListAuthProvidersRequest',
  full_name='yandex.cloud.mdb.elasticsearch.v1.ListAuthProvidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.ListAuthProvidersRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=332,
)


_LISTAUTHPROVIDERSRESPONSE = _descriptor.Descriptor(
  name='ListAuthProvidersResponse',
  full_name='yandex.cloud.mdb.elasticsearch.v1.ListAuthProvidersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='providers', full_name='yandex.cloud.mdb.elasticsearch.v1.ListAuthProvidersResponse.providers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=429,
)


_GETAUTHPROVIDERREQUEST = _descriptor.Descriptor(
  name='GetAuthProviderRequest',
  full_name='yandex.cloud.mdb.elasticsearch.v1.GetAuthProviderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.GetAuthProviderRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.elasticsearch.v1.GetAuthProviderRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50\362\3071\020[a-z][a-z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=537,
)


_ADDAUTHPROVIDERSREQUEST = _descriptor.Descriptor(
  name='AddAuthProvidersRequest',
  full_name='yandex.cloud.mdb.elasticsearch.v1.AddAuthProvidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.AddAuthProvidersRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='providers', full_name='yandex.cloud.mdb.elasticsearch.v1.AddAuthProvidersRequest.providers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\004<=10', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=540,
  serialized_end=677,
)


_UPDATEAUTHPROVIDERSREQUEST = _descriptor.Descriptor(
  name='UpdateAuthProvidersRequest',
  full_name='yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProvidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProvidersRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='providers', full_name='yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProvidersRequest.providers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\004<=10', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=820,
)


_DELETEAUTHPROVIDERSREQUEST = _descriptor.Descriptor(
  name='DeleteAuthProvidersRequest',
  full_name='yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProvidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProvidersRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider_names', full_name='yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProvidersRequest.provider_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\004<=10\212\3101\004<=50\362\3071\020[a-z][a-z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=822,
  serialized_end=946,
)


_UPDATEAUTHPROVIDERREQUEST = _descriptor.Descriptor(
  name='UpdateAuthProviderRequest',
  full_name='yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProviderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProviderRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProviderRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50\362\3071\020[a-z][a-z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProviderRequest.provider', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=949,
  serialized_end=1131,
)


_DELETEAUTHPROVIDERREQUEST = _descriptor.Descriptor(
  name='DeleteAuthProviderRequest',
  full_name='yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProviderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProviderRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProviderRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50\362\3071\020[a-z][a-z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1133,
  serialized_end=1242,
)


_ADDAUTHPROVIDERSMETADATA = _descriptor.Descriptor(
  name='AddAuthProvidersMetadata',
  full_name='yandex.cloud.mdb.elasticsearch.v1.AddAuthProvidersMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.AddAuthProvidersMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='names', full_name='yandex.cloud.mdb.elasticsearch.v1.AddAuthProvidersMetadata.names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1244,
  serialized_end=1305,
)


_UPDATEAUTHPROVIDERSMETADATA = _descriptor.Descriptor(
  name='UpdateAuthProvidersMetadata',
  full_name='yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProvidersMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProvidersMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='names', full_name='yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProvidersMetadata.names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1307,
  serialized_end=1371,
)


_DELETEAUTHPROVIDERSMETADATA = _descriptor.Descriptor(
  name='DeleteAuthProvidersMetadata',
  full_name='yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProvidersMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProvidersMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='names', full_name='yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProvidersMetadata.names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1373,
  serialized_end=1437,
)

_LISTAUTHPROVIDERSRESPONSE.fields_by_name['providers'].message_type = yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2._AUTHPROVIDER
_ADDAUTHPROVIDERSREQUEST.fields_by_name['providers'].message_type = yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2._AUTHPROVIDER
_UPDATEAUTHPROVIDERSREQUEST.fields_by_name['providers'].message_type = yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2._AUTHPROVIDER
_UPDATEAUTHPROVIDERREQUEST.fields_by_name['provider'].message_type = yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2._AUTHPROVIDER
DESCRIPTOR.message_types_by_name['ListAuthProvidersRequest'] = _LISTAUTHPROVIDERSREQUEST
DESCRIPTOR.message_types_by_name['ListAuthProvidersResponse'] = _LISTAUTHPROVIDERSRESPONSE
DESCRIPTOR.message_types_by_name['GetAuthProviderRequest'] = _GETAUTHPROVIDERREQUEST
DESCRIPTOR.message_types_by_name['AddAuthProvidersRequest'] = _ADDAUTHPROVIDERSREQUEST
DESCRIPTOR.message_types_by_name['UpdateAuthProvidersRequest'] = _UPDATEAUTHPROVIDERSREQUEST
DESCRIPTOR.message_types_by_name['DeleteAuthProvidersRequest'] = _DELETEAUTHPROVIDERSREQUEST
DESCRIPTOR.message_types_by_name['UpdateAuthProviderRequest'] = _UPDATEAUTHPROVIDERREQUEST
DESCRIPTOR.message_types_by_name['DeleteAuthProviderRequest'] = _DELETEAUTHPROVIDERREQUEST
DESCRIPTOR.message_types_by_name['AddAuthProvidersMetadata'] = _ADDAUTHPROVIDERSMETADATA
DESCRIPTOR.message_types_by_name['UpdateAuthProvidersMetadata'] = _UPDATEAUTHPROVIDERSMETADATA
DESCRIPTOR.message_types_by_name['DeleteAuthProvidersMetadata'] = _DELETEAUTHPROVIDERSMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListAuthProvidersRequest = _reflection.GeneratedProtocolMessageType('ListAuthProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUTHPROVIDERSREQUEST,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.ListAuthProvidersRequest)
  })
_sym_db.RegisterMessage(ListAuthProvidersRequest)

ListAuthProvidersResponse = _reflection.GeneratedProtocolMessageType('ListAuthProvidersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUTHPROVIDERSRESPONSE,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.ListAuthProvidersResponse)
  })
_sym_db.RegisterMessage(ListAuthProvidersResponse)

GetAuthProviderRequest = _reflection.GeneratedProtocolMessageType('GetAuthProviderRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAUTHPROVIDERREQUEST,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.GetAuthProviderRequest)
  })
_sym_db.RegisterMessage(GetAuthProviderRequest)

AddAuthProvidersRequest = _reflection.GeneratedProtocolMessageType('AddAuthProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDAUTHPROVIDERSREQUEST,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.AddAuthProvidersRequest)
  })
_sym_db.RegisterMessage(AddAuthProvidersRequest)

UpdateAuthProvidersRequest = _reflection.GeneratedProtocolMessageType('UpdateAuthProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEAUTHPROVIDERSREQUEST,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProvidersRequest)
  })
_sym_db.RegisterMessage(UpdateAuthProvidersRequest)

DeleteAuthProvidersRequest = _reflection.GeneratedProtocolMessageType('DeleteAuthProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEAUTHPROVIDERSREQUEST,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProvidersRequest)
  })
_sym_db.RegisterMessage(DeleteAuthProvidersRequest)

UpdateAuthProviderRequest = _reflection.GeneratedProtocolMessageType('UpdateAuthProviderRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEAUTHPROVIDERREQUEST,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProviderRequest)
  })
_sym_db.RegisterMessage(UpdateAuthProviderRequest)

DeleteAuthProviderRequest = _reflection.GeneratedProtocolMessageType('DeleteAuthProviderRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEAUTHPROVIDERREQUEST,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProviderRequest)
  })
_sym_db.RegisterMessage(DeleteAuthProviderRequest)

AddAuthProvidersMetadata = _reflection.GeneratedProtocolMessageType('AddAuthProvidersMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ADDAUTHPROVIDERSMETADATA,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.AddAuthProvidersMetadata)
  })
_sym_db.RegisterMessage(AddAuthProvidersMetadata)

UpdateAuthProvidersMetadata = _reflection.GeneratedProtocolMessageType('UpdateAuthProvidersMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEAUTHPROVIDERSMETADATA,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.UpdateAuthProvidersMetadata)
  })
_sym_db.RegisterMessage(UpdateAuthProvidersMetadata)

DeleteAuthProvidersMetadata = _reflection.GeneratedProtocolMessageType('DeleteAuthProvidersMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEAUTHPROVIDERSMETADATA,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.auth_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.DeleteAuthProvidersMetadata)
  })
_sym_db.RegisterMessage(DeleteAuthProvidersMetadata)


DESCRIPTOR._options = None
_LISTAUTHPROVIDERSREQUEST.fields_by_name['cluster_id']._options = None
_GETAUTHPROVIDERREQUEST.fields_by_name['cluster_id']._options = None
_GETAUTHPROVIDERREQUEST.fields_by_name['name']._options = None
_ADDAUTHPROVIDERSREQUEST.fields_by_name['cluster_id']._options = None
_ADDAUTHPROVIDERSREQUEST.fields_by_name['providers']._options = None
_UPDATEAUTHPROVIDERSREQUEST.fields_by_name['cluster_id']._options = None
_UPDATEAUTHPROVIDERSREQUEST.fields_by_name['providers']._options = None
_DELETEAUTHPROVIDERSREQUEST.fields_by_name['cluster_id']._options = None
_DELETEAUTHPROVIDERSREQUEST.fields_by_name['provider_names']._options = None
_UPDATEAUTHPROVIDERREQUEST.fields_by_name['cluster_id']._options = None
_UPDATEAUTHPROVIDERREQUEST.fields_by_name['name']._options = None
_UPDATEAUTHPROVIDERREQUEST.fields_by_name['provider']._options = None
_DELETEAUTHPROVIDERREQUEST.fields_by_name['cluster_id']._options = None
_DELETEAUTHPROVIDERREQUEST.fields_by_name['name']._options = None

_AUTHSERVICE = _descriptor.ServiceDescriptor(
  name='AuthService',
  full_name='yandex.cloud.mdb.elasticsearch.v1.AuthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1440,
  serialized_end=3087,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListProviders',
    full_name='yandex.cloud.mdb.elasticsearch.v1.AuthService.ListProviders',
    index=0,
    containing_service=None,
    input_type=_LISTAUTHPROVIDERSREQUEST,
    output_type=_LISTAUTHPROVIDERSRESPONSE,
    serialized_options=b'\202\323\344\223\002@\022>/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetProvider',
    full_name='yandex.cloud.mdb.elasticsearch.v1.AuthService.GetProvider',
    index=1,
    containing_service=None,
    input_type=_GETAUTHPROVIDERREQUEST,
    output_type=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_auth__pb2._AUTHPROVIDER,
    serialized_options=b'\202\323\344\223\002G\022E/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers/{name}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddProviders',
    full_name='yandex.cloud.mdb.elasticsearch.v1.AuthService.AddProviders',
    index=2,
    containing_service=None,
    input_type=_ADDAUTHPROVIDERSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002C\">/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers:\001*\262\322*)\n\030AddAuthProvidersMetadata\022\rAuthProviders',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProviders',
    full_name='yandex.cloud.mdb.elasticsearch.v1.AuthService.UpdateProviders',
    index=3,
    containing_service=None,
    input_type=_UPDATEAUTHPROVIDERSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002C\032>/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers:\001*\262\322*,\n\033UpdateAuthProvidersMetadata\022\rAuthProviders',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteProviders',
    full_name='yandex.cloud.mdb.elasticsearch.v1.AuthService.DeleteProviders',
    index=4,
    containing_service=None,
    input_type=_DELETEAUTHPROVIDERSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002@*>/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers\262\322*4\n\033DeleteAuthProvidersMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProvider',
    full_name='yandex.cloud.mdb.elasticsearch.v1.AuthService.UpdateProvider',
    index=5,
    containing_service=None,
    input_type=_UPDATEAUTHPROVIDERREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002J\032E/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers/{name}:\001*\262\322*,\n\033UpdateAuthProvidersMetadata\022\rAuthProviders',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteProvider',
    full_name='yandex.cloud.mdb.elasticsearch.v1.AuthService.DeleteProvider',
    index=6,
    containing_service=None,
    input_type=_DELETEAUTHPROVIDERREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002G*E/managed-elasticsearch/v1/clusters/{cluster_id}/auth/providers/{name}\262\322*4\n\033DeleteAuthProvidersMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHSERVICE)

DESCRIPTOR.services_by_name['AuthService'] = _AUTHSERVICE

# @@protoc_insertion_point(module_scope)