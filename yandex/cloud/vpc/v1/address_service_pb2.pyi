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
import yandex.cloud.vpc.v1.address_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetAddressRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: builtins.str
    """ID of the Address resource to return.

    To get Address resource ID make a [AddressService.List] request.
    """
    def __init__(
        self,
        *,
        address_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address_id", b"address_id"]) -> None: ...

global___GetAddressRequest = GetAddressRequest

@typing.final
class GetAddressByValueRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXTERNAL_IPV4_ADDRESS_FIELD_NUMBER: builtins.int
    external_ipv4_address: builtins.str
    def __init__(
        self,
        *,
        external_ipv4_address: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["address", b"address", "external_ipv4_address", b"external_ipv4_address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "external_ipv4_address", b"external_ipv4_address"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["address", b"address"]) -> typing.Literal["external_ipv4_address"] | None: ...

global___GetAddressByValueRequest = GetAddressByValueRequest

@typing.final
class ListAddressesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to list addresses in.

    To get the folder ID use a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListAddressesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListAddressesResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters Address listed in the response.

    The expression must specify:
    1. The field name. Currently you can use filtering only on [Address.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    Example of a filter: `name=my-address`.
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

global___ListAddressesRequest = ListAddressesRequest

@typing.final
class ListAddressesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESSES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListAddressesRequest.page_size], use `next_page_token` as the value
    for the [ListAddressesRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def addresses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.vpc.v1.address_pb2.Address]:
        """List of addresses."""

    def __init__(
        self,
        *,
        addresses: collections.abc.Iterable[yandex.cloud.vpc.v1.address_pb2.Address] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["addresses", b"addresses", "next_page_token", b"next_page_token"]) -> None: ...

global___ListAddressesResponse = ListAddressesResponse

@typing.final
class CreateAddressRequest(google.protobuf.message.Message):
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

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    EXTERNAL_IPV4_ADDRESS_SPEC_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    DNS_RECORD_SPECS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """ID of the folder to create a address in.

    To get a folder ID make a [yandex.cloud.resourcemanager.v1.FolderService.List] request.
    """
    name: builtins.str
    """Name of the address.
    The name must be unique within the folder.
    """
    description: builtins.str
    """Description of the address."""
    deletion_protection: builtins.bool
    """Specifies if address protected from deletion."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Address labels as `key:value` pairs."""

    @property
    def external_ipv4_address_spec(self) -> global___ExternalIpv4AddressSpec: ...
    @property
    def dns_record_specs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DnsRecordSpec]:
        """Optional DNS record specifications"""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        external_ipv4_address_spec: global___ExternalIpv4AddressSpec | None = ...,
        deletion_protection: builtins.bool = ...,
        dns_record_specs: collections.abc.Iterable[global___DnsRecordSpec] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["address_spec", b"address_spec", "external_ipv4_address_spec", b"external_ipv4_address_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address_spec", b"address_spec", "deletion_protection", b"deletion_protection", "description", b"description", "dns_record_specs", b"dns_record_specs", "external_ipv4_address_spec", b"external_ipv4_address_spec", "folder_id", b"folder_id", "labels", b"labels", "name", b"name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["address_spec", b"address_spec"]) -> typing.Literal["external_ipv4_address_spec"] | None: ...

global___CreateAddressRequest = CreateAddressRequest

@typing.final
class ExternalIpv4AddressSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    ZONE_ID_FIELD_NUMBER: builtins.int
    REQUIREMENTS_FIELD_NUMBER: builtins.int
    address: builtins.str
    """Value of address.
    if unspecified, one will be automatically allocated from other params
    """
    zone_id: builtins.str
    """Availability zone from which the address will be allocated.
    only if address unspecified
    """
    @property
    def requirements(self) -> yandex.cloud.vpc.v1.address_pb2.AddressRequirements:
        """Parameters of the allocated address, for example DDoS Protection."""

    def __init__(
        self,
        *,
        address: builtins.str = ...,
        zone_id: builtins.str = ...,
        requirements: yandex.cloud.vpc.v1.address_pb2.AddressRequirements | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["requirements", b"requirements"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address", b"address", "requirements", b"requirements", "zone_id", b"zone_id"]) -> None: ...

global___ExternalIpv4AddressSpec = ExternalIpv4AddressSpec

@typing.final
class DnsRecordSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FQDN_FIELD_NUMBER: builtins.int
    DNS_ZONE_ID_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    PTR_FIELD_NUMBER: builtins.int
    fqdn: builtins.str
    """Required. DNS record name (absolute or relative to the DNS zone in use)."""
    dns_zone_id: builtins.str
    """Required. ID of the public DNS zone. The maximum string length in characters is 20."""
    ttl: builtins.int
    """TTL of record. Acceptable values are 0 to 86400, inclusive."""
    ptr: builtins.bool
    """Optional. If the PTR record is required, this parameter must be set to "true"."""
    def __init__(
        self,
        *,
        fqdn: builtins.str = ...,
        dns_zone_id: builtins.str = ...,
        ttl: builtins.int = ...,
        ptr: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dns_zone_id", b"dns_zone_id", "fqdn", b"fqdn", "ptr", b"ptr", "ttl", b"ttl"]) -> None: ...

global___DnsRecordSpec = DnsRecordSpec

@typing.final
class CreateAddressMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: builtins.str
    """ID of the address that is being created."""
    def __init__(
        self,
        *,
        address_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address_id", b"address_id"]) -> None: ...

global___CreateAddressMetadata = CreateAddressMetadata

@typing.final
class UpdateAddressRequest(google.protobuf.message.Message):
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

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    RESERVED_FIELD_NUMBER: builtins.int
    DELETION_PROTECTION_FIELD_NUMBER: builtins.int
    DNS_RECORD_SPECS_FIELD_NUMBER: builtins.int
    address_id: builtins.str
    """ID of the address to update.

    To get the address ID make a [AddressService.List] request.
    """
    name: builtins.str
    """New name for the address.
    The name must be unique within the folder.
    """
    description: builtins.str
    """New description of the address."""
    reserved: builtins.bool
    """Specifies if address is reserved or not."""
    deletion_protection: builtins.bool
    """Specifies if address protected from deletion."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which attributes of the Address should be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Address labels as `key:value` pairs.

        Existing set of labels is completely replaced by the provided set, so if you just want
        to add or remove a label:
        1. Get the current set of labels with a [AddressService.Get] request.
        2. Add or remove a label in this set.
        3. Send the new set in this field.
        """

    @property
    def dns_record_specs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DnsRecordSpec]:
        """Optional DNS record specifications"""

    def __init__(
        self,
        *,
        address_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        reserved: builtins.bool = ...,
        deletion_protection: builtins.bool = ...,
        dns_record_specs: collections.abc.Iterable[global___DnsRecordSpec] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["address_id", b"address_id", "deletion_protection", b"deletion_protection", "description", b"description", "dns_record_specs", b"dns_record_specs", "labels", b"labels", "name", b"name", "reserved", b"reserved", "update_mask", b"update_mask"]) -> None: ...

global___UpdateAddressRequest = UpdateAddressRequest

@typing.final
class UpdateAddressMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: builtins.str
    """ID of the Address that is being updated."""
    def __init__(
        self,
        *,
        address_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address_id", b"address_id"]) -> None: ...

global___UpdateAddressMetadata = UpdateAddressMetadata

@typing.final
class DeleteAddressRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: builtins.str
    """ID of the address to delete.

    To get a address ID make a [AddressService.List] request.
    """
    def __init__(
        self,
        *,
        address_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address_id", b"address_id"]) -> None: ...

global___DeleteAddressRequest = DeleteAddressRequest

@typing.final
class DeleteAddressMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: builtins.str
    """ID of the address that is being deleted."""
    def __init__(
        self,
        *,
        address_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address_id", b"address_id"]) -> None: ...

global___DeleteAddressMetadata = DeleteAddressMetadata

@typing.final
class ListAddressOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    address_id: builtins.str
    """ID of the address to list operations for.

    To get a address ID make a [AddressService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListAddressOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListAddressOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        address_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address_id", b"address_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListAddressOperationsRequest = ListAddressOperationsRequest

@typing.final
class ListAddressOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListAddressOperationsRequest.page_size], use `next_page_token` as the value
    for the [ListAddressOperationsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified address."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListAddressOperationsResponse = ListAddressOperationsResponse

@typing.final
class MoveAddressRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    DESTINATION_FOLDER_ID_FIELD_NUMBER: builtins.int
    address_id: builtins.str
    """ID of the address that is being moved."""
    destination_folder_id: builtins.str
    """ID of the folder to move address to."""
    def __init__(
        self,
        *,
        address_id: builtins.str = ...,
        destination_folder_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address_id", b"address_id", "destination_folder_id", b"destination_folder_id"]) -> None: ...

global___MoveAddressRequest = MoveAddressRequest

@typing.final
class MoveAddressMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_ID_FIELD_NUMBER: builtins.int
    address_id: builtins.str
    """ID of the address that is being moved."""
    def __init__(
        self,
        *,
        address_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["address_id", b"address_id"]) -> None: ...

global___MoveAddressMetadata = MoveAddressMetadata