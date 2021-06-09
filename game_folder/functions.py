import sys
import pygame

# Define o código RGB das cores utilizadas
BLACK = (0,0,0)
BLUE_MIDNIGHT = (0,0,30)
BLUE = (12,12,100)
BLUE_ICE = (0,255,251)
YELLOW_GOLD = (255,215,0)
WHITE = (255,255,255)

# Estabelece a pasta que contem as sprites.
LEFTblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueLEFT.png'
RIGHTblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueRIGHT.png'
UPblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueUP.png'
DOWNblue_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_blueDOWN.png'
LEFTyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowLEFT.png'
RIGHTyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowRIGHT.png'
UPyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowUP.png'
DOWNyellow_dir = 'SPRITES/SPRITE_TRON_LIGHTCICLE_yellowDOWN.png'
derezzedVFX_dir = 'SPRITES/VFX DEREZZED EXPLOSION.png'

pygame.init() # inicia o pygame
screen_size = (800,800) # Largura e altura da tela
surface =  pygame.display.set_mode(screen_size) # Define tela

class yellowLightCicle(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.size_vert = (32,80)
        self.size_horiz = (80,32)
        self.image = pygame.image.load(LEFTyellow_dir).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size_horiz)
        self.rect = self.image.get_rect()
        self.set_position(400,200)
        self.set_velocity(-0.2,0)
        self.direction = "LEFT"
        self.trace = []

    def set_position(self, x, y):
        self.rect.center = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        """
        Define a velocidade
        vx: velocidade no eixo x
        vy: velocidade no eixo y
        """
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def update_direction(self, direction):
        if direction != self.direction:
            position = self.rect.center
            if direction == "UP":
                self.image = pygame.image.load(DOWNyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_vert)
                self.set_velocity(0,0.2)
            if direction == "DOWN":
                self.image = pygame.image.load(UPyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_vert)
                self.set_velocity(0,-0.2)
            if direction == "LEFT":
                self.image = pygame.image.load(LEFTyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_horiz)
                self.set_velocity(-0.2,0)
            if direction == "RIGHT":
                self.image = pygame.image.load(RIGHTyellow_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_horiz)
                self.set_velocity(0.2,0)
            self.rect = self.image.get_rect()
            self.rect.center = position
            self.direction = direction

    def update_position(self, time):
        self.rect.center += self.velocity * time
        self.trace.append(self.rect.center)
    
    def slow_down(self):
        if self.direction == "UP":
            if self.velocity == (0,0.2):
                self.set_velocity(0,0.1)
            elif self.velocity == (0,0.1):
                self.set_velocity(0,0.2)
        if self.direction == "DOWN":
            if self.velocity == (0,-0.2):
                self.set_velocity(0,-0.1)
            elif self.velocity == (0,-0.1):
                self.set_velocity(0,-0.2)
        if self.direction == "LEFT":
            if self.velocity == (-0.2,0):
                self.set_velocity(-0.1,0)
            elif self.velocity == (-0.1,0):
                self.set_velocity(-0.2,0)
        if self.direction == "RIGHT":
            if self.velocity == (0.2,0):
                self.set_velocity(0.1,0)
            elif self.velocity == (0.1,0):
                self.set_velocity(0.2,0)

class blueLightCicle(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.size_vert = (32,80)
        self.size_horiz = (80,32)
        self.image = pygame.image.load(RIGHTblue_dir).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size_horiz)
        self.rect = self.image.get_rect()
        self.set_position(100,400)
        self.set_velocity(0.2,0) # VALOR TESTE
        self.direction = "RIGHT"
        self.trace = []

    def set_position(self, x, y):
        self.rect.center = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def update_direction(self, direction):
        if direction != self.direction:
            position = self.rect.center
            if direction == "UP":
                self.image = pygame.image.load(DOWNblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_vert)
                self.set_velocity(0,0.2)
            if direction == "DOWN":
                self.image = pygame.image.load(UPblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_vert)
                self.set_velocity(0,-0.2)
            if direction == "LEFT":
                self.image = pygame.image.load(LEFTblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_horiz)
                self.set_velocity(-0.2,0)
            if direction == "RIGHT":
                self.image = pygame.image.load(RIGHTblue_dir).convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size_horiz)
                self.set_velocity(0.2,0)
            self.rect = self.image.get_rect()
            self.rect.center = position
            self.direction = direction

    def update_position(self, time):
        self.rect.center += self.velocity * time
        self.trace.append(self.rect.center)
    
    def slow_down(self):
        if self.direction == "UP":
            if self.velocity == (0,0.2):
                self.set_velocity(0,0.1)
            elif self.velocity == (0,0.1):
                self.set_velocity(0,0.2)
        if self.direction == "DOWN":
            if self.velocity == (0,-0.2):
                self.set_velocity(0,-0.1)
            elif self.velocity == (0,-0.1):
                self.set_velocity(0,-0.2)
        if self.direction == "LEFT":
            if self.velocity == (-0.2,0):
                self.set_velocity(-0.1,0)
            elif self.velocity == (-0.1,0):
                self.set_velocity(-0.2,0)
        if self.direction == "RIGHT":
            if self.velocity == (0.2,0):
                self.set_velocity(0.1,0)
            elif self.velocity == (0.1,0):
                self.set_velocity(0.2,0)

