import pygame
from pygame.locals import *
pygame. init()

window=pygame.display.set_mode((1000,700))  #taille de la fenêtre soit 1000 pixel en abscisse(x) et 700 pixels en ordonnée(y)
screen=pygame.display.get_surface()


#chargement des images

    #image de la page d'acceuil
fondpage=                pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Fond2.PNG")
Jouer=                   pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Jouer.PNG")
Jouerclic=               pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Jouerclic.PNG")
Bandeau=                 pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Bandeau.PNG")
smiley=                  pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Player.PNG")
credits=                 pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Credits.PNG")
creditsclic=             pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Creditsclic.PNG")
S=                       pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/S.PNG")
N=                       pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/N.PNG")
E=                       pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/E.PNG")
A=                       pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/A.PNG")
key=                     pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/key.PNG")
fond=                    pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/fondvert.PNG")

    #images standart du jeu
terrain=                 pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/limbyrintheterrain2.PNG")
joueur=                  pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/player1.PNG")
ordi=                    pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/ordi.PNG")#ordi

    #fonds divers du jeu
gameover=                pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/gameover.PNG")#game over
fond_coupe=              pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Coupe.PNG")

    #confetti
conf_1=                  pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/conf_1.PNG")
conf_2=                  pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/conf_2.PNG")
conf_3=                  pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/conf_3.PNG")

    #images des vies
vie1=                    pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/vie1.PNG")#vies pleines
vie2=                    pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/vie2.PNG")#vies vides

    #images des étoiles
etoile1=                 pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/etoile1.PNG")#étoiles noirs
etoile2=                 pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/etoile2.PNG")#étoiles jaune
etoile3=                 pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/etoile3.PNG")#étoiles tournées
etoile4=                 pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/etoile4.PNG")#étoiles gagnées
etoile5=                 pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/etoile5.PNG")#étoiles rouge de fin

    #images du levier
Manivelle_bas=           pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Manivelle_bas.PNG")
Manivelle_bas_levier=    pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Manivelle_bas_levier.PNG")
Manivelle_bas_sortie=    pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Manivelle_bas_sortie.PNG")
Manivelle_haut=          pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Manivelle_haut.PNG")
Manivelle_haut_levier=   pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Manivelle_haut_levier.PNG")
Manivelle_haut_sortie=   pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Manivelle_haut_sortie.PNG")
Manivelle_milieu=        pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Manivelle_milieu.PNG")
porte_rose=              pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/porte_rose.PNG")
porte_violette=          pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/porte_violette.PNG")
levier_rose=             pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/levier_rose.PNG")
levier_violet=           pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/levier_violet.PNG")

    #images du menu pause
image_menu_pause=        pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_menu_pause.PNG")
Reprendre=               pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Reprendre.PNG")
Reprendreclic=           pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Reprendreclic.PNG")
Quitter_pause=           pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Quitter_pause.PNG")
Quitter_pauseclic=       pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Quitter_pauseclic.PNG")
image_bouton_pause=      pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_pause.PNG")
image_bouton_pause_selectionne=pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_pause_selectionne.PNG")

    #image du menu crédit
Quitter=                 pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Quitter.PNG")
Quitterclic=             pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/Quitter2.PNG")
auteurs=                 pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/developpeurs.PNG")

    #images pour le son
image_son_monte=         pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_son_monte.PNG")
image_son_monte_appuye=  pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_son_monte_appuye.PNG")
image_son_baisse=        pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_son_baisse.PNG")
image_son_baisse_appuye= pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_son_baisse_appuye.PNG")
image_son_allume=        pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_son_allume.PNG")
image_son_allume_appuye= pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_son_allume_appuye.PNG")
image_son_coupe=         pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_son_coupe.PNG")
image_son_coupe_appuye=  pygame.image.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/image_son_coupe_appuye.PNG")


#chargement des musiques et des sons
pygame.mixer.music.load("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/sneaky_music.wav")
son_etoile =             pygame.mixer.Sound("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/sonsympa.wav")
sontoucher =             pygame.mixer.Sound("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/petitbruit.wav")#son toucher ordi
sonclic =                pygame.mixer.Sound("C:/Users/Utilisateur/Desktop/Pyzo/Sneaky/imagesons/clic.wav")

#58 images, 3 sons et 1 musiques

#initialiser les variables

    #communes
continuer=1                 #si variable=1 -> on y rentre           si variable=0 -> on n'y rentre pas ou on y sort
boucle_menu=1
boucle_jeu=0
boucle_pause=0
boucle_credit=0
boucle_levier=0
boucle_fin=0
touche=0
touche_entree=0
touche_shift=0

    #menu d'accueil
imageaff=0
x_smiley=500
x_S=0
x_N=58
x_E=121
x_A=169
x_key=225
commencement=0
    
    #ordinateurs
x_ordi_1=20     #emplacement initiale des ordis
y_ordi_1=36
x_ordi_2=173
y_ordi_2=530
x_ordi_3=395
y_ordi_3=34
x_ordi_4=111
y_ordi_4=215
x_ordi_5=273
y_ordi_5=350
x_ordi_6=560
y_ordi_6=130
x_ordi_7=586
y_ordi_7=210
variable1=4    #vitesse des ordis
variable2=3
variable3=1
variable4=4
direction_5=1 #(sens de direction des ordis 5 et 6)
direction_6=1
variable5=3
variable6=4
variable7=1.5
    
    #étoiles
toucher_etoile_1=1  #toucher_etoile correspond si le joueur passe sur les coordonnées de l'étoiles
toucher_etoile_2=1
toucher_etoile_3=1
toucher_etoile_4=1
rotation_etoile_1=1 #rotation_etoile correspond si le jeu doit afficher l'étoile complète ou l'étoile tournée
rotation_etoile_2=1
rotation_etoile_3=1  
rotation_etoile_4=1   
temps_rotation_1=0  #temps_rotation correspond aux nombres de tours de la boucle (ici 25) avent de tourner l'étoile
temps_rotation_2=0
temps_rotation_3=0
temps_rotation_4=0
ordre_etoile=0      #ordre_etoile correspond aux nombres d'étoile attrapées
etoile_1_gagnee=0   #etoile_gagnee correspond valider notre premier passage sur les coordonnées de l'étoile et ainsi ignorer les autres
etoile_2_gagnee=0
etoile_3_gagnee=0
etoile_4_gagnee=0

    #vies
vie_restante = 3    #nombre de vie qu'il nous reste
recommencer = 0     #lorsque l'on perd une vie
zero_vie=0          #lorsque l'on n'a plus de vie

    #personnage et souris
x_perso=122            
y_perso=11 
x_souris=0
y_souris=0

    #manipulation du son
aff_son_allume_coupe=0
changement_son=1
aff_son_baisse=0
aff_son_monte=0
volume=0.5

    #levier
porte_rose_ouverte=1
porte_violette_ouverte=1
activation_rose=0
activation_violet=0
arriver_levier=0

    #score final
