from random import shuffle
import algorithms
import time
import os
import sys
import pygame


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def update(algorithm, swap1, swap2):
    screen.fill(BLACK)
    k = int(screen_width/len(algorithm.array))

    for i, height in enumerate(algorithm.array):
        color = (255, 255, 255)
        if swap1 == algorithm.array[i]:
            color = (0, 255, 0)
        elif swap2 == algorithm.array[i]:
            color = (255, 0, 0)
        pygame.draw.rect(screen, color, [i*k, screen_height - height, k, height])
    check_events()
    pygame.display.flip()


pygame.init()

BLACK = (0,  0,  0)
WHITE = (255, 255, 255)

screen_width = 1024
screen_height = 512
size = [screen_width, screen_height]
screen = pygame.display.set_mode(size)
screen.fill(BLACK)

pygame.display.set_caption("Visualizer")
clock = pygame.time.Clock()

algo = algorithms.LSDRadixSort()
algo.run()

while True:
    check_events()
    pygame.display.flip()
