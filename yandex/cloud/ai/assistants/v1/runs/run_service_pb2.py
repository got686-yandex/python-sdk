# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/assistants/v1/runs/run_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.common import common_pb2 as yandex_dot_cloud_dot_ai_dot_common_dot_common__pb2
from yandex.cloud.ai.assistants.v1 import common_pb2 as yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_common__pb2
from yandex.cloud.ai.assistants.v1.threads import message_pb2 as yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_threads_dot_message__pb2
from yandex.cloud.ai.assistants.v1.runs import run_pb2 as yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_runs_dot_run__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4yandex/cloud/ai/assistants/v1/runs/run_service.proto\x12\"yandex.cloud.ai.assistants.v1.runs\x1a#yandex/cloud/ai/common/common.proto\x1a*yandex/cloud/ai/assistants/v1/common.proto\x1a\x33yandex/cloud/ai/assistants/v1/threads/message.proto\x1a,yandex/cloud/ai/assistants/v1/runs/run.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xe0\x03\n\x10\x43reateRunRequest\x12\x1a\n\x0c\x61ssistant_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x17\n\tthread_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12P\n\x06labels\x18\x03 \x03(\x0b\x32@.yandex.cloud.ai.assistants.v1.runs.CreateRunRequest.LabelsEntry\x12O\n\x13\x61\x64\x64itional_messages\x18\x04 \x03(\x0b\x32\x32.yandex.cloud.ai.assistants.v1.threads.MessageData\x12`\n custom_prompt_truncation_options\x18\x05 \x01(\x0b\x32\x36.yandex.cloud.ai.assistants.v1.PromptTruncationOptions\x12S\n\x19\x63ustom_completion_options\x18\x06 \x01(\x0b\x32\x30.yandex.cloud.ai.assistants.v1.CompletionOptions\x12\x0e\n\x06stream\x18\x07 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"_\n\x10ListenRunRequest\x12\x14\n\x06run_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x35\n\x10\x65vents_start_idx\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"%\n\rGetRunRequest\x12\x14\n\x06run_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"4\n\x19GetLastRunByThreadRequest\x12\x17\n\tthread_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"Q\n\x0fListRunsRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"b\n\x10ListRunsResponse\x12\x35\n\x04runs\x18\x01 \x03(\x0b\x32\'.yandex.cloud.ai.assistants.v1.runs.Run\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"K\n\x0cStreamCursor\x12\x19\n\x11\x63urrent_event_idx\x18\x01 \x01(\x03\x12 \n\x18num_user_events_received\x18\x02 \x01(\x03\"\xd4\x03\n\x0bStreamEvent\x12M\n\nevent_type\x18\x01 \x01(\x0e\x32\x39.yandex.cloud.ai.assistants.v1.runs.StreamEvent.EventType\x12G\n\rstream_cursor\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.ai.assistants.v1.runs.StreamCursor\x12.\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1d.yandex.cloud.ai.common.ErrorH\x00\x12P\n\x0fpartial_message\x18\x04 \x01(\x0b\x32\x35.yandex.cloud.ai.assistants.v1.threads.MessageContentH\x00\x12K\n\x11\x63ompleted_message\x18\x05 \x01(\x0b\x32..yandex.cloud.ai.assistants.v1.threads.MessageH\x00\"Q\n\tEventType\x12\x1a\n\x16\x45VENT_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fPARTIAL_MESSAGE\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x08\n\x04\x44ONE\x10\x03\x42\x0b\n\tEventData2\xee\x05\n\nRunService\x12\x87\x01\n\x06\x43reate\x12\x34.yandex.cloud.ai.assistants.v1.runs.CreateRunRequest\x1a\'.yandex.cloud.ai.assistants.v1.runs.Run\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/assistants/v1/runs:\x01*\x12\x95\x01\n\x06Listen\x12\x34.yandex.cloud.ai.assistants.v1.runs.ListenRunRequest\x1a/.yandex.cloud.ai.assistants.v1.runs.StreamEvent\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/assistants/v1/runs/listen0\x01\x12\x87\x01\n\x03Get\x12\x31.yandex.cloud.ai.assistants.v1.runs.GetRunRequest\x1a\'.yandex.cloud.ai.assistants.v1.runs.Run\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/assistants/v1/runs/{run_id}\x12\xa2\x01\n\x0fGetLastByThread\x12=.yandex.cloud.ai.assistants.v1.runs.GetLastRunByThreadRequest\x1a\'.yandex.cloud.ai.assistants.v1.runs.Run\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/assistants/v1/runs:getByThread\x12\x8e\x01\n\x04List\x12\x33.yandex.cloud.ai.assistants.v1.runs.ListRunsRequest\x1a\x34.yandex.cloud.ai.assistants.v1.runs.ListRunsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/assistants/v1/runsBu\n&yandex.cloud.api.ai.assistants.v1.runsZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1/runs;runsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.assistants.v1.runs.run_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&yandex.cloud.api.ai.assistants.v1.runsZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/assistants/v1/runs;runs'
  _CREATERUNREQUEST_LABELSENTRY._options = None
  _CREATERUNREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATERUNREQUEST.fields_by_name['assistant_id']._options = None
  _CREATERUNREQUEST.fields_by_name['assistant_id']._serialized_options = b'\350\3071\001'
  _CREATERUNREQUEST.fields_by_name['thread_id']._options = None
  _CREATERUNREQUEST.fields_by_name['thread_id']._serialized_options = b'\350\3071\001'
  _LISTENRUNREQUEST.fields_by_name['run_id']._options = None
  _LISTENRUNREQUEST.fields_by_name['run_id']._serialized_options = b'\350\3071\001'
  _GETRUNREQUEST.fields_by_name['run_id']._options = None
  _GETRUNREQUEST.fields_by_name['run_id']._serialized_options = b'\350\3071\001'
  _GETLASTRUNBYTHREADREQUEST.fields_by_name['thread_id']._options = None
  _GETLASTRUNBYTHREADREQUEST.fields_by_name['thread_id']._serialized_options = b'\350\3071\001'
  _LISTRUNSREQUEST.fields_by_name['folder_id']._options = None
  _LISTRUNSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _RUNSERVICE.methods_by_name['Create']._options = None
  _RUNSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\030\"\023/assistants/v1/runs:\001*'
  _RUNSERVICE.methods_by_name['Listen']._options = None
  _RUNSERVICE.methods_by_name['Listen']._serialized_options = b'\202\323\344\223\002\034\022\032/assistants/v1/runs/listen'
  _RUNSERVICE.methods_by_name['Get']._options = None
  _RUNSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\036\022\034/assistants/v1/runs/{run_id}'
  _RUNSERVICE.methods_by_name['GetLastByThread']._options = None
  _RUNSERVICE.methods_by_name['GetLastByThread']._serialized_options = b'\202\323\344\223\002!\022\037/assistants/v1/runs:getByThread'
  _RUNSERVICE.methods_by_name['List']._options = None
  _RUNSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\025\022\023/assistants/v1/runs'
  _globals['_CREATERUNREQUEST']._serialized_start=366
  _globals['_CREATERUNREQUEST']._serialized_end=846
  _globals['_CREATERUNREQUEST_LABELSENTRY']._serialized_start=801
  _globals['_CREATERUNREQUEST_LABELSENTRY']._serialized_end=846
  _globals['_LISTENRUNREQUEST']._serialized_start=848
  _globals['_LISTENRUNREQUEST']._serialized_end=943
  _globals['_GETRUNREQUEST']._serialized_start=945
  _globals['_GETRUNREQUEST']._serialized_end=982
  _globals['_GETLASTRUNBYTHREADREQUEST']._serialized_start=984
  _globals['_GETLASTRUNBYTHREADREQUEST']._serialized_end=1036
  _globals['_LISTRUNSREQUEST']._serialized_start=1038
  _globals['_LISTRUNSREQUEST']._serialized_end=1119
  _globals['_LISTRUNSRESPONSE']._serialized_start=1121
  _globals['_LISTRUNSRESPONSE']._serialized_end=1219
  _globals['_STREAMCURSOR']._serialized_start=1221
  _globals['_STREAMCURSOR']._serialized_end=1296
  _globals['_STREAMEVENT']._serialized_start=1299
  _globals['_STREAMEVENT']._serialized_end=1767
  _globals['_STREAMEVENT_EVENTTYPE']._serialized_start=1673
  _globals['_STREAMEVENT_EVENTTYPE']._serialized_end=1754
  _globals['_RUNSERVICE']._serialized_start=1770
  _globals['_RUNSERVICE']._serialized_end=2520
# @@protoc_insertion_point(module_scope)