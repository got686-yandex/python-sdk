# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/foundation_models/v1/text_generation/text_generation_service.proto
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
    'yandex/cloud/ai/foundation_models/v1/text_generation/text_generation_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.ai.foundation_models.v1 import text_common_pb2 as yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_text__common__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nRyandex/cloud/ai/foundation_models/v1/text_generation/text_generation_service.proto\x12$yandex.cloud.ai.foundation_models.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x36yandex/cloud/ai/foundation_models/v1/text_common.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\"\xe9\x02\n\x11\x43ompletionRequest\x12\x11\n\tmodel_uri\x18\x01 \x01(\t\x12S\n\x12\x63ompletion_options\x18\x02 \x01(\x0b\x32\x37.yandex.cloud.ai.foundation_models.v1.CompletionOptions\x12?\n\x08messages\x18\x03 \x03(\x0b\x32-.yandex.cloud.ai.foundation_models.v1.Message\x12\x39\n\x05tools\x18\x04 \x03(\x0b\x32*.yandex.cloud.ai.foundation_models.v1.Tool\x12\x15\n\x0bjson_object\x18\x05 \x01(\x08H\x00\x12G\n\x0bjson_schema\x18\x06 \x01(\x0b\x32\x30.yandex.cloud.ai.foundation_models.v1.JsonSchemaH\x00\x42\x10\n\x0eResponseFormat\"\xb7\x01\n\x12\x43ompletionResponse\x12G\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32\x31.yandex.cloud.ai.foundation_models.v1.Alternative\x12\x41\n\x05usage\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.ai.foundation_models.v1.ContentUsage\x12\x15\n\rmodel_version\x18\x03 \x01(\t\"2\n\x0fTokenizeRequest\x12\x11\n\tmodel_uri\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"f\n\x10TokenizeResponse\x12;\n\x06tokens\x18\x01 \x03(\x0b\x32+.yandex.cloud.ai.foundation_models.v1.Token\x12\x15\n\rmodel_version\x18\x02 \x01(\t2\xc7\x01\n\x15TextGenerationService\x12\xad\x01\n\nCompletion\x12\x37.yandex.cloud.ai.foundation_models.v1.CompletionRequest\x1a\x38.yandex.cloud.ai.foundation_models.v1.CompletionResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/foundationModels/v1/completion:\x01*0\x01\x32\xd0\x01\n\x1aTextGenerationAsyncService\x12\xb1\x01\n\nCompletion\x12\x37.yandex.cloud.ai.foundation_models.v1.CompletionRequest\x1a!.yandex.cloud.operation.Operation\"G\xb2\xd2*\x14\x12\x12\x43ompletionResponse\x82\xd3\xe4\x93\x02)\"$/foundationModels/v1/completionAsync:\x01*2\xf4\x02\n\x10TokenizerService\x12\xa3\x01\n\x08Tokenize\x12\x35.yandex.cloud.ai.foundation_models.v1.TokenizeRequest\x1a\x36.yandex.cloud.ai.foundation_models.v1.TokenizeResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/foundationModels/v1/tokenize:\x01*\x12\xb9\x01\n\x12TokenizeCompletion\x12\x37.yandex.cloud.ai.foundation_models.v1.CompletionRequest\x1a\x36.yandex.cloud.ai.foundation_models.v1.TokenizeResponse\"2\x82\xd3\xe4\x93\x02,\"\'/foundationModels/v1/tokenizeCompletion:\x01*B\x96\x01\n(yandex.cloud.api.ai.foundation_models.v1Zjgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1/text_generation;foundation_modelsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.ai.foundation_models.v1Zjgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1/text_generation;foundation_models'
  _globals['_TEXTGENERATIONSERVICE'].methods_by_name['Completion']._loaded_options = None
  _globals['_TEXTGENERATIONSERVICE'].methods_by_name['Completion']._serialized_options = b'\202\323\344\223\002$\"\037/foundationModels/v1/completion:\001*'
  _globals['_TEXTGENERATIONASYNCSERVICE'].methods_by_name['Completion']._loaded_options = None
  _globals['_TEXTGENERATIONASYNCSERVICE'].methods_by_name['Completion']._serialized_options = b'\262\322*\024\022\022CompletionResponse\202\323\344\223\002)\"$/foundationModels/v1/completionAsync:\001*'
  _globals['_TOKENIZERSERVICE'].methods_by_name['Tokenize']._loaded_options = None
  _globals['_TOKENIZERSERVICE'].methods_by_name['Tokenize']._serialized_options = b'\202\323\344\223\002\"\"\035/foundationModels/v1/tokenize:\001*'
  _globals['_TOKENIZERSERVICE'].methods_by_name['TokenizeCompletion']._loaded_options = None
  _globals['_TOKENIZERSERVICE'].methods_by_name['TokenizeCompletion']._serialized_options = b'\202\323\344\223\002,\"\'/foundationModels/v1/tokenizeCompletion:\001*'
  _globals['_COMPLETIONREQUEST']._serialized_start=285
  _globals['_COMPLETIONREQUEST']._serialized_end=646
  _globals['_COMPLETIONRESPONSE']._serialized_start=649
  _globals['_COMPLETIONRESPONSE']._serialized_end=832
  _globals['_TOKENIZEREQUEST']._serialized_start=834
  _globals['_TOKENIZEREQUEST']._serialized_end=884
  _globals['_TOKENIZERESPONSE']._serialized_start=886
  _globals['_TOKENIZERESPONSE']._serialized_end=988
  _globals['_TEXTGENERATIONSERVICE']._serialized_start=991
  _globals['_TEXTGENERATIONSERVICE']._serialized_end=1190
  _globals['_TEXTGENERATIONASYNCSERVICE']._serialized_start=1193
  _globals['_TEXTGENERATIONASYNCSERVICE']._serialized_end=1401
  _globals['_TOKENIZERSERVICE']._serialized_start=1404
  _globals['_TOKENIZERSERVICE']._serialized_end=1776
# @@protoc_insertion_point(module_scope)
