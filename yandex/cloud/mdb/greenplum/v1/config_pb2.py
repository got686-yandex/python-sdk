# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/greenplum/v1/config.proto
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
    'yandex/cloud/mdb/greenplum/v1/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/mdb/greenplum/v1/config.proto\x12\x1dyandex.cloud.mdb.greenplum.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"P\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\x12\x14\n\x0c\x64isk_type_id\x18\x03 \x01(\t\"\x90\x02\n\x16\x43onnectionPoolerConfig\x12L\n\x04mode\x18\x01 \x01(\x0e\x32>.yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfig.PoolMode\x12)\n\x04size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x13\x63lient_idle_timeout\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"C\n\x08PoolMode\x12\x19\n\x15POOL_MODE_UNSPECIFIED\x10\x00\x12\x0b\n\x07SESSION\x10\x01\x12\x0f\n\x0bTRANSACTION\x10\x02\"O\n\x19\x42\x61\x63kgroundActivityStartAt\x12\x17\n\x05hours\x18\x01 \x01(\x03\x42\x08\xfa\xc7\x31\x04\x30-23\x12\x19\n\x07minutes\x18\x02 \x01(\x03\x42\x08\xfa\xc7\x31\x04\x30-59\"_\n\nTableSizes\x12Q\n\x06starts\x18\x01 \x03(\x0b\x32\x38.yandex.cloud.mdb.greenplum.v1.BackgroundActivityStartAtB\x07\x82\xc8\x31\x03<=4\"\xe6\x01\n\x10\x41nalyzeAndVacuum\x12G\n\x05start\x18\x01 \x01(\x0b\x32\x38.yandex.cloud.mdb.greenplum.v1.BackgroundActivityStartAt\x12\x44\n\x0f\x61nalyze_timeout\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n7200-86399\x12\x43\n\x0evacuum_timeout\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n7200-86399\"\xfa\x01\n\x1a\x42\x61\x63kgroundActivitiesConfig\x12>\n\x0btable_sizes\x18\x01 \x01(\x0b\x32).yandex.cloud.mdb.greenplum.v1.TableSizes\x12K\n\x12\x61nalyze_and_vacuum\x18\x02 \x01(\x0b\x32/.yandex.cloud.mdb.greenplum.v1.AnalyzeAndVacuum\x12O\n\x14query_killer_scripts\x18\x03 \x01(\x0b\x32\x31.yandex.cloud.mdb.greenplum.v1.QueryKillerScripts\"\x8a\x01\n\x0bQueryKiller\x12*\n\x06\x65nable\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x07max_age\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0b\xfa\xc7\x31\x07\x31-86400\x12\x14\n\x0cignore_users\x18\x03 \x03(\t\"\xd9\x01\n\x12QueryKillerScripts\x12\x38\n\x04idle\x18\x01 \x01(\x0b\x32*.yandex.cloud.mdb.greenplum.v1.QueryKiller\x12G\n\x13idle_in_transaction\x18\x02 \x01(\x0b\x32*.yandex.cloud.mdb.greenplum.v1.QueryKiller\x12@\n\x0clong_running\x18\x03 \x01(\x0b\x32*.yandex.cloud.mdb.greenplum.v1.QueryKiller\"U\n\x16MasterSubclusterConfig\x12;\n\tresources\x18\x01 \x01(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.Resources\"V\n\x17SegmentSubclusterConfig\x12;\n\tresources\x18\x01 \x01(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.Resources\"\x96\x05\n\x10GreenplumConfig6\x12\x34\n\x0fmax_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16max_slot_wal_keep_size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\x1dgp_workfile_limit_per_segment\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bgp_workfile_limit_per_query\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x46\n!gp_workfile_limit_files_per_query\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_prepared_transactions\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x17gp_workfile_compression\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x11max_statement_mem\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\rlog_statement\x18\t \x01(\x0e\x32+.yandex.cloud.mdb.greenplum.v1.LogStatement\x12H\n$gp_add_column_inherits_table_setting\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xd3\x03\n\x13GreenplumConfig6_17\x12\x34\n\x0fmax_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16max_slot_wal_keep_size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\x1dgp_workfile_limit_per_segment\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bgp_workfile_limit_per_query\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x46\n!gp_workfile_limit_files_per_query\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_prepared_transactions\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x17gp_workfile_compression\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xcf\x04\n\x13GreenplumConfig6_19\x12\x34\n\x0fmax_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16max_slot_wal_keep_size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\x1dgp_workfile_limit_per_segment\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bgp_workfile_limit_per_query\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x46\n!gp_workfile_limit_files_per_query\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_prepared_transactions\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x17gp_workfile_compression\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x11max_statement_mem\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\rlog_statement\x18\t \x01(\x0e\x32+.yandex.cloud.mdb.greenplum.v1.LogStatement\"\x99\x05\n\x13GreenplumConfig6_21\x12\x34\n\x0fmax_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16max_slot_wal_keep_size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\x1dgp_workfile_limit_per_segment\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bgp_workfile_limit_per_query\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x46\n!gp_workfile_limit_files_per_query\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_prepared_transactions\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x17gp_workfile_compression\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x11max_statement_mem\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\rlog_statement\x18\t \x01(\x0e\x32+.yandex.cloud.mdb.greenplum.v1.LogStatement\x12H\n$gp_add_column_inherits_table_setting\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x99\x05\n\x13GreenplumConfig6_22\x12\x34\n\x0fmax_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16max_slot_wal_keep_size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\x1dgp_workfile_limit_per_segment\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bgp_workfile_limit_per_query\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x46\n!gp_workfile_limit_files_per_query\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_prepared_transactions\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x17gp_workfile_compression\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x11max_statement_mem\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\rlog_statement\x18\t \x01(\x0e\x32+.yandex.cloud.mdb.greenplum.v1.LogStatement\x12H\n$gp_add_column_inherits_table_setting\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x81\x02\n\x16GreenplumConfigSet6_17\x12R\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_17B\x04\xe8\xc7\x31\x01\x12G\n\x0buser_config\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_17\x12J\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_17\"\x81\x02\n\x16GreenplumConfigSet6_19\x12R\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_19B\x04\xe8\xc7\x31\x01\x12G\n\x0buser_config\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_19\x12J\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_19\"\x81\x02\n\x16GreenplumConfigSet6_21\x12R\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_21B\x04\xe8\xc7\x31\x01\x12G\n\x0buser_config\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_21\x12J\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_21\"\x81\x02\n\x16GreenplumConfigSet6_22\x12R\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_22B\x04\xe8\xc7\x31\x01\x12G\n\x0buser_config\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_22\x12J\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_22\"\xf5\x01\n\x13GreenplumConfigSet6\x12O\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32/.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6B\x04\xe8\xc7\x31\x01\x12\x44\n\x0buser_config\x18\x02 \x01(\x0b\x32/.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6\x12G\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32/.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6\"\x8d\x02\n\x19\x43onnectionPoolerConfigSet\x12U\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfigB\x04\xe8\xc7\x31\x01\x12J\n\x0buser_config\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfig\x12M\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfig*R\n\x0cLogStatement\x12\x1d\n\x19LOG_STATEMENT_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x07\n\x03\x44\x44L\x10\x02\x12\x07\n\x03MOD\x10\x03\x12\x07\n\x03\x41LL\x10\x04\x42p\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplumb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.greenplum.v1.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplum'
  _globals['_BACKGROUNDACTIVITYSTARTAT'].fields_by_name['hours']._loaded_options = None
  _globals['_BACKGROUNDACTIVITYSTARTAT'].fields_by_name['hours']._serialized_options = b'\372\3071\0040-23'
  _globals['_BACKGROUNDACTIVITYSTARTAT'].fields_by_name['minutes']._loaded_options = None
  _globals['_BACKGROUNDACTIVITYSTARTAT'].fields_by_name['minutes']._serialized_options = b'\372\3071\0040-59'
  _globals['_TABLESIZES'].fields_by_name['starts']._loaded_options = None
  _globals['_TABLESIZES'].fields_by_name['starts']._serialized_options = b'\202\3101\003<=4'
  _globals['_ANALYZEANDVACUUM'].fields_by_name['analyze_timeout']._loaded_options = None
  _globals['_ANALYZEANDVACUUM'].fields_by_name['analyze_timeout']._serialized_options = b'\372\3071\n7200-86399'
  _globals['_ANALYZEANDVACUUM'].fields_by_name['vacuum_timeout']._loaded_options = None
  _globals['_ANALYZEANDVACUUM'].fields_by_name['vacuum_timeout']._serialized_options = b'\372\3071\n7200-86399'
  _globals['_QUERYKILLER'].fields_by_name['max_age']._loaded_options = None
  _globals['_QUERYKILLER'].fields_by_name['max_age']._serialized_options = b'\372\3071\0071-86400'
  _globals['_GREENPLUMCONFIGSET6_17'].fields_by_name['effective_config']._loaded_options = None
  _globals['_GREENPLUMCONFIGSET6_17'].fields_by_name['effective_config']._serialized_options = b'\350\3071\001'
  _globals['_GREENPLUMCONFIGSET6_19'].fields_by_name['effective_config']._loaded_options = None
  _globals['_GREENPLUMCONFIGSET6_19'].fields_by_name['effective_config']._serialized_options = b'\350\3071\001'
  _globals['_GREENPLUMCONFIGSET6_21'].fields_by_name['effective_config']._loaded_options = None
  _globals['_GREENPLUMCONFIGSET6_21'].fields_by_name['effective_config']._serialized_options = b'\350\3071\001'
  _globals['_GREENPLUMCONFIGSET6_22'].fields_by_name['effective_config']._loaded_options = None
  _globals['_GREENPLUMCONFIGSET6_22'].fields_by_name['effective_config']._serialized_options = b'\350\3071\001'
  _globals['_GREENPLUMCONFIGSET6'].fields_by_name['effective_config']._loaded_options = None
  _globals['_GREENPLUMCONFIGSET6'].fields_by_name['effective_config']._serialized_options = b'\350\3071\001'
  _globals['_CONNECTIONPOOLERCONFIGSET'].fields_by_name['effective_config']._loaded_options = None
  _globals['_CONNECTIONPOOLERCONFIGSET'].fields_by_name['effective_config']._serialized_options = b'\350\3071\001'
  _globals['_LOGSTATEMENT']._serialized_start=6322
  _globals['_LOGSTATEMENT']._serialized_end=6404
  _globals['_RESOURCES']._serialized_start=140
  _globals['_RESOURCES']._serialized_end=220
  _globals['_CONNECTIONPOOLERCONFIG']._serialized_start=223
  _globals['_CONNECTIONPOOLERCONFIG']._serialized_end=495
  _globals['_CONNECTIONPOOLERCONFIG_POOLMODE']._serialized_start=428
  _globals['_CONNECTIONPOOLERCONFIG_POOLMODE']._serialized_end=495
  _globals['_BACKGROUNDACTIVITYSTARTAT']._serialized_start=497
  _globals['_BACKGROUNDACTIVITYSTARTAT']._serialized_end=576
  _globals['_TABLESIZES']._serialized_start=578
  _globals['_TABLESIZES']._serialized_end=673
  _globals['_ANALYZEANDVACUUM']._serialized_start=676
  _globals['_ANALYZEANDVACUUM']._serialized_end=906
  _globals['_BACKGROUNDACTIVITIESCONFIG']._serialized_start=909
  _globals['_BACKGROUNDACTIVITIESCONFIG']._serialized_end=1159
  _globals['_QUERYKILLER']._serialized_start=1162
  _globals['_QUERYKILLER']._serialized_end=1300
  _globals['_QUERYKILLERSCRIPTS']._serialized_start=1303
  _globals['_QUERYKILLERSCRIPTS']._serialized_end=1520
  _globals['_MASTERSUBCLUSTERCONFIG']._serialized_start=1522
  _globals['_MASTERSUBCLUSTERCONFIG']._serialized_end=1607
  _globals['_SEGMENTSUBCLUSTERCONFIG']._serialized_start=1609
  _globals['_SEGMENTSUBCLUSTERCONFIG']._serialized_end=1695
  _globals['_GREENPLUMCONFIG6']._serialized_start=1698
  _globals['_GREENPLUMCONFIG6']._serialized_end=2360
  _globals['_GREENPLUMCONFIG6_17']._serialized_start=2363
  _globals['_GREENPLUMCONFIG6_17']._serialized_end=2830
  _globals['_GREENPLUMCONFIG6_19']._serialized_start=2833
  _globals['_GREENPLUMCONFIG6_19']._serialized_end=3424
  _globals['_GREENPLUMCONFIG6_21']._serialized_start=3427
  _globals['_GREENPLUMCONFIG6_21']._serialized_end=4092
  _globals['_GREENPLUMCONFIG6_22']._serialized_start=4095
  _globals['_GREENPLUMCONFIG6_22']._serialized_end=4760
  _globals['_GREENPLUMCONFIGSET6_17']._serialized_start=4763
  _globals['_GREENPLUMCONFIGSET6_17']._serialized_end=5020
  _globals['_GREENPLUMCONFIGSET6_19']._serialized_start=5023
  _globals['_GREENPLUMCONFIGSET6_19']._serialized_end=5280
  _globals['_GREENPLUMCONFIGSET6_21']._serialized_start=5283
  _globals['_GREENPLUMCONFIGSET6_21']._serialized_end=5540
  _globals['_GREENPLUMCONFIGSET6_22']._serialized_start=5543
  _globals['_GREENPLUMCONFIGSET6_22']._serialized_end=5800
  _globals['_GREENPLUMCONFIGSET6']._serialized_start=5803
  _globals['_GREENPLUMCONFIGSET6']._serialized_end=6048
  _globals['_CONNECTIONPOOLERCONFIGSET']._serialized_start=6051
  _globals['_CONNECTIONPOOLERCONFIGSET']._serialized_end=6320
# @@protoc_insertion_point(module_scope)
