import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group

import game_functions as gf

def run_game():
	#Initialize game and create a screen object"
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
	pygame.display.set_caption("Alien Invasion")


	#make a ship
	ship = Ship(ai_settings,screen)

	#Make a goup to store bullets in
	bullets = Group()

	

	#Start the main loop for the game
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_screen(ai_settings,screen,ship,bullets)



run_game()
