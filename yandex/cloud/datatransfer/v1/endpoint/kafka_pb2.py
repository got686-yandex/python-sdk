# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/kafka.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.datatransfer.v1.endpoint import common_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2
from yandex.cloud.datatransfer.v1.endpoint import parsers_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_parsers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datatransfer/v1/endpoint/kafka.proto',
  package='yandex.cloud.datatransfer.v1.endpoint',
  syntax='proto3',
  serialized_options=b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\252\002%Yandex.Cloud.Datatransfer.V1.EndPoint',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1yandex/cloud/datatransfer/v1/endpoint/kafka.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x32yandex/cloud/datatransfer/v1/endpoint/common.proto\x1a\x33yandex/cloud/datatransfer/v1/endpoint/parsers.proto\"\x89\x01\n\x16KafkaConnectionOptions\x12\x14\n\ncluster_id\x18\x01 \x01(\tH\x00\x12K\n\non_premise\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.datatransfer.v1.endpoint.OnPremiseKafkaH\x00\x42\x0c\n\nconnection\"z\n\x0eOnPremiseKafka\x12\x13\n\x0b\x62roker_urls\x18\x01 \x03(\t\x12@\n\x08tls_mode\x18\x05 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.endpoint.TLSMode\x12\x11\n\tsubnet_id\x18\x04 \x01(\t\"\xa3\x01\n\tKafkaAuth\x12H\n\x04sasl\x18\x01 \x01(\x0b\x32\x38.yandex.cloud.datatransfer.v1.endpoint.KafkaSaslSecurityH\x00\x12@\n\x07no_auth\x18\x02 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.NoAuthH\x00\x42\n\n\x08security\"\xac\x01\n\x11KafkaSaslSecurity\x12\x0c\n\x04user\x18\x01 \x01(\t\x12?\n\x08password\x18\x04 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12H\n\tmechanism\x18\x03 \x01(\x0e\x32\x35.yandex.cloud.datatransfer.v1.endpoint.KafkaMechanism\"\xe3\x02\n\x0bKafkaSource\x12Q\n\nconnection\x18\x01 \x01(\x0b\x32=.yandex.cloud.datatransfer.v1.endpoint.KafkaConnectionOptions\x12>\n\x04\x61uth\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.datatransfer.v1.endpoint.KafkaAuth\x12\x17\n\x0fsecurity_groups\x18\x03 \x03(\t\x12\x12\n\ntopic_name\x18\x04 \x01(\t\x12U\n\x0btransformer\x18\x05 \x01(\x0b\x32@.yandex.cloud.datatransfer.v1.endpoint.DataTransformationOptions\x12=\n\x06parser\x18\x07 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Parser\"\x92\x02\n\x0bKafkaTarget\x12Q\n\nconnection\x18\x01 \x01(\x0b\x32=.yandex.cloud.datatransfer.v1.endpoint.KafkaConnectionOptions\x12>\n\x04\x61uth\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.datatransfer.v1.endpoint.KafkaAuth\x12\x17\n\x0fsecurity_groups\x18\x03 \x03(\t\x12W\n\x0etopic_settings\x18\x07 \x01(\x0b\x32?.yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopicSettings\"\x8e\x01\n\x18KafkaTargetTopicSettings\x12H\n\x05topic\x18\x01 \x01(\x0b\x32\x37.yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopicH\x00\x12\x16\n\x0ctopic_prefix\x18\x02 \x01(\tH\x00\x42\x10\n\x0etopic_settings\"=\n\x10KafkaTargetTopic\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\x15\n\rsave_tx_order\x18\x02 \x01(\x08*i\n\x0eKafkaMechanism\x12\x1f\n\x1bKAFKA_MECHANISM_UNSPECIFIED\x10\x00\x12\x1a\n\x16KAFKA_MECHANISM_SHA256\x10\x01\x12\x1a\n\x16KAFKA_MECHANISM_SHA512\x10\x02\x42\xa7\x01\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\xaa\x02%Yandex.Cloud.Datatransfer.V1.EndPointb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2.DESCRIPTOR,yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_parsers__pb2.DESCRIPTOR,])

_KAFKAMECHANISM = _descriptor.EnumDescriptor(
  name='KafkaMechanism',
  full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaMechanism',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KAFKA_MECHANISM_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KAFKA_MECHANISM_SHA256', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KAFKA_MECHANISM_SHA512', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1645,
  serialized_end=1750,
)
_sym_db.RegisterEnumDescriptor(_KAFKAMECHANISM)

KafkaMechanism = enum_type_wrapper.EnumTypeWrapper(_KAFKAMECHANISM)
KAFKA_MECHANISM_UNSPECIFIED = 0
KAFKA_MECHANISM_SHA256 = 1
KAFKA_MECHANISM_SHA512 = 2



