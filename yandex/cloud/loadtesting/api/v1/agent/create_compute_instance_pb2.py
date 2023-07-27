# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/loadtesting/api/v1/agent/create_compute_instance.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.compute.v1 import instance_service_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/loadtesting/api/v1/agent/create_compute_instance.proto',
  package='yandex.cloud.loadtesting.api.v1.agent',
  syntax='proto3',
  serialized_options=b'\n)yandex.cloud.api.loadtesting.api.v1.agentZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/api/v1/agent;agent',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCyandex/cloud/loadtesting/api/v1/agent/create_compute_instance.proto\x12%yandex.cloud.loadtesting.api.v1.agent\x1a.yandex/cloud/compute/v1/instance_service.proto\x1a\x1dyandex/cloud/validation.proto\"\x9a\x05\n\x15\x43reateComputeInstance\x12\xa1\x01\n\x06labels\x18\x04 \x03(\x0b\x32H.yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.LabelsEntryBG\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x16\x12\x14[a-z][-_./\\@0-9a-z]*\x12\x1d\n\x07zone_id\x18\x05 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x44\n\x0eresources_spec\x18\x07 \x01(\x0b\x32&.yandex.cloud.compute.v1.ResourcesSpecB\x04\xe8\xc7\x31\x01\x12\\\n\x08metadata\x18\x08 \x03(\x0b\x32J.yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.MetadataEntry\x12G\n\x0e\x62oot_disk_spec\x18\t \x01(\x0b\x32).yandex.cloud.compute.v1.AttachedDiskSpecB\x04\xe8\xc7\x31\x01\x12U\n\x17network_interface_specs\x18\x0b \x03(\x0b\x32-.yandex.cloud.compute.v1.NetworkInterfaceSpecB\x05\x82\xc8\x31\x01\x31\x12\x1a\n\x12service_account_id\x18\x0e \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42|\n)yandex.cloud.api.loadtesting.api.v1.agentZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/api/v1/agent;agentb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_CREATECOMPUTEINSTANCE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=762,
  serialized_end=807,
)

_CREATECOMPUTEINSTANCE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=809,
  serialized_end=856,
)

_CREATECOMPUTEINSTANCE = _descriptor.Descriptor(
  name='CreateComputeInstance',
  full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.labels', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\004<=64\212\3101\004<=63\362\3071\017[-_./\\@0-9a-z]*\262\3101\006\032\0041-63\262\3101\026\022\024[a-z][-_./\\@0-9a-z]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.zone_id', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resources_spec', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.resources_spec', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.metadata', index=3,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boot_disk_spec', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.boot_disk_spec', index=4,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_interface_specs', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.network_interface_specs', index=5,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\0011', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.service_account_id', index=6,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CREATECOMPUTEINSTANCE_LABELSENTRY, _CREATECOMPUTEINSTANCE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=856,
)

_CREATECOMPUTEINSTANCE_LABELSENTRY.containing_type = _CREATECOMPUTEINSTANCE
_CREATECOMPUTEINSTANCE_METADATAENTRY.containing_type = _CREATECOMPUTEINSTANCE
_CREATECOMPUTEINSTANCE.fields_by_name['labels'].message_type = _CREATECOMPUTEINSTANCE_LABELSENTRY
_CREATECOMPUTEINSTANCE.fields_by_name['resources_spec'].message_type = yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2._RESOURCESSPEC
_CREATECOMPUTEINSTANCE.fields_by_name['metadata'].message_type = _CREATECOMPUTEINSTANCE_METADATAENTRY
_CREATECOMPUTEINSTANCE.fields_by_name['boot_disk_spec'].message_type = yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2._ATTACHEDDISKSPEC
_CREATECOMPUTEINSTANCE.fields_by_name['network_interface_specs'].message_type = yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2._NETWORKINTERFACESPEC
DESCRIPTOR.message_types_by_name['CreateComputeInstance'] = _CREATECOMPUTEINSTANCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateComputeInstance = _reflection.GeneratedProtocolMessageType('CreateComputeInstance', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATECOMPUTEINSTANCE_LABELSENTRY,
    '__module__' : 'yandex.cloud.loadtesting.api.v1.agent.create_compute_instance_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.LabelsEntry)
    })
  ,

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATECOMPUTEINSTANCE_METADATAENTRY,
    '__module__' : 'yandex.cloud.loadtesting.api.v1.agent.create_compute_instance_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _CREATECOMPUTEINSTANCE,
  '__module__' : 'yandex.cloud.loadtesting.api.v1.agent.create_compute_instance_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.loadtesting.api.v1.agent.CreateComputeInstance)
  })
_sym_db.RegisterMessage(CreateComputeInstance)
_sym_db.RegisterMessage(CreateComputeInstance.LabelsEntry)
_sym_db.RegisterMessage(CreateComputeInstance.MetadataEntry)


DESCRIPTOR._options = None
_CREATECOMPUTEINSTANCE_LABELSENTRY._options = None
_CREATECOMPUTEINSTANCE_METADATAENTRY._options = None
_CREATECOMPUTEINSTANCE.fields_by_name['labels']._options = None
_CREATECOMPUTEINSTANCE.fields_by_name['zone_id']._options = None
_CREATECOMPUTEINSTANCE.fields_by_name['resources_spec']._options = None
_CREATECOMPUTEINSTANCE.fields_by_name['boot_disk_spec']._options = None
_CREATECOMPUTEINSTANCE.fields_by_name['network_interface_specs']._options = None
# @@protoc_insertion_point(module_scope)