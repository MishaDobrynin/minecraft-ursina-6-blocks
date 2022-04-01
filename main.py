import random

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

sky_texture = load_texture('assets/skybox.png')
grass = load_texture('assets/grass_14.png')
stone = load_texture('assets/stone.png')
brick = load_texture('assets/brick.png')
ironOre = load_texture('assets/ironOre.png')
gold = load_texture('assets/gold.png')
emeraldOre = load_texture('assets/emeraldOre.png')

c = color.green
t = grass

def update():
    global t,c
    if held_keys['1']:
        t = grass
        c = color.green
    if held_keys['2']:
        t = stone
        c = color.light_gray
    if held_keys['3']:
        t = brick
        c = color.rgb(203,65,84)
    if held_keys['4']:
        t = ironOre
        c = color.light_gray
    if held_keys['5']:
        t = emeraldOre
        c = color.light_gray
    if held_keys['6']:
        t = gold
        c = color.yellow

class Voxel(Button):
    def __init__(selfself, position=(0,0,0), co = color.green, te = grass):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            color = co,
            texture = te,
            #color = color.color(0,0,random.uniform(.9,1.0)),
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position = self.position + mouse.normal, co = c, te = t)
            if key == 'right mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True,
        )



for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))
sky = Sky()
player = FirstPersonController()
app.run()