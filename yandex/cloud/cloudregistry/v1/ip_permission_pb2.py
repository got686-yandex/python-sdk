# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cloudregistry/v1/ip_permission.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/cloudregistry/v1/ip_permission.proto\x12\x1dyandex.cloud.cloudregistry.v1\x1a\x1dyandex/cloud/validation.proto\"\x94\x01\n\x0cIpPermission\x12\x42\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x32.yandex.cloud.cloudregistry.v1.IpPermission.Action\x12\n\n\x02ip\x18\x02 \x01(\t\"4\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\x08\n\x04PULL\x10\x01\x12\x08\n\x04PUSH\x10\x02\"\xab\x01\n\x11IpPermissionDelta\x12L\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x36.yandex.cloud.cloudregistry.v1.IpPermissionDeltaActionB\x04\xe8\xc7\x31\x01\x12H\n\rip_permission\x18\x02 \x01(\x0b\x32+.yandex.cloud.cloudregistry.v1.IpPermissionB\x04\xe8\xc7\x31\x01*Z\n\x17IpPermissionDeltaAction\x12*\n&IP_PERMISSION_DELTA_ACTION_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\x42t\n!yandex.cloud.api.cloudregistry.v1ZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/cloudregistry/v1;cloudregistryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cloudregistry.v1.ip_permission_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!yandex.cloud.api.cloudregistry.v1ZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/cloudregistry/v1;cloudregistry'
  _IPPERMISSIONDELTA.fields_by_name['action']._options = None
  _IPPERMISSIONDELTA.fields_by_name['action']._serialized_options = b'\350\3071\001'
  _IPPERMISSIONDELTA.fields_by_name['ip_permission']._options = None
  _IPPERMISSIONDELTA.fields_by_name['ip_permission']._serialized_options = b'\350\3071\001'
  _globals['_IPPERMISSIONDELTAACTION']._serialized_start=440
  _globals['_IPPERMISSIONDELTAACTION']._serialized_end=530
  _globals['_IPPERMISSION']._serialized_start=116
  _globals['_IPPERMISSION']._serialized_end=264
  _globals['_IPPERMISSION_ACTION']._serialized_start=212
  _globals['_IPPERMISSION_ACTION']._serialized_end=264
  _globals['_IPPERMISSIONDELTA']._serialized_start=267
  _globals['_IPPERMISSIONDELTA']._serialized_end=438
# @@protoc_insertion_point(module_scope)