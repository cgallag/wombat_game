'''
Created on Oct 6, 2013

@author: cagallagher
'''

import pyglet
import random

class GameObject(pyglet.sprite.Sprite):
    
    def __init__(self, *args, **kwargs): 
        super(GameObject, self).__init__(*args, **kwargs) 
        self.velocity_x = 0.0 
        self.velocity_y = 0.0 
        
    def update(self, dt, windowWidth, windowHeight): 
        self.x += self.velocity_x * dt 
        self.y += self.velocity_y * dt
        self.boundingBox(windowWidth, windowHeight)
        
    def boundingBox(self, windowWidth, windowHeight):
        min_x = -self.image.width/2
        min_y = -self.image.height/2
        max_x = windowWidth + self.image.width/2
        max_y = windowHeight + self.image.height/2
        
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y
           
class Wombat(GameObject):
    
    def __init__(self, scale=0.5, *args, **kwargs):
        wombat_image = pyglet.image.load('croppedWombat.png')
        super(Wombat,self).__init__(wombat_image, *args, **kwargs)
        self.scale = scale
        
    def scaleWombat(self, y):
        return 0.5 - (0.45/260)*y
         
    def update(self, dt, windowWidth, windowHeight): 
        super(Wombat,self).update(dt, windowWidth, windowHeight)
        self.scale = self.scaleWombat(self.y)
        
    def wombatBounding(self, windowWidth, windowHeight, horizonHeight):
        max_x = windowWidth + self.image.width/2
        
        if self.x > max_x:
            self.y = random.randint(0,260)
        
        super(Wombat,self).boundingBox(windowWidth, windowHeight)
         
        
        
            