"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.operation.operation_pb2
import yandex.cloud.smartcaptcha.v1.captcha_pb2
import yandex.cloud.smartcaptcha.v1.captcha_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class CaptchaServiceStub:
    """A set of methods for managing Captcha resources."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.GetCaptchaRequest,
        yandex.cloud.smartcaptcha.v1.captcha_pb2.Captcha,
    ]
    """Returns the specified Captcha resource."""

    GetSecretKey: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.GetCaptchaRequest,
        yandex.cloud.smartcaptcha.v1.captcha_pb2.CaptchaSecretKey,
    ]
    """Returns the secret data of specified Captcha resource."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.ListCaptchasRequest,
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.ListCaptchasResponse,
    ]
    """Retrieves the list of Captcha resources in the specified folder."""

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.CreateCaptchaRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a captcha in the specified folder using the data specified in the request."""

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.UpdateCaptchaRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified captcha."""

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.DeleteCaptchaRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified captcha."""

class CaptchaServiceAsyncStub:
    """A set of methods for managing Captcha resources."""

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.GetCaptchaRequest,
        yandex.cloud.smartcaptcha.v1.captcha_pb2.Captcha,
    ]
    """Returns the specified Captcha resource."""

    GetSecretKey: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.GetCaptchaRequest,
        yandex.cloud.smartcaptcha.v1.captcha_pb2.CaptchaSecretKey,
    ]
    """Returns the secret data of specified Captcha resource."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.ListCaptchasRequest,
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.ListCaptchasResponse,
    ]
    """Retrieves the list of Captcha resources in the specified folder."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.CreateCaptchaRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a captcha in the specified folder using the data specified in the request."""

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.UpdateCaptchaRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates the specified captcha."""

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.smartcaptcha.v1.captcha_service_pb2.DeleteCaptchaRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes the specified captcha."""

class CaptchaServiceServicer(metaclass=abc.ABCMeta):
    """A set of methods for managing Captcha resources."""

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.smartcaptcha.v1.captcha_service_pb2.GetCaptchaRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.smartcaptcha.v1.captcha_pb2.Captcha, collections.abc.Awaitable[yandex.cloud.smartcaptcha.v1.captcha_pb2.Captcha]]:
        """Returns the specified Captcha resource."""

    @abc.abstractmethod
    def GetSecretKey(
        self,
        request: yandex.cloud.smartcaptcha.v1.captcha_service_pb2.GetCaptchaRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.smartcaptcha.v1.captcha_pb2.CaptchaSecretKey, collections.abc.Awaitable[yandex.cloud.smartcaptcha.v1.captcha_pb2.CaptchaSecretKey]]:
        """Returns the secret data of specified Captcha resource."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.smartcaptcha.v1.captcha_service_pb2.ListCaptchasRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.smartcaptcha.v1.captcha_service_pb2.ListCaptchasResponse, collections.abc.Awaitable[yandex.cloud.smartcaptcha.v1.captcha_service_pb2.ListCaptchasResponse]]:
        """Retrieves the list of Captcha resources in the specified folder."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.smartcaptcha.v1.captcha_service_pb2.CreateCaptchaRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a captcha in the specified folder using the data specified in the request."""

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.smartcaptcha.v1.captcha_service_pb2.UpdateCaptchaRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates the specified captcha."""

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.smartcaptcha.v1.captcha_service_pb2.DeleteCaptchaRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes the specified captcha."""

def add_CaptchaServiceServicer_to_server(servicer: CaptchaServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...