# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/speechsense/v1/talk.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.speechsense.v1.analysis import conversation_statistics_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_analysis_dot_conversation__statistics__pb2
from yandex.cloud.speechsense.v1.analysis import interrupts_statistics_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_analysis_dot_interrupts__statistics__pb2
from yandex.cloud.speechsense.v1.analysis import silence_statistics_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_analysis_dot_silence__statistics__pb2
from yandex.cloud.speechsense.v1.analysis import speech_statistics_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_analysis_dot_speech__statistics__pb2
from yandex.cloud.speechsense.v1.analysis import summarization_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_analysis_dot_summarization__pb2
from yandex.cloud.speechsense.v1.analysis import transcription_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_analysis_dot_transcription__pb2
from yandex.cloud.speechsense.v1.analysis import text_classifiers_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_analysis_dot_text__classifiers__pb2
from yandex.cloud.speechsense.v1.analysis import points_pb2 as yandex_dot_cloud_dot_speechsense_dot_v1_dot_analysis_dot_points__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&yandex/cloud/speechsense/v1/talk.proto\x12\x1byandex.cloud.speechsense.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x42yandex/cloud/speechsense/v1/analysis/conversation_statistics.proto\x1a@yandex/cloud/speechsense/v1/analysis/interrupts_statistics.proto\x1a=yandex/cloud/speechsense/v1/analysis/silence_statistics.proto\x1a<yandex/cloud/speechsense/v1/analysis/speech_statistics.proto\x1a\x38yandex/cloud/speechsense/v1/analysis/summarization.proto\x1a\x38yandex/cloud/speechsense/v1/analysis/transcription.proto\x1a;yandex/cloud/speechsense/v1/analysis/text_classifiers.proto\x1a\x31yandex/cloud/speechsense/v1/analysis/points.proto\"\xf1\x07\n\x04Talk\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0forganization_id\x18\x02 \x01(\t\x12\x10\n\x08space_id\x18\x03 \x01(\t\x12\x15\n\rconnection_id\x18\x04 \x01(\t\x12\x13\n\x0bproject_ids\x18\x05 \x03(\t\x12\x12\n\ncreated_by\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bmodified_by\x18\x08 \x01(\t\x12/\n\x0bmodified_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x0btalk_fields\x18\n \x03(\x0b\x32\".yandex.cloud.speechsense.v1.Field\x12J\n\rtranscription\x18\x0b \x01(\x0b\x32\x33.yandex.cloud.speechsense.v1.analysis.Transcription\x12Q\n\x11speech_statistics\x18\x0c \x01(\x0b\x32\x36.yandex.cloud.speechsense.v1.analysis.SpeechStatistics\x12S\n\x12silence_statistics\x18\r \x01(\x0b\x32\x37.yandex.cloud.speechsense.v1.analysis.SilenceStatistics\x12Y\n\x15interrupts_statistics\x18\x0e \x01(\x0b\x32:.yandex.cloud.speechsense.v1.analysis.InterruptsStatistics\x12]\n\x17\x63onversation_statistics\x18\x0f \x01(\x0b\x32<.yandex.cloud.speechsense.v1.analysis.ConversationStatistics\x12<\n\x06points\x18\x10 \x01(\x0b\x32,.yandex.cloud.speechsense.v1.analysis.Points\x12O\n\x10text_classifiers\x18\x11 \x01(\x0b\x32\x35.yandex.cloud.speechsense.v1.analysis.TextClassifiers\x12J\n\rsummarization\x18\x12 \x01(\x0b\x32\x33.yandex.cloud.speechsense.v1.analysis.Summarization\x12:\n\ntalk_state\x18\x13 \x01(\x0b\x32&.yandex.cloud.speechsense.v1.TalkState\"\xad\x01\n\tTalkState\x12\x46\n\x10processing_state\x18\x01 \x01(\x0e\x32,.yandex.cloud.speechsense.v1.ProcessingState\x12X\n\x1a\x61lgorithm_processing_infos\x18\x02 \x03(\x0b\x32\x34.yandex.cloud.speechsense.v1.AlgorithmProcessingInfo\"Z\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x34\n\x04type\x18\x03 \x01(\x0e\x32&.yandex.cloud.speechsense.v1.FieldType\"\x9c\x01\n\x17\x41lgorithmProcessingInfo\x12\x39\n\talgorithm\x18\x01 \x01(\x0e\x32&.yandex.cloud.speechsense.v1.Algorithm\x12\x46\n\x10processing_state\x18\x02 \x01(\x0e\x32,.yandex.cloud.speechsense.v1.ProcessingState*\xaf\x01\n\tFieldType\x12\x1a\n\x16\x46IELD_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11\x46IELD_TYPE_STRING\x10\x01\x12\x15\n\x11\x46IELD_TYPE_NUMBER\x10\x02\x12\x16\n\x12\x46IELD_TYPE_DECIMAL\x10\x03\x12\x16\n\x12\x46IELD_TYPE_BOOLEAN\x10\x04\x12\x13\n\x0f\x46IELD_TYPE_DATE\x10\x05\x12\x13\n\x0f\x46IELD_TYPE_JSON\x10\x06*\xb1\x01\n\x0fProcessingState\x12 \n\x1cPROCESSING_STATE_UNSPECIFIED\x10\x00\x12 \n\x1cPROCESSING_STATE_NOT_STARTED\x10\x01\x12\x1f\n\x1bPROCESSING_STATE_PROCESSING\x10\x02\x12\x1c\n\x18PROCESSING_STATE_SUCCESS\x10\x03\x12\x1b\n\x17PROCESSING_STATE_FAILED\x10\x04*\xbd\x01\n\tAlgorithm\x12\x19\n\x15\x41LGORITHM_UNSPECIFIED\x10\x00\x12\x17\n\x13\x41LGORITHM_SPEECHKIT\x10\x01\x12\x12\n\x0e\x41LGORITHM_YGPT\x10\x02\x12\x18\n\x14\x41LGORITHM_CLASSIFIER\x10\x03\x12\x1b\n\x17\x41LGORITHM_SUMMARIZATION\x10\x04\x12\x17\n\x13\x41LGORITHM_EMBEDDING\x10\x05\x12\x18\n\x14\x41LGORITHM_STATISTICS\x10\x06\x42y\n\x1fyandex.cloud.api.speechsense.v1B\tTalkProtoZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1;speechsenseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.speechsense.v1.talk_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037yandex.cloud.api.speechsense.v1B\tTalkProtoZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/speechsense/v1;speechsense'
  _globals['_FIELDTYPE']._serialized_start=2031
  _globals['_FIELDTYPE']._serialized_end=2206
  _globals['_PROCESSINGSTATE']._serialized_start=2209
  _globals['_PROCESSINGSTATE']._serialized_end=2386
  _globals['_ALGORITHM']._serialized_start=2389
  _globals['_ALGORITHM']._serialized_end=2578
  _globals['_TALK']._serialized_start=592
  _globals['_TALK']._serialized_end=1601
  _globals['_TALKSTATE']._serialized_start=1604
  _globals['_TALKSTATE']._serialized_end=1777
  _globals['_FIELD']._serialized_start=1779
  _globals['_FIELD']._serialized_end=1869
  _globals['_ALGORITHMPROCESSINGINFO']._serialized_start=1872
  _globals['_ALGORITHMPROCESSINGINFO']._serialized_end=2028
# @@protoc_insertion_point(module_scope)
