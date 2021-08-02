import pygame
from . import TerrainGenerator

class TileMap:
    def __init__(self,width,height,res,default,top):
        chnksize = 16
        self.surface = pygame.Surface(res,pygame.SRCALPHA)#.convert()
        self.res = res

        self.chunkmap = []
        chunkGen = TerrainGenerator.ChunkGenerator()
        for x in range(width):
            row = []
            for y in range(height):
                #if y ==0:
                row.append(Chunk(chnksize,res,chunkGen.generate(x,y,width,height)))
                # else:
                #     row.append(Chunk(chnksize,res,default))
            self.chunkmap.append(row)

    def draw(self, camera):
        chnksize = 16
        chnkRes = chnksize*32
        self.surface.fill((255,255,255,0))


        for cx,x in enumerate(self.chunkmap):
            #if ((cx+1)*chnkRes)>=camPos[0] and (cx*chnkRes)<=self.res[0]+camPos[0]:
            if True:
                for cy, y in enumerate(x):
                    #print(cy)
                    #if ((cy+1)*chnkRes)>=camPos[1]-(chnkRes) and (cy*chnkRes)<=self.res[1]+camPos[1]:
                    if True:
                        y.draw(camera.surface,camera,[((cx)*chnkRes),((cy)*chnkRes)])
        #camera.blit(self.surface,[0,0])

    def __repr__(self):
        out = ""
        for x in self.chunkmap:
            None

    def change_to_air(self,camPos):
        pos = pygame.mouse.get_pos()
        pos = [
            pos[0]+camPos[0],
            pos[1]+camPos[1],
        ]
        click = pygame.mouse.get_pressed()
        selected_chunk = self.chunkmap[int(pos[0]/(32*16))*(32*16)][int(pos[1]/(32*16))*(32*16)]
        print(selected_chunk)

class Chunk:
    def __init__(self,size,res,tiles):
        self.surface = pygame.Surface((size*32,size*32),pygame.SRCALPHA)#.convert()
        #self.default = default
        self.res = res
        self.width = self.surface.get_width()

        self.tilemap = tiles
        self.surface.fill((50,50,50,0))
        renderDist = 1.5
        for cx,x in enumerate(self.tilemap):
            for cy, y in enumerate(x):
                y.draw(
                    self.surface,
                    [
                        (16*32)-(cx*32)-32,
                        (16*32)-(cy*32)-32
                    ]
                )

    def draw(self, surf, cam,pos):
        # self.surface.fill((50,50,50,200))
        # renderDist = 1.5
        # for cx,x in enumerate(self.tilemap):
        #     if ((self.width-(cx*32))+((renderDist-1)*32))+pos[0]>=camPos[0] and ((self.width-(cx*32))-((renderDist)*32))+pos[0]<=camPos[0]+self.res[0]:
        #         for cy, y in enumerate(x):
        #             if ((self.width-(cy*32))+((renderDist-1)*32))+pos[1]>=camPos[1] and ((self.width-(cy*32))-((renderDist)*32))+pos[1]<=camPos[1]+self.res[1]:
        #                 y.draw(
        #                     self.surface,
        #                     [
        #                         (16*32)-(cx*32)-32,
        #                         (16*32)-(cy*32)-32
        #                     ]
        #                 )
        surf.blit(self.surface,[pos[0]-cam.position[0],pos[1]-cam.position[1]])

    def render_full(self):
        self.surface.fill((255,255,255,0))
        renderDist = 1.5
        for cx,x in enumerate(self.tilemap):
            for cy, y in enumerate(x):
                y.draw(
                    self.surface,
                    [
                        (cx*32)-32,
                        (cy*32)-32
                    ]
                )

    def render_single(self, x,y, tiles):
        self.tilemap[x][y].draw(
            self.surface,
            [
                (16*32)-(x*32)-32,
                (16*32)-(y*32)-32
            ]
        )
