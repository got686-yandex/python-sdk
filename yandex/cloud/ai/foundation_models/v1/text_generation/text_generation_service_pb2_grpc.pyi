"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2
import yandex.cloud.operation.operation_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class TextGenerationServiceStub:
    """Service for text generation."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Completion: grpc.UnaryStreamMultiCallable[
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionRequest,
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionResponse,
    ]
    """A method for generating text completions in [synchronous mode](/docs/foundation-models/concepts/#working-mode)."""

class TextGenerationServiceAsyncStub:
    """Service for text generation."""

    Completion: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionRequest,
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionResponse,
    ]
    """A method for generating text completions in [synchronous mode](/docs/foundation-models/concepts/#working-mode)."""

class TextGenerationServiceServicer(metaclass=abc.ABCMeta):
    """Service for text generation."""

    @abc.abstractmethod
    def Completion(
        self,
        request: yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionResponse], collections.abc.AsyncIterator[yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionResponse]]:
        """A method for generating text completions in [synchronous mode](/docs/foundation-models/concepts/#working-mode)."""

def add_TextGenerationServiceServicer_to_server(servicer: TextGenerationServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

class TextGenerationAsyncServiceStub:
    """Service for asynchronous text generation."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Completion: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """A method for generating text completions in [asynchronous mode](/docs/foundation-models/concepts/#working-mode)."""

class TextGenerationAsyncServiceAsyncStub:
    """Service for asynchronous text generation."""

    Completion: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """A method for generating text completions in [asynchronous mode](/docs/foundation-models/concepts/#working-mode)."""

class TextGenerationAsyncServiceServicer(metaclass=abc.ABCMeta):
    """Service for asynchronous text generation."""

    @abc.abstractmethod
    def Completion(
        self,
        request: yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """A method for generating text completions in [asynchronous mode](/docs/foundation-models/concepts/#working-mode)."""

def add_TextGenerationAsyncServiceServicer_to_server(servicer: TextGenerationAsyncServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

class TextGenerationBatchServiceStub:
    """Service for text generation."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Completion: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.BatchCompletionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """A method for generating text completions in [synchronous mode](/docs/foundation-models/concepts/#working-mode).
    Note: Not implemented yet
    """

class TextGenerationBatchServiceAsyncStub:
    """Service for text generation."""

    Completion: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.BatchCompletionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """A method for generating text completions in [synchronous mode](/docs/foundation-models/concepts/#working-mode).
    Note: Not implemented yet
    """

class TextGenerationBatchServiceServicer(metaclass=abc.ABCMeta):
    """Service for text generation."""

    @abc.abstractmethod
    def Completion(
        self,
        request: yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.BatchCompletionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """A method for generating text completions in [synchronous mode](/docs/foundation-models/concepts/#working-mode).
        Note: Not implemented yet
        """

def add_TextGenerationBatchServiceServicer_to_server(servicer: TextGenerationBatchServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

class TokenizerServiceStub:
    """Service for tokenizing input content."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Tokenize: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeRequest,
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeResponse,
    ]
    """RPC method for tokenizing text."""

    TokenizeCompletion: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionRequest,
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeResponse,
    ]
    """RPC method for tokenizing content of CompletionRequest"""

class TokenizerServiceAsyncStub:
    """Service for tokenizing input content."""

    Tokenize: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeRequest,
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeResponse,
    ]
    """RPC method for tokenizing text."""

    TokenizeCompletion: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionRequest,
        yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeResponse,
    ]
    """RPC method for tokenizing content of CompletionRequest"""

class TokenizerServiceServicer(metaclass=abc.ABCMeta):
    """Service for tokenizing input content."""

    @abc.abstractmethod
    def Tokenize(
        self,
        request: yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeResponse, collections.abc.Awaitable[yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeResponse]]:
        """RPC method for tokenizing text."""

    @abc.abstractmethod
    def TokenizeCompletion(
        self,
        request: yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.CompletionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeResponse, collections.abc.Awaitable[yandex.cloud.ai.foundation_models.v1.text_generation.text_generation_service_pb2.TokenizeResponse]]:
        """RPC method for tokenizing content of CompletionRequest"""

def add_TokenizerServiceServicer_to_server(servicer: TokenizerServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
