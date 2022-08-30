# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iot/broker/v1/broker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iot/broker/v1/broker.proto',
  package='yandex.cloud.iot.broker.v1',
  syntax='proto3',
  serialized_options=b'\n\036yandex.cloud.api.iot.broker.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/broker/v1;broker',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'yandex/cloud/iot/broker/v1/broker.proto\x12\x1ayandex.cloud.iot.broker.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xee\x02\n\x06\x42roker\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.iot.broker.v1.Broker.LabelsEntry\x12\x39\n\x06status\x18\x07 \x01(\x0e\x32).yandex.cloud.iot.broker.v1.Broker.Status\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\"\x85\x01\n\x11\x42rokerCertificate\x12\x11\n\tbroker_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x02 \x01(\t\x12\x18\n\x10\x63\x65rtificate_data\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"_\n\x0e\x42rokerPassword\x12\x11\n\tbroker_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampBg\n\x1eyandex.cloud.api.iot.broker.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/broker/v1;brokerb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_BROKER_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.iot.broker.v1.Broker.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=399,
  serialized_end=471,
)
_sym_db.RegisterEnumDescriptor(_BROKER_STATUS)


_BROKER_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.iot.broker.v1.Broker.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.iot.broker.v1.Broker.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.iot.broker.v1.Broker.LabelsEntry.value', index=1,
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
  serialized_start=352,
  serialized_end=397,
)

_BROKER = _descriptor.Descriptor(
  name='Broker',
  full_name='yandex.cloud.iot.broker.v1.Broker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.iot.broker.v1.Broker.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.iot.broker.v1.Broker.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iot.broker.v1.Broker.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.iot.broker.v1.Broker.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.iot.broker.v1.Broker.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.iot.broker.v1.Broker.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.iot.broker.v1.Broker.status', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BROKER_LABELSENTRY, ],
  enum_types=[
    _BROKER_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=471,
)


_BROKERCERTIFICATE = _descriptor.Descriptor(
  name='BrokerCertificate',
  full_name='yandex.cloud.iot.broker.v1.BrokerCertificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='broker_id', full_name='yandex.cloud.iot.broker.v1.BrokerCertificate.broker_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='yandex.cloud.iot.broker.v1.BrokerCertificate.fingerprint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='certificate_data', full_name='yandex.cloud.iot.broker.v1.BrokerCertificate.certificate_data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iot.broker.v1.BrokerCertificate.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=474,
  serialized_end=607,
)


_BROKERPASSWORD = _descriptor.Descriptor(
  name='BrokerPassword',
  full_name='yandex.cloud.iot.broker.v1.BrokerPassword',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='broker_id', full_name='yandex.cloud.iot.broker.v1.BrokerPassword.broker_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.iot.broker.v1.BrokerPassword.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.iot.broker.v1.BrokerPassword.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=609,
  serialized_end=704,
)

_BROKER_LABELSENTRY.containing_type = _BROKER
_BROKER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BROKER.fields_by_name['labels'].message_type = _BROKER_LABELSENTRY
_BROKER.fields_by_name['status'].enum_type = _BROKER_STATUS
_BROKER_STATUS.containing_type = _BROKER
_BROKERCERTIFICATE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BROKERPASSWORD.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Broker'] = _BROKER
DESCRIPTOR.message_types_by_name['BrokerCertificate'] = _BROKERCERTIFICATE
DESCRIPTOR.message_types_by_name['BrokerPassword'] = _BROKERPASSWORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Broker = _reflection.GeneratedProtocolMessageType('Broker', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BROKER_LABELSENTRY,
    '__module__' : 'yandex.cloud.iot.broker.v1.broker_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.iot.broker.v1.Broker.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _BROKER,
  '__module__' : 'yandex.cloud.iot.broker.v1.broker_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.broker.v1.Broker)
  })
_sym_db.RegisterMessage(Broker)
_sym_db.RegisterMessage(Broker.LabelsEntry)

BrokerCertificate = _reflection.GeneratedProtocolMessageType('BrokerCertificate', (_message.Message,), {
  'DESCRIPTOR' : _BROKERCERTIFICATE,
  '__module__' : 'yandex.cloud.iot.broker.v1.broker_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.broker.v1.BrokerCertificate)
  })
_sym_db.RegisterMessage(BrokerCertificate)

BrokerPassword = _reflection.GeneratedProtocolMessageType('BrokerPassword', (_message.Message,), {
  'DESCRIPTOR' : _BROKERPASSWORD,
  '__module__' : 'yandex.cloud.iot.broker.v1.broker_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.broker.v1.BrokerPassword)
  })
_sym_db.RegisterMessage(BrokerPassword)


DESCRIPTOR._options = None
_BROKER_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)