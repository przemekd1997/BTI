# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import game_service_pb2 as game__service__pb2


class TTTStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JoinMatchmaking = channel.unary_unary(
                '/protos.TTT/JoinMatchmaking',
                request_serializer=game__service__pb2.New_game.SerializeToString,
                response_deserializer=game__service__pb2.Game.FromString,
                )
        self.Matchmaking_Ready = channel.unary_unary(
                '/protos.TTT/Matchmaking_Ready',
                request_serializer=game__service__pb2.New_game_status.SerializeToString,
                response_deserializer=game__service__pb2.Status.FromString,
                )
        self.End_Turn = channel.unary_unary(
                '/protos.TTT/End_Turn',
                request_serializer=game__service__pb2.Forward_to_server.SerializeToString,
                response_deserializer=game__service__pb2.Status.FromString,
                )
        self.Next_Turn_Status = channel.unary_unary(
                '/protos.TTT/Next_Turn_Status',
                request_serializer=game__service__pb2.Game_status.SerializeToString,
                response_deserializer=game__service__pb2.Status.FromString,
                )
        self.Next_Turn = channel.unary_unary(
                '/protos.TTT/Next_Turn',
                request_serializer=game__service__pb2.Next_Turn_Info.SerializeToString,
                response_deserializer=game__service__pb2.Forward_to_player.FromString,
                )
        self.Test_Clear_Game = channel.unary_unary(
                '/protos.TTT/Test_Clear_Game',
                request_serializer=game__service__pb2.Status.SerializeToString,
                response_deserializer=game__service__pb2.Status.FromString,
                )


class TTTServicer(object):
    """Missing associated documentation comment in .proto file."""

    def JoinMatchmaking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Matchmaking_Ready(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def End_Turn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Next_Turn_Status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Next_Turn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Test_Clear_Game(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TTTServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JoinMatchmaking': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinMatchmaking,
                    request_deserializer=game__service__pb2.New_game.FromString,
                    response_serializer=game__service__pb2.Game.SerializeToString,
            ),
            'Matchmaking_Ready': grpc.unary_unary_rpc_method_handler(
                    servicer.Matchmaking_Ready,
                    request_deserializer=game__service__pb2.New_game_status.FromString,
                    response_serializer=game__service__pb2.Status.SerializeToString,
            ),
            'End_Turn': grpc.unary_unary_rpc_method_handler(
                    servicer.End_Turn,
                    request_deserializer=game__service__pb2.Forward_to_server.FromString,
                    response_serializer=game__service__pb2.Status.SerializeToString,
            ),
            'Next_Turn_Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Next_Turn_Status,
                    request_deserializer=game__service__pb2.Game_status.FromString,
                    response_serializer=game__service__pb2.Status.SerializeToString,
            ),
            'Next_Turn': grpc.unary_unary_rpc_method_handler(
                    servicer.Next_Turn,
                    request_deserializer=game__service__pb2.Next_Turn_Info.FromString,
                    response_serializer=game__service__pb2.Forward_to_player.SerializeToString,
            ),
            'Test_Clear_Game': grpc.unary_unary_rpc_method_handler(
                    servicer.Test_Clear_Game,
                    request_deserializer=game__service__pb2.Status.FromString,
                    response_serializer=game__service__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.TTT', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TTT(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def JoinMatchmaking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.TTT/JoinMatchmaking',
            game__service__pb2.New_game.SerializeToString,
            game__service__pb2.Game.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Matchmaking_Ready(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.TTT/Matchmaking_Ready',
            game__service__pb2.New_game_status.SerializeToString,
            game__service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def End_Turn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.TTT/End_Turn',
            game__service__pb2.Forward_to_server.SerializeToString,
            game__service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Next_Turn_Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.TTT/Next_Turn_Status',
            game__service__pb2.Game_status.SerializeToString,
            game__service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Next_Turn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.TTT/Next_Turn',
            game__service__pb2.Next_Turn_Info.SerializeToString,
            game__service__pb2.Forward_to_player.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Test_Clear_Game(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.TTT/Test_Clear_Game',
            game__service__pb2.Status.SerializeToString,
            game__service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