score = 0
score_etoile=0
score_vie=0
temps_score=0
temps_jeu=0

    #menu pause
imageaff_reprendre=0
imageaff_quitter=0

    #confetti
conf=0

#initialisation du texte
blanc=(255,255,255)
taille_texte=pygame.font.SysFont(None,50)
score_texte=taille_texte.render(str(score),1,blanc)


#pouvoir rester appuyer sur les boutons pour pouvoir jouer fluidement
pygame.key.set_repeat(10,10) #1er 10: le temps de fluidité entre la première pression et le reste
                             #2e: le temps de pose entre chaques intervalles
                            
#jouer la musique
pygame.mixer.music.play(loops=-1) #play(loops=-1) permet de répéter en boucle la musique
pygame.mixer.music.set_volume(volume) #permet de contrôler l'intensité du son (entre 0 et 1)

#boucle du programme principale _______________________________________________________________________________________________________________________________ _______________________________________________________________________________________________________________________________________________________________

while continuer==1:
    #variable remise à zéro pour chaque tour
    touche=0
    touche_entree=0
    touche_shift=0
    image=0
    imageaff=0
    imageaff2=0
    aff_son_allume_coupe=0
    aff_son_baisse=0
    aff_son_monte=0
    imageaff_reprendre=0
    imageaff_quitter=0
    imageaff_pause=0
    imageaff_quitter_credit=0
    
    #initialisation des touches du clavier et de la souris
    for event in pygame.event.get():    #_get() -> le programme tourne et agit lorsqu'on intervient   =! _wait() qui attends sans tourner
        if event.type ==QUIT:    #appuyer sur la croix
            continuer=0                    #quitter le programme
        if event.type==KEYDOWN:     #clavier
            if event.key==K_SPACE:    #touche_espace
                continuer=0        #changement de variable de la boucle pour quitter le programme
        
            if event.key == K_DOWN: #fléche du bas
                y_perso=y_perso+2
                    
            if event.key==K_UP: #fèche du haut
                y_perso=y_perso-2
                    
            if event.key==K_RIGHT: #flèche de droit
                x_perso=x_perso+2
                        
            if  event.key==K_LEFT: #flèche de gauche
                x_perso=x_perso-2
                
            if event.key==K_RETURN: #la touche entrée
                touche_entree=1
                
            if event.key== K_RSHIFT: #touche shift droit
                touche_shift=1
                
        
        if event.type == MOUSEMOTION:	#Si la souris bouge
            x_souris = event.pos[0] #détermine les positions en x de la souris
            y_souris = event.pos[1] #détermine les positions en y de la souris

            
        if event.type == MOUSEBUTTONUP and event.button == 1: # si on appuie sur la souris ET s'il s'agit du clic gauche
                touche=1


    #début de la parti du menu principal_______________________________________________________________________________________________________________________
    if boucle_menu==1:  
        
        
        
        #programme
        
        if x_souris>150 and y_souris>50 and x_souris<815 and y_souris<200 or touche_entree==1:  #bouton jouer
            imageaff=1
            if touche==1 or touche_entree==1:
                commencement=0
                boucle_jeu=1
                boucle_menu=0
                sonclic.play()
                touche_entree=0
        
        
        if x_souris>150 and y_souris>270 and x_souris<815 and y_souris<420: #bouton crédit
            imageaff2=2
            if touche==1:
                boucle_credit=1
                boucle_menu=0
                sonclic.play()
        
        x_smiley=x_smiley+8
        if x_smiley>1000:
            x_smiley=0
        
        x_S=x_S+8
        if x_S>1000:
            x_S=0
        
        x_N=x_N+8
        if x_N>1000:
            x_N=0
        
        x_E=x_E+8
        if x_E>1000:
            x_E=0  
            
        
        x_A=x_A+8
        if x_A>1000:
            x_A=0  

            
        x_key=x_key+8
        if x_key>1000:
            x_key=0        
        
            
            
        
        #affichage des images
        
        screen.blit(fondpage,(0,0))                  
        screen.blit(Bandeau,(0,500))
        screen.blit(smiley,(x_smiley,530))
        screen.blit(S,(x_S,530))
        screen.blit(N,(x_N,528))
        screen.blit(E,(x_E,530))
        screen.blit(A,(x_A,532))
        screen.blit(key,(x_key,531))
        
        if imageaff==0:     #pour montrer au joueur qu'il peut appuyer sur le bouton
            screen.blit(Jouer,(145,50))
            
        elif imageaff==1:
            screen.blit(Jouerclic,(150,50))
            
        if imageaff2==0:
            screen.blit(credits,(150,270))
            
        else:
            screen.blit(creditsclic,(150,270))
        
        pygame.display.flip()
        
        
    #début du jeu_______________________________________________________________________________________________________________________________________________
    if boucle_jeu==1:
        
        #initialisation des variables pour le premier tour (arriver sur cette page)
        if commencement==0:
            commencement=1
            
            #emplacement initiale des ordis
            x_ordi_1=20     
            y_ordi_1=36
            x_ordi_2=173
            y_ordi_2=530
            x_ordi_3=395
            y_ordi_3=34
            x_ordi_4=111
            y_ordi_4=215
            x_ordi_5=273
            y_ordi_5=350
            x_ordi_6=560
            y_ordi_6=130
            x_ordi_7=586
            y_ordi_7=210

            #étoiles
            toucher_etoile_1=1  #toucher_etoile correspond si le joueur passe sur les coordonnées de l'étoiles
            toucher_etoile_2=1
            toucher_etoile_3=1
            toucher_etoile_4=1
            rotation_etoile_1=1 #rotation_etoile correspond si le jeu doit afficher l'étoile complète ou l'étoile tournée
            rotation_etoile_2=1
            rotation_etoile_3=1  
            rotation_etoile_4=1   
            temps_rotation_1=0  #temps_rotation correspond aux nombres de tours de la boucle (ici 25) avent de tourner l'étoile
            temps_rotation_2=0
            temps_rotation_3=0
            temps_rotation_4=0
            ordre_etoile=0      #ordre_etoile correspond aux nombres d'étoile attrapées
            etoile_1_gagnee=0   #etoile_gagnee correspond valider notre premier passage sur les coordonnées de l'étoile et ainsi ignorer les autres
            etoile_2_gagnee=0
            etoile_3_gagnee=0
            etoile_4_gagnee=0
            
            #spéciales des vies
            vie_restante = 3
            recommencer = 0
            zero_vie=0
                
                
            #personnage
            x_perso=122            
            y_perso=11 
            
            #portes
            porte_rose_ouverte=1
            porte_violette_ouverte=1
            
            #temps pour le calcul du score
            temps_score=0
            temps_jeu=0
        
        if recommencer==1: #retour à la case départ lorsqu'on touche un ordi
            sontoucher.play()
            x_perso=122
            y_perso=11
            recommencer=0
        
        screen.blit(terrain,(0,0))
        
        #programme
        
            #murs-----------------------------------------------------------------------------------------------------------------------------------------------
        #mur contour haut
        if x_perso<144 and x_perso>98 and y_perso<=8:    
            y_perso=8
 
        if  x_perso<=145 and x_perso>=143 and y_perso<=29:
            x_perso=143
        if x_perso<=90 and y_perso<30:
            y_perso=30
        if x_perso>145 and y_perso<30:
            y_perso=30
        
        #mur contour bas
        if x_perso<650 and x_perso>604 and y_perso>=674:
            y_perso=674
        if x_perso<=606 and x_perso>=603 and y_perso>=653:
            x_perso=605
        if x_perso>=648 and x_perso<=651 and y_perso>=653:
            x_perso=649
        
        if x_perso<604 and y_perso>=652:
            y_perso=652
        if x_perso>650 and y_perso>=652:
            y_perso=652
        
        #mur contour gauche
        if x_perso<6:
            x_perso=6
            
        #mur contour droite
        if x_perso>672:
            x_perso=672
        
        #murs en haut à gauche
            #petit
        if x_perso<=98 and x_perso>=97 and y_perso<95:
            x_perso=99
        if x_perso>54 and x_perso<99 and y_perso<=95:
            y_perso=95
        if x_perso<=53 and x_perso>=52 and y_perso<95:
            x_perso=51
            
            #grand     
            
            # x=190   y=182
        if x_perso<=146 and x_perso>=145 and y_perso<182:
            x_perso=143
        if x_perso>144 and x_perso<188 and y_perso<=182:
            y_perso=182
        if x_perso>=188 and x_perso<=189 and y_perso<182:
            x_perso=190
            
            # x=53  y=135
        
        if x_perso<=188 and x_perso>=53 and y_perso<=137 and y_perso>=135:
            y_perso=135
        if x_perso>53 and x_perso<188 and y_perso<=182 and y_perso>=180:
            y_perso=182
        
            #   x=99    y=288
        
        if x_perso<=55 and x_perso>=54 and y_perso<288 and y_perso>135:
            x_perso=53
        if x_perso>=97 and x_perso<=98 and y_perso<288 and y_perso>135:
            x_perso=99
        
            #   x=282   y=288
            
        if x_perso<282 and x_perso>53 and y_perso<=288 and y_perso>=286:
            y_perso=288
        if x_perso>53 and x_perso<282 and y_perso<=246 and y_perso>=244:
            y_perso=244
            
            
            #   x=282  y=332
            
        if x_perso<=281 and x_perso>=280 and y_perso<332 and y_perso>244:
            x_perso=282
        if x_perso>=237 and x_perso<=238 and y_perso<332 and y_perso>244:
            x_perso=236
            
            #   x=375  y=332
            
        if x_perso<375 and x_perso>236 and y_perso<=290 and y_perso>=289:
            y_perso=288
        if x_perso>236 and x_perso<375 and y_perso<=331 and y_perso>=330:
            y_perso=332
            
            #   x=326  y=95
            
        if x_perso<=328 and x_perso>=327 and y_perso<332 and y_perso>95:
            x_perso=326
        if x_perso>=373 and x_perso<=374 and y_perso<332 and y_perso>95:
            x_perso=375
            
            #   x=282-284  y=138
            
        if x_perso<375 and x_perso>281 and y_perso<=97 and y_perso>=96:
            y_perso=95
        if x_perso>283 and x_perso<375 and y_perso<=137 and y_perso>=136:
            y_perso=138
            
            #   x=236  y=202
        
        if x_perso<=238 and x_perso>=237 and y_perso<202 and y_perso>73:
            x_perso=236
        if x_perso>=280 and x_perso<=281 and y_perso<97 and y_perso>73:
            x_perso=282
        if x_perso>=282 and x_perso<=283 and y_perso<202 and y_perso>100:
            x_perso=284
            
        if x_perso<282 and x_perso>236 and y_perso<=75 and y_perso>=74:
            y_perso=73
        if x_perso>236 and x_perso<284 and y_perso<=201 and y_perso>=200:
            y_perso=202
        
        #grand mur du bas
        #_1
        if x_perso<=258 and x_perso>=257 and y_perso>589 :
            x_perso=256 
        #_2 et 32
        if x_perso<326 and x_perso>213 and y_perso<=589 and y_perso>=588:
            y_perso=590
        #_3
        if x_perso<=215 and x_perso>=214 and y_perso<590 and y_perso>546:
            x_perso=213 
        #_4
        if x_perso<284 and x_perso>213 and y_perso<=548 and y_perso>=547:
            y_perso=546
        #_5
        if x_perso<=285 and x_perso>=283 and y_perso<547 and y_perso>501 :
            x_perso=283 
        #_6
        if x_perso<284 and x_perso>213 and y_perso<=501 and y_perso>=500:
            y_perso=502
        #_7
        if x_perso<=215 and x_perso>=214 and y_perso<499 and y_perso>418 :
            x_perso=213
        #_8
        if x_perso<214 and x_perso>143 and y_perso<=418 and y_perso>=417:
            y_perso=419
        #_9
        if x_perso<=145 and x_perso>=144 and y_perso<419 and y_perso>374 :
            x_perso=143
        #_10
        if x_perso<144 and x_perso>98 and y_perso<=374 and y_perso>=373:
            y_perso=375
        #_11
        if x_perso<=98 and x_perso>=97 and y_perso<460 and y_perso>374 :
            x_perso=99
        #_12
        if x_perso<166 and x_perso>98 and y_perso<=461 and y_perso>=460:
            y_perso=459
        #_13
        if x_perso<=165 and x_perso>=164 and y_perso<590 and y_perso>459 :
            x_perso=166
        #_14
        if x_perso<166 and x_perso>53 and y_perso<=589 and y_perso>=588:
            y_perso=590
        #_15
        if x_perso<=55 and x_perso>=54 and y_perso<590 and y_perso>546 :
            x_perso=53
        #_16
        if x_perso<121 and x_perso>53 and y_perso<=548 and y_perso>=547:
            y_perso=546
        #_17
        if x_perso<=122 and x_perso>=121 and y_perso<547 and y_perso>501 :
            x_perso=120
        #_18
        if x_perso<121 and x_perso>53 and y_perso<=501 and y_perso>=500:
            y_perso=502
        #_19
        if x_perso<=55 and x_perso>=54 and y_perso<502 and y_perso>331 :
            x_perso=53
        #_20
        if x_perso<190 and x_perso>53 and y_perso<=333 and y_perso>=332:
            y_perso=331
        #_21
        if x_perso<=189 and x_perso>=188 and y_perso<373 and y_perso>331 :
            x_perso=190
        #_22
        if x_perso<259 and x_perso>189 and y_perso<=374 and y_perso>=373:
            y_perso=372
        #_23
        if x_perso<=258 and x_perso>=257 and y_perso<460 and y_perso>372 :
            x_perso=259
        #_24
        if x_perso<329 and x_perso>258 and y_perso<=461 and y_perso>=460:
            y_perso=459
        #_25
        if x_perso<=328 and x_perso>=327 and y_perso<526 and y_perso>460 :
            x_perso=329
        #_26
        if x_perso<489 and x_perso>328 and y_perso<=527 and y_perso>=526:
            y_perso=525
        #_27
        if x_perso<=488 and x_perso>=487 and y_perso<590 and y_perso>525 :
            x_perso=489
        #_28
        if x_perso<489 and x_perso>443 and y_perso<=589 and y_perso>=588:
            y_perso=590
        #_29
        if x_perso<=445 and x_perso>=444 and y_perso<590 and y_perso>567 :
            x_perso=443
        #_30
        if x_perso<444 and x_perso>328 and y_perso<=567 and y_perso>=566:
            y_perso=568
        #_31
        if x_perso<=328 and x_perso>=327 and y_perso<590 and y_perso>567 :
            x_perso=329
        #_32
            #fait au _2
        #_33
        if x_perso<=305 and x_perso>=304 and y_perso>589 :
            x_perso=306
            
        #grand mur du "milieu"
        #_1
        if x_perso<=535 and x_perso>=534 and y_perso>480 :
            x_perso=533
        #_2 et 16
        if x_perso<628 and x_perso>420 and y_perso<=480 and y_perso>=479:
            y_perso=481
        #_3 et 7
        if x_perso<=422 and x_perso>=421 and y_perso<480 and y_perso>92 :
            x_perso=420
        #_4
        if x_perso<421 and x_perso>306 and y_perso<=415 and y_perso>=414:
            y_perso=416
        #_5
        if x_perso<=308 and x_perso>=307 and y_perso<416 and y_perso>373 :
            x_perso=306
        #_6
        if x_perso<421 and x_perso>306 and y_perso<=374 and y_perso>=373:
            y_perso=372
        #_7
            #fait au _3
        #_8
        if x_perso<466 and x_perso>420 and y_perso<=94 and y_perso>=93:
            y_perso=92
        #_9 et 13
        if x_perso<=465 and x_perso>=464 and y_perso<438 and y_perso>92 :
            x_perso=466
        #_10
        if x_perso<490 and x_perso>465 and y_perso<=202 and y_perso>=201:
            y_perso=200
        #_11
        if x_perso<=489 and x_perso>=488 and y_perso<244 and y_perso>200 :
            x_perso=490
        #_12
        if x_perso<490 and x_perso>465 and y_perso<=244 and y_perso>=243:
            y_perso=245
        #_13
            #fait au _13
        #_14
        if x_perso<628 and x_perso>465 and y_perso<=439 and y_perso>=438:
            y_perso=437
        #_15
        if x_perso<=627 and x_perso>=626 and y_perso<481 and y_perso>437 :
            x_perso=628
        #_16
            #fait au _2
        #_17
        if x_perso<=581 and x_perso>=580 and y_perso>480:
            x_perso=582
            
        #grand mur de droite
        #_1
        if x_perso>533 and y_perso<=395 and y_perso>=394:
            y_perso=396
        #_2 et 6
        if x_perso<=535 and x_perso>=534 and y_perso<396 and y_perso>158 :
            x_perso=533
        #_3
        if x_perso<534 and x_perso>510 and y_perso<=352 and y_perso>=351:
            y_perso=353
        #_4
        if x_perso<=512 and x_perso>=511 and y_perso<353 and y_perso>309 :
            x_perso=510
        #_5
        if x_perso<534 and x_perso>510 and y_perso<=311 and y_perso>=310:
            y_perso=309
        #_6
            #fait au _2
        #_7
        if x_perso<580 and x_perso>533 and y_perso<=160 and y_perso>=159:
            y_perso=158
        #_8
        if x_perso<=581 and x_perso>=580 and y_perso<159 and y_perso>116 :
            x_perso=579
        #_9
        if x_perso<580 and x_perso>513 and y_perso<=116 and y_perso>=115:
            y_perso=117
        #_10
        if x_perso<=515 and x_perso>=514 and y_perso<117 and y_perso>71 :
            x_perso=513
        #_11
        if x_perso<628 and x_perso>513 and y_perso<=73 and y_perso>=72:
            y_perso=71
        #_12
        if x_perso<=627 and x_perso>=626 and y_perso<204 and y_perso>71 :
            x_perso=628
        #_13
        if x_perso<628 and x_perso>581 and y_perso<=203 and y_perso>=202:
            y_perso=204
        #_14
        if x_perso<=581 and x_perso>=580 and y_perso<351 and y_perso>203 :
            x_perso=582
        #_15
        if x_perso>581 and y_perso<=352 and y_perso>=351:
            y_perso=350
            
        #petit mur en bas
        #_1
        if x_perso<=445 and x_perso>=444 and y_perso>631 :
            x_perso=443
        #_2
        if x_perso<489 and x_perso>443 and y_perso<=633 and y_perso>=632:
            y_perso=631
        #_3
        if x_perso<=488 and x_perso>=487 and y_perso>631 :
            x_perso=489
        
        #petit mur en haut
        #_1
        if x_perso<=422 and x_perso>=421 and y_perso<51 :
            x_perso=420
        #_2
        if x_perso<466 and x_perso>420 and y_perso<=50 and y_perso>=49:
            y_perso=51
        #_3
        if x_perso<=465 and x_perso>=464 and y_perso<51 :
            x_perso=466
        
        #petit mur à gauche
        #_1 (côté bas)
        if x_perso>626 and y_perso<=589 and y_perso>=588:
            y_perso=590
        #_2
        if x_perso<=628 and x_perso>=627 and y_perso<590 and y_perso>544 :
            x_perso=626
        #_3
        if x_perso>626 and y_perso<=546 and y_perso>=545:
            y_perso=544
            
            #déplacement des ordinateurs------------------------------------------------------------------------------------------------------------------------
        if y_ordi_1<35:    #ordinateurs numéro 1
            variable1= variable1*(-1) 
    
        if y_ordi_1>640:
            variable1= variable1*(-1) 
    
        y_ordi_1=y_ordi_1+variable1
    
        if x_ordi_2<172:    #ordinateurs numéro 2
            variable2=variable2*(-1)
    
        if x_ordi_2>258:
            variable2=variable2*(-1)
    
        x_ordi_2=x_ordi_2+variable2
    
        if y_ordi_3<33:    #ordinateurs numéro 3
            variable3=variable3*(-1)
    
        if y_ordi_3>350:
            variable3=variable3*(-1)
    
        y_ordi_3=y_ordi_3+variable3
    
        if x_ordi_4<110:    #ordinateurs numéro 4
            variable4=variable4*(-1)
    
        if x_ordi_4>295:
            variable4=variable4*(-1)
    
        x_ordi_4=x_ordi_4+variable4
    
        if x_ordi_7<585:    #ordinateurs numéro 7
            variable7=variable7*(-1)
        
        if x_ordi_7>658:
            variable7=variable7*(-1)
        
        x_ordi_7=x_ordi_7+variable7
    
        #déplacment autre que rectiligne
        if y_ordi_5<351:    #ordinateurs numéro 5
            direction_5=1
        elif y_ordi_5>624:
            direction_5=-1
    
        if direction_5==1:#descendre
            if x_ordi_5==273 and y_ordi_5<432:
                y_ordi_5=y_ordi_5 + variable5
            elif x_ordi_5<345 and y_ordi_5==434:
                x_ordi_5= x_ordi_5 + variable5
            elif x_ordi_5==345 and y_ordi_5<500:
                y_ordi_5 = y_ordi_5 + variable5
            elif x_ordi_5<502 and y_ordi_5==500:
                x_ordi_5=x_ordi_5 + variable5
            elif x_ordi_5==504 and y_ordi_5<625:
                y_ordi_5=y_ordi_5 + variable5
    
        elif direction_5==-1:#monter
            if x_ordi_5==273 and y_ordi_5>350:
                y_ordi_5=y_ordi_5 - variable5
            elif x_ordi_5>272 and y_ordi_5==434:
                x_ordi_5= x_ordi_5 - variable5
            elif x_ordi_5==345 and y_ordi_5>432:
                y_ordi_5 = y_ordi_5 - variable5
            elif x_ordi_5>345 and y_ordi_5==500:
                x_ordi_5=x_ordi_5 - variable5
            elif x_ordi_5==504 and y_ordi_5>500:
                y_ordi_5=y_ordi_5 - variable5
            
        if x_ordi_6>560 and y_ordi_6==130:  #ordinateurs numéro 6
            direction_6=1
        elif x_ordi_6>649 and y_ordi_6==410:
            direction_6=-1
        
        if direction_6==1:#descendre
            if x_ordi_6 > 470 and y_ordi_6 == 130:
                x_ordi_6 = x_ordi_6 - variable6
            elif x_ordi_6==468 and y_ordi_6<180:
                y_ordi_6=y_ordi_6 + variable6
            elif x_ordi_6<510 and y_ordi_6==182:
                x_ordi_6 = x_ordi_6 + variable6
            elif x_ordi_6==512 and y_ordi_6<290:
                y_ordi_6=y_ordi_6 + variable6
            elif x_ordi_6>480 and y_ordi_6==290:
                x_ordi_6 = x_ordi_6 - variable6
            elif x_ordi_6==480 and y_ordi_6<410:
                y_ordi_6=y_ordi_6 + variable6
            elif x_ordi_6<650 and y_ordi_6==410:
                x_ordi_6 = x_ordi_6 + variable6
            
        elif direction_6==-1:#monter
            if x_ordi_6 < 561 and y_ordi_6 == 130:
                x_ordi_6 = x_ordi_6 + variable6
            elif x_ordi_6==470 and y_ordi_6>130:
                y_ordi_6=y_ordi_6 - variable6
            elif x_ordi_6>470 and y_ordi_6==180:
                x_ordi_6 = x_ordi_6 - variable6
            elif x_ordi_6==512 and y_ordi_6>130 and y_ordi_6<300:
                y_ordi_6=y_ordi_6 - variable6
            elif x_ordi_6<510 and y_ordi_6==262:
                x_ordi_6 = x_ordi_6 + variable6
            elif x_ordi_6==480 and y_ordi_6>260:
                y_ordi_6=y_ordi_6 - variable6
            elif x_ordi_6>480 and y_ordi_6==410:
                x_ordi_6 = x_ordi_6 - variable6
            
            
            #toucher les ordinateurs-------------------------------------------------------------------------------------------------------------------------
        x_ordi_1_gauche = x_ordi_1 -23
        x_ordi_1_droite = x_ordi_1 +37
        y_ordi_1_haut = y_ordi_1 - 22
        y_ordi_1_bas = y_ordi_1 + 31
        
        x_ordi_2_gauche = x_ordi_2 -23
        x_ordi_2_droite = x_ordi_2 +37
        y_ordi_2_haut = y_ordi_2 - 22
        y_ordi_2_bas = y_ordi_2 + 31
        
        x_ordi_3_gauche = x_ordi_3 -23
        x_ordi_3_droite = x_ordi_3 +37
        y_ordi_3_haut = y_ordi_3 - 22
        y_ordi_3_bas = y_ordi_3 + 31
        
        x_ordi_4_gauche = x_ordi_4 -23
        x_ordi_4_droite = x_ordi_4 +37
        y_ordi_4_haut = y_ordi_4 - 22
        y_ordi_4_bas = y_ordi_4 + 31
        
        x_ordi_5_gauche = x_ordi_5 -23
        x_ordi_5_droite = x_ordi_5 +37
        y_ordi_5_haut = y_ordi_5 - 22
        y_ordi_5_bas = y_ordi_5 + 31
        
        x_ordi_6_gauche = x_ordi_6 -23
        x_ordi_6_droite = x_ordi_6 +37
        y_ordi_6_haut = y_ordi_6 - 22
        y_ordi_6_bas = y_ordi_6 + 31
        
        x_ordi_7_gauche = x_ordi_7 -23
        x_ordi_7_droite = x_ordi_7 +37
        y_ordi_7_haut = y_ordi_7 - 22
        y_ordi_7_bas = y_ordi_7 + 31
        
        #toucher les ordis -23 37   22 31
        if x_perso>x_ordi_1_gauche and x_perso<x_ordi_1_droite and y_perso>y_ordi_1_haut and y_perso<y_ordi_1_bas: #coordonnées de l'ordi_1
            vie_restante = vie_restante -1 #on a une vie en moins
            recommencer=1   #on recommence
            
        if x_perso>x_ordi_2_gauche and x_perso<x_ordi_2_droite and y_perso>y_ordi_2_haut and y_perso<y_ordi_2_bas: #coordonnées de l'ordi_2
            vie_restante = vie_restante -1 #on a une vie en moins
            recommencer=1   #on recommence
            
        if x_perso>x_ordi_3_gauche and x_perso<x_ordi_3_droite and y_perso>y_ordi_3_haut and y_perso<y_ordi_3_bas: #coordonnées de l'ordi_3
            vie_restante = vie_restante -1 #on a une vie en moins
            recommencer=1   #on recommence
            
        if x_perso>x_ordi_4_gauche and x_perso<x_ordi_4_droite and y_perso>y_ordi_4_haut and y_perso<y_ordi_4_bas: #coordonnées de l'ordi_4
            vie_restante = vie_restante -1 #on a une vie en moins
            recommencer=1   #on recommence
            
        if x_perso>x_ordi_5_gauche and x_perso<x_ordi_5_droite and y_perso>y_ordi_5_haut and y_perso<y_ordi_5_bas: #coordonnées de l'ordi_5
            vie_restante = vie_restante -1 #on a une vie en moins
            recommencer=1   #on recommence
            
        if x_perso>x_ordi_6_gauche and x_perso<x_ordi_6_droite and y_perso>y_ordi_6_haut and y_perso<y_ordi_6_bas: #coordonnées de l'ordi_6
            vie_restante = vie_restante -1 #on a une vie en moins
            recommencer=1   #on recommence
            
        if x_perso>x_ordi_7_gauche and x_perso<x_ordi_7_droite and y_perso>y_ordi_7_haut and y_perso<y_ordi_7_bas: #coordonnées de l'ordi_7
            vie_restante = vie_restante -1 #on a une vie en moins
            recommencer=1   #on recommence
            
            #vies-----------------------------------------------------------------------------------------------------------------------------------------------
        if vie_restante>2:  #lorsque l'on a 3 vies
            screen.blit(vie1,(900,200)) 
        else:
            screen.blit(vie2,(900,200))
            
        if vie_restante>1: #lorsque que l'on a 2 vies ou plus
            screen.blit(vie1,(830,200))
        else:
            screen.blit(vie2,(830,200))
            
        if vie_restante>0: #lorsque l'on a 1 vie ou plus
            screen.blit(vie1,(750,200))
        else:
            screen.blit(vie2,(750,200))
        
        if vie_restante==0: #lorsque l'on n'a plus de vie
            zero_vie=1
            
            #étoiles--------------------------------------------------------------------------------------------------------------------------------------------
        #attraper une étoile
        #1_
        if x_perso>350 and x_perso<400 and y_perso>580 and y_perso<630: #coordonnées de l'étoile la plus basse
            if toucher_etoile_1==1: #permet de ne valider qu'uniquement le premier passage avec un son joué
                son_etoile.play() 
            
            toucher_etoile_1=0
        #2_
        if x_perso>280 and x_perso<330 and y_perso>150 and y_perso<188: #coordonnées de l'étoile la plus à gauche
            if toucher_etoile_2==1: #permet de ne valider qu'uniquement le premier passage avec un son joué
                son_etoile.play()
            
            toucher_etoile_2=0
        #3_
        if x_perso>100 and x_perso<150 and y_perso>380 and y_perso<440: #coordonnées de l'étoile la plus haute
            if toucher_etoile_3==1: #permet de ne valider qu'uniquement le premier passage avec un son joué
                son_etoile.play()
            
            toucher_etoile_3=0
        #4_
        if x_perso>600 and x_perso<650 and y_perso>270 and y_perso<320: #coordonnées de l'étoile la plus à droite
            if toucher_etoile_4==1: #permet de ne valider qu'uniquement le premier passage avec un son joué
                son_etoile.play()
            
            toucher_etoile_4=0
        #
        
        #rotation et affichage des étoiles
        
            #rotation des étoiles
        #_1
        if toucher_etoile_1==1:     #si l'étoile 1 n'est pas touchée
            if rotation_etoile_1==1:
                screen.blit(etoile2,(370,600))
            else:
                screen.blit(etoile3,(385,600))
            if temps_rotation_1<25:     #permet une pause entre l'alternace entre les deux images de rotation
                temps_rotation_1 = temps_rotation_1 +1 
            else:
                rotation_etoile_1 = rotation_etoile_1 * (-1) #permet l'alternance des deux images pour créer une rotation
                temps_rotation_1 =0
        else:           #si l'étoile a été touchée
            if etoile_1_gagnee==0: #valide l'étoile comme prise
                ordre_etoile = ordre_etoile +1 #permet d'afficher l'étoile dans le bon ordre
                etoile_1_gagnee =1  #bloque l'entrée à nouveau dans la condition
                
        #_2    
        if toucher_etoile_2==1:      #si l'étoile 2 n'est pas touchée
            if rotation_etoile_2==1:
                screen.blit(etoile2,(300,150))
            else:
                screen.blit(etoile3,(315,150))
            if temps_rotation_2<25:     #permet une pause entre l'alternace entre les deux images de rotation
                temps_rotation_2 = temps_rotation_2 +1
            else:
                rotation_etoile_2 = rotation_etoile_2 * (-1)        #permet l'alternance des deux images pour créer une rotation
                temps_rotation_2 =0
        else:         #si l'étoile a été touchée
            if etoile_2_gagnee==0:      #valide l'étoile comme prise
                ordre_etoile = ordre_etoile +1  #permet d'afficher l'étoile dans le bon ordre
                etoile_2_gagnee =1  #bloque l'entrée à nouveau dans la condition
                
        #_3    
        if toucher_etoile_3==1:         #si l'étoile 3 n'est pas touchée
            if rotation_etoile_3==1:
                screen.blit(etoile2,(120,410))
            else:
                screen.blit(etoile3,(125,410))
            if temps_rotation_3<25:              #permet une pause entre l'alternace entre les deux images de rotation
                temps_rotation_3 = temps_rotation_3 +1
            else:
                rotation_etoile_3 = rotation_etoile_3 * (-1)    #permet l'alternance des deux images pour créer une rotation
                temps_rotation_3 =0
        else:       #si l'étoile a été touchée
            if etoile_3_gagnee==0:  #valide l'étoile comme prise
                ordre_etoile = ordre_etoile +1  #permet d'afficher l'étoile dans le bon ordre
                etoile_3_gagnee=1   #bloque l'entrée à nouveau dans la condition
        
        #_4    
        if toucher_etoile_4==1:     #si l'étoile 4 n'est pas touchée
            if rotation_etoile_4==1:
                screen.blit(etoile2,(620,290))
            else:
                screen.blit(etoile3,(625,290))
            if temps_rotation_4<25:              #permet une pause entre l'alternace entre les deux images de rotation
                temps_rotation_4 = temps_rotation_4 +1
            else:
                rotation_etoile_4 = rotation_etoile_4 * (-1)    #permet l'alternance des deux images pour créer une rotation
                temps_rotation_4 =0
        else:       #si l'étoile a été touchée
            if etoile_4_gagnee==0:  #valide l'étoile comme prise
                ordre_etoile = ordre_etoile+1   #permet d'afficher l'étoile dans le bon ordre
                etoile_4_gagnee=1   #bloque l'entrée à nouveau dans la condition
        #
                
                
                
        #ordre d'affichage des étoiles    
        
        if ordre_etoile>0:  #permet de savoir si on a une étoile ou plus
            screen.blit(etoile4,(720,300))
        else:
            screen.blit(etoile1,(720,300))
            
        if ordre_etoile>1: #permet de savoir si on a deux étoiles ou plus
            screen.blit(etoile4,(790,300))
        else:
            screen.blit(etoile1,(790,300))
            
        if ordre_etoile>2:  #permet de savoir si on a trois étoiles ou plus
            screen.blit(etoile4,(860,300))
        else:
            screen.blit(etoile1,(860,300))
            
        if ordre_etoile == 4:   #permet de savoir si on a les quatres étoiles
            screen.blit(etoile4,(930,300))
        else:
            screen.blit(etoile1,(930,300))    
        
        
        #portes------------------------------------------------------------------------------------------------------------------------------------------------
        screen.blit(levier_rose,(312,280))
        
        screen.blit(levier_violet,(106,520))
        
        if x_perso>308 and x_perso<341 and y_perso>276 and y_perso<308 :
            if touche_entree==1:
                boucle_jeu=0
                boucle_levier=1
                activation_rose=1
                activation_violet=0
                touche_entree=0
                arriver_levier=1
                
        if x_perso>102 and x_perso<135 and y_perso>516 and y_perso<548 :
            if touche_entree==1:
                boucle_jeu=0
                boucle_levier=1
                activation_violet=1
                activation_rose=0
                touche_entree=0
                arriver_levier=1
        
        if porte_rose_ouverte==1:
            if x_perso>427 and x_perso<458 and y_perso>50 and y_perso<167:
                x_perso=427
        
        if porte_violette_ouverte==1:
            if x_perso>77 and x_perso<91 and y_perso>280 and y_perso<354 :
                x_perso=77
        
       
        
        if porte_rose_ouverte==1:
            screen.blit(porte_rose,(450,51))
        
        if porte_violette_ouverte==1:
            screen.blit(porte_violette,(100,288))
            
            
        #son---------------------------------------------------------------------------------------------------------------------------------------------------
        if x_souris>750 and x_souris<800 and y_souris>550 and y_souris<600:
            aff_son_allume_coupe=1
            if touche==1:
                sonclic.play()
                if changement_son==1:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                changement_son=changement_son*(-1)
        
        if aff_son_allume_coupe==0 and changement_son==1:
            screen.blit(image_son_allume,(750,550))
        elif aff_son_allume_coupe==1 and changement_son==1:
            screen.blit(image_son_allume_appuye,(750,550))
        elif aff_son_allume_coupe==0 and changement_son==(-1):
            screen.blit(image_son_coupe,(750,550))
        elif aff_son_allume_coupe==1 and changement_son==(-1):
            screen.blit(image_son_coupe_appuye,(750,550))
            
        
        if x_souris>825 and x_souris<875 and y_souris>550 and y_souris<600:
            aff_son_baisse=1
            if touche==1:
                volume=volume-0.25
                if volume>(-0.20):
                    sonclic.play()
                if volume<0:
                    volume=0
                pygame.mixer.music.set_volume(volume)
                
        if aff_son_baisse==0:
            screen.blit(image_son_baisse,(825,550))
        else:
            screen.blit(image_son_baisse_appuye,(825,550))
    
    
        if x_souris>900 and x_souris<950 and y_souris>550 and y_souris<600:
            aff_son_monte=1
            if touche==1:
                volume=volume+0.25
                if volume<1.2:
                   sonclic.play() 
                if volume>1:
                    volume=1
                
                pygame.mixer.music.set_volume(volume)
                       
        if aff_son_monte==0:
            screen.blit(image_son_monte,(900,550))
        else:
            screen.blit(image_son_monte_appuye,(900,550))
        
        #calcul du temps de jeu--------------------------------------------------------------------------------------------------------------------------------
        temps_jeu=temps_jeu+1
        if temps_jeu==25:
            temps_score=temps_score+1
            temps_jeu=0
            
        #bouton pause------------------------------------------------------------------------------------------------------------------------------------------
        
        if x_souris>750 and x_souris<949 and y_souris>444 and y_souris<500 or touche_shift==1: 
            imageaff_pause=1
            if touche==1 or touche_shift==1:
                boucle_jeu=0
                boucle_pause=1
                sonclic.play()
                touche_shift=0
            
            
        if imageaff_pause==1:
            screen.blit(image_bouton_pause_selectionne,(750,444))
        else:
            screen.blit(image_bouton_pause,(750,444))
        
        #affichage des images----------------------------------------------------------------------------------------------------------------------------------
        
        screen.blit(joueur,(x_perso,y_perso)) 
        screen.blit(ordi,(20,y_ordi_1))
        screen.blit(ordi,(x_ordi_2,530)) 
        screen.blit(ordi,(395,y_ordi_3))
        screen.blit(ordi,(x_ordi_4,215))
        screen.blit(ordi,(x_ordi_5,y_ordi_5))
        screen.blit(ordi,(x_ordi_6,y_ordi_6))
        screen.blit(ordi,(x_ordi_7,210))
        
        if zero_vie==1: #affichage du game over----------------------------------------------------------------------------------------------------------------
            sontoucher.play()
            screen.blit(gameover,(0,0))
            pygame.display.flip()
            pygame.time.delay(3000) # attendre 3 ssecondes
            boucle_menu=1
            boucle_jeu=0
        
        #arriver à la fin--------------------------------------------------------------------------------------------------------------------------------------
        if x_perso<677 and x_perso>600 and y_perso>660:
            boucle_jeu=0
            boucle_fin=1
            
    
        pygame.display.flip()   #programme terminé -> affichage complet du jeu (renouveau à chaque tour -> superposition)
        
    #boucle fin________________________________________________________________________________________________________________________________________________
    
    if boucle_fin:
        
        #calcul du score
        score_etoile=ordre_etoile*100
        score_vie=(3-vie_restante)*50
    
        score = 1000 + score_etoile - score_vie - temps_score
        
        if temps_score>(1000+score_etoile-score_vie):
            score=0
    
        score_texte=taille_texte.render(str(score),1,blanc) #détermine la valeur du score
        
        if conf<15:
            screen.blit(conf_1,(0,0))
        elif conf<30:
            screen.blit(conf_2,(0,0))
        elif conf<45:
            screen.blit(conf_3,(0,0))
        else:
            conf=0
        
        conf=conf+1
        
        screen.blit(fond_coupe,(250,0)) #affichage du fond
                
        screen.blit(score_texte,(460,45))   #affichage du score
                
        #nombre d'étoiles attrapées + affichage
        
        if ordre_etoile==1:
            screen.blit(etoile5,(482,460))
    
    
        if ordre_etoile==2:  
            screen.blit(etoile5,(448,460))
            screen.blit(etoile5,(518,460))
            
        if ordre_etoile==3: 
            screen.blit(etoile5,(425,460))
            screen.blit(etoile5,(483,460))
            screen.blit(etoile5,(540,460))
            
            
        if ordre_etoile == 4:  
            screen.blit(etoile5,(391,460))
            screen.blit(etoile5,(451,460))
            screen.blit(etoile5,(514,460))
            screen.blit(etoile5,(575,460))
            
                
        pygame.display.flip()
        
        #pour sortir de la boucle
        if touche_entree==1:
            boucle_menu=1
            boucle_fin=0
            touche_entree=0
            pygame.time.delay(500)
        
        
    #boucle parti levier_______________________________________________________________________________________________________________________________________
    if boucle_levier==1:
        
        
        if activation_rose==1: #programme pour la porte rose
            if porte_rose_ouverte==1: #si la porte rose est fermée
                screen.blit(Manivelle_haut,(0,0))
                if x_souris>357 and x_souris<471 and y_souris>108 and y_souris<271: #selection le levier
                    screen.blit(Manivelle_haut_levier,(0,0))
                    if touche==1:
                        screen.blit(Manivelle_milieu,(0,0)) #animation pour l'activation du levier
                        pygame.display.flip()
                        pygame.time.delay(100)
                        porte_rose_ouverte=porte_rose_ouverte*(-1) #la porte rose devient ouverte
                    
                    
                    
            if porte_rose_ouverte==(-1): #si la porte rose est ouvert
                screen.blit(Manivelle_bas,(0,0))
                if x_souris>359 and x_souris<473 and y_souris>249 and y_souris<411:
                    screen.blit(Manivelle_bas_levier,(0,0))
                    if touche==1:
                        screen.blit(Manivelle_milieu,(0,0))
                        pygame.display.flip()
                        pygame.time.delay(100)
                        porte_rose_ouverte=porte_rose_ouverte*(-1)
                        
            if touche_entree==1:
                if porte_rose_ouverte==1:
                    porte_rose_ouverte=porte_rose_ouverte*(-1)
                    screen.blit(Manivelle_haut_levier,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.blit(Manivelle_milieu,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.blit(Manivelle_bas,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    screen.blit(Manivelle_bas_sortie,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    boucle_levier=0
                    boucle_jeu=1
                    
                
                elif porte_rose_ouverte==-1:
                    porte_rose_ouverte=porte_rose_ouverte*(-1)
                    screen.blit(Manivelle_bas_levier,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.blit(Manivelle_milieu,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.blit(Manivelle_haut,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    screen.blit(Manivelle_haut_sortie,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    boucle_levier=0
                    boucle_jeu=1
                    
                    
                    
            if x_souris>605 and x_souris<902 and y_souris>218 and y_souris<307: # sortir de l'écran
                if porte_rose_ouverte==1:
                    screen.blit(Manivelle_haut_sortie,(0,0)) #si levier levé soit porte fermée
                if porte_rose_ouverte==(-1):
                    screen.blit(Manivelle_bas_sortie,(0,0)) #si levier baissé soit porte ouverte
                if touche==1: #détermine si on appuie sur la souris sur le panneau exit
                    boucle_levier=0
                    boucle_jeu=1
        
        if activation_violet==1:    #programme pour la porte violette
            if porte_violette_ouverte==1:   #si la porte violette est fermée
                screen.blit(Manivelle_haut,(0,0))
                if x_souris>357 and x_souris<471 and y_souris>108 and y_souris<271:
                    screen.blit(Manivelle_haut_levier,(0,0))
                    if touche==1:
                        screen.blit(Manivelle_milieu,(0,0))
                        pygame.display.flip()
                        pygame.time.delay(100)
                        porte_violette_ouverte=porte_violette_ouverte*(-1)#la porte violette devient ouverte
                    
                    
                    
            if porte_violette_ouverte==(-1):    #si la porte violette est ouverte
                screen.blit(Manivelle_bas,(0,0))
                if x_souris>359 and x_souris<473 and y_souris>249 and y_souris<411:
                    screen.blit(Manivelle_bas_levier,(0,0))
                    if touche==1:
                        screen.blit(Manivelle_milieu,(0,0))
                        pygame.display.flip()
                        pygame.time.delay(100)
                        porte_violette_ouverte=porte_violette_ouverte*(-1) #la porte violette devient fermée
                        
            if touche_entree==1:
                if porte_violette_ouverte==1:
                    porte_violette_ouverte=porte_violette_ouverte*(-1)
                    screen.blit(Manivelle_haut_levier,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.blit(Manivelle_milieu,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.blit(Manivelle_bas,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    screen.blit(Manivelle_bas_sortie,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    boucle_levier=0
                    boucle_jeu=1
                    
                
                elif porte_violette_ouverte==-1:
                    porte_violette_ouverte=porte_violette_ouverte*(-1)
                    screen.blit(Manivelle_bas_levier,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.blit(Manivelle_milieu,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    screen.blit(Manivelle_haut,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    screen.blit(Manivelle_haut_sortie,(0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    boucle_levier=0
                    boucle_jeu=1          
                        
            
                    
            if x_souris>605 and x_souris<902 and y_souris>218 and y_souris<307: #sortir de la boucle
                if porte_violette_ouverte==1:
                    screen.blit(Manivelle_haut_sortie,(0,0))
                if porte_violette_ouverte==(-1):
                    screen.blit(Manivelle_bas_sortie,(0,0))
                if touche==1:
                    boucle_levier=0
                    boucle_jeu=1
        
        pygame.display.flip()
        if arriver_levier==1:
            arriver_levier=0
            pygame.time.delay(500)
        
        
        
    #boucle du menu pause______________________________________________________________________________________________________________________________________
    if boucle_pause==1:
       
        screen.blit(fondpage,(0,0))
        
        if x_souris>150 and y_souris>50 and x_souris<815 and y_souris<200 or touche_entree==1: #reprendre
            imageaff_reprendre=1
            if touche==1 or touche_entree==1:
                boucle_jeu=1
                boucle_pause=0
                sonclic.play()
                touche_entree=0
                
                
        if x_souris>150 and y_souris>270 and x_souris<815 and y_souris<420:#quitter
            imageaff_quitter=1
            if touche==1:
                boucle_pause=0
                boucle_menu=1
                sonclic.play()
    
        #afficher les images
        
        
        if imageaff_reprendre==0:
            screen.blit(Reprendre,(145,50))
            
        else:
            screen.blit(Reprendreclic,(150,50))
            
        if imageaff_quitter==0:
            screen.blit(Quitter_pause,(150,270))
            
        else:
            screen.blit(Quitter_pauseclic,(150,270))
        
        
        screen.blit(image_menu_pause,(310,483))
        
        pygame.display.flip()
        

        
        #affichage des images
        
        
    #boucle de la page de crédit_______________________________________________________________________________________________________________________________
    if boucle_credit==1:
       
        screen.blit(fondpage,(0,0))
        
        if x_souris>170 and y_souris>520 and x_souris<825 and y_souris<670: #contour du bouton quitter
            imageaff_quitter_credit=1
            if touche==1:
                boucle_credit=0
                boucle_menu=1
                sonclic.play()
        
        screen.blit(auteurs,(5,5)) #image principale
        
        #image du bouton quitter
        if imageaff_quitter_credit==0:
            screen.blit(Quitter,(170,520))  #image quand on n'est pas dessus
        else:
            screen.blit(Quitterclic,(170,520))  #image dessus
       
       
    #affichage des images
    pygame.display.flip()


#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#fin du programme
pygame.time.delay(1000) #pause de 1 seconde avant de fermer la fenêtre


pygame.quit() #la fenêtre se ferme avec pygame