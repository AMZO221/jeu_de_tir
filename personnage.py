import pygame

class Cube:
    def __init__(self,x,y):
        self.x =x
        self.y=y
        self.largeur=25
        self.hauteur=25
        self.vilosite=5
        self.color="red"
        self.rect= pygame.Rect(self.x,self.y,self.largeur,self.hauteur)
        self.image = pygame.image.load("python fill/jeu de tir/char.png")
        self.image = pygame.transform.scale(self.image, (self.largeur,self.hauteur))
        self.image = pygame.transform.rotate(self.image,90)
    def dessin(self,fenetre):
        self.rect= pygame.Rect(self.x,self.y,self.largeur,self.hauteur)
        #pygame.draw.rect(fenetre,self.color , self.rect)
        fenetre.blit(self.image, (self.x,self.y))