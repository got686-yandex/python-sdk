# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/postgres.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.datatransfer.v1.endpoint import common_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4yandex/cloud/datatransfer/v1/endpoint/postgres.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x32yandex/cloud/datatransfer/v1/endpoint/common.proto\"\xaa\x0b\n\x1ePostgresObjectTransferSettings\x12L\n\x08sequence\x18\x01 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12U\n\x11sequence_owned_by\x18\x02 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12I\n\x05table\x18\x03 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12O\n\x0bprimary_key\x18\x04 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12Q\n\rfk_constraint\x18\x05 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12R\n\x0e\x64\x65\x66\x61ult_values\x18\x06 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12N\n\nconstraint\x18\x07 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12I\n\x05index\x18\x08 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04view\x18\t \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12L\n\x08\x66unction\x18\n \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12K\n\x07trigger\x18\x0b \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04type\x18\x0c \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04rule\x18\r \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12M\n\tcollation\x18\x0e \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12J\n\x06policy\x18\x0f \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04\x63\x61st\x18\x10 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12U\n\x11materialized_view\x18\x11 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12P\n\x0csequence_set\x18\x12 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\"\x91\x01\n\x11OnPremisePostgres\x12\x0c\n\x04port\x18\x02 \x01(\x03\x12\x11\n\tsubnet_id\x18\x04 \x01(\t\x12\r\n\x05hosts\x18\x05 \x03(\t\x12@\n\x08tls_mode\x18\x06 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.endpoint.TLSModeJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x04\"\x8c\x01\n\x12PostgresConnection\x12\x18\n\x0emdb_cluster_id\x18\x01 \x01(\tH\x00\x12N\n\non_premise\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.datatransfer.v1.endpoint.OnPremisePostgresH\x00\x42\x0c\n\nconnection\"\xb3\x03\n\x0ePostgresSource\x12M\n\nconnection\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.datatransfer.v1.endpoint.PostgresConnection\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12?\n\x08password\x18\x04 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12\x16\n\x0einclude_tables\x18\x05 \x03(\t\x12\x16\n\x0e\x65xclude_tables\x18\x06 \x03(\t\x12\x1b\n\x13slot_byte_lag_limit\x18\x08 \x01(\x03\x12\x16\n\x0eservice_schema\x18\t \x01(\t\x12g\n\x18object_transfer_settings\x18\r \x01(\x0b\x32\x45.yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings\x12\x17\n\x0fsecurity_groups\x18\x0e \x03(\tJ\x04\x08\x07\x10\x08J\x04\x08\n\x10\r\"\xad\x02\n\x0ePostgresTarget\x12M\n\nconnection\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.datatransfer.v1.endpoint.PostgresConnection\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12?\n\x08password\x18\x04 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12L\n\x0e\x63leanup_policy\x18\x05 \x01(\x0e\x32\x34.yandex.cloud.datatransfer.v1.endpoint.CleanupPolicy\x12\x17\n\x0fsecurity_groups\x18\x07 \x03(\tJ\x04\x08\x06\x10\x07\x42\xa7\x01\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\xaa\x02%Yandex.Cloud.Datatransfer.V1.EndPointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\252\002%Yandex.Cloud.Datatransfer.V1.EndPoint'
  _globals['_POSTGRESOBJECTTRANSFERSETTINGS']._serialized_start=148
  _globals['_POSTGRESOBJECTTRANSFERSETTINGS']._serialized_end=1598
  _globals['_ONPREMISEPOSTGRES']._serialized_start=1601
  _globals['_ONPREMISEPOSTGRES']._serialized_end=1746
  _globals['_POSTGRESCONNECTION']._serialized_start=1749
  _globals['_POSTGRESCONNECTION']._serialized_end=1889
  _globals['_POSTGRESSOURCE']._serialized_start=1892
  _globals['_POSTGRESSOURCE']._serialized_end=2327
  _globals['_POSTGRESTARGET']._serialized_start=2330
  _globals['_POSTGRESTARGET']._serialized_end=2631
# @@protoc_insertion_point(module_scope)
