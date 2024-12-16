# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/clickhouse/v1/user.proto
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
    'yandex/cloud/mdb/clickhouse/v1/user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/mdb/clickhouse/v1/user.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xe4\x01\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12?\n\x0bpermissions\x18\x03 \x03(\x0b\x32*.yandex.cloud.mdb.clickhouse.v1.Permission\x12>\n\x08settings\x18\x04 \x01(\x0b\x32,.yandex.cloud.mdb.clickhouse.v1.UserSettings\x12\x39\n\x06quotas\x18\x05 \x03(\x0b\x32).yandex.cloud.mdb.clickhouse.v1.UserQuota\")\n\nPermission\x12\x15\n\rdatabase_name\x18\x01 \x01(\tJ\x04\x08\x02\x10\x03\"\xa1\x02\n\x08UserSpec\x12\x38\n\x04name\x18\x01 \x01(\tB*\xe8\xc7\x31\x01\xf2\xc7\x31\x1a[a-zA-Z0-9_][a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12\x1f\n\x08password\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x38-128\x12?\n\x0bpermissions\x18\x03 \x03(\x0b\x32*.yandex.cloud.mdb.clickhouse.v1.Permission\x12>\n\x08settings\x18\x04 \x01(\x0b\x32,.yandex.cloud.mdb.clickhouse.v1.UserSettings\x12\x39\n\x06quotas\x18\x05 \x03(\x0b\x32).yandex.cloud.mdb.clickhouse.v1.UserQuota\"\xac\x63\n\x0cUserSettings\x12\x36\n\x08readonly\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03\x30-2\x12-\n\tallow_ddl\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x41\n\x1d\x61llow_introspection_functions\x18` \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x0f\x63onnect_timeout\x18\' \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12J\n\x1d\x63onnect_timeout_with_failover\x18\x61 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12<\n\x0freceive_timeout\x18( \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12\x39\n\x0csend_timeout\x18) \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12L\n\'timeout_before_checking_execution_speed\x18\x62 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\rinsert_quorum\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x46\n\x15insert_quorum_timeout\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06>=1000\x12:\n\x16insert_quorum_parallel\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12:\n\x16insert_null_as_default\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x41\n\x1dselect_sequential_consistency\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12V\n2deduplicate_blocks_in_dependent_materialized_views\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12O\n!replication_alter_partitions_sync\x18* \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03\x30-2\x12Z\n)max_replica_delay_for_distributed_queries\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06>=1000\x12V\n2fallback_to_stale_replicas_for_distributed_queries\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x65\n\x18\x64istributed_product_mode\x18+ \x01(\x0e\x32\x43.yandex.cloud.mdb.clickhouse.v1.UserSettings.DistributedProductMode\x12L\n(distributed_aggregation_memory_efficient\x18H \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x41\n\x1c\x64istributed_ddl_task_timeout\x18I \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x17skip_unavailable_shards\x18Q \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x37\n\x13\x63ompile_expressions\x18. \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12M\n\x1fmin_count_to_compile_expression\x18/ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12;\n\x0emax_block_size\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12H\n\x1amin_insert_block_size_rows\x18\x30 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12I\n\x1bmin_insert_block_size_bytes\x18\x31 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x42\n\x15max_insert_block_size\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12H\n\x1amin_bytes_to_use_direct_io\x18\x32 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12:\n\x16use_uncompressed_cache\x18\x33 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12M\n merge_tree_max_rows_to_use_cache\x18\x34 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12N\n!merge_tree_max_bytes_to_use_cache\x18\x35 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12T\n\'merge_tree_min_rows_for_concurrent_read\x18\x36 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12U\n(merge_tree_min_bytes_for_concurrent_read\x18\x37 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12G\n\"max_bytes_before_external_group_by\x18J \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x43\n\x1emax_bytes_before_external_sort\x18K \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x41\n\x1cgroup_by_two_level_threshold\x18L \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12G\n\"group_by_two_level_threshold_bytes\x18M \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x08priority\x18\x38 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x38\n\x0bmax_threads\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12>\n\x10max_memory_usage\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12G\n\x19max_memory_usage_for_user\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12:\n\x15max_network_bandwidth\x18\x39 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x43\n\x1emax_network_bandwidth_for_user\x18: \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x44\n\x1fmax_partitions_per_insert_block\x18\x66 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x44\n\x1fmax_concurrent_queries_for_user\x18g \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x37\n\x13\x66orce_index_by_date\x18; \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\x11\x66orce_primary_key\x18< \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12>\n\x10max_rows_to_read\x18\r \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12?\n\x11max_bytes_to_read\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12U\n\x12read_overflow_mode\x18\x0f \x01(\x0e\x32\x39.yandex.cloud.mdb.clickhouse.v1.UserSettings.OverflowMode\x12\x42\n\x14max_rows_to_group_by\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12`\n\x16group_by_overflow_mode\x18\x11 \x01(\x0e\x32@.yandex.cloud.mdb.clickhouse.v1.UserSettings.GroupByOverflowMode\x12>\n\x10max_rows_to_sort\x18\x12 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12?\n\x11max_bytes_to_sort\x18\x13 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12U\n\x12sort_overflow_mode\x18\x14 \x01(\x0e\x32\x39.yandex.cloud.mdb.clickhouse.v1.UserSettings.OverflowMode\x12=\n\x0fmax_result_rows\x18\x15 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12>\n\x10max_result_bytes\x18\x16 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12W\n\x14result_overflow_mode\x18\x17 \x01(\x0e\x32\x39.yandex.cloud.mdb.clickhouse.v1.UserSettings.OverflowMode\x12\x42\n\x14max_rows_in_distinct\x18\x18 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x43\n\x15max_bytes_in_distinct\x18\x19 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12Y\n\x16\x64istinct_overflow_mode\x18\x1a \x01(\x0e\x32\x39.yandex.cloud.mdb.clickhouse.v1.UserSettings.OverflowMode\x12\x42\n\x14max_rows_to_transfer\x18\x1b \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x43\n\x15max_bytes_to_transfer\x18\x1c \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12Y\n\x16transfer_overflow_mode\x18\x1d \x01(\x0e\x32\x39.yandex.cloud.mdb.clickhouse.v1.UserSettings.OverflowMode\x12@\n\x12max_execution_time\x18\x1e \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12X\n\x15timeout_overflow_mode\x18\x1f \x01(\x0e\x32\x39.yandex.cloud.mdb.clickhouse.v1.UserSettings.OverflowMode\x12=\n\x0fmax_rows_in_set\x18W \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12>\n\x10max_bytes_in_set\x18X \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12T\n\x11set_overflow_mode\x18Y \x01(\x0e\x32\x39.yandex.cloud.mdb.clickhouse.v1.UserSettings.OverflowMode\x12>\n\x10max_rows_in_join\x18Z \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12?\n\x11max_bytes_in_join\x18[ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12U\n\x12join_overflow_mode\x18\\ \x01(\x0e\x32\x39.yandex.cloud.mdb.clickhouse.v1.UserSettings.OverflowMode\x12R\n\x0ejoin_algorithm\x18h \x03(\x0e\x32:.yandex.cloud.mdb.clickhouse.v1.UserSettings.JoinAlgorithm\x12\x46\n\"any_join_distinct_right_table_keys\x18i \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x41\n\x13max_columns_to_read\x18  \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x43\n\x15max_temporary_columns\x18! \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12M\n\x1fmax_temporary_non_const_columns\x18\" \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12;\n\x0emax_query_size\x18# \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12:\n\rmax_ast_depth\x18$ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12=\n\x10max_ast_elements\x18% \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12\x46\n\x19max_expanded_ast_elements\x18& \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12\x41\n\x13min_execution_speed\x18T \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12G\n\x19min_execution_speed_bytes\x18U \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12o\n\x1d\x63ount_distinct_implementation\x18V \x01(\x0e\x32H.yandex.cloud.mdb.clickhouse.v1.UserSettings.CountDistinctImplementation\x12M\n)input_format_values_interpret_expressions\x18= \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12L\n(input_format_defaults_for_omitted_fields\x18> \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12@\n\x1cinput_format_null_as_default\x18j \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12`\n\x16\x64\x61te_time_input_format\x18k \x01(\x0e\x32@.yandex.cloud.mdb.clickhouse.v1.UserSettings.DateTimeInputFormat\x12\x46\n\"input_format_with_names_use_header\x18l \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12p\n\'output_format_json_quote_64bit_integers\x18? \x01(\x0b\x32\x1a.google.protobuf.BoolValueR#outputFormatJsonQuote_64bitIntegers\x12\x46\n\"output_format_json_quote_denormals\x18@ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x62\n\x17\x64\x61te_time_output_format\x18m \x01(\x0e\x32\x41.yandex.cloud.mdb.clickhouse.v1.UserSettings.DateTimeOutputFormat\x12J\n&low_cardinality_allow_in_native_format\x18N \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12J\n&allow_suspicious_low_cardinality_types\x18n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12M\n)empty_result_for_aggregation_by_empty_set\x18O \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x17http_connection_timeout\x18\x41 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14http_receive_timeout\x18\x42 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11http_send_timeout\x18\x43 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x17\x65nable_http_compression\x18\x44 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x41\n\x1dsend_progress_in_http_headers\x18\x45 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x43\n\x1ehttp_headers_progress_interval\x18\x46 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x14\x61\x64\x64_http_cors_header\x18G \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12P\n,cancel_http_readonly_queries_on_client_close\x18o \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12;\n\x16max_http_get_redirects\x18p \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\x1ejoined_subquery_requires_alias\x18] \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0ejoin_use_nulls\x18^ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\x11transform_null_in\x18_ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12J\n\nquota_mode\x18P \x01(\x0e\x32\x36.yandex.cloud.mdb.clickhouse.v1.UserSettings.QuotaMode\x12\x32\n\x0e\x66latten_nested\x18q \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x15\n\rformat_regexp\x18r \x01(\t\x12j\n\x1b\x66ormat_regexp_escaping_rule\x18s \x01(\x0e\x32\x45.yandex.cloud.mdb.clickhouse.v1.UserSettings.FormatRegexpEscapingRule\x12@\n\x1c\x66ormat_regexp_skip_unmatched\x18t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\x0c\x61sync_insert\x18u \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x14\x61sync_insert_threads\x18v \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x15wait_for_async_insert\x18w \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x42\n\x1dwait_for_async_insert_timeout\x18x \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12?\n\x1a\x61sync_insert_max_data_size\x18y \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19\x61sync_insert_busy_timeout\x18z \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12?\n\x1a\x61sync_insert_stale_timeout\x18{ \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14memory_profiler_step\x18| \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12H\n\"memory_profiler_sample_probability\x18} \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12?\n\x11max_final_threads\x18~ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x41\n\x1dinput_format_parallel_parsing\x18\x7f \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x44\n\x1finput_format_import_nested_json\x18\x80\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12m\n\x1clocal_filesystem_read_method\x18\x81\x01 \x01(\x0e\x32\x46.yandex.cloud.mdb.clickhouse.v1.UserSettings.LocalFilesystemReadMethod\x12\x42\n\x14max_read_buffer_size\x18\x82\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\x12H\n\x19insert_keeper_max_retries\x18\x83\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12W\n(max_temporary_data_on_disk_size_for_user\x18\x84\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12X\n)max_temporary_data_on_disk_size_for_query\x18\x85\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12?\n\x10max_parser_depth\x18\x86\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12o\n\x1dremote_filesystem_read_method\x18\x87\x01 \x01(\x0e\x32G.yandex.cloud.mdb.clickhouse.v1.UserSettings.RemoteFilesystemReadMethod\x12R\n#memory_overcommit_ratio_denominator\x18\x88\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12[\n,memory_overcommit_ratio_denominator_for_user\x18\x89\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\\\n-memory_usage_overcommit_max_wait_microseconds\x18\x8a\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x36\n\x11log_query_threads\x18\x8b\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x41\n\x12max_insert_threads\x18\x8c\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x38\n\x13use_hedged_requests\x18\x8d\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x46\n\x17idle_connection_timeout\x18\x8e\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12K\n\x1chedged_connection_timeout_ms\x18\x8f\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12S\n\x0eload_balancing\x18\x90\x01 \x01(\x0e\x32:.yandex.cloud.mdb.clickhouse.v1.UserSettings.LoadBalancing\x12=\n\x18prefer_localhost_replica\x18\x91\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x07\x63ompile\x18, \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x02\x18\x01\x12=\n\x14min_count_to_compile\x18- \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x02\x18\x01\"_\n\x0cOverflowMode\x12\x1d\n\x19OVERFLOW_MODE_UNSPECIFIED\x10\x00\x12\x17\n\x13OVERFLOW_MODE_THROW\x10\x01\x12\x17\n\x13OVERFLOW_MODE_BREAK\x10\x02\"\xa1\x01\n\x13GroupByOverflowMode\x12&\n\"GROUP_BY_OVERFLOW_MODE_UNSPECIFIED\x10\x00\x12 \n\x1cGROUP_BY_OVERFLOW_MODE_THROW\x10\x01\x12 \n\x1cGROUP_BY_OVERFLOW_MODE_BREAK\x10\x02\x12\x1e\n\x1aGROUP_BY_OVERFLOW_MODE_ANY\x10\x03\"\xd2\x01\n\x16\x44istributedProductMode\x12(\n$DISTRIBUTED_PRODUCT_MODE_UNSPECIFIED\x10\x00\x12!\n\x1d\x44ISTRIBUTED_PRODUCT_MODE_DENY\x10\x01\x12\"\n\x1e\x44ISTRIBUTED_PRODUCT_MODE_LOCAL\x10\x02\x12#\n\x1f\x44ISTRIBUTED_PRODUCT_MODE_GLOBAL\x10\x03\x12\"\n\x1e\x44ISTRIBUTED_PRODUCT_MODE_ALLOW\x10\x04\"q\n\tQuotaMode\x12\x1a\n\x16QUOTA_MODE_UNSPECIFIED\x10\x00\x12\x16\n\x12QUOTA_MODE_DEFAULT\x10\x01\x12\x14\n\x10QUOTA_MODE_KEYED\x10\x02\x12\x1a\n\x16QUOTA_MODE_KEYED_BY_IP\x10\x03\"\xb6\x02\n\x1b\x43ountDistinctImplementation\x12-\n)COUNT_DISTINCT_IMPLEMENTATION_UNSPECIFIED\x10\x00\x12&\n\"COUNT_DISTINCT_IMPLEMENTATION_UNIQ\x10\x01\x12/\n+COUNT_DISTINCT_IMPLEMENTATION_UNIQ_COMBINED\x10\x02\x12\x32\n.COUNT_DISTINCT_IMPLEMENTATION_UNIQ_COMBINED_64\x10\x03\x12-\n)COUNT_DISTINCT_IMPLEMENTATION_UNIQ_HLL_12\x10\x04\x12,\n(COUNT_DISTINCT_IMPLEMENTATION_UNIQ_EXACT\x10\x05\"\x90\x02\n\rJoinAlgorithm\x12\x1e\n\x1aJOIN_ALGORITHM_UNSPECIFIED\x10\x00\x12\x17\n\x13JOIN_ALGORITHM_HASH\x10\x01\x12 \n\x1cJOIN_ALGORITHM_PARALLEL_HASH\x10\x02\x12 \n\x1cJOIN_ALGORITHM_PARTIAL_MERGE\x10\x03\x12\x19\n\x15JOIN_ALGORITHM_DIRECT\x10\x04\x12\x17\n\x13JOIN_ALGORITHM_AUTO\x10\x05\x12%\n!JOIN_ALGORITHM_FULL_SORTING_MERGE\x10\x06\x12\'\n#JOIN_ALGORITHM_PREFER_PARTIAL_MERGE\x10\x07\"\xad\x02\n\x18\x46ormatRegexpEscapingRule\x12+\n\'FORMAT_REGEXP_ESCAPING_RULE_UNSPECIFIED\x10\x00\x12\'\n#FORMAT_REGEXP_ESCAPING_RULE_ESCAPED\x10\x01\x12&\n\"FORMAT_REGEXP_ESCAPING_RULE_QUOTED\x10\x02\x12#\n\x1f\x46ORMAT_REGEXP_ESCAPING_RULE_CSV\x10\x03\x12$\n FORMAT_REGEXP_ESCAPING_RULE_JSON\x10\x04\x12#\n\x1f\x46ORMAT_REGEXP_ESCAPING_RULE_XML\x10\x05\x12#\n\x1f\x46ORMAT_REGEXP_ESCAPING_RULE_RAW\x10\x06\"\xb2\x01\n\x13\x44\x61teTimeInputFormat\x12&\n\"DATE_TIME_INPUT_FORMAT_UNSPECIFIED\x10\x00\x12&\n\"DATE_TIME_INPUT_FORMAT_BEST_EFFORT\x10\x01\x12 \n\x1c\x44\x41TE_TIME_INPUT_FORMAT_BASIC\x10\x02\x12)\n%DATE_TIME_INPUT_FORMAT_BEST_EFFORT_US\x10\x03\"\xb0\x01\n\x14\x44\x61teTimeOutputFormat\x12\'\n#DATE_TIME_OUTPUT_FORMAT_UNSPECIFIED\x10\x00\x12\"\n\x1e\x44\x41TE_TIME_OUTPUT_FORMAT_SIMPLE\x10\x01\x12\x1f\n\x1b\x44\x41TE_TIME_OUTPUT_FORMAT_ISO\x10\x02\x12*\n&DATE_TIME_OUTPUT_FORMAT_UNIX_TIMESTAMP\x10\x03\"\xf2\x01\n\x19LocalFilesystemReadMethod\x12,\n(LOCAL_FILESYSTEM_READ_METHOD_UNSPECIFIED\x10\x00\x12%\n!LOCAL_FILESYSTEM_READ_METHOD_READ\x10\x01\x12\x31\n-LOCAL_FILESYSTEM_READ_METHOD_PREAD_THREADPOOL\x10\x02\x12&\n\"LOCAL_FILESYSTEM_READ_METHOD_PREAD\x10\x03\x12%\n!LOCAL_FILESYSTEM_READ_METHOD_NMAP\x10\x04\"\xa1\x01\n\x1aRemoteFilesystemReadMethod\x12-\n)REMOTE_FILESYSTEM_READ_METHOD_UNSPECIFIED\x10\x00\x12&\n\"REMOTE_FILESYSTEM_READ_METHOD_READ\x10\x01\x12,\n(REMOTE_FILESYSTEM_READ_METHOD_THREADPOOL\x10\x02\"\xd0\x01\n\rLoadBalancing\x12\x1e\n\x1aLOAD_BALANCING_UNSPECIFIED\x10\x00\x12\x19\n\x15LOAD_BALANCING_RANDOM\x10\x01\x12#\n\x1fLOAD_BALANCING_NEAREST_HOSTNAME\x10\x02\x12\x1b\n\x17LOAD_BALANCING_IN_ORDER\x10\x03\x12\"\n\x1eLOAD_BALANCING_FIRST_OR_RANDOM\x10\x04\x12\x1e\n\x1aLOAD_BALANCING_ROUND_ROBIN\x10\x05J\x04\x08R\x10T\"\xee\x02\n\tUserQuota\x12\x42\n\x11interval_duration\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06>=1000\x12\x35\n\x07queries\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x34\n\x06\x65rrors\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x39\n\x0bresult_rows\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x37\n\tread_rows\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12<\n\x0e\x65xecution_time\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0Bs\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.clickhouse.v1.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse'
  _globals['_USERSPEC'].fields_by_name['name']._loaded_options = None
  _globals['_USERSPEC'].fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\032[a-zA-Z0-9_][a-zA-Z0-9_-]*\212\3101\004<=63'
  _globals['_USERSPEC'].fields_by_name['password']._loaded_options = None
  _globals['_USERSPEC'].fields_by_name['password']._serialized_options = b'\350\3071\001\212\3101\0058-128'
  _globals['_USERSETTINGS'].fields_by_name['readonly']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['readonly']._serialized_options = b'\372\3071\0030-2'
  _globals['_USERSETTINGS'].fields_by_name['connect_timeout']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['connect_timeout']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['connect_timeout_with_failover']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['connect_timeout_with_failover']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['receive_timeout']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['receive_timeout']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['send_timeout']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['send_timeout']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['insert_quorum']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['insert_quorum']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['insert_quorum_timeout']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['insert_quorum_timeout']._serialized_options = b'\372\3071\006>=1000'
  _globals['_USERSETTINGS'].fields_by_name['replication_alter_partitions_sync']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['replication_alter_partitions_sync']._serialized_options = b'\372\3071\0030-2'
  _globals['_USERSETTINGS'].fields_by_name['max_replica_delay_for_distributed_queries']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_replica_delay_for_distributed_queries']._serialized_options = b'\372\3071\006>=1000'
  _globals['_USERSETTINGS'].fields_by_name['min_count_to_compile_expression']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['min_count_to_compile_expression']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_block_size']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_block_size']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['min_insert_block_size_rows']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['min_insert_block_size_rows']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['min_insert_block_size_bytes']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['min_insert_block_size_bytes']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_insert_block_size']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_insert_block_size']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['min_bytes_to_use_direct_io']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['min_bytes_to_use_direct_io']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['merge_tree_max_rows_to_use_cache']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['merge_tree_max_rows_to_use_cache']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['merge_tree_max_bytes_to_use_cache']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['merge_tree_max_bytes_to_use_cache']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['merge_tree_min_rows_for_concurrent_read']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['merge_tree_min_rows_for_concurrent_read']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['merge_tree_min_bytes_for_concurrent_read']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['merge_tree_min_bytes_for_concurrent_read']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['priority']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['priority']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_threads']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_threads']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['max_memory_usage']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_memory_usage']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_memory_usage_for_user']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_memory_usage_for_user']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_rows_to_read']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_rows_to_read']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_to_read']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_to_read']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_rows_to_group_by']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_rows_to_group_by']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_rows_to_sort']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_rows_to_sort']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_to_sort']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_to_sort']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_result_rows']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_result_rows']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_result_bytes']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_result_bytes']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_rows_in_distinct']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_rows_in_distinct']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_in_distinct']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_in_distinct']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_rows_to_transfer']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_rows_to_transfer']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_to_transfer']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_to_transfer']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_execution_time']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_execution_time']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_rows_in_set']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_rows_in_set']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_in_set']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_in_set']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_rows_in_join']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_rows_in_join']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_in_join']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_bytes_in_join']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_columns_to_read']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_columns_to_read']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_temporary_columns']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_temporary_columns']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_temporary_non_const_columns']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_temporary_non_const_columns']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_query_size']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_query_size']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['max_ast_depth']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_ast_depth']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['max_ast_elements']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_ast_elements']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['max_expanded_ast_elements']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_expanded_ast_elements']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['min_execution_speed']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['min_execution_speed']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['min_execution_speed_bytes']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['min_execution_speed_bytes']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_final_threads']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_final_threads']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_read_buffer_size']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_read_buffer_size']._serialized_options = b'\372\3071\002>0'
  _globals['_USERSETTINGS'].fields_by_name['insert_keeper_max_retries']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['insert_keeper_max_retries']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_temporary_data_on_disk_size_for_user']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_temporary_data_on_disk_size_for_user']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_temporary_data_on_disk_size_for_query']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_temporary_data_on_disk_size_for_query']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_parser_depth']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_parser_depth']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['memory_overcommit_ratio_denominator']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['memory_overcommit_ratio_denominator']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['memory_overcommit_ratio_denominator_for_user']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['memory_overcommit_ratio_denominator_for_user']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['memory_usage_overcommit_max_wait_microseconds']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['memory_usage_overcommit_max_wait_microseconds']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['max_insert_threads']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['max_insert_threads']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['idle_connection_timeout']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['idle_connection_timeout']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['hedged_connection_timeout_ms']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['hedged_connection_timeout_ms']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERSETTINGS'].fields_by_name['compile']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['compile']._serialized_options = b'\030\001'
  _globals['_USERSETTINGS'].fields_by_name['min_count_to_compile']._loaded_options = None
  _globals['_USERSETTINGS'].fields_by_name['min_count_to_compile']._serialized_options = b'\030\001'
  _globals['_USERQUOTA'].fields_by_name['interval_duration']._loaded_options = None
  _globals['_USERQUOTA'].fields_by_name['interval_duration']._serialized_options = b'\372\3071\006>=1000'
  _globals['_USERQUOTA'].fields_by_name['queries']._loaded_options = None
  _globals['_USERQUOTA'].fields_by_name['queries']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERQUOTA'].fields_by_name['errors']._loaded_options = None
  _globals['_USERQUOTA'].fields_by_name['errors']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERQUOTA'].fields_by_name['result_rows']._loaded_options = None
  _globals['_USERQUOTA'].fields_by_name['result_rows']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERQUOTA'].fields_by_name['read_rows']._loaded_options = None
  _globals['_USERQUOTA'].fields_by_name['read_rows']._serialized_options = b'\372\3071\003>=0'
  _globals['_USERQUOTA'].fields_by_name['execution_time']._loaded_options = None
  _globals['_USERQUOTA'].fields_by_name['execution_time']._serialized_options = b'\372\3071\003>=0'
  _globals['_USER']._serialized_start=141
  _globals['_USER']._serialized_end=369
  _globals['_PERMISSION']._serialized_start=371
  _globals['_PERMISSION']._serialized_end=412
  _globals['_USERSPEC']._serialized_start=415
  _globals['_USERSPEC']._serialized_end=704
  _globals['_USERSETTINGS']._serialized_start=707
  _globals['_USERSETTINGS']._serialized_end=13423
  _globals['_USERSETTINGS_OVERFLOWMODE']._serialized_start=10958
  _globals['_USERSETTINGS_OVERFLOWMODE']._serialized_end=11053
  _globals['_USERSETTINGS_GROUPBYOVERFLOWMODE']._serialized_start=11056
  _globals['_USERSETTINGS_GROUPBYOVERFLOWMODE']._serialized_end=11217
  _globals['_USERSETTINGS_DISTRIBUTEDPRODUCTMODE']._serialized_start=11220
  _globals['_USERSETTINGS_DISTRIBUTEDPRODUCTMODE']._serialized_end=11430
  _globals['_USERSETTINGS_QUOTAMODE']._serialized_start=11432
  _globals['_USERSETTINGS_QUOTAMODE']._serialized_end=11545
  _globals['_USERSETTINGS_COUNTDISTINCTIMPLEMENTATION']._serialized_start=11548
  _globals['_USERSETTINGS_COUNTDISTINCTIMPLEMENTATION']._serialized_end=11858
  _globals['_USERSETTINGS_JOINALGORITHM']._serialized_start=11861
  _globals['_USERSETTINGS_JOINALGORITHM']._serialized_end=12133
  _globals['_USERSETTINGS_FORMATREGEXPESCAPINGRULE']._serialized_start=12136
  _globals['_USERSETTINGS_FORMATREGEXPESCAPINGRULE']._serialized_end=12437
  _globals['_USERSETTINGS_DATETIMEINPUTFORMAT']._serialized_start=12440
  _globals['_USERSETTINGS_DATETIMEINPUTFORMAT']._serialized_end=12618
  _globals['_USERSETTINGS_DATETIMEOUTPUTFORMAT']._serialized_start=12621
  _globals['_USERSETTINGS_DATETIMEOUTPUTFORMAT']._serialized_end=12797
  _globals['_USERSETTINGS_LOCALFILESYSTEMREADMETHOD']._serialized_start=12800
  _globals['_USERSETTINGS_LOCALFILESYSTEMREADMETHOD']._serialized_end=13042
  _globals['_USERSETTINGS_REMOTEFILESYSTEMREADMETHOD']._serialized_start=13045
  _globals['_USERSETTINGS_REMOTEFILESYSTEMREADMETHOD']._serialized_end=13206
  _globals['_USERSETTINGS_LOADBALANCING']._serialized_start=13209
  _globals['_USERSETTINGS_LOADBALANCING']._serialized_end=13417
  _globals['_USERQUOTA']._serialized_start=13426
  _globals['_USERQUOTA']._serialized_end=13792
# @@protoc_insertion_point(module_scope)
