from defines import Stats

class Board:
    def __init__(self):
        self.gid = 0
        self.player = 0
        self.day = 1
        self.war = False
        self.gold = 300
        self.tech = 300
        self.field = 3
        self.tech_level = 1
        self.gold_level = 1
        self.foot_att_level = 1
        self.foot_def_level = 1
        self.arch_att_level = 1
        self.arch_def_level = 1
        self.cav_att_level = 1
        self.cav_def_level = 1
        self.enemy_units = [0,0,0]
        self.player_units = [[0 for col in range(3)] for row in range(8)]
        self.stats = Stats()