import pygame
import sys
#Test
pygame.init()

# Set up the display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Girl Drawing")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 192, 203)
blue = (0, 0, 255)
brown = (139, 69, 19)
red = (255, 0, 0)

def draw_girl():
    # Draw the girl's head
    pygame.draw.circle(screen, pink, (200, 150), 60)

    # Draw the girl's body
    pygame.draw.rect(screen, blue, (170, 210, 60, 100))

    # Draw the girl's hair (simple representation)
    pygame.draw.arc(screen, brown, (140, 110, 120, 80), 0, 3.14)

    # Draw the girl's eyes
    pygame.draw.circle(screen, black, (175, 135), 10)
    pygame.draw.circle(screen, black, (225, 135), 10)

    # Draw the girl's mouth (simple representation)
    pygame.draw.arc(screen, red, (175, 150, 50, 30), 0, 3.14)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    draw_girl()
    pygame.display.flip()

pygame.quit()
sys.exit()
