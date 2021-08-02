from . import Tiles
import random, perlin

class ChunkGenerator:
    def __init__(self):
        self.perlin = perlin.Perlin(8983)
        self.perlin.one_octave(0.25)
    def generate(self, x,y,w,h):
        #h,w = 16,16
        chnk = []
        for i in range(16):
            row = []
            p = int(self.perlin.one((i+(x*16))))
            for j in range(16):
                # if y<=2 and y>=0:
                #     row.append(Tiles.TilesEnum.AIR)
                # if y<=4:
                #
                # else:
                #     row.append(self.subsurface_chunk(i+(x*w),j+(y*h)))
                #     continue
                row.append(self.surface_chunk((i+(x*16)),(16*h)-(j+(y*16)),(16*h)-p))
                #continue
            #chnk.append(row)
            chnk.append(row[::-1])
        #return chnk[::-1]
        return chnk



    def surface_chunk(self,x,y,p):
        stoneH = 80
        h = p
        gh = h-60
        #if x<16: print(y,h)
        boundary = 12
        if y==gh:
            return Tiles.TilesEnum.GRASS
        elif y<gh and y>gh-80:# and y>h-80:
            return Tiles.TilesEnum.DIRT
        elif y<=gh-80:
            return self.subsurface_chunk(x,y-60)
        elif y>gh:
            return Tiles.TilesEnum.AIR
        else:
            return Tiles.TilesEnum.ERROR

        # else:
        #     p = random.randint(0,(y-boundary)*4)
        #     if p ==0:
        #         return Tiles.TilesEnum.DIRT
        #     else:
        #         return Tiles.TilesEnum.STONE

    def subsurface_chunk(self,x,y):
        return random.choices([
                Tiles.TilesEnum.STONE,
                Tiles.TilesEnum.COAL,
                Tiles.TilesEnum.IRON,
                Tiles.TilesEnum.SILVER,
                Tiles.TilesEnum.GOLD,
                Tiles.TilesEnum.COREDIUM,
                Tiles.TilesEnum.SKYRITE
            ],
            weights=[
                200,
                6,
                max(min((y-20)/3,4),0),
                max(min((y-20)/3,4),0),
                max(min((y-40)/3,2),0),
                max(min((y-50)/3,1),0),
                max(min((y-70)/3,1),0)
            ]
        )[0]
