# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v2/jobs/project_job_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.datasphere.v2.jobs import jobs_pb2 as yandex_dot_cloud_dot_datasphere_dot_v2_dot_jobs_dot_jobs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9yandex/cloud/datasphere/v2/jobs/project_job_service.proto\x12\x1fyandex.cloud.datasphere.v2.jobs\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a yandex/cloud/api/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a&yandex/cloud/operation/operation.proto\x1a*yandex/cloud/datasphere/v2/jobs/jobs.proto\"\xce\x01\n\x17\x43reateProjectJobRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x46\n\x0ejob_parameters\x18\x02 \x01(\x0b\x32..yandex.cloud.datasphere.v2.jobs.JobParameters\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x05 \x01(\t\x12+\n\x08\x64\x61ta_ttl\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\".\n\x18\x43reateProjectJobMetadata\x12\x12\n\nproject_id\x18\x01 \x01(\t\"n\n\x18\x43reateProjectJobResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x42\n\x0cupload_files\x18\x02 \x03(\x0b\x32,.yandex.cloud.datasphere.v2.jobs.StorageFile\"*\n\x18\x45xecuteProjectJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\x9b\x01\n\x19\x45xecuteProjectJobResponse\x12\x42\n\x0coutput_files\x18\x01 \x03(\x0b\x32,.yandex.cloud.datasphere.v2.jobs.StorageFile\x12:\n\x06result\x18\x02 \x01(\x0b\x32*.yandex.cloud.datasphere.v2.jobs.JobResult\"N\n\x19\x45xecuteProjectJobMetadata\x12\x31\n\x03job\x18\x01 \x01(\x0b\x32$.yandex.cloud.datasphere.v2.jobs.Job\"9\n\x17\x43\x61ncelProjectJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\"+\n\x19\x46inalizeProjectJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\",\n\x1a\x46inalizeProjectJobResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\">\n\x1cReadProjectJobStdLogsRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\"f\n\x1dReadProjectJobStdLogsResponse\x12\x35\n\x04logs\x18\x01 \x03(\x0b\x32\'.yandex.cloud.datasphere.v2.jobs.StdLog\x12\x0e\n\x06offset\x18\x02 \x01(\x03\";\n\x19ReadProjectJobLogsRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\"g\n\x1aReadProjectJobLogsResponse\x12\x39\n\x04logs\x18\x01 \x03(\x0b\x32+.yandex.cloud.datasphere.v2.jobs.LogMessage\x12\x0e\n\x06offset\x18\x02 \x01(\x03\"u\n\x1e\x44ownloadProjectJobFilesRequest\x12\x14\n\x06job_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12=\n\x05\x66iles\x18\x02 \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.FileB\x07\x82\xc8\x31\x03>=1\"g\n\x1f\x44ownloadProjectJobFilesResponse\x12\x44\n\x0e\x64ownload_files\x18\x01 \x03(\x0b\x32,.yandex.cloud.datasphere.v2.jobs.StorageFile\"R\n\x15ListProjectJobRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"`\n\x16ListProjectJobResponse\x12\x32\n\x04jobs\x18\x01 \x03(\x0b\x32$.yandex.cloud.datasphere.v2.jobs.Job\x12\x12\n\npage_token\x18\x02 \x01(\t\"&\n\x14GetProjectJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\")\n\x17\x44\x65leteProjectJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"*\n\x18\x44\x65leteProjectJobMetadata\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\x85\x01\n\x06StdLog\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12:\n\x04type\x18\x02 \x01(\x0e\x32,.yandex.cloud.datasphere.v2.jobs.StdLog.Type\".\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03OUT\x10\x01\x12\x07\n\x03\x45RR\x10\x02\"\xb8\x01\n\nLogMessage\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12J\n\x0fstandard_stream\x18\x03 \x01(\x0e\x32/.yandex.cloud.datasphere.v2.jobs.StandardStreamH\x00\x12\x13\n\tfile_path\x18\x04 \x01(\tH\x00\x42\x08\n\x06source*C\n\x0eStandardStream\x12\x1f\n\x1bSTANDARD_STREAM_UNSPECIFIED\x10\x00\x12\x07\n\x03OUT\x10\x01\x12\x07\n\x03\x45RR\x10\x02\x32\xef\n\n\x11ProjectJobService\x12\x9f\x01\n\x06\x43reate\x12\x38.yandex.cloud.datasphere.v2.jobs.CreateProjectJobRequest\x1a!.yandex.cloud.operation.Operation\"8\xb2\xd2*4\n\x18\x43reateProjectJobMetadata\x12\x18\x43reateProjectJobResponse\x12\xa3\x01\n\x07\x45xecute\x12\x39.yandex.cloud.datasphere.v2.jobs.ExecuteProjectJobRequest\x1a!.yandex.cloud.operation.Operation\":\xb2\xd2*6\n\x19\x45xecuteProjectJobMetadata\x12\x19\x45xecuteProjectJobResponse\x12Z\n\x06\x43\x61ncel\x12\x38.yandex.cloud.datasphere.v2.jobs.CancelProjectJobRequest\x1a\x16.google.protobuf.Empty\x12\x83\x01\n\x08\x46inalize\x12:.yandex.cloud.datasphere.v2.jobs.FinalizeProjectJobRequest\x1a;.yandex.cloud.datasphere.v2.jobs.FinalizeProjectJobResponse\x12\x93\x01\n\x0bReadStdLogs\x12=.yandex.cloud.datasphere.v2.jobs.ReadProjectJobStdLogsRequest\x1a>.yandex.cloud.datasphere.v2.jobs.ReadProjectJobStdLogsResponse\"\x03\x88\x02\x01\x30\x01\x12\x85\x01\n\x08ReadLogs\x12:.yandex.cloud.datasphere.v2.jobs.ReadProjectJobLogsRequest\x1a;.yandex.cloud.datasphere.v2.jobs.ReadProjectJobLogsResponse0\x01\x12\x95\x01\n\x10\x44ownloadJobFiles\x12?.yandex.cloud.datasphere.v2.jobs.DownloadProjectJobFilesRequest\x1a@.yandex.cloud.datasphere.v2.jobs.DownloadProjectJobFilesResponse\x12w\n\x04List\x12\x36.yandex.cloud.datasphere.v2.jobs.ListProjectJobRequest\x1a\x37.yandex.cloud.datasphere.v2.jobs.ListProjectJobResponse\x12\x62\n\x03Get\x12\x35.yandex.cloud.datasphere.v2.jobs.GetProjectJobRequest\x1a$.yandex.cloud.datasphere.v2.jobs.Job\x12\x9c\x01\n\x06\x44\x65lete\x12\x38.yandex.cloud.datasphere.v2.jobs.DeleteProjectJobRequest\x1a!.yandex.cloud.operation.Operation\"5\xb2\xd2*1\n\x18\x44\x65leteProjectJobMetadata\x12\x15google.protobuf.EmptyB|\n#yandex.cloud.api.datasphere.v2.jobsB\x05\x44SPJSZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2/jobs;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.jobs.project_job_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#yandex.cloud.api.datasphere.v2.jobsB\005DSPJSZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2/jobs;datasphere'
  _DOWNLOADPROJECTJOBFILESREQUEST.fields_by_name['job_id']._options = None
  _DOWNLOADPROJECTJOBFILESREQUEST.fields_by_name['job_id']._serialized_options = b'\350\3071\001'
  _DOWNLOADPROJECTJOBFILESREQUEST.fields_by_name['files']._options = None
  _DOWNLOADPROJECTJOBFILESREQUEST.fields_by_name['files']._serialized_options = b'\202\3101\003>=1'
  _PROJECTJOBSERVICE.methods_by_name['Create']._options = None
  _PROJECTJOBSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*4\n\030CreateProjectJobMetadata\022\030CreateProjectJobResponse'
  _PROJECTJOBSERVICE.methods_by_name['Execute']._options = None
  _PROJECTJOBSERVICE.methods_by_name['Execute']._serialized_options = b'\262\322*6\n\031ExecuteProjectJobMetadata\022\031ExecuteProjectJobResponse'
  _PROJECTJOBSERVICE.methods_by_name['ReadStdLogs']._options = None
  _PROJECTJOBSERVICE.methods_by_name['ReadStdLogs']._serialized_options = b'\210\002\001'
  _PROJECTJOBSERVICE.methods_by_name['Delete']._options = None
  _PROJECTJOBSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*1\n\030DeleteProjectJobMetadata\022\025google.protobuf.Empty'
  _globals['_STANDARDSTREAM']._serialized_start=2328
  _globals['_STANDARDSTREAM']._serialized_end=2395
  _globals['_CREATEPROJECTJOBREQUEST']._serialized_start=338
  _globals['_CREATEPROJECTJOBREQUEST']._serialized_end=544
  _globals['_CREATEPROJECTJOBMETADATA']._serialized_start=546
  _globals['_CREATEPROJECTJOBMETADATA']._serialized_end=592
  _globals['_CREATEPROJECTJOBRESPONSE']._serialized_start=594
  _globals['_CREATEPROJECTJOBRESPONSE']._serialized_end=704
  _globals['_EXECUTEPROJECTJOBREQUEST']._serialized_start=706
  _globals['_EXECUTEPROJECTJOBREQUEST']._serialized_end=748
  _globals['_EXECUTEPROJECTJOBRESPONSE']._serialized_start=751
  _globals['_EXECUTEPROJECTJOBRESPONSE']._serialized_end=906
  _globals['_EXECUTEPROJECTJOBMETADATA']._serialized_start=908
  _globals['_EXECUTEPROJECTJOBMETADATA']._serialized_end=986
  _globals['_CANCELPROJECTJOBREQUEST']._serialized_start=988
  _globals['_CANCELPROJECTJOBREQUEST']._serialized_end=1045
  _globals['_FINALIZEPROJECTJOBREQUEST']._serialized_start=1047
  _globals['_FINALIZEPROJECTJOBREQUEST']._serialized_end=1090
  _globals['_FINALIZEPROJECTJOBRESPONSE']._serialized_start=1092
  _globals['_FINALIZEPROJECTJOBRESPONSE']._serialized_end=1136
  _globals['_READPROJECTJOBSTDLOGSREQUEST']._serialized_start=1138
  _globals['_READPROJECTJOBSTDLOGSREQUEST']._serialized_end=1200
  _globals['_READPROJECTJOBSTDLOGSRESPONSE']._serialized_start=1202
  _globals['_READPROJECTJOBSTDLOGSRESPONSE']._serialized_end=1304
  _globals['_READPROJECTJOBLOGSREQUEST']._serialized_start=1306
  _globals['_READPROJECTJOBLOGSREQUEST']._serialized_end=1365
  _globals['_READPROJECTJOBLOGSRESPONSE']._serialized_start=1367
  _globals['_READPROJECTJOBLOGSRESPONSE']._serialized_end=1470
  _globals['_DOWNLOADPROJECTJOBFILESREQUEST']._serialized_start=1472
  _globals['_DOWNLOADPROJECTJOBFILESREQUEST']._serialized_end=1589
  _globals['_DOWNLOADPROJECTJOBFILESRESPONSE']._serialized_start=1591
  _globals['_DOWNLOADPROJECTJOBFILESRESPONSE']._serialized_end=1694
  _globals['_LISTPROJECTJOBREQUEST']._serialized_start=1696
  _globals['_LISTPROJECTJOBREQUEST']._serialized_end=1778
  _globals['_LISTPROJECTJOBRESPONSE']._serialized_start=1780
  _globals['_LISTPROJECTJOBRESPONSE']._serialized_end=1876
  _globals['_GETPROJECTJOBREQUEST']._serialized_start=1878
  _globals['_GETPROJECTJOBREQUEST']._serialized_end=1916
  _globals['_DELETEPROJECTJOBREQUEST']._serialized_start=1918
  _globals['_DELETEPROJECTJOBREQUEST']._serialized_end=1959
  _globals['_DELETEPROJECTJOBMETADATA']._serialized_start=1961
  _globals['_DELETEPROJECTJOBMETADATA']._serialized_end=2003
  _globals['_STDLOG']._serialized_start=2006
  _globals['_STDLOG']._serialized_end=2139
  _globals['_STDLOG_TYPE']._serialized_start=2093
  _globals['_STDLOG_TYPE']._serialized_end=2139
  _globals['_LOGMESSAGE']._serialized_start=2142
  _globals['_LOGMESSAGE']._serialized_end=2326
  _globals['_PROJECTJOBSERVICE']._serialized_start=2398
  _globals['_PROJECTJOBSERVICE']._serialized_end=3789
# @@protoc_insertion_point(module_scope)
