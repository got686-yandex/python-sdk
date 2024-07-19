# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/smartcaptcha/v1/captcha_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.smartcaptcha.v1 import captcha_pb2 as yandex_dot_cloud_dot_smartcaptcha_dot_v1_dot_captcha__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/smartcaptcha/v1/captcha_service.proto\x12\x1cyandex.cloud.smartcaptcha.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a&yandex/cloud/operation/operation.proto\x1a*yandex/cloud/smartcaptcha/v1/captcha.proto\"5\n\x11GetCaptchaRequest\x12 \n\ncaptcha_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"6\n\x13ListCaptchasRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\\\n\x14ListCaptchasResponse\x12\x38\n\tresources\x18\x03 \x03(\x0b\x32%.yandex.cloud.smartcaptcha.v1.CaptchaJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"\xca\x04\n\x14\x43reateCaptchaRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x32\n\x04name\x18\x02 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x15\n\rallowed_sites\x18\x03 \x03(\t\x12\x43\n\ncomplexity\x18\x04 \x01(\x0e\x32/.yandex.cloud.smartcaptcha.v1.CaptchaComplexity\x12\x12\n\nstyle_json\x18\x05 \x01(\t\x12\x1f\n\x17turn_off_hostname_check\x18\x06 \x01(\x08\x12I\n\x0epre_check_type\x18\x08 \x01(\x0e\x32\x31.yandex.cloud.smartcaptcha.v1.CaptchaPreCheckType\x12J\n\x0e\x63hallenge_type\x18\t \x01(\x0e\x32\x32.yandex.cloud.smartcaptcha.v1.CaptchaChallengeType\x12\x42\n\x0esecurity_rules\x18\x0b \x03(\x0b\x32*.yandex.cloud.smartcaptcha.v1.SecurityRule\x12\x1b\n\x13\x64\x65letion_protection\x18\x0c \x01(\x08\x12H\n\x11override_variants\x18\r \x03(\x0b\x32-.yandex.cloud.smartcaptcha.v1.OverrideVariantJ\x04\x08\x07\x10\x08J\x04\x08\n\x10\x0b\"+\n\x15\x43reateCaptchaMetadata\x12\x12\n\ncaptcha_id\x18\x01 \x01(\t\"8\n\x14\x44\x65leteCaptchaRequest\x12 \n\ncaptcha_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"+\n\x15\x44\x65leteCaptchaMetadata\x12\x12\n\ncaptcha_id\x18\x01 \x01(\t\"\xfc\x04\n\x14UpdateCaptchaRequest\x12 \n\ncaptcha_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x15\n\rallowed_sites\x18\x04 \x03(\t\x12\x43\n\ncomplexity\x18\x05 \x01(\x0e\x32/.yandex.cloud.smartcaptcha.v1.CaptchaComplexity\x12\x12\n\nstyle_json\x18\x06 \x01(\t\x12\x1f\n\x17turn_off_hostname_check\x18\x07 \x01(\x08\x12I\n\x0epre_check_type\x18\t \x01(\x0e\x32\x31.yandex.cloud.smartcaptcha.v1.CaptchaPreCheckType\x12J\n\x0e\x63hallenge_type\x18\n \x01(\x0e\x32\x32.yandex.cloud.smartcaptcha.v1.CaptchaChallengeType\x12\x42\n\x0esecurity_rules\x18\x0c \x03(\x0b\x32*.yandex.cloud.smartcaptcha.v1.SecurityRule\x12\x1b\n\x13\x64\x65letion_protection\x18\r \x01(\x08\x12H\n\x11override_variants\x18\x0e \x03(\x0b\x32-.yandex.cloud.smartcaptcha.v1.OverrideVariantJ\x04\x08\x08\x10\tJ\x04\x08\x0b\x10\x0c\"+\n\x15UpdateCaptchaMetadata\x12\x12\n\ncaptcha_id\x18\x01 \x01(\t2\x8b\x08\n\x0e\x43\x61ptchaService\x12\x8d\x01\n\x03Get\x12/.yandex.cloud.smartcaptcha.v1.GetCaptchaRequest\x1a%.yandex.cloud.smartcaptcha.v1.Captcha\".\x82\xd3\xe4\x93\x02(\x12&/smartcaptcha/v1/captchas/{captcha_id}\x12\xac\x01\n\x0cGetSecretKey\x12/.yandex.cloud.smartcaptcha.v1.GetCaptchaRequest\x1a..yandex.cloud.smartcaptcha.v1.CaptchaSecretKey\";\x82\xd3\xe4\x93\x02\x35\x12\x33/smartcaptcha/v1/captchas/{captcha_id}:getSecretKey\x12\x90\x01\n\x04List\x12\x31.yandex.cloud.smartcaptcha.v1.ListCaptchasRequest\x1a\x32.yandex.cloud.smartcaptcha.v1.ListCaptchasResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/smartcaptcha/v1/captchas\x12\xa9\x01\n\x06\x43reate\x12\x32.yandex.cloud.smartcaptcha.v1.CreateCaptchaRequest\x1a!.yandex.cloud.operation.Operation\"H\xb2\xd2* \n\x15\x43reateCaptchaMetadata\x12\x07\x43\x61ptcha\x82\xd3\xe4\x93\x02\x1e\"\x19/smartcaptcha/v1/captchas:\x01*\x12\xb6\x01\n\x06Update\x12\x32.yandex.cloud.smartcaptcha.v1.UpdateCaptchaRequest\x1a!.yandex.cloud.operation.Operation\"U\xb2\xd2* \n\x15UpdateCaptchaMetadata\x12\x07\x43\x61ptcha\x82\xd3\xe4\x93\x02+2&/smartcaptcha/v1/captchas/{captcha_id}:\x01*\x12\xc1\x01\n\x06\x44\x65lete\x12\x32.yandex.cloud.smartcaptcha.v1.DeleteCaptchaRequest\x1a!.yandex.cloud.operation.Operation\"`\xb2\xd2*.\n\x15\x44\x65leteCaptchaMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02(*&/smartcaptcha/v1/captchas/{captcha_id}Bq\n yandex.cloud.api.smartcaptcha.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/smartcaptcha/v1;smartcaptchab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.smartcaptcha.v1.captcha_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n yandex.cloud.api.smartcaptcha.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/smartcaptcha/v1;smartcaptcha'
  _GETCAPTCHAREQUEST.fields_by_name['captcha_id']._options = None
  _GETCAPTCHAREQUEST.fields_by_name['captcha_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTCAPTCHASREQUEST.fields_by_name['folder_id']._options = None
  _LISTCAPTCHASREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATECAPTCHAREQUEST.fields_by_name['folder_id']._options = None
  _CREATECAPTCHAREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATECAPTCHAREQUEST.fields_by_name['name']._options = None
  _CREATECAPTCHAREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _DELETECAPTCHAREQUEST.fields_by_name['captcha_id']._options = None
  _DELETECAPTCHAREQUEST.fields_by_name['captcha_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATECAPTCHAREQUEST.fields_by_name['captcha_id']._options = None
  _UPDATECAPTCHAREQUEST.fields_by_name['captcha_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATECAPTCHAREQUEST.fields_by_name['name']._options = None
  _UPDATECAPTCHAREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _CAPTCHASERVICE.methods_by_name['Get']._options = None
  _CAPTCHASERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002(\022&/smartcaptcha/v1/captchas/{captcha_id}'
  _CAPTCHASERVICE.methods_by_name['GetSecretKey']._options = None
  _CAPTCHASERVICE.methods_by_name['GetSecretKey']._serialized_options = b'\202\323\344\223\0025\0223/smartcaptcha/v1/captchas/{captcha_id}:getSecretKey'
  _CAPTCHASERVICE.methods_by_name['List']._options = None
  _CAPTCHASERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\033\022\031/smartcaptcha/v1/captchas'
  _CAPTCHASERVICE.methods_by_name['Create']._options = None
  _CAPTCHASERVICE.methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateCaptchaMetadata\022\007Captcha\202\323\344\223\002\036\"\031/smartcaptcha/v1/captchas:\001*'
  _CAPTCHASERVICE.methods_by_name['Update']._options = None
  _CAPTCHASERVICE.methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateCaptchaMetadata\022\007Captcha\202\323\344\223\002+2&/smartcaptcha/v1/captchas/{captcha_id}:\001*'
  _CAPTCHASERVICE.methods_by_name['Delete']._options = None
  _CAPTCHASERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteCaptchaMetadata\022\025google.protobuf.Empty\202\323\344\223\002(*&/smartcaptcha/v1/captchas/{captcha_id}'
  _globals['_GETCAPTCHAREQUEST']._serialized_start=297
  _globals['_GETCAPTCHAREQUEST']._serialized_end=350
  _globals['_LISTCAPTCHASREQUEST']._serialized_start=352
  _globals['_LISTCAPTCHASREQUEST']._serialized_end=406
  _globals['_LISTCAPTCHASRESPONSE']._serialized_start=408
  _globals['_LISTCAPTCHASRESPONSE']._serialized_end=500
  _globals['_CREATECAPTCHAREQUEST']._serialized_start=503
  _globals['_CREATECAPTCHAREQUEST']._serialized_end=1089
  _globals['_CREATECAPTCHAMETADATA']._serialized_start=1091
  _globals['_CREATECAPTCHAMETADATA']._serialized_end=1134
  _globals['_DELETECAPTCHAREQUEST']._serialized_start=1136
  _globals['_DELETECAPTCHAREQUEST']._serialized_end=1192
  _globals['_DELETECAPTCHAMETADATA']._serialized_start=1194
  _globals['_DELETECAPTCHAMETADATA']._serialized_end=1237
  _globals['_UPDATECAPTCHAREQUEST']._serialized_start=1240
  _globals['_UPDATECAPTCHAREQUEST']._serialized_end=1876
  _globals['_UPDATECAPTCHAMETADATA']._serialized_start=1878
  _globals['_UPDATECAPTCHAMETADATA']._serialized_end=1921
  _globals['_CAPTCHASERVICE']._serialized_start=1924
  _globals['_CAPTCHASERVICE']._serialized_end=2959
# @@protoc_insertion_point(module_scope)