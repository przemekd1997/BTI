import pygame
from forward import Forward
from board import Board
from defines import Cost
from defines import Stats
from assets import GFX
import game_service_pb2
import game_service_pb2_grpc
import grpc
import time
import json

class Mgame():
    def __init__(self, ip):
        pygame.init()
        self.window_size = (1800,800)
        self.channel = grpc.insecure_channel(ip)
        self.stub = game_service_pb2_grpc.TTTStub(self.channel)
        self.screen = pygame.display.set_mode(self.window_size)
        self.forward = Forward()
        self.board = Board()
        self.costs = Cost()
        self.stats = Stats()
        self.gfx = GFX()
        self.tooltip_1 = ""
        self.tooltip_2 = ""
        self.tooltip_cost1 = 0
        self.tooltip_cost2 = 0

    def matchmaking(self):
        pygame.display.set_caption("Matchmaking Screen Demo")
        screen = pygame.display.set_mode(self.window_size)
        s = pygame.Surface(self.window_size)
        s.fill((0,0,0))
        screen.blit(s,(0,0))
        pygame.display.update()

        response = self.stub.JoinMatchmaking(game_service_pb2.New_game(name = 0))
        gid = response.id
        player = response.uid
        if response.stat == 1:          
            return gid, player
        else:
            while True:
                response = self.stub.Matchmaking_Ready(game_service_pb2.New_game_status(name = gid))
                if response.stat == 1:
                    return gid, player         
                time.sleep(2)

    def end_turn(self):
        message = game_service_pb2.Forward_to_server()
        message.gold_up = self.forward.up_gold
        message.tech_up = self.forward.up_tech
        message.gold = self.forward.gold
        message.tech = self.forward.tech
        message.up_foot_att = self.forward.up_foot_att
        message.up_foot_def = self.forward.up_foot_def
        message.up_arch_att = self.forward.up_arch_att
        message.up_arch_def = self.forward.up_arch_def
        message.up_cav_att = self.forward.up_cav_att
        message.up_cav_def = self.forward.up_cav_def
        message.foot = self.forward.foot
        message.arch = self.forward.arch
        message.cav = self.forward.cav
        message.name = self.board.gid
        message.player = self.board.player
    
        #print(message.player)
        #print(message)
        self.stub.End_Turn(message)
        print("poszedł forward")

    def ready_check(self):
        response = self.stub.Next_Turn_Status(game_service_pb2.Game_status(gid = self.board.gid, day = self.board.day))
        return response.stat
    def get_new_turn(self):
        status = self.stub.Next_Turn(game_service_pb2.Next_Turn_Info(gid = self.board.gid, player = self.board.player))
        #update stats
        self.board.day = status.day
        self.board.field = status.field
        self.board.war = status.war
        self.board.gold = status.gold
        self.board.tech = status.tech
        self.board.gold_level += self.forward.up_gold
        self.board.tech_level += self.forward.up_tech
        self.board.foot_att_level += self.forward.up_foot_att
        self.board.foot_def_level += self.forward.up_foot_def
        self.board.arch_att_level += self.forward.up_arch_att
        self.board.arch_def_level += self.forward.up_arch_def
        self.board.cav_att_level += self.forward.up_cav_att
        self.board.cav_def_level += self.forward.up_cav_def

        #update units stats
        self.board.stats.footman_damage_min = status.foot_att_min
        self.board.stats.footman_damage_max = status.foot_att_max
        self.board.stats.footman_armor = status.foot_armor
        self.board.stats.archer_damage_min = status.arch_att_min
        self.board.stats.archer_damage_max = status.arch_att_max
        self.board.stats.archer_armor = status.arch_armor
        self.board.stats.cavalry_damage_min = status.cav_att_min
        self.board.stats.cavalry_damage_max = status.cav_att_max
        self.board.stats.cavalry_armor = status.cav_armor

        #update units    
        self.board.enemy_units = status.enemy
        player_units = []
        for i in range (8):
            player_units.append(status.player[(i*3):(i*3)+3])
        self.board.player_units = player_units
        return status.winner

    def title(self):     
        #screen title
        pygame.display.set_caption("Title Screen Demo")
        self.window_size = (300,500)
        self.screen = pygame.display.set_mode(self.window_size)

        #Font
        smallfont = pygame.font.SysFont('Corbel',35)
        text_quit = smallfont.render('Quit' , True , (0,0,0))
        text_ng = smallfont.render('New Game' , True , (0,0,0))

        running = True
        while running:
            mouse = pygame.mouse.get_pos()
            #quit event
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
            #mouse click event
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    #quit
                    if self.gfx.b2_pos[0] <= mouse[0] <= self.gfx.b2_pos[0] + self.gfx.b2_pos[2] \
                    and self.gfx.b2_pos[1] <= mouse[1] <= self.gfx.b2_pos[1] + self.gfx.b2_pos[3]:
                        pygame.quit()
                    #new game
                    if self.gfx.b1_pos[0] <= mouse[0] <= self.gfx.b1_pos[0] + self.gfx.b1_pos[2] \
                    and self.gfx.b1_pos[1] <= mouse[1] <= self.gfx.b1_pos[1] + self.gfx.b1_pos[3]:
                        return 1
                
            

            #draw bg
            self.screen.blit(self.gfx.tbg, (0,0))

            #draw exit
            self.screen.blit(self.gfx.b_red, (self.gfx.b2_pos[0],self.gfx.b2_pos[1]))
            if self.gfx.b2_pos[0] <= mouse[0] <= self.gfx.b2_pos[0] + self.gfx.b2_pos[2] \
            and self.gfx.b2_pos[1] <= mouse[1] <= self.gfx.b2_pos[1] + self.gfx.b2_pos[3]:
                self.screen.blit(self.gfx.b_pink, (self.gfx.b2_pos[0],self.gfx.b2_pos[1]))
        
            self.screen.blit(text_quit , (self.gfx.b2_pos[0] + 60,self.gfx.b2_pos[1] + 35))

            #draw new game
            self.screen.blit(self.gfx.b_red, (self.gfx.b1_pos[0],self.gfx.b1_pos[1]))
            if self.gfx.b1_pos[0] <= mouse[0] <= self.gfx.b1_pos[0] + self.gfx.b1_pos[2] \
            and self.gfx.b1_pos[1] <= mouse[1] <= self.gfx.b1_pos[1] + self.gfx.b1_pos[3]:
                self.screen.blit(self.gfx.b_pink, (self.gfx.b1_pos[0],self.gfx.b1_pos[1]))
            self.screen.blit(text_ng , (self.gfx.b1_pos[0] + 20,self.gfx.b1_pos[1] + 35))

            pygame.display.update()

    def update_left(self):
        #blit bg
        self.screen.blit(self.gfx.bg, (0,0))
        self.screen.blit(self.gfx.border_bg, (1500 - (122/2),0))
        
        #peace and day info
        text_day = self.gfx.smallfont.render(str(self.board.day) , True , (0,0,0))
        self.screen.blit(self.gfx.icon_sun, (0,0))
        self.screen.blit(text_day, (25,20))
        pygame.draw.circle(self.screen,(0,0,0),(20,100),30)
        pygame.draw.circle(self.screen,(255,255,255),(20,100),30)
        if self.board.war:
            self.screen.blit(self.gfx.icon_war, (-3,77))
        else:
            self.screen.blit(self.gfx.icon_peace, (0,75))
        
        #units bg
        s = pygame.Surface((50,50))
        s.set_alpha(140)
        for i in range (8):
            for j in range (3):
                if i <= self.board.field:
                    s.fill((9,163,235))
                else:
                    s.fill((224,49,49))
                p = (1250 - i*150, 500 + j* 60)
                self.screen.blit(s,p)
        #units - player
        for i in range (8):
            if self.board.player_units[i][0] != 0:
                text_icon_tooltip = self.gfx.battlefont.render(str(self.board.player_units[i][0]) , True , self.gfx.tooltip_icon_battle_color)
                self.screen.blit(self.gfx.icon_foot_battle, (1252 - i*150, 502 + 0))
                self.screen.blit(text_icon_tooltip, (1252 - i*150 + 3, 502 + 3))
            if self.board.player_units[i][1] != 0:
                text_icon_tooltip = self.gfx.battlefont.render(str(self.board.player_units[i][1]) , True , self.gfx.tooltip_icon_battle_color)
                self.screen.blit(self.gfx.icon_arch_battle, (1252 - i*150, 502 + 60))
                self.screen.blit(text_icon_tooltip, (1252 - i*150 + 3, 502 + 63))
            if self.board.player_units[i][2] != 0:
                text_icon_tooltip = self.gfx.battlefont.render(str(self.board.player_units[i][2]) , True , self.gfx.tooltip_icon_battle_color)
                self.screen.blit(self.gfx.icon_cav_battle, (1252 - i*150, 502 + 120))
                self.screen.blit(text_icon_tooltip, (1252 - i*150 + 3, 502 + 123))
        #units - enemy
        if self.board.enemy_units[0] != 0:
            text_icon_tooltip = self.gfx.battlefont.render(str(self.board.enemy_units[0]) , True , self.gfx.tooltip_icon_battle_color)
            self.screen.blit(self.gfx.icon_foot_battle, (1252 - (self.board.field + 1)*150, 502 + 0))
            self.screen.blit(text_icon_tooltip, (1252 - (self.board.field + 1)*150 + 3, 502 + 3))
        if self.board.enemy_units[1] != 0:
            text_icon_tooltip = self.gfx.battlefont.render(str(self.board.enemy_units[1]) , True , self.gfx.tooltip_icon_battle_color)
            self.screen.blit(self.gfx.icon_arch_battle, (1252 - (self.board.field + 1)*150, 502 + 60))
            self.screen.blit(text_icon_tooltip, (1252 - (self.board.field + 1)*150 + 3, 502 + 63))
        if self.board.enemy_units[2] != 0:
            text_icon_tooltip = self.gfx.battlefont.render(str(self.board.enemy_units[2]) , True , self.gfx.tooltip_icon_battle_color)
            self.screen.blit(self.gfx.icon_cav_battle, (1252 - (self.board.field + 1)*150, 502 + 120))
            self.screen.blit(text_icon_tooltip, (1252 - (self.board.field + 1)*150 + 3, 502 + 123))   
        pygame.display.update()

    def update_right(self):
        #bg
        self.screen.blit(self.gfx.up_bg, (1500,0))
        s = pygame.Surface((300,100))
        s.set_alpha(140)
        s.fill((0,0,0))
        self.screen.blit(s,(1500, self.gfx.row_y + 6*self.gfx.row_sp + 20))
        self.screen.blit(self.gfx.border_bg, (1500 - (122/2),0))

        #tech and gold text info
        text_gold = self.gfx.smallfont.render(str(self.board.gold) , True , (255,255,255))
        text_tech = self.gfx.smallfont.render(str(self.board.tech) , True , (255,255,255))

        #tech and gold banner + display
        self.screen.blit(self.gfx.banner, (1525,10))
        self.screen.blit(self.gfx.icon_gold_min, (1575,20))
        self.screen.blit(text_gold, (1600,25))
        self.screen.blit(self.gfx.icon_tech_min, (1675,20))
        self.screen.blit(text_tech, (1700,25))
        self.screen.blit(self.gfx.banner, (1525,55))
        self.screen.blit(self.gfx.text_up, (1600,65))    

        #update icon    
        self.screen.blit(self.gfx.icon_gold, self.gfx.icon_gold_pos)
        if self.forward.up_gold == True:
            self.screen.blit(self.gfx.icon_x, self.gfx.icon_gold_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render(str(self.board.gold_level) , True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_gold_pos[0] + 5,self.gfx.icon_gold_pos[1] + self.gfx.icon_size[1] - 15))
        self.screen.blit(self.gfx.icon_tech, self.gfx.icon_tech_pos)
        if self.forward.up_tech == True:
            self.screen.blit(self.gfx.icon_x, self.gfx.icon_tech_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render(str(self.board.tech_level) , True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_tech_pos[0] + 5,self.gfx.icon_tech_pos[1] + self.gfx.icon_size[1] - 15))
        self.screen.blit(self.gfx.icon_foot_att, self.gfx.icon_foot_att_pos)
        if self.forward.up_foot_att == True:
            self.screen.blit(self.gfx.icon_x, self.gfx.icon_foot_att_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render(str(self.board.foot_att_level) , True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_foot_att_pos[0] + 5,self.gfx.icon_foot_att_pos[1] + self.gfx.icon_size[1] - 15))
        self.screen.blit(self.gfx.icon_foot_def, self.gfx.icon_foot_def_pos)
        if self.forward.up_foot_def == True:
            self.screen.blit(self.gfx.icon_x, self.gfx.icon_foot_def_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render(str(self.board.foot_def_level) , True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_foot_def_pos[0] + 5,self.gfx.icon_foot_def_pos[1] + self.gfx.icon_size[1] - 15))
        self.screen.blit(self.gfx.icon_arch_att, self.gfx.icon_arch_att_pos)
        if self.forward.up_arch_att == True:
            self.screen.blit(self.gfx.icon_x, self.gfx.icon_arch_att_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render(str(self.board.arch_att_level) , True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_arch_att_pos[0] + 5,self.gfx.icon_arch_att_pos[1] + self.gfx.icon_size[1] - 15))
        self.screen.blit(self.gfx.icon_arch_def, self.gfx.icon_arch_def_pos)
        if self.forward.up_arch_def == True:
            self.screen.blit(self.gfx.icon_x, self.gfx.icon_arch_def_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render(str(self.board.arch_def_level) , True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_arch_def_pos[0] + 5,self.gfx.icon_arch_def_pos[1] + self.gfx.icon_size[1] - 15))
        self.screen.blit(self.gfx.icon_cav_att, self.gfx.icon_cav_att_pos)
        if self.forward.up_cav_att == True:
            self.screen.blit(self.gfx.icon_x, self.gfx.icon_cav_att_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render(str(self.board.cav_att_level) , True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_cav_att_pos[0] + 5,self.gfx.icon_cav_att_pos[1] + self.gfx.icon_size[1] - 15))
        self.screen.blit(self.gfx.icon_cav_def, self.gfx.icon_cav_def_pos)
        if self.forward.up_cav_def == True:
            self.screen.blit(self.gfx.icon_x, self.gfx.icon_cav_def_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render(str(self.board.cav_def_level) , True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_cav_def_pos[0] + 5,self.gfx.icon_cav_def_pos[1] + self.gfx.icon_size[1] - 15))

        self.screen.blit(self.gfx.banner,(1525, self.gfx.row_y + 4*self.gfx.row_sp - 20))
        self.screen.blit(self.gfx.text_unit, (1625,self.gfx.row_y + 4*self.gfx.row_sp - 10))    
        self.screen.blit(self.gfx.icon_arch, self.gfx.icon_arch_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render('(+' + str(self.forward.arch) + ')', True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_arch_pos[0] + 5,self.gfx.icon_arch_pos[1] + 5))
        self.screen.blit(self.gfx.icon_cav, self.gfx.icon_cav_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render('(+' + str(self.forward.cav) + ')', True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_cav_pos[0] + 5,self.gfx.icon_cav_pos[1] + 5))
        self.screen.blit(self.gfx.icon_foot, self.gfx.icon_foot_pos)
        text_icon_tooltip = self.gfx.tooltipfont.render('(+' + str(self.forward.foot) + ')', True , self.gfx.tooltip_icon_text_color)
        self.screen.blit(text_icon_tooltip,(self.gfx.icon_foot_pos[0] + 5,self.gfx.icon_foot_pos[1] + 5))
        self.screen.blit(self.gfx.icon_et, self.gfx.icon_et_pos)
        self.screen.blit(self.gfx.icon_hg, self.gfx.icon_et_pos)

        #update tooltips
        text_icon_tooltip1 = self.gfx.tooltipfont.render(self.tooltip_1 , True , self.gfx.tooltip_icon_text_color)
        text_icon_tooltip2 = self.gfx.tooltipfont.render(self.tooltip_2 , True , self.gfx.tooltip_icon_text_color)
        if self.tooltip_cost1 != 0:
            text_cost = self.gfx.tooltipfont.render(str(self.tooltip_cost1) , True , self.gfx.tooltip_icon_text_color)
            self.screen.blit(self.gfx.icon_gold_min, (self.gfx.row_x - 40, self.gfx.row_y + 6*self.gfx.row_sp + 25))
            self.screen.blit(text_cost,(self.gfx.row_x - 10, self.gfx.row_y + 6*self.gfx.row_sp + 30))
        elif self.tooltip_cost2 != 0:
            text_cost = self.gfx.tooltipfont.render(str(self.tooltip_cost2) , True , self.gfx.tooltip_icon_text_color)
            self.screen.blit(self.gfx.icon_tech_min, (self.gfx.row_x - 40, self.gfx.row_y + 6*self.gfx.row_sp + 25))
            self.screen.blit(text_cost,(self.gfx.row_x - 10, self.gfx.row_y + 6*self.gfx.row_sp + 30))
        self.screen.blit(text_icon_tooltip1,(self.gfx.row_x + 20, self.gfx.row_y + 6*self.gfx.row_sp + 30))
        self.screen.blit(text_icon_tooltip2,(self.gfx.row_x - 40, self.gfx.row_y + 6*self.gfx.row_sp + 70))

        pygame.display.update()
    
    def event_handler(self,mouse):
        #events
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #gold up
                if self.gfx.icon_gold_pos[0] <= mouse[0] <= self.gfx.icon_gold_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_gold_pos[1] <= mouse[1] <= self.gfx.icon_gold_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.tech >= self.costs.cost_gold_tech + (self.costs.pl_gold_tech * self.board.gold_level) \
                    and self.forward.up_gold == False:
                        self.forward.up_gold = 1
                        self.board.tech -= self.costs.cost_gold_tech + (self.costs.pl_gold_tech * self.board.gold_level)

                    if ev.button == 3 and self.forward.up_gold == True:
                        self.forward.up_gold = 0
                        self.board.tech += self.costs.cost_gold_tech + (self.costs.pl_gold_tech * self.board.gold_level)
                    
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['gold_up']['name']
                        self.tooltip_2 = self.gfx.tooltip['gold_up']['desc'][0] + str(self.costs.pl_gold_tech)
                        self.tooltip_cost1 = 0
                        self.tooltip_cost2 = self.costs.cost_gold_tech + (self.costs.pl_gold_tech * self.board.gold_level)

                    self.update_right()
                #tech up
                elif self.gfx.icon_tech_pos[0] <= mouse[0] <= self.gfx.icon_tech_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_tech_pos[1] <= mouse[1] <= self.gfx.icon_tech_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.gold >= self.costs.cost_tech_gold + (self.costs.pl_tech_gold * self.board.tech_level) \
                    and self.forward.up_tech == False:
                        self.forward.up_tech = 1
                        self.board.gold -= self.costs.cost_gold_tech + (self.costs.pl_tech_gold * self.board.tech_level)
                    if ev.button == 3 and self.forward.up_tech == True:
                        self.forward.up_tech = 0
                        self.board.gold += self.costs.cost_gold_tech + (self.costs.pl_tech_gold * self.board.tech_level)

                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['tech_up']['name']
                        self.tooltip_2 = self.gfx.tooltip['tech_up']['desc'][0] + str(self.costs.pl_tech_gold)
                        self.tooltip_cost1 = self.costs.cost_gold_tech + (self.costs.pl_tech_gold * self.board.tech_level)
                        self.tooltip_cost2 = 0
                    self.update_right()
                #footmen attack up
                elif self.gfx.icon_foot_att_pos[0] <= mouse[0] <= self.gfx.icon_foot_att_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_foot_att_pos[1] <= mouse[1] <= self.gfx.icon_foot_att_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.tech >= self.costs.cost_foot_att_tech + (self.costs.pl_foot_att_tech * self.board.foot_att_level) and self.forward.up_foot_att == False:
                        self.forward.up_foot_att = 1
                        self.board.tech -= self.costs.cost_foot_att_tech + (self.costs.pl_foot_att_tech * self.board.foot_att_level)
                    if ev.button == 3 and self.forward.up_foot_att == True:
                        self.forward.up_foot_att = 0
                        self.board.tech += self.costs.cost_foot_att_tech + (self.costs.pl_foot_att_tech * self.board.foot_att_level)
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['foot_att']['name']
                        self.tooltip_2 = self.gfx.tooltip['foot_att']['desc'][0] + str(self.stats.footman_damage_min_pl * self.board.foot_att_level) + " - " + str(self.stats.footman_damage_max_pl * self.board.foot_att_level)
                        self.tooltip_cost1 = 0
                        self.tooltip_cost2 = self.costs.cost_foot_att_tech + (self.costs.pl_foot_att_tech * self.board.foot_att_level)
                    self.update_right()
                #footmen defence up
                elif self.gfx.icon_foot_def_pos[0] <= mouse[0] <= self.gfx.icon_foot_def_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_foot_def_pos[1] <= mouse[1] <= self.gfx.icon_foot_def_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.tech >= self.costs.cost_foot_def_tech + (self.costs.pl_foot_def_tech * self.board.foot_def_level) and self.forward.up_foot_def == False:
                        self.forward.up_foot_def = 1
                        self.board.tech -= self.costs.cost_foot_def_tech + (self.costs.pl_foot_def_tech * self.board.foot_def_level)
                    if ev.button == 3 and self.forward.up_foot_def == True:
                        self.forward.up_foot_def = 0
                        self.board.tech += self.costs.cost_foot_def_tech + (self.costs.pl_foot_def_tech * self.board.foot_def_level)
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['foot_def']['name']
                        self.tooltip_2 = self.gfx.tooltip['foot_def']['desc'][0] + str(self.stats.footman_armor_pl * self.board.foot_def_level) 
                        self.tooltip_cost1 = 0
                        self.tooltip_cost2 = self.costs.cost_foot_def_tech + (self.costs.pl_foot_def_tech * self.board.foot_def_level)
                    self.update_right()
                #archer attack up
                elif self.gfx.icon_arch_att_pos[0] <= mouse[0] <= self.gfx.icon_arch_att_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_arch_att_pos[1] <= mouse[1] <= self.gfx.icon_arch_att_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.tech >= self.costs.cost_arch_att_tech + (self.costs.pl_arch_att_tech * self.board.arch_att_level) and self.forward.up_arch_att == False:
                        self.forward.up_arch_att = 1
                        self.board.tech -= self.costs.cost_arch_att_tech + (self.costs.pl_arch_att_tech * self.board.arch_att_level)
                    if ev.button == 3 and self.forward.up_arch_att == True:
                        self.forward.up_arch_att = 0
                        self.board.tech += self.costs.cost_arch_att_tech + (self.costs.pl_arch_att_tech * self.board.arch_att_level)
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['arch_att']['name']
                        self.tooltip_2 = self.gfx.tooltip['arch_att']['desc'][0] + str(self.stats.archer_damage_min_pl * self.board.arch_att_level) + " - " + str(self.stats.archer_damage_max_pl * self.board.arch_att_level)
                        self.tooltip_cost1 = 0
                        self.tooltip_cost2 = self.costs.cost_arch_att_tech + (self.costs.pl_arch_att_tech * self.board.arch_att_level)
                    self.update_right()
            #archer defence up
                elif self.gfx.icon_arch_def_pos[0] <= mouse[0] <= self.gfx.icon_arch_def_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_arch_def_pos[1] <= mouse[1] <= self.gfx.icon_arch_def_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.tech >= self.costs.cost_arch_def_tech + (self.costs.pl_arch_def_tech * self.board.arch_def_level) and self.forward.up_arch_def == False:
                        self.forward.up_arch_def = 1
                        self.board.tech -= self.costs.cost_arch_def_tech + (self.costs.pl_arch_def_tech * self.board.arch_def_level)
                    if ev.button == 3 and self.forward.up_arch_def == True:
                        self.forward.up_arch_def = 0
                        self.board.tech += self.costs.cost_arch_def_tech + (self.costs.pl_arch_def_tech * self.board.arch_def_level)
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['arch_def']['name']
                        self.tooltip_2 = self.gfx.tooltip['arch_def']['desc'][0] + str(self.stats.archer_armor_pl * self.board.arch_def_level)
                        self.tooltip_cost1 = 0
                        self.tooltip_cost2 = self.costs.cost_arch_def_tech + (self.costs.pl_arch_def_tech * self.board.arch_def_level)
                    self.update_right()
                #cavalry attack up
                elif self.gfx.icon_cav_att_pos[0] <= mouse[0] <= self.gfx.icon_cav_att_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_cav_att_pos[1] <= mouse[1] <= self.gfx.icon_cav_att_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.tech >= self.costs.cost_cav_att_tech + (self.costs.pl_cav_att_tech * self.board.cav_att_level) and self.forward.up_cav_att == False:
                        self.forward.up_cav_att = 1
                        self.board.tech -= self.costs.cost_cav_att_tech + (self.costs.pl_cav_att_tech * self.board.cav_att_level)
                    if ev.button == 3 and self.forward.up_cav_att == True:
                        self.forward.up_cav_att = 0
                        self.board.tech += self.costs.cost_cav_att_tech + (self.costs.pl_cav_att_tech * self.board.cav_att_level)
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['cav_att']['name']
                        self.tooltip_2 = self.gfx.tooltip['cav_att']['desc'][0] + str(self.stats.cavalry_damage_min_pl * self.board.cav_att_level) + " - " + str(self.stats.cavalry_damage_max_pl * self.board.cav_att_level)
                        self.tooltip_cost1 = 0
                        self.tooltip_cost2 = self.costs.cost_cav_att_tech + (self.costs.pl_cav_att_tech * self.board.cav_att_level)
                    self.update_right()
                #cavalry defence up
                elif self.gfx.icon_cav_def_pos[0] <= mouse[0] <= self.gfx.icon_cav_def_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_cav_def_pos[1] <= mouse[1] <= self.gfx.icon_cav_def_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.tech >= self.costs.cost_cav_def_tech + (self.costs.pl_cav_def_tech * self.board.cav_def_level) and self.forward.up_cav_def == False:
                        self.forward.up_cav_def = 1
                        self.board.tech -= self.costs.cost_cav_def_tech + (self.costs.pl_cav_def_tech * self.board.cav_def_level)
                    if ev.button == 3 and self.forward.up_cav_def == True:
                        self.forward.up_cav_def = 0
                        self.board.tech += self.costs.cost_cav_def_tech + (self.costs.pl_cav_def_tech * self.board.cav_def_level)
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['cav_def']['name']
                        self.tooltip_2 = self.gfx.tooltip['cav_def']['desc'][0] + str(self.stats.cavalry_armor_pl * self.board.cav_def_level)
                        self.tooltip_cost1 = 0
                        self.tooltip_cost2 = self.costs.cost_cav_def_tech + (self.costs.pl_cav_def_tech * self.board.cav_def_level)
                    self.update_right()
                #archer recrut
                elif self.gfx.icon_arch_pos[0] <= mouse[0] <= self.gfx.icon_arch_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_arch_pos[1] <= mouse[1] <= self.gfx.icon_arch_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.gold >= self.costs.cost_arch_gold + (self.costs.pl_arch * (self.board.arch_att_level + self.board.arch_def_level)):
                        self.forward.arch += 1
                        self.board.gold -= self.costs.cost_arch_gold + (self.costs.pl_arch * (self.board.arch_att_level + self.board.arch_def_level))
                    if ev.button == 3 and self.forward.arch  > 0:
                        self.forward.arch -= 1
                        self.board.gold += self.costs.cost_arch_gold + (self.costs.pl_arch * (self.board.arch_att_level + self.board.arch_def_level))
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['archer']['name'] + " " + self.gfx.tooltip['archer']['desc'][0]
                        self.tooltip_2 = self.gfx.tooltip['archer']['desc'][1] + str(self.board.stats.archer_damage_min) \
                            + " - " + str(self.board.stats.archer_damage_max) + " " \
                            + self.gfx.tooltip['archer']['desc'][2] + str(self.board.stats.archer_armor) + " "\
                            + self.gfx.tooltip['archer']['desc'][3] + str(self.board.stats.archer_hp)
                        self.tooltip_cost2 = 0
                        self.tooltip_cost1 = self.costs.cost_arch_gold + (self.costs.pl_arch * (self.board.arch_att_level + self.board.arch_def_level))
                    self.update_right()
                #cavalry recrut
                elif self.gfx.icon_cav_pos[0] <= mouse[0] <= self.gfx.icon_cav_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_cav_pos[1] <= mouse[1] <= self.gfx.icon_cav_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.gold >= self.costs.cost_cav_gold + (self.costs.pl_cav * (self.board.cav_att_level + self.board.cav_def_level)):
                        self.forward.cav += 1
                        self.board.gold -= self.costs.cost_cav_gold + (self.costs.pl_cav * (self.board.cav_att_level + self.board.cav_def_level))
                    if ev.button == 3 and self.forward.cav  > 0:
                        self.forward.cav -= 1
                        self.board.gold += self.costs.cost_cav_gold + (self.costs.pl_cav * (self.board.cav_att_level + self.board.cav_def_level))
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['cavalry']['name'] + " " + self.gfx.tooltip['cavalry']['desc'][0]
                        self.tooltip_2 = self.gfx.tooltip['cavalry']['desc'][1] + str(self.board.stats.cavalry_damage_min) \
                            + " - " + str(self.board.stats.cavalry_damage_max) + " " \
                            + self.gfx.tooltip['cavalry']['desc'][2] + str(self.board.stats.cavalry_armor) + " "\
                            + self.gfx.tooltip['cavalry']['desc'][3] + str(self.board.stats.cavalry_hp)
                        self.tooltip_cost2 = 0
                        self.tooltip_cost1 = self.costs.cost_cav_gold + (self.costs.pl_cav * (self.board.cav_att_level + self.board.cav_def_level))
                    self.update_right()
                #footman recrut
                elif self.gfx.icon_foot_pos[0] <= mouse[0] <= self.gfx.icon_foot_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_foot_pos[1] <= mouse[1] <= self.gfx.icon_foot_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 1 and self.board.gold >= self.costs.cost_foot_gold + (self.costs.pl_foot * (self.board.foot_att_level + self.board.foot_def_level)):
                        self.forward.foot += 1
                        self.board.gold -= self.costs.cost_foot_gold + (self.costs.pl_foot * (self.board.foot_att_level + self.board.foot_def_level))
                    if ev.button == 3 and self.forward.foot  > 0:
                        self.forward.foot -= 1
                        self.board.gold += self.costs.cost_foot_gold + (self.costs.pl_foot * (self.board.foot_att_level + self.board.foot_def_level))
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['footman']['name'] + " " + self.gfx.tooltip['footman']['desc'][0]
                        self.tooltip_2 = self.gfx.tooltip['footman']['desc'][1] + str(self.board.stats.footman_damage_min) \
                            + " - " + str(self.board.stats.footman_damage_max) + " " \
                            + self.gfx.tooltip['footman']['desc'][2] + str(self.board.stats.footman_armor) + " "\
                            + self.gfx.tooltip['footman']['desc'][3] + str(self.board.stats.footman_hp)
                        self.tooltip_cost2 = 0
                        self.tooltip_cost1 = self.costs.cost_foot_gold + (self.costs.pl_foot * (self.board.foot_att_level + self.board.foot_def_level))
                    self.update_right()
                #end turn
                elif self.gfx.icon_et_pos[0] <= mouse[0] <= self.gfx.icon_et_pos[0] + self.gfx.icon_size[0] \
                and self.gfx.icon_et_pos[1] <= mouse[1] <= self.gfx.icon_et_pos[1] + self.gfx.icon_size[1]:
                    if ev.button == 2:
                        self.tooltip_1 = self.gfx.tooltip['end_turn']['name']
                        self.tooltip_2 = ""
                        self.tooltip_cost2 = 0
                        self.tooltip_cost1 = 0
                    else:
                        s = pygame.Surface(self.window_size)
                        s.set_alpha(140)
                        s.fill((0,0,0))
                        self.screen.blit(s,(0,0))
                        pygame.display.update()
                        self.forward.gold = self.board.gold
                        self.forward.tech = self.board.tech
                        self.end_turn()
                        while True:
                            print("w petli")
                            time.sleep(2)
                            if self.ready_check() == 1:
                                break
                        winner = self.get_new_turn()
                        self.forward = Forward()
                        if winner != 0:
                            return 1
                        self.update_left()
                        self.update_right()
                        pygame.display.update()
                else:
                    self.tooltip_1 = ""
                    self.tooltip_2 = ""
                    self.tooltip_cost2 = 0
                    self.tooltip_cost1 = 0
        return 0

    def game(self,gid,pid):
        pygame.display.set_caption("Main Screen Demo")  
        self.window_size = (1800,800)
        self.screen = pygame.display.set_mode(self.window_size)      
        self.board.gid = gid
        self.board.player = pid

        self.update_left()
        self.update_right()
        
        while True:
            mouse = pygame.mouse.get_pos()
            x = self.event_handler(mouse)
            if x == 1:
                break
        return 0



if __name__ == "__main__":
    with open('config.txt') as f:
        data = f.read()
    info = json.loads(data)
    mode = 0
    game = Mgame(info['ip_address'] + ':' + info['port'])
    while True:
        if mode == 0:
            mode = game.title()
        if mode == 1:
            if info['test_mode']:
                gid = "test"
                player = 1
                mode = game.game(gid,player)
            else:
                gid, player = game.matchmaking()
                mode = game.game(gid,player)