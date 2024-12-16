# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/dataproc/manager/v1/job_service.proto
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
    'yandex/cloud/dataproc/manager/v1/job_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.dataproc.manager.v1 import job_pb2 as yandex_dot_cloud_dot_dataproc_dot_manager_dot_v1_dot_job__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/dataproc/manager/v1/job_service.proto\x12 yandex.cloud.dataproc.manager.v1\x1a\x1dyandex/cloud/validation.proto\x1a*yandex/cloud/dataproc/manager/v1/job.proto\"\x89\x01\n\x0fListJobsRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"`\n\x10ListJobsResponse\x12\x33\n\x04jobs\x18\x01 \x03(\x0b\x32%.yandex.cloud.dataproc.manager.v1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xdb\x01\n\x16UpdateJobStatusRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x18\n\x06job_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12<\n\x06status\x18\x03 \x01(\x0e\x32,.yandex.cloud.dataproc.manager.v1.Job.Status\x12K\n\x10\x61pplication_info\x18\x04 \x01(\x0b\x32\x31.yandex.cloud.dataproc.manager.v1.ApplicationInfo\"\x19\n\x17UpdateJobStatusResponse\"n\n\x17ListSupportJobsResponse\x12:\n\x04jobs\x18\x01 \x03(\x0b\x32,.yandex.cloud.dataproc.manager.v1.SupportJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x9c\x01\n\x1dUpdateSupportJobStatusRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x18\n\x06job_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x43\n\x06status\x18\x03 \x01(\x0e\x32\x33.yandex.cloud.dataproc.manager.v1.SupportJob.Status\"b\n\x18SaveSupportJobLogRequest\x12\x1c\n\ncluster_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x18\n\x06job_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x0e\n\x06output\x18\x03 \x01(\t\"\x1b\n\x19SaveSupportJobLogResponse2\xb5\x05\n\nJobService\x12u\n\nListActive\x12\x31.yandex.cloud.dataproc.manager.v1.ListJobsRequest\x1a\x32.yandex.cloud.dataproc.manager.v1.ListJobsResponse\"\x00\x12\x85\x01\n\x0cUpdateStatus\x12\x38.yandex.cloud.dataproc.manager.v1.UpdateJobStatusRequest\x1a\x39.yandex.cloud.dataproc.manager.v1.UpdateJobStatusResponse\"\x00\x12\x83\x01\n\x11ListSupportActive\x12\x31.yandex.cloud.dataproc.manager.v1.ListJobsRequest\x1a\x39.yandex.cloud.dataproc.manager.v1.ListSupportJobsResponse\"\x00\x12\x93\x01\n\x13UpdateSupportStatus\x12?.yandex.cloud.dataproc.manager.v1.UpdateSupportJobStatusRequest\x1a\x39.yandex.cloud.dataproc.manager.v1.UpdateJobStatusResponse\"\x00\x12\x8b\x01\n\x0eSaveSupportLog\x12:.yandex.cloud.dataproc.manager.v1.SaveSupportJobLogRequest\x1a;.yandex.cloud.dataproc.manager.v1.SaveSupportJobLogResponse\"\x00\x42}\n$yandex.cloud.api.dataproc.manager.v1ZUgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/manager/v1;dataproc_managerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.dataproc.manager.v1.job_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$yandex.cloud.api.dataproc.manager.v1ZUgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/manager/v1;dataproc_manager'
  _globals['_LISTJOBSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_LISTJOBSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTJOBSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTJOBSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTJOBSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTJOBSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTJOBSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTJOBSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_UPDATEJOBSTATUSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATEJOBSTATUSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_UPDATEJOBSTATUSREQUEST'].fields_by_name['job_id']._loaded_options = None
  _globals['_UPDATEJOBSTATUSREQUEST'].fields_by_name['job_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_UPDATESUPPORTJOBSTATUSREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_UPDATESUPPORTJOBSTATUSREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_UPDATESUPPORTJOBSTATUSREQUEST'].fields_by_name['job_id']._loaded_options = None
  _globals['_UPDATESUPPORTJOBSTATUSREQUEST'].fields_by_name['job_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_SAVESUPPORTJOBLOGREQUEST'].fields_by_name['cluster_id']._loaded_options = None
  _globals['_SAVESUPPORTJOBLOGREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_SAVESUPPORTJOBLOGREQUEST'].fields_by_name['job_id']._loaded_options = None
  _globals['_SAVESUPPORTJOBLOGREQUEST'].fields_by_name['job_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_LISTJOBSREQUEST']._serialized_start=164
  _globals['_LISTJOBSREQUEST']._serialized_end=301
  _globals['_LISTJOBSRESPONSE']._serialized_start=303
  _globals['_LISTJOBSRESPONSE']._serialized_end=399
  _globals['_UPDATEJOBSTATUSREQUEST']._serialized_start=402
  _globals['_UPDATEJOBSTATUSREQUEST']._serialized_end=621
  _globals['_UPDATEJOBSTATUSRESPONSE']._serialized_start=623
  _globals['_UPDATEJOBSTATUSRESPONSE']._serialized_end=648
  _globals['_LISTSUPPORTJOBSRESPONSE']._serialized_start=650
  _globals['_LISTSUPPORTJOBSRESPONSE']._serialized_end=760
  _globals['_UPDATESUPPORTJOBSTATUSREQUEST']._serialized_start=763
  _globals['_UPDATESUPPORTJOBSTATUSREQUEST']._serialized_end=919
  _globals['_SAVESUPPORTJOBLOGREQUEST']._serialized_start=921
  _globals['_SAVESUPPORTJOBLOGREQUEST']._serialized_end=1019
  _globals['_SAVESUPPORTJOBLOGRESPONSE']._serialized_start=1021
  _globals['_SAVESUPPORTJOBLOGRESPONSE']._serialized_end=1048
  _globals['_JOBSERVICE']._serialized_start=1051
  _globals['_JOBSERVICE']._serialized_end=1744
# @@protoc_insertion_point(module_scope)
