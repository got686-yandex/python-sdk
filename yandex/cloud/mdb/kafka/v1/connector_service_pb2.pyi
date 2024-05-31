"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.mdb.kafka.v1.connector_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster the connector belongs to.

    To get this ID, make a [ClusterService.List] request.
    """
    connector_name: builtins.str
    """Name of the Apache Kafka® connector to return information about.

    To get this name, make a [ConnectorService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_name", b"connector_name"]) -> None: ...

global___GetConnectorRequest = GetConnectorRequest

@typing.final
class ListConnectorsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to list connectors in.

    To get this ID, make a [ClusterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return.

    If the number of available results is larger than [page_size], the API returns a [ListConnectorsResponse.next_page_token] that can be used to get the next page of results in the subsequent [ConnectorService.List] requests.
    """
    page_token: builtins.str
    """Page token that can be used to iterate through multiple pages of results.

    To get the next page of results, set [page_token] to the [ListConnectorsResponse.next_page_token] returned by the previous [ConnectorService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListConnectorsRequest = ListConnectorsRequest

@typing.final
class ListConnectorsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTORS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """The token that can be used to get the next page of results.

    If the number of results is larger than [ListConnectorsRequest.page_size], use the [next_page_token] as the value for the [ListConnectorsRequest.page_token] in the subsequent [ConnectorService.List] request to iterate through multiple pages of results.
    """
    @property
    def connectors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.kafka.v1.connector_pb2.Connector]:
        """List of Apache Kafka® Connectors."""

    def __init__(
        self,
        *,
        connectors: collections.abc.Iterable[yandex.cloud.mdb.kafka.v1.connector_pb2.Connector] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connectors", b"connectors", "next_page_token", b"next_page_token"]) -> None: ...

global___ListConnectorsResponse = ListConnectorsResponse

@typing.final
class CreateConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_SPEC_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to create the connector in.

    To get this ID, make a [ClusterService.List] request.
    """
    @property
    def connector_spec(self) -> yandex.cloud.mdb.kafka.v1.connector_pb2.ConnectorSpec:
        """Configuration of the connector to create."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_spec: yandex.cloud.mdb.kafka.v1.connector_pb2.ConnectorSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["connector_spec", b"connector_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_spec", b"connector_spec"]) -> None: ...

global___CreateConnectorRequest = CreateConnectorRequest

@typing.final
class CreateConnectorMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster the connector is being created in."""
    connector_name: builtins.str
    """Name of the Apache Kafka® connector that is being created."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_name", b"connector_name"]) -> None: ...

global___CreateConnectorMetadata = CreateConnectorMetadata

@typing.final
class UpdateConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    CONNECTOR_SPEC_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to update the connector in.

    To get this ID, make a [ClusterService.List] request.
    """
    connector_name: builtins.str
    """Name of the connector to update.

    To get this name, make a [ConnectorService.List] request.
    """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which settings of the connector should be updated."""

    @property
    def connector_spec(self) -> yandex.cloud.mdb.kafka.v1.connector_pb2.UpdateConnectorSpec:
        """Configuration of the connector to update."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_name: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        connector_spec: yandex.cloud.mdb.kafka.v1.connector_pb2.UpdateConnectorSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["connector_spec", b"connector_spec", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_name", b"connector_name", "connector_spec", b"connector_spec", "update_mask", b"update_mask"]) -> None: ...

global___UpdateConnectorRequest = UpdateConnectorRequest

@typing.final
class UpdateConnectorMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster the connector is being updated in."""
    connector_name: builtins.str
    """Name of the Apache Kafka® connector that is being updated."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_name", b"connector_name"]) -> None: ...

global___UpdateConnectorMetadata = UpdateConnectorMetadata

@typing.final
class DeleteConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to delete the connector from.

    To get this ID, make a [ClusterService.List] request.
    """
    connector_name: builtins.str
    """Name of the connector to delete.

    To get this name, make a [ConnectorService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_name", b"connector_name"]) -> None: ...

global___DeleteConnectorRequest = DeleteConnectorRequest

@typing.final
class DeleteConnectorMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster the connector is being deleted from."""
    connector_name: builtins.str
    """Name of the Apache Kafka® connector that is being deleted."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_name", b"connector_name"]) -> None: ...

global___DeleteConnectorMetadata = DeleteConnectorMetadata

@typing.final
class ResumeConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to resume the connector in.

    To get this ID, make a [ClusterService.List] request.
    """
    connector_name: builtins.str
    """Name of the Apache Kafka® connector to resume.

    To get this name, make a [ConnectorService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_name", b"connector_name"]) -> None: ...

global___ResumeConnectorRequest = ResumeConnectorRequest

@typing.final
class ResumeConnectorMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster the connector is being resumed in."""
    connector_name: builtins.str
    """Name of the Apache Kafka® connector that is beign resumed."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_name", b"connector_name"]) -> None: ...

global___ResumeConnectorMetadata = ResumeConnectorMetadata

@typing.final
class PauseConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster to pause the connector in.

    To get this ID, make a [ClusterService.List] request.
    """
    connector_name: builtins.str
    """Name of the Apache Kafka® connector to pause.

    To get this name, make a [ConnectorService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_name", b"connector_name"]) -> None: ...

global___PauseConnectorRequest = PauseConnectorRequest

@typing.final
class PauseConnectorMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CONNECTOR_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Apache Kafka® cluster the connector is being paused in."""
    connector_name: builtins.str
    """Name of the Apache Kafka® connector that is being paused."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        connector_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "connector_name", b"connector_name"]) -> None: ...

global___PauseConnectorMetadata = PauseConnectorMetadata