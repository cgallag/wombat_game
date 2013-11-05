'''
Created on Oct 6, 2013

@author: cagallagher
'''

import pyglet
import random
from gameobject import *

windowWidth = 1000
windowHeight = 800

window = pyglet.window.Window(caption="Wombat Insanity", fullscreen=True)

def center_image(image): 
    """Sets an image's anchor point to its center""" 
    image.anchor_x = image.width/2 
    image.anchor_y = image.height/2
    
desert_image = pyglet.image.load('australiaDesert.jpg')
desert = pyglet.sprite.Sprite(desert_image, x=0, y=0)
desert.scale = 3.5

# wombat_image = pyglet.image.load('croppedWombat.png')
# wombat = GameObject(wombat_image, x=0, y=260)
wombat = Wombat(x=0, y=500)
wombat.scale = 0.05
wombat.velocity_x = 25

gameobjs = [wombat]

def makeWombats(numWombats):
    for num in xrange(1,numWombats):
        new_wombat = Wombat(x=random.randint(0,400), y=random.randint(0,900))
        new_wombat.velocity_x = random.randint(10,100)
        new_wombat.velocity_y = random.randrange(-10,10)
        gameobjs.append(new_wombat)
        # print "made new wombat with num={}".format(num)
        
makeWombats(100)
gameobjs.sort(key=lambda x:x.y, reverse=True)

def update(dt):
    for obj in gameobjs:
        obj.update(dt, windowWidth, windowHeight)

@window.event
def on_draw():
    window.clear()
    desert.draw()
    for obj in gameobjs:
        obj.draw()

pyglet.clock.schedule_interval(update, 1/120.0) # update at 120Hz
pyglet.app.run()