_KAFKACONNECTIONOPTIONS = _descriptor.Descriptor(
  name='KafkaConnectionOptions',
  full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaConnectionOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaConnectionOptions.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='on_premise', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaConnectionOptions.on_premise', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='connection', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaConnectionOptions.connection',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=198,
  serialized_end=335,
)


_ONPREMISEKAFKA = _descriptor.Descriptor(
  name='OnPremiseKafka',
  full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremiseKafka',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='broker_urls', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremiseKafka.broker_urls', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tls_mode', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremiseKafka.tls_mode', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremiseKafka.subnet_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=337,
  serialized_end=459,
)


_KAFKAAUTH = _descriptor.Descriptor(
  name='KafkaAuth',
  full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaAuth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sasl', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaAuth.sasl', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='no_auth', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaAuth.no_auth', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='security', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaAuth.security',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=462,
  serialized_end=625,
)


_KAFKASASLSECURITY = _descriptor.Descriptor(
  name='KafkaSaslSecurity',
  full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSaslSecurity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSaslSecurity.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSaslSecurity.password', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mechanism', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSaslSecurity.mechanism', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=628,
  serialized_end=800,
)


_KAFKASOURCE = _descriptor.Descriptor(
  name='KafkaSource',
  full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSource.connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auth', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSource.auth', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security_groups', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSource.security_groups', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSource.topic_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transformer', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSource.transformer', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parser', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaSource.parser', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=803,
  serialized_end=1158,
)


_KAFKATARGET = _descriptor.Descriptor(
  name='KafkaTarget',
  full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTarget.connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auth', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTarget.auth', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security_groups', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTarget.security_groups', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic_settings', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTarget.topic_settings', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1161,
  serialized_end=1435,
)


