# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_key.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'yandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_key.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHyandex/cloud/kms/v1/asymmetricencryption/asymmetric_encryption_key.proto\x12(yandex.cloud.kms.v1.asymmetricencryption\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc1\x04\n\x17\x41symmetricEncryptionKey\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12]\n\x06labels\x18\x06 \x03(\x0b\x32M.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.LabelsEntry\x12X\n\x06status\x18\x07 \x01(\x0e\x32H.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionKey.Status\x12\x65\n\x14\x65ncryption_algorithm\x18\x08 \x01(\x0e\x32G.yandex.cloud.kms.v1.asymmetricencryption.AsymmetricEncryptionAlgorithm\x12\x1b\n\x13\x64\x65letion_protection\x18\t \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08INACTIVE\x10\x03*\xad\x01\n\x1d\x41symmetricEncryptionAlgorithm\x12/\n+ASYMMETRIC_ENCRYPTION_ALGORITHM_UNSPECIFIED\x10\x00\x12\x1d\n\x19RSA_2048_ENC_OAEP_SHA_256\x10\x01\x12\x1d\n\x19RSA_3072_ENC_OAEP_SHA_256\x10\x02\x12\x1d\n\x19RSA_4096_ENC_OAEP_SHA_256\x10\x03\x42k\n\x17yandex.cloud.api.kms.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricencryption;kmsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.kms.v1.asymmetricencryption.asymmetric_encryption_key_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.kms.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricencryption;kms'
  _globals['_ASYMMETRICENCRYPTIONKEY_LABELSENTRY']._loaded_options = None
  _globals['_ASYMMETRICENCRYPTIONKEY_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_ASYMMETRICENCRYPTIONALGORITHM']._serialized_start=732
  _globals['_ASYMMETRICENCRYPTIONALGORITHM']._serialized_end=905
  _globals['_ASYMMETRICENCRYPTIONKEY']._serialized_start=152
  _globals['_ASYMMETRICENCRYPTIONKEY']._serialized_end=729
  _globals['_ASYMMETRICENCRYPTIONKEY_LABELSENTRY']._serialized_start=610
  _globals['_ASYMMETRICENCRYPTIONKEY_LABELSENTRY']._serialized_end=655
  _globals['_ASYMMETRICENCRYPTIONKEY_STATUS']._serialized_start=657
  _globals['_ASYMMETRICENCRYPTIONKEY_STATUS']._serialized_end=729
# @@protoc_insertion_point(module_scope)
