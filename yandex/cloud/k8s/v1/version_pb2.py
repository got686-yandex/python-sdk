# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/k8s/v1/version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/k8s/v1/version.proto',
  package='yandex.cloud.k8s.v1',
  syntax='proto3',
  serialized_options=_b('\n\027yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8s'),
  serialized_pb=_b('\n!yandex/cloud/k8s/v1/version.proto\x12\x13yandex.cloud.k8s.v1\x1a\x1dyandex/cloud/validation.proto\"\x80\x01\n\x0bVersionInfo\x12\x17\n\x0f\x63urrent_version\x18\x01 \x01(\t\x12\x1e\n\x16new_revision_available\x18\x02 \x01(\x08\x12\x1c\n\x14new_revision_summary\x18\x03 \x01(\t\x12\x1a\n\x12version_deprecated\x18\x04 \x01(\x08\"T\n\x11UpdateVersionSpec\x12\x11\n\x07version\x18\x01 \x01(\tH\x00\x12\x19\n\x0flatest_revision\x18\x02 \x01(\x08H\x00\x42\x11\n\tspecifier\x12\x04\xc0\xc1\x31\x01\x42V\n\x17yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8sb\x06proto3')
  ,
  dependencies=[yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_VERSIONINFO = _descriptor.Descriptor(
  name='VersionInfo',
  full_name='yandex.cloud.k8s.v1.VersionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_version', full_name='yandex.cloud.k8s.v1.VersionInfo.current_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_revision_available', full_name='yandex.cloud.k8s.v1.VersionInfo.new_revision_available', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_revision_summary', full_name='yandex.cloud.k8s.v1.VersionInfo.new_revision_summary', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_deprecated', full_name='yandex.cloud.k8s.v1.VersionInfo.version_deprecated', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=90,
  serialized_end=218,
)


_UPDATEVERSIONSPEC = _descriptor.Descriptor(
  name='UpdateVersionSpec',
  full_name='yandex.cloud.k8s.v1.UpdateVersionSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='yandex.cloud.k8s.v1.UpdateVersionSpec.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latest_revision', full_name='yandex.cloud.k8s.v1.UpdateVersionSpec.latest_revision', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='specifier', full_name='yandex.cloud.k8s.v1.UpdateVersionSpec.specifier',
      index=0, containing_type=None, fields=[], serialized_options=_b('\300\3011\001')),
  ],
  serialized_start=220,
  serialized_end=304,
)

_UPDATEVERSIONSPEC.oneofs_by_name['specifier'].fields.append(
  _UPDATEVERSIONSPEC.fields_by_name['version'])
_UPDATEVERSIONSPEC.fields_by_name['version'].containing_oneof = _UPDATEVERSIONSPEC.oneofs_by_name['specifier']
_UPDATEVERSIONSPEC.oneofs_by_name['specifier'].fields.append(
  _UPDATEVERSIONSPEC.fields_by_name['latest_revision'])
_UPDATEVERSIONSPEC.fields_by_name['latest_revision'].containing_oneof = _UPDATEVERSIONSPEC.oneofs_by_name['specifier']
DESCRIPTOR.message_types_by_name['VersionInfo'] = _VERSIONINFO
DESCRIPTOR.message_types_by_name['UpdateVersionSpec'] = _UPDATEVERSIONSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VersionInfo = _reflection.GeneratedProtocolMessageType('VersionInfo', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONINFO,
  '__module__' : 'yandex.cloud.k8s.v1.version_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.VersionInfo)
  })
_sym_db.RegisterMessage(VersionInfo)

UpdateVersionSpec = _reflection.GeneratedProtocolMessageType('UpdateVersionSpec', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVERSIONSPEC,
  '__module__' : 'yandex.cloud.k8s.v1.version_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.UpdateVersionSpec)
  })
_sym_db.RegisterMessage(UpdateVersionSpec)


DESCRIPTOR._options = None
_UPDATEVERSIONSPEC.oneofs_by_name['specifier']._options = None
# @@protoc_insertion_point(module_scope)