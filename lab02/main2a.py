import pygame

pygame.init() #inicia diversas funcionalidades do pygame

#retorna uma tela pronta com a dimensão passada por parametro
screen = pygame.display.set_mode((600,400)) 

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            pygame.quit()
            exit()

    screen.fill((255,255,255)) #preenche a tela com uma determinada cor
    pygame.display.flip() #atualiza o display


    