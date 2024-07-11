import pygame as py
import module_pm as m

# Initialisation de Pygame
py.init()

# Initialisation de la fenêtre graphique avec son nom
fenetre = py.display.set_mode((m.LARGUEUR, m.HAUTEUR), py.DOUBLEBUF | py.HWSURFACE)
py.display.set_caption("PAC MAN P.A.")

# Vérification des paramètres d'affichage dans le terminal :
print(py.display.Info())

# Fonction pour afficher le menu principal
def afficher_menu(fenetre):
    fenetre.fill(m.NOIR)
    font = py.font.Font(None, 74)
    titre = font.render("PAC MAN P.A.", True, m.BLANC)
    fenetre.blit(titre, (m.LARGUEUR // 2 - titre.get_width() // 2, 100))
    
    font = py.font.Font(None, 36)
    jouer = font.render("1. Jouer", True, m.BLANC)
    reglement = font.render("2. Règlement", True, m.BLANC)
    quitter = font.render("3. Quitter", True, m.BLANC)
    
    fenetre.blit(jouer, (m.LARGUEUR // 2 - jouer.get_width() // 2, 300))
    fenetre.blit(reglement, (m.LARGUEUR // 2 - reglement.get_width() // 2, 350))
    fenetre.blit(quitter, (m.LARGUEUR // 2 - quitter.get_width() // 2, 400))
    
    py.display.flip()

# Fonction pour afficher le sous-menu de sélection de difficulté
def afficher_menu_difficulte(fenetre):
    fenetre.fill(m.NOIR)
    font = py.font.Font(None, 74)
    titre = font.render("Sélectionner la difficulté", True, m.BLANC)
    fenetre.blit(titre, (m.LARGUEUR // 2 - titre.get_width() // 2, 100))
    
    font = py.font.Font(None, 36)
    facile = font.render("1. Facile", True, m.BLANC)
    moyen = font.render("2. Moyen", True, m.BLANC)
    difficile = font.render("3. Difficile", True, m.BLANC)
    
    fenetre.blit(facile, (m.LARGUEUR // 2 - facile.get_width() // 2, 300))
    fenetre.blit(moyen, (m.LARGUEUR // 2 - moyen.get_width() // 2, 350))
    fenetre.blit(difficile, (m.LARGUEUR // 2 - difficile.get_width() // 2, 400))
    
    py.display.flip()

# Fonction principale pour gérer le jeu
def main():
    fenetre = py.display.set_mode((m.LARGUEUR, m.HAUTEUR), py.DOUBLEBUF | py.HWSURFACE)
    py.display.set_caption("PAC MAN P.A.")
    
    clock = py.time.Clock()
    menu_principal = True
    selection_difficulte = False
    running = False
    vitesse_fantomes = 5

    while True:
        if menu_principal:
            afficher_menu(fenetre)
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    return
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_1:
                        menu_principal = False
                        selection_difficulte = True
                    elif event.key == py.K_2:
                        # Afficher le règlement
                        pass
                    elif event.key == py.K_3:
                        py.quit()
                        return

        elif selection_difficulte:
            afficher_menu_difficulte(fenetre)
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    return
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_1:
                        vitesse_fantomes = 5
                        selection_difficulte = False
                        running = True
                    elif event.key == py.K_2:
                        vitesse_fantomes = 10
                        selection_difficulte = False
                        running = True
                    elif event.key == py.K_3:
                        vitesse_fantomes = 15
                        selection_difficulte = False
                        running = True

        elif running:
            # Placez ici le code de votre jeu (le cœur du programme)
            m.speed = vitesse_fantomes
            fenetre.blit(m.fond, [0, 0])
            fenetre.blit(m.pac_g, [m.Xpm, m.Ypm])
            for i in m.fantome:
                fenetre.blit(m.fant, [i[0], i[1]])
            py.display.flip()
            
            # Placez le cœur de votre jeu ici
            A = True
            while A and running:
                for event in py.event.get():
                    if event.type == py.QUIT:
                        A = False
                        running = False
                        break
                    if event.type == py.KEYDOWN:
                        if event.key == py.K_SPACE:
                            A = False
                            break
                    elif event.type == py.MOUSEBUTTONDOWN:
                        if event.button == 3:
                            A = False
                            break
                
                # Placez ici le reste de la logique de votre jeu
                m.Xpm, m.Ypm, m.DIRECTION, m.DIRECTION_last, m.DIRECTION_next, m.DIRECTION_com = m.avance_pac(
                    m.Xpm, m.Ypm, m.Xpm_last, m.Ypm_last, m.DIRECTION, m.DIRECTION_last, m.DIRECTION_next, m.DIRECTION_com, m.cote, True)
                m.fantome = m.avance_fantome(m.fantome, int(m.cote))

                for i in m.fantome:
                    if i[0] == m.Xpm and i[1] == m.Ypm:
                        m.fin_loose(fenetre, m.score)
                        running = False
                        break

                if m.score == 200:
                    m.fin_win(fenetre, m.score)
                    running = False
                    break

                fenetre.blit(m.pac[m.direct.index(m.DIRECTION)], [m.Xpm, m.Ypm])
                for i in m.fantome:
                    fenetre.blit(m.fant, [i[0], i[1]])

                m.compteur += 1
                py.time.delay(m.speed)
                py.display.flip()
            
            clock.tick(60)

if __name__ == "__main__":
    main()
