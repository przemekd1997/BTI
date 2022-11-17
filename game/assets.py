import pygame
import json

class GFX:
    def __init__(self):
        #TITLE ASSETS
        self.title_window_size = (300,500)
        self.tbg = pygame.image.load("resources/back.jpg").convert()
        self.tbg = pygame.transform.scale(self.tbg,self.title_window_size)
        self.b_red = pygame.image.load("resources/b1.png").convert_alpha()
        self.b_red = pygame.transform.scale(self.b_red,(200,100))
        self.b_pink = pygame.image.load("resources/b2.png").convert_alpha()
        self.b_pink = pygame.transform.scale(self.b_pink,(200,100))
        self.b1_pos = (50, 150, 200, 100)
        self.b2_pos = (50, 250, 200, 100)
        
        #GAME ASSETS
        #import background
        self.bg = pygame.image.load("resources/w3_main.png").convert()
        self.bg = pygame.transform.scale(self.bg,(1500,800))
        self.up_bg = pygame.image.load("resources/upg_back.jpg").convert()
        self.up_bg = pygame.transform.scale(self.up_bg,(300,800))
        self.border_bg = pygame.image.load("resources/sword.png").convert_alpha()
        self.border_bg = pygame.transform.scale(self.border_bg,(122,800))

        #import icons
        self.icon_size = (75,75)
        self.icon_battle_size = (46,46)
        self.row_x = 1570
        self.row_y = 100
        self.row_sp = 100
        self.icon_gold = pygame.image.load("resources/income_up.png").convert()
        self.icon_gold = pygame.transform.scale(self.icon_gold, self.icon_size)
        self.icon_gold_pos = (self.row_x, self.row_y)
        self.icon_tech = pygame.image.load("resources/tech_up.png").convert()
        self.icon_tech = pygame.transform.scale(self.icon_tech, self.icon_size)
        self.icon_tech_pos = (self.row_x + self.row_sp, self.row_y)
        self.icon_foot_att = pygame.image.load("resources/footman_weapon_up.png").convert()
        self.icon_foot_att = pygame.transform.scale(self.icon_foot_att, self.icon_size)
        self.icon_foot_att_pos = (self.row_x, self.row_y + self.row_sp)
        self.icon_foot_def = pygame.image.load("resources/footman_armor_up.png").convert()
        self.icon_foot_def = pygame.transform.scale(self.icon_foot_def, self.icon_size)
        self.icon_foot_def_pos = (self.row_x + self.row_sp, self.row_y + self.row_sp)
        self.icon_arch_att = pygame.image.load("resources/archer_weapon_up.png").convert()
        self.icon_arch_att = pygame.transform.scale(self.icon_arch_att, self.icon_size)
        self.icon_arch_att_pos = (self.row_x, self.row_y + 2*self.row_sp)
        self.icon_arch_def = pygame.image.load("resources/archer_armor_up.png").convert()
        self.icon_arch_def = pygame.transform.scale(self.icon_arch_def, self.icon_size)
        self.icon_arch_def_pos = (self.row_x + self.row_sp, self.row_y + 2*self.row_sp)
        self.icon_cav_att = pygame.image.load("resources/cav_weapon_up.png").convert()
        self.icon_cav_att = pygame.transform.scale(self.icon_cav_att, self.icon_size)
        self.icon_cav_att_pos = (self.row_x, self.row_y + 3*self.row_sp)
        self.icon_cav_def = pygame.image.load("resources/cav_armor_up.png").convert()
        self.icon_cav_def = pygame.transform.scale(self.icon_cav_def, self.icon_size)
        self.icon_cav_def_pos = (self.row_x + self.row_sp, self.row_y + 3*self.row_sp)
        self.icon_arch = pygame.image.load("resources/archer.png").convert()
        self.icon_arch = pygame.transform.scale(self.icon_arch, self.icon_size)
        self.icon_arch_battle = pygame.transform.scale(self.icon_arch, self.icon_battle_size)
        self.icon_arch_pos = (self.row_x, self.row_y + 4*self.row_sp + 30)
        self.icon_cav = pygame.image.load("resources/cav.png").convert()
        self.icon_cav = pygame.transform.scale(self.icon_cav, self.icon_size)
        self.icon_cav_battle = pygame.transform.scale(self.icon_cav, self.icon_battle_size)
        self.icon_cav_pos = (self.row_x + self.row_sp, self.row_y + 4*self.row_sp + 30)
        self.icon_foot = pygame.image.load("resources/footman.png").convert()
        self.icon_foot = pygame.transform.scale(self.icon_foot, self.icon_size)
        self.icon_foot_battle = pygame.transform.scale(self.icon_foot, self.icon_battle_size)
        self.icon_foot_pos = (self.row_x, self.row_y + 5*self.row_sp + 30)
        self.icon_et = pygame.image.load("resources/b1.png").convert_alpha()
        self.icon_et = pygame.transform.scale(self.icon_et, self.icon_size)
        self.icon_et_pos = (self.row_x + self.row_sp, self.row_y + 5*self.row_sp + 30)

        #import misc
        self.banner = pygame.image.load("resources/banner.png").convert_alpha()
        self.banner = pygame.transform.scale(self.banner, (250,50))
        self.icon_gold_min = pygame.image.load("resources/Coin_icon.png").convert_alpha()
        self.icon_gold_min = pygame.transform.scale(self.icon_gold_min, (20,20))
        self.icon_tech_min = pygame.image.load("resources/tech.png").convert_alpha()
        self.icon_tech_min = pygame.transform.scale(self.icon_tech_min, (20,20))
        self.icon_peace = pygame.image.load("resources/dove.png").convert_alpha()
        self.icon_peace = pygame.transform.scale(self.icon_peace, (45,45))
        self.icon_war = pygame.image.load("resources/war.png").convert_alpha()
        self.icon_war = pygame.transform.scale(self.icon_war, (45,45))
        self.icon_sun = pygame.image.load("resources/sun.png").convert_alpha()
        self.icon_sun = pygame.transform.scale(self.icon_sun, (60,60))
        self.icon_hg = pygame.image.load("resources/hourglass.png").convert_alpha()
        self.icon_hg = pygame.transform.scale(self.icon_hg, self.icon_size)
        self.icon_x = pygame.image.load("resources/X.png").convert_alpha()
        self.icon_x = pygame.transform.scale(self.icon_x, self.icon_size)

        #battle icon position
        self.battle_icon_pos = []
        for i in range (8):
            pp = []
            for j in range (3):
                p = (1250 - i*150, 500 + j* 60)
                pp.append([(p[0]+2,p[1]+2)])
            self.battle_icon_pos.append(pp)
        
        #texts
        self.bigfont = pygame.font.SysFont('Corbel',25, bold=True)
        self.smallfont = pygame.font.SysFont('Corbel',20, bold=True)
        self.battlefont = pygame.font.SysFont('Corbel',20, bold=True)
        self.tooltipfont = pygame.font.SysFont('Corbel',15, bold=True)
        self.text_up = self.bigfont.render('Upgrades' , True , (255,255,255))
        self.text_unit = self.bigfont.render('Units' , True , (255,255,255))
        self.tooltip_icon_text_color = (255,255,255)
        self.tooltip_icon_battle_color = (255,255,0)

        with open('resources/desc.txt') as f:
            data = f.read()
        self.tooltip = json.loads(data)