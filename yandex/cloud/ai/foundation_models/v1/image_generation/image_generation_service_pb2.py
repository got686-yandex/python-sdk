# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/foundation_models/v1/image_generation/image_generation_service.proto
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
    'yandex/cloud/ai/foundation_models/v1/image_generation/image_generation_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.ai.foundation_models.v1.image_generation import image_generation_pb2 as yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_image__generation_dot_image__generation__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nTyandex/cloud/ai/foundation_models/v1/image_generation/image_generation_service.proto\x12\x35yandex.cloud.ai.foundation_models.v1.image_generation\x1a\x1cgoogle/api/annotations.proto\x1aLyandex/cloud/ai/foundation_models/v1/image_generation/image_generation.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\"\xe8\x01\n\x16ImageGenerationRequest\x12\x11\n\tmodel_uri\x18\x01 \x01(\t\x12P\n\x08messages\x18\x02 \x03(\x0b\x32>.yandex.cloud.ai.foundation_models.v1.image_generation.Message\x12i\n\x12generation_options\x18\x03 \x01(\x0b\x32M.yandex.cloud.ai.foundation_models.v1.image_generation.ImageGenerationOptions\"?\n\x17ImageGenerationResponse\x12\r\n\x05image\x18\x01 \x01(\x0c\x12\x15\n\rmodel_version\x18\x02 \x01(\t2\xef\x01\n\x1bImageGenerationAsyncService\x12\xcf\x01\n\x08Generate\x12M.yandex.cloud.ai.foundation_models.v1.image_generation.ImageGenerationRequest\x1a!.yandex.cloud.operation.Operation\"Q\xb2\xd2*\x19\x12\x17ImageGenerationResponse\x82\xd3\xe4\x93\x02.\")/foundationModels/v1/imageGenerationAsync:\x01*B\xa7\x01\n9yandex.cloud.api.ai.foundation_models.v1.image_generationZjgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1/image_generation;image_generationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.foundation_models.v1.image_generation.image_generation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n9yandex.cloud.api.ai.foundation_models.v1.image_generationZjgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1/image_generation;image_generation'
  _globals['_IMAGEGENERATIONASYNCSERVICE'].methods_by_name['Generate']._loaded_options = None
  _globals['_IMAGEGENERATIONASYNCSERVICE'].methods_by_name['Generate']._serialized_options = b'\262\322*\031\022\027ImageGenerationResponse\202\323\344\223\002.\")/foundationModels/v1/imageGenerationAsync:\001*'
  _globals['_IMAGEGENERATIONREQUEST']._serialized_start=326
  _globals['_IMAGEGENERATIONREQUEST']._serialized_end=558
  _globals['_IMAGEGENERATIONRESPONSE']._serialized_start=560
  _globals['_IMAGEGENERATIONRESPONSE']._serialized_end=623
  _globals['_IMAGEGENERATIONASYNCSERVICE']._serialized_start=626
  _globals['_IMAGEGENERATIONASYNCSERVICE']._serialized_end=865
# @@protoc_insertion_point(module_scope)
