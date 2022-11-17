from re import X
import firebase_admin
from firebase_admin import firestore
import numpy as np
import random
from math import ceil
from math import floor

class Battle:
    def __init__(self) -> None:
        pass
    
    def fight(self,p1_damage,p1_armor,p1_hp,p1_speed,p1_overkill,p1,p2_damage,p2_armor,p2_hp,p2_speed,p2_overkill,p2):
    
        print("p1b: {}  p2b{}".format(p1,p2))
        x = floor(p2_overkill - (p1_armor * p1)/p1_hp)
        y = floor(p1_overkill - (p2_armor * p2)/p2_hp)
        
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        p1 -= x
        p2 -= y
        

        if p1 < 0:
            p1 = 0
        if p2 < 0:
            p2 = 0
        
        print("p1a: {}  p2a{}".format(p1,p2))

        if p1_speed > p2_speed:
            p1_damage *= p1
            if p2_hp * p2 <= p1_damage:
                p1_overkill = p1_damage - (p2_hp * p2)
                p2 = 0
            else:
                p1_overkill = 0
                p2_hp_new = (p2_hp * p2) - p1_damage
                p2 = ceil(p2_hp_new/p2_hp)
                p2_damage *= p2
                if p1_hp * p1 <= p2_damage:
                    p2_overkill = p2_damage - (p1_hp * p1)
                    p1 = 0
                else:
                    p1_overkill = 0
                    p1_hp_new = (p1_hp * p1) - p2_damage
                    p1 = ceil(p1_hp_new/p1_hp)
        elif p1_speed == p2_speed:
            p1_damage *= p1
            p2_damage *= p2
            p1_damage -= (p2_armor * p2)
            p2_damage -= (p1_armor * p1)
            if p1_damage < 0:
                p1_damage = 0
            if p2_damage < 0:
                p2_damage = 0

            p2_hp_new = (p2_hp * p2) - p1_damage
            p1_hp_new = (p1_hp * p1) - p2_damage
            p1_overkill = 0
            p2_overkill = 0

            if p2_hp_new < 0:
                p1_overkill = p2_hp_new * -1
                p2_hp_new = 0
            if p1_hp_new < 0:
                p2_overkill = p1_hp_new * -1
                p1_hp_new = 0
            
            p1 = ceil(p1_hp_new/p1_hp)
            p2 = ceil(p2_hp_new/p2_hp)
        else:
            p2_damage *= p2
            if p1_hp * p1 <= p2_damage:
                p2_overkill = p2_damage - (p1_hp * p1)
                p1 = 0
            else:
                p2_overkill = 0
                p1_hp_new = (p1_hp * p1) - p2_damage
                p1 = ceil(p1_hp_new/p1_hp)
                p1_damage *= p1
                if p2_hp * p2 <= p1_damage:
                    p1_overkill = p1_damage - (p2_hp * p2)
                    p2 = 0
                else:
                    p2_overkill = 0
                    p2_hp_new = (p2_hp * p2) - p1_damage
                    p2 = ceil(p2_hp_new/p2_hp)

        return p1, p2, p1_overkill, p2_overkill





    def battle(self, player1, player2, field):
        p1 = player1['units'][str(field+1)]
        p2 = player2['units'][str(field)]
        #print("p1 {} \np2 {}".format(p1,p2))

        #cav damage
        p1_damage = random.randint(player1['unit_stats']['cavalry_damage_min'],player1['unit_stats']['cavalry_damage_max'] + 1)
        p1_armor = player1['unit_stats']['cavalry_armor']
        p1_hp = player1['unit_stats']['cavalry_hp']
        p1_speed = player1['unit_stats']['cavalry_speed']
        p1_overkill = 0
        p2_damage = random.randint(player2['unit_stats']['cavalry_damage_min'],player2['unit_stats']['cavalry_damage_max'] + 1)
        p2_armor = player2['unit_stats']['cavalry_armor']
        p2_hp = player2['unit_stats']['cavalry_hp']
        p2_speed = player2['unit_stats']['cavalry_speed']
        p2_overkill = 0
        print ("1: {}  2: {}  1o: {}  2o:  {}".format(p1[2], p2[2], p1_overkill, p2_overkill))
        p1[2], p2[2], p1_overkill, p2_overkill = self.fight(p1_damage,p1_armor,p1_hp,p1_speed,p1_overkill,p1[2],p2_damage,p2_armor,p2_hp,p2_speed,p2_overkill,p2[2])
        print ("1: {}  2: {}  1o: {}  2o:  {}".format(p1[2], p2[2], p1_overkill, p2_overkill))

        #archer damage
        p1_damage = random.randint(player1['unit_stats']['archer_damage_min'],player1['unit_stats']['archer_damage_max'] + 1)
        p1_armor = player1['unit_stats']['archer_armor']
        p1_hp = player1['unit_stats']['archer_hp']
        p1_speed = player1['unit_stats']['archer_speed']
        p2_damage = random.randint(player2['unit_stats']['archer_damage_min'],player2['unit_stats']['archer_damage_max'] + 1)
        p2_armor = player2['unit_stats']['archer_armor']
        p2_hp = player2['unit_stats']['archer_hp']
        p2_speed = player2['unit_stats']['archer_speed']
        print ("1: {}  2: {}  1o: {}  2o:  {}".format(p1[1], p2[1], p1_overkill, p2_overkill))
        p1[1], p2[1], p1_overkill, p2_overkill = self.fight(p1_damage,p1_armor,p1_hp,p1_speed,p1_overkill,p1[1],p2_damage,p2_armor,p2_hp,p2_speed,p2_overkill,p2[1])
        print ("1: {}  2: {}  1o: {}  2o:  {}".format(p1[1], p2[1], p1_overkill, p2_overkill))

        #footman damage
        p1_damage = random.randint(player1['unit_stats']['footman_damage_min'],player1['unit_stats']['footman_damage_max'] + 1)
        p1_armor = player1['unit_stats']['footman_armor']
        p1_hp = player1['unit_stats']['footman_hp']
        p1_speed = player1['unit_stats']['footman_speed']
        p2_damage = random.randint(player2['unit_stats']['footman_damage_min'],player2['unit_stats']['footman_damage_max'] + 1)
        p2_armor = player2['unit_stats']['footman_armor']
        p2_hp = player2['unit_stats']['footman_hp']
        p2_speed = player2['unit_stats']['footman_speed']
        print ("1: {}  2: {}  1o: {}  2o:  {}".format(p1[0], p2[0], p1_overkill, p2_overkill))
        p1[0], p2[0], p1_overkill, p2_overkill = self.fight(p1_damage,p1_armor,p1_hp,p1_speed,p1_overkill,p1[0],p2_damage,p2_armor,p2_hp,p2_speed,p2_overkill,p2[0])
        print ("1: {}  2: {}  1o: {}  2o:  {}".format(p1[0], p2[0], p1_overkill, p2_overkill))
        
        if p1[0] == 0 and p2[0] != 0:
            return 2, p1, p2
        elif p2[0] == 0 and p1[0] != 0:
            return 1, p1, p2
        else:
            return 0, p1, p2

    def move_units(self, player1, player2, field):
        #player1
        units_p1 = {}
        for i in range (0, 7):
            if i >= field + 1:
                previous = i + 1
                units_p1[str(i)] = (np.add(player1['units'][str(i)],player1['units'][str(previous)])).tolist()
                player1['units'][str(previous)] = [0,0,0]
            else:
                units_p1[str(i)] = [0,0,0]
        units_p1['7'] = [player1['next']['foot'] + player1['units']['7'][0],player1['next']['arch'] + player1['units']['7'][1],player1['next']['cav'] + player1['units']['7'][2]]

        #player2
        units_p2 = {}
        for i in range (7, 0, -1):
            if i <= field:
                previous = i - 1
                units_p2[str(i)] = (np.add(player2['units'][str(i)],player2['units'][str(previous)])).tolist()
                player2['units'][str(previous)] = [0,0,0]
            else:
                units_p2[str(i)] = [0,0,0]
        units_p2['0'] = [player2['next']['foot'] + player2['units']['0'][0],player2['next']['arch'] + player2['units']['0'][1],player2['next']['cav'] + player2['units']['0'][2]]
        return units_p1, units_p2



    def update_tech(self, player1, player2, defines):
        p1_next = player1['next']
        p1_current = player1['upgrades']
        p1_stats = player1['unit_stats']
        p2_next = player2['next']
        p2_current = player2['upgrades']
        p2_stats = player2['unit_stats']
        p1_data = {
            u'unit_stats': {
            u'footman_hp' : defines.footman_hp,
            u'footman_armor' : defines.footman_armor_pl * (p1_current['foot_def'] * p1_next['up_foot_def']) + p1_stats['footman_armor'],
            u'footman_damage_min' : defines.footman_damage_min_pl * (p1_current['foot_att'] * p1_next['up_foot_att']) + p1_stats['footman_damage_min'],
            u'footman_damage_max' : defines.footman_damage_max_pl * (p1_current['foot_att'] * p1_next['up_foot_att']) + p1_stats['footman_damage_max'],
            u'footman_speed' : defines.footman_speed,
            u'archer_hp' : defines.archer_hp,
            u'archer_armor' : defines.archer_armor_pl * (p1_current['arch_def'] * p1_next['up_arch_def']) + p1_stats['archer_armor'],
            u'archer_damage_min' : defines.archer_damage_min_pl * (p1_current['arch_att'] * p1_next['up_arch_att']) + p1_stats['archer_damage_min'],
            u'archer_damage_max' : defines.archer_damage_max_pl * (p1_current['arch_att'] * p1_next['up_arch_att']) + p1_stats['archer_damage_max'],
            u'archer_hp' : defines.archer_hp,
            u'archer_speed' : defines.archer_speed,
            u'cavalry_hp' : defines.cavalry_hp,
            u'cavalry_armor' : defines.cavalry_armor_pl * (p1_current['cav_def'] * p1_next['up_cav_def']) + p1_stats['cavalry_armor'],
            u'cavalry_damage_min' : defines.cavalry_damage_min_pl * (p1_current['cav_att'] * p1_next['up_cav_att']) + p1_stats['cavalry_damage_min'],
            u'cavalry_damage_max' : defines.cavalry_damage_max_pl * (p1_current['cav_att'] * p1_next['up_cav_att']) + p1_stats['cavalry_damage_max'],
            u'cavalry_speed' : defines.cavalry_speed
            },
            u'upgrades': {
                u'tech' : p1_current['tech'] + p1_next['tech_up'],
                u'gold' : p1_current['gold'] + p1_next['gold_up'],
                u'foot_att' : p1_current['foot_att'] + p1_next['up_foot_att'],
                u'foot_def' : p1_current['foot_def'] + p1_next['up_foot_def'],
                u'arch_att' : p1_current['arch_att'] + p1_next['up_arch_att'],
                u'arch_def' : p1_current['arch_def'] + p1_next['up_arch_def'],
                u'cav_att' : p1_current['cav_att'] + p1_next['up_cav_att'],
                u'cav_def' : p1_current['cav_def'] + p1_next['up_cav_def']
            },
            u'next' : firestore.DELETE_FIELD,
            u'gold' : p1_next['gold'],
            u'tech' : p1_next['tech']
        }
        p2_data = {
            u'unit_stats': {
            u'footman_hp' : defines.footman_hp,
            u'footman_armor' : defines.footman_armor_pl * (p2_current['foot_def'] * p2_next['up_foot_def']) + p2_stats['footman_armor'],
            u'footman_damage_min' : defines.footman_damage_min_pl * (p2_current['foot_att'] * p2_next['up_foot_att']) + p2_stats['footman_damage_min'],
            u'footman_damage_max' : defines.footman_damage_max_pl * (p2_current['foot_att'] * p2_next['up_foot_att']) + p2_stats['footman_damage_max'],
            u'footman_speed' : defines.footman_speed,
            u'archer_hp' : defines.archer_hp,
            u'archer_armor' : defines.archer_armor_pl * (p2_current['arch_def'] * p2_next['up_arch_def']) + p2_stats['archer_armor'],
            u'archer_damage_min' : defines.archer_damage_min_pl * (p2_current['arch_att'] * p2_next['up_arch_att']) + p2_stats['archer_damage_min'],
            u'archer_damage_max' : defines.archer_damage_max_pl * (p2_current['arch_att'] * p2_next['up_arch_att']) + p2_stats['archer_damage_max'],
            u'archer_hp' : defines.archer_hp,
            u'archer_speed' : defines.archer_speed,
            u'cavalry_hp' : defines.cavalry_hp,
            u'cavalry_armor' : defines.cavalry_armor_pl * (p2_current['cav_def'] * p2_next['up_cav_def']) + p2_stats['cavalry_armor'],
            u'cavalry_damage_min' : defines.cavalry_damage_min_pl * (p2_current['cav_att'] * p2_next['up_cav_att']) + p2_stats['cavalry_damage_min'],
            u'cavalry_damage_max' : defines.cavalry_damage_max_pl * (p2_current['cav_att'] * p2_next['up_cav_att']) + p2_stats['cavalry_damage_max'],
            u'cavalry_speed' : defines.cavalry_speed
            },
            u'upgrades': {
                u'tech' : p2_current['tech'] + p2_next['tech_up'],
                u'gold' : p2_current['gold'] + p2_next['gold_up'],
                u'foot_att' : p2_current['foot_att'] + p2_next['up_foot_att'],
                u'foot_def' : p2_current['foot_def'] + p2_next['up_foot_def'],
                u'arch_att' : p2_current['arch_att'] + p2_next['up_arch_att'],
                u'arch_def' : p2_current['arch_def'] + p2_next['up_arch_def'],
                u'cav_att' : p2_current['cav_att'] + p2_next['up_cav_att'],
                u'cav_def' : p2_current['cav_def'] + p2_next['up_cav_def']
            },
            u'next' : firestore.DELETE_FIELD,
            u'gold' : p2_next['gold'],
            u'tech' : p2_next['tech']
        }
        return p1_data, p2_data