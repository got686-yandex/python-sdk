# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/serverless/workflows/v1/execution_service.proto
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
    'yandex/cloud/serverless/workflows/v1/execution_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.serverless.workflows.v1 import execution_pb2 as yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_execution__pb2
from yandex.cloud.serverless.workflows.v1 import history_entry_pb2 as yandex_dot_cloud_dot_serverless_dot_workflows_dot_v1_dot_history__entry__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<yandex/cloud/serverless/workflows/v1/execution_service.proto\x12$yandex.cloud.serverless.workflows.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x34yandex/cloud/serverless/workflows/v1/execution.proto\x1a\x38yandex/cloud/serverless/workflows/v1/history_entry.proto\x1a\x1dyandex/cloud/validation.proto\"}\n\x15StartExecutionRequest\x12\x19\n\x0bworkflow_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x43\n\x05input\x18\x03 \x01(\x0b\x32\x34.yandex.cloud.serverless.workflows.v1.ExecutionInputJ\x04\x08\x02\x10\x03\".\n\x16StartExecutionResponse\x12\x14\n\x0c\x65xecution_id\x18\x01 \x01(\t\"2\n\x14StopExecutionRequest\x12\x1a\n\x0c\x65xecution_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"-\n\x15StopExecutionResponse\x12\x14\n\x0c\x65xecution_id\x18\x01 \x01(\t\"7\n\x19TerminateExecutionRequest\x12\x1a\n\x0c\x65xecution_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"2\n\x1aTerminateExecutionResponse\x12\x14\n\x0c\x65xecution_id\x18\x01 \x01(\t\"1\n\x13GetExecutionRequest\x12\x1a\n\x0c\x65xecution_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"Z\n\x14GetExecutionResponse\x12\x42\n\texecution\x18\x01 \x01(\x0b\x32/.yandex.cloud.serverless.workflows.v1.Execution\"8\n\x1aGetExecutionHistoryRequest\x12\x1a\n\x0c\x65xecution_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\xb5\x01\n\x1bGetExecutionHistoryResponse\x12I\n\texecution\x18\x01 \x01(\x0b\x32\x36.yandex.cloud.serverless.workflows.v1.ExecutionPreview\x12K\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x32.yandex.cloud.serverless.workflows.v1.HistoryEntryB\x06\x82\xc8\x31\x02>0\"{\n\x15ListExecutionsRequest\x12\x19\n\x0bworkflow_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12#\n\tpage_size\x18\x02 \x01(\x03\x42\x10\xfa\xc7\x31\x0c\x30-2147483647\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\"}\n\x16ListExecutionsResponse\x12J\n\nexecutions\x18\x01 \x03(\x0b\x32\x36.yandex.cloud.serverless.workflows.v1.ExecutionPreview\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe3\x08\n\x10\x45xecutionService\x12\xac\x01\n\x05Start\x12;.yandex.cloud.serverless.workflows.v1.StartExecutionRequest\x1a<.yandex.cloud.serverless.workflows.v1.StartExecutionResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/workflows/v1/execution/start:\x01*\x12\xb4\x01\n\x04Stop\x12:.yandex.cloud.serverless.workflows.v1.StopExecutionRequest\x1a;.yandex.cloud.serverless.workflows.v1.StopExecutionResponse\"3\x82\xd3\xe4\x93\x02-\"+/workflows/v1/execution/{execution_id}/stop\x12\xc8\x01\n\tTerminate\x12?.yandex.cloud.serverless.workflows.v1.TerminateExecutionRequest\x1a@.yandex.cloud.serverless.workflows.v1.TerminateExecutionResponse\"8\x82\xd3\xe4\x93\x02\x32\"0/workflows/v1/execution/{execution_id}/terminate\x12\xac\x01\n\x03Get\x12\x39.yandex.cloud.serverless.workflows.v1.GetExecutionRequest\x1a:.yandex.cloud.serverless.workflows.v1.GetExecutionResponse\".\x82\xd3\xe4\x93\x02(\x12&/workflows/v1/execution/{execution_id}\x12\xc9\x01\n\nGetHistory\x12@.yandex.cloud.serverless.workflows.v1.GetExecutionHistoryRequest\x1a\x41.yandex.cloud.serverless.workflows.v1.GetExecutionHistoryResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./workflows/v1/execution/{execution_id}/history\x12\xa2\x01\n\x04List\x12;.yandex.cloud.serverless.workflows.v1.ListExecutionsRequest\x1a<.yandex.cloud.serverless.workflows.v1.ListExecutionsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/workflows/v1/executionB~\n(yandex.cloud.api.serverless.workflows.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/workflows/v1;workflowsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.workflows.v1.execution_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.serverless.workflows.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/workflows/v1;workflows'
  _globals['_STARTEXECUTIONREQUEST'].fields_by_name['workflow_id']._loaded_options = None
  _globals['_STARTEXECUTIONREQUEST'].fields_by_name['workflow_id']._serialized_options = b'\350\3071\001'
  _globals['_STOPEXECUTIONREQUEST'].fields_by_name['execution_id']._loaded_options = None
  _globals['_STOPEXECUTIONREQUEST'].fields_by_name['execution_id']._serialized_options = b'\350\3071\001'
  _globals['_TERMINATEEXECUTIONREQUEST'].fields_by_name['execution_id']._loaded_options = None
  _globals['_TERMINATEEXECUTIONREQUEST'].fields_by_name['execution_id']._serialized_options = b'\350\3071\001'
  _globals['_GETEXECUTIONREQUEST'].fields_by_name['execution_id']._loaded_options = None
  _globals['_GETEXECUTIONREQUEST'].fields_by_name['execution_id']._serialized_options = b'\350\3071\001'
  _globals['_GETEXECUTIONHISTORYREQUEST'].fields_by_name['execution_id']._loaded_options = None
  _globals['_GETEXECUTIONHISTORYREQUEST'].fields_by_name['execution_id']._serialized_options = b'\350\3071\001'
  _globals['_GETEXECUTIONHISTORYRESPONSE'].fields_by_name['entries']._loaded_options = None
  _globals['_GETEXECUTIONHISTORYRESPONSE'].fields_by_name['entries']._serialized_options = b'\202\3101\002>0'
  _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['workflow_id']._loaded_options = None
  _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['workflow_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTEXECUTIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0140-2147483647'
  _globals['_EXECUTIONSERVICE'].methods_by_name['Start']._loaded_options = None
  _globals['_EXECUTIONSERVICE'].methods_by_name['Start']._serialized_options = b'\202\323\344\223\002\"\"\035/workflows/v1/execution/start:\001*'
  _globals['_EXECUTIONSERVICE'].methods_by_name['Stop']._loaded_options = None
  _globals['_EXECUTIONSERVICE'].methods_by_name['Stop']._serialized_options = b'\202\323\344\223\002-\"+/workflows/v1/execution/{execution_id}/stop'
  _globals['_EXECUTIONSERVICE'].methods_by_name['Terminate']._loaded_options = None
  _globals['_EXECUTIONSERVICE'].methods_by_name['Terminate']._serialized_options = b'\202\323\344\223\0022\"0/workflows/v1/execution/{execution_id}/terminate'
  _globals['_EXECUTIONSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_EXECUTIONSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002(\022&/workflows/v1/execution/{execution_id}'
  _globals['_EXECUTIONSERVICE'].methods_by_name['GetHistory']._loaded_options = None
  _globals['_EXECUTIONSERVICE'].methods_by_name['GetHistory']._serialized_options = b'\202\323\344\223\0020\022./workflows/v1/execution/{execution_id}/history'
  _globals['_EXECUTIONSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_EXECUTIONSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\031\022\027/workflows/v1/execution'
  _globals['_STARTEXECUTIONREQUEST']._serialized_start=275
  _globals['_STARTEXECUTIONREQUEST']._serialized_end=400
  _globals['_STARTEXECUTIONRESPONSE']._serialized_start=402
  _globals['_STARTEXECUTIONRESPONSE']._serialized_end=448
  _globals['_STOPEXECUTIONREQUEST']._serialized_start=450
  _globals['_STOPEXECUTIONREQUEST']._serialized_end=500
  _globals['_STOPEXECUTIONRESPONSE']._serialized_start=502
  _globals['_STOPEXECUTIONRESPONSE']._serialized_end=547
  _globals['_TERMINATEEXECUTIONREQUEST']._serialized_start=549
  _globals['_TERMINATEEXECUTIONREQUEST']._serialized_end=604
  _globals['_TERMINATEEXECUTIONRESPONSE']._serialized_start=606
  _globals['_TERMINATEEXECUTIONRESPONSE']._serialized_end=656
  _globals['_GETEXECUTIONREQUEST']._serialized_start=658
  _globals['_GETEXECUTIONREQUEST']._serialized_end=707
  _globals['_GETEXECUTIONRESPONSE']._serialized_start=709
  _globals['_GETEXECUTIONRESPONSE']._serialized_end=799
  _globals['_GETEXECUTIONHISTORYREQUEST']._serialized_start=801
  _globals['_GETEXECUTIONHISTORYREQUEST']._serialized_end=857
  _globals['_GETEXECUTIONHISTORYRESPONSE']._serialized_start=860
  _globals['_GETEXECUTIONHISTORYRESPONSE']._serialized_end=1041
  _globals['_LISTEXECUTIONSREQUEST']._serialized_start=1043
  _globals['_LISTEXECUTIONSREQUEST']._serialized_end=1166
  _globals['_LISTEXECUTIONSRESPONSE']._serialized_start=1168
  _globals['_LISTEXECUTIONSRESPONSE']._serialized_end=1293
  _globals['_EXECUTIONSERVICE']._serialized_start=1296
  _globals['_EXECUTIONSERVICE']._serialized_end=2419
# @@protoc_insertion_point(module_scope)