_KAFKATARGETTOPICSETTINGS = _descriptor.Descriptor(
  name='KafkaTargetTopicSettings',
  full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopicSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopicSettings.topic', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic_prefix', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopicSettings.topic_prefix', index=1,
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
    _descriptor.OneofDescriptor(
      name='topic_settings', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopicSettings.topic_settings',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1438,
  serialized_end=1580,
)


_KAFKATARGETTOPIC = _descriptor.Descriptor(
  name='KafkaTargetTopic',
  full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopic.topic_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='save_tx_order', full_name='yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopic.save_tx_order', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1582,
  serialized_end=1643,
)

_KAFKACONNECTIONOPTIONS.fields_by_name['on_premise'].message_type = _ONPREMISEKAFKA
_KAFKACONNECTIONOPTIONS.oneofs_by_name['connection'].fields.append(
  _KAFKACONNECTIONOPTIONS.fields_by_name['cluster_id'])
_KAFKACONNECTIONOPTIONS.fields_by_name['cluster_id'].containing_oneof = _KAFKACONNECTIONOPTIONS.oneofs_by_name['connection']
_KAFKACONNECTIONOPTIONS.oneofs_by_name['connection'].fields.append(
  _KAFKACONNECTIONOPTIONS.fields_by_name['on_premise'])
_KAFKACONNECTIONOPTIONS.fields_by_name['on_premise'].containing_oneof = _KAFKACONNECTIONOPTIONS.oneofs_by_name['connection']
_ONPREMISEKAFKA.fields_by_name['tls_mode'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._TLSMODE
_KAFKAAUTH.fields_by_name['sasl'].message_type = _KAFKASASLSECURITY
_KAFKAAUTH.fields_by_name['no_auth'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._NOAUTH
_KAFKAAUTH.oneofs_by_name['security'].fields.append(
  _KAFKAAUTH.fields_by_name['sasl'])
_KAFKAAUTH.fields_by_name['sasl'].containing_oneof = _KAFKAAUTH.oneofs_by_name['security']
_KAFKAAUTH.oneofs_by_name['security'].fields.append(
  _KAFKAAUTH.fields_by_name['no_auth'])
_KAFKAAUTH.fields_by_name['no_auth'].containing_oneof = _KAFKAAUTH.oneofs_by_name['security']
_KAFKASASLSECURITY.fields_by_name['password'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._SECRET
_KAFKASASLSECURITY.fields_by_name['mechanism'].enum_type = _KAFKAMECHANISM
_KAFKASOURCE.fields_by_name['connection'].message_type = _KAFKACONNECTIONOPTIONS
_KAFKASOURCE.fields_by_name['auth'].message_type = _KAFKAAUTH
_KAFKASOURCE.fields_by_name['transformer'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._DATATRANSFORMATIONOPTIONS
_KAFKASOURCE.fields_by_name['parser'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_parsers__pb2._PARSER
_KAFKATARGET.fields_by_name['connection'].message_type = _KAFKACONNECTIONOPTIONS
_KAFKATARGET.fields_by_name['auth'].message_type = _KAFKAAUTH
_KAFKATARGET.fields_by_name['topic_settings'].message_type = _KAFKATARGETTOPICSETTINGS
_KAFKATARGETTOPICSETTINGS.fields_by_name['topic'].message_type = _KAFKATARGETTOPIC
_KAFKATARGETTOPICSETTINGS.oneofs_by_name['topic_settings'].fields.append(
  _KAFKATARGETTOPICSETTINGS.fields_by_name['topic'])
_KAFKATARGETTOPICSETTINGS.fields_by_name['topic'].containing_oneof = _KAFKATARGETTOPICSETTINGS.oneofs_by_name['topic_settings']
_KAFKATARGETTOPICSETTINGS.oneofs_by_name['topic_settings'].fields.append(
  _KAFKATARGETTOPICSETTINGS.fields_by_name['topic_prefix'])
_KAFKATARGETTOPICSETTINGS.fields_by_name['topic_prefix'].containing_oneof = _KAFKATARGETTOPICSETTINGS.oneofs_by_name['topic_settings']
DESCRIPTOR.message_types_by_name['KafkaConnectionOptions'] = _KAFKACONNECTIONOPTIONS
DESCRIPTOR.message_types_by_name['OnPremiseKafka'] = _ONPREMISEKAFKA
DESCRIPTOR.message_types_by_name['KafkaAuth'] = _KAFKAAUTH
DESCRIPTOR.message_types_by_name['KafkaSaslSecurity'] = _KAFKASASLSECURITY
DESCRIPTOR.message_types_by_name['KafkaSource'] = _KAFKASOURCE
DESCRIPTOR.message_types_by_name['KafkaTarget'] = _KAFKATARGET
DESCRIPTOR.message_types_by_name['KafkaTargetTopicSettings'] = _KAFKATARGETTOPICSETTINGS
DESCRIPTOR.message_types_by_name['KafkaTargetTopic'] = _KAFKATARGETTOPIC
DESCRIPTOR.enum_types_by_name['KafkaMechanism'] = _KAFKAMECHANISM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KafkaConnectionOptions = _reflection.GeneratedProtocolMessageType('KafkaConnectionOptions', (_message.Message,), {
  'DESCRIPTOR' : _KAFKACONNECTIONOPTIONS,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.kafka_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.KafkaConnectionOptions)
  })
_sym_db.RegisterMessage(KafkaConnectionOptions)

OnPremiseKafka = _reflection.GeneratedProtocolMessageType('OnPremiseKafka', (_message.Message,), {
  'DESCRIPTOR' : _ONPREMISEKAFKA,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.kafka_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.OnPremiseKafka)
  })
_sym_db.RegisterMessage(OnPremiseKafka)

KafkaAuth = _reflection.GeneratedProtocolMessageType('KafkaAuth', (_message.Message,), {
  'DESCRIPTOR' : _KAFKAAUTH,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.kafka_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.KafkaAuth)
  })
_sym_db.RegisterMessage(KafkaAuth)

KafkaSaslSecurity = _reflection.GeneratedProtocolMessageType('KafkaSaslSecurity', (_message.Message,), {
  'DESCRIPTOR' : _KAFKASASLSECURITY,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.kafka_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.KafkaSaslSecurity)
  })
_sym_db.RegisterMessage(KafkaSaslSecurity)

KafkaSource = _reflection.GeneratedProtocolMessageType('KafkaSource', (_message.Message,), {
  'DESCRIPTOR' : _KAFKASOURCE,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.kafka_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.KafkaSource)
  })
_sym_db.RegisterMessage(KafkaSource)

KafkaTarget = _reflection.GeneratedProtocolMessageType('KafkaTarget', (_message.Message,), {
  'DESCRIPTOR' : _KAFKATARGET,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.kafka_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.KafkaTarget)
  })
_sym_db.RegisterMessage(KafkaTarget)

KafkaTargetTopicSettings = _reflection.GeneratedProtocolMessageType('KafkaTargetTopicSettings', (_message.Message,), {
  'DESCRIPTOR' : _KAFKATARGETTOPICSETTINGS,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.kafka_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopicSettings)
  })
_sym_db.RegisterMessage(KafkaTargetTopicSettings)

KafkaTargetTopic = _reflection.GeneratedProtocolMessageType('KafkaTargetTopic', (_message.Message,), {
  'DESCRIPTOR' : _KAFKATARGETTOPIC,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.kafka_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.KafkaTargetTopic)
  })
_sym_db.RegisterMessage(KafkaTargetTopic)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)