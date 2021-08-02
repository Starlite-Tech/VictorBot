import Math
import Utils
import pygame
pygame.init()

game = Utils.Game()
import GameObjects,Lighting
game.light = Lighting.Light([0,255,0,255],[0,100,100,100])
game.light2 = Lighting.Light([255,255,255,255],[100,0,100,100])
game.light3 = Lighting.Light([255,0,0,255],[100,200,100,100])
game.bgLight = Lighting.Light([255,255,255,255],[0,0,800,600])
game.lightLayer.appendAll([game.light,game.light2,game.light3])
game.player = GameObjects.Player.Player()

game.TileMap = GameObjects.blocks.TileMap.TileMap(15,16,game.originalRect.size, GameObjects.blocks.Tiles.TilesEnum.DIRT,GameObjects.blocks.Tiles.TilesEnum.GRASS)
#print(game.TileMap.chunkmap)
game.vel=[0,0]
game.direction = 1
game.camera.y+=1800

def update(dt):
    speed = 50
    game.light2.rect[0]=game.camPos[0]
    game.light2.rect[1]=game.camPos[1]
    game.light.rect[1]+=dt*speed*game.direction
    game.light3.rect[0]-=dt*speed*game.direction
    if game.light.rect[0]>200 or game.light.rect[0]<0:
        game.direction *=-1
    #game.TileMap.change_to_air(game.camPos)


pygame.event.set_allowed([pygame.QUIT,pygame.VIDEORESIZE])
speed = 200
def events(dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
    game.player.movement(game.camera,dt)
    #print(game.camera.position)

def render():
    game.TileMap.draw(game.camera)
    game.player.draw(game.camera)
    #game.lightLayer.draw(game.camera.surface,game.camPos)
    #pygame.draw.rect(game.screen,[255,255,255,255],[100-game.camPos[0],100-game.camPos[1],100,100])


if __name__=="__main__":
    game.update = update
    game.events = events
    game.render = render
    game.start()
