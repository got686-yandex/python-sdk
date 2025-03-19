# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/video/v1/channel.proto
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
    'yandex/cloud/video/v1/channel.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#yandex/cloud/video/v1/channel.proto\x12\x15yandex.cloud.video.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xe6\x02\n\x07\x43hannel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0forganization_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12;\n\x06labels\x18\xc8\x01 \x03(\x0b\x32*.yandex.cloud.video.v1.Channel.LabelsEntry\x12\x39\n\x08settings\x18\xc9\x01 \x01(\x0b\x32&.yandex.cloud.video.v1.ChannelSettings\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x05\x10\x64J\x05\x08\x66\x10\xc8\x01\"\xae\x01\n\x0f\x43hannelSettings\x12\x43\n\radvertisement\x18\x01 \x01(\x0b\x32,.yandex.cloud.video.v1.AdvertisementSettings\x12P\n\x14referer_verification\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.video.v1.RefererVerificationSettingsJ\x04\x08\x02\x10\x03\"\xc0\x01\n\x15\x41\x64vertisementSettings\x12R\n\ryandex_direct\x18\x64 \x01(\x0b\x32\x39.yandex.cloud.video.v1.AdvertisementSettings.YandexDirectH\x00\x1a\x41\n\x0cYandexDirect\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x0f\n\x07page_id\x18\x02 \x01(\x03\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\x03\x42\n\n\x08providerJ\x04\x08\x01\x10\x64\"\x9c\x01\n\x1bRefererVerificationSettings\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12m\n\x0f\x61llowed_domains\x18\x02 \x03(\tBT\xf2\xc7\x31>^(?:\\*\\.)?(?:[a-zA-Z0-9-]*\\.)+[a-zA-Z]{2,}$|^\\*\\.[a-zA-Z]{2,}$\x82\xc8\x31\x05<=100\x8a\xc8\x31\x05\x34-255B\\\n\x19yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;videob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.video.v1.channel_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031yandex.cloud.api.video.v1Z?github.com/yandex-cloud/go-genproto/yandex/cloud/video/v1;video'
  _globals['_CHANNEL_LABELSENTRY']._loaded_options = None
  _globals['_CHANNEL_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_REFERERVERIFICATIONSETTINGS'].fields_by_name['allowed_domains']._loaded_options = None
  _globals['_REFERERVERIFICATIONSETTINGS'].fields_by_name['allowed_domains']._serialized_options = b'\362\3071>^(?:\\*\\.)?(?:[a-zA-Z0-9-]*\\.)+[a-zA-Z]{2,}$|^\\*\\.[a-zA-Z]{2,}$\202\3101\005<=100\212\3101\0054-255'
  _globals['_CHANNEL']._serialized_start=127
  _globals['_CHANNEL']._serialized_end=485
  _globals['_CHANNEL_LABELSENTRY']._serialized_start=427
  _globals['_CHANNEL_LABELSENTRY']._serialized_end=472
  _globals['_CHANNELSETTINGS']._serialized_start=488
  _globals['_CHANNELSETTINGS']._serialized_end=662
  _globals['_ADVERTISEMENTSETTINGS']._serialized_start=665
  _globals['_ADVERTISEMENTSETTINGS']._serialized_end=857
  _globals['_ADVERTISEMENTSETTINGS_YANDEXDIRECT']._serialized_start=774
  _globals['_ADVERTISEMENTSETTINGS_YANDEXDIRECT']._serialized_end=839
  _globals['_REFERERVERIFICATIONSETTINGS']._serialized_start=860
  _globals['_REFERERVERIFICATIONSETTINGS']._serialized_end=1016
# @@protoc_insertion_point(module_scope)
