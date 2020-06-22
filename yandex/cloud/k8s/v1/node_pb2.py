# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/k8s/v1/node.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/k8s/v1/node.proto',
  package='yandex.cloud.k8s.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8s',
  serialized_pb=b'\n\x1eyandex/cloud/k8s/v1/node.proto\x12\x13yandex.cloud.k8s.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xc7\x05\n\x04Node\x12\x30\n\x06status\x18\x01 \x01(\x0e\x32 .yandex.cloud.k8s.v1.Node.Status\x12,\n\x04spec\x18\x02 \x01(\x0b\x32\x1e.yandex.cloud.k8s.v1.Node.Spec\x12;\n\x0c\x63loud_status\x18\x03 \x01(\x0b\x32%.yandex.cloud.k8s.v1.Node.CloudStatus\x12\x45\n\x11kubernetes_status\x18\x04 \x01(\x0b\x32*.yandex.cloud.k8s.v1.Node.KubernetesStatus\x1a\xbd\x01\n\x10KubernetesStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\nconditions\x18\x02 \x03(\x0b\x32\x1e.yandex.cloud.k8s.v1.Condition\x12*\n\x06taints\x18\x03 \x03(\x0b\x32\x1a.yandex.cloud.k8s.v1.Taint\x12=\n\x10\x61ttached_volumes\x18\x04 \x03(\x0b\x32#.yandex.cloud.k8s.v1.AttachedVolume\x1a\x41\n\x0b\x43loudStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x16\n\x0estatus_message\x18\x03 \x01(\t\x1aj\n\x04Spec\x12\x35\n\tresources\x18\x01 \x01(\x0b\x32\".yandex.cloud.k8s.v1.ResourcesSpec\x12+\n\x04\x64isk\x18\x02 \x01(\x0b\x32\x1d.yandex.cloud.k8s.v1.DiskSpec\"l\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x11\n\rNOT_CONNECTED\x10\x02\x12\r\n\tNOT_READY\x10\x03\x12\t\n\x05READY\x10\x04\x12\x0b\n\x07MISSING\x10\x05\"\xad\x01\n\tCondition\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x37\n\x13last_heartbeat_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14last_transition_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xb1\x01\n\x05Taint\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x31\n\x06\x65\x66\x66\x65\x63t\x18\x03 \x01(\x0e\x32!.yandex.cloud.k8s.v1.Taint.Effect\"Y\n\x06\x45\x66\x66\x65\x63t\x12\x16\n\x12\x45\x46\x46\x45\x43T_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNO_SCHEDULE\x10\x01\x12\x16\n\x12PREFER_NO_SCHEDULE\x10\x02\x12\x0e\n\nNO_EXECUTE\x10\x03\"<\n\x0e\x41ttachedVolume\x12\x13\n\x0b\x64river_name\x18\x01 \x01(\t\x12\x15\n\rvolume_handle\x18\x02 \x01(\t\"\xc1\x03\n\x0cNodeTemplate\x12\x13\n\x0bplatform_id\x18\x01 \x01(\t\x12:\n\x0eresources_spec\x18\x02 \x01(\x0b\x32\".yandex.cloud.k8s.v1.ResourcesSpec\x12\x35\n\x0e\x62oot_disk_spec\x18\x03 \x01(\x0b\x32\x1d.yandex.cloud.k8s.v1.DiskSpec\x12w\n\x08metadata\x18\x04 \x03(\x0b\x32/.yandex.cloud.k8s.v1.NodeTemplate.MetadataEntryB4\x82\xc8\x31\x04<=64\x8a\xc8\x31\x08<=131072\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x12\x12\x10[a-z][-_0-9a-z]*\x12=\n\x0fv4_address_spec\x18\x05 \x01(\x0b\x32$.yandex.cloud.k8s.v1.NodeAddressSpec\x12@\n\x11scheduling_policy\x18\x06 \x01(\x0b\x32%.yandex.cloud.k8s.v1.SchedulingPolicy\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"T\n\x0fNodeAddressSpec\x12\x41\n\x13one_to_one_nat_spec\x18\x01 \x01(\x0b\x32$.yandex.cloud.k8s.v1.OneToOneNatSpec\"E\n\x0fOneToOneNatSpec\x12\x32\n\nip_version\x18\x01 \x01(\x0e\x32\x1e.yandex.cloud.k8s.v1.IpVersion\"\xd7\x01\n\rResourcesSpec\x12\"\n\x06memory\x18\x01 \x01(\x03\x42\x12\xfa\xc7\x31\x0e<=824633720832\x12]\n\x05\x63ores\x18\x02 \x01(\x03\x42N\xfa\xc7\x31J0,1,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,40,44,48,52,56,60,64\x12(\n\rcore_fraction\x18\x03 \x01(\x03\x42\x11\xfa\xc7\x31\r0,5,20,50,100\x12\x19\n\x04gpus\x18\x04 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30,1,2,4\"f\n\x08\x44iskSpec\x12\x32\n\x0c\x64isk_type_id\x18\x01 \x01(\tB\x1c\xf2\xc7\x31\x18|network-ssd|network-hdd\x12&\n\tdisk_size\x18\x02 \x01(\x03\x42\x13\xfa\xc7\x31\x0f\x30-4398046511104\"\'\n\x10SchedulingPolicy\x12\x13\n\x0bpreemptible\x18\x01 \x01(\x08*;\n\tIpVersion\x12\x1a\n\x16IP_VERSION_UNSPECIFIED\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02\x42V\n\x17yandex.cloud.api.k8s.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1;k8sb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])

