import pygame
import sys
from classes import *
from pygame.locals import *
from graphics import *
from utils import *
from save_manager import save_game, display_save_confirmation, load_game


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("99 Floors : Ascent")

main_font = pygame.font.Font("graphics/resources/font/Cinzel-Regular.otf", 40)
font = main_font  # Utilisation partout sauf pour le titre

def main_menu(screen, font, clock):
    # Chargement des ressources
    background = pygame.image.load("graphics/resources/backgrounds/tour3.webp")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # L'image prend tout l'écran
    
    # Utilisation de la nouvelle police CinzelDecorative-Bold avec une taille plus petite
    title_font = pygame.font.Font("graphics/resources/font/CinzelDecorative-Bold.otf", 70)
    select_sound = pygame.mixer.Sound("graphics/resources/music/menuselection.mp3")
    click_sound = pygame.mixer.Sound("graphics/resources/music/menuclick.mp3")
    pygame.mixer.music.load("graphics/resources/music/mystical.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # Boucle infinie de la musique

    options = ["Nouvelle Partie", "Charger Partie", "Quitter"]
    selected = 0
    width, height = screen.get_size()
    box_width = 450  # Réduction de la largeur du menu
    box_height = 250  # Réduction de la hauteur du menu

    while True:
        # Affichage de l'arrière-plan pleine taille
        screen.blit(background, (0, 0))
        
        # Affiche le titre avec une taille plus petite pour éviter le dépassement
        title_surface = title_font.render("99 FLOORS : ASCENT", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(width // 2, height // 6))  # Titre placé légèrement plus haut
        screen.blit(title_surface, title_rect)

        # Crée une surface semi-transparente pour le menu
        menu_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        menu_surface.fill((0, 0, 0, 150))  # Fond noir avec 150 de transparence

        # Dessine la boîte semi-transparente
        screen.blit(menu_surface, (width // 2 - box_width // 2, height // 2 - box_height // 2 + 100))
        pygame.draw.rect(screen, (255, 255, 255), 
                         (width // 2 - box_width // 2, height // 2 - box_height // 2 + 100, 
                          box_width, box_height), 3)
        
        # Affiche les options du menu
        for i, option in enumerate(options):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            text_surface = font.render(option, True, color)
            
            text_rect = text_surface.get_rect(center=(width // 2, height // 2 + 50 + i * 50))  # Réduction de l'espace entre les options
            screen.blit(text_surface, text_rect.topleft)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    select_sound.play()
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    select_sound.play()
                if event.key == pygame.K_RETURN:
                    click_sound.play()
                    pygame.time.wait(300)
                    return selected


            
def prologue(hero, screen, font, clock):
    
    global background
    
    title_font = pygame.font.Font("graphics/resources/font/CinzelDecorative-Bold.otf", 60)
   
    sprites = load_sprites()

    sprite_aldric = sprites["Aldric"]
    sprite_garen = sprites["Garen"]
    sprite_mysterieux = sprites["Homme_mysterieux"]
    sprite_kael = sprites["Kael"]
    sprite_brandio = sprites["Brandio"]

    sprite_ayela = sprites["Ayela"]
    sprite_clotaire = sprites["Clotaire"]
    sprite_durnir = sprites["Durnir"]
    sprite_emphyr = sprites["Emphyr"]
    sprite_gallius = sprites["Gallius"]
    sprite_velm = sprites["Velm"]
    sprite_yohna = sprites["Yohna"]
    sprite_zyn = sprites["Zyn"]
    
    # Fade to black initial
    fade_out(screen, WIDTH, HEIGHT)
    fade_in_music("graphics/resources/music/AmbientHecate.mp3", max_volume=0.5, fade_duration=4000)
    
    clear_screen(screen)
    fade_in_text(screen, 
             "Personne ne sais quand ni comment elle est apparue...mais je compte bien la gravir", 
             font, 
             (WIDTH // 2, HEIGHT // 2), 
             duration=4000,  # Plus long
             fade_speed=1)   # Plus lent

    clear_screen(screen)
    
    clear_screen(screen)
    fade_in_text(screen, 
             "Si je ne reviens pas, que les dieux te protegent...mon fils..", 
             font, 
             (WIDTH // 2, HEIGHT // 2), 
             duration=4000,  # Plus long
             fade_speed=1)   # Plus lent

    clear_screen(screen)

    # Premier message avec fade-in adouci et redimensionnement automatique
    clear_screen(screen)
    fade_in_text(screen, 
             "À ceux qui tenteront l'ascension, qui échoueront, qui réussiront...", 
             font, 
             (WIDTH // 2, HEIGHT // 2), 
             duration=4000,  # Plus long
             fade_speed=1)   # Plus lent

    clear_screen(screen)
    pygame.time.wait(2000)

    # Titre avec fade-in plus lent
    fade_in_text(screen, "99 FLOORS : ASCENT", title_font, (WIDTH // 2, HEIGHT // 2 + 50), fade_speed=2)
    
    

    fade_out_text(screen, 5000, fade_speed=2)
    fade_out_music(fade_duration=4000)
    pygame.time.wait(1000)
    
    # Suite du prologue
    clear_screen(screen)
    fade_in_text(screen, 
             "Chapitre 1 : Au pied de l' ascension", 
             font, 
             (WIDTH // 2, HEIGHT // 2),  # Centré sur l'écran
             duration=3000)
    fade_out_text(screen, 3000, fade_speed=2)
    pygame.time.wait(1000)
    
    fade_in_music("graphics/resources/music/Meditating.mp3", max_volume=0.2, fade_duration=4000)
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/Village1.webp", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Définition de dialogues avant de les utiliser
    dialogues = [
        
        "Je marche encore et encore, village après village, route après route... Chaque sentier m'éloigne "
        "du monde que je connaissais, me rapprochant d'un destin incertain.",
        
        "Certains prétendent qu'elle juge l'ambition... d'autres y voient un défi divin. "
        "Mais ce qui se trouve sommet...et bien, les legendes sont nombreuses, suffisament pour laisser les plus fous s'y aventurer.",

        "La crepuscule tombe lentement sur l’horizon, déchirée par des teintes de pourpre et de bleu. "
        "Une brume épaisse danse au pied de la tour, comme si la terre elle-même cherchait à cacher ce monstre de pierre.",
    ]  
    
    for dialogue in dialogues:
        screen.blit(background, (0, 0))
        pygame.display.flip()
        if isinstance(dialogue, tuple):
            display_dialogue_with_sprite(screen, dialogue[1], font, clock, dialogue[0])
        else:
            display_dialogue_box(screen, dialogue, font, clock)
     
       
    background = fade_in_background(screen, "graphics/resources/backgrounds/Colline.PNG", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    dialogues = [
        "Au loin, la tour se dresse, avec une silhouette d'obsidienne luisante, projetant son ombre jusqu'aux étoiles. "
        "Chaque pierre semble polie par des siècles de tempêtes et de sang versé.",
        (sprites["Aldric"],"Aldric (murmurant) : La voilà… comme dans mes rêves…"),
        "Perché sur une colline, Aldric contemple la Tour depuis les hauteurs. Le vent balaie son manteau clair, "
        "et ses cheveux blonds tombent en mèches éparses sur son front. L'épée sans garde à sa ceinture semble légère, mais ses doigts la frôlent par réflexe.",
    ]

    for dialogue in dialogues:
        screen.blit(background, (0, 0))
        pygame.display.flip()
        if isinstance(dialogue, tuple):
            display_dialogue_with_sprite(screen, dialogue[1], font, clock, dialogue[0])
        else:
            display_dialogue_box(screen, dialogue, font, clock)

    # Transition en fondu vers la scène suivante
    fade_out(screen, WIDTH, HEIGHT)
    clear_screen(screen)

    fade_out_music(fade_duration=4000)

    # Poursuite du prologue avec l'environnement autour de la Tour
    clear_screen(screen)
    fade_in_text(screen, 
             "Autour de la Tour", 
             font, 
             (WIDTH // 2, HEIGHT // 2),  # Centré sur l'écran
             duration=3000)
    fade_out_text(screen, 3000, fade_speed=2)
    pygame.time.wait(1000)
    fade_in_music("graphics/resources/music/bell.mp3", max_volume=0.2, fade_duration=4000)
    clear_screen(screen)
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/enbas.webp", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    # Liste des dialogues autour de la Tour
    dialogues_autour_tour = [
        "En contrebas, une masse de silhouettes s'agite. Des dizaines de participants, guerriers, voleurs et mages se tiennent "
        "devant l’entrée de la Tour, scrutant l'obscurité avec appréhension.",
    
        "Dans un coin, un vieil homme vêtu d'une cape poussiéreuse murmure en boucle des avertissements. La Tour dévore tout… Le sommet ? "
        "Un mensonge. Personne ne revient jamais… Mais peu lui prêtent attention. Ils sont là pour une raison. Ils ont des comptes à régler.",
    
        "Non loin, une silhouette d'un vieux mage s’appuie sur un bâton orné de runes anciennes, observant la Tour avec un air de familiarité. "
        "Ses yeux mi-clos semblent sonder quelque chose au-delà des murs de pierre. Un étrange calme entoure cet homme malgré l’effervescence ambiante.",
    
        "Plus loin, deux jeunes figures, presque identiques, échangent à voix basse. "
        "Le garçon, légèrement plus grand, trace des cercles dans la terre de la pointe de son bâton, "
        "tandis que sa sœur resserre la sangle d’un grimoire fatigué sur son dos. Tous deux arborent des vêtements marqués de symboles tribaux.",
    
        "Adossée à une pierre, une archère affûte la pointe de ses flèches à l’aide d’un petit couteau. "
        "Son regard vif scrute discrètement chaque participant, mais elle évite soigneusement tout contact visuel prolongé. "
        "Un bandage à peine visible serpente autour de son bras gauche.",
    
        "À l’ombre d’une torche vacillante, un homme mince jongle distraitement avec deux dagues. "
        "Son sourire narquois ne quitte jamais ses lèvres, et chaque fois qu’une dague scintille sous la lumière, "
        "son regard dérive vers les autres participants, comme s’il pesait déjà leurs chances de survie."
    ]
     # Affiche chaque ligne du dialogue avec display_delay
    afficher_dialogues(screen, font, clock, dialogues_autour_tour)

    clear_screen(screen)
    background = fade_in_background(screen,"graphics/resources/backgrounds/bande.webp", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    # Interaction avec Aldric
    display_dialogue_with_sprite(screen, 
    "??? (une voix rauque s’élève derrière Aldric) : C’est la première fois que tu viens ici ?",
    font,clock, sprite_brandio)
    
    display_dialogue_with_sprite(screen, 
    "Aldric (se retournant légèrement) : Oui. C’est encore plus flippant et impressionnant que dans les récits.",
    font,clock, sprite_aldric)
    
    display_dialogue_box(screen, 
    "La voix appartient à un homme massif, vêtu d’une armure cabossée. Son visage est marqué par d’anciennes cicatrices, "
    "Il arbord le blason d'une des gardes de l'empire, il est accompagné de ses compagnons,"
    "celui qui semble etre leur chef ressemble à un roi des voleurs et son acolyte plus petit aux cheveux rouges se tient pas loin a coté d'une femme.",
    font,clock)
    
    display_dialogue_with_sprite(screen, 
    "??? (hochant la tête) : Impressionnant, hein… ? Jusqu’à ce que tu sois là-dedans. C'est tuer ou être tué ici. Garde ca a l'esprit, personne te fera de cadeaux",
    font,clock, sprite_brandio)
    
    display_dialogue_with_sprite(screen, 
    "Aldric (s'éloignant) : Hm...Le conseil vaut aussi pour toi..",
    font,clock, sprite_aldric)
    
    display_dialogue_with_sprite(screen,
    "??? : Alors comme ca tu parle aux etrangers Brandio ?", font, clock, sprite_velm)
    
    display_dialogue_with_sprite(screen, 
    "Brandio : Un etranger ?", font, clock, sprite_brandio)
    
    display_dialogue_with_sprite(screen,
    "??? (L'homme au long manteau joue avec son anneau en regardant la scène) : Velm a raison, Ce type n'est clairement pas de l'empire...Ca se voit, gardons le à l'oeil," 
    " il pourrait bien sortir du lot.", font, clock, sprite_clotaire)
    
    display_dialogue_with_sprite(screen,
    "???  : N'oublie pas Clotaire, J'accepte de faire quelques étages avec vous car ca m'est profitable, mais ne compter pas sur moi sur la totalité de l'ascension.." 
    , font, clock, sprite_emphyr)
    
    display_dialogue_with_sprite(screen,
    "Clotaire (faisant une reverance pour se moquer)  : Oui m'dame ! Nous sommes vos obligés Ô dame Emphyr !" 
    , font, clock, sprite_clotaire)
    
    clear_screen(screen)
    fade_in_background(screen,"graphics/resources/backgrounds/attente.PNG", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    display_dialogue_box(screen, 
    "Plus loin, Devant Aldric se trouve des dizaines de participants forment des groupes dispersés, certains adossés aux parois rocheuses, d'autres concentrés "
    "dans des cercles discrets. Quelques torches éclairent faiblement les visages tendus et les reflets métalliques des lames. ",
    font,clock)
    
    # Interaction avec Garen
    garen = Character("Garen", "graphics/resources/sprites/Garen1.webp", 
                  "Un jeune homme sincère mais maladroit.", 
                  "Protecteur", gender="garçon")

    hero.add_relation(garen, "Neutre")


    display_dialogue_with_sprite(screen, 
    "Garen : Salut… Euh… toi aussi, tu participes ? Haha, évidemment, sinon tu ne serais pas là, hein ?\n",
    font,clock, sprite_garen)
    
    display_dialogue_box(screen,
    "La voix semble amicale mais vacille légèrement, signe d’un mélange de nervosité et d’excitation contenue., le jeune homme aux cheveux marrons poursuit :", font, clock)

    display_dialogue_with_sprite(screen, 
    "Garen : Moi, c'est Garen. Je pensais qu'il serait peut-être utile d'avoir un allié ? "
    "Juste pour commencer, hein ? Héhé, on ne sait jamais... Cette tour... apparemment, c'est difficile, mais j'aimerais aller le plus loin possible.",
    font,clock,sprite_garen)

    display_dialogue_box(screen, 
    "Son sac en bandoulière semble lourd, rempli d'objets en tout genre, il porte une épauliere bas de gamme et d'occasion.",
    font,clock)

    display_dialogue_box(screen, 
    "Derrière Garen, quelques participants observent la scène avec curiosité. Certains échangent des murmures. "
    "Un homme encapuchonné ricane doucement, comme s'il devinait déjà le destin du jeune guerrier inexpérimenté.",
    font,clock)

    display_dialogue_with_sprite(screen, 
    "Aldric : Je ne savais pas que les paysans souhaiteraient participer à la tour…",
    font,clock,sprite_aldric)

    display_dialogue_with_sprite(screen, 
    "Garen (rougissant légèrement) : Je... Je ne suis pas un paysans ! enfin certes peut-être un peu... "
    "Dire que j'ai depensé toutes mes économies pour m'équiper...Et c'est tout que j'ai eu..",
    font,clock, sprite_garen)

    display_dialogue_with_sprite(screen, 
    "Aldric (calme) : Oh, vraiment ? Et tu comptes survivre combien de temps dans cette Tour avec des bottes trop grandes et une épée que tu ne sais pas tenir ?",
    font,clock, sprite_aldric)

    display_dialogue_with_sprite(screen, 
    "Garen (gêné) : Tout le monde commence quelque part, non ? Je me débrouillerai ! Je suis peut-être pas aussi expérimenté que toi, mais… "
    "j’ai ma place ici. Puis on pourrait faire équipe...non ?",
    font, clock, sprite_garen)

    # Ajout du dialogue interactif
    options = [
        (
            "Garen, hein ? Hm… On verra. Tu peux me suivre. Pour combien de temps...ça..",
            10,
            [
                (sprites["Garen"],"Garen esquisse un sourire sincère, visiblement soulagé. (Garen +10) "),
                (sprites["Garen"], "Garen : Tu verras, je suis pas si inutile que ça !"),
                (sprites["Aldric"],"Aldric : Hm. Espérons que tu dises vrai."),
                (sprites["Aldric"], "A mon avis, la moitié des participants, voir plus, vont tomber au cours des deux, trois premiers étages.."),
                (sprites["Garen"], "..."),
                (sprites["Garen"], "Je veux au moins essayer..."),
            ]
        ),
        (
            "Si tu me ralentis, je te laisse derrière. Compris ?",
            5,
            [
                (sprites["Garen"],"Garen hoche la tête avec résolution. Il vous suit tout en regardant la Tour.(Garen +5)"),
                (sprites["Garen"],"Garen (gêné) : Je ferai de mon mieux…"),
                (sprites["Aldric"],"Aldric (froidement) : Pas de place pour l'erreur."),
                (sprites["Aldric"],"Aldric : Combien d'étage tu vise avant de mourir ? moi 10 au bas mots"),
                (sprites["Garen"],"Garen (gêné) : Je..Je ne sais pas.."),  
            ]
        ),
        (
            "Tolérer Garen.",
            -5,
            [
                (sprites["Aldric"],"Aldric (taciturne) : Hm..fait comme tu veux, tu fera pas long feu de toute façon."),
                (sprites["Garen"],"Garen (tristement) : Laisse moi au moins une chance...je veux dire...(Garen -5)"),
                (sprites["Aldric"],"Aldric : Regarde la tour, tu crois qu'elle te fera des cadeaux ? Prepare toi...combien d'etage pense tu tenir ?"),
            ]
        )
    ]
    
    process_dialogue(screen, font, hero, options, clock, "Garen")
    clear_screen(screen)
    background = fade_in_background(screen,"graphics/resources/backgrounds/Aldrix x Garen.webp", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    
     # Échange supplémentaire
    display_dialogue_with_sprite(screen, 
    "Garen (baisse brièvement les yeux, visiblement mal à l'aise) :\n"
    "Je sais que personne n'a jamais atteint le sommet et que tout ceux qui ont tenté sont sois morts ou ne sont jamais resorti et sont toujours dedans..",
    font,clock, sprite_garen)

    display_dialogue_with_sprite(screen,
    "Aldric : Il paraît... mais personnellement, ça ne me fait ni chaud ni froid. Regarde autour de toi, ces gens, ils en ont plus rien à foutre..",
    font,clock, sprite_aldric)
    
    display_dialogue_with_sprite(screen,
    "Garen (souriant naivement) : Alors on sera les premiers !",
    font,clock, sprite_garen)
    
    display_dialogue_with_sprite(screen,
    "Aldric : Optimiste...moi je pense tenir 10 étages avant de mourir..(serrant le poing) même si je dois tenir plus longtemps...",
    font,clock, sprite_aldric)

    display_dialogue_box(screen, 
    "Vos doigts se resserrent sur le manche de votre épée courte sans garde, et vous levez les yeux vers la Tour imposante.",
    font,clock)

    display_dialogue_with_sprite(screen, 
    "Garen : Cette épée... elle ne vient pas d'ici, n'est-ce pas ? Je... je n'en ai jamais vu des comme ça. D'ou vient tu ? pas de l'Empire j'imagine..",
    font,clock, sprite_garen)

    display_dialogue_with_sprite(screen,
    "Aldric (sourcils froncés) : Ne la touche pas !...et non pas de l'empire..",
    font,clock, sprite_aldric)

    display_dialogue_with_sprite(screen, 
    "Garen (levant les mains en signe d'excuse) : Ah, pardon ahah... Je pose trop de questions. c'est rare les étrangers ici..",
    font,clock,sprite_garen )

    display_dialogue_with_sprite(screen, 
    "Garen (murmure) :Puis tu as l'air de savoir ce que tu fais… contrairement à moi.",
    font,clock,sprite_garen )
        
    # Création du personnage Kael
    kael = Character("Kael", "graphics/resources/sprites/Kael.webp", 
                 "Un homme élégant et provocant.", 
                 "Escrimeur", gender="garçon")
    hero.add_relation(kael, "Neutre")

    # Description initiale de l'arrivée de Kael
    display_dialogue_box(screen, 
        "Le vent se lève alors qu'Aldric poursuit son chemin vers la Tour. "
        "Garen marche maladroitement derrière, peinant à suivre. Autour de vous, des participants silencieux "
        "échangent des regards méfiants.",
        font, clock
    )
    
    clear_screen(screen)
    background = fade_in_background(screen,"graphics/resources/backgrounds/Kael1.PNG", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    display_dialogue_box(screen, 
        "Plus loin, adossé à un rocher imposant, un jeune homme observe la scène avec amusement. "
        "Son allure raffinée contraste avec l'ambiance oppressante. Il porte une rapière, une chemise blanche de noble, "
        "et ses cheveux blancs sont soigneusement coiffés vers l'arrière.",
        font,clock
    )
    display_dialogue_with_sprite(screen, 
        "Kael : Eh bien, voilà un spectacle intéressant... Un mercenaire accompagné d'un fermier. "
        "Dites-moi, vous espérez vraiment survivre au-delà du premier étage ?\n",
        font,clock, sprite_kael
    )
    display_dialogue_with_sprite(screen, 
        "Kael : Essaie au moins de ne pas salir le sol avec ton sang. J'aimerais mieux éviter de glisser et de mourir bêtement...",
        font,clock, sprite_kael
    )

    # Lancer le dialogue interactif après l'introduction de Kael
    options = [
    (
        "Et toi ? Tu comptes m'emmerder jusqu'à l'entrée ?",
        5,
        [
            (sprites["Kael"], "Kael (rire moqueur) : Hah ! Le chien mord ! Je sens que vais apprécier cette ascension !(Kael +5)"),
            (sprites["Aldric"], "Aldric : Ne t'attends pas à ce que je te nettoie si tu te salis, noble."),
            (sprites["Kael"], "Kael : Oh, je n'ai jamais eu besoin d'aide... et surtout pas de toi."),
            (sprites["Aldric"], "Aldric : Parfait...on est sur la même longueur d'onde.")
        ]
    ),
    (
        "Tu parles beaucoup pour quelqu'un qui n'a pas encore posé un pied dans la Tour.",
        -5,
        [
            (sprites["Kael"], "Kael (perd brièvement son sourire) : Ah… Un chien qui aboie. Espérons que tu mordes aussi fort.(Kael -5)"),
            (sprites["Kael"], "Kael (s'éloigne légèrement) : On verra qui de nous deux atteindra le sommet."),
            (sprites["Aldric"], "Aldric : Pas toi...de toute évidence..")
        ]
    ),
    (
        "Ignorer Kael et passer votre chemin.",
        -10,
        [
            (sprites["Kael"], "Kael (hausse les épaules) : Trop lâche pour répondre ? Peu importe, tu finiras comme les autres.(Kael -10)"),
            (sprites["Garen"], "Garen (regardant Kael d'un air irrité) : Quel sale type... encore un fichu noble.."),
            (sprites["Aldric"], "Aldric (froidement) : Ignore-le. Il ne vaut pas notre énergie.")
        ]
    )
]
    process_dialogue(screen, font, hero, options, clock, "Kael")
    #Scène de clôture après la rencontre avec Kael
    display_dialogue_box(screen, 
        "Kael s'éloigne lentement vers l'entrée de la Tour, laissant derrière lui un léger ricanement.",
        font,clock)
    display_dialogue_with_sprite(screen, "Garen (marmonnant) : On dirait qu'il adore se faire des ennemis.",font, clock, sprite_garen)
    display_dialogue_with_sprite(screen, "Aldric (calme) : Ce genre de personne sont souvent la première à tomber… ou les dernier à rester debout.",font, clock, sprite_aldric)

    observer = Character("Homme mystérieux", "graphics/resources/sprites/hmystere.webp", 
                     "Un homme en cape sombre et silencieux.", 
                     "Inconnu", gender="inconnu")
    hero.add_relation(observer, "Neutre")
    
    
    # Description de l'observateur
    clear_screen(screen)
    background = fade_in_background(screen,"graphics/resources/backgrounds/bastour.webp", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    display_dialogue_box(screen, 
        "La pluie commence à tomber alors qu'Aldric et Garen s'avancent vers la Tour. "
        "Les braseros alignés de part et d'autre de l'escalier s'embrasent lentement, illuminant les visages "
        "des participants à travers les gouttes d'eau.",
        font,clock
    )
    display_dialogue_box(screen, 
        "Non loin de l'entrée, une silhouette encapuchonnée se tient immobile, adossée à la paroi. "
        "Ses yeux, dissimulés sous l'ombre de sa capuche, vous suivent silencieusement.",
        font,clock
    )
    
    clear_screen(screen)
    background = fade_in_background(screen,"graphics/resources/backgrounds/hommMystere.webp", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    display_dialogue_with_sprite(screen, 
        "Homme mystérieux (calme) : Tu vas donc tenter la tour alors... hmpf",font, clock, sprite_mysterieux
    )
    #Interaction avec l'homme mystérieux près de l'entrée de la Tour."""
    options = [
    (
        "Hocher la tête respectueusement.",
        10,
        [
            (sprites["Aldric"], "Aldric (calmement) : On se connait ?"),
            (sprites["Homme_mysterieux"], "Homme mystérieux (hochant légèrement la tête) : Hm..qui sait..(Homme mystérieux +10)"),
            (sprites["Homme_mysterieux"], "Tu vois ces gens, ils ont tous le même rêve desespéré, et toi ? quel est le tient ?"),
            (sprites["Aldric"], "Allez savoir..."),
            (sprites["Homme_mysterieux"], "Hm...Pourquoi je demande...C'est assez évident."),
        ]
    ),
    (
        "Rester silencieux et attendre.",
        0,
        [
            (sprites["Aldric"], "Aldric (gardant son calme) : Vous restez immobile, observant l'homme sans répondre."),
            (sprites["Homme_mysterieux"], "Homme mystérieux (sourire en coin) : Je vois. Tu veux la jouer comme ça... intéressant !"),
            (sprites["Aldric"], "Quoi ? On s'apprete a tenter l'ascention j'ai besoin de me concentrer.."),
            (sprites["Homme_mysterieux"], "Interessant, je sens que tu va aller loin...du moins je l'espère")
        ]
    ),
    (
        "Lui répondre avec défiance.",
        -5,
        [
            (sprites["Aldric"], "Aldric (fronçant les sourcils) : Ça te pose un problème ? Qu'est-ce que ça peut te faire ?(Homme mystérieux -5)"),
            (sprites["Homme_mysterieux"], "Homme mystérieux (sombre) : Combien d'étage ton copain aller vous tenir (réflcéhis) hmmm..."),
            (sprites["Garen"], "Garen (inquiet) : Laissons-le tranquille."),
        ]
    )
]

    # Affichage du choix
    process_dialogue(screen, font, hero, options, clock, "Homme mystérieux")


# Dialogue de Garen

    display_dialogue_with_sprite(screen, 
    "Garen (chuchotant) : Ce type… il dégage quelque chose de bizarre. Tu crois qu'il va participer ?",
    font, clock, sprite_garen)

    display_dialogue_with_sprite(screen, 
    "Aldric (sombre) : Il n'est pas comme les autres… Il observe.",
    font, clock, sprite_aldric)

    display_dialogue_with_sprite(screen, 
    "Garen (tremblant) : C'est qui alors ?",
    font, clock, sprite_garen)
    
    # Dialogue narratif initial
    display_dialogue_box(screen, 
    "L'homme mystérieux disparaît lentement dans l'ombre de la Tour, laissant derrière lui une atmosphère pesante. "
    "Garen jette un regard nerveux dans sa direction, avant de détourner les yeux.",
    font, clock)

    # Dialogue de l'Homme mystérieux

    display_dialogue_with_sprite(screen, 
    "Homme mystérieux : L'ascension peut prendre des années, si tu survit assez longtmemps...Je sens que nous nous reverrons bientôt, Aldric…",
    font, clock, sprite_mysterieux)

    display_dialogue_with_sprite(screen, 
    "Aldric : Hm... ? Comment connaissait vous mon nom ? (dit-il d'un air méfiant)",
    font, clock, sprite_aldric)

    # Narration après la disparition de l'homme mystérieux
    display_dialogue_box(screen, 
    "L'homme mystérieux disparaît sans un mot dans l'obscurité qui commence à tomber.",
    font, clock)

    # Suite avec Garen
    display_dialogue_with_sprite(screen, 
    "Garen : Tu... tu t'appelles Aldric ?",
    font, clock, sprite_garen)

    display_dialogue_with_sprite(screen, 
    "Aldric : Oui, mais ça n'a pas d'importance... En route.",
    font, clock, sprite_aldric)

    display_dialogue_with_sprite(screen, 
    "Garen : Euh d'accord... Je ne voulais pas être intrusif…",
    font, clock, sprite_garen)
    
    clear_screen(screen)
    background = fade_in_background(screen,"graphics/resources/backgrounds/entree2.webp", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Narration - L'entrée de la tour
    display_dialogue_box(screen, 
    "L'entrée béante de la tour se dresse devant toi, avalant la lumière du jour. "
    "Tu franchis lentement le seuil, laissant derrière toi les murmures et la brume du monde extérieur. "
    "L'ascension commence…",
    font, clock)

    # Dialogue d'Aldric
    display_dialogue_with_sprite(screen, 
    "Aldric : La tour...Te voilà...Quoi qu'il en soit, je ne reculerai pas, plus jamais... "
    "Quoi qu'il arrive..Je te retrouverai..",
    font, clock, sprite_aldric)

    display_dialogue_with_sprite(screen, 
    "Garen : Te retrouverai ? Tu veux dire que… tu es là pour quelqu'un ?",
    font, clock, sprite_garen)
    
    # Narration de l'ascension
    display_dialogue_box(screen, 
    "Aldric continue à gravir les marches sans prêter attention à ce que dit Garen. "
    "Garen vous suit, la gorge nouée… Kael est déjà entré, et l'homme mystérieux a disparu. "
    "La terrible ascension peut enfin commencer.",
    font, clock)
    
    fade_out_music(fade_duration=4000)

    fade_in_text(screen, "Fin du Chapitre 1", font, (WIDTH // 2, HEIGHT // 2), duration=2000)
    fade_out_text(screen, 1000)

# Affiche le menu de jeu après le prologue (sans relancer le chapitre)
    while True:
        selected_option = game_menu(screen, font, clock, WIDTH, HEIGHT)
        if selected_option == 0:  # Continuer
            start_next_chapter(hero, screen, font, clock)
            break
        elif selected_option == 1:  # Afficher Relation
           display_relations_menu(screen, font, hero, clock, WIDTH, HEIGHT)
        elif selected_option == 2:  # Afficher Santé
            display_text(screen, f"Santé actuelle : {hero.health} HP", (WIDTH // 2 - 100, HEIGHT // 2), font)
            pygame.time.wait(2000)
            game_menu(screen, font, clock, WIDTH, HEIGHT)
        elif selected_option == 3:  # Sauvegarder
            message = save_game(hero)
            display_save_confirmation(screen, font, message)
        elif selected_option == 4:  # Quitter
            pygame.quit()
            sys.exit()

    fade_in_text(screen, 
    f"Chapitre {hero.chapter_reached} : L'Ascension continue", 
    font, 
    (WIDTH // 2, HEIGHT // 2), 
    duration=3000)



def start_game():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("99 Floors : Ascent")
    
    font = pygame.font.Font("graphics/resources/font/Cinzel-Regular.otf", 40)
    clock = pygame.time.Clock()

    selected_option = main_menu(screen, font, clock)

    if selected_option == 0:  # Nouvelle partie
        hero = Heros()
        prologue(hero, screen, font, clock)

    elif selected_option == 1:  # Charger partie
        hero = load_game()
        if hero is None:
            hero = Heros()  # Si aucune sauvegarde, créer un nouveau héros
            prologue(hero, screen, font, clock)
        else:
            if hero.chapter_reached == 1:
                # Affiche directement le game menu si le chapitre 1 est terminé
                selected_option = game_menu(screen, font, clock, WIDTH, HEIGHT, hero)
                if selected_option == 0:  # Continuer
                    start_next_chapter(hero, screen, font, clock)
                elif selected_option == 1:  # Afficher Relation
                    display_relations_menu(screen, font, hero, clock, WIDTH, HEIGHT)
                    game_menu(screen, font, clock, WIDTH, HEIGHT, hero)
                elif selected_option == 3:  # Sauvegarder
                    message = save_game(hero)
                    display_save_confirmation(screen, font, message)
                    game_menu(screen, font, clock, WIDTH, HEIGHT, hero)
                elif selected_option == 4:  # Quitter
                    pygame.quit()
                    sys.exit()
            else:
                prologue(hero, screen, font, clock)

    elif selected_option == 2:  # Quitter
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    start_game()
    
  # Affichage du menu à la fin du prologue
hero = Heros()  # Initialisation correcte du héros
running = True
clock = pygame.time.Clock()
game_started = False
menu_displayed = False  # Pour afficher le menu uniquement après le prologue

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lancer le prologue au début
    if not game_started:
        game_started = True
        menu_displayed = True

    # Affichage du menu à la fin du prologue
    if menu_displayed:
        game_menu = GameMenu(hero)
        menu_running = True
        while menu_running:
            game_menu.draw(screen, font)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    menu_running = False
                choice = game_menu.handle_input(event)
                if choice == 0:
                    fade_out(screen, WIDTH, HEIGHT)
                    start_next_chapter(hero, screen, font, clock)
                    menu_running = False
                elif choice == 1:
                    print("Afficher Relations...")
                elif choice == 2:
                    message = save_game(hero)
                    display_save_confirmation(screen, font, message)
                elif choice == 3:
                    running = False
                    menu_running = False  # Quitte tout le programme après avoir choisi "Quitter"

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

    
