# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/ai/foundation_models/v1/text_classification/text_classification_service.proto
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
    'yandex/cloud/ai/foundation_models/v1/text_classification/text_classification_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.ai.foundation_models.v1.text_classification import text_classification_pb2 as yandex_dot_cloud_dot_ai_dot_foundation__models_dot_v1_dot_text__classification_dot_text__classification__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nZyandex/cloud/ai/foundation_models/v1/text_classification/text_classification_service.proto\x12\x38yandex.cloud.ai.foundation_models.v1.text_classification\x1a\x1cgoogle/api/annotations.proto\x1aRyandex/cloud/ai/foundation_models/v1/text_classification/text_classification.proto\"<\n\x19TextClassificationRequest\x12\x11\n\tmodel_uri\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x97\x01\n\x1aTextClassificationResponse\x12\x62\n\x0bpredictions\x18\x01 \x03(\x0b\x32M.yandex.cloud.ai.foundation_models.v1.text_classification.ClassificationLabel\x12\x15\n\rmodel_version\x18\x02 \x01(\t\"\xce\x01\n FewShotTextClassificationRequest\x12\x11\n\tmodel_uri\x18\x01 \x01(\t\x12\x18\n\x10task_description\x18\x02 \x01(\t\x12\x0e\n\x06labels\x18\x03 \x03(\t\x12\x0c\n\x04text\x18\x04 \x01(\t\x12_\n\x07samples\x18\x05 \x03(\x0b\x32N.yandex.cloud.ai.foundation_models.v1.text_classification.ClassificationSample\"\x9e\x01\n!FewShotTextClassificationResponse\x12\x62\n\x0bpredictions\x18\x01 \x03(\x0b\x32M.yandex.cloud.ai.foundation_models.v1.text_classification.ClassificationLabel\x12\x15\n\rmodel_version\x18\x02 \x01(\t2\x8f\x04\n\x19TextClassificationService\x12\xe9\x01\n\x08\x43lassify\x12S.yandex.cloud.ai.foundation_models.v1.text_classification.TextClassificationRequest\x1aT.yandex.cloud.ai.foundation_models.v1.text_classification.TextClassificationResponse\"2\x82\xd3\xe4\x93\x02,\"\'/foundationModels/v1/textClassification:\x01*\x12\x85\x02\n\x0f\x46\x65wShotClassify\x12Z.yandex.cloud.ai.foundation_models.v1.text_classification.FewShotTextClassificationRequest\x1a[.yandex.cloud.ai.foundation_models.v1.text_classification.FewShotTextClassificationResponse\"9\x82\xd3\xe4\x93\x02\x33\"./foundationModels/v1/fewShotTextClassification:\x01*B\xb0\x01\n<yandex.cloud.api.ai.foundation_models.v1.text_classificationZpgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1/text_classification;text_classificationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.foundation_models.v1.text_classification.text_classification_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n<yandex.cloud.api.ai.foundation_models.v1.text_classificationZpgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/foundation_models/v1/text_classification;text_classification'
  _globals['_TEXTCLASSIFICATIONSERVICE'].methods_by_name['Classify']._loaded_options = None
  _globals['_TEXTCLASSIFICATIONSERVICE'].methods_by_name['Classify']._serialized_options = b'\202\323\344\223\002,\"\'/foundationModels/v1/textClassification:\001*'
  _globals['_TEXTCLASSIFICATIONSERVICE'].methods_by_name['FewShotClassify']._loaded_options = None
  _globals['_TEXTCLASSIFICATIONSERVICE'].methods_by_name['FewShotClassify']._serialized_options = b'\202\323\344\223\0023\"./foundationModels/v1/fewShotTextClassification:\001*'
  _globals['_TEXTCLASSIFICATIONREQUEST']._serialized_start=266
  _globals['_TEXTCLASSIFICATIONREQUEST']._serialized_end=326
  _globals['_TEXTCLASSIFICATIONRESPONSE']._serialized_start=329
  _globals['_TEXTCLASSIFICATIONRESPONSE']._serialized_end=480
  _globals['_FEWSHOTTEXTCLASSIFICATIONREQUEST']._serialized_start=483
  _globals['_FEWSHOTTEXTCLASSIFICATIONREQUEST']._serialized_end=689
  _globals['_FEWSHOTTEXTCLASSIFICATIONRESPONSE']._serialized_start=692
  _globals['_FEWSHOTTEXTCLASSIFICATIONRESPONSE']._serialized_end=850
  _globals['_TEXTCLASSIFICATIONSERVICE']._serialized_start=853
  _globals['_TEXTCLASSIFICATIONSERVICE']._serialized_end=1380
# @@protoc_insertion_point(module_scope)
