# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/assistants/v1/searchindex/search_index_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.common import common_pb2 as yandex_dot_cloud_dot_ai_dot_common_dot_common__pb2
from yandex.cloud.ai.assistants.v1.searchindex import search_index_pb2 as yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDyandex/cloud/ai/assistants/v1/searchindex/search_index_service.proto\x12)yandex.cloud.ai.assistants.v1.searchindex\x1a#yandex/cloud/ai/common/common.proto\x1a<yandex/cloud/ai/assistants/v1/searchindex/search_index.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"\x80\x04\n\x18\x43reateSearchIndexRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x10\n\x08\x66ile_ids\x18\x02 \x03(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x43\n\x11\x65xpiration_config\x18\x05 \x01(\x0b\x32(.yandex.cloud.ai.common.ExpirationConfig\x12_\n\x06labels\x18\x06 \x03(\x0b\x32O.yandex.cloud.ai.assistants.v1.searchindex.CreateSearchIndexRequest.LabelsEntry\x12W\n\x11text_search_index\x18\x07 \x01(\x0b\x32:.yandex.cloud.ai.assistants.v1.searchindex.TextSearchIndexH\x00\x12[\n\x13vector_search_index\x18\x08 \x01(\x0b\x32<.yandex.cloud.ai.assistants.v1.searchindex.VectorSearchIndexH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0b\n\tIndexType\"6\n\x15GetSearchIndexRequest\x12\x1d\n\x0fsearch_index_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\xe8\x02\n\x18UpdateSearchIndexRequest\x12\x1d\n\x0fsearch_index_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x35\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe8\xc7\x31\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x43\n\x11\x65xpiration_config\x18\x05 \x01(\x0b\x32(.yandex.cloud.ai.common.ExpirationConfig\x12_\n\x06labels\x18\x06 \x03(\x0b\x32O.yandex.cloud.ai.assistants.v1.searchindex.UpdateSearchIndexRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"9\n\x18\x44\x65leteSearchIndexRequest\x12\x1d\n\x0fsearch_index_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x1b\n\x19\x44\x65leteSearchIndexResponse\"Z\n\x18ListSearchIndicesRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"}\n\x19ListSearchIndicesResponse\x12G\n\x07indices\x18\x01 \x03(\x0b\x32\x36.yandex.cloud.ai.assistants.v1.searchindex.SearchIndex\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xbc\x07\n\x12SearchIndexService\x12\xa8\x01\n\x06\x43reate\x12\x43.yandex.cloud.ai.assistants.v1.searchindex.CreateSearchIndexRequest\x1a!.yandex.cloud.operation.Operation\"6\xb2\xd2*\r\x12\x0bSearchIndex\x82\xd3\xe4\x93\x02\x1f\"\x1a/assistants/v1/searchIndex:\x01*\x12\xb5\x01\n\x03Get\x12@.yandex.cloud.ai.assistants.v1.searchindex.GetSearchIndexRequest\x1a\x36.yandex.cloud.ai.assistants.v1.searchindex.SearchIndex\"4\x82\xd3\xe4\x93\x02.\x12,/assistants/v1/searchIndex/{search_index_id}\x12\xbe\x01\n\x06Update\x12\x43.yandex.cloud.ai.assistants.v1.searchindex.UpdateSearchIndexRequest\x1a\x36.yandex.cloud.ai.assistants.v1.searchindex.SearchIndex\"7\x82\xd3\xe4\x93\x02\x31\x32,/assistants/v1/searchIndex/{search_index_id}:\x01*\x12\xc9\x01\n\x06\x44\x65lete\x12\x43.yandex.cloud.ai.assistants.v1.searchindex.DeleteSearchIndexRequest\x1a\x44.yandex.cloud.ai.assistants.v1.searchindex.DeleteSearchIndexResponse\"4\x82\xd3\xe4\x93\x02.*,/assistants/v1/searchIndex/{search_index_id}\x12\xb5\x01\n\x04List\x12\x43.yandex.cloud.ai.assistants.v1.searchindex.ListSearchIndicesRequest\x1a\x44.yandex.cloud.ai.assistants.v1.searchindex.ListSearchIndicesResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/assistants/v1/searchIndexB\x8a\x01\n-yandex.cloud.api.ai.assistants.v1.searchindexZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1/searchindex;searchindexb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.assistants.v1.searchindex.search_index_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n-yandex.cloud.api.ai.assistants.v1.searchindexZYgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1/searchindex;searchindex'
  _CREATESEARCHINDEXREQUEST_LABELSENTRY._options = None
  _CREATESEARCHINDEXREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATESEARCHINDEXREQUEST.fields_by_name['folder_id']._options = None
  _CREATESEARCHINDEXREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _GETSEARCHINDEXREQUEST.fields_by_name['search_index_id']._options = None
  _GETSEARCHINDEXREQUEST.fields_by_name['search_index_id']._serialized_options = b'\350\3071\001'
  _UPDATESEARCHINDEXREQUEST_LABELSENTRY._options = None
  _UPDATESEARCHINDEXREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATESEARCHINDEXREQUEST.fields_by_name['search_index_id']._options = None
  _UPDATESEARCHINDEXREQUEST.fields_by_name['search_index_id']._serialized_options = b'\350\3071\001'
  _UPDATESEARCHINDEXREQUEST.fields_by_name['update_mask']._options = None
  _UPDATESEARCHINDEXREQUEST.fields_by_name['update_mask']._serialized_options = b'\350\3071\001'
  _DELETESEARCHINDEXREQUEST.fields_by_name['search_index_id']._options = None
  _DELETESEARCHINDEXREQUEST.fields_by_name['search_index_id']._serialized_options = b'\350\3071\001'
  _LISTSEARCHINDICESREQUEST.fields_by_name['folder_id']._options = None
  _LISTSEARCHINDICESREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _SEARCHINDEXSERVICE.methods_by_name['Create']._options = None
  _SEARCHINDEXSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*\r\022\013SearchIndex\202\323\344\223\002\037\"\032/assistants/v1/searchIndex:\001*'
  _SEARCHINDEXSERVICE.methods_by_name['Get']._options = None
  _SEARCHINDEXSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002.\022,/assistants/v1/searchIndex/{search_index_id}'
  _SEARCHINDEXSERVICE.methods_by_name['Update']._options = None
  _SEARCHINDEXSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\00212,/assistants/v1/searchIndex/{search_index_id}:\001*'
  _SEARCHINDEXSERVICE.methods_by_name['Delete']._options = None
  _SEARCHINDEXSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002.*,/assistants/v1/searchIndex/{search_index_id}'
  _SEARCHINDEXSERVICE.methods_by_name['List']._options = None
  _SEARCHINDEXSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\034\022\032/assistants/v1/searchIndex'
  _globals['_CREATESEARCHINDEXREQUEST']._serialized_start=384
  _globals['_CREATESEARCHINDEXREQUEST']._serialized_end=896
  _globals['_CREATESEARCHINDEXREQUEST_LABELSENTRY']._serialized_start=838
  _globals['_CREATESEARCHINDEXREQUEST_LABELSENTRY']._serialized_end=883
  _globals['_GETSEARCHINDEXREQUEST']._serialized_start=898
  _globals['_GETSEARCHINDEXREQUEST']._serialized_end=952
  _globals['_UPDATESEARCHINDEXREQUEST']._serialized_start=955
  _globals['_UPDATESEARCHINDEXREQUEST']._serialized_end=1315
  _globals['_UPDATESEARCHINDEXREQUEST_LABELSENTRY']._serialized_start=838
  _globals['_UPDATESEARCHINDEXREQUEST_LABELSENTRY']._serialized_end=883
  _globals['_DELETESEARCHINDEXREQUEST']._serialized_start=1317
  _globals['_DELETESEARCHINDEXREQUEST']._serialized_end=1374
  _globals['_DELETESEARCHINDEXRESPONSE']._serialized_start=1376
  _globals['_DELETESEARCHINDEXRESPONSE']._serialized_end=1403
  _globals['_LISTSEARCHINDICESREQUEST']._serialized_start=1405
  _globals['_LISTSEARCHINDICESREQUEST']._serialized_end=1495
  _globals['_LISTSEARCHINDICESRESPONSE']._serialized_start=1497
  _globals['_LISTSEARCHINDICESRESPONSE']._serialized_end=1622
  _globals['_SEARCHINDEXSERVICE']._serialized_start=1625
  _globals['_SEARCHINDEXSERVICE']._serialized_end=2581
# @@protoc_insertion_point(module_scope)