def tutorial_screen():
    line_text = [
        "Olá programa! Aqui você testará suas habilidades com motos.",
        "Você iniciará no canto inferior esquerdo da tela.",
        "Para vencer, a moto amarela deve se chocar contra o seu rastro de luz.",
        "Esse rastro é deixado por todos os pontos em que sua moto passa.",
        "Para controlar a moto, aperte as teclas CIMA, BAIXO, DIREITA, ESQUERDA.",
        "E para diminuir a velocidade pressione a BARRA DE ESPAÇO.",
        "Da mesma forma, a moto amarela também tentará o mesmo.",
        "Que os jogos começem!"
    ]
    command = "...(pressione ENTER para continuar)"
    font_instructions = pygame.font.Font(pygame.font.get_default_font(), 20)
    
    for line in line_text:
        command_pressed = True
        while command_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # quebra o loop
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    command_pressed = False
                    break
            surface.fill(BLACK)
            pygame.draw.rect(surface, BLUE_ICE, (0,0,800,800), 20)
            line_image = font_instructions.render(line, True, BLUE_ICE)
            command_image = font_instructions.render(command, True, BLUE_ICE)
            surface.blit(line_image,(20,100))
            surface.blit(command_image,(20,700))
            pygame.display.flip()

def crash(collor1,collor2):
    if collor1.rect.topright[0] == 800 or collor1.rect.topright[1] == 0 or collor1.rect.bottomleft[1] == 800 or collor1.rect.bottomleft[0] == 0:
        derezzed_visual = pygame.image.load(derezzedVFX_dir).convert_alpha()
        derezzed_visual = pygame.transform.scale(derezzed_visual, (int(derezzed_visual.get_width()/5),int(derezzed_visual.get_height()/5)))
        surface.blit(derezzed_visual, collor1.rect.center)
        collor1.kill()
        return False # retorna um valor booleano "False" para parar o "trace"
    if collor2.rect.topright[0] == 800 or collor2.rect.topright[1] == 0 or collor2.rect.bottomleft[1] == 800 or collor2.rect.bottomleft[0] == 0:
        derezzed_visual = pygame.image.load(derezzedVFX_dir).convert_alpha()
        derezzed_visual = pygame.transform.scale(derezzed_visual, (int(derezzed_visual.get_width()/5),int(derezzed_visual.get_height()/5)))
        surface.blit(derezzed_visual, collor2.rect.center)
        collor2.kill()
        return False # retorna um valor booleano "False" para parar o "trace"
    for t in collor1.trace:
        if collor2.rect.collidepoint(t):
            derezzed_visual = pygame.image.load(derezzedVFX_dir).convert_alpha()
            derezzed_visual = pygame.transform.scale(derezzed_visual, (int(derezzed_visual.get_width()/5),int(derezzed_visual.get_height()/5)))
            surface.blit(derezzed_visual, collor2.rect.center)
            collor2.kill()
            return False # retorna um valor booleano "False" para parar o "trace"
    return True # Caso contrário, continua igual
        
def draw_background():
    surface.fill(BLUE)
    thickness = 10
    distance = screen_size[0]/8 # espaço entre cada quadrado
    i = 0
    while i < 9:
        pygame.draw.line(surface, BLUE_MIDNIGHT, (0,(i*distance)), (screen_size[0],(i*distance)), thickness) # Desenha linha horizontal
        pygame.draw.line(surface, BLUE_MIDNIGHT, ((i*distance),0), ((i*distance),screen_size[0]), thickness) # Desenha linha vertical
        i+=1

def show_score(stop_blue,stop_yellow):
    if stop_blue == False:
        score = ["Você PERDEU!","Para tentar novamente, clique N"]
        font_used = pygame.font.Font(pygame.font.get_default_font(), 40)
        line_image = font_used.render(score[0], True, BLUE_ICE, BLACK)
        surface.blit(line_image,(50,200))
        line_image2 = font_used.render(score[1], True, BLUE_ICE, BLACK)
        surface.blit(line_image2,(50,300))

    if stop_yellow == False:
        score = ["Você GANHOU!","Para prosseguir, clique M"]
        font_used = pygame.font.Font(pygame.font.get_default_font(), 40)
        line_image = font_used.render(score[0], True, BLUE_ICE, BLACK)
        surface.blit(line_image,(50,200))
        line_image2 = font_used.render(score[1], True, BLUE_ICE, BLACK)
        surface.blit(line_image2,(50,300))


