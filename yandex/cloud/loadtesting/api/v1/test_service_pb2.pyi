"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.loadtesting.api.v1.test.details_pb2
import yandex.cloud.loadtesting.api.v1.test.single_agent_configuration_pb2
import yandex.cloud.loadtesting.api.v1.test.test_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CreateTestRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    CONFIGURATIONS_FIELD_NUMBER: builtins.int
    TEST_DETAILS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a test in."""
    @property
    def configurations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.loadtesting.api.v1.test.single_agent_configuration_pb2.SingleAgentConfiguration]:
        """Test configuration associated with agents on which they will be executed.
        In case of multiple configurations, a multitest will be created.
        """

    @property
    def test_details(self) -> yandex.cloud.loadtesting.api.v1.test.details_pb2.Details:
        """Test details. Name, tags etc."""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        configurations: collections.abc.Iterable[yandex.cloud.loadtesting.api.v1.test.single_agent_configuration_pb2.SingleAgentConfiguration] | None = ...,
        test_details: yandex.cloud.loadtesting.api.v1.test.details_pb2.Details | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["test_details", b"test_details"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["configurations", b"configurations", "folder_id", b"folder_id", "test_details", b"test_details"]) -> None: ...

global___CreateTestRequest = CreateTestRequest

@typing.final
class CreateTestMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEST_ID_FIELD_NUMBER: builtins.int
    test_id: builtins.str
    """ID of the test that is being created."""
    def __init__(
        self,
        *,
        test_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["test_id", b"test_id"]) -> None: ...

global___CreateTestMetadata = CreateTestMetadata

@typing.final
class GetTestRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEST_ID_FIELD_NUMBER: builtins.int
    test_id: builtins.str
    """ID of the test to return."""
    def __init__(
        self,
        *,
        test_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["test_id", b"test_id"]) -> None: ...

global___GetTestRequest = GetTestRequest

@typing.final
class StopTestRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEST_ID_FIELD_NUMBER: builtins.int
    test_id: builtins.str
    """ID of the test to stop."""
    def __init__(
        self,
        *,
        test_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["test_id", b"test_id"]) -> None: ...

global___StopTestRequest = StopTestRequest

@typing.final
class StopTestMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEST_ID_FIELD_NUMBER: builtins.int
    test_id: builtins.str
    """ID of the test that is being stopped."""
    def __init__(
        self,
        *,
        test_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["test_id", b"test_id"]) -> None: ...

global___StopTestMetadata = StopTestMetadata

@typing.final
class DeleteTestRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEST_ID_FIELD_NUMBER: builtins.int
    test_id: builtins.str
    """ID of the test to delete."""
    def __init__(
        self,
        *,
        test_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["test_id", b"test_id"]) -> None: ...

global___DeleteTestRequest = DeleteTestRequest

@typing.final
class DeleteTestMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEST_ID_FIELD_NUMBER: builtins.int
    test_id: builtins.str
    """ID of the test that is being deleted."""
    def __init__(
        self,
        *,
        test_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["test_id", b"test_id"]) -> None: ...

global___DeleteTestMetadata = DeleteTestMetadata

@typing.final
class ListTestsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list tests in."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListTestsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the 
    [ListTestsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters tests listed in the response.

    The filter expression may contain multiple field expressions joined by `AND`.
    The field expression must specify:
    1. The field name.
    2. An operator:
       - `=`, `!=`, `<`, `<=`, `>`, `>=`, `CONTAINS`, `:` for single values.
       - `IN` or `NOT IN` for lists of values.
    3. The value. String values must be encosed in `"`, boolean values are {`true`, `false`}, timestamp values in ISO-8601.

    Currently supported fields:
    - `id` [yandex.cloud.loadtesting.api.v1.test.Test.id]
      - operators: `=`, `!=`, `IN`, `NOT IN`
    - `details.name` [yandex.cloud.loadtesting.api.v1.test.Details.name]
      - operators: `=`, `!=`, `IN`, `NOT IN`, `CONTAINS`
    - `details.tags.<TAG_NAME>` [yandex.cloud.loadtesting.api.v1.test.Details.tags]
      - operators: `:`
    - `summary.status` [yandex.cloud.loadtesting.api.v1.test.Summary.status]
      - operators: `=`, `!=`, `IN`, `NOT IN`
    - `summary.is_finished` [yandex.cloud.loadtesting.api.v1.test.Summary.is_finished]
      - operators: `=`
    - `summary.created_at` [yandex.cloud.loadtesting.api.v1.test.Summary.created_at]
      - operators: `<`, `<=`, `>`, `>=`
    - `summary.created_by` [yandex.cloud.loadtesting.api.v1.test.Summary.created_by]
      - operators: `=`, `!=`, `IN`, `NOT IN`

    Examples: 
    - `summary.status IN ("DONE", "ERROR") AND details.tags.author:"yandex"`
    - `summary.is_finished = true AND details.name CONTAINS "nightly-test"`
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListTestsRequest = ListTestsRequest

@typing.final
class ListTestsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TESTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListTestsRequest.page_size], use `next_page_token` as the value
    for the [ListTestsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def tests(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.loadtesting.api.v1.test.test_pb2.Test]:
        """List of tests in the specified folder."""

    def __init__(
        self,
        *,
        tests: collections.abc.Iterable[yandex.cloud.loadtesting.api.v1.test.test_pb2.Test] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "tests", b"tests"]) -> None: ...

global___ListTestsResponse = ListTestsResponse