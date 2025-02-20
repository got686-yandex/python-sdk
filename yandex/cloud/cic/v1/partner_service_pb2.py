# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/cic/v1/partner_service.proto
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
    'yandex/cloud/cic/v1/partner_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.cic.v1 import partner_pb2 as yandex_dot_cloud_dot_cic_dot_v1_dot_partner__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/cic/v1/partner_service.proto\x12\x13yandex.cloud.cic.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a!yandex/cloud/cic/v1/partner.proto\"5\n\x11GetPartnerRequest\x12 \n\npartner_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"u\n\x13ListPartnersRequest\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000J\x04\x08\x01\x10\x02\"_\n\x14ListPartnersResponse\x12.\n\x08partners\x18\x01 \x03(\x0b\x32\x1c.yandex.cloud.cic.v1.Partner\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xfb\x01\n\x0ePartnerService\x12r\n\x03Get\x12&.yandex.cloud.cic.v1.GetPartnerRequest\x1a\x1c.yandex.cloud.cic.v1.Partner\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cic/v1/partners/{partner_id}\x12u\n\x04List\x12(.yandex.cloud.cic.v1.ListPartnersRequest\x1a).yandex.cloud.cic.v1.ListPartnersResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/cic/v1/partnersBV\n\x17yandex.cloud.api.cic.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cic/v1;cicb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.cic.v1.partner_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027yandex.cloud.api.cic.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cic/v1;cic'
  _globals['_GETPARTNERREQUEST'].fields_by_name['partner_id']._loaded_options = None
  _globals['_GETPARTNERREQUEST'].fields_by_name['partner_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTPARTNERSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTPARTNERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTPARTNERSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTPARTNERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTPARTNERSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTPARTNERSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_PARTNERSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_PARTNERSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\037\022\035/cic/v1/partners/{partner_id}'
  _globals['_PARTNERSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_PARTNERSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\022\022\020/cic/v1/partners'
  _globals['_GETPARTNERREQUEST']._serialized_start=162
  _globals['_GETPARTNERREQUEST']._serialized_end=215
  _globals['_LISTPARTNERSREQUEST']._serialized_start=217
  _globals['_LISTPARTNERSREQUEST']._serialized_end=334
  _globals['_LISTPARTNERSRESPONSE']._serialized_start=336
  _globals['_LISTPARTNERSRESPONSE']._serialized_end=431
  _globals['_PARTNERSERVICE']._serialized_start=434
  _globals['_PARTNERSERVICE']._serialized_end=685
# @@protoc_insertion_point(module_scope)
