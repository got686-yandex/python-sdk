# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.video.v1 import playlist_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_playlist__pb2
from yandex.cloud.video.v1 import playlist_service_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2


class PlaylistServiceStub(object):
    """Playlist management service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.video.v1.PlaylistService/Get',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.GetPlaylistRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__pb2.Playlist.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.video.v1.PlaylistService/List',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.ListPlaylistsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.ListPlaylistsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.video.v1.PlaylistService/Create',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.CreatePlaylistRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.video.v1.PlaylistService/Update',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.UpdatePlaylistRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.video.v1.PlaylistService/Delete',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.DeletePlaylistRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.BatchDelete = channel.unary_unary(
                '/yandex.cloud.video.v1.PlaylistService/BatchDelete',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.BatchDeletePlaylistsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.GetPlayerURL = channel.unary_unary(
                '/yandex.cloud.video.v1.PlaylistService/GetPlayerURL',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.GetPlaylistPlayerURLRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.GetPlaylistPlayerURLResponse.FromString,
                )


class PlaylistServiceServicer(object):
    """Playlist management service.
    """

    def Get(self, request, context):
        """Returns the specific playlist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List playlists for a channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Create playlist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update playlist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete playlist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchDelete(self, request, context):
        """Batch delete playlist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlayerURL(self, request, context):
        """Returns player's url.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlaylistServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.GetPlaylistRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__pb2.Playlist.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.ListPlaylistsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.ListPlaylistsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.CreatePlaylistRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.UpdatePlaylistRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.DeletePlaylistRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'BatchDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchDelete,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.BatchDeletePlaylistsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetPlayerURL': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlayerURL,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.GetPlaylistPlayerURLRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.GetPlaylistPlayerURLResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.video.v1.PlaylistService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PlaylistService(object):
    """Playlist management service.
    """

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.PlaylistService/Get',
            yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.GetPlaylistRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_playlist__pb2.Playlist.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.PlaylistService/List',
            yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.ListPlaylistsRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.ListPlaylistsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.PlaylistService/Create',
            yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.CreatePlaylistRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.PlaylistService/Update',
            yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.UpdatePlaylistRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.PlaylistService/Delete',
            yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.DeletePlaylistRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.PlaylistService/BatchDelete',
            yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.BatchDeletePlaylistsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPlayerURL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.video.v1.PlaylistService/GetPlayerURL',
            yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.GetPlaylistPlayerURLRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_playlist__service__pb2.GetPlaylistPlayerURLResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
