# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/ocr/v1/ocr_service.proto
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
    'yandex/cloud/ai/ocr/v1/ocr_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.ocr.v1 import ocr_pb2 as yandex_dot_cloud_dot_ai_dot_ocr_dot_v1_dot_ocr__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/ai/ocr/v1/ocr_service.proto\x12\x16yandex.cloud.ai.ocr.v1\x1a yandex/cloud/ai/ocr/v1/ocr.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\"w\n\x14RecognizeTextRequest\x12\x11\n\x07\x63ontent\x18\x01 \x01(\x0cH\x00\x12\x11\n\tmime_type\x18\x02 \x01(\t\x12\x16\n\x0elanguage_codes\x18\x03 \x03(\t\x12\x17\n\x05model\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04<=50B\x08\n\x06source\"f\n\x15RecognizeTextResponse\x12?\n\x0ftext_annotation\x18\x01 \x01(\x0b\x32&.yandex.cloud.ai.ocr.v1.TextAnnotation\x12\x0c\n\x04page\x18\x02 \x01(\x03\";\n\x15GetRecognitionRequest\x12\"\n\x0coperation_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=502\xa7\x01\n\x16TextRecognitionService\x12\x8c\x01\n\tRecognize\x12,.yandex.cloud.ai.ocr.v1.RecognizeTextRequest\x1a-.yandex.cloud.ai.ocr.v1.RecognizeTextResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/ocr/v1/recognizeText:\x01*0\x01\x32\xd1\x02\n\x1bTextRecognitionAsyncService\x12\x9e\x01\n\tRecognize\x12,.yandex.cloud.ai.ocr.v1.RecognizeTextRequest\x1a!.yandex.cloud.operation.Operation\"@\xb2\xd2*\x17\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x1f\"\x1a/ocr/v1/recognizeTextAsync:\x01*\x12\x90\x01\n\x0eGetRecognition\x12-.yandex.cloud.ai.ocr.v1.GetRecognitionRequest\x1a-.yandex.cloud.ai.ocr.v1.RecognizeTextResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/ocr/v1/getRecognition0\x01\x42\\\n\x1ayandex.cloud.api.ai.ocr.v1Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/ocr/v1;ocrb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.ocr.v1.ocr_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032yandex.cloud.api.ai.ocr.v1Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/ocr/v1;ocr'
  _globals['_RECOGNIZETEXTREQUEST'].fields_by_name['model']._loaded_options = None
  _globals['_RECOGNIZETEXTREQUEST'].fields_by_name['model']._serialized_options = b'\212\3101\004<=50'
  _globals['_GETRECOGNITIONREQUEST'].fields_by_name['operation_id']._loaded_options = None
  _globals['_GETRECOGNITIONREQUEST'].fields_by_name['operation_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_TEXTRECOGNITIONSERVICE'].methods_by_name['Recognize']._loaded_options = None
  _globals['_TEXTRECOGNITIONSERVICE'].methods_by_name['Recognize']._serialized_options = b'\202\323\344\223\002\032\"\025/ocr/v1/recognizeText:\001*'
  _globals['_TEXTRECOGNITIONASYNCSERVICE'].methods_by_name['Recognize']._loaded_options = None
  _globals['_TEXTRECOGNITIONASYNCSERVICE'].methods_by_name['Recognize']._serialized_options = b'\262\322*\027\022\025google.protobuf.Empty\202\323\344\223\002\037\"\032/ocr/v1/recognizeTextAsync:\001*'
  _globals['_TEXTRECOGNITIONASYNCSERVICE'].methods_by_name['GetRecognition']._loaded_options = None
  _globals['_TEXTRECOGNITIONASYNCSERVICE'].methods_by_name['GetRecognition']._serialized_options = b'\202\323\344\223\002\030\022\026/ocr/v1/getRecognition'
  _globals['_RECOGNIZETEXTREQUEST']._serialized_start=237
  _globals['_RECOGNIZETEXTREQUEST']._serialized_end=356
  _globals['_RECOGNIZETEXTRESPONSE']._serialized_start=358
  _globals['_RECOGNIZETEXTRESPONSE']._serialized_end=460
  _globals['_GETRECOGNITIONREQUEST']._serialized_start=462
  _globals['_GETRECOGNITIONREQUEST']._serialized_end=521
  _globals['_TEXTRECOGNITIONSERVICE']._serialized_start=524
  _globals['_TEXTRECOGNITIONSERVICE']._serialized_end=691
  _globals['_TEXTRECOGNITIONASYNCSERVICE']._serialized_start=694
  _globals['_TEXTRECOGNITIONASYNCSERVICE']._serialized_end=1031
# @@protoc_insertion_point(module_scope)
