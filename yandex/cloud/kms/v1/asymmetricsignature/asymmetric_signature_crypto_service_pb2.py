# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/kms/v1/asymmetricsignature/asymmetric_signature_crypto_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/kms/v1/asymmetricsignature/asymmetric_signature_crypto_service.proto',
  package='yandex.cloud.kms.v1.asymmetricsignature',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.kms.v1ZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricsignature;kms',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nQyandex/cloud/kms/v1/asymmetricsignature/asymmetric_signature_crypto_service.proto\x12\'yandex.cloud.kms.v1.asymmetricsignature\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\"W\n\x15\x41symmetricSignRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12 \n\x07message\x18\x02 \x01(\x0c\x42\x0f\xe8\xc7\x31\x01\x8a\xc8\x31\x07<=32768\";\n\x16\x41symmetricSignResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"W\n\x19\x41symmetricSignHashRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\x04hash\x18\x02 \x01(\x0c\x42\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=4096\"?\n\x1a\x41symmetricSignHashResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"=\n\x1d\x41symmetricGetPublicKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"D\n\x1e\x41symmetricGetPublicKeyResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x12\n\npublic_key\x18\x02 \x01(\t2\x98\x05\n AsymmetricSignatureCryptoService\x12\xc1\x01\n\x04Sign\x12>.yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignRequest\x1a?.yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignResponse\"8\x82\xd3\xe4\x93\x02\x32\"-/kms/v1/asymmetricSignatureKeys/{key_id}:sign:\x01*\x12\xd1\x01\n\x08SignHash\x12\x42.yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignHashRequest\x1a\x43.yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignHashResponse\"<\x82\xd3\xe4\x93\x02\x36\"1/kms/v1/asymmetricSignatureKeys/{key_id}:signHash:\x01*\x12\xdb\x01\n\x0cGetPublicKey\x12\x46.yandex.cloud.kms.v1.asymmetricsignature.AsymmetricGetPublicKeyRequest\x1aG.yandex.cloud.kms.v1.asymmetricsignature.AsymmetricGetPublicKeyResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/kms/v1/asymmetricSignatureKeys/{key_id}/publicKeyBj\n\x17yandex.cloud.api.kms.v1ZOgithub.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1/asymmetricsignature;kmsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_ASYMMETRICSIGNREQUEST = _descriptor.Descriptor(
  name='AsymmetricSignRequest',
  full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignRequest.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignRequest.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\007<=32768', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=187,
  serialized_end=274,
)


_ASYMMETRICSIGNRESPONSE = _descriptor.Descriptor(
  name='AsymmetricSignResponse',
  full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignResponse.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignResponse.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=276,
  serialized_end=335,
)


_ASYMMETRICSIGNHASHREQUEST = _descriptor.Descriptor(
  name='AsymmetricSignHashRequest',
  full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignHashRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignHashRequest.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignHashRequest.hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\006<=4096', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=337,
  serialized_end=424,
)


_ASYMMETRICSIGNHASHRESPONSE = _descriptor.Descriptor(
  name='AsymmetricSignHashResponse',
  full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignHashResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignHashResponse.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignHashResponse.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=426,
  serialized_end=489,
)


_ASYMMETRICGETPUBLICKEYREQUEST = _descriptor.Descriptor(
  name='AsymmetricGetPublicKeyRequest',
  full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricGetPublicKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricGetPublicKeyRequest.key_id', index=0,
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
  serialized_start=491,
  serialized_end=552,
)


_ASYMMETRICGETPUBLICKEYRESPONSE = _descriptor.Descriptor(
  name='AsymmetricGetPublicKeyResponse',
  full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricGetPublicKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricGetPublicKeyResponse.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricGetPublicKeyResponse.public_key', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=622,
)

DESCRIPTOR.message_types_by_name['AsymmetricSignRequest'] = _ASYMMETRICSIGNREQUEST
DESCRIPTOR.message_types_by_name['AsymmetricSignResponse'] = _ASYMMETRICSIGNRESPONSE
DESCRIPTOR.message_types_by_name['AsymmetricSignHashRequest'] = _ASYMMETRICSIGNHASHREQUEST
DESCRIPTOR.message_types_by_name['AsymmetricSignHashResponse'] = _ASYMMETRICSIGNHASHRESPONSE
DESCRIPTOR.message_types_by_name['AsymmetricGetPublicKeyRequest'] = _ASYMMETRICGETPUBLICKEYREQUEST
DESCRIPTOR.message_types_by_name['AsymmetricGetPublicKeyResponse'] = _ASYMMETRICGETPUBLICKEYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AsymmetricSignRequest = _reflection.GeneratedProtocolMessageType('AsymmetricSignRequest', (_message.Message,), {
  'DESCRIPTOR' : _ASYMMETRICSIGNREQUEST,
  '__module__' : 'yandex.cloud.kms.v1.asymmetricsignature.asymmetric_signature_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignRequest)
  })
