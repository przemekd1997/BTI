import game_service_pb2
import game_service_pb2_grpc
import grpc
import time
import sys

def test_end_turn(n):
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = game_service_pb2_grpc.TTTStub(channel)
        message = game_service_pb2.Forward_to_server()
        message.gold_up = 0
        message.tech_up = 0
        message.gold = 0
        message.tech = 0
        message.up_foot_att = 0
        message.up_foot_def = 0
        message.up_arch_att = 0
        message.up_arch_def = 0
        message.up_cav_att = 0
        message.up_cav_def = 0
        message.foot = n
        message.arch = n
        message.cav = n
        message.name = "test"
        message.player = 2
    
        stub.End_Turn(message)
        print("poszedł forward")

def test_clear_game():
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = game_service_pb2_grpc.TTTStub(channel)
        message = game_service_pb2.Status()
        stub.Test_Clear_Game(message)
        print("wyczyszczono")


def test_get_turn():
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = game_service_pb2_grpc.TTTStub(channel)
        message = game_service_pb2.Next_Turn_Info(gid = "test", player = 1)
        status = stub.Next_Turn(message)
        print("poszedł forward")
        print(status)

if __name__ == '__main__':
    if int(sys.argv[1]) == 1:
        test_end_turn(0)
    elif int(sys.argv[1]) == 2:
        test_end_turn(int(sys.argv[2]))
    elif int(sys.argv[1]) == 0:
        test_clear_game()

    #test_get_turn()
