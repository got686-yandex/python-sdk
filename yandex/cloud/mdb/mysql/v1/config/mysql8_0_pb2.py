# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/mysql/v1/config/mysql8_0.proto
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
    'yandex/cloud/mdb/mysql/v1/config/mysql8_0.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/yandex/cloud/mdb/mysql/v1/config/mysql8_0.proto\x12 yandex.cloud.mdb.mysql.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xa0\x39\n\x0eMysqlConfig8_0\x12K\n\x17innodb_buffer_pool_size\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xfa\xc7\x31\t>=5242880\x12\x42\n\x0fmax_connections\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\x12\x35\n\x0flong_query_time\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\x0bgeneral_log\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\taudit_log\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12J\n\x08sql_mode\x18\x06 \x03(\x0e\x32\x38.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0.SQLMode\x12L\n\x12max_allowed_packet\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x13\xfa\xc7\x31\x0f\x31\x30\x32\x34-1073741824\x12\x62\n\x1d\x64\x65\x66\x61ult_authentication_plugin\x18\x08 \x01(\x0e\x32;.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0.AuthPlugin\x12L\n\x1einnodb_flush_log_at_trx_commit\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03\x31-2\x12J\n\x18innodb_lock_wait_timeout\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0b\xfa\xc7\x31\x07\x31-28800\x12\x64\n\x15transaction_isolation\x18\x0b \x01(\x0e\x32\x45.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0.TransactionIsolation\x12>\n\x1ainnodb_print_all_deadlocks\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x41\n\x10net_read_timeout\x18\r \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x31-1200\x12\x42\n\x11net_write_timeout\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x31-1200\x12I\n\x14group_concat_max_len\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n4-33554432\x12G\n\x0etmp_table_size\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x12\xfa\xc7\x31\x0e\x31\x30\x32\x34-536870912\x12M\n\x13max_heap_table_size\x18\x11 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x13\xfa\xc7\x31\x0f\x31\x36\x33\x38\x34-536870912\x12\x19\n\x11\x64\x65\x66\x61ult_time_zone\x18\x12 \x01(\t\x12\x1c\n\x14\x63haracter_set_server\x18\x13 \x01(\t\x12\x18\n\x10\x63ollation_server\x18\x14 \x01(\t\x12>\n\x1ainnodb_adaptive_hash_index\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12:\n\x16innodb_numa_interleave\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12R\n\x16innodb_log_buffer_size\x18\x17 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x15\xfa\xc7\x31\x11\x31\x30\x34\x38\x35\x37\x36-268435456\x12S\n\x14innodb_log_file_size\x18\x18 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x18\xfa\xc7\x31\x14\x32\x36\x38\x34\x33\x35\x34\x35\x36-4294967296\x12G\n\x12innodb_io_capacity\x18\x19 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n100-100000\x12K\n\x16innodb_io_capacity_max\x18\x1a \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n100-100000\x12\x45\n\x16innodb_read_io_threads\x18\x1b \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x31-16\x12\x46\n\x17innodb_write_io_threads\x18\x1c \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x31-16\x12\x43\n\x14innodb_purge_threads\x18\x1d \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x31-16\x12J\n\x19innodb_thread_concurrency\x18\x1e \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-1000\x12W\n\x1einnodb_temp_data_file_max_size\x18\x1f \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x12\xfa\xc7\x31\x0e\x30-107374182400\x12\x44\n\x11thread_cache_size\x18  \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-10000\x12\x46\n\x0cthread_stack\x18! \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x13\xfa\xc7\x31\x0f\x31\x33\x31\x30\x37\x32-16777216\x12H\n\x10join_buffer_size\x18\" \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x11\xfa\xc7\x31\r1024-16777216\x12H\n\x10sort_buffer_size\x18# \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x11\xfa\xc7\x31\r1024-16777216\x12K\n\x16table_definition_cache\x18$ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n400-524288\x12\x45\n\x10table_open_cache\x18% \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n400-524288\x12I\n\x1atable_open_cache_instances\x18& \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x31-32\x12\x43\n\x1f\x65xplicit_defaults_for_timestamp\x18\' \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12J\n\x18\x61uto_increment_increment\x18( \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0b\xfa\xc7\x31\x07\x31-65535\x12G\n\x15\x61uto_increment_offset\x18) \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0b\xfa\xc7\x31\x07\x31-65535\x12<\n\x0bsync_binlog\x18* \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-4096\x12I\n\x11\x62inlog_cache_size\x18+ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x11\xfa\xc7\x31\r4096-67108864\x12P\n\x1e\x62inlog_group_commit_sync_delay\x18, \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0b\xfa\xc7\x31\x07\x30-50000\x12Y\n\x10\x62inlog_row_image\x18- \x01(\x0e\x32?.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0.BinlogRowImage\x12@\n\x1c\x62inlog_rows_query_log_events\x18. \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12W\n)rpl_semi_sync_master_wait_for_slave_count\x18/ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03\x31-2\x12_\n\x13slave_parallel_type\x18\x30 \x01(\x0e\x32\x42.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0.SlaveParallelType\x12\x45\n\x16slave_parallel_workers\x18\x31 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x30-64\x12\x45\n\x11regexp_time_limit\x18\x32 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xfa\xc7\x31\t0-1048576\x12\\\n\x19mdb_preserve_binlog_bytes\x18\x33 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x1c\xfa\xc7\x31\x18\x31\x30\x37\x33\x37\x34\x31\x38\x32\x34-1099511627776\x12G\n\x13interactive_timeout\x18\x34 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xfa\xc7\x31\t600-86400\x12@\n\x0cwait_timeout\x18\x35 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xfa\xc7\x31\t600-86400\x12P\n\x1bmdb_offline_mode_enable_lag\x18\x36 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n600-432000\x12O\n\x1cmdb_offline_mode_disable_lag\x18\x37 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x36\x30-86400\x12X\n\x1crange_optimizer_max_mem_size\x18\x38 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x15\xfa\xc7\x31\x11\x31\x30\x34\x38\x35\x37\x36-268435456\x12\x32\n\x0eslow_query_log\x18\x39 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x46\n slow_query_log_always_write_time\x18: \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\\\n\x12log_slow_rate_type\x18; \x01(\x0e\x32@.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0.LogSlowRateType\x12\x44\n\x13log_slow_rate_limit\x18< \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x31-1000\x12:\n\x16log_slow_sp_statements\x18= \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12[\n\x0flog_slow_filter\x18> \x03(\x0e\x32\x42.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0.LogSlowFilterType\x12M\n\x1bmdb_priority_choice_max_lag\x18? \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0b\xfa\xc7\x31\x07\x30-86400\x12\x45\n\x10innodb_page_size\x18@ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n4096-65536\x12]\n innodb_online_alter_log_max_size\x18\x41 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x16\xfa\xc7\x31\x12\x36\x35\x35\x33\x36-107374182400\x12G\n\x18innodb_ft_min_token_size\x18\x42 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x30-16\x12H\n\x18innodb_ft_max_token_size\x18\x43 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\t\xfa\xc7\x31\x05\x31\x30-84\x12\x44\n\x16lower_case_table_names\x18\x44 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03\x30-1\x12\x46\n\x16max_sp_recursion_depth\x18\x45 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\t\xfa\xc7\x31\x05\x30-255\x12\x46\n\x18innodb_compression_level\x18\x46 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03\x30-9\x12\x84\x01\n&binlog_transaction_dependency_tracking\x18G \x01(\x0e\x32T.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0.BinlogTransactionDependencyTracking\x12.\n\nautocommit\x18H \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x14innodb_status_output\x18I \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x12innodb_strict_mode\x18J \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12G\n#innodb_print_lock_wait_timeout_info\x18K \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x41\n\x13log_error_verbosity\x18L \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03\x31-3\x12\x45\n\x11max_digest_length\x18M \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xfa\xc7\x31\t0-1048576\x12\x46\n\x11lock_wait_timeout\x18N \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n1-31536000\x12K\n\x17max_prepared_stmt_count\x18O \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xfa\xc7\x31\t0-4194304\x12\x18\n\x10optimizer_switch\x18P \x01(\t\x12\x45\n\x16optimizer_search_depth\x18Q \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x30-62\x12,\n\x08userstat\x18R \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12I\n\x12max_execution_time\x18S \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x10\xfa\xc7\x31\x0c\x30-4294967295\"\x88\x04\n\x07SQLMode\x12\x17\n\x13SQLMODE_UNSPECIFIED\x10\x00\x12\x17\n\x13\x41LLOW_INVALID_DATES\x10\x01\x12\x0f\n\x0b\x41NSI_QUOTES\x10\x02\x12\x1e\n\x1a\x45RROR_FOR_DIVISION_BY_ZERO\x10\x03\x12\x17\n\x13HIGH_NOT_PRECEDENCE\x10\x04\x12\x10\n\x0cIGNORE_SPACE\x10\x05\x12\x19\n\x15NO_AUTO_VALUE_ON_ZERO\x10\x06\x12\x18\n\x14NO_BACKSLASH_ESCAPES\x10\x07\x12\x1a\n\x16NO_ENGINE_SUBSTITUTION\x10\x08\x12\x1b\n\x17NO_UNSIGNED_SUBTRACTION\x10\t\x12\x10\n\x0cNO_ZERO_DATE\x10\n\x12\x13\n\x0fNO_ZERO_IN_DATE\x10\x0b\x12\x16\n\x12ONLY_FULL_GROUP_BY\x10\x0f\x12\x1b\n\x17PAD_CHAR_TO_FULL_LENGTH\x10\x10\x12\x13\n\x0fPIPES_AS_CONCAT\x10\x11\x12\x11\n\rREAL_AS_FLOAT\x10\x12\x12\x15\n\x11STRICT_ALL_TABLES\x10\x13\x12\x17\n\x13STRICT_TRANS_TABLES\x10\x14\x12\x1c\n\x18TIME_TRUNCATE_FRACTIONAL\x10\x15\x12\x08\n\x04\x41NSI\x10\x16\x12\x0f\n\x0bTRADITIONAL\x10\x17\x12\x14\n\x10NO_DIR_IN_CREATE\x10\x18\"t\n\nAuthPlugin\x12\x1b\n\x17\x41UTH_PLUGIN_UNSPECIFIED\x10\x00\x12\x19\n\x15MYSQL_NATIVE_PASSWORD\x10\x01\x12\x19\n\x15\x43\x41\x43HING_SHA2_PASSWORD\x10\x02\x12\x13\n\x0fSHA256_PASSWORD\x10\x03\"x\n\x14TransactionIsolation\x12%\n!TRANSACTION_ISOLATION_UNSPECIFIED\x10\x00\x12\x12\n\x0eREAD_COMMITTED\x10\x01\x12\x13\n\x0fREPEATABLE_READ\x10\x02\x12\x10\n\x0cSERIALIZABLE\x10\x03\"U\n\x0e\x42inlogRowImage\x12 \n\x1c\x42INLOG_ROW_IMAGE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\x12\x0b\n\x07MINIMAL\x10\x02\x12\n\n\x06NOBLOB\x10\x03\"Y\n\x11SlaveParallelType\x12#\n\x1fSLAVE_PARALLEL_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x44\x41TABASE\x10\x01\x12\x11\n\rLOGICAL_CLOCK\x10\x02\"M\n\x0fLogSlowRateType\x12\"\n\x1eLOG_SLOW_RATE_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07SESSION\x10\x01\x12\t\n\x05QUERY\x10\x02\"\xa1\x01\n\x11LogSlowFilterType\x12$\n LOG_SLOW_FILTER_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tFULL_SCAN\x10\x01\x12\r\n\tFULL_JOIN\x10\x02\x12\r\n\tTMP_TABLE\x10\x03\x12\x15\n\x11TMP_TABLE_ON_DISK\x10\x04\x12\x0c\n\x08\x46ILESORT\x10\x05\x12\x14\n\x10\x46ILESORT_ON_DISK\x10\x06\"\x93\x01\n#BinlogTransactionDependencyTracking\x12\x36\n2BINLOG_TRANSACTION_DEPENDENCY_TRACKING_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x43OMMIT_ORDER\x10\x01\x12\x0c\n\x08WRITESET\x10\x02\x12\x14\n\x10WRITESET_SESSION\x10\x03\"\xf0\x01\n\x11MysqlConfigSet8_0\x12J\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x30.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0\x12\x45\n\x0buser_config\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0\x12H\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mysql.v1.config.MysqlConfig8_0Br\n$yandex.cloud.api.mdb.mysql.v1.configZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1/config;mysqlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mysql.v1.config.mysql8_0_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$yandex.cloud.api.mdb.mysql.v1.configZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1/config;mysql'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_buffer_pool_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_buffer_pool_size']._serialized_options = b'\372\3071\t>=5242880'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_connections']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_connections']._serialized_options = b'\372\3071\01010-16384'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_allowed_packet']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_allowed_packet']._serialized_options = b'\372\3071\0171024-1073741824'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_flush_log_at_trx_commit']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_flush_log_at_trx_commit']._serialized_options = b'\372\3071\0031-2'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_lock_wait_timeout']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_lock_wait_timeout']._serialized_options = b'\372\3071\0071-28800'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['net_read_timeout']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['net_read_timeout']._serialized_options = b'\372\3071\0061-1200'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['net_write_timeout']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['net_write_timeout']._serialized_options = b'\372\3071\0061-1200'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['group_concat_max_len']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['group_concat_max_len']._serialized_options = b'\372\3071\n4-33554432'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['tmp_table_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['tmp_table_size']._serialized_options = b'\372\3071\0161024-536870912'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_heap_table_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_heap_table_size']._serialized_options = b'\372\3071\01716384-536870912'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_log_buffer_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_log_buffer_size']._serialized_options = b'\372\3071\0211048576-268435456'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_log_file_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_log_file_size']._serialized_options = b'\372\3071\024268435456-4294967296'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_io_capacity']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_io_capacity']._serialized_options = b'\372\3071\n100-100000'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_io_capacity_max']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_io_capacity_max']._serialized_options = b'\372\3071\n100-100000'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_read_io_threads']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_read_io_threads']._serialized_options = b'\372\3071\0041-16'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_write_io_threads']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_write_io_threads']._serialized_options = b'\372\3071\0041-16'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_purge_threads']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_purge_threads']._serialized_options = b'\372\3071\0041-16'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_thread_concurrency']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_thread_concurrency']._serialized_options = b'\372\3071\0060-1000'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_temp_data_file_max_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_temp_data_file_max_size']._serialized_options = b'\372\3071\0160-107374182400'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['thread_cache_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['thread_cache_size']._serialized_options = b'\372\3071\01010-10000'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['thread_stack']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['thread_stack']._serialized_options = b'\372\3071\017131072-16777216'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['join_buffer_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['join_buffer_size']._serialized_options = b'\372\3071\r1024-16777216'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['sort_buffer_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['sort_buffer_size']._serialized_options = b'\372\3071\r1024-16777216'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['table_definition_cache']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['table_definition_cache']._serialized_options = b'\372\3071\n400-524288'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['table_open_cache']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['table_open_cache']._serialized_options = b'\372\3071\n400-524288'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['table_open_cache_instances']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['table_open_cache_instances']._serialized_options = b'\372\3071\0041-32'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['auto_increment_increment']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['auto_increment_increment']._serialized_options = b'\372\3071\0071-65535'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['auto_increment_offset']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['auto_increment_offset']._serialized_options = b'\372\3071\0071-65535'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['sync_binlog']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['sync_binlog']._serialized_options = b'\372\3071\0060-4096'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['binlog_cache_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['binlog_cache_size']._serialized_options = b'\372\3071\r4096-67108864'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['binlog_group_commit_sync_delay']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['binlog_group_commit_sync_delay']._serialized_options = b'\372\3071\0070-50000'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['rpl_semi_sync_master_wait_for_slave_count']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['rpl_semi_sync_master_wait_for_slave_count']._serialized_options = b'\372\3071\0031-2'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['slave_parallel_workers']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['slave_parallel_workers']._serialized_options = b'\372\3071\0040-64'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['regexp_time_limit']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['regexp_time_limit']._serialized_options = b'\372\3071\t0-1048576'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['mdb_preserve_binlog_bytes']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['mdb_preserve_binlog_bytes']._serialized_options = b'\372\3071\0301073741824-1099511627776'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['interactive_timeout']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['interactive_timeout']._serialized_options = b'\372\3071\t600-86400'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['wait_timeout']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['wait_timeout']._serialized_options = b'\372\3071\t600-86400'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['mdb_offline_mode_enable_lag']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['mdb_offline_mode_enable_lag']._serialized_options = b'\372\3071\n600-432000'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['mdb_offline_mode_disable_lag']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['mdb_offline_mode_disable_lag']._serialized_options = b'\372\3071\01060-86400'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['range_optimizer_max_mem_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['range_optimizer_max_mem_size']._serialized_options = b'\372\3071\0211048576-268435456'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['log_slow_rate_limit']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['log_slow_rate_limit']._serialized_options = b'\372\3071\0061-1000'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['mdb_priority_choice_max_lag']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['mdb_priority_choice_max_lag']._serialized_options = b'\372\3071\0070-86400'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_page_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_page_size']._serialized_options = b'\372\3071\n4096-65536'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_online_alter_log_max_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_online_alter_log_max_size']._serialized_options = b'\372\3071\02265536-107374182400'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_ft_min_token_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_ft_min_token_size']._serialized_options = b'\372\3071\0040-16'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_ft_max_token_size']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_ft_max_token_size']._serialized_options = b'\372\3071\00510-84'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['lower_case_table_names']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['lower_case_table_names']._serialized_options = b'\372\3071\0030-1'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_sp_recursion_depth']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_sp_recursion_depth']._serialized_options = b'\372\3071\0050-255'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_compression_level']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['innodb_compression_level']._serialized_options = b'\372\3071\0030-9'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['log_error_verbosity']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['log_error_verbosity']._serialized_options = b'\372\3071\0031-3'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_digest_length']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_digest_length']._serialized_options = b'\372\3071\t0-1048576'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['lock_wait_timeout']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['lock_wait_timeout']._serialized_options = b'\372\3071\n1-31536000'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_prepared_stmt_count']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_prepared_stmt_count']._serialized_options = b'\372\3071\t0-4194304'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['optimizer_search_depth']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['optimizer_search_depth']._serialized_options = b'\372\3071\0040-62'
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_execution_time']._loaded_options = None
  _globals['_MYSQLCONFIG8_0'].fields_by_name['max_execution_time']._serialized_options = b'\372\3071\0140-4294967295'
  _globals['_MYSQLCONFIG8_0']._serialized_start=149
  _globals['_MYSQLCONFIG8_0']._serialized_end=7477
  _globals['_MYSQLCONFIG8_0_SQLMODE']._serialized_start=6146
  _globals['_MYSQLCONFIG8_0_SQLMODE']._serialized_end=6666
  _globals['_MYSQLCONFIG8_0_AUTHPLUGIN']._serialized_start=6668
  _globals['_MYSQLCONFIG8_0_AUTHPLUGIN']._serialized_end=6784
  _globals['_MYSQLCONFIG8_0_TRANSACTIONISOLATION']._serialized_start=6786
  _globals['_MYSQLCONFIG8_0_TRANSACTIONISOLATION']._serialized_end=6906
  _globals['_MYSQLCONFIG8_0_BINLOGROWIMAGE']._serialized_start=6908
  _globals['_MYSQLCONFIG8_0_BINLOGROWIMAGE']._serialized_end=6993
  _globals['_MYSQLCONFIG8_0_SLAVEPARALLELTYPE']._serialized_start=6995
  _globals['_MYSQLCONFIG8_0_SLAVEPARALLELTYPE']._serialized_end=7084
  _globals['_MYSQLCONFIG8_0_LOGSLOWRATETYPE']._serialized_start=7086
  _globals['_MYSQLCONFIG8_0_LOGSLOWRATETYPE']._serialized_end=7163
  _globals['_MYSQLCONFIG8_0_LOGSLOWFILTERTYPE']._serialized_start=7166
  _globals['_MYSQLCONFIG8_0_LOGSLOWFILTERTYPE']._serialized_end=7327
  _globals['_MYSQLCONFIG8_0_BINLOGTRANSACTIONDEPENDENCYTRACKING']._serialized_start=7330
  _globals['_MYSQLCONFIG8_0_BINLOGTRANSACTIONDEPENDENCYTRACKING']._serialized_end=7477
  _globals['_MYSQLCONFIGSET8_0']._serialized_start=7480
  _globals['_MYSQLCONFIGSET8_0']._serialized_end=7720
# @@protoc_insertion_point(module_scope)
