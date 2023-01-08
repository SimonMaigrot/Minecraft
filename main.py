from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise
from random import randint

app  = Ursina()

window.color = color.rgb(0, 200, 250)
window.exit_button.visible = False
window.borderless = False
window.fullscreen = True

grassStrokeTex = load_texture('assets/grass.jpg')

def input(key):
    if key == 'q' or key == 'escape':
        quit()

def update():
    pass

terrain = Entity(model = None, collider = None)
noise = PerlinNoise(octaves = 1, seed = 1)
amp = 3
freq = 12

terrainWidth = 32
for i in range(terrainWidth*terrainWidth):
    bud = Entity(model = 'cube', texture = grassStrokeTex)
    bud.x = floor(i / terrainWidth)
    bud.z = floor(i % terrainWidth)
    bud.y = floor((noise([bud.x/freq, bud.z/freq]))*amp)
    bud.parent = terrain

terrain.combine()
terrain.collider = 'mesh'
terrain.texture = grassStrokeTex

subject = FirstPersonController()
subject.x = subject.z = 5
subject.y = 12

app.run()