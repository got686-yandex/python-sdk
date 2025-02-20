# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/serverless/workflows/v1/workflow.proto
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
    'yandex/cloud/serverless/workflows/v1/workflow.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.logging.v1 import log_entry_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/serverless/workflows/v1/workflow.proto\x12$yandex.cloud.serverless.workflows.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\'yandex/cloud/logging/v1/log_entry.proto\x1a\x1dyandex/cloud/validation.proto\"\xec\x04\n\x08Workflow\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12R\n\rspecification\x18\x03 \x01(\x0b\x32;.yandex.cloud.serverless.workflows.v1.WorkflowSpecification\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12J\n\x06labels\x18\x07 \x03(\x0b\x32:.yandex.cloud.serverless.workflows.v1.Workflow.LabelsEntry\x12\x45\n\x06status\x18\x08 \x01(\x0e\x32\x35.yandex.cloud.serverless.workflows.v1.Workflow.Status\x12\x45\n\x0blog_options\x18\t \x01(\x0b\x32\x30.yandex.cloud.serverless.workflows.v1.LogOptions\x12\x12\n\nnetwork_id\x18\n \x01(\t\x12\x1a\n\x12service_account_id\x18\x0b \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"a\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\x12\t\n\x05\x45RROR\x10\x05\"\xc3\x03\n\x0fWorkflowPreview\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12Q\n\x06labels\x18\x06 \x03(\x0b\x32\x41.yandex.cloud.serverless.workflows.v1.WorkflowPreview.LabelsEntry\x12\x45\n\x06status\x18\x07 \x01(\x0e\x32\x35.yandex.cloud.serverless.workflows.v1.Workflow.Status\x12\x45\n\x0blog_options\x18\x08 \x01(\x0b\x32\x30.yandex.cloud.serverless.workflows.v1.LogOptions\x12\x12\n\nnetwork_id\x18\t \x01(\t\x12\x1a\n\x12service_account_id\x18\n \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\":\n\x15WorkflowSpecification\x12\x13\n\tspec_yaml\x18\x01 \x01(\tH\x00\x42\x0c\n\x04spec\x12\x04\xc0\xc1\x31\x01\"\x96\x01\n\nLogOptions\x12\x10\n\x08\x64isabled\x18\x01 \x01(\x08\x12\x16\n\x0clog_group_id\x18\x02 \x01(\tH\x00\x12\x13\n\tfolder_id\x18\x03 \x01(\tH\x00\x12:\n\tmin_level\x18\x04 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.LevelB\r\n\x0b\x64\x65stinationB~\n(yandex.cloud.api.serverless.workflows.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/workflows/v1;workflowsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.workflows.v1.workflow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(yandex.cloud.api.serverless.workflows.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/workflows/v1;workflows'
  _globals['_WORKFLOW_LABELSENTRY']._loaded_options = None
  _globals['_WORKFLOW_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_WORKFLOWPREVIEW_LABELSENTRY']._loaded_options = None
  _globals['_WORKFLOWPREVIEW_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_WORKFLOWSPECIFICATION'].oneofs_by_name['spec']._loaded_options = None
  _globals['_WORKFLOWSPECIFICATION'].oneofs_by_name['spec']._serialized_options = b'\300\3011\001'
  _globals['_WORKFLOW']._serialized_start=199
  _globals['_WORKFLOW']._serialized_end=819
  _globals['_WORKFLOW_LABELSENTRY']._serialized_start=675
  _globals['_WORKFLOW_LABELSENTRY']._serialized_end=720
  _globals['_WORKFLOW_STATUS']._serialized_start=722
  _globals['_WORKFLOW_STATUS']._serialized_end=819
  _globals['_WORKFLOWPREVIEW']._serialized_start=822
  _globals['_WORKFLOWPREVIEW']._serialized_end=1273
  _globals['_WORKFLOWPREVIEW_LABELSENTRY']._serialized_start=675
  _globals['_WORKFLOWPREVIEW_LABELSENTRY']._serialized_end=720
  _globals['_WORKFLOWSPECIFICATION']._serialized_start=1275
  _globals['_WORKFLOWSPECIFICATION']._serialized_end=1333
  _globals['_LOGOPTIONS']._serialized_start=1336
  _globals['_LOGOPTIONS']._serialized_end=1486
# @@protoc_insertion_point(module_scope)
