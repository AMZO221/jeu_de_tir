import pygame

class Balle:
    def __init__(self,x,y):
        self.x =x
        self.y=y
        self.largeur=10
        self.hauteur=10
        self.vilosite= 10
        self.color="white"
        self.rect= pygame.Rect(self.x,self.y,self.largeur,self.hauteur)
        self.image = pygame.image.load("python fill/jeu de tir/boulle de feu.png")
        self.image = pygame.transform.scale(self.image, (self.largeur,self.hauteur))
        self.image = pygame.transform.rotate(self.image,45)
    def dessin(self,fenetre):
        self.rect= pygame.Rect(self.x,self.y,self.largeur,self.hauteur)
        #pygame.draw.rect(fenetre,self.color , self.rect)
        fenetre.blit(self.image, (self.x,self.y))
        
    def mouvements(self):
        self.y -= self.vilosite