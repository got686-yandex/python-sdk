# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yandex.cloud.iam.v1.awscompatibility import access_key_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__pb2
from yandex.cloud.iam.v1.awscompatibility import access_key_service_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2


class AccessKeyServiceStub(object):
  """A set of methods for managing access keys.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.List = channel.unary_unary(
        '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/List',
        request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeysRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeysResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Get',
        request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.GetAccessKeyRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__pb2.AccessKey.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Create',
        request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.CreateAccessKeyRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.CreateAccessKeyResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.iam.v1.awscompatibility.AccessKeyService/Delete',
        request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.DeleteAccessKeyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class AccessKeyServiceServicer(object):
  """A set of methods for managing access keys.
  """

  def List(self, request, context):
    """Retrieves the list of access keys for the specified service account.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Returns the specified access key.

    To get the list of available access keys, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates an access key for the specified service account.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified access key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AccessKeyServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeysRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.ListAccessKeysResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.GetAccessKeyRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__pb2.AccessKey.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.CreateAccessKeyRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.CreateAccessKeyResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_awscompatibility_dot_access__key__service__pb2.DeleteAccessKeyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.iam.v1.awscompatibility.AccessKeyService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
