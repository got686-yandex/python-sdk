# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/loadtesting/agent/v1/monitoring_service.proto
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
    'yandex/cloud/loadtesting/agent/v1/monitoring_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/loadtesting/agent/v1/monitoring_service.proto\x12!yandex.cloud.loadtesting.agent.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\"\xca\x01\n\x10\x41\x64\x64MetricRequest\x12%\n\x13\x63ompute_instance_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1c\n\x06job_id\x18\x03 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x46\n\x06\x63hunks\x18\x04 \x03(\x0b\x32..yandex.cloud.loadtesting.agent.v1.MetricChunkB\x06\x82\xc8\x31\x02>0\x12#\n\x11\x61gent_instance_id\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=50J\x04\x08\x02\x10\x03\"\x8f\x01\n\x0bMetricChunk\x12?\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32).yandex.cloud.loadtesting.agent.v1.MetricB\x06\x82\xc8\x31\x02>0\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x1b\n\rinstance_host\x18\x04 \x01(\tB\x04\xe8\xc7\x31\x01\"T\n\x06Metric\x12\x19\n\x0bmetric_type\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x19\n\x0bmetric_name\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x14\n\x0cmetric_value\x18\x03 \x01(\x01\":\n\x11\x41\x64\x64MetricResponse\x12\x17\n\x0fmetric_trail_id\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x03\x32\xc8\x01\n\x11MonitoringService\x12\xb2\x01\n\tAddMetric\x12\x33.yandex.cloud.loadtesting.agent.v1.AddMetricRequest\x1a\x34.yandex.cloud.loadtesting.agent.v1.AddMetricResponse\":\x82\xd3\xe4\x93\x02\x34\"//loadtesting/agent/v1/monitorings/reportMetrics:\x01*Bt\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.loadtesting.agent.v1.monitoring_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%yandex.cloud.api.loadtesting.agent.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/loadtesting/agent/v1;agent'
  _globals['_ADDMETRICREQUEST'].fields_by_name['compute_instance_id']._loaded_options = None
  _globals['_ADDMETRICREQUEST'].fields_by_name['compute_instance_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_ADDMETRICREQUEST'].fields_by_name['job_id']._loaded_options = None
  _globals['_ADDMETRICREQUEST'].fields_by_name['job_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_ADDMETRICREQUEST'].fields_by_name['chunks']._loaded_options = None
  _globals['_ADDMETRICREQUEST'].fields_by_name['chunks']._serialized_options = b'\202\3101\002>0'
  _globals['_ADDMETRICREQUEST'].fields_by_name['agent_instance_id']._loaded_options = None
  _globals['_ADDMETRICREQUEST'].fields_by_name['agent_instance_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_METRICCHUNK'].fields_by_name['data']._loaded_options = None
  _globals['_METRICCHUNK'].fields_by_name['data']._serialized_options = b'\202\3101\002>0'
  _globals['_METRICCHUNK'].fields_by_name['instance_host']._loaded_options = None
  _globals['_METRICCHUNK'].fields_by_name['instance_host']._serialized_options = b'\350\3071\001'
  _globals['_METRIC'].fields_by_name['metric_type']._loaded_options = None
  _globals['_METRIC'].fields_by_name['metric_type']._serialized_options = b'\350\3071\001'
  _globals['_METRIC'].fields_by_name['metric_name']._loaded_options = None
  _globals['_METRIC'].fields_by_name['metric_name']._serialized_options = b'\350\3071\001'
  _globals['_MONITORINGSERVICE'].methods_by_name['AddMetric']._loaded_options = None
  _globals['_MONITORINGSERVICE'].methods_by_name['AddMetric']._serialized_options = b'\202\323\344\223\0024\"//loadtesting/agent/v1/monitorings/reportMetrics:\001*'
  _globals['_ADDMETRICREQUEST']._serialized_start=159
  _globals['_ADDMETRICREQUEST']._serialized_end=361
  _globals['_METRICCHUNK']._serialized_start=364
  _globals['_METRICCHUNK']._serialized_end=507
  _globals['_METRIC']._serialized_start=509
  _globals['_METRIC']._serialized_end=593
  _globals['_ADDMETRICRESPONSE']._serialized_start=595
  _globals['_ADDMETRICRESPONSE']._serialized_end=653
  _globals['_MONITORINGSERVICE']._serialized_start=656
  _globals['_MONITORINGSERVICE']._serialized_end=856
# @@protoc_insertion_point(module_scope)
