import pygame
from smbus import SMBus

addr = 0x8
bus = SMBus(1)


#We must open a Pygame window to allow it to detect user events
screen = pygame.display.set_mode([240, 160])

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				print('Right')
				bus.write_byte(addr, 0x4)
			if event.key == pygame.K_LEFT:
				print('Left')
				bus.write_byte(addr, 0x3)
			if event.key == pygame.K_UP:
				print('Up')
				bus.write_byte(addr, 0x1)
			if event.key == pygame.K_DOWN:
				print('Down')
				bus.write_byte(addr, 0x2)
			if event.key == pygame.K_t:
			    print('stop')
			    bus.write_byte(addr, 0x0)
			if event.key == pygame.K_q:
				pygame.quit()

