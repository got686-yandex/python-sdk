# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/compute/v1/hardware_generation.proto
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
    'yandex/cloud/compute/v1/hardware_generation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/compute/v1/hardware_generation.proto\x12\x17yandex.cloud.compute.v1\"\xc2\x01\n\x12HardwareGeneration\x12J\n\x0flegacy_features\x18\x01 \x01(\x0b\x32/.yandex.cloud.compute.v1.LegacyHardwareFeaturesH\x00\x12T\n\x14generation2_features\x18\x02 \x01(\x0b\x32\x34.yandex.cloud.compute.v1.Generation2HardwareFeaturesH\x00\x42\n\n\x08\x66\x65\x61tures\"T\n\x16LegacyHardwareFeatures\x12:\n\x0cpci_topology\x18\x01 \x01(\x0e\x32$.yandex.cloud.compute.v1.PCITopology\"\x1d\n\x1bGeneration2HardwareFeatures*U\n\x0bPCITopology\x12\x1c\n\x18PCI_TOPOLOGY_UNSPECIFIED\x10\x00\x12\x13\n\x0fPCI_TOPOLOGY_V1\x10\x01\x12\x13\n\x0fPCI_TOPOLOGY_V2\x10\x02\x42\x62\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.hardware_generation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _globals['_PCITOPOLOGY']._serialized_start=392
  _globals['_PCITOPOLOGY']._serialized_end=477
  _globals['_HARDWAREGENERATION']._serialized_start=79
  _globals['_HARDWAREGENERATION']._serialized_end=273
  _globals['_LEGACYHARDWAREFEATURES']._serialized_start=275
  _globals['_LEGACYHARDWAREFEATURES']._serialized_end=359
  _globals['_GENERATION2HARDWAREFEATURES']._serialized_start=361
  _globals['_GENERATION2HARDWAREFEATURES']._serialized_end=390
# @@protoc_insertion_point(module_scope)