_sym_db.RegisterMessage(AsymmetricSignRequest)

AsymmetricSignResponse = _reflection.GeneratedProtocolMessageType('AsymmetricSignResponse', (_message.Message,), {
  'DESCRIPTOR' : _ASYMMETRICSIGNRESPONSE,
  '__module__' : 'yandex.cloud.kms.v1.asymmetricsignature.asymmetric_signature_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignResponse)
  })
_sym_db.RegisterMessage(AsymmetricSignResponse)

AsymmetricSignHashRequest = _reflection.GeneratedProtocolMessageType('AsymmetricSignHashRequest', (_message.Message,), {
  'DESCRIPTOR' : _ASYMMETRICSIGNHASHREQUEST,
  '__module__' : 'yandex.cloud.kms.v1.asymmetricsignature.asymmetric_signature_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignHashRequest)
  })
_sym_db.RegisterMessage(AsymmetricSignHashRequest)

AsymmetricSignHashResponse = _reflection.GeneratedProtocolMessageType('AsymmetricSignHashResponse', (_message.Message,), {
  'DESCRIPTOR' : _ASYMMETRICSIGNHASHRESPONSE,
  '__module__' : 'yandex.cloud.kms.v1.asymmetricsignature.asymmetric_signature_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignHashResponse)
  })
_sym_db.RegisterMessage(AsymmetricSignHashResponse)

AsymmetricGetPublicKeyRequest = _reflection.GeneratedProtocolMessageType('AsymmetricGetPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _ASYMMETRICGETPUBLICKEYREQUEST,
  '__module__' : 'yandex.cloud.kms.v1.asymmetricsignature.asymmetric_signature_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.asymmetricsignature.AsymmetricGetPublicKeyRequest)
  })
_sym_db.RegisterMessage(AsymmetricGetPublicKeyRequest)

AsymmetricGetPublicKeyResponse = _reflection.GeneratedProtocolMessageType('AsymmetricGetPublicKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _ASYMMETRICGETPUBLICKEYRESPONSE,
  '__module__' : 'yandex.cloud.kms.v1.asymmetricsignature.asymmetric_signature_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.asymmetricsignature.AsymmetricGetPublicKeyResponse)
  })
_sym_db.RegisterMessage(AsymmetricGetPublicKeyResponse)


DESCRIPTOR._options = None
_ASYMMETRICSIGNREQUEST.fields_by_name['key_id']._options = None
_ASYMMETRICSIGNREQUEST.fields_by_name['message']._options = None
_ASYMMETRICSIGNHASHREQUEST.fields_by_name['key_id']._options = None
_ASYMMETRICSIGNHASHREQUEST.fields_by_name['hash']._options = None
_ASYMMETRICGETPUBLICKEYREQUEST.fields_by_name['key_id']._options = None

_ASYMMETRICSIGNATURECRYPTOSERVICE = _descriptor.ServiceDescriptor(
  name='AsymmetricSignatureCryptoService',
  full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignatureCryptoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=625,
  serialized_end=1289,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sign',
    full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignatureCryptoService.Sign',
    index=0,
    containing_service=None,
    input_type=_ASYMMETRICSIGNREQUEST,
    output_type=_ASYMMETRICSIGNRESPONSE,
    serialized_options=b'\202\323\344\223\0022\"-/kms/v1/asymmetricSignatureKeys/{key_id}:sign:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SignHash',
    full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignatureCryptoService.SignHash',
    index=1,
    containing_service=None,
    input_type=_ASYMMETRICSIGNHASHREQUEST,
    output_type=_ASYMMETRICSIGNHASHRESPONSE,
    serialized_options=b'\202\323\344\223\0026\"1/kms/v1/asymmetricSignatureKeys/{key_id}:signHash:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPublicKey',
    full_name='yandex.cloud.kms.v1.asymmetricsignature.AsymmetricSignatureCryptoService.GetPublicKey',
    index=2,
    containing_service=None,
    input_type=_ASYMMETRICGETPUBLICKEYREQUEST,
    output_type=_ASYMMETRICGETPUBLICKEYRESPONSE,
    serialized_options=b'\202\323\344\223\0024\0222/kms/v1/asymmetricSignatureKeys/{key_id}/publicKey',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ASYMMETRICSIGNATURECRYPTOSERVICE)

DESCRIPTOR.services_by_name['AsymmetricSignatureCryptoService'] = _ASYMMETRICSIGNATURECRYPTOSERVICE

# @@protoc_insertion_point(module_scope)