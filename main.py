import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Coming Soon")

width, height = screen.get_size()

font = pygame.font.Font(None, 80)

text = "Coming soon..."
text_surface = font.render(text, True, (255, 255, 255))

text_rect = text_surface.get_rect(center=(width // 2, height // 2))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press ESC to exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))

    screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()