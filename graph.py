import sys, pygame
pygame.init()

size = width, height = 1420, 640
black = 0, 0, 0
white = 255, 255, 255

def bar_graph(a_list):
	n = len(a_list)
	left = 10
	unit = (height - 10.0)/max(a_list)
	
	screen = pygame.display.set_mode(size)
	screen.fill(black)
	for i in a_list:
		Rect = pygame.Rect(left, (height - 10) - unit*i, width/n, unit*i)
		left = left + (width/n) + 2
		pygame.draw.rect(screen, white, Rect)
	
	while 1:
		pygame.display.flip()