_IPVERSION = _descriptor.EnumDescriptor(
  name='IpVersion',
  full_name='yandex.cloud.k8s.v1.IpVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IP_VERSION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IPV4', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IPV6', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2223,
  serialized_end=2282,
)
_sym_db.RegisterEnumDescriptor(_IPVERSION)

IpVersion = enum_type_wrapper.EnumTypeWrapper(_IPVERSION)
IP_VERSION_UNSPECIFIED = 0
IPV4 = 1
IPV6 = 2


_NODE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.k8s.v1.Node.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROVISIONING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_CONNECTED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_READY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=723,
  serialized_end=831,
)
_sym_db.RegisterEnumDescriptor(_NODE_STATUS)

_TAINT_EFFECT = _descriptor.EnumDescriptor(
  name='Effect',
  full_name='yandex.cloud.k8s.v1.Taint.Effect',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EFFECT_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_SCHEDULE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREFER_NO_SCHEDULE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_EXECUTE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1098,
  serialized_end=1187,
)
_sym_db.RegisterEnumDescriptor(_TAINT_EFFECT)


_NODE_KUBERNETESSTATUS = _descriptor.Descriptor(
  name='KubernetesStatus',
  full_name='yandex.cloud.k8s.v1.Node.KubernetesStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.k8s.v1.Node.KubernetesStatus.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='yandex.cloud.k8s.v1.Node.KubernetesStatus.conditions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taints', full_name='yandex.cloud.k8s.v1.Node.KubernetesStatus.taints', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attached_volumes', full_name='yandex.cloud.k8s.v1.Node.KubernetesStatus.attached_volumes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=357,
  serialized_end=546,
)

_NODE_CLOUDSTATUS = _descriptor.Descriptor(
  name='CloudStatus',
  full_name='yandex.cloud.k8s.v1.Node.CloudStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.k8s.v1.Node.CloudStatus.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.k8s.v1.Node.CloudStatus.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_message', full_name='yandex.cloud.k8s.v1.Node.CloudStatus.status_message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=548,
  serialized_end=613,
)

_NODE_SPEC = _descriptor.Descriptor(
  name='Spec',
  full_name='yandex.cloud.k8s.v1.Node.Spec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='yandex.cloud.k8s.v1.Node.Spec.resources', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk', full_name='yandex.cloud.k8s.v1.Node.Spec.disk', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=615,
  serialized_end=721,
)

