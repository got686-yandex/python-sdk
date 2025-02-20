# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.ai.assistants.v1.searchindex import search_index_file_pb2 as yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__pb2
from yandex.cloud.ai.assistants.v1.searchindex import search_index_file_service_pb2 as yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in yandex/cloud/ai/assistants/v1/searchindex/search_index_file_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SearchIndexFileServiceStub(object):
    """SearchIndexFileService provides operations for managing files within search indexes.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BatchCreate = channel.unary_unary(
                '/yandex.cloud.ai.assistants.v1.searchindex.SearchIndexFileService/BatchCreate',
                request_serializer=yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.BatchCreateSearchIndexFileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/yandex.cloud.ai.assistants.v1.searchindex.SearchIndexFileService/Get',
                request_serializer=yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.GetSearchIndexFileRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__pb2.SearchIndexFile.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.ai.assistants.v1.searchindex.SearchIndexFileService/List',
                request_serializer=yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.ListSearchIndexFilesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.ListSearchIndexFilesResponse.FromString,
                _registered_method=True)


class SearchIndexFileServiceServicer(object):
    """SearchIndexFileService provides operations for managing files within search indexes.
    """

    def BatchCreate(self, request, context):
        """Creates multiple files within a search index in [asynchronous mode](/docs/foundation-models/concepts/#working-mode).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Retrieves details of a specific file that has been indexed within a search index.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List files that are indexed within a specific search index.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SearchIndexFileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BatchCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchCreate,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.BatchCreateSearchIndexFileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.GetSearchIndexFileRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__pb2.SearchIndexFile.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.ListSearchIndexFilesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.ListSearchIndexFilesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.assistants.v1.searchindex.SearchIndexFileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.ai.assistants.v1.searchindex.SearchIndexFileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SearchIndexFileService(object):
    """SearchIndexFileService provides operations for managing files within search indexes.
    """

    @staticmethod
    def BatchCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.ai.assistants.v1.searchindex.SearchIndexFileService/BatchCreate',
            yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.BatchCreateSearchIndexFileRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.ai.assistants.v1.searchindex.SearchIndexFileService/Get',
            yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.GetSearchIndexFileRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__pb2.SearchIndexFile.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.ai.assistants.v1.searchindex.SearchIndexFileService/List',
            yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.ListSearchIndexFilesRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_assistants_dot_v1_dot_searchindex_dot_search__index__file__service__pb2.ListSearchIndexFilesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
