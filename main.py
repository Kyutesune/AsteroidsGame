# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	#order matters, these are created to create container fields to assign to player
	updatable	=	pygame.sprite.Group()
	drawable	=	pygame.sprite.Group()
	asteroidList 	= pygame.sprite.Group()

	#player gets created to contain these items after they have been generated above
	Asteroid.containers = (updatable, drawable, asteroidList)
	Player.containers = (updatable, drawable)
	AsteroidField.containers = (updatable)
	#generate player after containers are assigned
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroids = AsteroidField()

	dt = 0
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for item in updatable:
			item.update(dt)
		for asteroids in asteroidList:
			if(asteroids.checkCollision(player)):
				print("Game Over!")
				pygame.QUIT
				sys.exit()
		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
	main()
