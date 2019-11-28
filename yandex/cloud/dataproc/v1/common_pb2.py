# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dataproc/v1/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/dataproc/v1/common.proto',
  package='yandex.cloud.dataproc.v1',
  syntax='proto3',
  serialized_options=_b('\n\034yandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataproc'),
  serialized_pb=_b('\n%yandex/cloud/dataproc/v1/common.proto\x12\x18yandex.cloud.dataproc.v1\"P\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isk_type_id\x18\x02 \x01(\t\x12\x11\n\tdisk_size\x18\x03 \x01(\x03*?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\x42\x65\n\x1cyandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataprocb\x06proto3')
)

_HEALTH = _descriptor.EnumDescriptor(
  name='Health',
  full_name='yandex.cloud.dataproc.v1.Health',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HEALTH_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALIVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEAD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEGRADED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=149,
  serialized_end=212,
)
_sym_db.RegisterEnumDescriptor(_HEALTH)

Health = enum_type_wrapper.EnumTypeWrapper(_HEALTH)
HEALTH_UNKNOWN = 0
ALIVE = 1
DEAD = 2
DEGRADED = 3



_RESOURCES = _descriptor.Descriptor(
  name='Resources',
  full_name='yandex.cloud.dataproc.v1.Resources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_preset_id', full_name='yandex.cloud.dataproc.v1.Resources.resource_preset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_type_id', full_name='yandex.cloud.dataproc.v1.Resources.disk_type_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_size', full_name='yandex.cloud.dataproc.v1.Resources.disk_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=67,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.enum_types_by_name['Health'] = _HEALTH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Resources = _reflection.GeneratedProtocolMessageType('Resources', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCES,
  __module__ = 'yandex.cloud.dataproc.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.Resources)
  ))
_sym_db.RegisterMessage(Resources)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
