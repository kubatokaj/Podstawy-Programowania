import pygame
from pygame import *

# Initializing pygame
pygame.init()

# Screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Setting up frame rate
fps_clock = pygame.time.Clock()
# Setting up screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Setting up name of the window
pygame.display.set_caption("Ping pong")

#Font
font = pygame.font.SysFont("Arial", 35)

#Variables
live_ball = False
margin = 60
p1_score = 0
p2_score = 0
fps = 60
winner = 0

#Colours
background = (7, 73, 122)
white = (255, 255, 255)

def fill_screen():
    screen.fill(background)
    pygame.draw.line(screen, white, (0, margin), (SCREEN_WIDTH, margin))

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x,y))

# Creating paddles for both players, setting up movement and screen limits
class paddle_p1():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.rect = Rect(self.x, self.y, 20, 100)
            self.speed = 5

        def move1(self):
             key = pygame.key.get_pressed()
             if key[pygame.K_UP] and self.rect.top > margin:
                  self.rect.move_ip(0, -1 * self.speed)
             if key[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
                  self.rect.move_ip(0, self.speed)
        def draw(self):
             pygame.draw.rect(screen, white, self.rect)

class paddle_p2():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.rect = Rect(self.x, self.y, 20, 100)
            self.speed = 5

        def move2(self):
             key = pygame.key.get_pressed()
             if key[pygame.K_w] and self.rect.top > margin:
                  self.rect.move_ip(0, -1 * self.speed)
             if key[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
                  self.rect.move_ip(0, self.speed)
        def draw(self):
             pygame.draw.rect(screen, white, self.rect)


class ball():
        def __init__(self, x, y):
            self.reset(x ,y)
        
        def move(self):
             # Adding collision
             # Check collision with top margin
             if self.rect.top < margin:
                self.speed_y *= -1

            # Check collision with paddles
             if self.rect.colliderect(player1_paddle) or self.rect.colliderect(player2_paddle):
                self.speed_x *= -1
            # Check collision with bottom of the screen
             if self.rect.bottom > SCREEN_HEIGHT:
                self.speed_y *= -1


            # Check for out of bounds
             if self.rect.left < 0: 
                self.winner = 1
             if self.rect.right > SCREEN_WIDTH: 
                self.winner = -1
              
             # Uptade ball position
             self.rect.x += self.speed_x
             self.rect.y += self.speed_y

             return self.winner
        
        def draw(self):
            pygame.draw.circle(screen, white, (self.rect.x + self.ball_radius, self.rect.y + self.ball_radius), self.ball_radius)

        def reset(self, x, y):
            self.x = x
            self.y = y
            self.ball_radius = 10
            self.rect = Rect(self.x, self.y, self.ball_radius * 2, self.ball_radius * 2)
            self.speed_x = -5  
            self.speed_y = 5
            self.winner = 0 # -1 is score for player 1 and 1 is score for player 2

# Create paddles
player1_paddle = paddle_p1(SCREEN_WIDTH - 40, SCREEN_HEIGHT // 2)
player2_paddle = paddle_p2(20, SCREEN_HEIGHT // 2)

# Create ball
pong_ball = ball(SCREEN_WIDTH - 70, SCREEN_HEIGHT // 2 + 50)

# Main game loop
run = True
while run:

# Setting frame rate to 60 FPS
# Limit of frame rates affects how fast both paddles and ball can move 
    fps_clock.tick(60)
    
    fill_screen()
    draw_text("Player 1: " +str(p1_score), font, white, 30,20)
    draw_text("Player 2: " +str(p2_score), font, white, SCREEN_WIDTH - 170, 20)


    #Draw paddles
    player1_paddle.draw()
    player2_paddle.draw()

    if live_ball == True:
        # Move ball
        winner = pong_ball.move()
        if winner == 0:
            #Move paddle
            player1_paddle.move1()
            player2_paddle.move2()
            # Draw ball
            pong_ball.draw()
        else:
             live_ball = False
             if winner == 1:
                  p2_score += 1
             elif winner == -1:
                  p1_score += 1

    #Move paddle
    player1_paddle.move1()
    player2_paddle.move2()

# Loop that allows to quit the game by clicking X in the top right corner
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            pong_ball.reset(SCREEN_WIDTH - 70, SCREEN_HEIGHT // 2 + 50)
    
    pygame.display.update()

pygame.quit()