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
import yandex.cloud.operation.operation_pb2
import yandex.cloud.serverless.eventrouter.v1.connector_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector to return."""
    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connector_id", b"connector_id"]) -> None: ...

global___GetConnectorRequest = GetConnectorRequest

@typing.final
class ListConnectorsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUS_ID_FIELD_NUMBER: builtins.int
    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    bus_id: builtins.str
    """ID of the bus to list connectors in."""
    folder_id: builtins.str
    """ID of the folder to list connectors in."""
    page_size: builtins.int
    """The maximum number of results per response."""
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    `next_page_token` returned by a previous list request.
    """
    filter: builtins.str
    """Supported fields for filter:
      name
      created_at
    """
    def __init__(
        self,
        *,
        bus_id: builtins.str = ...,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["bus_id", b"bus_id", "container_id", b"container_id", "folder_id", b"folder_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["bus_id", b"bus_id", "container_id", b"container_id", "filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["container_id", b"container_id"]) -> typing.Literal["bus_id", "folder_id"] | None: ...

global___ListConnectorsRequest = ListConnectorsRequest

@typing.final
class ListConnectorsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTORS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list of results."""
    @property
    def connectors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.serverless.eventrouter.v1.connector_pb2.Connector]:
        """List of connectors."""

    def __init__(
        self,
        *,
        connectors: collections.abc.Iterable[yandex.cloud.serverless.eventrouter.v1.connector_pb2.Connector] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connectors", b"connectors", "next_page_token", b"next_page_token"]) -> None: ...

global___ListConnectorsResponse = ListConnectorsResponse

@typing.final
class CreateConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
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

    BUS_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    bus_id: builtins.str
    """ID of the bus to create a connector in."""
    name: builtins.str
    """Name of the connector."""
    description: builtins.str
    """Description of the connector."""
    deletion_protection: builtins.bool
    """Flag that disallow deletion of the connector."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels for the connector."""

    @property
    def source(self) -> yandex.cloud.serverless.eventrouter.v1.connector_pb2.Source:
        """Source of the connector."""

    def __init__(
        self,
        *,
        bus_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        source: yandex.cloud.serverless.eventrouter.v1.connector_pb2.Source | None = ...,
        deletion_protection: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["source", b"source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["bus_id", b"bus_id", "deletion_protection", b"deletion_protection", "description", b"description", "labels", b"labels", "name", b"name", "source", b"source"]) -> None: ...

global___CreateConnectorRequest = CreateConnectorRequest

@typing.final
class CreateConnectorMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    BUS_ID_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector that is being created."""
    bus_id: builtins.str
    """ID of the bus that the connector is created in."""
    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
        bus_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["bus_id", b"bus_id", "connector_id", b"connector_id"]) -> None: ...

global___CreateConnectorMetadata = CreateConnectorMetadata

@typing.final
class UpdateConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
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

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector to update."""
    name: builtins.str
    """New name of the connector."""
    description: builtins.str
    """New description of the connector."""
    deletion_protection: builtins.bool
    """New flag that disallow deletion of the connector."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the connector are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """New labels of the connector."""

    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        deletion_protection: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["connector_id", b"connector_id", "deletion_protection", b"deletion_protection", "description", b"description", "labels", b"labels", "name", b"name", "update_mask", b"update_mask"]) -> None: ...

global___UpdateConnectorRequest = UpdateConnectorRequest

@typing.final
class UpdateConnectorMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector that is being updated."""
    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connector_id", b"connector_id"]) -> None: ...

global___UpdateConnectorMetadata = UpdateConnectorMetadata

@typing.final
class DeleteConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector to delete."""
    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connector_id", b"connector_id"]) -> None: ...

global___DeleteConnectorRequest = DeleteConnectorRequest

@typing.final
class DeleteConnectorMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector that is being deleted."""
    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connector_id", b"connector_id"]) -> None: ...

global___DeleteConnectorMetadata = DeleteConnectorMetadata

@typing.final
class ListConnectorOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector to list operations for."""
    page_size: builtins.int
    """The maximum number of results per response."""
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    `next_page_token` returned by a previous list request.
    """
    filter: builtins.str
    """Supported attributes for filter:
      description
      created_at
      modified_at
      created_by
      done
    """
    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connector_id", b"connector_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListConnectorOperationsRequest = ListConnectorOperationsRequest

@typing.final
class ListConnectorOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list of results."""
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified connector."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListConnectorOperationsResponse = ListConnectorOperationsResponse

@typing.final
class StartConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector to start."""
    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connector_id", b"connector_id"]) -> None: ...

global___StartConnectorRequest = StartConnectorRequest

@typing.final
class StartConnectorMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector that is being started."""
    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connector_id", b"connector_id"]) -> None: ...

global___StartConnectorMetadata = StartConnectorMetadata

@typing.final
class StopConnectorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector to stop."""
    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connector_id", b"connector_id"]) -> None: ...

global___StopConnectorRequest = StopConnectorRequest

@typing.final
class StopConnectorMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_ID_FIELD_NUMBER: builtins.int
    connector_id: builtins.str
    """ID of the connector that is being stopped."""
    def __init__(
        self,
        *,
        connector_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connector_id", b"connector_id"]) -> None: ...

global___StopConnectorMetadata = StopConnectorMetadata