import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #Class manages bullets form ship

    def __init__(self, ai_settings, screen, ship):
        #Creates bullet object at ship position
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #Move the bullet up the screen
        #Update the decimal position of the bullet.
        self.y -= self.speed_factor
        
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        #Draw the bullet
        pygame.draw.rect(self.screen, self.color, self.rect)







"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
	# This is the class that manages bullets fired form the ship 
	# create bullet object At ships current position
	super(Bullet, self).__init__()
        self.screen = screen
	
	#Create bullet rect at (0,0) and then set the correct position
	self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
	self.rect.acenterx = self.rect.centerx
	self.rect.top = ship.rect.top
	
	# Store the bullet's position as a decimal value
	self.y = float(self.rect.y)
	
	self.color = ai_settings.bullet.color
	self.speed_factor - ai_settings.bullet_speed_factor 
	
    def update(self):
	# Move the bullet up the screen
	# update the decimal position of the bullet 
	self.y -= self.speed_factor
	
	# update the rect position
	self.rect.y = self.y
	
    def draw_bullet(self):
	# Draw the bullet on screen
	pygame.draw.rect(sef.screen, self.color, self.rect)
	
"""
