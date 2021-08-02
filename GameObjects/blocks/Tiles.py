import pygame,json

class Tile:
    _ID = 0
    def __init__(self,ID, name: str, imagePath: str, solid: bool,light = None):
        self.name = name
        if name!="Air":
            self.img = pygame.image.load(imagePath).convert()
        else:
            self.img = pygame.image.load(imagePath)
        self.solid = bool
        self.id = ID

    def __eq__(self,other):
        if other.__class__!=self.__class__:
            if other.id == self.id:
                return True
        else:
            return False

    def draw(self, surface, position):
        surface.blit(self.img,position)

    @property
    def rect(self):
        return self.img.get_rect()

class _TilesEnum:
    def __init__(self,):
        with open('assets/json/tiles.json','r') as f:
            self.jsonDict = json.loads(f.read())
        self.tiles = {}
        tiles = self.jsonDict["Tiles"]
        for c,x in enumerate(self.jsonDict["Tiles"].keys()):
            tiledata = tiles[x]
            self.tiles[x] = Tile(c,tiledata["name"],tiledata["texturePath"],tiledata["solid"])
    def __getattr__(self, name):
        return self.tiles[name]

TilesEnum = _TilesEnum()
