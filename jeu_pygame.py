import pygame
from personnage import Cube
from ennemi import Ennemy
from balle import Balle
#from acceuil import Debut
import random

pygame.init()
pygame.mixer.init()

largeur = 400
hauteur = 500
fenetre = pygame.display.set_mode([largeur, hauteur])
fps = 60
horloge=pygame.time.Clock()
temps_de_passage = 0
temps_entre_ennemis = 700
vie  = 5
points = 0
balles = []

balle_ultime = 0
temps_entre_balles = 100

fond = pygame.font.SysFont("Comic Sans", 20)

def creer_balle():
    global balle_ultime
    
    if ((pygame.time.get_ticks() - balle_ultime) > temps_entre_balles):
        balles.append(Balle(cube.rect.centerx,cube.rect.centery))
        balle_ultime = pygame.time.get_ticks()

def gestionnaire_teclas(teclas):
    if teclas[pygame.K_UP]:
        cube.y -= cube.vilosite
    if teclas[pygame.K_DOWN]:
        cube.y += cube.vilosite
    if teclas[pygame.K_LEFT]:
        cube.x -= cube.vilosite
    if teclas[pygame.K_RIGHT]:
        cube.x += cube.vilosite
    if teclas[pygame.K_SPACE]:
        creer_balle()

cube = Cube(largeur/2,hauteur-75)
mechants = []
mechants.append(Ennemy(largeur/2, 100))
jeux = True
while jeux and vie>0:
    temps_de_passage += horloge.tick(fps)
    if (temps_de_passage > temps_entre_ennemis):
        mechants.append(Ennemy(random.randint(0,largeur-50),-100)) 
        temps_de_passage = 0
    
    
    teclas = pygame.key.get_pressed()
    text_vie = fond.render(f"VIES : {vie}",True,"white")
    text_point = fond.render(f"SCORE : {points}",True,"white")
    gestionnaire_teclas(teclas)
    fenetre.fill("black")
    cube.dessin(fenetre) 
    
    for mechant in mechants:
        mechant.dessin(fenetre)
        mechant.mouvements()
        
        if (pygame.Rect.colliderect(cube.rect, mechant.rect)):
            vie -= 1
            mechants.remove(mechant)
            
        if (mechant.y > hauteur):
            # points += 1
            mechants.remove(mechant)
        #if (mechant.vies <= 0):
            # mechants.remove(mechant)
        for balle in balles:
            if balle.y <= 0:
                balles.remove(balle)
            if pygame.Rect.colliderect(balle.rect, mechant.rect):
                #mechant.vies -= 1 
                mechants.remove(mechant)                                                                                  
                points = points + 1
    
    for balle in balles:
        balle.dessin(fenetre)
        balle.mouvements()
    fenetre.blit(text_vie, (20, 20))
    fenetre.blit(text_point, (20, 50))
    pygame.display.update()
#debut = Debut(50,50)
#debut.dessin(fenetre)
    evenements = pygame.event.get()
    for evenement in evenements:
        if evenement.type == pygame.QUIT:
            jeux = False
quit()