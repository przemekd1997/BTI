
class Cost:
    def __init__(self):
        self.cost_gold_tech = 100
        self.cost_tech_gold = 100
        self.cost_foot_gold = 10
        self.cost_foot_att_tech = 100
        self.cost_foot_att_gold = 50
        self.cost_foot_def_tech = 100
        self.cost_foot_def_gold = 50
        self.cost_arch_gold = 10
        self.cost_arch_att_tech = 100
        self.cost_arch_att_gold = 50
        self.cost_arch_def_tech = 100
        self.cost_arch_def_gold = 50
        self.cost_cav_gold = 10
        self.cost_cav_att_tech = 100
        self.cost_cav_att_gold = 50
        self.cost_cav_def_tech = 100
        self.cost_cav_def_gold = 50

        self.pl_gold_tech = 50
        self.pl_tech_gold = 50
        self.pl_foot = 5
        self.pl_foot_att_gold = 25
        self.pl_foot_att_tech = 50
        self.pl_foot_def_gold = 25
        self.pl_foot_def_tech = 50
        self.pl_arch = 5
        self.pl_arch_att_gold = 25
        self.pl_arch_att_tech = 50
        self.pl_arch_def_gold = 25
        self.pl_arch_def_tech = 50
        self.pl_cav = 5
        self.pl_cav_att_gold = 25
        self.pl_cav_att_tech = 50
        self.pl_cav_def_gold = 25
        self.pl_cav_def_tech = 50

class Stats:
    def __init__(self):
        #footman stats
        self.footman_hp = 10
        self.footman_armor = 0
        self.footman_damage_min = 4
        self.footman_damage_max = 5
        self.footman_speed = 0
        self.footman_damage_min_pl = 4
        self.footman_damage_max_pl = 6
        self.footman_armor_pl = 5

        #archer stats
        self.archer_hp = 10
        self.archer_armor = 0
        self.archer_damage_min = 4
        self.archer_damage_max = 5
        self.archer_speed = 0
        self.archer_damage_min_pl = 4
        self.archer_damage_max_pl = 6
        self.archer_armor_pl = 5

        #cavalry stats
        self.cavalry_hp = 10
        self.cavalry_armor = 0
        self.cavalry_damage_min = 4
        self.cavalry_damage_max = 5
        self.cavalry_speed = 0
        self.cavalry_damage_min_pl = 4
        self.cavalry_damage_max_pl = 6
        self.cavalry_armor_pl = 5