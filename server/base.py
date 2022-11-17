#python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./game_service.proto 
import firebase_admin
from battle import Battle
from defines import Stats, Cost
from firebase_admin import credentials
from firebase_admin import firestore
import game_service_pb2
import random
import numpy as np
import string

class Base:
    def __init__(self, file):
        self.cred = credentials.Certificate(file)
        self.default_app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        self.battle = Battle()
        self.cost = Cost()
        self.unit_stat = Stats()

    def create_game(self):
        while True:
            s = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
            print (s)
            ref =  self.db.collection(s)
            doc_ref = ref.document(u'General')
            doc = doc_ref.get()
            if not doc.exists:
                break

        data_user = {
        u'gold' : 300,
        u'tech' : 300,
        u'unit_stats': {
            u'footman_hp' : self.unit_stat.footman_hp,
            u'footman_armor' : self.unit_stat.footman_armor,
            u'footman_damage_min' : self.unit_stat.footman_damage_min,
            u'footman_damage_max' : self.unit_stat.footman_damage_max,
            u'footman_speed' : self.unit_stat.footman_speed,
            u'archer_hp' : self.unit_stat.archer_hp,
            u'archer_armor' : self.unit_stat.archer_armor,
            u'archer_damage_min' : self.unit_stat.archer_damage_min,
            u'archer_damage_max' : self.unit_stat.archer_damage_max,
            u'archer_hp' : self.unit_stat.archer_hp,
            u'archer_speed' : self.unit_stat.archer_speed,
            u'cavalry_hp' : self.unit_stat.cavalry_hp,
            u'cavalry_armor' : self.unit_stat.cavalry_armor,
            u'cavalry_damage_min' : self.unit_stat.cavalry_damage_min,
            u'cavalry_damage_max' : self.unit_stat.cavalry_damage_max,
            u'cavalry_speed' : self.unit_stat.cavalry_speed
            },
        u'units': {
            u'7' : [0,0,0],
            u'6' : [0,0,0],
            u'5' : [0,0,0],
            u'4' : [0,0,0],
            u'3' : [0,0,0],
            u'2' : [0,0,0],
            u'1' : [0,0,0],
            u'0' : [0,0,0]
            },
        u'upgrades': {
            u'tech' : 1,
            u'gold' : 1,
            u'foot_att' : 1,
            u'foot_def' : 1,
            u'arch_att' : 1,
            u'arch_def' : 1,
            u'cav_att' : 1,
            u'cav_def' : 1
            }
        }
        data_general = {
            u'day' : 1,
            u'war' : False,
            u'tot' : 5,
            u'no_players_ready' : 0,
            u'field' : 3,
            u'winner' : 0
        }
        print("tworze gre")
        ref.document(u'General').set(data_general)
        ref.document('Player1').set(data_user)
        return ref.id

    def add_to_game(self,game):
        ref =  self.db.collection(game)
        data_user = {
        u'gold' : 300,
        u'tech' : 300,
        u'unit_stats': {
            u'footman_hp' : self.unit_stat.footman_hp,
            u'footman_armor' : self.unit_stat.footman_armor,
            u'footman_damage_min' : self.unit_stat.footman_damage_min,
            u'footman_damage_max' : self.unit_stat.footman_damage_max,
            u'footman_speed' : self.unit_stat.footman_speed,
            u'archer_hp' : self.unit_stat.archer_hp,
            u'archer_armor' : self.unit_stat.archer_armor,
            u'archer_damage_min' : self.unit_stat.archer_damage_min,
            u'archer_damage_max' : self.unit_stat.archer_damage_max,
            u'archer_hp' : self.unit_stat.archer_hp,
            u'archer_speed' : self.unit_stat.archer_speed,
            u'cavalry_hp' : self.unit_stat.cavalry_hp,
            u'cavalry_armor' : self.unit_stat.cavalry_armor,
            u'cavalry_damage_min' : self.unit_stat.cavalry_damage_min,
            u'cavalry_damage_max' : self.unit_stat.cavalry_damage_max,
            u'cavalry_speed' : self.unit_stat.cavalry_speed
            },
        u'units': {
            u'0' : [0,0,0],
            u'1' : [0,0,0],
            u'2' : [0,0,0],
            u'3' : [0,0,0],
            u'4' : [0,0,0],
            u'5' : [0,0,0],
            u'6' : [0,0,0],
            u'7' : [0,0,0]
            },
        u'upgrades': {
            u'tech' : 1,
            u'gold' : 1,
            u'foot_att' : 1,
            u'foot_def' : 1,
            u'arch_att' : 1,
            u'arch_def' : 1,
            u'cav_att' : 1,
            u'cav_def' : 1
            }
        }
        ref.document('Player2').set(data_user)
    
    def update_player(self,request):
        print(request)
        ref =  self.db.collection(request.name).document("Player"+str(request.player))
        board = ref.get().to_dict()
        print("update player")
        if "next" in board:
            print("next in board")
            return 0
        else:
            data = {
                u'next' : {
                    u'gold_up' : request.gold_up,
                    u'tech_up' : request.tech_up,
                    u'gold' : request.gold,
                    u'tech' : request.tech,
                    u'up_foot_att' : request.up_foot_att,
                    u'up_foot_def' : request.up_foot_def,
                    u'up_arch_att' : request.up_arch_att,
                    u'up_arch_def' : request.up_arch_def,
                    u'up_cav_att' : request.up_cav_att,
                    u'up_cav_def' : request.up_cav_def,
                    u'foot' : request.foot,
                    u'arch' : request.arch,
                    u'cav' : request.cav
                }
            }
            ref.set(data, merge=True)
            ref = self.db.collection(request.name).document(u'General')
            gen = ref.get().to_dict()
            gen = gen['no_players_ready']
            if gen < 1:
                ref.update({u'no_players_ready' : gen + 1})
                return 1
            else:
                self.next_turn_calc(request.name)
                return 1

    def player_turn_status(self,request):
        ref =  self.db.collection(request.gid).document(u'General')
        gen = ref.get().to_dict()
        day = int(gen['day'])
        pr = int(gen['no_players_ready'])
        if day == request.day + 1 and pr == 0:
            print("tu")
            return 1
        else:
            return 0
    def next_turn_calc(self,gid):
        ref = self.db.collection(gid).document(u'General')
        gen = ref.get().to_dict()
        war = gen['war']
        winner = gen['winner']
        if war == False:
            new_tot = gen['tot'] - 1
            if new_tot == 0:
                new_war = True
            else:
                new_war = False
        else:
            new_tot = gen['tot']
            new_war = war
        ref_p1 = self.db.collection(gid).document(u'Player1')
        player1 = ref_p1.get().to_dict()
        ref_p2 = self.db.collection(gid).document(u'Player2')
        player2 = ref_p2.get().to_dict()

        new_field = gen['field']

        p1_upgrades, p2_upgrades = self.battle.update_tech(player1,player2,self.unit_stat)
        if new_war == True:
            status, p1, p2 = self.battle.battle(player1,player2,new_field)
            #print("stat: {} \np1: {} \np2: {}".format(status,p1,p2))
            if status == 1:
                if new_field == 0:
                    winner = 1
                else:
                    player1['units'][str(new_field+1)] = [0,0,0]
                    player2['units'][str(new_field)] = [0,0,0]
                    new_field -= 1
                    player1['units'][str(new_field+1)] = p1
                    player2['units'][str(new_field)] = np.add(p2,player2['units'][str(new_field)]).tolist()
                    new_war = False
                    new_tot = 5
            elif status == 2:
                if new_field == 6:
                    winner = 2
                else:
                    player1['units'][str(new_field+1)] = [0,0,0]
                    player2['units'][str(new_field)] = [0,0,0]
                    new_field += 1
                    player2['units'][str(new_field)] = p2
                    player1['units'][str(new_field+1)] = np.add(p1,player1['units'][str(new_field+1)]).tolist()
                    new_war = False
                    new_tot = 5
            else:
                player1['units'][str(new_field+1)] = p1
                player2['units'][str(new_field)] = p2

        p1_units, p2_units = self.battle.move_units(player1,player2,new_field)
        p1_upgrades['units'] = p1_units
        p2_upgrades['units'] = p2_units
        
        ref.update({
            u'no_players_ready' : 0,
            u'tot' : new_tot,
            u'war' : new_war,
            u'day' : gen['day'] + 1,
            u'field' : new_field,
            u'winner' : winner
        })
        ref_p1.update(p1_upgrades)
        ref_p2.update(p2_upgrades)

    def send_next_turn(self,request):
        ref =  self.db.collection(request.gid)
        pid = request.player
        if pid == 1:
            eid = '2'
        else:
            eid = '1'
        general = ref.document(u'General').get().to_dict()
        player = ref.document("Player" + str(pid)).get().to_dict()
        upgrades = player['upgrades']
        stats = player['unit_stats']
        units = player['units']
        enemy = ref.document("Player" + str(eid)).get().to_dict()
        enemy_units = enemy['units']

        response = game_service_pb2.Forward_to_player()

        response.day = general['day']
        field = general['field']
        if pid == 1:
            response.field = 6 - field
        else:
            response.field = field
        response.war = general['war']
        response.gold = player['gold'] + 100 + (upgrades['gold'] * self.cost.pl_gold_tech)
        response.tech = player['tech'] + 100 + (upgrades['tech'] * self.cost.pl_tech_gold)
        response.foot_att_min = stats['footman_damage_min']
        response.foot_att_max = stats['footman_damage_max']
        response.foot_armor = stats['footman_armor']
        response.arch_att_min = stats['archer_damage_min']
        response.arch_att_max = stats['archer_damage_max']
        response.arch_armor = stats['archer_armor']
        response.cav_att_min = stats['cavalry_damage_min']
        response.cav_att_max = stats['cavalry_damage_max']
        response.cav_armor = stats['cavalry_armor']
        response.winner = general['winner']

        temp_list = []
        if pid == 1:
            temp_list.extend(enemy_units[str(field)])
        else:
            temp_list.extend(enemy_units[str(field+1)])
        response.enemy.extend(temp_list)

        temp_list = []
        if pid == 2:
            for i in range(8):
                temp_list.extend(units[str(i)])
        else:
            for i in range(7,-1,-1):
                temp_list.extend(units[str(i)])
        response.player.extend(temp_list)
        return response
    
    def test_clear(self):
        ref =  self.db.collection("test")
        ref.document('General').delete()
        ref.document('Player1').delete()
        ref.document('Player2').delete()
        data_user = {
        u'gold' : 300,
        u'tech' : 300,
        u'unit_stats': {
            u'footman_hp' : self.unit_stat.footman_hp,
            u'footman_armor' : self.unit_stat.footman_armor,
            u'footman_damage_min' : self.unit_stat.footman_damage_min,
            u'footman_damage_max' : self.unit_stat.footman_damage_max,
            u'footman_speed' : self.unit_stat.footman_speed,
            u'archer_hp' : self.unit_stat.archer_hp,
            u'archer_armor' : self.unit_stat.archer_armor,
            u'archer_damage_min' : self.unit_stat.archer_damage_min,
            u'archer_damage_max' : self.unit_stat.archer_damage_max,
            u'archer_hp' : self.unit_stat.archer_hp,
            u'archer_speed' : self.unit_stat.archer_speed,
            u'cavalry_hp' : self.unit_stat.cavalry_hp,
            u'cavalry_armor' : self.unit_stat.cavalry_armor,
            u'cavalry_damage_min' : self.unit_stat.cavalry_damage_min,
            u'cavalry_damage_max' : self.unit_stat.cavalry_damage_max,
            u'cavalry_speed' : self.unit_stat.cavalry_speed
            },
        u'units': {
            u'0' : [0,0,0],
            u'1' : [0,0,0],
            u'2' : [0,0,0],
            u'3' : [0,0,0],
            u'4' : [0,0,0],
            u'5' : [0,0,0],
            u'6' : [0,0,0],
            u'7' : [0,0,0]
            },
        u'upgrades': {
            u'tech' : 1,
            u'gold' : 1,
            u'foot_att' : 1,
            u'foot_def' : 1,
            u'arch_att' : 1,
            u'arch_def' : 1,
            u'cav_att' : 1,
            u'cav_def' : 1
            }
        }
        data_general = {
            u'day' : 1,
            u'war' : False,
            u'tot' : 5,
            u'no_players_ready' : 0,
            u'field' : 3,
            u'winner' : 0
        }
        ref.document('General').set(data_general)
        ref.document('Player1').set(data_user)
        ref.document('Player2').set(data_user)

#TESTING
#base = Base("./mg-db-4251d-firebase-adminsdk-qdwkt-92102e2f75.json")

def test_add_next(pl):
    message = game_service_pb2.Forward_to_server()
    message.gold_up = 1
    message.tech_up = 0
    message.gold = 10
    message.tech = 10
    message.up_foot_att = 1
    message.up_foot_def = 0
    message.up_arch_att = 1
    message.up_arch_def = 0
    message.up_cav_att = 1
    message.up_cav_def = 0
    message.name = "test"
    message.player = pl
    message.foot = 20
    message.arch = 10
    message.cav = 5
    base.update_player(message)
#message = game_service_pb2.Next_Turn_Info(gid = "test", player = 1)
#print(base.send_next_turn(message))

#test_add_next(1)
#test_add_next(2)
#base.next_turn_calc('test')
#base.add_to_game("test")