_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='yandex.cloud.k8s.v1.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.k8s.v1.Node.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='yandex.cloud.k8s.v1.Node.spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloud_status', full_name='yandex.cloud.k8s.v1.Node.cloud_status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kubernetes_status', full_name='yandex.cloud.k8s.v1.Node.kubernetes_status', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NODE_KUBERNETESSTATUS, _NODE_CLOUDSTATUS, _NODE_SPEC, ],
  enum_types=[
    _NODE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=831,
)


_CONDITION = _descriptor.Descriptor(
  name='Condition',
  full_name='yandex.cloud.k8s.v1.Condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.k8s.v1.Condition.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.k8s.v1.Condition.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='yandex.cloud.k8s.v1.Condition.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_heartbeat_time', full_name='yandex.cloud.k8s.v1.Condition.last_heartbeat_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_transition_time', full_name='yandex.cloud.k8s.v1.Condition.last_transition_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=834,
  serialized_end=1007,
)


_TAINT = _descriptor.Descriptor(
  name='Taint',
  full_name='yandex.cloud.k8s.v1.Taint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.k8s.v1.Taint.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.k8s.v1.Taint.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effect', full_name='yandex.cloud.k8s.v1.Taint.effect', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TAINT_EFFECT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1010,
  serialized_end=1187,
)


_ATTACHEDVOLUME = _descriptor.Descriptor(
  name='AttachedVolume',
  full_name='yandex.cloud.k8s.v1.AttachedVolume',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='driver_name', full_name='yandex.cloud.k8s.v1.AttachedVolume.driver_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume_handle', full_name='yandex.cloud.k8s.v1.AttachedVolume.volume_handle', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1189,
  serialized_end=1249,
)


_NODETEMPLATE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='yandex.cloud.k8s.v1.NodeTemplate.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.k8s.v1.NodeTemplate.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.k8s.v1.NodeTemplate.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1654,
  serialized_end=1701,
)

_NODETEMPLATE = _descriptor.Descriptor(
  name='NodeTemplate',
  full_name='yandex.cloud.k8s.v1.NodeTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='platform_id', full_name='yandex.cloud.k8s.v1.NodeTemplate.platform_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resources_spec', full_name='yandex.cloud.k8s.v1.NodeTemplate.resources_spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot_disk_spec', full_name='yandex.cloud.k8s.v1.NodeTemplate.boot_disk_spec', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='yandex.cloud.k8s.v1.NodeTemplate.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\004<=64\212\3101\010<=131072\262\3101\006\032\0041-63\262\3101\022\022\020[a-z][-_0-9a-z]*', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v4_address_spec', full_name='yandex.cloud.k8s.v1.NodeTemplate.v4_address_spec', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheduling_policy', full_name='yandex.cloud.k8s.v1.NodeTemplate.scheduling_policy', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NODETEMPLATE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1252,
  serialized_end=1701,
)


_NODEADDRESSSPEC = _descriptor.Descriptor(
  name='NodeAddressSpec',
  full_name='yandex.cloud.k8s.v1.NodeAddressSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='one_to_one_nat_spec', full_name='yandex.cloud.k8s.v1.NodeAddressSpec.one_to_one_nat_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1703,
  serialized_end=1787,
)


_ONETOONENATSPEC = _descriptor.Descriptor(
  name='OneToOneNatSpec',
  full_name='yandex.cloud.k8s.v1.OneToOneNatSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_version', full_name='yandex.cloud.k8s.v1.OneToOneNatSpec.ip_version', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=1789,
  serialized_end=1858,
)


_RESOURCESSPEC = _descriptor.Descriptor(
  name='ResourcesSpec',
  full_name='yandex.cloud.k8s.v1.ResourcesSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='memory', full_name='yandex.cloud.k8s.v1.ResourcesSpec.memory', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\016<=824633720832', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cores', full_name='yandex.cloud.k8s.v1.ResourcesSpec.cores', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071J0,1,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,40,44,48,52,56,60,64', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='core_fraction', full_name='yandex.cloud.k8s.v1.ResourcesSpec.core_fraction', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\r0,5,20,50,100', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpus', full_name='yandex.cloud.k8s.v1.ResourcesSpec.gpus', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0070,1,2,4', file=DESCRIPTOR),
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
  serialized_start=1861,
  serialized_end=2076,
)


