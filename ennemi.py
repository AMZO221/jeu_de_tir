import pygame

class Ennemy:
    def __init__(self,x,y):
        self.x =x
        self.y=y
        self.largeur=50
        self.hauteur=50
        self.vilosite= 5
        self.color="purple"
        self.rect= pygame.Rect(self.x,self.y,self.largeur,self.hauteur)
        self.vies= 3
        self.image = pygame.image.load("python fill/jeu de tir/zombie.png")
        self.image = pygame.transform.scale(self.image, (self.largeur,self.hauteur))
        self.image = pygame.transform.rotate(self.image,0)
    def dessin(self,fenetre):
        self.rect= pygame.Rect(self.x,self.y,self.largeur,self.hauteur)
        #pygame.draw.rect(fenetre,self.color , self.rect)
        fenetre.blit(self.image, (self.x,self.y))
        
    def mouvements(self):
        self.y += self.vilosite