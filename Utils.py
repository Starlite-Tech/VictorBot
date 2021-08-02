import pygame,Lighting,datetime
pygame.init()

class Game:
    def __init__(self):
        winSize = 50
        self.window = pygame.display.set_mode((winSize*16,winSize*9),pygame.RESIZABLE|pygame.HWSURFACE|pygame.DOUBLEBUF)
        self.originalRect = pygame.Rect(0,0,winSize*16,winSize*9)
        self.camera = Camera()
        self.lightLayer = Lighting.LightLayer(self.originalRect.size)
        self.clock = pygame.time.Clock()
        self.running = True
        self.camPos = [0,0]

    def start(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text= font.render('30', True, (0,255,0), (0,0,255))
        hfps = 1
        lfps = 0
        while self.running:
            tick = self.clock.tick(150)/1000

            self.update(tick)
            self.events(tick)

            self.window.fill((0,0,0))
            self.camera.fill((120,120,200,255))

            self.render()

            #self.lightLayer.draw(self.screen,self.camPos)
            hfps=max(min(hfps,tick),0.000001)
            lfps=max(lfps,tick)
            text = font.render(str(int(1/tick)), True, (0,255,0), (0,0,255))
            self.camera.fixed_blit(text,[0,0])
            self.camera.draw(self.window)

            pygame.display.update()
        pygame.quit()
        print(1/hfps,1/lfps)
        quit()

class Camera:
    def __init__(self):
        self.x, self.y = 0,0
        self.rect = pygame.Rect(0,0,50*16,50*9)
        self.surface = pygame.Surface(self.rect.size,pygame.SRCALPHA).convert()

    def draw(self, window):
        self.rect.left = self.x
        self.rect.top = self.y
        scale = int((window.get_height()/self.rect.size[1])*self.rect.size[0])
        newposition = [
            (window.get_width()/2)-(scale/2),
            0
        ]
        window.blit(
            pygame.transform.scale(
                self.surface,
                (scale,window.get_height())
            ),
            newposition
        )


    def fixed_blit(self, surf, pos):
        self.surface.blit(surf,pos)

    def blit(self, surf, pos):
        other = pygame.Rect(pos,surf.get_rect().size)
        if self.rect.colliderect(other):
            self.surface.blit(surf,pos)
            return True
        return False

    def fill(self, color):
        self.surface.fill(color)

    def move(self, new_position):
        #self.rect.move_ip(new_position[0],new_position[1])
        self.x += new_position[0]
        self.y += new_position[1]
        #self.rect.update()

    def set_position(self, new_position):
        self.rect.x = new_position[0]
        self.rect.y = new_position[1]

    @property
    def position(self):
        return self.rect.topleft
