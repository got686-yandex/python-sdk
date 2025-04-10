"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.ai.assistants.v1.runs.run_pb2
import yandex.cloud.ai.assistants.v1.runs.run_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class RunServiceStub:
    """RunService provides operations for managing runs."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.CreateRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]
    """Create a new run for a given assistant and thread."""

    Listen: grpc.UnaryStreamMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListenRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent,
    ]
    """Listen to events from a specific run.
    If the run was created with `stream = false`, Listen will only respond with the final status of the run
    and will not stream partial messages or intermediate events.
    """

    Attach: grpc.StreamStreamMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.AttachRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent,
    ]
    """Bi-directional streaming method to interact with a specific run.
    Like `Listen`, `Attach` streams events from the run, but also allows clients to send events back.
    For example, it can be used to submit function call results when the run is waiting for user input.
    """

    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]
    """Retrieve details of a specific run by its ID."""

    GetLastByThread: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetLastRunByThreadRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]
    """Retrieves the most recent run for a specific thread."""

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsResponse,
    ]
    """List runs in a specific folder."""

    Submit: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.SubmitToRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.SubmitToRunResponse,
    ]
    """Submit event to run
    For example, submit function call results when the run is waiting for user input.
    """

class RunServiceAsyncStub:
    """RunService provides operations for managing runs."""

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.CreateRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]
    """Create a new run for a given assistant and thread."""

    Listen: grpc.aio.UnaryStreamMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListenRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent,
    ]
    """Listen to events from a specific run.
    If the run was created with `stream = false`, Listen will only respond with the final status of the run
    and will not stream partial messages or intermediate events.
    """

    Attach: grpc.aio.StreamStreamMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.AttachRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent,
    ]
    """Bi-directional streaming method to interact with a specific run.
    Like `Listen`, `Attach` streams events from the run, but also allows clients to send events back.
    For example, it can be used to submit function call results when the run is waiting for user input.
    """

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]
    """Retrieve details of a specific run by its ID."""

    GetLastByThread: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetLastRunByThreadRequest,
        yandex.cloud.ai.assistants.v1.runs.run_pb2.Run,
    ]
    """Retrieves the most recent run for a specific thread."""

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsResponse,
    ]
    """List runs in a specific folder."""

    Submit: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.SubmitToRunRequest,
        yandex.cloud.ai.assistants.v1.runs.run_service_pb2.SubmitToRunResponse,
    ]
    """Submit event to run
    For example, submit function call results when the run is waiting for user input.
    """

class RunServiceServicer(metaclass=abc.ABCMeta):
    """RunService provides operations for managing runs."""

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.CreateRunRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run]]:
        """Create a new run for a given assistant and thread."""

    @abc.abstractmethod
    def Listen(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListenRunRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent], collections.abc.AsyncIterator[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent]]:
        """Listen to events from a specific run.
        If the run was created with `stream = false`, Listen will only respond with the final status of the run
        and will not stream partial messages or intermediate events.
        """

    @abc.abstractmethod
    def Attach(
        self,
        request_iterator: _MaybeAsyncIterator[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.AttachRunRequest],
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent], collections.abc.AsyncIterator[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.StreamEvent]]:
        """Bi-directional streaming method to interact with a specific run.
        Like `Listen`, `Attach` streams events from the run, but also allows clients to send events back.
        For example, it can be used to submit function call results when the run is waiting for user input.
        """

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetRunRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run]]:
        """Retrieve details of a specific run by its ID."""

    @abc.abstractmethod
    def GetLastByThread(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.GetLastRunByThreadRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.runs.run_pb2.Run]]:
        """Retrieves the most recent run for a specific thread."""

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsResponse, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.ListRunsResponse]]:
        """List runs in a specific folder."""

    @abc.abstractmethod
    def Submit(
        self,
        request: yandex.cloud.ai.assistants.v1.runs.run_service_pb2.SubmitToRunRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.SubmitToRunResponse, collections.abc.Awaitable[yandex.cloud.ai.assistants.v1.runs.run_service_pb2.SubmitToRunResponse]]:
        """Submit event to run
        For example, submit function call results when the run is waiting for user input.
        """

def add_RunServiceServicer_to_server(servicer: RunServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
