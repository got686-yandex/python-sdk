"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _FileCompressionType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FileCompressionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FileCompressionType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FILE_COMPRESSION_TYPE_UNSPECIFIED: _FileCompressionType.ValueType  # 0
    NONE: _FileCompressionType.ValueType  # 1
    ZIP: _FileCompressionType.ValueType  # 2

class FileCompressionType(_FileCompressionType, metaclass=_FileCompressionTypeEnumTypeWrapper): ...

FILE_COMPRESSION_TYPE_UNSPECIFIED: FileCompressionType.ValueType  # 0
NONE: FileCompressionType.ValueType  # 1
ZIP: FileCompressionType.ValueType  # 2
global___FileCompressionType = FileCompressionType

class _JobStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _JobStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_JobStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    JOB_STATUS_UNSPECIFIED: _JobStatus.ValueType  # 0
    CREATING: _JobStatus.ValueType  # 1
    EXECUTING: _JobStatus.ValueType  # 2
    UPLOADING_OUTPUT: _JobStatus.ValueType  # 3
    SUCCESS: _JobStatus.ValueType  # 4
    ERROR: _JobStatus.ValueType  # 5
    CANCELLED: _JobStatus.ValueType  # 6

class JobStatus(_JobStatus, metaclass=_JobStatusEnumTypeWrapper): ...

JOB_STATUS_UNSPECIFIED: JobStatus.ValueType  # 0
CREATING: JobStatus.ValueType  # 1
EXECUTING: JobStatus.ValueType  # 2
UPLOADING_OUTPUT: JobStatus.ValueType  # 3
SUCCESS: JobStatus.ValueType  # 4
ERROR: JobStatus.ValueType  # 5
CANCELLED: JobStatus.ValueType  # 6
global___JobStatus = JobStatus

@typing.final
class JobParameters(google.protobuf.message.Message):
    """Job parameters."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INPUT_FILES_FIELD_NUMBER: builtins.int
    OUTPUT_FILES_FIELD_NUMBER: builtins.int
    S3_MOUNT_IDS_FIELD_NUMBER: builtins.int
    DATASET_IDS_FIELD_NUMBER: builtins.int
    CMD_FIELD_NUMBER: builtins.int
    ENV_FIELD_NUMBER: builtins.int
    ATTACH_PROJECT_DISK_FIELD_NUMBER: builtins.int
    CLOUD_INSTANCE_TYPES_FIELD_NUMBER: builtins.int
    EXTENDED_WORKING_STORAGE_FIELD_NUMBER: builtins.int
    ARGUMENTS_FIELD_NUMBER: builtins.int
    cmd: builtins.str
    """Job run command."""
    attach_project_disk: builtins.bool
    """Should project disk be attached to VM."""
    @property
    def input_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]:
        """List of input files."""

    @property
    def output_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FileDesc]:
        """List of output files descriptions."""

    @property
    def s3_mount_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of DataSphere S3 mount ids."""

    @property
    def dataset_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of DataSphere dataset ids."""

    @property
    def env(self) -> global___Environment:
        """Job environment description."""

    @property
    def cloud_instance_types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CloudInstanceType]:
        """VM specification."""

    @property
    def extended_working_storage(self) -> global___ExtendedWorkingStorage:
        """Extended working storage configuration."""

    @property
    def arguments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Argument]:
        """List of literal arguments."""

    def __init__(
        self,
        *,
        input_files: collections.abc.Iterable[global___File] | None = ...,
        output_files: collections.abc.Iterable[global___FileDesc] | None = ...,
        s3_mount_ids: collections.abc.Iterable[builtins.str] | None = ...,
        dataset_ids: collections.abc.Iterable[builtins.str] | None = ...,
        cmd: builtins.str = ...,
        env: global___Environment | None = ...,
        attach_project_disk: builtins.bool = ...,
        cloud_instance_types: collections.abc.Iterable[global___CloudInstanceType] | None = ...,
        extended_working_storage: global___ExtendedWorkingStorage | None = ...,
        arguments: collections.abc.Iterable[global___Argument] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["env", b"env", "extended_working_storage", b"extended_working_storage"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["arguments", b"arguments", "attach_project_disk", b"attach_project_disk", "cloud_instance_types", b"cloud_instance_types", "cmd", b"cmd", "dataset_ids", b"dataset_ids", "env", b"env", "extended_working_storage", b"extended_working_storage", "input_files", b"input_files", "output_files", b"output_files", "s3_mount_ids", b"s3_mount_ids"]) -> None: ...

global___JobParameters = JobParameters

@typing.final
class CloudInstanceType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of DataSphere VM configuration."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name"]) -> None: ...

global___CloudInstanceType = CloudInstanceType

@typing.final
class ExtendedWorkingStorage(google.protobuf.message.Message):
    """Extended working storage configuration."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _StorageType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StorageTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ExtendedWorkingStorage._StorageType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STORAGE_TYPE_UNSPECIFIED: ExtendedWorkingStorage._StorageType.ValueType  # 0
        SSD: ExtendedWorkingStorage._StorageType.ValueType  # 1

    class StorageType(_StorageType, metaclass=_StorageTypeEnumTypeWrapper): ...
    STORAGE_TYPE_UNSPECIFIED: ExtendedWorkingStorage.StorageType.ValueType  # 0
    SSD: ExtendedWorkingStorage.StorageType.ValueType  # 1

    TYPE_FIELD_NUMBER: builtins.int
    SIZE_GB_FIELD_NUMBER: builtins.int
    type: global___ExtendedWorkingStorage.StorageType.ValueType
    size_gb: builtins.int
    def __init__(
        self,
        *,
        type: global___ExtendedWorkingStorage.StorageType.ValueType = ...,
        size_gb: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["size_gb", b"size_gb", "type", b"type"]) -> None: ...

