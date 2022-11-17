from base import Base
from concurrent import futures
import grpc
import game_service_pb2
import game_service_pb2_grpc
import threading
import time
import json

with open('config.txt') as f:
            data = f.read()
info = json.loads(data)
free_games = []
base = Base(info['base_driver'])

class Listener(game_service_pb2_grpc.TTTServicer):
    def __init__(self):
        self.data_base = base
        self.lock = threading.Lock()

    def JoinMatchmaking(self, request, context): 
        global free_games
        uid = request.name
        with self.lock:
            if (len(free_games) == 0):
                name = self.data_base.create_game()
                free_games.append(name)
                print("czekam na gre: " + str(uid))
                return game_service_pb2.Game(stat = 0, id = name, uid = 1)
            else:
                name = free_games.pop(0)
                print("dolaczylem sie: " + str(uid))
                self.data_base.add_to_game(name)
                return game_service_pb2.Game(stat = 1, id = name, uid = 2)
    
    def Matchmaking_Ready(self, request, context):
        global free_games
        gid = request.name
        if gid not in free_games:
            return game_service_pb2.Status(stat = 1)
        else:
            return game_service_pb2.Status(stat = 0)

    def End_Turn(self, request, context):
        print("Got end turn")
        status = self.data_base.update_player(request)
        return game_service_pb2.Status(stat = status)

    def Next_Turn_Status(self, request, context):
        print("check end turn")
        status = self.data_base.player_turn_status(request)
        return game_service_pb2.Status(stat = status)
    
    def Next_Turn(self, request, context):
        print("send next turn")
        response = self.data_base.send_next_turn(request)
        return response
    
    def Test_Clear_Game(self, request, context):
        self.data_base.test_clear()
        response = game_service_pb2.Status()
        return response
        

def server():
    configs = '[' + info['ip_address'] + ']:' + info['port']
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=info['threads']))
    game_service_pb2_grpc.add_TTTServicer_to_server(Listener(), server)
    server.add_insecure_port(configs)
    server.start()
    try:
        while True:
            print("server active: on threads %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("keyboard interrupt")
        server.stop(0)

if __name__ == "__main__":
    server()