##############################################################################

YELLOWdisk_dir = 'SPRITES_BOSS/disk_orange.png'
BLUEdisk_dir = 'SPRITES_BOSS/disk_blue.png'
tronREGULAR_dir = 'SPRITES_BOSS/normal_sem_disco.png'
tronDUCK_dir = 'SPRITES_BOSS/agachado.png'
tronDEREZZED1_dir = 'SPRITES_BOSS/desfazendo_1.png'
tronDEREZZED2_dir = 'SPRITES_BOSS/desfazendo_2.png'
wind_dir = 'SPRITES_BOSS/vento.png'
clu_dir = 'SPRITES_BOSS/boss_sem_disco.png'


class Disk_BF(pygame.sprite.Sprite):
    def __init__(self, group, colour, rect):
        super().__init__(group)
        self.colour = colour
        if self.colour == "yellow":
            self.image = pygame.image.load(YELLOWdisk_dir).convert_alpha()
            self.image = pygame.transform.scale(self.image, (31,28))
            self.set_velocity(-0.2,0) # TODO: mudar para um valor fixo
        if self.colour == "blue":
            self.image = pygame.image.load(BLUEdisk_dir).convert_alpha()
            self.image = pygame.transform.scale(self.image, (31,28))
            self.set_velocity(0.2,0) # TODO: mudar para um valor fixo
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(rect[0], rect[1], 31, 28)
    
    def set_position(self, x, y):
        self.rect.midbottom = pygame.math.Vector2(x, y)
    
    def set_velocity(self, vx, vy):
        """Define a velocidade
        vx: velocidade no eixo x
        vy: velocidade no eixo y"""
        self.velocity = pygame.math.Vector2(vx, vy)

    def update(self, time):
        print(self.rect.midbottom)
        self.rect.center += self.velocity * time

class CLU_BF(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load(clu_dir).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,90)) # TODO: mudar para um valor fixo
        self.rect = pygame.Rect(600, 535, 40, 90) # TODO: testar valores
        self.mask = pygame.mask.from_surface(self.image)

class TRON_BF(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.images = []
        self.i = pygame.image.load(tronREGULAR_dir).convert_alpha()
        self.i = pygame.transform.scale(self.i, (40,90)) # TODO: mudar para um valor fixo
        self.images.append(self.i)
        self.i = pygame.image.load(tronDUCK_dir).convert_alpha()
        self.i = pygame.transform.scale(self.i, (40,60)) # TODO: mudar para um valor fixo
        self.images.append(self.i)
        self.i = pygame.image.load(tronDEREZZED1_dir).convert_alpha()
        self.i = pygame.transform.scale(self.i, (40,90)) # TODO: mudar para um valor fixo
        self.images.append(self.i)
        self.i = pygame.image.load(tronDEREZZED2_dir).convert_alpha()
        self.i = pygame.transform.scale(self.i, (40,90)) # TODO: mudar para um valor fixo
        self.images.append(self.i)
        self.image = self.images[0]
        self.rect = pygame.Rect(150, 535, 40, 90) # TODO: testar valores
        self.og_x = self.rect.x
        self.og_y = self.rect.y
        self.mask = pygame.mask.from_surface(self.image)
        self.state = "STANDING"
        self.gravity = pygame.math.Vector2(0, 0.1) # TODO: testar valores
        self.set_velocity(0,0)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def set_velocity(self, vx, vy):
        """Define a velocidade
        vx: velocidade no eixo x
        vy: velocidade no eixo y"""
        self.velocity = pygame.math.Vector2(vx, vy)
    
    def stand(self):
        self.state = "STANDING"
        self.image = self.images[0]
        self.set_position(self.og_x, self.og_y) # TODO: testar valores
        self.set_velocity(0,0)
        self.mask = pygame.mask.from_surface(self.image)

    def duck(self):
        self.state = "DUCKING"
        self.set_position(self.og_x, self.og_y+30) # TODO: testar valores
        self.image = self.images[1]
        self.mask = pygame.mask.from_surface(self.image)
    
    def jump(self):
        self.jump_rect = self.rect
        if self.state == "STANDING":
            self.state = "JUMPING"
            self.set_velocity(0,-1) # TODO: testar valores
    
    def derezzed(self, sprite_name):
        self.image = self.images[2]
        pygame.time.delay(333)
        self.image = self.images[3]
        pygame.time.delay(333)
        sprite_name.kill()

    def update(self, time):
        if self.velocity == (0,1):
            self.stand()
        if self.state == "JUMPING":
            self.velocity += self.gravity
            self.rect.midbottom += self.velocity * time