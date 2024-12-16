# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/k8s/v1/version_service.proto
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
    'yandex/cloud/k8s/v1/version_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.k8s.v1 import cluster_pb2 as yandex_dot_cloud_dot_k8s_dot_v1_dot_cluster__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/k8s/v1/version_service.proto\x12\x13yandex.cloud.k8s.v1\x1a\x1cgoogle/api/annotations.proto\x1a!yandex/cloud/k8s/v1/cluster.proto\"\x15\n\x13ListVersionsRequest\"Z\n\x14ListVersionsResponse\x12\x42\n\x12\x61vailable_versions\x18\x01 \x03(\x0b\x32&.yandex.cloud.k8s.v1.AvailableVersions\"c\n\x11\x41vailableVersions\x12<\n\x0frelease_channel\x18\x01 \x01(\x0e\x32#.yandex.cloud.k8s.v1.ReleaseChannel\x12\x10\n\x08versions\x18\x02 \x03(\t2\x97\x01\n\x0eVersionService\x12\x84\x01\n\x04List\x12(.yandex.cloud.k8s.v1.ListVersionsRequest\x1a).yandex.cloud.k8s.v1.ListVersionsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/managed-kubernetes/v1/versionsBV\n\x17yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8sb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.k8s.v1.version_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8s'
  _globals['_VERSIONSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_VERSIONSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/managed-kubernetes/v1/versions'
  _globals['_LISTVERSIONSREQUEST']._serialized_start=131
  _globals['_LISTVERSIONSREQUEST']._serialized_end=152
  _globals['_LISTVERSIONSRESPONSE']._serialized_start=154
  _globals['_LISTVERSIONSRESPONSE']._serialized_end=244
  _globals['_AVAILABLEVERSIONS']._serialized_start=246
  _globals['_AVAILABLEVERSIONS']._serialized_end=345
  _globals['_VERSIONSERVICE']._serialized_start=348
  _globals['_VERSIONSERVICE']._serialized_end=499
# @@protoc_insertion_point(module_scope)
