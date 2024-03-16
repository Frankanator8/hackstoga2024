import sys

import pygame

from game.game import Game
from game.menu import Menu
from game.track import Track
from render.renderer import Renderer

#tracker
import cv2
import mediapipe as mp
import imutils

pygame.init()
screen = pygame.display.set_mode((900, 600))
renderer = Renderer()

clock = pygame.time.Clock()
game = Game(renderer)
menu = Menu(renderer, game)

char = pygame.image.load(r'assets/Cyborg idle 1.png') 
char_x = 170
char_y = 170

hands_mp = mp.solutions.hands
draw = mp.solutions.drawing_utils
cam = cv2.VideoCapture(0)
img_w = 900
hand_positions = []
frame_distance = 30
movement_threshold_x = img_w / 15
movement_threshold_y = img_w / 15
move_cooldown = 30
move_cooldown_timer = 0

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    dt = clock.get_time()/1000

    renderer.render(screen)
    if menu.active:
        menu.tick(pygame.mouse.get_pressed()[0], pygame.mouse.get_pos())

    else:
        game.tick(dt)
        menu.tick_passive()

    clock.tick()
    screen.blit(char, (char_x, char_y)) 

    pygame.display.update()

# tracker 
    is_on, image = cam.read()
    image_height, image_width, dp = image.shape
    move_cooldown_timer +=1

    #brg to rgb. cv2 is weird and does brg, WHO DOES BRG?!?!
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #Appying media pipe
    image_with_mp = hands_mp.Hands().process(image)
    #BACK TO CV2! Gotta convert back
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    if image_with_mp.multi_hand_landmarks: # as long as there is a hand: draw on
        for hand_lm in image_with_mp.multi_hand_landmarks:
            draw.draw_landmarks(image, hand_lm,connections=hands_mp.HAND_CONNECTIONS)
        for ids, lm in enumerate(hand_lm.landmark):
            x = lm.x * image_width
            y = lm.y * image_height
            hand_positions.append([x,y])
            char_x = min((int(x / 130) * 130 + 80), 3 * 130 + 80)
            char_y = min((int(y / 130) * 130 + 80), 3 * 130 + 80)


    print(char_x, char_y)
    image = imutils.resize(image, width=img_w)
    cv2.imshow('Midnight Dancer', image)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break
    

pygame.quit()
sys.exit()
