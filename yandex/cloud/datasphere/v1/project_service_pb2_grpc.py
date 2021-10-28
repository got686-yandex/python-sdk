# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yandex.cloud.datasphere.v1 import project_pb2 as yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__pb2
from yandex.cloud.datasphere.v1 import project_service_pb2 as yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ProjectServiceStub(object):
    """A set of methods for managing Project resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Create',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CreateProjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Update',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.UpdateProjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Delete',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.DeleteProjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Open = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Open',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.OpenProjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Get = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Get',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetProjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__pb2.Project.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/List',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsResponse.FromString,
                )
        self.GetUnitBalance = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/GetUnitBalance',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetUnitBalanceRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetUnitBalanceResponse.FromString,
                )
        self.SetUnitBalance = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/SetUnitBalance',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.SetUnitBalanceRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Execute = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Execute',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ProjectExecutionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.GetCellOutputs = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/GetCellOutputs',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CellOutputsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CellOutputsResponse.FromString,
                )
        self.GetStateVariables = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/GetStateVariables',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetStateVariablesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetStateVariablesResponse.FromString,
                )
        self.GetNotebookMetadata = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/GetNotebookMetadata',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetNotebookMetadataRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetNotebookMetadataResponse.FromString,
                )


class ProjectServiceServicer(object):
    """A set of methods for managing Project resources.
    """

    def Create(self, request, context):
        """Creates a project in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Open(self, request, context):
        """Opens the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Returns the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Lists projects for the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUnitBalance(self, request, context):
        """Returns the unit balance of the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetUnitBalance(self, request, context):
        """Sets the unit balance of the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Execute(self, request, context):
        """Executes code in the specified cell or notebook.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCellOutputs(self, request, context):
        """Returns outputs of the specified cell.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStateVariables(self, request, context):
        """Returns state variables of the specified notebook.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNotebookMetadata(self, request, context):
        """Returns metadata of the specified notebook.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CreateProjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.UpdateProjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.DeleteProjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Open': grpc.unary_unary_rpc_method_handler(
                    servicer.Open,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.OpenProjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetProjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__pb2.Project.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsResponse.SerializeToString,
            ),
            'GetUnitBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUnitBalance,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetUnitBalanceRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetUnitBalanceResponse.SerializeToString,
            ),
            'SetUnitBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.SetUnitBalance,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.SetUnitBalanceRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Execute': grpc.unary_unary_rpc_method_handler(
                    servicer.Execute,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ProjectExecutionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetCellOutputs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCellOutputs,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CellOutputsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CellOutputsResponse.SerializeToString,
            ),
            'GetStateVariables': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStateVariables,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetStateVariablesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetStateVariablesResponse.SerializeToString,
            ),
            'GetNotebookMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNotebookMetadata,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetNotebookMetadataRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetNotebookMetadataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.datasphere.v1.ProjectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectService(object):
    """A set of methods for managing Project resources.
    """

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Create',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CreateProjectRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Update',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.UpdateProjectRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Delete',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.DeleteProjectRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Open(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Open',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.OpenProjectRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Get',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetProjectRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__pb2.Project.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/List',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUnitBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/GetUnitBalance',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetUnitBalanceRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetUnitBalanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetUnitBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/SetUnitBalance',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.SetUnitBalanceRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Execute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Execute',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ProjectExecutionRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCellOutputs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/GetCellOutputs',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CellOutputsRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CellOutputsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStateVariables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/GetStateVariables',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetStateVariablesRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetStateVariablesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNotebookMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/GetNotebookMetadata',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetNotebookMetadataRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetNotebookMetadataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
