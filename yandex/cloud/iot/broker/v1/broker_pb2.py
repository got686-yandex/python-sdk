# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/iot/broker/v1/broker.proto
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
    'yandex/cloud/iot/broker/v1/broker.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.logging.v1 import log_entry_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'yandex/cloud/iot/broker/v1/broker.proto\x12\x1ayandex.cloud.iot.broker.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\'yandex/cloud/logging/v1/log_entry.proto\x1a\x1dyandex/cloud/validation.proto\"\xab\x03\n\x06\x42roker\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.iot.broker.v1.Broker.LabelsEntry\x12\x39\n\x06status\x18\x07 \x01(\x0e\x32).yandex.cloud.iot.broker.v1.Broker.Status\x12;\n\x0blog_options\x18\x08 \x01(\x0b\x32&.yandex.cloud.iot.broker.v1.LogOptions\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\"\x85\x01\n\x11\x42rokerCertificate\x12\x11\n\tbroker_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x02 \x01(\t\x12\x18\n\x10\x63\x65rtificate_data\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"_\n\x0e\x42rokerPassword\x12\x11\n\tbroker_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xe0\x01\n\nLogOptions\x12\x10\n\x08\x64isabled\x18\x01 \x01(\x08\x12;\n\x0clog_group_id\x18\x02 \x01(\tB#\xf2\xc7\x31\x1f([a-zA-Z][-a-zA-Z0-9_.]{0,63})?H\x00\x12\x38\n\tfolder_id\x18\x03 \x01(\tB#\xf2\xc7\x31\x1f([a-zA-Z][-a-zA-Z0-9_.]{0,63})?H\x00\x12:\n\tmin_level\x18\x04 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.LevelB\r\n\x0b\x64\x65stinationBg\n\x1eyandex.cloud.api.iot.broker.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/broker/v1;brokerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.iot.broker.v1.broker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.iot.broker.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/broker/v1;broker'
  _globals['_BROKER_LABELSENTRY']._loaded_options = None
  _globals['_BROKER_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_LOGOPTIONS'].fields_by_name['log_group_id']._loaded_options = None
  _globals['_LOGOPTIONS'].fields_by_name['log_group_id']._serialized_options = b'\362\3071\037([a-zA-Z][-a-zA-Z0-9_.]{0,63})?'
  _globals['_LOGOPTIONS'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LOGOPTIONS'].fields_by_name['folder_id']._serialized_options = b'\362\3071\037([a-zA-Z][-a-zA-Z0-9_.]{0,63})?'
  _globals['_BROKER']._serialized_start=177
  _globals['_BROKER']._serialized_end=604
  _globals['_BROKER_LABELSENTRY']._serialized_start=485
  _globals['_BROKER_LABELSENTRY']._serialized_end=530
  _globals['_BROKER_STATUS']._serialized_start=532
  _globals['_BROKER_STATUS']._serialized_end=604
  _globals['_BROKERCERTIFICATE']._serialized_start=607
  _globals['_BROKERCERTIFICATE']._serialized_end=740
  _globals['_BROKERPASSWORD']._serialized_start=742
  _globals['_BROKERPASSWORD']._serialized_end=837
  _globals['_LOGOPTIONS']._serialized_start=840
  _globals['_LOGOPTIONS']._serialized_end=1064
# @@protoc_insertion_point(module_scope)