_DISKSPEC = _descriptor.Descriptor(
  name='DiskSpec',
  full_name='yandex.cloud.k8s.v1.DiskSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disk_type_id', full_name='yandex.cloud.k8s.v1.DiskSpec.disk_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\3071\030|network-ssd|network-hdd', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_size', full_name='yandex.cloud.k8s.v1.DiskSpec.disk_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0170-4398046511104', file=DESCRIPTOR),
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
  serialized_start=2078,
  serialized_end=2180,
)


_SCHEDULINGPOLICY = _descriptor.Descriptor(
  name='SchedulingPolicy',
  full_name='yandex.cloud.k8s.v1.SchedulingPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='preemptible', full_name='yandex.cloud.k8s.v1.SchedulingPolicy.preemptible', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=2182,
  serialized_end=2221,
)

_NODE_KUBERNETESSTATUS.fields_by_name['conditions'].message_type = _CONDITION
_NODE_KUBERNETESSTATUS.fields_by_name['taints'].message_type = _TAINT
_NODE_KUBERNETESSTATUS.fields_by_name['attached_volumes'].message_type = _ATTACHEDVOLUME
_NODE_KUBERNETESSTATUS.containing_type = _NODE
_NODE_CLOUDSTATUS.containing_type = _NODE
_NODE_SPEC.fields_by_name['resources'].message_type = _RESOURCESSPEC
_NODE_SPEC.fields_by_name['disk'].message_type = _DISKSPEC
_NODE_SPEC.containing_type = _NODE
_NODE.fields_by_name['status'].enum_type = _NODE_STATUS
_NODE.fields_by_name['spec'].message_type = _NODE_SPEC
_NODE.fields_by_name['cloud_status'].message_type = _NODE_CLOUDSTATUS
_NODE.fields_by_name['kubernetes_status'].message_type = _NODE_KUBERNETESSTATUS
_NODE_STATUS.containing_type = _NODE
_CONDITION.fields_by_name['last_heartbeat_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONDITION.fields_by_name['last_transition_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TAINT.fields_by_name['effect'].enum_type = _TAINT_EFFECT
_TAINT_EFFECT.containing_type = _TAINT
_NODETEMPLATE_METADATAENTRY.containing_type = _NODETEMPLATE
_NODETEMPLATE.fields_by_name['resources_spec'].message_type = _RESOURCESSPEC
_NODETEMPLATE.fields_by_name['boot_disk_spec'].message_type = _DISKSPEC
_NODETEMPLATE.fields_by_name['metadata'].message_type = _NODETEMPLATE_METADATAENTRY
_NODETEMPLATE.fields_by_name['v4_address_spec'].message_type = _NODEADDRESSSPEC
_NODETEMPLATE.fields_by_name['scheduling_policy'].message_type = _SCHEDULINGPOLICY
_NODEADDRESSSPEC.fields_by_name['one_to_one_nat_spec'].message_type = _ONETOONENATSPEC
_ONETOONENATSPEC.fields_by_name['ip_version'].enum_type = _IPVERSION
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Condition'] = _CONDITION
DESCRIPTOR.message_types_by_name['Taint'] = _TAINT
DESCRIPTOR.message_types_by_name['AttachedVolume'] = _ATTACHEDVOLUME
DESCRIPTOR.message_types_by_name['NodeTemplate'] = _NODETEMPLATE
DESCRIPTOR.message_types_by_name['NodeAddressSpec'] = _NODEADDRESSSPEC
DESCRIPTOR.message_types_by_name['OneToOneNatSpec'] = _ONETOONENATSPEC
DESCRIPTOR.message_types_by_name['ResourcesSpec'] = _RESOURCESSPEC
DESCRIPTOR.message_types_by_name['DiskSpec'] = _DISKSPEC
DESCRIPTOR.message_types_by_name['SchedulingPolicy'] = _SCHEDULINGPOLICY
DESCRIPTOR.enum_types_by_name['IpVersion'] = _IPVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {

  'KubernetesStatus' : _reflection.GeneratedProtocolMessageType('KubernetesStatus', (_message.Message,), {
    'DESCRIPTOR' : _NODE_KUBERNETESSTATUS,
    '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.Node.KubernetesStatus)
    })
  ,

  'CloudStatus' : _reflection.GeneratedProtocolMessageType('CloudStatus', (_message.Message,), {
    'DESCRIPTOR' : _NODE_CLOUDSTATUS,
    '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.Node.CloudStatus)
    })
  ,

  'Spec' : _reflection.GeneratedProtocolMessageType('Spec', (_message.Message,), {
    'DESCRIPTOR' : _NODE_SPEC,
    '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.Node.Spec)
    })
  ,
  'DESCRIPTOR' : _NODE,
  '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.Node)
  })