global___ExtendedWorkingStorage = ExtendedWorkingStorage

@typing.final
class Argument(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    name: builtins.str
    value: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "value", b"value"]) -> None: ...

global___Argument = Argument

@typing.final
class File(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESC_FIELD_NUMBER: builtins.int
    SHA256_FIELD_NUMBER: builtins.int
    SIZE_BYTES_FIELD_NUMBER: builtins.int
    COMPRESSION_TYPE_FIELD_NUMBER: builtins.int
    sha256: builtins.str
    """SHA256 of the file."""
    size_bytes: builtins.int
    """File size in bytes."""
    compression_type: global___FileCompressionType.ValueType
    """File compression info"""
    @property
    def desc(self) -> global___FileDesc: ...
    def __init__(
        self,
        *,
        desc: global___FileDesc | None = ...,
        sha256: builtins.str = ...,
        size_bytes: builtins.int = ...,
        compression_type: global___FileCompressionType.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["desc", b"desc"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["compression_type", b"compression_type", "desc", b"desc", "sha256", b"sha256", "size_bytes", b"size_bytes"]) -> None: ...

global___File = File

@typing.final
class StorageFile(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    url: builtins.str
    """File URL."""
    @property
    def file(self) -> global___File: ...
    def __init__(
        self,
        *,
        file: global___File | None = ...,
        url: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["file", b"file"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["file", b"file", "url", b"url"]) -> None: ...

global___StorageFile = StorageFile

@typing.final
class FileDesc(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    VAR_FIELD_NUMBER: builtins.int
    path: builtins.str
    """Path of the file on filesystem."""
    var: builtins.str
    """Variable to use in cmd substitution."""
    def __init__(
        self,
        *,
        path: builtins.str = ...,
        var: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["path", b"path", "var", b"var"]) -> None: ...

global___FileDesc = FileDesc

@typing.final
class Environment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class VarsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    VARS_FIELD_NUMBER: builtins.int
    DOCKER_IMAGE_RESOURCE_ID_FIELD_NUMBER: builtins.int
    DOCKER_IMAGE_SPEC_FIELD_NUMBER: builtins.int
    PYTHON_ENV_FIELD_NUMBER: builtins.int
    docker_image_resource_id: builtins.str
    """DS docker image id."""
    @property
    def vars(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Environment variables."""

    @property
    def docker_image_spec(self) -> global___DockerImageSpec: ...
    @property
    def python_env(self) -> global___PythonEnv: ...
    def __init__(
        self,
        *,
        vars: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        docker_image_resource_id: builtins.str = ...,
        docker_image_spec: global___DockerImageSpec | None = ...,
        python_env: global___PythonEnv | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["docker_image", b"docker_image", "docker_image_resource_id", b"docker_image_resource_id", "docker_image_spec", b"docker_image_spec", "python_env", b"python_env"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["docker_image", b"docker_image", "docker_image_resource_id", b"docker_image_resource_id", "docker_image_spec", b"docker_image_spec", "python_env", b"python_env", "vars", b"vars"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["docker_image", b"docker_image"]) -> typing.Literal["docker_image_resource_id", "docker_image_spec"] | None: ...

global___Environment = Environment

@typing.final
class DockerImageSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_URL_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    PASSWORD_PLAIN_TEXT_FIELD_NUMBER: builtins.int
    PASSWORD_DS_SECRET_NAME_FIELD_NUMBER: builtins.int
    image_url: builtins.str
    """Docker image URL."""
    username: builtins.str
    """Username for container registry."""
    password_plain_text: builtins.str
    """Plaintext password."""
    password_ds_secret_name: builtins.str
    """ID of DataSphere secret containing password."""
    def __init__(
        self,
        *,
        image_url: builtins.str = ...,
        username: builtins.str = ...,
        password_plain_text: builtins.str = ...,
        password_ds_secret_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["password", b"password", "password_ds_secret_name", b"password_ds_secret_name", "password_plain_text", b"password_plain_text"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["image_url", b"image_url", "password", b"password", "password_ds_secret_name", b"password_ds_secret_name", "password_plain_text", b"password_plain_text", "username", b"username"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["password", b"password"]) -> typing.Literal["password_plain_text", "password_ds_secret_name"] | None: ...

global___DockerImageSpec = DockerImageSpec

@typing.final
class PythonEnv(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONDA_YAML_FIELD_NUMBER: builtins.int
    LOCAL_MODULES_FIELD_NUMBER: builtins.int
    conda_yaml: builtins.str
    """Conda YAML."""
    @property
    def local_modules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]:
        """List of local modules descriptions."""

    def __init__(
        self,
        *,
        conda_yaml: builtins.str = ...,
        local_modules: collections.abc.Iterable[global___File] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["conda_yaml", b"conda_yaml", "local_modules", b"local_modules"]) -> None: ...

global___PythonEnv = PythonEnv

@typing.final
class Job(google.protobuf.message.Message):
    """Instance of the job."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    FINISHED_AT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    CREATED_BY_ID_FIELD_NUMBER: builtins.int
    PROJECT_ID_FIELD_NUMBER: builtins.int
    JOB_PARAMETERS_FIELD_NUMBER: builtins.int
    DATA_EXPIRES_AT_FIELD_NUMBER: builtins.int
    DATA_CLEARED_FIELD_NUMBER: builtins.int
    OUTPUT_FILES_FIELD_NUMBER: builtins.int
    LOG_FILES_FIELD_NUMBER: builtins.int
    DIAGNOSTIC_FILES_FIELD_NUMBER: builtins.int
    DATA_SIZE_BYTES_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the job."""
    name: builtins.str
    """Name of the job."""
    desc: builtins.str
    """Description of the job."""
    status: global___JobStatus.ValueType
    """Status of the job."""
    config: builtins.str
    """Config of the job, copied from configuration file."""
    created_by_id: builtins.str
    """ID of the user who created the job."""
    project_id: builtins.str
    """ID of the project."""
    data_cleared: builtins.bool
    """Marks if the job data has been cleared."""
    data_size_bytes: builtins.int
    """Job total data size."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Create job timestamp."""

    @property
    def started_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Start job timestamp."""

    @property
    def finished_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Finish job timestamp."""

    @property
    def job_parameters(self) -> global___JobParameters: ...
    @property
    def data_expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Job data expiration timestamp."""

    @property
    def output_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]:
        """Output files of the job."""

    @property
    def log_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]:
        """Job log files."""

    @property
    def diagnostic_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]:
        """Job diagnostics files."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        desc: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        started_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        finished_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        status: global___JobStatus.ValueType = ...,
        config: builtins.str = ...,
        created_by_id: builtins.str = ...,
        project_id: builtins.str = ...,
        job_parameters: global___JobParameters | None = ...,
        data_expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        data_cleared: builtins.bool = ...,
        output_files: collections.abc.Iterable[global___File] | None = ...,
        log_files: collections.abc.Iterable[global___File] | None = ...,
        diagnostic_files: collections.abc.Iterable[global___File] | None = ...,
        data_size_bytes: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "data_expires_at", b"data_expires_at", "finished_at", b"finished_at", "job_parameters", b"job_parameters", "started_at", b"started_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["config", b"config", "created_at", b"created_at", "created_by_id", b"created_by_id", "data_cleared", b"data_cleared", "data_expires_at", b"data_expires_at", "data_size_bytes", b"data_size_bytes", "desc", b"desc", "diagnostic_files", b"diagnostic_files", "finished_at", b"finished_at", "id", b"id", "job_parameters", b"job_parameters", "log_files", b"log_files", "name", b"name", "output_files", b"output_files", "project_id", b"project_id", "started_at", b"started_at", "status", b"status"]) -> None: ...

global___Job = Job

@typing.final
class JobResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RETURN_CODE_FIELD_NUMBER: builtins.int
    return_code: builtins.int
    """Execution return code."""
    def __init__(
        self,
        *,
        return_code: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["return_code", b"return_code"]) -> None: ...

global___JobResult = JobResult