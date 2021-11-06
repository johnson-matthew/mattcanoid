import os
import pygame
from screeninfo import get_monitors

TITLE = "mattcanoid (matthew's arcanoid clone)"
WIDTH = 800
HEIGHT = 600

monitor = get_monitors().pop()
display_width = monitor.width
display_height = monitor.height

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (display_width // 2 - WIDTH // 2, display_height // 2 - HEIGHT // 2)
pygame.display.init()

import pgzrun
import random

paddle = Actor("paddle.png")
paddle.x = 400
paddle.y = 580

ball = Actor("ball.png")
ball.x = 400
ball.y = 557

ball_x_speed = 0
ball_y_speed = 0

bars_list = []
bar_x = 65
bar_y = 0

bars_colors_list = ["bar_red_rectangle.png",
                    "bar_green_rectangle.png",
                    "bar_blue_rectangle.png",
                    "bar_yellow_rectangle.png"]

def place_bars(x, y, image):
    for i in range(10):
        bar = Actor(image)
        bar.x = x
        bar.y = y
        bars_list.append(bar)
        x += 74

for bar_color in bars_colors_list:
    bar_x = 65
    bar_y += 42
    place_bars(bar_x, bar_y, bar_color)

def draw():
    screen.blit("background.jpg", (0, 0))
    screen.draw.text("Press any key to start...", center=(WIDTH // 2, HEIGHT // 2))
    paddle.draw()
    ball.draw()
    for bar in bars_list:
        bar.draw()

def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH - 11) or (ball.x <= 11):
        ball_x_speed *= -1
    if (ball.y <= 11):
        ball_y_speed *= -1
    if (ball.y >= HEIGHT):
        ball_y_speed *= -1

def on_key_down():
    global ball_x_speed, ball_y_speed
    if (ball_x_speed == 0) and (ball_y_speed == 0):
        screen.blit("background.jpg", (0, 0))
        ball_x_speed, ball_y_speed = 3, 3

def update():
    global ball_x_speed, ball_y_speed
    update_ball()
    if paddle.colliderect(ball):
        ball_y_speed *= -1
        rand = random.randint(0, 1)
        if rand:
            ball_x_speed *= -1
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1
            rand = random.randint(0, 1)
            if rand:
                ball_x_speed *= -1
    if keyboard.left and (paddle.x >= 52):
        paddle.x -= 5
    if keyboard.right and (paddle.x <= WIDTH - 52):
        paddle.x += 5

pgzrun.go()