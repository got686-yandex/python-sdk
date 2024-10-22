# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/functions/v1/function_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.serverless.functions.v1 import function_pb2 as yandex_dot_cloud_dot_serverless_dot_functions_dot_v1_dot_function__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;yandex/cloud/serverless/functions/v1/function_service.proto\x12$yandex.cloud.serverless.functions.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x33yandex/cloud/serverless/functions/v1/function.proto\x1a\x1dyandex/cloud/validation.proto\"/\n\x12GetFunctionRequest\x12\x19\n\x0b\x66unction_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\">\n\x19GetFunctionVersionRequest\x12!\n\x13\x66unction_version_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"h\n\x1eGetFunctionVersionByTagRequest\x12\x19\n\x0b\x66unction_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12+\n\x03tag\x18\x02 \x01(\tB\x1e\xf2\xc7\x31\x1a[a-z][-_0-9a-z]*|[$]latest\"f\n\x14ListFunctionsRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\"s\n\x15ListFunctionsResponse\x12\x41\n\tfunctions\x18\x01 \x03(\x0b\x32..yandex.cloud.serverless.functions.v1.Function\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xcf\x02\n\x15\x43reateFunctionRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x9c\x01\n\x06labels\x18\x04 \x03(\x0b\x32G.yandex.cloud.serverless.functions.v1.CreateFunctionRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\x16\x43reateFunctionMetadata\x12\x13\n\x0b\x66unction_id\x18\x01 \x01(\t\"\x82\x03\n\x15UpdateFunctionRequest\x12\x19\n\x0b\x66unction_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x9c\x01\n\x06labels\x18\x05 \x03(\x0b\x32G.yandex.cloud.serverless.functions.v1.UpdateFunctionRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\x16UpdateFunctionMetadata\x12\x13\n\x0b\x66unction_id\x18\x01 \x01(\t\"2\n\x15\x44\x65leteFunctionRequest\x12\x19\n\x0b\x66unction_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"-\n\x16\x44\x65leteFunctionMetadata\x12\x13\n\x0b\x66unction_id\x18\x01 \x01(\t\"V\n\x1c\x44\x65leteFunctionVersionRequest\x12!\n\x13\x66unction_version_id\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\r\n\x05\x66orce\x18\x03 \x01(\x08J\x04\x08\x01\x10\x02\"B\n\x1d\x44\x65leteFunctionVersionMetadata\x12\x1b\n\x13\x66unction_version_id\x18\x02 \x01(\tJ\x04\x08\x01\x10\x02\"\x15\n\x13ListRuntimesRequest\"(\n\x14ListRuntimesResponse\x12\x10\n\x08runtimes\x18\x01 \x03(\t\"\xb0\x01\n\x1cListFunctionsVersionsRequest\x12\x13\n\tfolder_id\x18\x01 \x01(\tH\x00\x12\x15\n\x0b\x66unction_id\x18\x02 \x01(\tH\x00\x12\x1d\n\tpage_size\x18\x03 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x05 \x01(\tB\n\x8a\xc8\x31\x06<=1000B\n\n\x02id\x12\x04\xc0\xc1\x31\x01\"y\n\x1dListFunctionsVersionsResponse\x12?\n\x08versions\x18\x01 \x03(\x0b\x32-.yandex.cloud.serverless.functions.v1.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x94\x01\n\x1dListFunctionOperationsRequest\x12\x19\n\x0b\x66unction_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"p\n\x1eListFunctionOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xf1\n\n\x1c\x43reateFunctionVersionRequest\x12\x19\n\x0b\x66unction_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x15\n\x07runtime\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05\x30-256\x12\x18\n\nentrypoint\x18\x04 \x01(\tB\x04\xe8\xc7\x31\x01\x12H\n\tresources\x18\x05 \x01(\x0b\x32/.yandex.cloud.serverless.functions.v1.ResourcesB\x04\xe8\xc7\x31\x01\x12\x46\n\x11\x65xecution_timeout\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationB\x10\xe8\xc7\x31\x01\xfa\xc7\x31\x08\x30s-3600s\x12\x1a\n\x12service_account_id\x18\x07 \x01(\t\x12@\n\x07package\x18\t \x01(\x0b\x32-.yandex.cloud.serverless.functions.v1.PackageH\x00\x12!\n\x07\x63ontent\x18\n \x01(\x0c\x42\x0e\x8a\xc8\x31\n<=52428800H\x00\x12\x14\n\nversion_id\x18\x0b \x01(\tH\x00\x12\x8f\x01\n\x0b\x65nvironment\x18\x0c \x03(\x0b\x32S.yandex.cloud.serverless.functions.v1.CreateFunctionVersionRequest.EnvironmentEntryB%\x8a\xc8\x31\x06<=4096\xb2\xc8\x31\x17\x12\x15[a-zA-Z][a-zA-Z0-9_]*\x12!\n\x03tag\x18\r \x03(\tB\x14\xf2\xc7\x31\x10[a-z][-_0-9a-z]*\x12H\n\x0c\x63onnectivity\x18\x11 \x01(\x0b\x32\x32.yandex.cloud.serverless.functions.v1.Connectivity\x12|\n\x16named_service_accounts\x18\x0f \x03(\x0b\x32\\.yandex.cloud.serverless.functions.v1.CreateFunctionVersionRequest.NamedServiceAccountsEntry\x12=\n\x07secrets\x18\x12 \x03(\x0b\x32,.yandex.cloud.serverless.functions.v1.Secret\x12\x45\n\x0blog_options\x18\x13 \x01(\x0b\x32\x30.yandex.cloud.serverless.functions.v1.LogOptions\x12J\n\x0estorage_mounts\x18\x14 \x03(\x0b\x32\x32.yandex.cloud.serverless.functions.v1.StorageMount\x12\\\n\x17\x61sync_invocation_config\x18\x16 \x01(\x0b\x32;.yandex.cloud.serverless.functions.v1.AsyncInvocationConfig\x12\x12\n\ntmpfs_size\x18\x17 \x01(\x03\x12\x1d\n\x0b\x63oncurrency\x18\x18 \x01(\x03\x42\x08\xfa\xc7\x31\x04\x30-16\x12;\n\x06mounts\x18\x19 \x03(\x0b\x32+.yandex.cloud.serverless.functions.v1.Mount\x1a\x32\n\x10\x45nvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a;\n\x19NamedServiceAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x16\n\x0epackage_source\x12\x04\xc0\xc1\x31\x01J\x04\x08\x0e\x10\x0fJ\x04\x08\x10\x10\x11J\x04\x08\x15\x10\x16J\x04\x08\x08\x10\t\"<\n\x1d\x43reateFunctionVersionMetadata\x12\x1b\n\x13\x66unction_version_id\x18\x01 \x01(\t\"]\n\x15SetFunctionTagRequest\x12!\n\x13\x66unction_version_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12!\n\x03tag\x18\x02 \x01(\tB\x14\xf2\xc7\x31\x10[a-z][-_0-9a-z]*\"`\n\x18RemoveFunctionTagRequest\x12!\n\x13\x66unction_version_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12!\n\x03tag\x18\x02 \x01(\tB\x14\xf2\xc7\x31\x10[a-z][-_0-9a-z]*\"5\n\x16SetFunctionTagMetadata\x12\x1b\n\x13\x66unction_version_id\x18\x01 \x01(\t\"8\n\x19RemoveFunctionTagMetadata\x12\x1b\n\x13\x66unction_version_id\x18\x01 \x01(\t\"\xc1\x01\n\x1dListFunctionTagHistoryRequest\x12\x19\n\x0b\x66unction_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12+\n\x03tag\x18\x02 \x01(\tB\x1e\xf2\xc7\x31\x1a[a-z][-_0-9a-z]*|[$]latest\x12\x1d\n\tpage_size\x18\x03 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x05 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"\x80\x03\n\x1eListFunctionTagHistoryResponse\x12\x82\x01\n\x1b\x66unction_tag_history_record\x18\x01 \x03(\x0b\x32].yandex.cloud.serverless.functions.v1.ListFunctionTagHistoryResponse.FunctionTagHistoryRecord\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x1a\xbf\x01\n\x18\x46unctionTagHistoryRecord\x12\x13\n\x0b\x66unction_id\x18\x01 \x01(\t\x12\x1b\n\x13\x66unction_version_id\x18\x03 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x32\n\x0e\x65\x66\x66\x65\x63tive_from\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x65\x66\x66\x65\x63tive_to\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"u\n\x1aListScalingPoliciesRequest\x12\x19\n\x0b\x66unction_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x85\x01\n\x1bListScalingPoliciesResponse\x12M\n\x10scaling_policies\x18\x01 \x03(\x0b\x32\x33.yandex.cloud.serverless.functions.v1.ScalingPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xef\x01\n\x17SetScalingPolicyRequest\x12\x19\n\x0b\x66unction_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x03tag\x18\x02 \x01(\tB\"\xe8\xc7\x31\x01\xf2\xc7\x31\x1a[a-z][-_0-9a-z]*|[$]latest\x12/\n\x1bprovisioned_instances_count\x18\x04 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12(\n\x14zone_instances_limit\x18\x05 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\'\n\x13zone_requests_limit\x18\x06 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000J\x04\x08\x03\x10\x04\"/\n\x18SetScalingPolicyMetadata\x12\x13\n\x0b\x66unction_id\x18\x01 \x01(\t\"h\n\x1aRemoveScalingPolicyRequest\x12\x19\n\x0b\x66unction_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x03tag\x18\x02 \x01(\tB\"\xe8\xc7\x31\x01\xf2\xc7\x31\x1a[a-z][-_0-9a-z]*|[$]latest\"2\n\x1bRemoveScalingPolicyMetadata\x12\x13\n\x0b\x66unction_id\x18\x01 \x01(\t2\xc4!\n\x0f\x46unctionService\x12\x9e\x01\n\x03Get\x12\x38.yandex.cloud.serverless.functions.v1.GetFunctionRequest\x1a..yandex.cloud.serverless.functions.v1.Function\"-\x82\xd3\xe4\x93\x02\'\x12%/functions/v1/functions/{function_id}\x12\xa0\x01\n\x04List\x12:.yandex.cloud.serverless.functions.v1.ListFunctionsRequest\x1a;.yandex.cloud.serverless.functions.v1.ListFunctionsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/functions/v1/functions\x12\xb2\x01\n\x06\x43reate\x12;.yandex.cloud.serverless.functions.v1.CreateFunctionRequest\x1a!.yandex.cloud.operation.Operation\"H\xb2\xd2*\"\n\x16\x43reateFunctionMetadata\x12\x08\x46unction\x82\xd3\xe4\x93\x02\x1c\"\x17/functions/v1/functions:\x01*\x12\xc0\x01\n\x06Update\x12;.yandex.cloud.serverless.functions.v1.UpdateFunctionRequest\x1a!.yandex.cloud.operation.Operation\"V\xb2\xd2*\"\n\x16UpdateFunctionMetadata\x12\x08\x46unction\x82\xd3\xe4\x93\x02*2%/functions/v1/functions/{function_id}:\x01*\x12\xca\x01\n\x06\x44\x65lete\x12;.yandex.cloud.serverless.functions.v1.DeleteFunctionRequest\x1a!.yandex.cloud.operation.Operation\"`\xb2\xd2*/\n\x16\x44\x65leteFunctionMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\'*%/functions/v1/functions/{function_id}\x12\xb2\x01\n\nGetVersion\x12?.yandex.cloud.serverless.functions.v1.GetFunctionVersionRequest\x1a-.yandex.cloud.serverless.functions.v1.Version\"4\x82\xd3\xe4\x93\x02.\x12,/functions/v1/versions/{function_version_id}\x12\xac\x01\n\x0fGetVersionByTag\x12\x44.yandex.cloud.serverless.functions.v1.GetFunctionVersionByTagRequest\x1a-.yandex.cloud.serverless.functions.v1.Version\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/functions/v1/versions:byTag\x12\xb7\x01\n\x0cListVersions\x12\x42.yandex.cloud.serverless.functions.v1.ListFunctionsVersionsRequest\x1a\x43.yandex.cloud.serverless.functions.v1.ListFunctionsVersionsResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/functions/v1/versions\x12\xe6\x01\n\rDeleteVersion\x12\x42.yandex.cloud.serverless.functions.v1.DeleteFunctionVersionRequest\x1a!.yandex.cloud.operation.Operation\"n\xb2\xd2*6\n\x1d\x44\x65leteFunctionVersionMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02.*,/functions/v1/versions/{function_version_id}\x12\xcd\x01\n\x06SetTag\x12;.yandex.cloud.serverless.functions.v1.SetFunctionTagRequest\x1a!.yandex.cloud.operation.Operation\"c\xb2\xd2*!\n\x16SetFunctionTagMetadata\x12\x07Version\x82\xd3\xe4\x93\x02\x38\"3/functions/v1/versions/{function_version_id}:setTag:\x01*\x12\xd9\x01\n\tRemoveTag\x12>.yandex.cloud.serverless.functions.v1.RemoveFunctionTagRequest\x1a!.yandex.cloud.operation.Operation\"i\xb2\xd2*$\n\x19RemoveFunctionTagMetadata\x12\x07Version\x82\xd3\xe4\x93\x02;\"6/functions/v1/versions/{function_version_id}:removeTag:\x01*\x12\xd5\x01\n\x0eListTagHistory\x12\x43.yandex.cloud.serverless.functions.v1.ListFunctionTagHistoryRequest\x1a\x44.yandex.cloud.serverless.functions.v1.ListFunctionTagHistoryResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/functions/v1/functions/{function_id}:tagHistory\x12\xc5\x01\n\rCreateVersion\x12\x42.yandex.cloud.serverless.functions.v1.CreateFunctionVersionRequest\x1a!.yandex.cloud.operation.Operation\"M\xb2\xd2*(\n\x1d\x43reateFunctionVersionMetadata\x12\x07Version\x82\xd3\xe4\x93\x02\x1b\"\x16/functions/v1/versions:\x01*\x12\xa5\x01\n\x0cListRuntimes\x12\x39.yandex.cloud.serverless.functions.v1.ListRuntimesRequest\x1a:.yandex.cloud.serverless.functions.v1.ListRuntimesResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/functions/v1/runtimes\x12\xd5\x01\n\x0eListOperations\x12\x43.yandex.cloud.serverless.functions.v1.ListFunctionOperationsRequest\x1a\x44.yandex.cloud.serverless.functions.v1.ListFunctionOperationsResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/functions/v1/functions/{function_id}/operations\x12\xb7\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/functions/v1/functions/{resource_id}:listAccessBindings\x12\xe6\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x7f\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02<\"7/functions/v1/functions/{resource_id}:setAccessBindings:\x01*\x12\xf3\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x85\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02?\":/functions/v1/functions/{resource_id}:updateAccessBindings:\x01*\x12\xd9\x01\n\x13ListScalingPolicies\x12@.yandex.cloud.serverless.functions.v1.ListScalingPoliciesRequest\x1a\x41.yandex.cloud.serverless.functions.v1.ListScalingPoliciesResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/functions/v1/functions/{function_id}/scalingPolicies\x12\xe4\x01\n\x10SetScalingPolicy\x12=.yandex.cloud.serverless.functions.v1.SetScalingPolicyRequest\x1a!.yandex.cloud.operation.Operation\"n\xb2\xd2*)\n\x18SetScalingPolicyMetadata\x12\rScalingPolicy\x82\xd3\xe4\x93\x02;\"6/functions/v1/functions/{function_id}:setScalingPolicy:\x01*\x12\xf8\x01\n\x13RemoveScalingPolicy\x12@.yandex.cloud.serverless.functions.v1.RemoveScalingPolicyRequest\x1a!.yandex.cloud.operation.Operation\"|\xb2\xd2*4\n\x1bRemoveScalingPolicyMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02>\"9/functions/v1/functions/{function_id}:removeScalingPolicy:\x01*B~\n(yandex.cloud.api.serverless.functions.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/functions/v1;functionsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.functions.v1.function_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(yandex.cloud.api.serverless.functions.v1ZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/functions/v1;functions'
  _GETFUNCTIONREQUEST.fields_by_name['function_id']._options = None
  _GETFUNCTIONREQUEST.fields_by_name['function_id']._serialized_options = b'\350\3071\001'
  _GETFUNCTIONVERSIONREQUEST.fields_by_name['function_version_id']._options = None
  _GETFUNCTIONVERSIONREQUEST.fields_by_name['function_version_id']._serialized_options = b'\350\3071\001'
  _GETFUNCTIONVERSIONBYTAGREQUEST.fields_by_name['function_id']._options = None
  _GETFUNCTIONVERSIONBYTAGREQUEST.fields_by_name['function_id']._serialized_options = b'\350\3071\001'
  _GETFUNCTIONVERSIONBYTAGREQUEST.fields_by_name['tag']._options = None
  _GETFUNCTIONVERSIONBYTAGREQUEST.fields_by_name['tag']._serialized_options = b'\362\3071\032[a-z][-_0-9a-z]*|[$]latest'
  _LISTFUNCTIONSREQUEST.fields_by_name['folder_id']._options = None
  _LISTFUNCTIONSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATEFUNCTIONREQUEST_LABELSENTRY._options = None
  _CREATEFUNCTIONREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEFUNCTIONREQUEST.fields_by_name['folder_id']._options = None
  _CREATEFUNCTIONREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATEFUNCTIONREQUEST.fields_by_name['name']._options = None
  _CREATEFUNCTIONREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _CREATEFUNCTIONREQUEST.fields_by_name['description']._options = None
  _CREATEFUNCTIONREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATEFUNCTIONREQUEST.fields_by_name['labels']._options = None
  _CREATEFUNCTIONREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _UPDATEFUNCTIONREQUEST_LABELSENTRY._options = None
  _UPDATEFUNCTIONREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEFUNCTIONREQUEST.fields_by_name['function_id']._options = None
  _UPDATEFUNCTIONREQUEST.fields_by_name['function_id']._serialized_options = b'\350\3071\001'
  _UPDATEFUNCTIONREQUEST.fields_by_name['name']._options = None
  _UPDATEFUNCTIONREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _UPDATEFUNCTIONREQUEST.fields_by_name['description']._options = None
  _UPDATEFUNCTIONREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATEFUNCTIONREQUEST.fields_by_name['labels']._options = None
  _UPDATEFUNCTIONREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _DELETEFUNCTIONREQUEST.fields_by_name['function_id']._options = None
  _DELETEFUNCTIONREQUEST.fields_by_name['function_id']._serialized_options = b'\350\3071\001'
  _DELETEFUNCTIONVERSIONREQUEST.fields_by_name['function_version_id']._options = None
  _DELETEFUNCTIONVERSIONREQUEST.fields_by_name['function_version_id']._serialized_options = b'\350\3071\001'
  _LISTFUNCTIONSVERSIONSREQUEST.oneofs_by_name['id']._options = None
  _LISTFUNCTIONSVERSIONSREQUEST.oneofs_by_name['id']._serialized_options = b'\300\3011\001'
  _LISTFUNCTIONSVERSIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTFUNCTIONSVERSIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTFUNCTIONSVERSIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTFUNCTIONSVERSIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTFUNCTIONSVERSIONSREQUEST.fields_by_name['filter']._options = None
  _LISTFUNCTIONSVERSIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTFUNCTIONOPERATIONSREQUEST.fields_by_name['function_id']._options = None
  _LISTFUNCTIONOPERATIONSREQUEST.fields_by_name['function_id']._serialized_options = b'\350\3071\001'
  _LISTFUNCTIONOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTFUNCTIONOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTFUNCTIONOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTFUNCTIONOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTFUNCTIONOPERATIONSREQUEST.fields_by_name['filter']._options = None
  _LISTFUNCTIONOPERATIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _CREATEFUNCTIONVERSIONREQUEST_ENVIRONMENTENTRY._options = None
  _CREATEFUNCTIONVERSIONREQUEST_ENVIRONMENTENTRY._serialized_options = b'8\001'
  _CREATEFUNCTIONVERSIONREQUEST_NAMEDSERVICEACCOUNTSENTRY._options = None
  _CREATEFUNCTIONVERSIONREQUEST_NAMEDSERVICEACCOUNTSENTRY._serialized_options = b'8\001'
  _CREATEFUNCTIONVERSIONREQUEST.oneofs_by_name['package_source']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.oneofs_by_name['package_source']._serialized_options = b'\300\3011\001'
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['function_id']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['function_id']._serialized_options = b'\350\3071\001'
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['runtime']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['runtime']._serialized_options = b'\350\3071\001'
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['description']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\0050-256'
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['entrypoint']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['entrypoint']._serialized_options = b'\350\3071\001'
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['resources']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['resources']._serialized_options = b'\350\3071\001'
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['execution_timeout']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['execution_timeout']._serialized_options = b'\350\3071\001\372\3071\0100s-3600s'
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['content']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['content']._serialized_options = b'\212\3101\n<=52428800'
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['environment']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['environment']._serialized_options = b'\212\3101\006<=4096\262\3101\027\022\025[a-zA-Z][a-zA-Z0-9_]*'
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['tag']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['tag']._serialized_options = b'\362\3071\020[a-z][-_0-9a-z]*'
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['concurrency']._options = None
  _CREATEFUNCTIONVERSIONREQUEST.fields_by_name['concurrency']._serialized_options = b'\372\3071\0040-16'
  _SETFUNCTIONTAGREQUEST.fields_by_name['function_version_id']._options = None
  _SETFUNCTIONTAGREQUEST.fields_by_name['function_version_id']._serialized_options = b'\350\3071\001'
  _SETFUNCTIONTAGREQUEST.fields_by_name['tag']._options = None
  _SETFUNCTIONTAGREQUEST.fields_by_name['tag']._serialized_options = b'\362\3071\020[a-z][-_0-9a-z]*'
  _REMOVEFUNCTIONTAGREQUEST.fields_by_name['function_version_id']._options = None
  _REMOVEFUNCTIONTAGREQUEST.fields_by_name['function_version_id']._serialized_options = b'\350\3071\001'
  _REMOVEFUNCTIONTAGREQUEST.fields_by_name['tag']._options = None
  _REMOVEFUNCTIONTAGREQUEST.fields_by_name['tag']._serialized_options = b'\362\3071\020[a-z][-_0-9a-z]*'
  _LISTFUNCTIONTAGHISTORYREQUEST.fields_by_name['function_id']._options = None
  _LISTFUNCTIONTAGHISTORYREQUEST.fields_by_name['function_id']._serialized_options = b'\350\3071\001'
  _LISTFUNCTIONTAGHISTORYREQUEST.fields_by_name['tag']._options = None
  _LISTFUNCTIONTAGHISTORYREQUEST.fields_by_name['tag']._serialized_options = b'\362\3071\032[a-z][-_0-9a-z]*|[$]latest'
  _LISTFUNCTIONTAGHISTORYREQUEST.fields_by_name['page_size']._options = None
  _LISTFUNCTIONTAGHISTORYREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTFUNCTIONTAGHISTORYREQUEST.fields_by_name['page_token']._options = None
  _LISTFUNCTIONTAGHISTORYREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTFUNCTIONTAGHISTORYREQUEST.fields_by_name['filter']._options = None
  _LISTFUNCTIONTAGHISTORYREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTSCALINGPOLICIESREQUEST.fields_by_name['function_id']._options = None
  _LISTSCALINGPOLICIESREQUEST.fields_by_name['function_id']._serialized_options = b'\350\3071\001'
  _LISTSCALINGPOLICIESREQUEST.fields_by_name['page_size']._options = None
  _LISTSCALINGPOLICIESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTSCALINGPOLICIESREQUEST.fields_by_name['page_token']._options = None
  _LISTSCALINGPOLICIESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _SETSCALINGPOLICYREQUEST.fields_by_name['function_id']._options = None
  _SETSCALINGPOLICYREQUEST.fields_by_name['function_id']._serialized_options = b'\350\3071\001'
  _SETSCALINGPOLICYREQUEST.fields_by_name['tag']._options = None
  _SETSCALINGPOLICYREQUEST.fields_by_name['tag']._serialized_options = b'\350\3071\001\362\3071\032[a-z][-_0-9a-z]*|[$]latest'
  _SETSCALINGPOLICYREQUEST.fields_by_name['provisioned_instances_count']._options = None
  _SETSCALINGPOLICYREQUEST.fields_by_name['provisioned_instances_count']._serialized_options = b'\372\3071\0060-1000'
  _SETSCALINGPOLICYREQUEST.fields_by_name['zone_instances_limit']._options = None
  _SETSCALINGPOLICYREQUEST.fields_by_name['zone_instances_limit']._serialized_options = b'\372\3071\0060-1000'
  _SETSCALINGPOLICYREQUEST.fields_by_name['zone_requests_limit']._options = None
  _SETSCALINGPOLICYREQUEST.fields_by_name['zone_requests_limit']._serialized_options = b'\372\3071\0060-1000'
  _REMOVESCALINGPOLICYREQUEST.fields_by_name['function_id']._options = None
  _REMOVESCALINGPOLICYREQUEST.fields_by_name['function_id']._serialized_options = b'\350\3071\001'
  _REMOVESCALINGPOLICYREQUEST.fields_by_name['tag']._options = None
  _REMOVESCALINGPOLICYREQUEST.fields_by_name['tag']._serialized_options = b'\350\3071\001\362\3071\032[a-z][-_0-9a-z]*|[$]latest'
  _FUNCTIONSERVICE.methods_by_name['Get']._options = None
  _FUNCTIONSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\'\022%/functions/v1/functions/{function_id}'
  _FUNCTIONSERVICE.methods_by_name['List']._options = None
  _FUNCTIONSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\031\022\027/functions/v1/functions'
  _FUNCTIONSERVICE.methods_by_name['Create']._options = None
  _FUNCTIONSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*\"\n\026CreateFunctionMetadata\022\010Function\202\323\344\223\002\034\"\027/functions/v1/functions:\001*'
  _FUNCTIONSERVICE.methods_by_name['Update']._options = None
  _FUNCTIONSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*\"\n\026UpdateFunctionMetadata\022\010Function\202\323\344\223\002*2%/functions/v1/functions/{function_id}:\001*'
  _FUNCTIONSERVICE.methods_by_name['Delete']._options = None
  _FUNCTIONSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*/\n\026DeleteFunctionMetadata\022\025google.protobuf.Empty\202\323\344\223\002\'*%/functions/v1/functions/{function_id}'
  _FUNCTIONSERVICE.methods_by_name['GetVersion']._options = None
  _FUNCTIONSERVICE.methods_by_name['GetVersion']._serialized_options = b'\202\323\344\223\002.\022,/functions/v1/versions/{function_version_id}'
  _FUNCTIONSERVICE.methods_by_name['GetVersionByTag']._options = None
  _FUNCTIONSERVICE.methods_by_name['GetVersionByTag']._serialized_options = b'\202\323\344\223\002\036\022\034/functions/v1/versions:byTag'
  _FUNCTIONSERVICE.methods_by_name['ListVersions']._options = None
  _FUNCTIONSERVICE.methods_by_name['ListVersions']._serialized_options = b'\202\323\344\223\002\030\022\026/functions/v1/versions'
  _FUNCTIONSERVICE.methods_by_name['DeleteVersion']._options = None
  _FUNCTIONSERVICE.methods_by_name['DeleteVersion']._serialized_options = b'\262\322*6\n\035DeleteFunctionVersionMetadata\022\025google.protobuf.Empty\202\323\344\223\002.*,/functions/v1/versions/{function_version_id}'
  _FUNCTIONSERVICE.methods_by_name['SetTag']._options = None
  _FUNCTIONSERVICE.methods_by_name['SetTag']._serialized_options = b'\262\322*!\n\026SetFunctionTagMetadata\022\007Version\202\323\344\223\0028\"3/functions/v1/versions/{function_version_id}:setTag:\001*'
  _FUNCTIONSERVICE.methods_by_name['RemoveTag']._options = None
  _FUNCTIONSERVICE.methods_by_name['RemoveTag']._serialized_options = b'\262\322*$\n\031RemoveFunctionTagMetadata\022\007Version\202\323\344\223\002;\"6/functions/v1/versions/{function_version_id}:removeTag:\001*'
  _FUNCTIONSERVICE.methods_by_name['ListTagHistory']._options = None
  _FUNCTIONSERVICE.methods_by_name['ListTagHistory']._serialized_options = b'\202\323\344\223\0022\0220/functions/v1/functions/{function_id}:tagHistory'
  _FUNCTIONSERVICE.methods_by_name['CreateVersion']._options = None
  _FUNCTIONSERVICE.methods_by_name['CreateVersion']._serialized_options = b'\262\322*(\n\035CreateFunctionVersionMetadata\022\007Version\202\323\344\223\002\033\"\026/functions/v1/versions:\001*'
  _FUNCTIONSERVICE.methods_by_name['ListRuntimes']._options = None
  _FUNCTIONSERVICE.methods_by_name['ListRuntimes']._serialized_options = b'\202\323\344\223\002\030\022\026/functions/v1/runtimes'
  _FUNCTIONSERVICE.methods_by_name['ListOperations']._options = None
  _FUNCTIONSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0022\0220/functions/v1/functions/{function_id}/operations'
  _FUNCTIONSERVICE.methods_by_name['ListAccessBindings']._options = None
  _FUNCTIONSERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002:\0228/functions/v1/functions/{resource_id}:listAccessBindings'
  _FUNCTIONSERVICE.methods_by_name['SetAccessBindings']._options = None
  _FUNCTIONSERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002<\"7/functions/v1/functions/{resource_id}:setAccessBindings:\001*'
  _FUNCTIONSERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _FUNCTIONSERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002?\":/functions/v1/functions/{resource_id}:updateAccessBindings:\001*'
  _FUNCTIONSERVICE.methods_by_name['ListScalingPolicies']._options = None
  _FUNCTIONSERVICE.methods_by_name['ListScalingPolicies']._serialized_options = b'\202\323\344\223\0027\0225/functions/v1/functions/{function_id}/scalingPolicies'
  _FUNCTIONSERVICE.methods_by_name['SetScalingPolicy']._options = None
  _FUNCTIONSERVICE.methods_by_name['SetScalingPolicy']._serialized_options = b'\262\322*)\n\030SetScalingPolicyMetadata\022\rScalingPolicy\202\323\344\223\002;\"6/functions/v1/functions/{function_id}:setScalingPolicy:\001*'
  _FUNCTIONSERVICE.methods_by_name['RemoveScalingPolicy']._options = None
  _FUNCTIONSERVICE.methods_by_name['RemoveScalingPolicy']._serialized_options = b'\262\322*4\n\033RemoveScalingPolicyMetadata\022\025google.protobuf.Empty\202\323\344\223\002>\"9/functions/v1/functions/{function_id}:removeScalingPolicy:\001*'
  _globals['_GETFUNCTIONREQUEST']._serialized_start=422
  _globals['_GETFUNCTIONREQUEST']._serialized_end=469
  _globals['_GETFUNCTIONVERSIONREQUEST']._serialized_start=471
  _globals['_GETFUNCTIONVERSIONREQUEST']._serialized_end=533
  _globals['_GETFUNCTIONVERSIONBYTAGREQUEST']._serialized_start=535
  _globals['_GETFUNCTIONVERSIONBYTAGREQUEST']._serialized_end=639
  _globals['_LISTFUNCTIONSREQUEST']._serialized_start=641
  _globals['_LISTFUNCTIONSREQUEST']._serialized_end=743
  _globals['_LISTFUNCTIONSRESPONSE']._serialized_start=745
  _globals['_LISTFUNCTIONSRESPONSE']._serialized_end=860
  _globals['_CREATEFUNCTIONREQUEST']._serialized_start=863
  _globals['_CREATEFUNCTIONREQUEST']._serialized_end=1198
  _globals['_CREATEFUNCTIONREQUEST_LABELSENTRY']._serialized_start=1153
  _globals['_CREATEFUNCTIONREQUEST_LABELSENTRY']._serialized_end=1198
  _globals['_CREATEFUNCTIONMETADATA']._serialized_start=1200
  _globals['_CREATEFUNCTIONMETADATA']._serialized_end=1245
  _globals['_UPDATEFUNCTIONREQUEST']._serialized_start=1248
  _globals['_UPDATEFUNCTIONREQUEST']._serialized_end=1634
  _globals['_UPDATEFUNCTIONREQUEST_LABELSENTRY']._serialized_start=1153
  _globals['_UPDATEFUNCTIONREQUEST_LABELSENTRY']._serialized_end=1198
  _globals['_UPDATEFUNCTIONMETADATA']._serialized_start=1636
  _globals['_UPDATEFUNCTIONMETADATA']._serialized_end=1681
  _globals['_DELETEFUNCTIONREQUEST']._serialized_start=1683
  _globals['_DELETEFUNCTIONREQUEST']._serialized_end=1733
  _globals['_DELETEFUNCTIONMETADATA']._serialized_start=1735
  _globals['_DELETEFUNCTIONMETADATA']._serialized_end=1780
  _globals['_DELETEFUNCTIONVERSIONREQUEST']._serialized_start=1782
  _globals['_DELETEFUNCTIONVERSIONREQUEST']._serialized_end=1868
  _globals['_DELETEFUNCTIONVERSIONMETADATA']._serialized_start=1870
  _globals['_DELETEFUNCTIONVERSIONMETADATA']._serialized_end=1936
  _globals['_LISTRUNTIMESREQUEST']._serialized_start=1938
  _globals['_LISTRUNTIMESREQUEST']._serialized_end=1959
  _globals['_LISTRUNTIMESRESPONSE']._serialized_start=1961
  _globals['_LISTRUNTIMESRESPONSE']._serialized_end=2001
  _globals['_LISTFUNCTIONSVERSIONSREQUEST']._serialized_start=2004
  _globals['_LISTFUNCTIONSVERSIONSREQUEST']._serialized_end=2180
  _globals['_LISTFUNCTIONSVERSIONSRESPONSE']._serialized_start=2182
  _globals['_LISTFUNCTIONSVERSIONSRESPONSE']._serialized_end=2303
  _globals['_LISTFUNCTIONOPERATIONSREQUEST']._serialized_start=2306
  _globals['_LISTFUNCTIONOPERATIONSREQUEST']._serialized_end=2454
  _globals['_LISTFUNCTIONOPERATIONSRESPONSE']._serialized_start=2456
  _globals['_LISTFUNCTIONOPERATIONSRESPONSE']._serialized_end=2568
  _globals['_CREATEFUNCTIONVERSIONREQUEST']._serialized_start=2571
  _globals['_CREATEFUNCTIONVERSIONREQUEST']._serialized_end=3964
  _globals['_CREATEFUNCTIONVERSIONREQUEST_ENVIRONMENTENTRY']._serialized_start=3805
  _globals['_CREATEFUNCTIONVERSIONREQUEST_ENVIRONMENTENTRY']._serialized_end=3855
  _globals['_CREATEFUNCTIONVERSIONREQUEST_NAMEDSERVICEACCOUNTSENTRY']._serialized_start=3857
  _globals['_CREATEFUNCTIONVERSIONREQUEST_NAMEDSERVICEACCOUNTSENTRY']._serialized_end=3916
  _globals['_CREATEFUNCTIONVERSIONMETADATA']._serialized_start=3966
  _globals['_CREATEFUNCTIONVERSIONMETADATA']._serialized_end=4026
  _globals['_SETFUNCTIONTAGREQUEST']._serialized_start=4028
  _globals['_SETFUNCTIONTAGREQUEST']._serialized_end=4121
  _globals['_REMOVEFUNCTIONTAGREQUEST']._serialized_start=4123
  _globals['_REMOVEFUNCTIONTAGREQUEST']._serialized_end=4219
  _globals['_SETFUNCTIONTAGMETADATA']._serialized_start=4221
  _globals['_SETFUNCTIONTAGMETADATA']._serialized_end=4274
  _globals['_REMOVEFUNCTIONTAGMETADATA']._serialized_start=4276
  _globals['_REMOVEFUNCTIONTAGMETADATA']._serialized_end=4332
  _globals['_LISTFUNCTIONTAGHISTORYREQUEST']._serialized_start=4335
  _globals['_LISTFUNCTIONTAGHISTORYREQUEST']._serialized_end=4528
  _globals['_LISTFUNCTIONTAGHISTORYRESPONSE']._serialized_start=4531
  _globals['_LISTFUNCTIONTAGHISTORYRESPONSE']._serialized_end=4915
  _globals['_LISTFUNCTIONTAGHISTORYRESPONSE_FUNCTIONTAGHISTORYRECORD']._serialized_start=4724
  _globals['_LISTFUNCTIONTAGHISTORYRESPONSE_FUNCTIONTAGHISTORYRECORD']._serialized_end=4915
  _globals['_LISTSCALINGPOLICIESREQUEST']._serialized_start=4917
  _globals['_LISTSCALINGPOLICIESREQUEST']._serialized_end=5034
  _globals['_LISTSCALINGPOLICIESRESPONSE']._serialized_start=5037
  _globals['_LISTSCALINGPOLICIESRESPONSE']._serialized_end=5170
  _globals['_SETSCALINGPOLICYREQUEST']._serialized_start=5173
  _globals['_SETSCALINGPOLICYREQUEST']._serialized_end=5412
  _globals['_SETSCALINGPOLICYMETADATA']._serialized_start=5414
  _globals['_SETSCALINGPOLICYMETADATA']._serialized_end=5461
  _globals['_REMOVESCALINGPOLICYREQUEST']._serialized_start=5463
  _globals['_REMOVESCALINGPOLICYREQUEST']._serialized_end=5567
  _globals['_REMOVESCALINGPOLICYMETADATA']._serialized_start=5569
  _globals['_REMOVESCALINGPOLICYMETADATA']._serialized_end=5619
  _globals['_FUNCTIONSERVICE']._serialized_start=5622
  _globals['_FUNCTIONSERVICE']._serialized_end=9914
# @@protoc_insertion_point(module_scope)