_sym_db.RegisterMessage(Node)
_sym_db.RegisterMessage(Node.KubernetesStatus)
_sym_db.RegisterMessage(Node.CloudStatus)
_sym_db.RegisterMessage(Node.Spec)

Condition = _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), {
  'DESCRIPTOR' : _CONDITION,
  '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.Condition)
  })
_sym_db.RegisterMessage(Condition)

Taint = _reflection.GeneratedProtocolMessageType('Taint', (_message.Message,), {
  'DESCRIPTOR' : _TAINT,
  '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.Taint)
  })
_sym_db.RegisterMessage(Taint)

AttachedVolume = _reflection.GeneratedProtocolMessageType('AttachedVolume', (_message.Message,), {
  'DESCRIPTOR' : _ATTACHEDVOLUME,
  '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.AttachedVolume)
  })
_sym_db.RegisterMessage(AttachedVolume)

NodeTemplate = _reflection.GeneratedProtocolMessageType('NodeTemplate', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _NODETEMPLATE_METADATAENTRY,
    '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.NodeTemplate.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _NODETEMPLATE,
  '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.NodeTemplate)
  })
_sym_db.RegisterMessage(NodeTemplate)
_sym_db.RegisterMessage(NodeTemplate.MetadataEntry)

NodeAddressSpec = _reflection.GeneratedProtocolMessageType('NodeAddressSpec', (_message.Message,), {
  'DESCRIPTOR' : _NODEADDRESSSPEC,
  '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.NodeAddressSpec)
  })
_sym_db.RegisterMessage(NodeAddressSpec)

OneToOneNatSpec = _reflection.GeneratedProtocolMessageType('OneToOneNatSpec', (_message.Message,), {
  'DESCRIPTOR' : _ONETOONENATSPEC,
  '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.OneToOneNatSpec)
  })
_sym_db.RegisterMessage(OneToOneNatSpec)

ResourcesSpec = _reflection.GeneratedProtocolMessageType('ResourcesSpec', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCESSPEC,
  '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.ResourcesSpec)
  })
_sym_db.RegisterMessage(ResourcesSpec)

DiskSpec = _reflection.GeneratedProtocolMessageType('DiskSpec', (_message.Message,), {
  'DESCRIPTOR' : _DISKSPEC,
  '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.DiskSpec)
  })
_sym_db.RegisterMessage(DiskSpec)

SchedulingPolicy = _reflection.GeneratedProtocolMessageType('SchedulingPolicy', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULINGPOLICY,
  '__module__' : 'yandex.cloud.k8s.v1.node_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.k8s.v1.SchedulingPolicy)
  })
_sym_db.RegisterMessage(SchedulingPolicy)


DESCRIPTOR._options = None
_NODETEMPLATE_METADATAENTRY._options = None
_NODETEMPLATE.fields_by_name['metadata']._options = None
_RESOURCESSPEC.fields_by_name['memory']._options = None
_RESOURCESSPEC.fields_by_name['cores']._options = None
_RESOURCESSPEC.fields_by_name['core_fraction']._options = None
_RESOURCESSPEC.fields_by_name['gpus']._options = None
_DISKSPEC.fields_by_name['disk_type_id']._options = None
_DISKSPEC.fields_by_name['disk_size']._options = None
# @@protoc_insertion_point(module_scope)