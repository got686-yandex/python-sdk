# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/k8s/marketplace/v1/helm_release_service.proto
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
    'yandex/cloud/k8s/marketplace/v1/helm_release_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.k8s.marketplace.v1 import helm_release_pb2 as yandex_dot_cloud_dot_k8s_dot_marketplace_dot_v1_dot_helm__release__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/k8s/marketplace/v1/helm_release_service.proto\x12\x1fyandex.cloud.k8s.marketplace.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x32yandex/cloud/k8s/marketplace/v1/helm_release.proto\"q\n\x17ListHelmReleasesRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"x\n\x18ListHelmReleasesResponse\x12\x43\n\rhelm_releases\x18\x01 \x03(\x0b\x32,.yandex.cloud.k8s.marketplace.v1.HelmRelease\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\")\n\x15GetHelmReleaseRequest\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x95\x01\n\x19InstallHelmReleaseRequest\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1a\n\x12product_version_id\x18\x02 \x01(\t\x12\x42\n\x0buser_values\x18\x03 \x03(\x0b\x32-.yandex.cloud.k8s.marketplace.v1.ValueWithKey\"e\n\x1aInstallHelmReleaseMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x17\n\x0fhelm_release_id\x18\x02 \x01(\t\x12\x1a\n\x12product_version_id\x18\x03 \x01(\t\"\x8c\x01\n\x18UpdateHelmReleaseRequest\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1a\n\x12product_version_id\x18\x02 \x01(\t\x12\x42\n\x0buser_values\x18\x03 \x03(\x0b\x32-.yandex.cloud.k8s.marketplace.v1.ValueWithKey\"d\n\x19UpdateHelmReleaseMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x17\n\x0fhelm_release_id\x18\x02 \x01(\t\x12\x1a\n\x12product_version_id\x18\x03 \x01(\t\"/\n\x1bUninstallHelmReleaseRequest\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"W\n\x1cUninstallHelmReleaseMetadata\x12\x18\n\ncluster_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\x0fhelm_release_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\"X\n\x0cValueWithKey\x12\x11\n\x03key\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.yandex.cloud.k8s.marketplace.v1.Value\"\'\n\x05Value\x12\x15\n\x0btyped_value\x18\x01 \x01(\tH\x00\x42\x07\n\x05value2\xac\x08\n\x12HelmReleaseService\x12\xb5\x01\n\x04List\x12\x38.yandex.cloud.k8s.marketplace.v1.ListHelmReleasesRequest\x1a\x39.yandex.cloud.k8s.marketplace.v1.ListHelmReleasesResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/managed-kubernetes/marketplace/v1/helm-releases\x12\xaa\x01\n\x03Get\x12\x36.yandex.cloud.k8s.marketplace.v1.GetHelmReleaseRequest\x1a,.yandex.cloud.k8s.marketplace.v1.HelmRelease\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/managed-kubernetes/marketplace/v1/helm-releases/{id}\x12\xda\x01\n\x07Install\x12:.yandex.cloud.k8s.marketplace.v1.InstallHelmReleaseRequest\x1a!.yandex.cloud.operation.Operation\"p\xb2\xd2*)\n\x1aInstallHelmReleaseMetadata\x12\x0bHelmRelease\x82\xd3\xe4\x93\x02=\"8/managed-kubernetes/marketplace/v1/helm-releases:install:\x01*\x12\xd4\x01\n\x06Update\x12\x39.yandex.cloud.k8s.marketplace.v1.UpdateHelmReleaseRequest\x1a!.yandex.cloud.operation.Operation\"l\xb2\xd2*(\n\x19UpdateHelmReleaseMetadata\x12\x0bHelmRelease\x82\xd3\xe4\x93\x02:25/managed-kubernetes/marketplace/v1/helm-releases/{id}:\x01*\x12\xfc\x01\n\tUninstall\x12<.yandex.cloud.k8s.marketplace.v1.UninstallHelmReleaseRequest\x1a!.yandex.cloud.operation.Operation\"\x8d\x01\xb2\xd2*5\n\x1cUninstallHelmReleaseMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02N\"I/managed-kubernetes/marketplace/v1/helm-releases/uninstall/{id}:uninstall:\x01*Bz\n#yandex.cloud.api.k8s.marketplace.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/k8s/marketplace/v1;k8s_marketplaceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.k8s.marketplace.v1.helm_release_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#yandex.cloud.api.k8s.marketplace.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/k8s/marketplace/v1;k8s_marketplace'
  _globals['_LISTHELMRELEASESREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTHELMRELEASESREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTHELMRELEASESREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTHELMRELEASESREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTHELMRELEASESREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTHELMRELEASESREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_GETHELMRELEASEREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_GETHELMRELEASEREQUEST'].fields_by_name['id']._serialized_options = b'\350\3071\001'
  _globals['_INSTALLHELMRELEASEREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_INSTALLHELMRELEASEREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_UPDATEHELMRELEASEREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_UPDATEHELMRELEASEREQUEST'].fields_by_name['id']._serialized_options = b'\350\3071\001'
  _globals['_UNINSTALLHELMRELEASEREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_UNINSTALLHELMRELEASEREQUEST'].fields_by_name['id']._serialized_options = b'\350\3071\001'
  _globals['_UNINSTALLHELMRELEASEMETADATA'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UNINSTALLHELMRELEASEMETADATA'].fields_by_name['cluster_id']._serialized_options = b'\350\3071\001'
  _globals['_UNINSTALLHELMRELEASEMETADATA'].fields_by_name['helm_release_id']._loaded_options = None
  _globals['_UNINSTALLHELMRELEASEMETADATA'].fields_by_name['helm_release_id']._serialized_options = b'\350\3071\001'
  _globals['_VALUEWITHKEY'].fields_by_name['key']._loaded_options = None
  _globals['_VALUEWITHKEY'].fields_by_name['key']._serialized_options = b'\350\3071\001'
  _globals['_HELMRELEASESERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_HELMRELEASESERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\0022\0220/managed-kubernetes/marketplace/v1/helm-releases'
  _globals['_HELMRELEASESERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_HELMRELEASESERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\0027\0225/managed-kubernetes/marketplace/v1/helm-releases/{id}'
  _globals['_HELMRELEASESERVICE'].methods_by_name['Install']._loaded_options = None
  _globals['_HELMRELEASESERVICE'].methods_by_name['Install']._serialized_options = b'\262\322*)\n\032InstallHelmReleaseMetadata\022\013HelmRelease\202\323\344\223\002=\"8/managed-kubernetes/marketplace/v1/helm-releases:install:\001*'
  _globals['_HELMRELEASESERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_HELMRELEASESERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*(\n\031UpdateHelmReleaseMetadata\022\013HelmRelease\202\323\344\223\002:25/managed-kubernetes/marketplace/v1/helm-releases/{id}:\001*'
  _globals['_HELMRELEASESERVICE'].methods_by_name['Uninstall']._loaded_options = None
  _globals['_HELMRELEASESERVICE'].methods_by_name['Uninstall']._serialized_options = b'\262\322*5\n\034UninstallHelmReleaseMetadata\022\025google.protobuf.Empty\202\323\344\223\002N\"I/managed-kubernetes/marketplace/v1/helm-releases/uninstall/{id}:uninstall:\001*'
  _globals['_LISTHELMRELEASESREQUEST']._serialized_start=282
  _globals['_LISTHELMRELEASESREQUEST']._serialized_end=395
  _globals['_LISTHELMRELEASESRESPONSE']._serialized_start=397
  _globals['_LISTHELMRELEASESRESPONSE']._serialized_end=517
  _globals['_GETHELMRELEASEREQUEST']._serialized_start=519
  _globals['_GETHELMRELEASEREQUEST']._serialized_end=560
  _globals['_INSTALLHELMRELEASEREQUEST']._serialized_start=563
  _globals['_INSTALLHELMRELEASEREQUEST']._serialized_end=712
  _globals['_INSTALLHELMRELEASEMETADATA']._serialized_start=714
  _globals['_INSTALLHELMRELEASEMETADATA']._serialized_end=815
  _globals['_UPDATEHELMRELEASEREQUEST']._serialized_start=818
  _globals['_UPDATEHELMRELEASEREQUEST']._serialized_end=958
  _globals['_UPDATEHELMRELEASEMETADATA']._serialized_start=960
  _globals['_UPDATEHELMRELEASEMETADATA']._serialized_end=1060
  _globals['_UNINSTALLHELMRELEASEREQUEST']._serialized_start=1062
  _globals['_UNINSTALLHELMRELEASEREQUEST']._serialized_end=1109
  _globals['_UNINSTALLHELMRELEASEMETADATA']._serialized_start=1111
  _globals['_UNINSTALLHELMRELEASEMETADATA']._serialized_end=1198
  _globals['_VALUEWITHKEY']._serialized_start=1200
  _globals['_VALUEWITHKEY']._serialized_end=1288
  _globals['_VALUE']._serialized_start=1290
  _globals['_VALUE']._serialized_end=1329
  _globals['_HELMRELEASESERVICE']._serialized_start=1332
  _globals['_HELMRELEASESERVICE']._serialized_end=2400
# @@protoc_insertion_point(module_scope)
