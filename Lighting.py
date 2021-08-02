import pygame

class LightLayer:
    def __init__(self,size):
        self.lights = []
        self.LightSurf =  pygame.Surface(size,pygame.SRCALPHA).convert()
        self.size = size

    def draw(self,surf,camPos):
        self.LightSurf.fill((80,80,80,255))
        for x in self.lights:
            if x.rect[0]+x.rect[2]>camPos[0] and x.rect[0]<self.size[0]+camPos[0]:
                if x.rect[1]+x.rect[3]>camPos[1] and x.rect[1]<self.size[1]+camPos[1]:
                    x.draw(self.LightSurf,camPos)
            else:
                continue
        surf.blit(self.LightSurf,(0,0),special_flags=pygame.BLEND_RGBA_MULT)

    def append(self,light):
        self.lights.append(light)

    def appendAll(self,lights):
        self.lights+=lights

class Light:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect
        self.lightSurf = pygame.Surface([rect[2],rect[3]],pygame.SRCALPHA).convert()
        pygame.draw.rect(self.lightSurf,color,[0,0,rect[2],rect[3]])
    def draw(self,surf,camPos):
        surf.blit(self.lightSurf,(self.rect[0]-camPos[0],self.rect[1]-camPos[1]),special_flags=pygame.BLEND_RGBA_ADD)
