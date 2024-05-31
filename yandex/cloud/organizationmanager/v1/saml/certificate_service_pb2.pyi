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
import yandex.cloud.organizationmanager.v1.saml.certificate_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    certificate_id: builtins.str
    """ID of the certificate to return.
    To get the certificate ID, make a [CertificateService.List] request.
    """
    def __init__(
        self,
        *,
        certificate_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificate_id", b"certificate_id"]) -> None: ...

global___GetCertificateRequest = GetCertificateRequest

@typing.final
class ListCertificatesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to list certificates in.
    To get the federation ID make a [yandex.cloud.organizationmanager.v1.saml.FederationService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListCertificatesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token]
    to the [ListCertificatesResponse.next_page_token]
    returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters resources listed in the response.
    The expression must specify:
    1. The field name. Currently you can use filtering only on [Certificate.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["federation_id", b"federation_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListCertificatesRequest = ListCertificatesRequest

@typing.final
class ListCertificatesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListCertificatesRequest.page_size], use
    the [next_page_token] as the value
    for the [ListCertificatesRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def certificates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.organizationmanager.v1.saml.certificate_pb2.Certificate]:
        """List of certificates."""

    def __init__(
        self,
        *,
        certificates: collections.abc.Iterable[yandex.cloud.organizationmanager.v1.saml.certificate_pb2.Certificate] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificates", b"certificates", "next_page_token", b"next_page_token"]) -> None: ...

global___ListCertificatesResponse = ListCertificatesResponse

@typing.final
class CreateCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEDERATION_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    federation_id: builtins.str
    """ID of the federation to add new certificate.
    To get the federation ID make a [yandex.cloud.organizationmanager.v1.saml.FederationService.List] request.
    """
    name: builtins.str
    """Name of the certificate.
    The name must be unique within the federation.
    """
    description: builtins.str
    """Description of the certificate."""
    data: builtins.str
    """Certificate data in PEM format."""
    def __init__(
        self,
        *,
        federation_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        data: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data", b"data", "description", b"description", "federation_id", b"federation_id", "name", b"name"]) -> None: ...

global___CreateCertificateRequest = CreateCertificateRequest

@typing.final
class CreateCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    certificate_id: builtins.str
    """ID of the certificate that is being created."""
    def __init__(
        self,
        *,
        certificate_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificate_id", b"certificate_id"]) -> None: ...

global___CreateCertificateMetadata = CreateCertificateMetadata

@typing.final
class UpdateCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    certificate_id: builtins.str
    """ID of the certificate to update.
    To get the certificate ID, make a [CertificateService.List] request.
    """
    name: builtins.str
    """Name of the certificate.
    The name must be unique within the federation.
    """
    description: builtins.str
    """Description of the certificate."""
    data: builtins.str
    """Certificate data in PEM format."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the certificate are going to be updated."""

    def __init__(
        self,
        *,
        certificate_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        data: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["certificate_id", b"certificate_id", "data", b"data", "description", b"description", "name", b"name", "update_mask", b"update_mask"]) -> None: ...

global___UpdateCertificateRequest = UpdateCertificateRequest

@typing.final
class UpdateCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    certificate_id: builtins.str
    """ID of the certificate that is being updated."""
    def __init__(
        self,
        *,
        certificate_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificate_id", b"certificate_id"]) -> None: ...

global___UpdateCertificateMetadata = UpdateCertificateMetadata

@typing.final
class DeleteCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    certificate_id: builtins.str
    """ID of the certificate to delete.
    To get the certificate ID, make a [CertificateService.List] request.
    """
    def __init__(
        self,
        *,
        certificate_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificate_id", b"certificate_id"]) -> None: ...

global___DeleteCertificateRequest = DeleteCertificateRequest

@typing.final
class DeleteCertificateMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    certificate_id: builtins.str
    """ID of the certificate that is being deleted."""
    def __init__(
        self,
        *,
        certificate_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificate_id", b"certificate_id"]) -> None: ...

global___DeleteCertificateMetadata = DeleteCertificateMetadata

@typing.final
class ListCertificateOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    certificate_id: builtins.str
    """ID of the certificate to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListCertificateOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token]
    to the [ListCertificateOperationsResponse.next_page_token]
    returned by a previous list request.
    """
    def __init__(
        self,
        *,
        certificate_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificate_id", b"certificate_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListCertificateOperationsRequest = ListCertificateOperationsRequest

@typing.final
class ListCertificateOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListCertificateOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListCertificateOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified certificate."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListCertificateOperationsResponse = ListCertificateOperationsResponse