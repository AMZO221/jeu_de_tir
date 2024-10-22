import pygame

class Debut:
    def __init__(self,x,y):
        self.x =x
        self.y=y
        self.largeur=400
        self.hauteur=500
        # self.vilosite=5
        # self.color="red"
        self.rect= pygame.Rect(self.x,self.y,
                            self.largeur,self.hauteur)
        self.image = pygame.image.load("python fill/jeu de tir/petit soldat.jpeg")
        self.image = pygame.transform.scale(self.image, (self.largeur,self.hauteur))
        self.image = pygame.transform.rotate(self.image,0)
    def dessin(self,fenetre):
        self.rect= pygame.Rect(self.x,self.y,
                            self.largeur,self.hauteur)
        #pygame.draw.rect(fenetre,self.color , self.rect)
        fenetre.blit(self.image, (self.largeur,self.hauteur))