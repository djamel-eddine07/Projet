import pygame as py

# Dimensions de la fenêtre
LARGUEUR, HAUTEUR = 800, 600

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
C_FOND = (0, 0, 0)

# Images (ajustez les chemins selon vos fichiers)
#logo = py.image.load('LOGO.png')
fond = py.image.load('fond.png')
pac_g = py.image.load('pac.png')
fant = py.image.load('fond.png')
boule_j = py.image.load('boule.png')

# Position et direction initiales
Xpm, Ypm = 100, 100
DIRECTION = "droite"
DIRECTION_last = "droite"
DIRECTION_next = "droite"
direct = ["haut", "bas", "gauche", "droite"]

# Taille des éléments
cote = 20

# Fantômes
fantome = [[300, 300], [400, 400]]

# Bonbons
bonbon = [[200, 200], [250, 250]]

# Score
score = 0

# Compteur et vitesse
compteur = 0
speed = 5

def avance_pac(Xpm, Ypm, Xpm_last, Ypm_last, DIRECTION, DIRECTION_last, DIRECTION_next, DIRECTION_com, cote, touche):
    # Logique de mouvement de Pacman
    if touche:
        DIRECTION = DIRECTION_com
    if DIRECTION == "haut":
        Ypm -= cote
    elif DIRECTION == "bas":
        Ypm += cote
    elif DIRECTION == "gauche":
        Xpm -= cote
    elif DIRECTION == "droite":
        Xpm += cote
    return Xpm, Ypm, DIRECTION, DIRECTION_last, DIRECTION_next, DIRECTION_com

def avance_fantome(fantome, cote):
    # Logique de mouvement des fantômes
    for f in fantome:
        f[0] += cote if f[0] % 2 == 0 else -cote
        f[1] += cote if f[1] % 2 == 0 else -cote
    return fantome

def fin_loose(fenetre, score):
    # Affichage de la fin de jeu en cas de défaite
    font = py.font.Font(None, 74)
    texte = font.render(f"Perdu! Score: {score}", True, BLANC)
    fenetre.blit(texte, (LARGUEUR // 2 - texte.get_width() // 2, HAUTEUR // 2 - texte.get_height() // 2))
    py.display.flip()
    py.time.wait(3000)

def fin_win(fenetre, score):
    # Affichage de la fin de jeu en cas de victoire
    font = py.font.Font(None, 74)
    texte = font.render(f"Gagné! Score: {score}", True, BLANC)
    fenetre.blit(texte, (LARGUEUR // 2 - texte.get_width() // 2, HAUTEUR // 2 - texte.get_height() // 2))
    py.display.flip()
    py.time.wait(3000)
