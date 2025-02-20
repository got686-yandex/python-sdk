# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/datasphere/v2/jobs/jobs.proto
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
    'yandex/cloud/datasphere/v2/jobs/jobs.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/datasphere/v2/jobs/jobs.proto\x12\x1fyandex.cloud.datasphere.v2.jobs\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1egoogle/protobuf/duration.proto\"\x8c\x06\n\rJobParameters\x12:\n\x0binput_files\x18\x01 \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12?\n\x0coutput_files\x18\x02 \x03(\x0b\x32).yandex.cloud.datasphere.v2.jobs.FileDesc\x12\x14\n\x0cs3_mount_ids\x18\x03 \x03(\t\x12\x13\n\x0b\x64\x61taset_ids\x18\x04 \x03(\t\x12\x0b\n\x03\x63md\x18\x05 \x01(\t\x12\x39\n\x03\x65nv\x18\x06 \x01(\x0b\x32,.yandex.cloud.datasphere.v2.jobs.Environment\x12\x1b\n\x13\x61ttach_project_disk\x18\x07 \x01(\x08\x12Y\n\x14\x63loud_instance_types\x18\x08 \x03(\x0b\x32\x32.yandex.cloud.datasphere.v2.jobs.CloudInstanceTypeB\x07\x82\xc8\x31\x03>=1\x12Y\n\x18\x65xtended_working_storage\x18\t \x01(\x0b\x32\x37.yandex.cloud.datasphere.v2.jobs.ExtendedWorkingStorage\x12<\n\targuments\x18\n \x03(\x0b\x32).yandex.cloud.datasphere.v2.jobs.Argument\x12K\n\x0foutput_datasets\x18\x0b \x03(\x0b\x32\x32.yandex.cloud.datasphere.v2.jobs.OutputDatasetDesc\x12\x61\n\x1cgraceful_shutdown_parameters\x18\x0c \x01(\x0b\x32;.yandex.cloud.datasphere.v2.jobs.GracefulShutdownParameters\x12J\n\x10spark_parameters\x18\r \x01(\x0b\x32\x30.yandex.cloud.datasphere.v2.jobs.SparkParameters\"!\n\x11\x43loudInstanceType\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xb2\x01\n\x16\x45xtendedWorkingStorage\x12Q\n\x04type\x18\x01 \x01(\x0e\x32\x43.yandex.cloud.datasphere.v2.jobs.ExtendedWorkingStorage.StorageType\x12\x0f\n\x07size_gb\x18\x02 \x01(\x03\"4\n\x0bStorageType\x12\x1c\n\x18STORAGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03SSD\x10\x01\"\'\n\x08\x41rgument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xb3\x01\n\x04\x46ile\x12\x37\n\x04\x64\x65sc\x18\x01 \x01(\x0b\x32).yandex.cloud.datasphere.v2.jobs.FileDesc\x12\x0e\n\x06sha256\x18\x02 \x01(\t\x12\x12\n\nsize_bytes\x18\x03 \x01(\x03\x12N\n\x10\x63ompression_type\x18\x04 \x01(\x0e\x32\x34.yandex.cloud.datasphere.v2.jobs.FileCompressionType\"O\n\x0bStorageFile\x12\x33\n\x04\x66ile\x18\x01 \x01(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12\x0b\n\x03url\x18\x02 \x01(\t\"%\n\x08\x46ileDesc\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0b\n\x03var\x18\x02 \x01(\t\"\xa8\x02\n\x0f\x46ileUploadError\x12\x45\n\x10output_file_desc\x18\x01 \x01(\x0b\x32).yandex.cloud.datasphere.v2.jobs.FileDescH\x00\x12\x17\n\rlog_file_name\x18\x02 \x01(\tH\x00\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12H\n\x04type\x18\x04 \x01(\x0e\x32:.yandex.cloud.datasphere.v2.jobs.FileUploadError.ErrorType\"I\n\tErrorType\x12\x1a\n\x16\x45RROR_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rUPLOAD_FAILED\x10\x01\x12\r\n\tNOT_FOUND\x10\x02\x42\x0b\n\tfile_type\"\xc3\x02\n\x0b\x45nvironment\x12\x44\n\x04vars\x18\x01 \x03(\x0b\x32\x36.yandex.cloud.datasphere.v2.jobs.Environment.VarsEntry\x12\"\n\x18\x64ocker_image_resource_id\x18\x02 \x01(\tH\x00\x12M\n\x11\x64ocker_image_spec\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.datasphere.v2.jobs.DockerImageSpecH\x00\x12>\n\npython_env\x18\x04 \x01(\x0b\x32*.yandex.cloud.datasphere.v2.jobs.PythonEnv\x1a+\n\tVarsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0e\n\x0c\x64ocker_image\"\x84\x01\n\x0f\x44ockerImageSpec\x12\x11\n\timage_url\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x1d\n\x13password_plain_text\x18\x03 \x01(\tH\x00\x12!\n\x17password_ds_secret_name\x18\x04 \x01(\tH\x00\x42\n\n\x08password\"\xcd\x01\n\tPythonEnv\x12\x12\n\nconda_yaml\x18\x01 \x01(\t\x12<\n\rlocal_modules\x18\x02 \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12\x16\n\x0epython_version\x18\x03 \x01(\t\x12\x14\n\x0crequirements\x18\x04 \x03(\t\x12@\n\x0bpip_options\x18\x05 \x01(\x0b\x32+.yandex.cloud.datasphere.v2.jobs.PipOptions\"a\n\nPipOptions\x12\x11\n\tindex_url\x18\x01 \x01(\t\x12\x18\n\x10\x65xtra_index_urls\x18\x02 \x03(\t\x12\x15\n\rtrusted_hosts\x18\x03 \x03(\t\x12\x0f\n\x07no_deps\x18\x04 \x01(\x08\"\xd3\x01\n\x11OutputDatasetDesc\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12N\n\x06labels\x18\x03 \x03(\x0b\x32>.yandex.cloud.datasphere.v2.jobs.OutputDatasetDesc.LabelsEntry\x12\x0f\n\x07size_gb\x18\x04 \x01(\x03\x12\x0b\n\x03var\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"]\n\rOutputDataset\x12@\n\x04\x64\x65sc\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.datasphere.v2.jobs.OutputDatasetDesc\x12\n\n\x02id\x18\x02 \x01(\t\"\xb0\x07\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x06status\x18\x06 \x01(\x0e\x32*.yandex.cloud.datasphere.v2.jobs.JobStatus\x12\x0e\n\x06\x63onfig\x18\x07 \x01(\t\x12\x15\n\rcreated_by_id\x18\x08 \x01(\t\x12\x12\n\nproject_id\x18\t \x01(\t\x12\x46\n\x0ejob_parameters\x18\n \x01(\x0b\x32..yandex.cloud.datasphere.v2.jobs.JobParameters\x12\x33\n\x0f\x64\x61ta_expires_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0c\x64\x61ta_cleared\x18\x0c \x01(\x08\x12;\n\x0coutput_files\x18\r \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12\x38\n\tlog_files\x18\x0e \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12?\n\x10\x64iagnostic_files\x18\x0f \x03(\x0b\x32%.yandex.cloud.datasphere.v2.jobs.File\x12\x17\n\x0f\x64\x61ta_size_bytes\x18\x10 \x01(\x03\x12.\n\nstarted_at\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0estatus_details\x18\x12 \x01(\t\x12V\n\x1a\x61\x63tual_cloud_instance_type\x18\x13 \x01(\x0b\x32\x32.yandex.cloud.datasphere.v2.jobs.CloudInstanceType\x12\x15\n\rparent_job_id\x18\x14 \x01(\t\x12\x45\n\x0b\x66ile_errors\x18\x15 \x03(\x0b\x32\x30.yandex.cloud.datasphere.v2.jobs.FileUploadError\x12G\n\x0foutput_datasets\x18\x16 \x03(\x0b\x32..yandex.cloud.datasphere.v2.jobs.OutputDataset\" \n\tJobResult\x12\x13\n\x0breturn_code\x18\x01 \x01(\x03\"X\n\x1aGracefulShutdownParameters\x12*\n\x07timeout\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0e\n\x06signal\x18\x02 \x01(\x03\"\x98\x03\n\x0bJobMetadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstarted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0f\x64\x61ta_expires_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x06status\x18\x08 \x01(\x0e\x32*.yandex.cloud.datasphere.v2.jobs.JobStatus\x12\x16\n\x0estatus_details\x18\t \x01(\t\x12\x15\n\rcreated_by_id\x18\n \x01(\t\x12\x12\n\nproject_id\x18\x0b \x01(\t\x12\x15\n\rparent_job_id\x18\x0c \x01(\t\"a\n\x0bJobProgress\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08progress\x18\x02 \x01(\x03\x12/\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\'\n\x0fSparkParameters\x12\x14\n\x0c\x63onnector_id\x18\x01 \x01(\t*O\n\x13\x46ileCompressionType\x12%\n!FILE_COMPRESSION_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x07\n\x03ZIP\x10\x02*\xa0\x01\n\tJobStatus\x12\x1a\n\x16JOB_STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\r\n\tEXECUTING\x10\x02\x12\x14\n\x10UPLOADING_OUTPUT\x10\x03\x12\x0b\n\x07SUCCESS\x10\x04\x12\t\n\x05\x45RROR\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\x0e\n\nCANCELLING\x10\x07\x12\r\n\tPREPARING\x10\x08\x42{\n#yandex.cloud.api.datasphere.v2.jobsB\x04JobsZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2/jobs;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.jobs.jobs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#yandex.cloud.api.datasphere.v2.jobsB\004JobsZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2/jobs;datasphere'
  _globals['_JOBPARAMETERS'].fields_by_name['cloud_instance_types']._loaded_options = None
  _globals['_JOBPARAMETERS'].fields_by_name['cloud_instance_types']._serialized_options = b'\202\3101\003>=1'
  _globals['_ENVIRONMENT_VARSENTRY']._loaded_options = None
  _globals['_ENVIRONMENT_VARSENTRY']._serialized_options = b'8\001'
  _globals['_OUTPUTDATASETDESC_LABELSENTRY']._loaded_options = None
  _globals['_OUTPUTDATASETDESC_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_FILECOMPRESSIONTYPE']._serialized_start=4515
  _globals['_FILECOMPRESSIONTYPE']._serialized_end=4594
  _globals['_JOBSTATUS']._serialized_start=4597
  _globals['_JOBSTATUS']._serialized_end=4757
  _globals['_JOBPARAMETERS']._serialized_start=176
  _globals['_JOBPARAMETERS']._serialized_end=956
  _globals['_CLOUDINSTANCETYPE']._serialized_start=958
  _globals['_CLOUDINSTANCETYPE']._serialized_end=991
  _globals['_EXTENDEDWORKINGSTORAGE']._serialized_start=994
  _globals['_EXTENDEDWORKINGSTORAGE']._serialized_end=1172
  _globals['_EXTENDEDWORKINGSTORAGE_STORAGETYPE']._serialized_start=1120
  _globals['_EXTENDEDWORKINGSTORAGE_STORAGETYPE']._serialized_end=1172
  _globals['_ARGUMENT']._serialized_start=1174
  _globals['_ARGUMENT']._serialized_end=1213
  _globals['_FILE']._serialized_start=1216
  _globals['_FILE']._serialized_end=1395
  _globals['_STORAGEFILE']._serialized_start=1397
  _globals['_STORAGEFILE']._serialized_end=1476
  _globals['_FILEDESC']._serialized_start=1478
  _globals['_FILEDESC']._serialized_end=1515
  _globals['_FILEUPLOADERROR']._serialized_start=1518
  _globals['_FILEUPLOADERROR']._serialized_end=1814
  _globals['_FILEUPLOADERROR_ERRORTYPE']._serialized_start=1728
  _globals['_FILEUPLOADERROR_ERRORTYPE']._serialized_end=1801
  _globals['_ENVIRONMENT']._serialized_start=1817
  _globals['_ENVIRONMENT']._serialized_end=2140
  _globals['_ENVIRONMENT_VARSENTRY']._serialized_start=2081
  _globals['_ENVIRONMENT_VARSENTRY']._serialized_end=2124
  _globals['_DOCKERIMAGESPEC']._serialized_start=2143
  _globals['_DOCKERIMAGESPEC']._serialized_end=2275
  _globals['_PYTHONENV']._serialized_start=2278
  _globals['_PYTHONENV']._serialized_end=2483
  _globals['_PIPOPTIONS']._serialized_start=2485
  _globals['_PIPOPTIONS']._serialized_end=2582
  _globals['_OUTPUTDATASETDESC']._serialized_start=2585
  _globals['_OUTPUTDATASETDESC']._serialized_end=2796
  _globals['_OUTPUTDATASETDESC_LABELSENTRY']._serialized_start=2751
  _globals['_OUTPUTDATASETDESC_LABELSENTRY']._serialized_end=2796
  _globals['_OUTPUTDATASET']._serialized_start=2798
  _globals['_OUTPUTDATASET']._serialized_end=2891
  _globals['_JOB']._serialized_start=2894
  _globals['_JOB']._serialized_end=3838
  _globals['_JOBRESULT']._serialized_start=3840
  _globals['_JOBRESULT']._serialized_end=3872
  _globals['_GRACEFULSHUTDOWNPARAMETERS']._serialized_start=3874
  _globals['_GRACEFULSHUTDOWNPARAMETERS']._serialized_end=3962
  _globals['_JOBMETADATA']._serialized_start=3965
  _globals['_JOBMETADATA']._serialized_end=4373
  _globals['_JOBPROGRESS']._serialized_start=4375
  _globals['_JOBPROGRESS']._serialized_end=4472
  _globals['_SPARKPARAMETERS']._serialized_start=4474
  _globals['_SPARKPARAMETERS']._serialized_end=4513
# @@protoc_insertion_point(module_scope)
