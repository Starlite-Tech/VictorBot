import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/textures/mobs/player.png")
        self.velocity = pygame.math.Vector2(0,0)
        self.position = pygame.math.Vector2(400,9*25)
        self.direction = False #false = left, True=Right

    def draw(self, cam):
        if self.direction:
            cam.fixed_blit(self.image,self.position)
        else:
            cam.fixed_blit(pygame.transform.flip(self.image,1,0),self.position)

    def movement(self, cam,dt):
        speed=200
        friction = 300
        #key inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_LEFT]:
            self.velocity.x=speed
            self.direction = True
        elif keys[pygame.K_a]:
            self.velocity.x=-speed
            self.direction=False
        if keys[pygame.K_s]:
            cam.y+=208*dt
        elif keys[pygame.K_w]:
            cam.y-=208*dt
        #move camera or player
        nx = ((self.velocity.x*dt)+self.position.x) #nx is newX
        if nx<=200 or nx>600-15:
            cam.move(self.velocity*dt)
        else:
            self.position.x+=self.velocity.x*dt
            cam.y+=self.velocity.y*dt
        #Friction
        if self.velocity.x>0:
            self.velocity.x -= friction*dt
            self.velocity.x = max(self.velocity.x,0)
        else:# self.velocity.x<0:
            self.velocity.x += friction*dt
            self.velocity.x = min(self.velocity.x,0)
