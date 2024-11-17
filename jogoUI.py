#IGNORE ESSE ARQUIVO POR ENQUANTO
import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Configurações da janela
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Jornada Épica")

# Configurações do jogador
player_image = pygame.image.load("imagens/Player.png") 
background_image = pygame.image.load("imagens/background.jpg")
player_size = 40
player_image = pygame.transform.scale(player_image, (player_size, player_size))
background_image = pygame.transform.scale(background_image, (600, 600))
player_x, player_y = 600 // 2, 600 // 2
player_speed = 5

# Configurações do jogo
running = True
while running:
    # Preencher a tela com cor branca
    screen.blit(background_image, (0,0))
    
    # Eventos de movimento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Limitar o movimento do jogador aos limites da tela
    player_x = max(0, min(600 - player_size, player_x))
    player_y = max(0, min(600 - player_size, player_y))

    # Desenhar o personagem na tela
    screen.blit(player_image, (player_x, player_y))

    # Atualizar a tela
    pygame.display.flip()

    # Processar eventos de saída
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controle de FPS
    pygame.time.Clock().tick(30)

# Finalizar o Pygame
pygame.quit()
sys.exit()
