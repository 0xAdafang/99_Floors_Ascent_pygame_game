import pygame
import sys
from classes import *
from pygame.locals import *
from graphics import *
from utils import *
from save_manager import save_game,load_game


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("99 Floors : Ascent")

main_font = pygame.font.Font("graphics/resources/font/Cinzel-Regular.otf", 40)
font = main_font  # Utilisation partout sauf pour le titre




            
def chapitre_1(hero, screen, font, clock, sprites):
    
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
    fade_in_music("graphics/resources/music/Erebor.mp3", max_volume=0.2, fade_duration=4000)
    
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
             "Chapitre 1 : Au pied de l'ascension", 
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
        (sprites["Aldric"],"Aldric (murmurant) : La voilà… comme dans mes rêves…, j'espère trouver les réponses que je cherche.."),
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
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/aldric.webp", WIDTH, HEIGHT)
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
    "La voix appartient à un homme massif, vêtu d’une armure cabossée. Son visage est marqué par d’anciennes cicatrices. "
    "Il arbore le blason d'une des gardes de l'Empire. Il est accompagné de ses compagnons, "
    "celui qui semble être leur chef ressemble à un roi des voleurs, et son acolyte, plus petit, aux cheveux rouges, "
    "se tient non loin à côté d'une femme.",
    font, clock)
    
    display_dialogue_with_sprite(screen, 
    "??? (hochant la tête) : Impressionnant, hein… ? Jusqu’à ce que tu sois là-dedans. C'est tuer ou être tué ici. "
    "Garde ça à l'esprit, personne ne te fera de cadeaux.",
    font, clock, sprite_brandio)
    
    display_dialogue_with_sprite(screen, 
    "Aldric (s'éloignant) : Hm... Le conseil vaut aussi pour toi.",
    font, clock, sprite_aldric)
    
    display_dialogue_with_sprite(screen,
    "??? : Alors comme ça tu parles aux étrangers, Brandio ?", font, clock, sprite_velm)
    
    display_dialogue_with_sprite(screen, 
    "Brandio : Un étranger ?", font, clock, sprite_brandio)
    
    display_dialogue_with_sprite(screen,
    "??? (L'homme au long manteau joue avec son anneau en regardant la scène) : Velm a raison. "
    "Ce type n'est clairement pas de l'Empire... Ça se voit. Gardons-le à l'œil, "
    "il pourrait bien sortir du lot.", font, clock, sprite_clotaire)

    display_dialogue_with_sprite(screen,
    "??? : N'oublie pas, Clotaire, j'accepte de faire quelques étages avec vous car cela m'est profitable, "
    "mais ne comptez pas sur moi pour la totalité de l'ascension.", font, clock, sprite_emphyr)
    
    display_dialogue_with_sprite(screen,
    "Clotaire (faisant une révérence moqueuse) : Oui m'dame ! Nous sommes vos obligés, ô dame Emphyr !", 
    font, clock, sprite_clotaire)
    
    clear_screen(screen)
    background = fade_in_background(screen,"graphics/resources/backgrounds/attente.PNG", WIDTH, HEIGHT)
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
    "Garen : Salut… Euh… toi aussi, tu participes ? Haha, évidemment, sinon tu ne serais pas là, hein ?",
    font, clock, sprite_garen)
    background = fade_in_background(screen,"graphics/resources/backgrounds/garen1.webp", WIDTH, HEIGHT)
    
    display_dialogue_box(screen,
    "La voix semble amicale mais vacille légèrement, signe d’un mélange de nervosité et d’excitation contenue. "
    "Le jeune homme aux cheveux marrons poursuit :", font, clock)

    display_dialogue_with_sprite(screen, 
    "Garen : Moi, c'est Garen. Je pensais qu'il serait peut-être utile d'avoir un allié ? "
    "Juste pour commencer, hein ? Héhé, on ne sait jamais... Cette tour... apparemment, c'est difficile, "
    "mais j'aimerais aller le plus loin possible.",
    font, clock, sprite_garen)

    display_dialogue_box(screen, 
    "Son sac en bandoulière semble lourd, rempli d'objets en tout genre. Il porte une épaulière bas de gamme et d'occasion.",
    font, clock)

    display_dialogue_box(screen, 
    "Derrière Garen, quelques participants observent la scène avec curiosité. Certains échangent des murmures. "
    "Un homme encapuchonné ricane doucement, comme s'il devinait déjà le destin du jeune guerrier inexpérimenté.",
    font, clock)

    display_dialogue_with_sprite(screen, 
    "Aldric : Je ne savais pas que les paysans souhaitaient participer à la tour…",
    font, clock, sprite_aldric)

    display_dialogue_with_sprite(screen, 
    "Garen (rougissant légèrement) : Je... Je ne suis pas un paysan ! Enfin, certes, peut-être un peu... "
    "Dire que j'ai dépensé toutes mes économies pour m'équiper... Et c'est tout ce que j'ai eu.",
    font, clock, sprite_garen)
    
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
        "Garen, hein ? Hm… On verra. Tu peux me suivre. Pour combien de temps... ça...",
        10,
        [
            (sprites["Garen"], "Garen esquisse un sourire sincère, visiblement soulagé. (Garen +10)"),
            (sprites["Garen"], "Garen : Tu verras, je ne suis pas si inutile que ça !"),
            (sprites["Aldric"], "Aldric : Hm. Espérons que tu dises vrai."),
            (sprites["Aldric"], "À mon avis, la moitié des participants, voire plus, tomberont au cours des deux ou trois premiers étages..."),
            (sprites["Garen"], "..."),
            (sprites["Garen"], "Je veux au moins essayer..."),
        ]
    ),
    (
        "Si tu me ralentis, je te laisse derrière. Compris ?",
        5,
        [
            (sprites["Garen"], "Garen hoche la tête avec résolution. Il vous suit tout en regardant la Tour. (Garen +5)"),
            (sprites["Garen"], "Garen (gêné) : Je ferai de mon mieux…"),
            (sprites["Aldric"], "Aldric (froidement) : Pas de place pour l'erreur."),
            (sprites["Aldric"], "Aldric : Combien d'étages tu vises avant de mourir ? Moi, dix au bas mot."),
            (sprites["Garen"], "Garen (gêné) : Je... Je ne sais pas..."),
        ]
    ),
    (
        "Tolérer Garen.",
        -5,
        [
            (sprites["Aldric"], "Aldric (taciturne) : Hm... Fais comme tu veux. Tu ne feras pas long feu de toute façon."),
            (sprites["Garen"], "Garen (tristement) : Laisse-moi au moins une chance... Je veux dire... (Garen -5)"),
            (sprites["Aldric"], "Aldric : Regarde la Tour, tu crois qu'elle te fera des cadeaux ? Prépare-toi... Combien d'étages penses-tu tenir ?"),
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
    "Je sais que personne n'a jamais atteint le sommet, et que tous ceux qui ont tenté sont soit morts, soit n'en sont jamais ressortis... "
    "Ils sont toujours dedans...",
    font, clock, sprite_garen)

    display_dialogue_with_sprite(screen,
    "Aldric : Il paraît... mais personnellement, ça ne me fait ni chaud ni froid. Regarde autour de toi, ces gens, ils n'en ont plus rien à foutre.",
    font, clock, sprite_aldric)
    
    display_dialogue_with_sprite(screen,
    "Garen (souriant naïvement) : Alors on sera les premiers !",
    font, clock, sprite_garen)
    
    display_dialogue_with_sprite(screen,
    "Aldric : Optimiste... Moi, je pense tenir dix étages avant de mourir... (serrant le poing) Même si je dois tenir plus longtemps...",
    font, clock, sprite_aldric)

    display_dialogue_box(screen, 
    "Vos doigts se resserrent sur le manche de votre épée courte sans garde, et vous levez les yeux vers la Tour imposante.",
    font, clock)

    display_dialogue_with_sprite(screen, 
    "Garen : Cette épée... elle ne vient pas d'ici, n'est-ce pas ? Je... je n'en ai jamais vu des comme ça. D'où viens-tu ? Pas de l'Empire j'imagine...",
    font, clock, sprite_garen)

    display_dialogue_with_sprite(screen,
    "Aldric (sourcils froncés) : Ne la touche pas !... Et non, je ne viens pas de l'Empire.",
    font, clock, sprite_aldric)

    display_dialogue_with_sprite(screen, 
    "Garen (levant les mains en signe d'excuse) : Ah, pardon, ahah... Je pose trop de questions. C'est rare les étrangers ici.",
    font, clock, sprite_garen)

    display_dialogue_with_sprite(screen, 
    "Garen (murmure) : Puis tu as l'air de savoir ce que tu fais… contrairement à moi.",
    font, clock, sprite_garen)

        
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
    background = fade_in_background(screen,"graphics/resources/backgrounds/kael1.webp", WIDTH, HEIGHT)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    display_dialogue_box(screen, 
    "Plus loin, adossé à un rocher imposant, un jeune homme observe la scène avec amusement. "
    "Son allure raffinée contraste avec l'ambiance oppressante. Il porte une rapière, une chemise blanche de noble, "
    "et ses cheveux blancs sont soigneusement coiffés vers l'arrière.",
    font, clock
    )

    display_dialogue_with_sprite(screen, 
    "Kael : Eh bien, voilà un spectacle intéressant... Un mercenaire accompagné d'un fermier. "
    "Dites-moi, vous espérez vraiment survivre au-delà du premier étage ?",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen, 
    "Garen (détournant le regard) : Je ne suis pas juste un fermier... J'ai mes raisons de monter cette Tour.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen, 
    "Kael (ricane) : Tes raisons, hein ? C'est mignon. Peut-être devrais-tu retourner cultiver tes champs. "
    "Il est rare que les champs mordent en retour.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen, 
    "Garen (baissant la tête) : ... Je suis peut-être inexpérimenté, mais je n'ai pas peur.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen, 
    "Kael : Hahaha, admirable ! Je suis sûr que ton courage impressionnera les monstres... juste avant qu'ils ne t'avalent tout cru.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen, 
    "Kael : Essaie au moins de ne pas salir le sol avec ton sang. J'aimerais mieux éviter de glisser et de mourir bêtement...",
    font, clock, sprite_kael
    )


    # Lancer le dialogue interactif après l'introduction de Kael
    options = [
    (
        "Et toi ? Tu comptes m'emmerder jusqu'à l'entrée ?",
        5,
        [
            (sprites["Kael"], "Kael (rire moqueur) : Hah ! Le chien mord ! Je sens que je vais apprécier cette ascension. (Kael +5)"),
            (sprites["Aldric"], "Aldric : Ne t'attends pas à ce que je te nettoie si tu te salis, noble."),
            (sprites["Kael"], "Kael : Oh, je n'ai jamais eu besoin d'aide... et surtout pas de toi."),
            (sprites["Aldric"], "Aldric : Parfait... on est sur la même longueur d'onde."),
            (sprites["Garen"], "Garen (à voix basse) : Il a de la répartie... mais il est agaçant quand même.")
        ]
    ),
    (
        "Tu parles beaucoup pour quelqu'un qui n'a pas encore posé un pied dans la Tour.",
        -5,
        [
            (sprites["Kael"], "Kael (perd brièvement son sourire) : Ah… Un chien qui aboie. Espérons que tu mordes aussi fort. (Kael -5)"),
            (sprites["Kael"], "Kael (s'éloigne légèrement) : On verra qui de nous deux atteindra le sommet."),
            (sprites["Aldric"], "Aldric : Pas toi... de toute évidence."),
            (sprites["Garen"], "Garen (regardant Kael du coin de l'œil) : Pourquoi il cherche à provoquer tout le monde ?")
        ]
    ),
    (
        "Ignorer Kael et passer votre chemin.",
        -10,
        [
            (sprites["Kael"], "Kael (hausse les épaules) : Trop lâche pour répondre ? Peu importe, tu finiras comme les autres. (Kael -10)"),
            (sprites["Garen"], "Garen (regardant Kael d'un air irrité) : Quel sale type... encore un fichu noble."),
            (sprites["Aldric"], "Aldric (froidement) : Ignore-le. Il ne vaut pas notre énergie."),
            (sprites["Garen"], "Garen (soufflant discrètement) : Je n'aime pas ce gars... mais il a peut-être raison sur certaines choses.")
        ]
    )
    ]

    process_dialogue(screen, font, hero, options, clock, "Kael")
    #Scène de clôture après la rencontre avec Kael
    display_dialogue_box(screen, 
        "Kael s'éloigne lentement vers l'entrée de la Tour, laissant derrière lui un léger ricanement.",
        font,clock)
    display_dialogue_with_sprite(screen, "Garen (marmonnant) : On dirait qu'il adore se faire des ennemis.",font, clock, sprite_garen)
    display_dialogue_with_sprite(screen, "Aldric (calme) : Ce genre de personne sont souvent la première à tomber…",font, clock, sprite_aldric)

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
            (sprites["Aldric"], "Aldric (calmement) : On se connaît ?"),
            (sprites["Homme_mysterieux"], "Homme mystérieux (hochant légèrement la tête) : Hm... qui sait... (Homme mystérieux +10)"),
            (sprites["Homme_mysterieux"], "Tu vois ces gens, ils ont tous le même rêve désespéré. Et toi ? Quel est le tien ?"),
            (sprites["Aldric"], "Allez savoir..."),
            (sprites["Homme_mysterieux"], "Hm... Pourquoi je demande... C'est assez évident."),
            (sprites["Garen"], "Garen (chuchotant) : C'est qui ce gars ? Il te connaît vraiment ou c'est juste un de ces fous de la Tour ?")
        ]
    ),
    (
        "Rester silencieux et attendre.",
        0,
        [
            (sprites["Aldric"], "Aldric (gardant son calme) : Vous restez immobile, observant l'homme sans répondre."),
            (sprites["Homme_mysterieux"], "Homme mystérieux (sourire en coin) : Je vois. Tu veux la jouer comme ça... intéressant !"),
            (sprites["Aldric"], "Quoi ? On s'apprête à tenter l'ascension, j'ai besoin de me concentrer..."),
            (sprites["Homme_mysterieux"], "Intéressant. Je sens que tu vas aller loin... du moins je l'espère."),
            (sprites["Garen"], "Garen (baissant la voix) : Il est bizarre... mais il a peut-être raison. Tu es plus calme que moi.")
        ]
    ),
    (
        "Lui répondre avec défiance.",
        -5,
        [
            (sprites["Aldric"], "Aldric (fronçant les sourcils) : Ça te pose un problème ? Qu'est-ce que ça peut te faire ? (Homme mystérieux -5)"),
            (sprites["Homme_mysterieux"], "Homme mystérieux (sombre) : Combien d'étages ton copain va-t-il tenir ? Hmmm..."),
            (sprites["Garen"], "Garen (inquiet) : Laissons-le tranquille."),
            (sprites["Garen"], "Garen (plus bas) : Il n'a peut-être pas tort... mais je préfère éviter ce genre de type.")
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
    "Homme mystérieux : L'ascension peut prendre des années, si tu survis assez longtemps... Je sens que nous nous reverrons bientôt, Aldric…",
    font, clock, sprite_mysterieux)

    display_dialogue_with_sprite(screen, 
    "Aldric : Hm... ? Comment connaissez-vous mon nom ? (dit-il d'un air méfiant)",
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
    "Aldric : La Tour... te voilà... Quoi qu'il en soit, je ne reculerai pas. Plus jamais... "
    "Quoi qu'il arrive... je te retrouverai peu importe le temps qu'il faudra.",
    font, clock, sprite_aldric)

    display_dialogue_with_sprite(screen, 
    "Garen : Te retrouver ? Tu veux dire que… tu es là pour quelqu'un ?",
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
    game_menu(screen, font, clock, WIDTH, HEIGHT, hero)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def chapitre_2(hero, screen, font, clock,sprites):
    
    global background
    
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
    sprite_random_participant = sprites["Participant"]
    
    fade_in_music("graphics/resources/music/AmbientHades.mp3", max_volume=0.2, fade_duration=1000)
    clear_screen(screen)
    fade_in_text(screen, 
             "Chapitre 2 : L'ascension commence - Etage 1/99", 
             font, 
             (WIDTH // 2, HEIGHT // 2),  # Centré sur l'écran
             duration=3000)
    fade_out_text(screen, 3000, fade_speed=2)
    pygame.time.wait(1000)
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/porte.webp", WIDTH, HEIGHT)
   # Narration de l'étage 1
    display_dialogue_box(screen,
    "La lourde porte de pierre se referme derrière vous dans un grondement sourd. L’intérieur de la Tour est sombre, "
    "éclairé seulement par quelques torches vacillantes. L’air est froid, chargé de l’odeur de pierre humide.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Kael : Plus de retour en arrière possible hein ?",
    font, clock, sprite_kael
    )

    display_dialogue_box(screen,
    "Un silence pesant s’installe, comme si la Tour elle-même retenait son souffle. "
    "Les bruits de pas résonnent à chaque mouvement, amplifiés par l’architecture de la salle. "
    "Chaque écho semble étirer l’espace, donnant l’impression que les murs vous observent en silence.",
    font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/hall.webp", WIDTH, HEIGHT)
    display_dialogue_box(screen,
    "Un vaste hall circulaire s’étend devant vous, orné de statues de guerriers alignées le long des murs. "
    "Leur regard semble peser sur chaque nouvel arrivant. Garen reste proche de vous, tandis que Kael s’avance légèrement en tête.",
    font, clock
    )

    display_dialogue_box(screen,
    "Une immense porte de fer se dresse au fond du hall. Une grille d’acier noirci la barre. Devant elle, "
    "une inscription brille faiblement à la lumière des torches :\n"
    "« Seuls ceux qui abandonnent peuvent passer. Mais que perdez-vous vraiment ? »",
    font, clock
    )

    display_dialogue_box(screen,
    "L’inscription semble danser sous l’effet de la flamme vacillante des torches. "
    "L’air devient plus dense, comme si la pièce attendait votre décision. "
    "Au loin, un léger craquement se fait entendre, mais rien ne semble bouger. "
    "Pourtant, cette salle dégage une énergie sourde… presque vivante.",
    font, clock
    )

# Nouveau paragraphe pour ajouter des détails sur l'environnement
    display_dialogue_box(screen,
    "En observant plus attentivement, vous remarquez que les statues ne sont pas simplement décoratives. "
    "Certaines d’entre elles possèdent d’étranges cavités dissimulées dans leur plastron ou au niveau de leurs mains tendues. "
    "Des traces de poussière déplacée et des rayures autour de ces cavités suggèrent que d’autres ont tenté d’y glisser des objets.",
    font, clock
    )

    display_dialogue_box(screen,
    "Certains participants semblent avoir eu la même idée. Un homme à la carrure imposante essaie d’insérer un médaillon dans la cavité d’une statue, "
    "mais celle-ci reste inerte. Un autre, plus jeune, dépose une bourse pleine de pièces dans les mains d’une autre statue. "
    "Un bruit sourd résonne, mais rien ne se produit. Frustré, il récupère son or en lançant un regard inquiet vers la porte.",
    font, clock
    )

    display_dialogue_box(screen,
    "Plus loin, une femme vêtue d’une cape sombre prie devant l’une des statues. "
    "Elle murmure quelques mots et glisse un petit poignard dans la fente d’une autre cavité. "
    "Pendant un bref instant, il semble que la lumière des torches faiblisse, mais le phénomène disparaît aussi rapidement qu’il est apparu.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Kael : Je parie qu’on pourrait rester ici toute la nuit à observer ces clowns. "
    "Ils donnent tout ce qu’ils ont… Je doute que ce soit aussi simple.",
    font, clock, sprite_kael  
    )

    display_dialogue_with_sprite(screen,
    "Garen : Peut-être qu’il ne s’agit pas de donner… mais de comprendre ce que nous devons vraiment abandonner.",
    font, clock, sprite_garen ) 
    
    display_dialogue_box(screen,
    "La voix de Garen résonne légèrement dans la salle. "
    "Le silence pesant qui suit vous donne l’impression que les statues vous écoutent… "
    "comme si elles attendaient quelque chose de plus personnel, de plus profond.",
    font, clock
    )
    
    choix = display_choices_box(screen, font, [
    ("Déposer votre arme devant une statue", 0),
    ("Offrir une partie de vos provisions", 1),
    ("Observer davantage avant d’agir", 2)
    ], clock)

    if choix == 0:
        display_dialogue_box(screen,
        "Vous déposez votre épée devant une statue. "
        "Un courant d’air glacial traverse la pièce… mais rien ne se passe. "
        "Vous récupérez votre arme, son manche étrangement froid.",
        font, clock
        )
        hero.health -= 5  # Le héros ressent une légère perte de force (symbolique)
        hero.get_relation("Kael").adjust_score(+5)  # Kael apprécie votre audace

    elif choix == 1:
        display_dialogue_box(screen,
        "Vous sortez une ration de vos provisions et la posez devant la statue. "
        "Elle disparaît dans la cavité. Un léger bruit de mécanisme se fait entendre.",
        font, clock
        )
        hero.get_relation("Garen").adjust_score(+5)  # Garen apprécie ce sacrifice
        
    elif choix == 2:
        display_dialogue_box(screen,
        "Vous décidez de ne rien faire pour l’instant. "
        "Kael secoue la tête, mais Garen semble approuver votre prudence.",
        font, clock
        )
        hero.get_relation("Kael").adjust_score(-5)  # Kael n’aime pas l'hésitation
        hero.get_relation("Garen").adjust_score(+5)  # Garen respecte votre patience

    # Dialogue
    display_dialogue_with_sprite(screen,
    "Kael : Hah. Quelle plaisanterie. Il suffit d’abandonner pour avancer ? Je pensais que cette Tour serait plus créative.",
    font, clock, sprite_kael
    )
    
    display_dialogue_box(screen,
    "Votre bande s'enfonce plus profondément entre les statues silencieuses, "
    "jusqu'à ce qu'une étrange stèle se dresse au centre d'un passage étroit, partiellement dissimulée par l'ombre.",
    font, clock
    )
    background = fade_in_background(screen, "graphics/resources/backgrounds/stele1.webp", WIDTH, HEIGHT)

    display_dialogue_with_sprite(screen,
    "Aldric (jetant un regard à Kael) : Dis-moi, Kael… pourquoi tu nous suis encore ?",
    font, clock, sprite_aldric
    )

    display_dialogue_with_sprite(screen,
    "Kael (croisant les bras, légèrement embarrassé) : Hmph. C’est vous qui me suivez, pas l’inverse.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Garen (riant doucement) : Ah oui ? Alors pourquoi t’es toujours devant ?",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Kael (détournant les yeux) : Quelqu’un doit bien vous ouvrir la voie. Considérez ça comme un service.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Aldric (souriant) : Un vrai guide… Comment on ferait sans toi.",
    font, clock, sprite_aldric)
    
    options = [
    ("Allez avoue le, tu fait le brave mais tu sais aussi que l'ascension est perilleuse.", 0),
    ("Je crois que tu as juste peur d’avancer seul.", 1),
    ("Tant que tu restes devant et que tu attires les ennuis, ça me va.", 2)
    ]

    choix = display_choices_box(screen, font, options, clock)

    # Résolution des choix et modification des relations
    if choix == 0:
        display_dialogue_with_sprite(screen,
        "Kael (léger sourire) : Hah… C’est vrai, je suis un peu votre protecteur. Essayez juste de ne pas trop compter sur moi.(Kael +5)",
        font, clock, sprite_kael
    )
        hero.get_relation("Kael").adjust_score(+5)  # Relation avec Kael améliorée

    elif choix == 1:
        display_dialogue_with_sprite(screen,
        "Kael (fixant Aldric, piqué au vif) : Je n’ai peur de rien. Mais si vous traînez derrière moi, "
        "c’est peut-être vous qui cherchez une protection.(Kael -5, Garen +5)",
        font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
        "Garen (souriant) : Touché.",
        font, clock, sprite_garen
        )
        hero.get_relation("Kael").adjust_score(-5)  # Kael perd des points
        hero.get_relation("Garen").adjust_score(+5)  # Garen gagne des points

    elif choix == 2:
        display_dialogue_with_sprite(screen,
        "Kael (roulant des yeux) : Charmant. Tant que vous me laissez les ennuis, vous pouvez toujours compter sur moi.",
        font, clock, sprite_kael
    )
        display_dialogue_with_sprite(screen,
        "Garen (ricanant) : Voilà une répartition équitable.(Kael -2, Garen +2)",
        font, clock, sprite_garen
    )
        hero.get_relation("Kael").adjust_score(-2)  # Légère perte de relation avec Kael
        hero.get_relation("Garen").adjust_score(+2)  # Relation avec Garen renforcée)
        
    
    
    display_dialogue_box(screen,
        "Kael croise les bras, jetant un regard dédaigneux à l’inscription. "
        "Malgré ses mots, son regard s’attarde un instant de trop sur les statues, "
        "comme s’il s’attendait à ce qu’elles bougent. Votre bande s'approche d'une stèle, Garen et Aldric tentent de la lire.",
        font, clock
        )


    display_dialogue_with_sprite(screen,
        "Garen (fronçant les sourcils) : C’est quoi cette langue ? Je… je ne comprends rien.",
        font, clock, sprite_garen
        )

    display_dialogue_box(screen,
    "Garen s’approche davantage, plissant les yeux en suivant les gravures sur la pierre. "
    "Les symboles gravés dans la stèle lui sont totalement étrangers. "
    "Il recule légèrement, secouant la tête.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Garen : Cette langue… Ce n’est pas quelque chose que j’ai vu dans l’Empire. "
    "Je ne pense même pas que ça existe dans nos bibliothèques.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Kael (jetant un œil distrait) : Il a raison. Ce n’est pas une langue impériale.",
    font, clock, sprite_kael
    )

    display_dialogue_box(screen,
    "Kael scrute la stèle quelques instants de plus, comme s’il voulait prouver qu’il en savait davantage. "
    "Mais son regard se durcit rapidement, et il se détourne avec un léger rictus.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Kael : Si l’Empire ne l’a pas jugée digne d’être étudiée, ce n’est probablement qu’une relique inutile.",
    font, clock, sprite_kael
    )

    display_dialogue_box(screen,
    "Aldric reste silencieux, ses yeux fixés sur l’inscription. "
    "Un frisson parcourt l’air autour de lui tandis qu’il s’approche lentement, posant sa main sur la pierre froide.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Aldric (murmurant) : … S’abandonner… Abandonner sa fierté, embrasser l’humilité…",
    font, clock, sprite_aldric
    )

    display_dialogue_box(screen,
    "Les mots s’échappent de sa bouche sans qu’il en prenne pleinement conscience. "
    "La stèle semble vibrer légèrement sous sa paume.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Garen (étonné) : Attends, quoi ? Comment tu peux lire ça ?!",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Kael (plissant les yeux) : Tu te moques de nous, Aldric ? Ce n’est qu’une suite de symboles…",
    font, clock, sprite_kael
    )

    display_dialogue_box(screen,
    "Aldric retire lentement sa main, clignant des yeux comme s’il revenait à lui. "
    "Il fixe la stèle, surpris autant que ses compagnons.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Aldric (à voix basse) : Vous… vous ne pouvez pas le lire ? C’est pourtant clair…",
    font, clock, sprite_aldric
    )

    display_dialogue_with_sprite(screen,
    "Garen (médusé) : Pas du tout. Pour moi, ce sont juste des gribouillis…",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Kael (croisant les bras, l’air plus sérieux) : Et ce n’est certainement pas une langue impériale. "
    "Comment peux-tu comprendre quelque chose qui n’a jamais été répertorié ?",
    font, clock, sprite_kael
    )
    
    display_dialogue_with_sprite(screen,
    "Aldric : Ah ! J'avais oublié que je ne suis pas de l'empire, la d'ou je viens ces symboles sont omiprésents.."
    "On parle la langue de l'empire mais plusieurs stèles comme celle ci sont disséminée un peu partout dans ma contré, c'est ce qui m'a poussé à...",
    font, clock, sprite_aldric
    )

    display_dialogue_box(screen,
    "Un silence pesant s'installe, chacun réfléchissant aux implications. "
    "Soudain, des cris éclatent plus loin dans la salle. Des participants s’agitent frénétiquement autour d’un autre point d’intérêt.",
    font, clock
    )

    display_dialogue_box(screen,
    "Kael et Garen échangent un regard bref avant de porter la main à leurs armes, "
    "mais Aldric reste concentré sur la stèle, comme si elle recelait encore un secret.",
    font, clock
    )

    display_dialogue_box(screen,
    "Votre propre voix résonne dans l’obscurité. En avançant d’un pas, vous sentez la présence des statues peser davantage. "
    "Elles semblent vous scruter, jaugeant chaque mot, chaque hésitation. Aldric, Kael et Garen s'engouffre dans une des failles proche des statues et tombe sur un grande statues de guerrier.",
    font, clock
    )

    def chapitre_2_interaction(hero, screen, font, clock, sprites):
        global background
        background = fade_in_background(screen, "graphics/resources/backgrounds/enigme.webp", WIDTH, HEIGHT)

        display_dialogue_box(screen,
        "Un courant d’air glacial traverse la salle. La lumière des torches vacille légèrement, projetant des ombres tremblantes sur le sol de pierre.",
        font, clock
        )

        actions = [
        "Inspecter la porte de plus près.",
        "Examiner les statues alignées sur les murs.",
        "Observer la réaction des autres participants.",
        "Tenter de forcer la porte avec ton épée."
        ]

        choix_valide = False

        while not choix_valide and actions:
            options = [(action, i) for i, action in enumerate(actions)]

        # Affiche la boîte de choix et récupère l'index sélectionné
            choix = display_choices_box(screen, font, options, clock)

        # Applique l'action sélectionnée
            if actions[choix] == "Inspecter la porte de plus près.":
                display_dialogue_box(screen,
                "En t’approchant de la porte, tu remarques des gravures représentant des silhouettes agenouillées, "
                "déposant des objets devant une entité obscure.",
                font, clock
                )
                display_dialogue_with_sprite(screen,
                "Aldric : Intéressant. Ce n’est pas un simple abandon matériel. C’est… plus profond.",
                font, clock, sprites["Aldric"]
                )
                display_dialogue_with_sprite(screen,
                "Kael : Oh tu te mets à la philosophie maintenant ? Je ne savais pas que les mercenaires étaient cultivés.",
                font, clock, sprites["Kael"]
                )
                display_dialogue_with_sprite(screen,
                "Aldric : Tu devrais essayer, ça ne te ferait pas de mal.",
                font, clock, sprites["Aldric"]
                )
                display_dialogue_with_sprite(screen,
                "Kael : Le mercenaire a de la repartie. esperons que ca te serve..",
                font, clock, sprites["Kael"]
                )
                hero.get_relation("Kael").adjust_score(+5)
                choix_valide = True

            elif actions[choix] == "Examiner les statues alignées sur les murs.":
                display_dialogue_box(screen,
                "Les statues semblent représenter d’anciens guerriers. Certaines ont des fissures profondes au niveau de leur cœur "
                "ou de leurs mains. Sur l’une d’elles, il manque une arme.",
                font, clock
                )
                display_dialogue_with_sprite(screen,
                "Aldric : Ces statues… Ce ne sont peut-être pas que des œuvres d’art.",
                font, clock, sprites["Aldric"]
                )
                display_dialogue_with_sprite(screen,
                "Garen : Tu crois qu’ils étaient… comme nous ?",
                font, clock, sprites["Garen"]
                )
                display_dialogue_with_sprite(screen,
                "Aldric : Je ne sais pas... Ma théorie serait que ce sont d'anciens héros de la Tour ou bien… les fondateurs.",
                font, clock, sprites["Aldric"]
                )
                display_dialogue_with_sprite(screen,
                "Garen : Oooh mais oui ! Ça serait logique.",
                font, clock, sprites["Garen"]
                )
                hero.get_relation("Garen").adjust_score(+5)
                actions.remove("Examiner les statues alignées sur les murs.")

            elif actions[choix] == "Observer la réaction des autres participants.":
                display_dialogue_box(screen,
                "Certains participants chuchotent entre eux. L’un d’eux dépose son épée devant la porte… sans succès.",
                font, clock
                )
                display_dialogue_with_sprite(screen,
                "Kael : Pfff. La moitié va rester bloquée ici à essayer de comprendre.",
                font, clock, sprites["Kael"]
                )
                display_dialogue_with_sprite(screen,
                "Garen : Au lieu de te plaindre, tu ferais mieux de nous aider… mais tu es trop noble pour ça, hein ?",
                font, clock, sprites["Garen"]
                )
                display_dialogue_with_sprite(screen,
                "Kael : Un problème, paysan ? Avec ton équipement d'occasion… le marchand a dû faire une bonne affaire.",
                font, clock, sprites["Kael"]
                )
                display_dialogue_with_sprite(screen,
                "Garen : Tu aimes ça, hein ? Rabaisser les plus démunis… Vous me dégoûtez, vous les nobles.",
                font, clock, sprites["Garen"]
                )
                display_dialogue_with_sprite(screen,
                "Aldric : Ça suffit tous les deux… Par pitié… Concentrons-nous, c’est bel et bien une épreuve.",
                font, clock, sprites["Aldric"]
                )
                choix_valide = True

            elif actions[choix] == "Tenter de forcer la porte avec ton épée.":
                display_dialogue_box(screen,
                "Tu dégaines ton épée et frappes la grille, mais une lumière repousse la lame.",
                font, clock
                )
                display_dialogue_with_sprite(screen,
                "Kael (ricanant) : C’était… spectaculaire. Bravo.",
                font, clock, sprites["Kael"]
                )
                hero.get_relation("Kael").adjust_score(+5)

            # Supprime l'option pour éviter qu'elle soit réutilisée
                actions.remove("Tenter de forcer la porte avec ton épée.")
        
            else:
                display_dialogue_box(screen,
                "Choix invalide. Veuillez réessayer.",
                font, clock
            )
    chapitre_2_interaction(hero, screen, font, clock, sprites)
    # Ajout de la tension avec le passage du temps
    display_dialogue_box(screen,
    "Les heures s’écoulent lentement. Aucun des participants n’a trouvé la solution. "
    "Certains commencent à murmurer, jetant des regards inquiets vers la porte de fer. "
    "L’atmosphère devient de plus en plus pesante, presque suffocante.",
    font, clock
    )

    display_dialogue_box(screen,
    "Kael s’appuie contre une colonne, les bras croisés, scrutant les tentatives infructueuses. "
    "Garen reste vigilant, balayant la salle du regard. "
    "Au fil du temps, l’impatience s’installe. Un homme massif, à la barbe hirsute, commence à s’agiter.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Participant (hurlant) : Ça suffit ! Cette épreuve est une farce ! "
    "Je refuse de rester ici à attendre la mort !",
    font, clock, sprite_random_participant  # Sprite d'un participant générique
    )

    display_dialogue_with_sprite(screen,
    "Garen (calme) : Du calme. Nous finirons par comprendre. "
    "La panique ne nous aidera pas.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Participant : Tu crois tout savoir, hein ? Pourquoi tu ne passes pas devant et ne nous montres pas comment faire, Gamin ?",
    font, clock, sprite_random_participant
    )
    fade_out_music(fade_duration=1000)
    display_dialogue_with_sprite(screen,
    "Kael (murmurant à Aldric) : Ça va mal finir…",
    font, clock, sprite_kael
    )
    fade_in_music("graphics/resources/music/chase.mp3", max_volume=0.2, fade_duration=1000)
    background = fade_in_background(screen, "graphics/resources/backgrounds/attack.webp", WIDTH, HEIGHT)

    display_dialogue_box(screen,
    "Le participant se précipite soudain vers Garen, les poings levés, prêt à frapper.",
    font, clock
    )

    # Choix du joueur : Intervenir ou non
    choix = display_choices_box(screen, font, [
    ("Intervenir et tuer l’assaillant", 0),
    ("Se mettre devant Garen", 1),
    ("Ne rien faire", 2)
    ], clock)

    if choix == 0:  # Intervenir et tuer l'assaillant
        fade_out_music(fade_duration=1000)
        display_dialogue_box(screen,
        "Aldric s’élance sans hésiter et intercepte l’assaillant. "
        "Dans un mouvement fluide, il dégaine son épée et abat l’homme sur place. "
        "Le silence retombe, lourd et pesant.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Kael : Eh bien… tu n’y es pas allé de main morte. Espérons que cela dissuadera les autres.",
        font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
        "Garen (tête baissée) : Tu n'etait pas obligé de le tuer...(Garen -5, Kael +10)",
        font, clock, sprite_garen
        )
        hero.get_relation("Kael").adjust_score(+10)  # Kael apprécie la fermeté
        hero.get_relation("Garen").adjust_score(+5)
        

    elif choix == 1:  # Se mettre devant Garen
        fade_out_music(fade_duration=1000)
        display_dialogue_box(screen,
        "Vous vous placez devant Garen, prêt à encaisser l’attaque. "
        "L’assaillant s’élance… mais s’effondre soudainement, une dague enfoncée dans son dos. ",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Kael (baissant les yeux sur l’homme) : Tiens donc… Je ne l’ai pas vu venir. "
        "Quelqu’un ici ne plaisante pas.",
        font, clock, sprite_kael
        )
        display_dialogue_box(screen,
        "Vous regardez autour de vous, mais personne ne semble avoir bougé. "
        "La dague est noire et n’a aucune marque distinctive.(Garen +5)",
        font, clock
        )
        hero.get_relation("Garen").adjust_score(+5)  # Garen apprécie la protection

    elif choix == 2:  # Ne rien faire
        fade_out_music(fade_duration=1000)
        display_dialogue_box(screen,
        "L’assaillant bondit vers Garen… mais ses pieds se figent au sol. "
        "Des chaînes de lumière l’enserrent soudainement, le forçant à s’agenouiller. "
        "Au loin, un mage encapuchonné baisse lentement la main avant de disparaître dans l’ombre.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Kael (chuchotant) : Ce n’est pas un simple concours. "
        "Certains ici… sont prêts à tout.(Garen +5, Kael -5)",
        font, clock, sprite_kael
        )
        
        hero.get_relation("Kael").adjust_score(-5)  # Kael voit votre inaction comme un manque de courage
        hero.get_relation("Garen").adjust_score(+5)  # Garen comprend votre prudence
        
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/hall.webp", WIDTH, HEIGHT)
    fade_in_music("graphics/resources/music/AmbientHades.mp3", max_volume=0.2, fade_duration=1000)
    
    display_dialogue_with_sprite(screen,
    "Aldric : Ça va, Garen ?",
    font, clock, sprite_aldric
    )

    display_dialogue_with_sprite(screen,
    "Garen (s'essuyant le front) : Oui… J'ai bien failli être le premier à y passer. Merci de ton intervention.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Kael (ricanant légèrement) : Ce type avait l'air d'un paysan… Si vous vous battez même ici, "
    "ça en dit long sur votre sang.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Garen (froidement) : Tu crois vraiment que la noblesse protège de la stupidité ? "
    "Quand vient la guerre, vous êtes bien contents de laisser la piétaille paysanne nourrir vos armées "
    "et mourir en première ligne.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Garen (baissant légèrement la voix) : Mon frère… il est mort comme ça… "
    "pour protéger des terres qu’il n’a jamais possédées.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Kael (serrant les poings) : Peut-être… Mais ce sont nos maisons qui tombent en dernier. "
    "Quand tout s’effondre, nous sommes ceux qui portent le poids de la défaite.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Kael (fixant Garen) : Tu crois tout savoir. Mais quand ta propre maison brûle… "
    "ce n’est pas la piétaille qui reste pour te défendre.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Aldric (intervenant pour briser la tension) : Ça suffit. Ce n’est ni le lieu, ni le moment pour ces histoires. "
    "Nous devons rester concentrés.",
    font, clock, sprite_aldric
    )

    display_dialogue_with_sprite(screen,
    "Kael (détournant le regard) : Tch… Peu importe. "
    "Si ce genre d'épreuve vous effraie, vous ne survivrez pas longtemps ici.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Garen (murmurant) : Ce n’est pas la peur qui me tuera… mais l’arrogance de certains.",
    font, clock, sprite_garen
    )

    display_dialogue_box(screen,
    "Kael et Garen échangent un regard chargé de défi. "
    "L’incident semble clos, mais la tension entre eux est plus palpable que jamais. "
    "Aldric soupire intérieurement. La Tour est déjà assez dangereuse sans que des conflits internes n’enveniment la situation.",
    font, clock
    )
    
    # Conclusion de la scène
    display_dialogue_box(screen,
    "Après cet incident, les murmures s’atténuent. "
    "Tous retournent à l’observation de la porte, évitant soigneusement de croiser votre regard.",
    font, clock
    )

    display_dialogue_box(screen,
        "Après plusieurs minutes, un participant s’agenouille devant la porte, une main sur son cœur. La grille se lève lentement.",
        font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/solution.webp", WIDTH, HEIGHT)
    # Dialogue et narration après la découverte de la porte
    display_dialogue_with_sprite(screen,
    "Kael : Hm. Alors c’est ça… s’abandonner soi-même.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Garen (visiblement nerveux) : On… on fait quoi ? Je pense qu'on devrait s'agenouiller... c'est... c'est une épreuve d'humilité !!",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Kael (sarcastique) : Bien sûr… L’humilité sauvera nos vies. Pourquoi pas embrasser le sol pendant que tu y es ?",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Aldric (hésitant) : Peut-être que Garen a raison… Mais, si ce n’est pas ça ?",
    font, clock, sprite_aldric
    )

    display_dialogue_with_sprite(screen,
    "Kael (fixant la porte) : Peu importe ce que nous faisons, la Tour teste notre esprit. "
    "Je doute qu’elle laisse passer ceux qui se contentent de copier sans réfléchir.",
    font, clock, sprite_kael
    )

# Présentation des choix
    def chapitre_2_final_choice(hero, screen, font, clock, sprites):
        global background
        display_dialogue_box(screen,
        "La pression monte. L’air semble s’épaissir tandis que la salle retient son souffle.\n"
        "Que fais-tu ?",
        font, clock
        )

    # Définition des options de choix
        options = [
        ("S’agenouiller et traverser la porte.", 1),
        ("Observer et attendre.", 2),
        ("Ignorer et forcer la porte.", 3)
        ]

    # Affiche la boîte de choix
        choix = display_choices_box(screen, font, options, clock)

    # Gestion des choix
        if choix == 0:  # S’agenouiller et traverser la porte
            display_dialogue_with_sprite(screen,
            "Aldric s’agenouille lentement. Une chaleur étrange envahit ton corps tandis que la grille s'ouvre lentement. "
            "Garen, soulagé, suit votre exemple. Kael, bien qu’agacé, s’agenouille à son tour, fixant la porte avec mépris.",
            font, clock, sprite_aldric
            )
            display_dialogue_with_sprite(screen,
            "Kael : Si cette épreuve est censée représenter quelque chose, elle est pitoyable. (kael -2, Garen +3)",
            font, clock, sprite_kael
            )
            hero.get_relation("Garen").adjust_score(+5)
            hero.get_relation("Kael").adjust_score(-2)  # Kael déteste suivre les autres

        elif choix == 1:  # Observer et attendre
            display_dialogue_with_sprite(screen,
            "Vous restez immobile, scrutant la porte et les statues alentours. "
            "Kael s’impatiente mais reste à vos côtés, les bras croisés. "
            "Garen, mal à l’aise, s’agenouille seul, jetant des regards nerveux vers vous.",
            font, clock, sprite_kael
            )
            display_dialogue_with_sprite(screen,
            "Kael (soufflant) : Tu réfléchis trop, Aldric. Cette Tour ne nous attendra pas éternellement.(kael +3, Garen -3)",
            font, clock, sprite_kael
            )
            hero.get_relation("Kael").adjust_score(+3)
            hero.get_relation("Garen").adjust_score(-3)  # Garen doute de votre confiance

        elif choix == 2:  # Ignorer et forcer la porte
            display_dialogue_with_sprite(screen,
            "Aldric s’approche de la grille et tente de la pousser. "
            "Un courant d’air froid se glisse dans la salle. "
            "La porte ne bouge pas. Garen s’approche pour intervenir, mais Kael l’arrête d’un geste.",
            font, clock, sprite_kael
            )
            display_dialogue_with_sprite(screen,
            "Kael : Laisse-le. Il veut jouer au héros. Peut-être que la Tour a prévu de tester sa force…",
            font, clock, sprite_kael
            )
            display_dialogue_with_sprite(screen,
            "Soudain, la grille s’illumine brièvement et repousse Aldric violemment, le projetant en arrière.(Vie -10)",
            font, clock, sprite_garen
            )
            hero.health -= 10
            display_dialogue_with_sprite(screen,
            "Garen (aidant Aldric) : Tu vas bien ?! Tu n’aurais pas dû...(kael +5, Garen -5)",
            font, clock, sprite_garen
            )
            hero.get_relation("Kael").adjust_score(+5)  # Kael apprécie la témérité
            hero.get_relation("Garen").adjust_score(-5)  # Garen craint votre impulsivité

        else:
            display_dialogue_box(screen,
            "Choix invalide. Aldric reste sur place, indécis.",
            font, clock
        )
    chapitre_2_final_choice(hero, screen, font, clock, sprites)
    # Transition vers l'étage suivant
    background = fade_in_background(screen, "graphics/resources/backgrounds/escalier.webp", WIDTH, HEIGHT)
    display_dialogue_box(screen,
    "Après avoir franchi la porte, vous montez les escaliers menant à l’étage suivant. "
    "Derrière vous, la porte se referme lourdement, comme pour marquer le début d’une nouvelle épreuve.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
        "Kael (jetant un regard à Garen) : Ne te réjouis pas trop vite, paysan. "
        "Ce n’était qu’un test facile. Je doute que la Tour s'arrête là.",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Garen (calme) : Je préfère la simplicité à l’arrogance.",
        font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
        "Aldric (pensif) : Peu importe. Nous avons passé cette épreuve… "
        "mais je doute que celles à venir nous laissent autant de choix.",
        font, clock, sprite_aldric
    )

    display_dialogue_box(screen,
    "La lumière des torches s’amenuise. Les ombres dansantes sur les murs vous tiennent compagnie "
    "tandis que le groupe de participants s’étire. Certains gravissent les marches rapidement, "
    "d’autres hésitent après l’épreuve.",
    font, clock
    )

    # Dialogue après l'épreuve
    display_dialogue_with_sprite(screen,
    "Kael (marchant devant, jetant un regard par-dessus son épaule) : Hah… Je me demande combien sont restés bloqués là-bas. "
    "J’espère pour eux que l’épreuve suivante ne sera pas trop difficile…",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Kael (s'arrêtant brièvement) : Mais en y réfléchissant… peut-être que c’est mieux qu’ils restent en bas. "
    "La Tour ne pardonne pas aux faibles.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Garen (haletant légèrement) : Tu parles comme si c’était une promenade… J’ai cru que cette porte ne s’ouvrirait jamais…",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Kael (souriant) : C’est bien là la différence entre nous. "
    "Pour toi, survivre est un exploit. Pour moi, c’est une évidence.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Aldric (calme) : Si ce genre de test te fait peur, tu n’iras pas loin. C’était juste une mise en bouche.",
    font, clock, sprite_aldric
    )

    display_dialogue_with_sprite(screen,
    "Kael : Exactement. La Tour teste d'abord notre esprit, mais ce n’est qu’un prélude. "
    "Le vrai danger se cache dans ce qui ne peut être vu.",
    font, clock, sprite_kael
    )
    display_dialogue_box(screen,
    "Alors que vous continuez à avancer, un lourd grondement résonne derrière vous. "
    "La porte du premier étage se referme lentement, scellant le passage. "
    "Six participants restent de l'autre côté, certains étendus au sol, morts, immobiles. "
    "D'autres n'ont simplement pas eu le temps ou le courage de traverser.",
    font, clock
    )

    display_dialogue_box(screen,
    "La Tour ne pardonne pas aux faibles. Ceux qui échouent sont laissés derrière, effacés de l'épreuve aussi brutalement "
    "que s'ils n'avaient jamais existé.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Kael (sombre) : Voilà ce que signifie rester en arrière. "
    "Mieux vaut ne jamais ralentir, peu importe le prix.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
    "Garen (baissant les yeux) : Ils savaient à quoi s’attendre… mais ça reste difficile à regarder.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Aldric (calme) : C’est ainsi que la Tour sélectionne. Ce n'est que le début.",
    font, clock, sprite_aldric
    )


# Une ambiance mystérieuse s'installe
    display_dialogue_box(screen,
    "Plus loin dans l'étage 1, un groupe de participants observe Aldric, Kael et Garen poursuivre leur chemin. "
    "Leurs regards sont chargés d’envie… et de crainte.",
    font, clock
    )

    display_dialogue_box(screen,
    "Alors qu’Aldric et son groupe avancent, l’ombre d’un regard perçant se dessine brièvement dans les ténèbres, "
    "puis disparaît. Aucun d’eux ne semble le remarquer.",
    font, clock
    )

    # Description des personnages

    background = fade_in_background(screen,"graphics/resources/backgrounds/ClotaireE.PNG", WIDTH, HEIGHT)
    # Narration initiale
    display_dialogue_box(screen,
    "Derrière eux, Clotaire et son groupe échangent des regards furtifs. "
    "Leur murmure constant forme un bourdonnement à peine audible. "
    "Ils observent les autres participants avec des sourires en coin, comme s'ils en savaient plus qu'ils ne laissaient paraître. "
    "Malgré leur apparente insouciance, une tension subtile se dégage… quelque chose semble rôder sous la surface.",
    font, clock
    )

# Dialogue des personnages
    display_dialogue_with_sprite(screen,
    "Clotaire (voix basse, un sourire narquois) : Bien joué, Emphyr... "
    "T’agenouiller était donc la clef. Tu es plus maligne que tu ne le montres.",
    font, clock, sprite_clotaire
    )

    display_dialogue_with_sprite(screen,
    "Emphyr (haussant les épaules) : Oh, je t’en prie. C’est Velm qui l’a suggéré en plaisantant. "
    "Je me suis dit… pourquoi pas ?",
    font, clock, sprite_emphyr
    )

    display_dialogue_with_sprite(screen,
    "Velm (rire nerveux) : Ahah ! Hé, je ne suis pas si bête, hein ?",
    font, clock, sprite_velm
    )

    display_dialogue_with_sprite(screen,
    "Brandio (froidement) : Si. Tu es bête. On appelle ça la chance, pas l’intelligence.",
    font, clock, sprite_brandio
    )

    display_dialogue_with_sprite(screen,
    "Emphyr (soupirant, regard distant) : C’est bon les gars… Vous fatiguez. "
    "Il y a quelque chose d’étrange dans cette Tour. Je préfère avancer.",
    font, clock, sprite_emphyr
    )

    display_dialogue_with_sprite(screen,
    "Clotaire (calme, un éclat malicieux dans les yeux) : Vous avez entendu la demoiselle. "
    "On ne fait jamais attendre une dame. En avant.",
    font, clock, sprite_clotaire
    )

    display_dialogue_with_sprite(screen,
    "Velm et Brandio (en chœur, moqueurs) : Oui, boss !",
    font, clock, sprite_brandio
    )

# Ajout de tension avec un regard caché
    display_dialogue_box(screen,
    "Alors que Clotaire et son groupe s’éloignent, Aldric ne peut s’empêcher de remarquer quelque chose. "
    "Un bref instant, Clotaire tourne légèrement la tête, croisant votre regard. "
    "Son sourire s’élargit, mais il n'y a aucune chaleur dans ses yeux. "
    "Puis il disparaît dans l’ombre du couloir, laissant derrière lui une sensation étrange.",
    font, clock
    )

    fade_out_music(fade_duration=4000)
    fade_in_text(screen, "Fin du Chapitre 2 - Il reste 93 participants sur 99 et 98 étages", font, (WIDTH // 2, HEIGHT // 2), duration=2000)
    fade_out_text(screen, 1000)

    game_menu(screen, font, clock, WIDTH, HEIGHT, hero)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def chapitre_3(hero, screen, font, clock,sprites):
    
    global background
    
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
    sprite_random_participant = sprites["Participant"]
    
    ayela = Character("Ayela", "graphics/resources/sprites/Ayela.webp", 
                  "Une archère espiègle et maligne.", 
                  "alliée", gender="fille")
    hero.add_relation(ayela, "Neutre")
    
    clotaire = Character(
    "Clotaire", "graphics/resources/sprites/Clotaire.webp", 
    "Un combattant expérimenté, au regard fourbe et prêt à tout pour réussir.", 
    "antagoniste", gender="garçon"
    )

    velm = Character(
    "Velm", "graphics/resources/sprites/Velm.webp", 
    "Un jeune homme rusé et discret, à l'aura mystérieuse.", 
    "antagoniste", gender="garçon"
    )

    brandio = Character(
    "Brandio", "graphics/resources/sprites/Brandio.webp", 
    "Un colosse loyal et protecteur, peu bavard.", 
    "antagoniste", gender="garçon"
    )

    emphyr = Character(
    "Emphyr", "graphics/resources/sprites/Emphyr.webp", 
    "Une espionne séduisante et féline.", 
    "neutre", gender="fille"
    )

# Ajout des relations avec vérification préalable

    hero.add_relation(clotaire, "Neutre")

    hero.add_relation(velm, "Neutre")

    hero.add_relation(brandio, "Neutre")
    
    hero.add_relation(emphyr, "Neutre")
    clear_screen(screen)
    fade_in_music("graphics/resources/music/AmbientElves.mp3", max_volume=0.2, fade_duration=1000)
    fade_in_text(screen, 
             "Chapitre 3 : Mirroir, Mirroir... - Etage 2/99", 
             font, 
             (WIDTH // 2, HEIGHT // 2),  # Centré sur l'écran
             duration=3000)
    fade_out_text(screen, 3000, fade_speed=2)
    pygame.time.wait(1000)
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/porte.webp", WIDTH, HEIGHT)
    
    display_dialogue_box(screen,
        "L'escalier s'étire interminablement, chaque pas résonnant lourdement contre la pierre froide. "
        "L'air devient plus lourd à mesure que vous grimpez, comme si l'étage suivant vous oppressait déjà. "
        "Même Garen, pourtant d'ordinaire bavard, se contente de serrer la poignée de son arme.",
        font, clock
    )

    display_dialogue_box(screen,
        "Un courant d'air glacé descend des marches supérieures, "
        "comme pour vous prévenir de ce qui vous attend.",
        font, clock
    )

    # Salle circulaire
    background = fade_in_background(screen, "graphics/resources/backgrounds/mirroirKnight.webp", WIDTH, HEIGHT)
    display_dialogue_box(screen,
        "Finalement, la volée de marches s'ouvre sur une salle circulaire immense. "
        "Des torches aux murs diffusent une lumière bleutée étrange, projetant des ombres mouvantes. "
        "Le silence est pesant, comme si cet endroit attendait depuis des siècles.",
        font, clock
    )

    display_dialogue_box(screen,
        "Un chevalier d'une taille inhumaine – plus de quatre mètres de haut – se tient immobile, tel une sculpture d'acier. "
        "Son bouclier poli reflète l'image des visiteurs, mais ce n'est pas une simple surface… ",
        font, clock
    )

    # Dialogue des personnages
    display_dialogue_with_sprite(screen,
        "Kael (bras croisés) : C'est quoi ce truc… un colosse qui garde la porte ? "
        "On dirait que la Tour commence à s'amuser. J’ai presque envie de lui demander son nom.",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Garen (visiblement tendu) : Tu crois… qu'il va nous attaquer ? "
        "Je n'aime pas ce silence…",
        font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
        "Aldric (les yeux fixés sur le chevalier) : Pas besoin de croire. Il est là pour ça.",
        font, clock, sprite_aldric
    )

    # Ajout de dialogues supplémentaires
    display_dialogue_with_sprite(screen,
        "Kael (haussant un sourcil) : Super… On doit se battre contre lui ? "
        "Je ne savais pas que la Tour appréciait les jeux de puissance.",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Garen (mal à l'aise) : Il est enorme...mais à plusieurs ca peut le faire non ? Il est tout seul après tout.",
        font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
        "Aldric (calme) : Peu importe. On découvrira la réponse bien assez tôt.",
        font, clock, sprite_aldric
    )

    # Choix interactif - Réaction face au chevalier miroir
    # Phase de choix - Interaction avec le chevalier
    options = [
    ("Observer calmement et analyser le chevalier.", 0),
    ("Provoquer le chevalier à voix haute.", 1),
    ("Ignorer le chevalier et continuer d'avancer prudemment.", 2)
    ]

    # Affiche la boîte de choix
    choix = display_choices_box(screen, font, options, clock)

# Gestion des choix et conséquences
    if choix == 0:  # Observer calmement
        display_dialogue_with_sprite(screen,
        "Aldric (observant) : Il est immobile mais il a l'air conscient...bizarre.",
        font, clock, sprite_aldric
        )
        display_dialogue_with_sprite(screen,
        "Garen (impressionné) : Bonne observation. Ça nous donne peut-être une chance de trouver une faille. (+5 Garen)",
        font, clock, sprite_garen
        )
        hero.get_relation("Garen").adjust_score(+5)

    elif choix == 1:  # Provoquer le chevalier
        display_dialogue_with_sprite(screen,
        "Kael (pointant son épée) : Hé, grand machin ! Qu’est-ce que tu attends pour bouger ?!",
        font, clock, sprite_kael
        )
        display_dialogue_box(screen,
        "Le chevalier ne réagit pas, mais son reflet dans le bouclier semble plus vif, comme s'il répondait à l'agressivité.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Garen (gêné) : Kael… Fais attention. On ne sait pas de quoi il est capable. (+10 Kael, -5 Garen)",
        font, clock, sprite_garen
        )
        hero.get_relation("Kael").adjust_score(+10)
        hero.get_relation("Garen").adjust_score(-5)

    elif choix == 2:  # Ignorer et avancer
        display_dialogue_with_sprite(screen,
        "Aldric (calme) : Il n’attaquera peut-être que si nous faisons un faux pas. Restons prudents.",
        font, clock, sprite_aldric
        )
        display_dialogue_with_sprite(screen,
        "Kael (sarcastique) : On avance alors… J’espère que ce géant de fer n’a pas l’intention de nous suivre.",
        font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
        "Garen (inquiet) : J'ai un mauvais pressentiment… mais d'accord.",
        font, clock, sprite_garen
        )
    else:
        display_dialogue_box(screen,
        "Choix invalide. Aldric reste sur place, indécis.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
            "Kael (sarcastique) : On avance alors… J’espère que ce géant de fer n’a pas l’intention de nous suivre.",
            font, clock, sprite_kael
        )

        display_dialogue_with_sprite(screen,
            "Garen (inquiet) : J'ai un mauvais pressentiment… mais d'accord.",
            font, clock, sprite_garen
        )

    # Suite du scénario
    display_dialogue_box(screen,
        "Le groupe continue d'avancer lentement, laissant derrière eux l’ombre imposante du chevalier miroir… "
        "Mais même immobile, il semble suivre chacun de leurs pas.",
        font, clock
    )
    fade_out_music(fade_duration=1000)
    
    # Arrivée du chevalier et de ses doubles
    display_dialogue_box(screen,
        "Un grincement métallique brise soudain le silence. "
        "Le chevalier à genoux prend lentement vie, ses plaques raclant contre la pierre. "
        "Il se redresse, brandissant son gigantesque bouclier avec une lourdeur sinistre. "
        "Des formes fantomatiques émergent à sa surface… Ce sont des doubles du chevalier, plus petits et moins imposants, "
        "mais suffisamment menaçants.",
        font, clock
    )
    fade_in_music("graphics/resources/music/Abyss.mp3", max_volume=0.2, fade_duration=1000)
    display_dialogue_box(screen,
        "Les doubles quittent la surface du bouclier comme des ombres s’arrachant à un miroir brisé. "
        "Ils marchent d’un pas coordonné, alignés dans une formation parfaite. "
        "Bien qu’ils soient plus petits que l’original, leur acier brille de la même lueur oppressante.",
        font, clock
    )

    # Réactions des personnages
    display_dialogue_with_sprite(screen,
        "Kael (plissant les yeux) : …Génial. Des copies conformes. Et je parie qu'ils frappent aussi fort que nous.",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Garen (prenant une posture défensive) : Tu crois qu’on peut les battre ? "
        "Ce n’est pas juste de simples illusions… On dirait qu'ils nous testent.",
        font, clock, sprite_garen
    )

    display_dialogue_box(screen,
        "Son regard ne quitte pas son reflet dans le bouclier. L’un des doubles lève lentement son épée, "
        "répliquant chacun de ses mouvements, mais avec une précision mécanique et implacable.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Aldric (fixant les doubles) : C’est une épreuve… Mais pas seulement de force.",
        font, clock, sprite_aldric
    )

    # Ajout de tension avant le combat
    display_dialogue_box(screen,
        "L'air s'alourdit encore plus. Chaque respiration devient un poids, chaque pas résonne à travers la salle. "
        "Le combat contre les doubles est imminent, et le moindre faux pas pourrait être fatal.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Kael (un sourire en coin) : Il n’y a qu’une seule façon de le savoir. "
        "Si on s’en débarrasse vite, on pourra éviter d’en affronter d’autres. On frappe en premier ?",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Garen (plus nerveux) : Frapper en premier, c'est bien… Mais on ne sait pas combien d’entre eux vont sortir de ce bouclier. "
        "Peut-être qu’ils se multiplient.",
        font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
        "Aldric (s'approchant légèrement) : Ils ne sont pas invincibles… mais on ne sortira pas indemnes.",
        font, clock, sprite_aldric
    )

    # Choix interactif : Stratégie face au chevalier
    options = [
    ("Frapper immédiatement et tenter de briser la formation ennemie.", 0),
    ("Attendre et observer leurs mouvements.", 1),
    ("Chercher une faiblesse dans leur armure.", 2)
    ]

# Affiche la boîte de choix
    choix = display_choices_box(screen, font, options, clock)

# Gestion des choix et conséquences
    if choix == 0:  # Attaque immédiate
        display_dialogue_with_sprite(screen,
        "Kael (brandissant son épée) : Je savais que tu prendrais la bonne décision. Suivez-moi !",
        font, clock, sprite_kael
        )
        display_dialogue_box(screen,
        "Kael s’élance vers les doubles, son épée brillant sous la lueur des torches. "
        "Les doubles réagissent immédiatement, levant leurs armes dans une synchronisation parfaite.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Garen (fronçant les sourcils) : Tête brûlée… On n'a pas de plan ! (+10 Kael, -5 Garen)",
        font, clock, sprite_garen
        )
        hero.get_relation("Kael").adjust_score(+10)
        hero.get_relation("Garen").adjust_score(-5)

    elif choix == 1:  # Observation stratégique
        display_dialogue_with_sprite(screen,
        "Aldric (calme) : Pas de précipitation. Voyons comment ils réagissent.",
        font, clock, sprite_aldric
        )
        display_dialogue_box(screen,
        "Le groupe reste en retrait, analysant chaque mouvement des doubles. "
        "Ils avancent lentement, suivant un schéma répétitif. Une faille pourrait apparaître.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Garen (soulagé) : C’est mieux comme ça… Frapper à l’aveugle, c’est risqué. (+5 Garen, neutre Kael)",
        font, clock, sprite_garen
        )
        hero.get_relation("Garen").adjust_score(+5)

    elif choix == 2:  # Analyse de faiblesse
        display_dialogue_box(screen,
        "Vous scrutez les moindres détails de leur armure. "
        "Une brèche semble apparaître dans les jointures, là où l’acier s’assemble maladroitement.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Kael (intrigué) : Tu as vu quelque chose ?",
        font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
        "Aldric (désignant la brèche) : Là. On frappe ici. Ça pourrait les déstabiliser. (+5 Garen, +5 Kael)",
        font, clock, sprite_aldric
        )
        hero.get_relation("Kael").adjust_score(+5)
        hero.get_relation("Garen").adjust_score(+5)
    else:
        display_dialogue_box(screen,
        "Choix invalide. Aldric reste en garde, observant la situation sans agir.",
        font, clock
    )

    # Transition vers la phase de combat
    display_dialogue_box(screen,
        "Les doubles avancent lentement, leurs épées prêtes. Le combat est inévitable.",
        font, clock
    )


    display_dialogue_box(screen,
        "Alors que le chevalier avance de quelques pas, les doubles bondissent en avant, fondant sur les participants. "
        "Les premières lames s'entrechoquent dans une cacophonie d'acier et de cris. "
        "Certains attaquent directement le colosse, mais leurs coups rebondissent sans laisser la moindre égratignure.",
        font, clock
    )

    display_dialogue_box(screen,
        "Au cœur de la mêlée, une silhouette fluide se distingue des autres. "
        "Avec une aisance féline, celui qui jonglait avec ses dagues plus tôt glisse entre les clones, évitant chaque coup d’un simple mouvement du buste ou d’un saut agile. "
        "Ses dagues dansent dans ses mains, frappant les doubles un à un, qui s’effondrent sans bruit, leurs formes disparaissant comme des ombres dissipées par la lumière.",
        font, clock
    )

    display_dialogue_box(screen,
        "Plus loin, le vieux mage élève son bâton, traçant dans l’air des cercles lumineux. "
        "Une brève incantation résonne, et soudain, des éclats de lumière jaillissent, aveuglant temporairement les doubles. "
        "Derrière cette barrière éphémère, plusieurs participants profitent de l’ouverture pour abattre les clones désorientés.",
        font, clock
    )

    display_dialogue_box(screen,
        "Les deux jumeaux avec leur tenue tribale se placent dos à dos. "
        "L’un tend la main vers le sol, et une masse sombre se matérialise sous forme d’un loup de pierre, bondissant sur les doubles. "
        "Sa sœur frappe dans ses mains, invoquant une volée d’oiseaux de vent qui lacèrent les adversaires du haut des airs. "
        "Le duo combat en parfaite synchronisation, comme s’ils partageaient le même souffle.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Kael (frappant du pied avec frustration) : Rien ne passe ! Qu'est-ce que c'est que ce foutu truc ?!",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Garen (haletant, après avoir paré une attaque) : On va se faire massacrer si on continue comme ça…",
        font, clock, sprite_garen
    )

    display_dialogue_box(screen,
        "Les doubles se multiplient, encerclant les participants. "
        "Aldric se tient dos à dos avec Kael et Garen, leurs armes levées. "
        "Autour d'eux, les cris de ceux qui tombent sous les lames des reflets se mêlent aux bruits sourds des coups portés sur l’armure du chevalier. "
        "Il semble inébranlable, et ses doubles se battent avec une coordination parfaite, comme un funeste ballet orchestré dans l'ombre.",
        font, clock
    )

    display_dialogue_box(screen,
        "Un silence pesant s'installe pendant une fraction de seconde, seulement brisé par le bruit métallique des doubles qui avancent. "
        "Soudain, une flèche fend l'air avec une précision chirurgicale, transperçant l'un des reflets qui s'effondre dans un éclat d'énergie vaporeuse.",
        font, clock
    )
    
    display_dialogue_box(screen,
        "Vous suivez la trajectoire de la flèche et apercevez une femme archère perchée sur une colonne brisée, "
        "son arc toujours tendu. Elle scrute le terrain de bataille avec calme, détachée du chaos environnant.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "??? (calme, abaissant légèrement son arc) : Si vous continuez à frapper comme des brutes, vous allez tous mourir.",
        font, clock, sprite_ayela
    )

    display_dialogue_with_sprite(screen,
        "Ayela (esquissant un léger sourire) : Je suis Ayela, mais on fera les présentations plus tard. On a plus urgent.",
        font, clock, sprite_ayela
    )
    background = fade_in_background(screen, "graphics/resources/backgrounds/mirrorfight.webp", WIDTH, HEIGHT)
    display_dialogue_box(screen,
        "Ayela était une jeune archère à la silhouette athlétique et élancée, sa peau claire parsemée de taches de rousseur discrètes."
        "L’arc qu’elle tenait était finement sculpté, décoré de motifs elfiques, trahissant une certaine élégance malgré sa robustesse."
        "Chaque mouvement d'Ayela semblait mesuré, précis, comme si elle dansait avec le danger.",
        font, clock
    )

    display_dialogue_box(screen,
        "Sa voix, bien que posée, résonne comme une mise en garde glaciale. "
        "Derrière son air serein, vous devinez une combattante habituée à survivre dans des situations désespérées.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Kael (esquissant un sourire tout en esquivant une attaque) : Hah… Voilà qui devient intéressant. "
        "J’aime quand quelqu’un d’autre fait le sale boulot.",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Garen (haletant, relevant son bouclier) : Elle a réussi à en abattre un… Mais comment ?!",
        font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
        "Ayela (préparant une autre flèche) : Vous vous obstinez à frapper l’armure. Visez les reflets dans le bouclier… "
        "C’est là qu’ils naissent.",
        font, clock, sprite_ayela
    )

    display_dialogue_box(screen,
        "À ces mots, une nouvelle salve part et frappe un autre double en plein cœur, le réduisant en cendres. "
        "Kael échange un regard rapide avec Aldric, hochant la tête avec un rictus satisfait.",
        font, clock
    )
    
    display_dialogue_with_sprite(screen,
        "Kael : Eh bien, au moins l’un de nous réfléchit. C’est bon à savoir. Je commençais à désespérer de notre équipe d'infortune.",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Aldric : Tu devrais plutôt te concentrer Kael, ou tu risques d’être le prochain a terre.",
        font, clock, sprite_aldric
    )

    display_dialogue_with_sprite(screen,
        "Ayela (tirant une flèche supplémentaire sans même détourner le regard, elle se dit à elle meme) : Il pourrait s’avérer utile… s’il survit assez longtemps.",
        font, clock, sprite_ayela
    )

    display_dialogue_box(screen,
        "Kael éclate de rire, mais il s’interrompt immédiatement en esquivant de justesse une attaque venant d’un double. "
        "L’expression moqueuse laisse place à une grimace déterminée. "
        "Le combat ne fait que commencer, et la salle semble vibrer sous l’intensité des affrontements.",
        font, clock
    )
    
    display_dialogue_with_sprite(screen,
        "Ayela (s'approchant) : Écoutez. Son point faible, c'est lui-même. "
        "Il faut lui renvoyer un coup en utilisant ses doubles. J'ai... juste besoin d'un angle... j'ai besoin de vous hihi,",
        font, clock, sprite_ayela
    )

    display_dialogue_with_sprite(screen,
        "Ayela (léger sourire gêné) : Je peux envoyer une flèche enchantée, mais vous devrez me couvrir et trouver le bon angle.",
        font, clock, sprite_ayela
    )

    options = [
    ("Aider Ayela à viser.", 0),
    ("Tenter une attaque frontale avec Kael.", 1),
    ("Protéger Garen et les autres participants.", 2)
    ]

    # Affiche la boîte de choix
    choix = display_choices_box(screen, font, options, clock)

# Gestion des choix et conséquences
    if choix == 0:  # Aider Ayela
        display_dialogue_box(screen,
        "Vous vous placez aux côtés d'Ayela, vos yeux suivant la trajectoire des créatures. "
        "D'un geste rapide, vous pointez une faille dans l'illusion du bouclier.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Aldric (calme) : Là. Tire juste à cet angle.",
        font, clock, sprite_aldric
        )
        display_dialogue_box(screen,
        "Ayela hoche la tête, retenant son souffle alors que la corde de son arc se tend. "
        "Sa flèche fuse comme un éclair argenté et frappe le bouclier du chevalier. "
        "Une lumière éclate, déchirant l'ombre et projetant une onde qui fait reculer l’adversaire.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Kael (impressionné) : Ça fonctionne ! Refais-le encore, rend toi utile !",
        font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
        "Ayela (sourire léger) : Tant qu’ils n'esquivent pas mes flèches, ça ira.",
        font, clock, sprite_ayela
        )
        display_dialogue_with_sprite(screen,
        "Garen (souriant nerveusement) : Rappelle-moi de toujours écouter Ayela.",
        font, clock, sprite_garen
        )
        hero.get_relation("Kael").adjust_score(+5)
        hero.get_relation("Ayela").adjust_score(+5)

    elif choix == 1:  # Attaque frontale avec Kael
        display_dialogue_box(screen,
        "Vous suivez Kael dans une attaque frontale, vos lames scintillant sous les torches. "
        "Avec un cri, vous vous précipitez pour attaquer le chevalier. Mais vos coups rebondissent sur son armure.",
        font, clock
        )
        display_dialogue_box(screen,
        "Kael jure tandis qu’un double émerge du reflet du bouclier. "
        "Il frappe Kael, laissant une plaie visible alors que Kael s'effondre.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Kael (grimaçant) : Bordel… Je crois qu’il n’aime pas qu’on joue de trop près… (-10 Kael)",
        font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
        "Garen (horrifié) : Kael ! Ça va ?",
        font, clock, sprite_garen
        )
        display_dialogue_with_sprite(screen,
        "Ayela (froide) : Évitez de mourir bêtement.",
        font, clock, sprite_ayela
        )
        hero.get_relation("Kael").adjust_score(-10)

    elif choix == 2:  # Protéger Garen
        display_dialogue_box(screen,
        "Vous écartez Garen de justesse alors qu'un double s'élance vers lui. "
        "Ayela bande son arc rapidement, mais sa flèche vous frôle, laissant une coupure sur votre bras.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Ayela (agacée) : Je vous ai dit de ne pas bouger !",
        font, clock, sprite_ayela
        )
        display_dialogue_with_sprite(screen,
        "Aldric (grimaçant) : Et moi je t'ai dit de viser correctement…",
        font, clock, sprite_aldric
        )
        display_dialogue_box(screen,
        "Garen, figé par la peur, recule en tenant son épée. "
        "Les doubles l'encerclent lentement.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Kael : Si tu continues à crier, ils vont tous te tomber dessus… Calme-toi  (-12 PV)!",
        font, clock, sprite_kael
        )
        hero.adjust_health(-12)

    else:
        display_dialogue_box(screen,
        "Choix invalide. Réessayez.",
        font, clock
        )
    # Nouvelle phase de combat avant la conclusion
        display_dialogue_box(screen,
        "Le chevalier vacille un instant sous le poids des assauts répétés, mais quelque chose change. "
        "Des éclats de lumière noire s'élèvent de son armure fissurée, et son bouclier projette une onde d’énergie, "
        "repoussant violemment tous ceux qui s'approchaient trop près.",
        font, clock
        )

        display_dialogue_with_sprite(screen,
        "Kael (se redressant) : Tch… Il ne tombe pas aussi facilement. Je suppose qu’on doit continuer à danser ?",
        font, clock, sprite_kael
        )

        display_dialogue_with_sprite(screen,
        "Garen (haletant) : Je ne sais pas combien de temps on tiendra… Il devient plus rapide !",
        font, clock, sprite_garen
        )

        display_dialogue_with_sprite(screen,
        "Ayela (arc bandé) : Restez en arrière ! Si vous le tenez occupé, je peux viser son point faible. "
        "Il y a une ouverture entre les jointures de son plastron.",
        font, clock, sprite_ayela
        )
    background = fade_in_background(screen, "graphics/resources/backgrounds/mirrorfight3.webp", WIDTH, HEIGHT)

    # Interaction rapide - Choix stratégique
    # Phase de choix - Combat contre le chevalier
    options = [
    ("Créer une diversion en attaquant frontalement.", 0),
    ("Protéger Ayela pendant qu'elle vise.", 1),
    ("Reculer et chercher une faille dans l’armure.", 2)
    ]

# Affiche la boîte de choix
    choix = display_choices_box(screen, font, options, clock)

# Gestion des choix et conséquences
    if choix == 0:  # Attaque frontale
        display_dialogue_with_sprite(screen,
        "Kael (chargeant) : J’aime cette stratégie. Simple et direct !",
        font, clock, sprite_kael
        )
        display_dialogue_box(screen,
        "Kael se précipite vers le chevalier, frappant de toutes ses forces. L’impact fait vaciller l’adversaire, "
        "mais la contre-attaque est brutale. Kael parvient à l'éviter de justesse, mais Aldric est projeté en arrière.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Aldric (se relevant lentement) : …Je m’en souviendrai. La prochaine fois, préviens avant de charger. (+10 Kael, -5 PV)",
        font, clock, sprite_aldric
        )
        hero.get_relation("Kael").adjust_score(+10)
        hero.adjust_health(-5)

    elif choix == 1:  # Protection d’Ayela
        display_dialogue_with_sprite(screen,
        "Garen (se plaçant devant Ayela) : Tiens bon, Ayela. Je couvre tes arrières.",
        font, clock, sprite_garen
        )
        display_dialogue_box(screen,
        "Vous levez votre arme juste à temps pour dévier l’attaque d’un des doubles du chevalier. "
        "Ayela s'agenouille et bande son arc, gardant un œil attentif sur la moindre ouverture.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Ayela (prête à tirer) : Continuez comme ça… Encore un peu. (+10 Ayela, +5 Garen)",
        font, clock, sprite_ayela
        )
        hero.get_relation("Ayela").adjust_score(+10)
        hero.get_relation("Garen").adjust_score(+5)

    elif choix == 2:  # Recherche d’une faille
        display_dialogue_box(screen,
        "Vous reculez lentement, scrutant chaque mouvement du chevalier. "
        "Une lumière vacille légèrement sous son oeil droit… un point faible ?",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Aldric (désignant la faille) : Là. Ayela, visez ce point précis !",
        font, clock, sprite_aldric
        )
        display_dialogue_with_sprite(screen,
        "Ayela (hochant la tête) : Compris.",
        font, clock, sprite_ayela
        )

    else:
        display_dialogue_box(screen,
        "Choix invalide. Aldric hésite un instant, laissant le temps à l'ennemi d'avancer davantage.",
        font, clock
        )


    # Passage à la conclusion
    display_dialogue_box(screen,
        "Finalement, la dernière flèche d'Ayela frappe le chevalier. "
        "L'armure s'effondre, et son bouclier se brise en éclats de lumière.",
        font, clock
    )
    fade_out_music(fade_duration=1000)
    
    display_dialogue_box(screen,
        "Sur les 99 participants initiaux, seuls 72 restent debout… La tour, impitoyable, commençait déjà son tri.",
        font, clock
    )
    fade_in_music("graphics/resources/music/AmbientElves.mp3", max_volume=0.2, fade_duration=1000)
    background = fade_in_background(screen,"graphics/resources/backgrounds/porteetage2.webp", WIDTH, HEIGHT)
    # Dialogue après combat - Kael
    display_dialogue_with_sprite(screen,
        "Kael (essuyant sa lame) : Je déteste admettre ça, mais… bien joué. Tu sers à quelque chose après tout…",
        font, clock, sprite_kael
    )

    display_dialogue_box(screen,
        "Son regard se détourne rapidement, comme pour masquer une pointe de respect.",
        font, clock
    )
    
    # Garen soulagé
    display_dialogue_with_sprite(screen,
        "Garen (s'écroulant au sol, haletant) : On est vivant... c'est tout ce qui compte. J'en ai eu deux ! J'en ai eu deux... je... je crois...",
        font, clock, sprite_garen
    )
    
    display_dialogue_box(screen,
        "Un rire nerveux s'échappe alors qu'il regarde ses mains trembler.",
        font, clock
    )
    
    # Aldric remet les pendules à l'heure
    display_dialogue_with_sprite(screen,
        "Aldric (croisant les bras) : Ne crie pas victoire trop vite. Ce n'était que le deuxieme étages...regarde tout ceux qui sont deja tombés, je te l'avais dit",
        font, clock, sprite_aldric
    )
    
    display_dialogue_with_sprite(screen,
        "Garen (Baissant la tête) : Que la plupart tomberont au cours des deux, trois premiers étages... ",
        font, clock, sprite_garen
    )

    display_dialogue_box(screen,
        "Il fixe la porte du troisième étage qui s'entrouvre lentement devant eux, laissant apparaître l'escalier sinueux.",
        font, clock
    )

    # Kael taquine Garen
    display_dialogue_with_sprite(screen,
        "Kael (tapant dans le dos de Garen) : T’as survécu… Pour l’instant. Mais vu ton état, t’as l’air prêt à t’effondrer, paysan. "
        "T’as encore du chemin à faire avant de ressembler à un combattant…",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Garen (soufflant, mais souriant faiblement) : Ouais… ouais… Je vais m’améliorer, promis. Merci… à vous deux.",
        font, clock, sprite_garen
    )

    # Ayela s'impose dans l'équipe
    display_dialogue_with_sprite(screen,
        "Ayela (s'approchant d'Aldric, sourire en coin) : Tu n'es pas comme les autres. Ce regard… Je l'ai déjà vu. "
        "Tu sais ce que tu fais… Et j'aime ça. Tu n'as pas le choix ! Faisons équipe.",
        font, clock, sprite_ayela
    )

    display_dialogue_box(screen,
        "Elle lui fait un clin d'œil avant de se placer à ses côtés. (Ayela +5)",
        font, clock
    )

    hero.get_relation("Ayela").adjust_score(+5)

    # Présentation de Garen
    display_dialogue_with_sprite(screen,
        "Garen (timidement) : Je suis Garen. Enchanté, Ayela. Lui, c'est Aldric… Et le gars là-bas qui se prend pour un prince, c'est Kael.",
        font, clock, sprite_garen
    )

    # Kael répond à sa manière
    display_dialogue_with_sprite(screen,
        "Kael (plissant les yeux) : Essaye de ne pas postillonner quand tu parles de moi, paysan. Je suis Kael. "
        "Et évite de me toucher, ça vaut mieux pour toi…",
        font, clock, sprite_kael
    )

    # Ayela rétorque avec humour
    display_dialogue_with_sprite(screen,
        "Ayela (ricanant) : Oh, toi t’es du genre « monsieur parfait ». Tu devrais redescendre un peu…",
        font, clock, sprite_ayela
    )

    # Kael fier de lui
    display_dialogue_with_sprite(screen,
        "Kael (avec fierté) : Ce n’est pas de l’arrogance… Juste un constat. Je suis raffiné, vous trois… disons… moins.",
        font, clock, sprite_kael
    )
    
    display_dialogue_with_sprite(screen,
        "Garen (boueux et fatigué) : Raffiné, hein ? Avec un peu de boue tu le serai moins !",
        font, clock, sprite_garen
    )

    # Kael réplique
    display_dialogue_with_sprite(screen,
        "Kael (dégaine lentement son épée, sourire provocateur) : Oh de la provocation hmmm ? Tu veux croiser le fer maintenant ? "
        "Fais attention, tu trembles encore. Ne va pas te pisser dessus..",
        font, clock, sprite_kael
    )

    # Aldric intervient pour calmer le jeu
    display_dialogue_box(screen,
        "Alors que les deux jeunes hommes s’apprêtent à se battre, Aldric fait un pas entre eux et bloque leurs lames avec la sienne.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Aldric (calme, mais ferme) : Ça suffit. Si vous voulez mourir, attendez l'étage suivant. "
        "Mais arrêtez ces gamineries. J'ai pas de temps à perdre avec ça.",
        font, clock, sprite_aldric
    )

    # Ayela commente avec amusement
    display_dialogue_with_sprite(screen,
        "Ayela (amusée, mains sur les hanches) : Le beau gosse ténébreux a raison. "
        "Se battre ici ne servira à rien. Gardez votre énergie… La tour nous attend.",
        font, clock, sprite_ayela
    )

    # Narration - tension persistante
    display_dialogue_box(screen,
        "Kael et Garen rangent leurs lames, mais l'animosité demeure palpable. "
        "Chacun garde une certaine distance alors que le groupe s’avance en direction de la porte suivante.",
        font, clock
    )

    # Narration - pilleurs et hésitants
    display_dialogue_box(screen,
        "Les participants se dirigent vers la prochaine épreuve, mais certains restent en arrière… "
        "Quelques-uns commencent à piller des morceaux du chevalier défait, croyant y trouver des reliques précieuses. "
        "D’autres, encore tremblants, s'assoient et réfléchissent à abandonner.",
        font, clock
    )

    # Apparition de la silhouette mystérieuse
    display_dialogue_box(screen,
        "Alors qu’Aldric, Ayela, Kael et Garen s’éloignent, une silhouette encapuchonnée apparaît brièvement en haut d'une rembarde.. "
        "L’homme mystérieux qui avait salué Aldric les observe silencieusement, avant de disparaître dans l’ombre.",
        font, clock
    )

    # Fermeture de la porte du deuxième étage
    

    # Interaction avec Clotaire
    display_dialogue_box(screen,
    "Vous remarquez un groupe d'individus suspects près de la grille qui vous toise.",
    font, clock
    )
    

# Clotaire fait trébucher Garen
    display_dialogue_box(screen,
    "Alors que la porte commence à se refermer lentement, Garen s'élance pour la franchir… "
    "Mais au dernier moment, l'un des hommes du groupe – un sourire narquois aux lèvres – "
    "tend discrètement la jambe, faisant trébucher Garen.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Garen (paniqué) : Aldric !",
    font, clock, sprite_garen
    )
    
# Aldric intervient
    display_dialogue_box(screen,
    "Sans hésiter, Aldric attrape la main de Garen et tire de toutes ses forces. "
    "Dans un bruit sourd, Garen roule sous la porte qui se referme violemment derrière lui. "
    "Un souffle de poussière s'élève alors que le mécanisme scelle l'entrée.",
    font, clock
    )
    display_dialogue_box(screen,
        "Derrière eux, la porte du deuxième étage se referme, et les derniers bruits des pilleurs résonnent…d'un coup le chevalier-mirroir se reforme.. ",
        font, clock
    )

    display_dialogue_box(screen,
        "Leurs cris s’élèvent alors, tambourinant contre la pierre froide. Jusqu'à ce qu'ils comprennent que la porte ne s’ouvrira plus.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
    "Kael (secouant la tête) : Tch… On dirait que certains aiment jouer aux imbéciles.",
    font, clock, sprite_kael
    )

# Aldric fait face à Clotaire
    display_dialogue_with_sprite(screen,
    "Aldric (calme mais tranchant) : Je te conseille de faire attention la prochaine fois. "
    "Ce serait dommage… que ta tête vole par accident.",
    font, clock, sprite_aldric
    )

    display_dialogue_with_sprite(screen,
    "Clotaire (souriant) : Oh ? Je vois… C'est ce genre de personne que tu es. "
    "Mais je te rassure, je suis très attentif… Toujours.",
    font, clock, sprite_clotaire
    )

    display_dialogue_box(screen,
    "Garen se redresse lentement, époussetant ses vêtements, visiblement secoué mais indemne.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Garen (à voix basse) : Merci… Une seconde de plus et...",
    font, clock, sprite_garen
    )

    # Clotaire fait une remarque provocante
    display_dialogue_with_sprite(screen,
    "Clotaire : C'est pas de ma faute si le gamin a des bottes trop grandes ahah ! La tour est ancienne...On peut...Vite trébucher...Tu vois ?",
    font, clock, sprite_clotaire
    )

    display_dialogue_with_sprite(screen,
    "Aldric (froid) : Hm..",
    font, clock, sprite_aldric
    )


    background = fade_in_background(screen,"graphics/resources/backgrounds/escalier.PNG", WIDTH, HEIGHT)
    # Présentation des choix de réponse
    options = [
    ("« J'ai aussi remarqué que tu nous espionnais.." 
     "Si tu deviens une menace, je te tue. »", 0),
    ("« Ils ont raison. Garen, tes bottes sont trop grandes...", 1),
    ("« On n’a pas besoin de s’attarder. Venez, on continue. »", 2)
    ]

# Affiche la boîte de choix
    choix = display_choices_box(screen, font, options, clock)

# Gestion des choix et conséquences
    if choix == 0:  # Choix de provocation directe
        display_dialogue_with_sprite(screen,
        "Kael (approuvant) : Enfin quelqu’un qui parle. C’est pas trop tôt.",
        font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
        "Garen (hoche la tête, soulagé) : C’est bien… Il faut leur montrer qu’on n’est pas des proies faciles.",
        font, clock, sprite_garen
        )
        display_dialogue_with_sprite(screen,
        "Clotaire (plissant les yeux) : Oh ? Menace-moi encore, blondinet.. J’adore ça. (+10 Kael, +5 Garen, -10 Clotaire)",
        font, clock, sprite_clotaire
        )
        hero.get_relation("Kael").adjust_score(+10)
        hero.get_relation("Garen").adjust_score(+5)
        hero.get_relation("Clotaire").adjust_score(-10)

    elif choix == 1:  # Moquerie envers Garen
        display_dialogue_with_sprite(screen,
        "Clotaire (souriant) : Ahahahah il a de l'humour ! J'aime ça ! Vous avez entendu les gars ? Ahahah je me marre !",
        font, clock, sprite_clotaire
        )
        display_dialogue_with_sprite(screen,
        "Garen (déçu) : Aldric… Tu penses vraiment ça ?",
        font, clock, sprite_garen
        )
        display_dialogue_with_sprite(screen,
        "Ayela (froide) : C’est une façon de voir les choses… mais ne t’attends pas à ce que je cautionne ça.",
        font, clock, sprite_ayela
        )
        display_dialogue_with_sprite(screen,
        "Kael (soupire) : Garen… il a pas tort… (+10 Clotaire, -10 Garen, -5 Ayela, -5 Kael)",
        font, clock, sprite_kael
        )
        hero.get_relation("Clotaire").adjust_score(+10)
        hero.get_relation("Garen").adjust_score(-10)
        hero.get_relation("Ayela").adjust_score(-5)
        hero.get_relation("Kael").adjust_score(-5)

    elif choix == 2:  # Choix pacifique
        display_dialogue_with_sprite(screen,
        "Ayela (hoche la tête) : Tu as raison. Ils ne valent pas notre temps.",
        font, clock, sprite_ayela
        )
        display_dialogue_with_sprite(screen,
        "Garen (souriant) : Ouais… Il vaut mieux ne pas les provoquer inutilement.",
        font, clock, sprite_garen
        )
        display_dialogue_with_sprite(screen,
        "Clotaire (amusé) : Hah, regarde-les fuir. Classique. (renifle) Vous sentez ça ? Ça sent la mort… (+5 Ayela, +5 Garen)",
        font, clock, sprite_clotaire
        )
        hero.get_relation("Ayela").adjust_score(+5)
        hero.get_relation("Garen").adjust_score(+5)

    else:
        display_dialogue_box(screen,
        "Choix invalide. Aldric ne répond pas et continue son chemin en silence.",
        font, clock
        )

    background = fade_in_background(screen,"graphics/resources/backgrounds/Clotaire2.PNG", WIDTH, HEIGHT)
    # Clotaire et sa bande discutent après le départ d'Aldric
    display_dialogue_box(screen,
        "Une fois la bande d'Aldric partie, la bande de Clotaire discute entre elle.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Clotaire : Cette bande de joyeux lurons n’est pas si mauvaise. Je propose qu'on les laisse agir…",
        font, clock, sprite_clotaire
    )

    display_dialogue_with_sprite(screen,
        "Emphyr : Je suis du même avis. Pourquoi mettre nos propres vies en jeu alors qu'ils le font pour nous…",
        font, clock, sprite_emphyr
    )

    display_dialogue_with_sprite(screen,
        "Velm : Bien vu !",
        font, clock, sprite_velm
    )

    display_dialogue_with_sprite(screen,
        "Brandio : On a qu'à attendre derrière eux !",
        font, clock, sprite_brandio
    )

    display_dialogue_with_sprite(screen,
        "Emphyr (prévoyant) : Attention toutefois ! Ça a marché pour cet étage… mais rien ne dit que ça le sera pour les autres !",
        font, clock, sprite_emphyr
    )

    display_dialogue_with_sprite(screen,
        "Clotaire : Emphyr a raison. Tâchons juste d'adopter leur stratégie.",
        font, clock, sprite_clotaire
    )

    display_dialogue_with_sprite(screen,
        "Velm et Brandio : Compris boss !!!",
        font, clock, sprite_brandio
    )
    

    fade_out_music(fade_duration=4000)
    fade_in_text(screen, "Fin du Chapitre 3 - Il reste 67 participants sur 99 et 97 étages", font, (WIDTH // 2, HEIGHT // 2), duration=2000)
    fade_out_text(screen, 1000)
    game_menu(screen, font, clock, WIDTH, HEIGHT, hero)

def chapitre_4(hero, screen, font, clock,sprites):
    
    global background
    
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
    sprite_random_participant = sprites["Participant"]
    sprite_creature = sprites["Creature"]
    
    fade_in_music("graphics/resources/music/Fates.mp3", max_volume=0.2, fade_duration=1000)
    clear_screen(screen)
    fade_in_text(screen, 
             "Chapitre 4 : Lumière noire - Etage 3/99", 
             font, 
             (WIDTH // 2, HEIGHT // 2),  # Centré sur l'écran
             duration=3000)
    fade_out_text(screen, 3000, fade_speed=2)
    pygame.time.wait(1000)
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/etage4a.webp", WIDTH, HEIGHT)
    
    display_dialogue_box(screen,
        "L’ascension vers le troisième étage se fait dans un silence oppressant. "
        "Les marches semblent s’étirer plus que nécessaire, comme si la tour elle-même cherchait à vous retenir. "
        "Le moindre bruit semble résonner plus fort qu'il ne devrait. Le simple battement de votre cœur devient assourdissant.",
        font, clock
    )

    display_dialogue_box(screen,
        "Enfin, la porte s’ouvre lentement sur une vaste salle sombre. "
        "Un frisson glacé vous parcourt l’échine au moment où vous franchissez le seuil. "
        "L’air est glacial, et une brume noire s’enroule autour de vos chevilles, "
        "rampant tel un serpent silencieux. La sensation est étrange, comme si cette brume cherchait à s’accrocher à vous… "
        "Le plafond disparaît dans une obscurité insondable, et seuls quelques piliers brisés se dressent çà et là, "
        "comme les vestiges d’un temple oublié, témoin silencieux d’un passé depuis longtemps effacé.",
        font, clock
    )

    display_dialogue_box(screen,
        "Des voix s’élèvent doucement dans l’air. Des murmures. Incompréhensibles, mais omniprésents. "
        "C’est comme si la salle entière chuchotait des secrets que vous n’étiez pas censé entendre. "
        "À la lueur d’une faible torche, des silhouettes apparaissent lentement dans la pénombre… "
        "Des créatures fines et décharnées, vêtues de robes en lambeaux, "
        "tenant des lanternes irradiant une lumière noire, une lumière qui semble absorber plutôt qu’éclairer.",
        font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/salle4a.webp", WIDTH, HEIGHT)

    display_dialogue_box(screen,
        "Les créatures flottent plus qu’elles ne marchent, glissant silencieusement entre les piliers comme des ombres arrachées à un autre monde. "
        "Elles semblent appartenir à cet endroit, leur existence même fondue dans la tour. "
        "Leurs visages sont cachés sous des capuches déchirées. "
        "Elles n’ont pas d’yeux… mais elles écoutent. Chaque souffle trop fort, chaque pas imprudent pourrait attirer leur attention.",
        font, clock
    )

    display_dialogue_box(screen,
        "L'homme aux dagues et aux mouvements félins se glisse dans l’obscurité. "
        "Ses dagues brillent faiblement sous la lumière vacillante des torches. "
        "Avec une précision chirurgicale, il tranche l’une des créatures d’un geste rapide. "
        "Mais au moment où elle vacille, la lanterne noire qu’elle porte s’illumine, projetant un faisceau de lumière spectrale droit sur lui. "
        "D’un bond, il disparaît dans l’ombre d’un pilier voisin, évitant de justesse l’éclat mortel. "
        "Son regard perçant scrute l’obscurité, calculant chaque mouvement.",
        font, clock
    )

    display_dialogue_box(screen,
        "Non loin, un éclat bleu se dessine à travers les ténèbres. "
        "Un vieil homme au manteau usé plante fermement son bâton dans le sol, traçant des symboles lumineux dans les airs. "
        "Une onde de lumière irradie doucement autour de lui, forçant les créatures à reculer un bref instant. "
        "Ses lèvres murmurent des incantations anciennes, et chaque créature approchant trop près est frappée d’une lueur aveuglante, "
        "lui laissant le temps de réajuster sa position avec un calme implacable.",
        font, clock
    )
    
    display_dialogue_box(screen,
        "Dos à dos, les jumeaux invoqueurs agissent avec une synchronisation parfaite. "
        "L’un d’eux élève les bras,prend la forme d’un oiseau de feu, fondant sur les créatures dans un tourbillon ardent. "
        "De l’autre côté, sa sœur convoque un poisson spectral qui surgit des ombres."
        "Les invocations se déchaînent autour d’eux, créant un cercle de protection redoutable. "
        "Malgré leur talent, chaque invocation arrachée au néant semble leur coûter en énergie,",
        font, clock
    )

    display_dialogue_box(screen,
        "Un des murmures s’amplifie soudain, devenant presque perceptible à l’oreille, comme un soupir à la limite du langage. "
        "La lumière des lanternes noires semble pulser au rythme de ce murmure grandissant, comme un avertissement.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Kael (murmure, les yeux fixés sur les créatures) : C’est quoi ces choses ?... Aldric avait raison, ça va empirer…",
        font, clock, sprite_kael
    )

    display_dialogue_box(screen,
        "Kael se déplace lentement, ses doigts effleurant la garde de sa rapière, "
        "comme s'il s'attendait à devoir se défendre à tout moment, bien qu’il sache probablement que l’acier n’y changerait rien.",
        font, clock
    )
    options = [
    ("Observer attentivement les ombres pour y trouver un indice.", 0),
    ("Avancer prudemment vers les lanternes pour comprendre leur rôle.", 1),
    ("Rester sur place et analyser le comportement des créatures.", 2)
    ]

    choix = display_choices_box(screen, font, options, clock)

# Résolution des choix
    if choix == 0:
        display_dialogue_box(screen,
        "Vous fixez intensément les ombres mouvantes. Pendant un bref instant, "
        "vous apercevez une forme humanoïde indistincte se faufiler dans l’obscurité. "
        "Un frisson glacé parcourt votre échine alors qu’elle disparaît presque aussitôt.",
        font, clock
    )
        display_dialogue_with_sprite(screen,
        "Aldric : Ce n’est pas seulement une épreuve physique… Ces ombres sont vivantes. Restez sur vos gardes.",
        font, clock, sprite_aldric
    )
        hero.get_relation("Kael").adjust_score(+5)  # Kael apprécie votre perspicacité

    elif choix == 1:
        display_dialogue_box(screen,
        "Vous vous approchez prudemment des lanternes. Leur lumière semble vaciller étrangement lorsque vous les fixez de trop près. "
        "En observant attentivement, vous remarquez des symboles gravés à leur base, presque effacés.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Kael : Ces symboles… Ils ressemblent à ceux des stèles. Peut-être que la lumière cache quelque chose.",
        font, clock, sprite_kael
        )
        display_dialogue_box(screen,
        "Vous touchez un des symboles, et un murmure plus fort s'élève dans l’air. "
        "La lumière pulse brièvement avant de revenir à la normale.(Garen +5)",
        font, clock
        )
        hero.get_relation("Garen").adjust_score(+5)  # Garen admire votre courage

    elif choix == 2:
        display_dialogue_box(screen,
        "Vous restez immobile, observant les créatures. Elles semblent réagir au rythme des murmures, "
        "leurs mouvements saccadés devenant plus précis à chaque pulsation de lumière.",
        font, clock
        )
        display_dialogue_with_sprite(screen,
        "Garen (murmure) : Elles bougent… au même rythme que la lumière… C’est comme si elles étaient synchronisées.",
        font, clock, sprite_garen
        )
        display_dialogue_box(screen,
        "Vous réalisez que leurs déplacements suivent un schéma précis, et qu'il est possible de prévoir leur prochain mouvement.(Kael +5)",
        font, clock
        )
        hero.get_relation("Kael").adjust_score(+5)  # Kael admire votre calme et analyse

# Transition après les choix
    display_dialogue_box(screen,
        "Le groupe reste silencieux, chacun digérant ce qu’il a observé. "
        "Les murmures s'atténuent légèrement, mais l’impression d’être surveillé persiste.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Garen (la gorge nouée) : Ce sont… des démons ? On ne peut pas combattre ça…",
        font, clock, sprite_garen
    )

    display_dialogue_box(screen,
        "Garen recule légèrement derrière vous, évitant soigneusement de marcher sur une pierre craquelée qui pourrait trahir sa présence. "
        "Il s’efforce de contrôler sa respiration, mais ses doigts tremblants trahissent sa peur grandissante.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Aldric (calme) : Ce ne sont pas des démons. Mais elles ne sont pas vivantes non plus.",
        font, clock, sprite_aldric
    )

    display_dialogue_box(screen,
        "Votre voix se fait basse, mesurée. Inutile de montrer la moindre hésitation. "
        "Vous avancez avec précaution, observant ces entités sans vie, espérant que leur attention reste ailleurs.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Ayela (tremblante, en serrant son arc) : Je… Je n’ai jamais vu… rien de tel…",
        font, clock, sprite_ayela
    )

    display_dialogue_box(screen,
        "Ayela s’accroche nerveusement à son arc, mais ses mains tremblent trop pour bander correctement une flèche. "
        "Vous sentez qu’elle lutte contre l’envie de fuir, mais ses pieds restent ancrés au sol, malgré la peur qui tord ses traits.",
        font, clock
    )

    display_dialogue_box(screen,
        "L’air devient de plus en plus froid. Chaque pas semble pesé et surveillé. "
        "Les créatures poursuivent leur ronde, ignorant encore votre présence, mais combien de temps cela durera-t-il… ?",
        font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/etage4b.webp", WIDTH, HEIGHT)
    
    fade_in_music("graphics/resources/music/DarkLight.mp3", max_volume=0.2, fade_duration=1000)
    
    display_dialogue_box(screen,
    "Les hurlements d’agonie se répercutent dans la salle. Certains participants, pensant pouvoir affronter les créatures, "
    "se jettent imprudemment dans la bataille. Ils réalisent trop tard que leur bravoure est vaine.",
    font, clock
    )

    display_dialogue_box(screen,
    "Une lanterne noire s’abat sur un guerrier en armure, sa lumière spectrale le consumant en un instant. "
    "Son cri s’étouffe alors que son corps s’effondre, vidé de toute énergie vitale.",
    font, clock
    )

    display_dialogue_box(screen,
    "Plus loin, une silhouette tente de fuir, mais une créature surgit des ombres et l'attrape. "
    "La victime est entraînée dans l'obscurité, ses cris s'estompant rapidement, laissant place à un silence pesant.",
    font, clock
    )

    display_dialogue_box(screen,
    "Chaque mouvement imprudent attire l’attention des créatures. "
    "Leur lanterne noire danse dans l’obscurité, et chaque pulsation de lumière marque une nouvelle victime.",
    font, clock
    )

    display_dialogue_box(screen,
    "Certains participants tentent de rester immobiles, espérant passer inaperçus. "
    "D’autres, paralysés par la peur, se font surprendre sans même pouvoir se défendre.",
    font, clock
    )

    display_dialogue_box(screen,
    "Le groupe d’Aldric avance prudemment, évitant les pièges et les regards perçants des créatures. "
    "Mais la tension est palpable. Chaque pas pourrait être leur dernier dans cette salle infernale.",
    font, clock
    )
    display_dialogue_box(screen,
        "La salle est vaste, mais les créatures sont nombreuses. "
        "Elles avancent lentement, balayant l’espace de leur lanterne noire. "
        "Il n’y a que deux options : avancer lentement et en silence, ou détourner leur attention.",
        font, clock
    )
    display_dialogue_with_sprite(screen,
            "Clotaire : Et Emphyr pourquoi tu aides le paysan ?",
            font, clock, sprite_clotaire
        )

# Ajout du conseil d'Aldric
    display_dialogue_box(screen,
    "Alors que le groupe avance, Aldric observe attentivement les créatures et leurs mouvements. "
    "Après un moment de réflexion, il se tourne vers Clotaire et les autres.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Aldric : 'Ces lanternes... Elles semblent être la source de leur pouvoir. Si on tranche leurs mains, elles ne pourront plus les utiliser.'",
        font, clock, sprite_aldric
    )

    display_dialogue_box(screen,
    "Clotaire lève un sourcil, un sourire moqueur au coin des lèvres, mais ne répond rien. "
    "Quelques pas plus tard, une créature se rapproche dangereusement du groupe, sa lanterne noire balayant la zone.",
    font, clock
    )

# Clotaire met le plan en action
    display_dialogue_with_sprite(screen,
    "Clotaire (d’un ton sarcastique) : Très bien, blondinet, testons ta brillante idée.",
    font, clock, sprite_clotaire
    )

    display_dialogue_box(screen,
    "Avec une précision mortelle, Clotaire s’élance et tranche d’un seul coup les deux mains de la créature. "
    "La lanterne tombe au sol, et la créature recule en poussant un hurlement strident avant de disparaître dans les ombres.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Clotaire (sarcastique) : Eh bien, merci pour le conseil, Aldric. Prochain coup, je te laisse t’en charger.",
    font, clock, sprite_clotaire
    )

# Réactions après l’action
    display_dialogue_with_sprite(screen,
    "Garen (impressionné) : Grrr il nous as entendu.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Aldric (calme) : Laise le. Cet imbécilé de Clotaire m'a servit d'appat et a confirmer mon idée.",
    font, clock, sprite_aldric
    )

    display_dialogue_box(screen,
    "Le groupe continue à avancer avec prudence, utilisant la stratégie d’Aldric pour neutraliser les créatures. "
    "Mais chaque attaque porte le risque d’une contre-offensive fatale.",
    font, clock
    )

    
        # Définir les actions possibles
    options = [
        ("Avancer lentement (Discrétion totale).", 0),
        ("Créer une diversion (Prendre un risque calculé).", 1)
    ]

    # Affiche la boîte de choix
    choix = display_choices_box(screen, font, options, clock)

    # Gestion des choix et conséquences
    if choix == 0:  # Avancer lentement
        display_dialogue_box(screen,
            "Vous avancez à pas feutrés, chaque souffle retenu, évitant soigneusement les lanternes funestes. "
            "L'air est si dense que même vos propres battements de cœur semblent résonner contre les piliers antiques. "
            "Les murmures des créatures, bien que lointains, glissent jusqu'à vos oreilles, tissant une toile d'angoisse palpable.",
            font, clock
        )

        display_dialogue_box(screen,
            "Mais alors que vous progressez en ligne serrée, un cri retentit. "
            "Derrière vous, l’un des participants trébuche, son pied heurtant violemment une pierre dissimulée par la brume. "
            "Le bruit résonne dans toute la salle comme une cloche funèbre.",
            font, clock
        )

        display_dialogue_box(screen,
            "Avant même qu'il ne puisse se relever, la lumière noire s'élève, enveloppant son corps frêle comme un linceul. "
            "Son cri s'étouffe rapidement, remplacé par un silence terrifiant. "
            "Son visage figé dans une grimace de terreur disparaît sous une couche de pierre sombre.",
            font, clock
        )

        display_dialogue_with_sprite(screen,
            "Clotaire : Merci bien pour la couverture !",
            font, clock, sprite_clotaire
        )
        display_dialogue_with_sprite(screen,
            "Garen : Enfoiré !!!",
            font, clock, sprite_garen
        )
        display_dialogue_with_sprite(screen,
            "Velm : La ferme paysan !  Tu veux finir comme lui ?",
            font, clock, sprite_velm
        )

        display_dialogue_with_sprite(screen,
            "Kael (à voix basse, un regard sombre) : Mort. Il n'aurait pas dû venir dos à lui… Continue de marcher. Ce Clotaire...",
            font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
            "Aldric : Il est prêt à tous les coups bas. Attention !",
            font, clock, sprite_aldric
        )

        display_dialogue_with_sprite(screen,
            "Kael : Garen ! Si tu t'arrêtes pour pleurer, tu seras le suivant.",
            font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
            "Emphyr : Endurcis-toi un peu !",
            font, clock, sprite_emphyr
        )
        display_dialogue_with_sprite(screen,
            "Garen (les poings serrés, regard fixé au sol) :Il voulait juste réussir…",
            font, clock, sprite_garen
        )
        display_dialogue_with_sprite(screen,
            "Brandio : Gamin ! L'ascension est impitoyable ! Tu dois penser d'abord à toi !",
            font, clock, sprite_brandio
        )
        display_dialogue_box(screen,
            "Les statues silencieuses continuent de veiller sur leur victime nouvelle, tandis que vous poursuivez votre marche, les épaules plus lourdes qu'avant.",
            font, clock
        )

    elif choix == 1:  # Créer une diversion
        display_dialogue_box(screen,
            "Tu t’accroupis lentement, cherchant du bout des doigts une pierre lisse et froide. "
            "En la serrant dans ta paume, tu ressens toute la tension pesant sur tes épaules. "
            "Le regard des créatures semble peser sur toi sans même qu'elles ne t’aient repéré. "
            "Tu inspires profondément… et lances la pierre au loin, vers un amas de piliers brisés.",
            font, clock
        )

        display_dialogue_box(screen,
            "Un bruit sourd résonne. Presque aussitôt, la créature la plus proche lève lentement la tête. "
            "Son capuchon tressaille, et elle glisse silencieusement vers l’origine du son, ses mouvements aussi fluides que l’ombre.",
            font, clock
        )

        display_dialogue_box(screen,
            "Vous profitez de cette diversion pour avancer rapidement. Mais à quelques pas de l’autre côté, "
            "Kael et Garen se retrouvent soudain bloqués. "
            "Un autre groupe de créatures s’est déplacé et les encercle partiellement, laissant très peu d’espace pour passer.",
            font, clock
        )

        display_dialogue_with_sprite(screen,
            "Kael (à voix basse, le regard froid) : Fantastique. Piégés. Juste quand ça devenait intéressant…",
            font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
            "Garen (le souffle court, regard anxieux) : On peut pas rester là. "
            "Si on bouge pas ensemble… ils nous auront l’un après l’autre.",
            font, clock, sprite_garen
        )
        display_dialogue_with_sprite(screen,
            "Emphyr : Bouge maintenant ! C'est le bon timing !",
            font, clock, sprite_emphyr
        )
        display_dialogue_with_sprite(screen,
            "Clotaire : Et Emphyr pourquoi tu aides le paysan ?",
            font, clock, sprite_clotaire
        )

        display_dialogue_box(screen,
            "Kael finit par hocher la tête, et Garen s’accroche à l’épée qu’il tient maladroitement. "
            "Vous attendez un court instant, puis glissez silencieusement à travers les ombres, "
            "espérant que la tour détourne son regard un instant de plus.",
            font, clock
        )

    else:  # Cas d'erreur pour un choix invalide
        display_dialogue_box(screen,
            "Choix invalide. Réessayez.",
            font, clock
        )
    
    display_dialogue_box(screen,
        "À mi-chemin, l’une des créatures s’arrête et lève sa lanterne, comme si elle percevait quelque chose. "
        "Ayela recule d’un pas involontaire…",
        font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/creature4.webp", WIDTH, HEIGHT)
    display_dialogue_box(screen,
        "La créature s’approche lentement et pousse un cri assourdissant, ses mouvements étrangement fluides malgré sa stature déformée. "
        "Sa lanterne noire projette des éclats de lumière malsaine dans la salle.",
        font, clock
    )

    display_dialogue_box(screen,
        "Un souffle glacial effleure Ayela en premier, et la créature incline légèrement sa lanterne vers elle, comme pour sonder son âme.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Créature (murmurant) : Ayela… Les bois, la maladie… Tu n’y échapperas pas. "
        "Peu importe ta fuite, tu ne les sauveras pas...",
        font, clock, sprite_creature
    )

    display_dialogue_box(screen,
        "Ayela serre son arc, mais un frisson la parcourt malgré elle. Elle détourne brièvement les yeux.",
        font, clock
    )

    display_dialogue_box(screen,
        "La créature se détourne ensuite vers Aldric, sa lanterne vibrant d’une lumière plus sombre.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Créature : Aldric… Un étranger parmi eux. Tu viens de loin… Loin de cet empire brisé.",
        font, clock, sprite_creature
    )

    display_dialogue_box(screen,
        "Aldric soutient son regard sans ciller, mais il sent le poids de cette présence familière.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Créature (voix grave) : Pourquoi la tour t’est-elle si familière ?",
        font, clock, sprite_creature
    )

    display_dialogue_box(screen,
        "Aucune réponse ne vient. La créature continue…",
        font, clock
    )

    # Passage sur Kael
    display_dialogue_box(screen,
        "Elle s’arrête devant Kael. Son regard semble sonder la noblesse enfouie sous ses cicatrices.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Créature (sifflante) : Kael… Dernier vestige d’une maison que même les corbeaux ont abandonnée.",
        font, clock, sprite_creature
    )

    display_dialogue_with_sprite(screen,
        "Créature : Je vois ton oncle agenouillé, implorant pitié devant l’Empire. Mais toi… Toi, tu refuses de plier."
        " C’est une fierté noble, mais les fiertés solitaires sont des tombes bien creuses.",
        font, clock, sprite_creature
    )
    
    display_dialogue_box(screen,
        "Kael lève la tête, serrant la garde de sa rapière. "
        "Pourtant, malgré son regard dur, il ne parvient pas à cacher une brève lueur de doute.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Kael (froidement) : Tu ne sais rien de moi.",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Créature (moqueuse) : C’est ce que tu crois… Je vois un avenir. "
        "Un avenir où tu ne venges personne. "
        "Seulement un nom gravé dans la pierre, oublié des vivants.",
        font, clock, sprite_creature
    )

    # Passage sur Garen
    display_dialogue_box(screen,
        "La créature poursuit sa route, lentement, jusqu’à ce que la lanterne s’arrête sur Garen, "
        "baissant presque comme pour l’examiner de plus près.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Créature (doucement) : Garen… Le fermier qui rêve de héros. "
        "Combien de fois as-tu échoué avant même de commencer ?",
        font, clock, sprite_creature
    )

    display_dialogue_box(screen,
        "Garen évite le regard de la créature, le poing serré contre sa poitrine. "
        "Il tente de garder contenance, mais ses épaules s’affaissent légèrement.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Créature (plus sévère) : Tu n’as pas protégé ton frère…il est mort à la guerre "
        "Et tu échoueras à protéger ceux qui restent."
        " Quand tu rentreras, ta ferme sera en ruine… Ta famille n’attendra plus personne.",
        font, clock, sprite_creature
    )

    display_dialogue_box(screen,
        "Les mots pèsent lourd. Garen reste silencieux, mais une rage froide grandit en lui.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Garen (murmurant) :Tu te trompes...j'y arriverai...Je crois..",
        font, clock, sprite_garen
    )

    display_dialogue_box(screen,
        "La créature sourit dans l’ombre, continuant son chemin. Elle dirige sa lanterne sur Ayela créeant un faiseau.",
        font, clock
    )
    
        # Définir les actions possibles
    options = [
        ("Tirer Ayela hors du faisceau.", 0),
        ("Utiliser un objet pour bloquer la lumière.", 1),
        ("Affronter la créature malgré les avertissements.", 2)
    ]

    # Affiche la boîte de choix
    choix_ayela = display_choices_box(screen, font, options, clock)
    background = fade_in_background(screen,"graphics/resources/backgrounds/ayelaetage4.webp", WIDTH, HEIGHT)
    # Gestion des choix et conséquences
    if choix_ayela == 0:  # Tirer Ayela hors du faisceau
        display_dialogue_box(screen,
            "Voyant le danger s'approcher d'Ayela, tu réagis instinctivement. "
            "Tu l'attrapes fermement par le bras et la tires violemment en arrière, hors du faisceau noir. "
            "La lumière effleure la bordure de ton manteau, brûlant le tissu et marquant ta peau d'une vive douleur.",
            font, clock
        )

        display_dialogue_box(screen,
            "Ayela trébuche contre toi, ses mains agrippant ton bras avec force. "
            "Son souffle est saccadé, et ses yeux, écarquillés de terreur, croisent les tiens dans un silence pesant.",
            font, clock
        )

        display_dialogue_with_sprite(screen,
            "Ayela (voix tremblante) : Merci… Je… Je te dois la vie...(+5 relation avec Ayela, PV -15).",
            font, clock, sprite_ayela
        )

        display_dialogue_with_sprite(screen,
            "Aldric (sérieux, gardant son calme) : Reste concentrée. La prochaine fois, je ne pourrai peut-être pas t’aider.",
            font, clock, sprite_aldric
        )

        display_dialogue_box(screen,
            "Ayela hoche la tête faiblement, reprenant lentement ses esprits. "
            "Malgré la brûlure qui te lance, tu reprends la marche en silence, sentant le regard d'Ayela peser sur toi.",
            font, clock
        )

        hero.get_relation("Ayela").adjust_score(+5)
        hero.adjust_health(-15)

    elif choix_ayela == 1:  # Utiliser un objet pour bloquer la lumière
        display_dialogue_box(screen,
            "Calme et méthodique, tu plonges la main dans ta sacoche, sortant un petit miroir poli. "
            "Sans hésitation, tu l'élèves devant toi, capturant brièvement la lumière noire. "
            "Un faisceau inversé se propage, attirant l'attention de la créature vers un autre groupe.",
            font, clock
        )

        display_dialogue_box(screen,
            "Trois participants, plus lents à réagir, se retrouvent pris au piège du faisceau. "
            "Leur corps se raidit, leurs cris s'étouffent et bientôt ils ne sont plus que des statues figées dans l'horreur.",
            font, clock
        )

        display_dialogue_with_sprite(screen,
            "Garen (abasourdi, la voix brisée) : On aurait pu les sauver… (-15 relation avec Garen).",
            font, clock, sprite_garen
        )

        display_dialogue_with_sprite(screen,
            "Ayela (les larmes aux yeux, secouée) : C'est ma faute... Je suis trop conne... Si je n'avais pas… je… je…",
            font, clock, sprite_ayela
        )

        display_dialogue_with_sprite(screen,
            "Emphyr : On ne peut pas sauver tout le monde !",
            font, clock, sprite_emphyr
        )

        display_dialogue_with_sprite(screen,
            "Kael (calme, mais tranchant) : Hé, la demoiselle… C’est pas le moment de chialer. "
            "C'était eux ou toi. La tour ne fait pas de cadeaux. Pas vrai, Aldric ?",
            font, clock, sprite_kael
        )

        display_dialogue_with_sprite(screen,
            "Aldric (froid, détaché) : Ils savaient les risques. Si c'était nous à leur place, ils n'auraient pas hésité non plus.",
            font, clock, sprite_aldric
        )

        display_dialogue_with_sprite(screen,
            "Kael (souriant légèrement) : Bien parlé. J'apprécie ton sens des priorités. (+10 relation pragmatique avec Kael).",
            font, clock, sprite_kael
        )

        display_dialogue_box(screen,
            "Ayela serre les poings, les yeux rivés au sol. Garen reste en retrait, le regard hanté par la scène."
            "Le poids des décisions prises pèse lourdement sur le groupe alors que vous reprenez lentement votre marche vers l’inconnu.",
            font, clock
        )

        hero.get_relation("Garen").adjust_score(-15)
        hero.get_relation("Kael").adjust_score(+10)

    else:  # Choix invalide
        display_dialogue_box(screen,
            "Choix invalide.",
            font, clock
        )
    background = fade_in_background(screen,"graphics/resources/backgrounds/etage4fin.webp", WIDTH, HEIGHT)


# Scène où Garen tombe et la créature utilise sa lanterne
    display_dialogue_box(screen,
    "Alors que le groupe progresse prudemment et péniblement, un cri perçant brise le silence. "
    "Garen trébuche et tombe lourdement sur le sol, à la merci d’une créature sinistre sortant des ombres.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Garen (terrifié) : Mon épée...merde ! Je suis foutu !",
    font, clock, sprite_garen
    )

    display_dialogue_box(screen,
    "La créature brandit une lanterne ténébreuse, d’où émane une lumière spectrale. "
    "Une chaleur oppressante envahit l’air, et la lanterne semble vouloir brûler Garen, "
    "aspirant lentement son énergie vitale dans un tourbillon sombre.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Aldric (dégainant son épée) : Tiens bon, Garen !",
    font, clock, sprite_aldric
    )
    display_dialogue_with_sprite(screen,
    "Kael (avec mépris) : Laisse le ! A chaque fois il nous fait le coup..",
    font, clock, sprite_kael
    )

    display_dialogue_box(screen,
    "Aldric s’apprête à intervenir, mais une explosion de lumière éclatante le devance. "
    "Emhyr apparaît soudain, levant une main entourée d’un cercle de symboles alchimiques lumineux. "
    "Un éclat doré enveloppe la créature avant qu’elle ne se désintègre dans un hurlement déchirant.",
    font, clock
    )  

# Réactions après la destruction de la créature
    display_dialogue_with_sprite(screen,
    "Emhyr (croisant les bras, regardant Aldric) : Trop lent, blondinet.",
    font, clock, sprite_emphyr
    )

    display_dialogue_box(screen,
    "Malgré le ton moqueur, aucune méchanceté ne transparaît dans ses mots. "
    "Elle regarde Garen, toujours au sol, le souffle court.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Emhyr (calmement) : Lève-toi, paysan. La Tour ne pardonne pas ceux qui traînent.",
    font, clock, sprite_emphyr
    )

    display_dialogue_with_sprite(screen,
    "Garen (haletant, terrifié) :Merci… Merci… Je… Je me voyer mort...",
    font, clock, sprite_garen
    )

    display_dialogue_box(screen,
    "Emhyr tend brièvement la main à Garen pour l’aider à se relever, puis se retourne sans ajouter un mot. "
    "Aldric reste immobile, fixant Emhyr, les sourcils légèrement froncés.",
    font, clock
    )

# Réflexion interne d'Aldric
    display_dialogue_box(screen,
    "Un instant, Aldric se demande pourquoi Emhyr, qui est avec Clotaire, a choisi de sauver Garen. "
    "Mais avant qu’il ne puisse trouver une réponse, elle disparaît à nouveau dans l’ombre.",
    font, clock
    )

# Transition vers la suite
    display_dialogue_box(screen,
    "Finalement, après une progression lente et douloureuse, vous atteignez l’autre côté de la salle. "
    "Les créatures cessent de vous poursuivre dès que vous franchissez la porte suivante, "
    "comme retenues par une barrière invisible. Derrière vous, l’obscurité s’étend, avalant les silhouettes des malheureux restés derrière.",
    font, clock
    )

    display_dialogue_box(screen,
        "Finalement, après une progression lente et douloureuse, vous atteignez l’autre côté de la salle. "
        "Les créatures cessent de vous poursuivre dès que vous franchissez la porte suivante, "
        "comme retenues par une barrière invisible. Derrière vous, l’obscurité s’étend, avalant les silhouettes des malheureux restés derrière.",
        font, clock
    )

    display_dialogue_box(screen,
        "Ayela s’appuie un instant contre le mur froid, la respiration encore irrégulière. "
        "Ses doigts tremblants effleurent son arc alors qu’elle tente de retrouver son calme. "
        "Une larme solitaire glisse sur sa joue avant qu’elle ne l’essuie rapidement, évitant tout regard prolongé.",
        font, clock
    )

    display_dialogue_box(screen,
        "Elle reste silencieuse un moment, scrutant la porte par laquelle ils viennent de passer, "
        "comme si quelque chose la retenait encore là-bas, dans cette salle où la créature avait murmuré son destin.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Ayela (à voix basse, esquissant un faible sourire malgré elle) : Merci… Tu as fait ce qu’il fallait…",
        font, clock, sprite_ayela
    )
    fade_out_music(fade_duration=1000)

    display_dialogue_box(screen,
        "Mais dans sa voix, quelque chose a changé. "
        "Un doute persiste, creusant une faille qu’elle tente maladroitement de masquer.",
        font, clock
    )
    display_dialogue_box(screen,
        "Alors que le groupe avance avec prudence, les ombres menaçantes et le silence oppressant semblent s'atténuer. "
        "Devant eux, une porte massive en métal se dessine, brillant faiblement sous la lumière vacillante des torches.",
        font, clock
    )

    display_dialogue_box(screen,
        "Chaque pas résonne lourdement, comme une promesse tacite que cet étage dangereux est enfin derrière eux. "
        "Ils sentent un mélange de soulagement et d’appréhension en approchant de la porte qui marquera leur passage au prochain niveau.",
        font, clock
    )
    fade_in_music("graphics/resources/music/Fates.mp3", max_volume=0.2, fade_duration=1000)
    background = fade_in_background(screen,"graphics/resources/backgrounds/escalier4.PNG", WIDTH, HEIGHT)
    
    display_dialogue_with_sprite(screen,
        "Kael (croisant les bras, jetant un regard amusé à Garen) : On a survécu. C’est tout ce qui compte. "
        "la tour devra essayer plus fort pour me mettre à genoux.",
        font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen,
        "Garen (haletant, les mains sur les genoux) :Parle pour toi… Moi, j’ai cru que c’était fini à trois reprises. "
        "Ces créatures… elles… elles n’ont même pas d’yeux, mais elles savent où nous sommes.",
        font, clock, sprite_garen
    )

    display_dialogue_box(screen,
        "Un silence s’installe alors que Garen jette un regard inquiet vers Aldric. "
        "Les mots de la créature semblent peser davantage sur le jeune fermier, comme une prédiction qu’il ne peut effacer de son esprit.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Garen (murmurant) : Elle a dit que je ne sauverai personne…",
        font, clock, sprite_garen
    )

    display_dialogue_box(screen,
        "Il évite les regards de ses compagnons, baissant légèrement la tête.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Kael (soupirant) : Ignore ces foutaises. Ce n’était qu’un monstre cherchant à nous briser.",
        font, clock, sprite_kael
    )

    display_dialogue_box(screen,
        "Kael serre brièvement la garde de sa rapière, mais un éclat dans ses yeux laisse deviner qu’il n’est pas aussi convaincu qu’il le prétend.",
        font, clock
    )
    
    display_dialogue_with_sprite(screen,
        "Kael (plus bas) : Elle parlait de mon oncle… De l’Empire. Comment aurait-elle pu savoir ça ?",
        font, clock, sprite_kael
    )
    
    display_dialogue_box(screen,
        "Son ton se durcit, trahissant une fêlure profonde qu’il garde d’ordinaire enfouie sous son arrogance.",
        font, clock
    )

    display_dialogue_box(screen,
        "Aldric observe Kael du coin de l’œil, mais ne dit rien. "
        "Le guerrier comprend que ce combat n’était pas simplement physique. "
        "La tour creuse, perce les âmes… et cette créature n’était qu’un avant-goût de ce qui les attend.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Aldric (calmement) : C’était plus simple que je ne le pensais. Elles ne semblent pas vouloir franchir cette porte…",
        font, clock, sprite_aldric
    )
    display_dialogue_box(screen,
        "Il observe l'obscurité derrière lui, pensif.",
        font, clock
    )

    display_dialogue_box(screen,
        "Les pas du groupe résonnent dans l’escalier en colimaçon, les ombres des torches dansant sur les murs humides. "
        "Garen marche en silence, jetant des regards nerveux derrière lui à chaque grincement. "
        "Kael, en revanche, semble détendu, mais son regard ne quitte pas Aldric.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Kael (légèrement moqueur, un sourire en coin) : À quoi tu penses ? D’ailleurs… je ne suis pas le seul à le remarquer, n’est-ce pas ?",
        font, clock, sprite_kael
    )
    display_dialogue_box(screen,
        "Kael incline la tête vers Garen, qui acquiesce silencieusement.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Kael : Tu es dans ton élément ici… c’est presque… trop naturel pour toi. "
        "Tu n’as pas peur, tu avances d’un pas assuré… C’est suspect…",
        font, clock, sprite_kael
    )

    display_dialogue_box(screen,
        "Aldric ne répond pas immédiatement, ses yeux fixés sur les marches devant lui. "
        "Il sent le poids du regard de Kael, mais il ne détourne pas le sien de la torche vacillante qui guide leur ascension.",
        font, clock
    )

    display_dialogue_with_sprite(screen,
        "Aldric (calme, mais distant) : Je sais me battre, j'ai vu la guerre, la misère, la désolation...ces ombres..j'ai deja vu pire.",
        font, clock, sprite_aldric
    )

    display_dialogue_with_sprite(screen,
        "Kael (ricanant doucement) : Hah. Peut-être… ou peut-être que tu es juste inconscient ou suicidaire.",
        font, clock, sprite_kael
    )

    display_dialogue_box(screen,
        "Garen reste silencieux, préférant garder ses pensées pour lui. "
        "Ayela serre la sangle de son carquois, jetant un dernier regard vers Aldric. "
        "Tous ressentent que ce n’est que le début… et que plus ils montent, plus la tour se montrera cruelle.",
        font, clock
    )
    
        # Dialogue avec Kael
    def kael_dialogue_3(hero, screen, font, clock, sprites):
        # Initialiser les dialogues
        kael = sprites["Kael"]
        garen = sprites["Garen"]
        ayela = sprites["Ayela"]

        # Narration avant le dialogue
        display_dialogue_box(screen,
            "Une tension palpable s’installe dans le groupe. Les regards échangés oscillent entre défiance et curiosité. "
            "Kael, comme à son habitude, ne peut s’empêcher de provoquer Aldric.",
            font, clock
        )

        # Options de dialogue
        options = [
            (
                "Un conseil, je suis pas comme Garen. Joue au malin avec moi et ca sera ton dernier étage.",
                -5,  # Impact sur Kael
                [
                    (kael, "Kael (froidement) : Tu ferais mieux de tenir tes promesses, Aldric."),
                    (garen, "Garen (inquiet) : Tu n’avais pas besoin d’être aussi direct..."),
                    (ayela, "Ayela (croisant les bras) : C’est bon, pas besoin de jouer les durs. On est tous dans la même galère.")
                ]
            ),
            (
                "Rien ne t’oblige à me suivre. Si je pose problème, tu est libre de continuer sans moi.",
                5,  # Impact positif sur Kael et autres
                [
                    (kael, "Kael (soupirant légèrement) : Hm. Tu n’as pas tort... C’est notre choix de rester ici."),
                    (garen, "Garen (avec un sourire timide) : Je suis d’accord. Aldric est quelqu’un de fiable."),
                    (ayela, "Ayela (taquinant) : Et plutôt mignon, non ? Courageux, mystérieux... Je suis fan.")
                ]
            ),
            (
                "Je ne cherche pas de conflits. Nous avons besoin de rester unis si nous voulons survivre.",
                10,  # Impact positif sur tout le groupe
                [
                    (kael, "Kael (hésitant) : Hm… Peut-être que tu n’es pas aussi arrogant que je le pensais."),
                    (garen, "Garen (enthousiaste) :Oui, Aldric a raison ! Si on reste soudés, on peut surmonter n’importe quoi."),
                    (ayela, "Ayela (souriant doucement) : Enfin quelqu’un avec un peu de bon sens. Merci, Aldric.")
                ]
            )
        ]

        # Gérer le dialogue et les relations
        process_dialogue(screen, font, hero, options, clock, "Kael")
    kael_dialogue_3(hero, screen, font, clock, sprites)
    

        # Narration après le dialogue
    display_dialogue_box(screen,
            "Après cet échange, le groupe continue à avancer, chacun digérant les paroles d’Aldric à sa manière. "
            "La tension semble s’être dissipée légèrement, bien que Kael garde son air méfiant habituel.",
            font, clock
        )

    # Réactions en fonction du choix
    if hero.get_relation("Kael").score >= 15:
        display_dialogue_with_sprite(screen,
            "Kael (soupirant, baissant légèrement les yeux) : Tu as... raison après tout. "
            "Ce n’est pas comme si tu m’avais forcé a vous suivre, hein ?",
            font, clock, sprite_kael
        )
        display_dialogue_box(screen,
            "Il évite le regard direct d’Aldric, tentant de masquer cette pointe d’embarras qui transparaît dans sa voix.",
            font, clock
        )
        display_dialogue_with_sprite(screen,
            "Garen (hochant la tête, avec assurance) : J’ai confiance en Aldric. "
            "Il parle peu mais c’est quelqu’un de fiable, même dans le pire des cas.",
            font, clock, sprite_garen
        )
        display_dialogue_box(screen,
            "Garen se tient un peu plus droit, bien que ses mains tremblent encore légèrement. "
            "Ses mots sont pleins de sincérité, mais une lueur d’inquiétude brille au fond de ses yeux. "
            "Kael, malgré son arrogance habituelle, détourne brièvement le regard, comme s'il évitait d'admettre qu'il partage ce sentiment.",
            font, clock
        )
        display_dialogue_with_sprite(screen,
            "Ayela (taquinant légèrement, croisant les bras) : ...Et puis, il est plutôt beau garçon, non ? "
            "Courageux, ténébreux… Un vrai protagoniste de conte.",
            font, clock, sprite_ayela
        )
        display_dialogue_box(screen,
            "Une tentative évidente d’alléger l’atmosphère pesante, mais quelque chose dans sa voix trahit une certaine tendresse. "
            "Ses yeux se posent sur Aldric un peu trop longtemps avant qu’elle ne détourne le regard rapidement.",
            font, clock
        )
        display_dialogue_with_sprite(screen,
            "Kael (gêné, agitant la main) : Ok, ça suffit. Je suis là pour survivre, pas pour écouter tes fantasmes.",
            font, clock, sprite_kael
        )
        display_dialogue_box(screen,
            "Le rire léger d’Ayela s’élève, brisant pour un instant la tension qui pesait sur le groupe. "
            "Pourtant, même ce bref moment de détente est teinté d’un voile de nervosité. "
            "Comme si tous savaient que l’obscurité de la tour n’attendait que de les rattraper.",
            font, clock
        )
    else:
        display_dialogue_with_sprite(screen,
            "Kael (froidement, baissant la voix) : Je vais te le dire une fois, Aldric. "
            "Si tu deviens une menace pour ma survie… je te neutraliserai. Je n’hésiterai pas.",
            font, clock, sprite_kael
        )
        display_dialogue_box(screen,
            "Son regard perçant s'attarde sur Aldric, pesant et sans équivoque.",
            font, clock
        )
        display_dialogue_box(screen,
            "L’espace autour d’eux semble se contracter, comme si chaque mot alourdissait l’air. "
            "Kael ne cligne pas des yeux, ses doigts effleurant subtilement la garde de sa rapière, prêt à tout instant.",
            font, clock
        )
        display_dialogue_with_sprite(screen,
            "Garen (inquiet, jetant un regard vers Kael) : Aldric… Fais attention à lui.",
            font, clock, sprite_garen
        )
        display_dialogue_box(screen,
            "Le jeune fermier a baissé d’un ton, mais la peur est perceptible dans ses paroles. "
            "Il tente de cacher cette nervosité par une posture plus droite, mais son regard fuyant le trahit.",
            font, clock
        )
        display_dialogue_box(screen,
            "Aldric croise les bras, observant Kael sans détour. "
            "La tension entre eux est palpable, une étincelle prête à embraser le fragile équilibre du groupe.",
            font, clock
        )
        display_dialogue_with_sprite(screen,
            "Aldric (calmement) : Tu n’auras pas à le faire.",
            font, clock, sprite_aldric
        )
        display_dialogue_box(screen,
            "Kael esquisse un rictus en guise de réponse, mais ne dit rien de plus. "
            "Le groupe continue son ascension dans un silence inconfortable, "
            "les ombres des torches projetant des silhouettes menaçantes sur les murs étroits.",
            font, clock
        )
        display_dialogue_box(screen,
            "La tour semble s’amuser de leurs doutes, testant non seulement leur force, "
            "mais aussi leur confiance mutuelle. Une chose est claire : chaque marche gravie les rapproche "
            "non seulement du sommet, mais aussi de la fracture inévitable qui pourrait séparer le groupe.",
            font, clock
        )

    # Interaction entre Garen et Emphyr
    display_dialogue_with_sprite(screen,
        "Garen : M...merci pour tout à l'heure...",
        font, clock, sprite_garen
    )
    display_dialogue_with_sprite(screen,
        "Emphyr : Te fais pas d’idée... essaie au moins de rester en vie...compris ?",
        font, clock, sprite_emphyr
    )
    display_dialogue_with_sprite(screen,
        "Garen (géné):Euh..compris",
        font, clock, sprite_garen
    )

    
    fade_out_music(fade_duration=4000)
    fade_in_text(screen, "Fin du Chapitre 4 - Il reste 39 participants sur 99 et 96 étages", font, (WIDTH // 2, HEIGHT // 2), duration=2000)
    fade_out_text(screen, 1000)
    game_menu(screen, font, clock, WIDTH, HEIGHT, hero)
    
    
    
def chapitre_5(hero, screen, font, clock,sprites):
    
    global background
    
    sprites = load_sprites()

    sprite_aldric = sprites["Aldric"]
    sprite_garen = sprites["Garen"]
    sprite_mysterieux = sprites["Homme_mysterieux"]
    sprite_kael = sprites["Kael"]
    sprite_brandio = sprites["Brandio"]
    sprite_archeon = sprites["Archeon"]
    sprite_ayela = sprites["Ayela"]
    sprite_clotaire = sprites["Clotaire"]
    sprite_durnir = sprites["Durnir"]
    sprite_emphyr = sprites["Emphyr"]
    sprite_gallius = sprites["Gallius"]
    sprite_velm = sprites["Velm"]
    sprite_yohna = sprites["Yohna"]
    sprite_zyn = sprites["Zyn"]
    sprite_random_participant = sprites["Participant"]
    sprite_creature = sprites["Creature"]
    
    fade_in_music("graphics/resources/music/safe.mp3", max_volume=0.2, fade_duration=1000)
    clear_screen(screen)
    fade_in_text(screen, 
             "Chapitre 5 : A l'ombre d'un répis - Etage 4/99", 
             font, 
             (WIDTH // 2, HEIGHT // 2),  # Centré sur l'écran
             duration=3000)
    fade_out_text(screen, 3000, fade_speed=2)
    pygame.time.wait(1000)
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/passage.webp", WIDTH, HEIGHT)
    
    observer_relation = hero.get_relation("Homme mystérieux")
    if observer_relation:
        # Si une relation existe déjà, mettez à jour les informations du personnage
        archeon = observer_relation.character
        archeon.name = "Archeon"
        archeon.description = "Un homme énigmatique à la présence magnétique."
    else:
        # Si aucune relation n'existe, créez le personnage et ajoutez la relation
        archeon = Character("Archeon", "graphics/resources/sprites/Archeon.webp", 
                  "Un homme mysterieux.", 
                  "Ombre", gender="garçon")
        hero.add_relation(archeon, "neutral")
        return archeon
    
    
    # Description initiale de la scène
    display_dialogue_box(screen, 
    "La porte s'ouvre lentement, laissant place à une scène qui semble tout droit sortie d'un rêve. "
    "Des tapis d’un velours pourpre tapissent le sol, des tables en bois massif couvertes de plats fumants s’étendent à perte de vue. "
    "Les lanternes suspendues flottent doucement dans l’air, projetant une lumière dorée qui danse sur les murs de pierre. "
    "L’odeur sucrée du vin et des fruits frais envahit vos narines, tranchant radicalement avec la lourdeur des étages précédents.",
    font, clock
    )
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/repas.webp", WIDTH, HEIGHT)

    # Premières réactions des personnages
    display_dialogue_with_sprite(screen, 
    "Kael (méfiant, scrutant la salle) : Une blague ? Je n'y crois pas une seconde. Trop beau pour être vrai.",
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen, 
    "Garen (haletant, s’essuyant le front) : Est-ce... réel ? Je n’ai jamais vu ça... même chez les nobles du village.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen, 
    "Ayela (voix basse, yeux plissés) : Après tout ce qu’on a traversé, tu crois vraiment qu’on peut juste s’asseoir et manger ?",
    font, clock, sprite_ayela
    )

    display_dialogue_box(screen, 
    "Autour de vous, d’autres participants s’approchent timidement des tables. Certains échangent des regards inquiets, "
    "tandis que d’autres, trop fatigués, s’effondrent sans même poser de questions, attrapant des morceaux de pain ou des coupes de vin. "
    "Les murmures se répandent dans la salle, mais une chose est claire : personne ne fait confiance à cette apparente hospitalité.",
    font, clock
    )

# Apparition d'Archeon
    display_dialogue_box(screen, 
    "Un frisson parcourt la pièce alors qu’une silhouette se détache lentement de l’ombre. "
    "Adossé à un pilier au fond de la salle, l’homme mystérieux de l’entrée vous observe en silence. "
    "Ses yeux brillent dans la pénombre, et sans un bruit, il s’avance au milieu de la pièce, un sourire indéchiffrable au coin des lèvres.",
    font, clock
    )

    display_dialogue_with_sprite(screen, 
    "??? (d'une voix suave) : Qu’attendez-vous ? Mangez. La tour récompense ceux qui survivent.",
    font, clock, sprite_mysterieux
    )

    display_dialogue_box(screen, 
    "Il abaisse sa capuche avec une lenteur calculée, laissant apparaître de longs cheveux écarlates qui retombent sur ses épaules. "
    "Ses traits sont fins, presque trop parfaits, mais quelque chose dans son regard vous met mal à l’aise. "
    "Il dégage une confiance implacable, comme si chaque mouvement de cette tour était orchestré par sa volonté.",
    font, clock
    )

    display_dialogue_with_sprite(screen, 
    "Garen (murmurant, incapable de détourner les yeux) : C’est pas le type de l'entrée Aldric ? Il dégage une drôle d’aura.",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen, 
    "Kael (croisant les bras, un rictus nerveux au coin des lèvres) : Ce type me plaît pas. Ce type est suspect.",
    font, clock, sprite_kael
    )

    display_dialogue_box(screen, 
    "Kael ne quitte pas Archeon du regard, ses doigts effleurant discrètement la garde de sa rapière.",
    font, clock
    )
    
    display_dialogue_with_sprite(screen,
    "??? (regardant Kael, sourire amusé) : Tu n’as pas besoin de m’aimer. Écoute seulement. "
    "C’est tout ce que je demande. Je me nomme Archeon",
    font, clock, sprite_archeon
    )

# Narration - Archeon s'avance
    display_dialogue_box(screen,
    "Le silence s’installe alors qu’Archeon s’avance, passant lentement entre les tables. "
    "Chacun de ses pas semble échoir plus lourdement que les autres. "
    "Les participants détournent les yeux, mais vous pouvez sentir que tous retiennent leur souffle.",
    font, clock
    )

# Archeon avertit les participants
    display_dialogue_with_sprite(screen,
    "Archeon (voix calme, presque bienveillante) : Vous êtes trente-neuf. Peu atteindront le sommet. "
    "Les deux prochains étages seront impitoyables.",
    font, clock, sprite_archeon
    )

# Archeon parle du prix
    display_dialogue_with_sprite(screen,
    "Archeon : D’ailleurs, avant que je ne parte… Pour ouvrir la porte, vous devrez en payer le prix. "
    "Le prix de l’étage…",
    font, clock, sprite_archeon
    )

# Narration - Suspense
    display_dialogue_box(screen,
    "Il s’arrête un instant, laissant les mots planer dans l’air, savourant la confusion qui s’installe.",
    font, clock
    )

# Kael réagit
    display_dialogue_with_sprite(screen,
    "Kael (haussant un sourcil, bras croisés) : Poétique. Mais ça ne nous avance à rien.",
    font, clock, sprite_kael
    )

    display_dialogue_box(screen,
    "Kael ricane doucement, mais son rire sonne creux. "
    "Même lui n’arrive pas à cacher l’anxiété qui monte à mesure qu’Archeon parle.",
    font, clock
    )

# Narration - Disparition d’Archeon
    display_dialogue_box(screen,
    "Archeon sourit légèrement avant de se détourner, disparaissant lentement dans l’ombre du pilier d’où il était venu. "
    "Son absence laisse un vide étrange dans la salle, comme si la chaleur de la lumière avait quitté l’endroit avec lui.",
    font, clock
    )

# Interaction spéciale avec Aldric
    display_dialogue_box(screen,
    "Alors qu'Archeon s'apprête à se retirer dans l'ombre, il s'arrête un bref instant près d'Aldric. "
    "Son regard, perçant et presque amusé, s'attarde sur vous plus longtemps que nécessaire. "
    "Là, dans cette fraction de seconde, vous sentez qu'il vous observe d'une manière différente… Comme s'il voyait quelque chose que les autres ignorent.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Archeon (d'un ton bas et presque conspirateur) : Prends des forces. Je t'attends plus haut... Ne me déçois pas.",
    font, clock, sprite_archeon
    )

# Narration - Impression finale
    display_dialogue_box(screen,
    "Son murmure s’infiltre comme un frisson désagréable, laissant derrière lui une étrange impression de déjà-vu.",
    font, clock
    )
        # Narration - Disparition d'Archeon
    display_dialogue_box(screen,
    "Son ombre glisse au loin alors que ses pas disparaissent dans l'obscurité du pilier. Pourtant, même en son absence, "
    "l'aura d'Archeon semble planer dans la pièce, imprégnant chaque coin du regard des autres participants.",
    font, clock
    )

# Dialogue - Ayela inquiète
    display_dialogue_with_sprite(screen,
    "Ayela (inquiète, fronçant les sourcils) : Tu le connais ?",
    font, clock, sprite_ayela
    )

    display_dialogue_box(screen,
    "Sa voix est plus basse qu’à l’accoutumée, comme si elle craignait qu’Archeon puisse encore l’entendre.",
    font, clock
    )

# Dialogue - Réponse d'Aldric
    display_dialogue_with_sprite(screen,
    "Aldric (après une longue pause, fixant l'endroit où Archeon se tenait) : Je ne pense pas..Enfin je crois..",
    font, clock, sprite_aldric
    )

    display_dialogue_box(screen,
    "Mais même en prononçant ces mots, une part de vous doute. Comme si, quelque part, son visage vous était familier… "
    "Sans savoir pourquoi.",
    font, clock
    )

# Réactions silencieuses de Kael et Garen
    display_dialogue_box(screen,
    "Les regards de Kael et Garen se tournent vers vous, mais aucun d'eux ne parle. "
    "Kael détourne rapidement les yeux, comme agacé par la scène, tandis que Garen semble simplement troublé par l’échange silencieux.",
    font, clock
    )

# Relation avec Archeon
    hero.get_relation("Archeon").adjust_score(+5)

# Narration - Ressenti d'Aldric
    display_dialogue_box(screen,
    "Aldric peut sentir quelque chose changer en lui, un mélange d’excitation et d’appréhension… "
    "Car dans les profondeurs de la tour, il sait que ce n'est pas la dernière fois qu'il croise Archeon.",
    font, clock
    )
    display_dialogue_box(screen,
    "Après leurs échanges, Ayela, Garen, et Kael s'éloignent chacun de leur côté. "
    "Ayela s'installe à une table isolée, ses mains serrées autour de son arc. "
    "Garen s'assied près du feu pour se détendre. "
    "Kael, fidèle à lui-même, se calfeutre nonchalamment dans un coin sombre, un verre de vin, "
    "l'air pensif mais détendu.",
    font, clock
    )
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/repas.webp", WIDTH, HEIGHT)
    interactions = [
    "Parler à Garen.",
    "Parler à Kael.",
    "Parler à Ayela.",
    ]

    while interactions:
    # Préparer les options pour `display_choices_box`
        options = [(interaction, 0) for interaction in interactions]  # Placeholder pour la valeur
        choix_index = display_choices_box(screen, font, options, clock)  # Récupérer l'index sélectionné
        personnage = interactions[choix_index]

        if personnage == "Parler à Garen.":
            
            display_dialogue_with_sprite(screen, 
            "Aldric (vous vous approchez de Garen, le voyant pensif à l'écart des autres) : "
            "Au fait, tu m'as jamais dit pourquoi tu avais tenté la tour... ?", 
            font, clock, sprite_aldric
            )
            display_dialogue_with_sprite(screen, 
            "Garen (baissant les yeux, triturant l'anneau en cuir de son gantelet) : "
            "Ah ça... eh bien... J'ai quitté ma ferme. Mon père voulait me marier pour un prêt… parce que la ferme fait faillite depuis la mort de mon frère.", 
            font, clock, sprite_garen
        )
            display_dialogue_with_sprite(screen, 
            "Garen (légèrement tremblant) : "
            "Je voulais prouver à mon père que je pouvais subvenir... sauver la ferme. Mais je crois que j'ai surtout voulu me prouver à moi-même… "
            "que je ne suis pas l'incapable qu'il prétend.", 
            font, clock, sprite_garen
        )
            display_dialogue_box(screen, 
            "Sa voix est lourde de regrets et d'espoir. Il semble gêné, incapable de croiser votre regard.", 
            font, clock
        )
            display_dialogue_with_sprite(screen, 
            "Garen (riant nerveusement) : J'ai alors dépensé toutes mes économies… pour cet equipement et venir ici. "
            "Regarde-moi ça, du toc. Je crois que je me suis fait avoir...l'empire s'ecroule...ca se voit.", 
            font, clock, sprite_garen
        )
            display_dialogue_with_sprite(screen, 
            "Garen (voix basse) : Le pire dans tout ça, c'est que ma mère m'a dit au revoir... comme si elle savait que je ne reviendrais jamais. C'est peut etre pas plus mal..", 
            font, clock, sprite_garen
        )

    # Options de réponse pour Garen
            display_dialogue_box(screen, "Comment répondez-vous à Garen ?", font, clock)
            options_garen = [
            ("Tu te bats pour eux, certes... mais aussi pour toi. C'est ce qui compte. Tu veux te prouver que tu es capable.", 15),
            ("Peut-être que tu n'aurais pas dû venir…", -5)
            ]
            choix_garen = display_choices_box(screen, font, options_garen, clock)

    # Branches des réponses
            if choix_garen == 0:  # Réponse positive
                hero.get_relation("Garen").adjust_score(10)
                display_dialogue_with_sprite(screen, 
                "Garen (souriant sincèrement, levant enfin la tête) : Tu le penses vraiment ?", 
                font, clock, sprite_garen
                )
                display_dialogue_box(screen, 
                "Il vous regarde avec une sincérité touchante, un sourire timide aux lèvres.", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Garen : Merci Aldric. C'est grâce à toi si j'ai pu survivre jusqu'ici. "
                "Je vais sûrement mourir ici, mais au moins… je suis content de te connaître.", 
                font, clock, sprite_garen
                )
                display_dialogue_with_sprite(screen, 
                "Aldric (croisant les bras avec un léger sourire) : Je m'attendais pas à faire équipe non plus... mais je suis content aussi de te connaître, Garen.", 
                font, clock, sprite_aldric
                )
                display_dialogue_with_sprite(screen, 
                "Garen (regardant la porte suivante, déterminé) : J'espère que nous survivrons à tout ça... Merci Aldric.", 
                font, clock, sprite_garen
                )
                display_dialogue_with_sprite(screen, 
                "Aldric  : Possible que non..il reste 95 étages et on deja plus que 39 mais je crois que nous savions tous que c'etait un aller simple.(Garen +5)", 
                font, clock, sprite_aldric
                )
                display_dialogue_box(screen,
                "Vous Vous eloigner..",                     
                font, clock)

            elif choix_garen == 1:  # Réponse négative
                hero.get_relation("Garen").adjust_score(-5)
                display_dialogue_with_sprite(screen, 
                "Garen (déçu, baissant la tête encore plus bas) : Tu... tu as sûrement raison. Je ne suis qu'un boulet… (Garen -5)"
                "et en plus de ça, je vais sûrement mourir.", 
                font, clock, sprite_garen
                )
                display_dialogue_box(screen, 
                "Un silence inconfortable s'installe. Garen essaie de masquer sa peine, mais vous devinez facilement ses pensées.", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Aldric (tapant doucement l'épaule de Garen) : Je m'attendais pas à faire équipe non plus... mais je suis content aussi de te connaître.", 
                font, clock, sprite_aldric
                )
                display_dialogue_with_sprite(screen, 
                "Aldric (en se levant) : C'est trop tard pour faire demi-tour maintenant. Assume.", 
                font, clock, sprite_aldric
                )
                display_dialogue_with_sprite(screen, 
                "Garen (hochant doucement la tête) : Ouais… T'as raison.", 
                font, clock, sprite_garen
                )
                display_dialogue_box(screen,
                "Vous Vous eloigner..",                     
                font, clock)


        elif personnage == "Parler à Kael.":

            display_dialogue_with_sprite(screen,
            "Aldric (vous approchez Kael, installé nonchalamment près d'une table, une chope à la main) : "
            "Alors le noble, Dis-moi... Qu'est-ce qu'un type comme toi fait ici ?", 
            font, clock, sprite_aldric
        )
            display_dialogue_box(screen, 
            "Kael, le dos appuyé contre une poutre, lève à peine les yeux de sa boisson. "
            "Son sourire en coin trahit un amusement non dissimulé.", 
            font, clock
        )
            display_dialogue_with_sprite(screen, 
            "Kael (ricane en buvant sa bière) : Un noble, oui. Mais pas assez riche pour éviter de finir ruiné.", 
            font, clock, sprite_kael
        )
            display_dialogue_box(screen, 
            "Mon domaine viticole est en mauvais état. Je veux le sauver... Pour ne pas perdre mon titre et mon honneur. "
            "Tu comprends ça, non ? Si les legendes sont vraies alors la tour pourra m'aider..", 
            font, clock
        )
            display_dialogue_box(screen, 
            "Il tourne la chope entre ses doigts, pensif, mais son regard ne vous quitte pas. "
            "Un voile d'ironie couvre ses paroles, mais vous devinez qu'il en dit moins qu'il ne pense.", 
            font, clock
        )

    # Options de réponse pour Kael
            display_dialogue_box(screen, "Comment répondez-vous à Kael ?", font, clock)
            options_kael = [
            ( "Ça semble crédible. Mais tu caches autre chose.", -5),
            ("Tu mens mal, Kael.", 15)
            ]
            choix_kael = display_choices_box(screen, font, options_kael, clock)

    # Branches des réponses
            if choix_kael == 0:  # Réponse : Ça semble crédible
                hero.get_relation("Kael").adjust_score(5)
                display_dialogue_with_sprite(screen,
                "Kael (hausse un sourcil, amusé) : Hm… sans doute. Qui sait ?(Kael +5)", 
                font, clock, sprite_kael
                )
                display_dialogue_box(screen, 
                "Il prend une nouvelle gorgée, sans se départir de ce sourire narquois.", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Kael : Tu es bien plus malin que tu en as l'air, blondinet.", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Aldric (fronçant les sourcils) : M'appelle pas comme ça.", 
                font, clock, sprite_aldric
                )
                display_dialogue_with_sprite(screen, 
                "Kael (riant) : Oooh, j'ai touché une corde sensible ahah !", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Aldric : Mon père m'appelais comme ca..", 
                font, clock, sprite_aldric
                )
                display_dialogue_with_sprite(screen, 
                "Kael (riant) : Ton père ? t'appelais ? pourquoi en parle tu au passé ?", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Aldric : Il a disparu quand j'etait gamin...j'en ai des souvenirs..partiels mais bien la..", 
                font, clock, sprite_aldric
                )
                display_dialogue_with_sprite(screen, 
                "Kael : Tu pense qu'il est ici ?", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Aldric (s'éloignant): C'est ma dernière théorie...Pour ca je dois continuer !", 
                font, clock, sprite_aldric
                )
                display_dialogue_box(screen,
                "Vous Vous eloigner..",                     
                font, clock)

            elif choix_kael == 1:  # Réponse : Tu mens mal
                hero.get_relation("Kael").adjust_score(10)
                display_dialogue_with_sprite(screen,
                "Kael (sourire effacé, l'air surpris) : …Hah, t'es un petit futé toi. "
                "Je l'avais deviné dès qu'on s'est croisés à l'extérieur de la tour.(Kael +10)", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Kael : Tu es le genre de gars dont il faut se méfier, et c'est toujours mon cas.", 
                font, clock, sprite_kael
                )
                display_dialogue_box(screen, 
                "Il pose sa chope et tend la main, son regard sincère pour une fois.", 
                font, clock
                )
                display_dialogue_box(screen, 
                "Les deux hommes échangent une poignée de main ferme. La tension entre eux s'atténue légèrement.", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Kael : Mais je te respecte. Contrairement à d'autres ici…même si je ne sais pas ce qui te motive a tenter l'ascension..", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Aldric : Hm..mon père à disparu quand j'etait gamin...je suis tombé sur son journal il a mentionné la tour ", 
                font, clock, sprite_aldric
                )
                display_dialogue_with_sprite(screen, 
                "Kael : Hm interessant...", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Aldric : C'est ma dernière piste...", 
                font, clock, sprite_aldric
                )
                display_dialogue_with_sprite(screen, 
                "Kael (souriant à nouveau) : Alors Tâchons de ne pas mourir trop bas avant d'avoir trouver ce qu'on cherche..", 
                font, clock, sprite_kael
                )
                display_dialogue_box(screen,
                "Vous Vous eloigner..",                     
                font, clock)


        elif personnage == "Parler à Ayela.":
            display_dialogue_with_sprite(screen,
            "Aldric (vous approchez Ayela, assise à l'écart des autres, fixant le vide) : "
            "Et toi, alors, pourquoi tenter cette ascension au péril de ta vie ?", 
            font, clock, sprite_aldric
            )
            display_dialogue_box(screen, 
            "Ayela détourne légèrement les yeux, cherchant ses mots. Ses mains tremblent légèrement sur son arc posé à ses côtés.", 
            font, clock
            )
            display_dialogue_with_sprite(screen, 
            "Ayela (voix douce, presque murmurée) : Je viens de Rher a l'ouest, Mon village est frappé par une épidémie. Personne ne sait d'où ça vient…", 
            font, clock, sprite_ayela
            )
            display_dialogue_box(screen, 
            "Sa voix se brise un instant, trahissant une fragilité qu'elle s'efforce de masquer. J'ai pensé… que cette tour pourrait m'apporter des réponses.", 
            font, clock
            )
            display_dialogue_with_sprite(screen, 
            "Ayela (baissant légèrement la voix, l'air inquiet) : Certains pensent… que c'est l'Empereur Vilmar II. "
            "Mon village a toujours été en froid avec l'Empire. Peut-être qu'ils nous punissent.", 
            font, clock, sprite_ayela
            )
            display_dialogue_with_sprite(screen, 
            "Aldric (soupirant, esquissant un sourire amer) : Qui n'est pas en froid avec l'Empire ?", 
            font, clock, sprite_aldric
            )
            display_dialogue_with_sprite(screen, 
            "Ayela : Hm...Tout l'empire est en ruine...Quel gachis..", 
            font, clock, sprite_ayela
            )
            display_dialogue_with_sprite(screen, 
            "Aldric (calme mais direct) : Tu espères pouvoir sauver ton village, c'est ça ?", 
            font, clock, sprite_aldric
            )
            display_dialogue_box(screen, 
            "Ayela hoche doucement la tête. Ses yeux humides reflètent la lumière tremblante des torches, mais elle s'efforce de retenir ses larmes.", 
            font, clock
            )
            display_dialogue_with_sprite(screen, 
            "Ayela (à voix basse) : C'était stupide, je le sais...Aldric...J'ai peur de mourir..", 
            font, clock, sprite_ayela
            )

    # Options de réponse pour Ayela
            display_dialogue_box(screen, "Que dites-vous à Ayela ?", font, clock)
            options_ayela = [
            ("Ce n'est pas stupide. Tu fais ce que tu peux.", 5),
            ("Les chances sont faibles. Ne te fais pas d'illusions.", -10)
            ]
            choix_ayela = display_choices_box(screen, font, options_ayela, clock)

    # Branches des réponses
            if choix_ayela == 0:  # Réponse : Ce n'est pas stupide
                hero.get_relation("Ayela").adjust_score(10)
                display_dialogue_box(screen, 
                "Ayela lève les yeux vers vous, rougissante et légèrement surprise par votre réponse.(Ayela +10)", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Ayela (d'une voix tremblante) : Tu crois ? Mais… Et si je meurs ?", 
                font, clock, sprite_ayela
                )
                display_dialogue_box(screen, 
                "Elle détourne à nouveau le regard, jouant nerveusement avec la corde de son arc.", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Ayela (souffle un rire nerveux) : Je suis tellement idiote parfois…", 
                font, clock, sprite_ayela
                )
                display_dialogue_box(screen, 
                "Aldric s'approche et pose doucement sa main sur son épaule, parlant d'une voix posée.", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Aldric : Tu es une fille bien. Peu de gens risqueraient leur vie pour les autres. "
                "Si tu meurs dans cette tour… alors meurs en sachant que tu auras tout fait pour ceux que tu aimes. C'est ce qui compte.", 
                font, clock, sprite_aldric
                )
                display_dialogue_box(screen, 
                "Ayela cligne des yeux plusieurs fois, essayant de retenir ses larmes avant de vous adresser un sourire discret.", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Ayela (rougissant légèrement) : Aldric… Merci…", 
                font, clock, sprite_ayela
                )
                display_dialogue_box(screen,
                "Vous Vous eloigner..",                     
                font, clock)

            elif choix_ayela == 1:  # Réponse : Les chances sont faibles
                hero.get_relation("Ayela").adjust_score(-15)
                display_dialogue_box(screen, 
                "Ayela baisse brusquement la tête, ses épaules s'affaissant sous le poids de vos mots.(Ayela -15)", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Ayela (voix brisée) : J'avais déjà pas le moral… mais là… merci Aldric…", 
                font, clock, sprite_ayela
                )
                display_dialogue_box(screen, 
                "Elle se détourne sans ajouter un mot, s'isolant un peu plus loin, essuyant une larme discrète du revers de sa main.", 
                font, clock
                )
                display_dialogue_box(screen,
                "Vous Vous eloigner..",                     
                font, clock)


    # Supprimer le personnage des interactions après discussion
        interactions.pop(choix_index)

# Fin des interactions
    display_dialogue_box(screen, "Vous avez discuté avec tout le monde.", font, clock)
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/porte4.webp", WIDTH, HEIGHT)
    # Clôture de l'étage 4
    display_dialogue_box(screen, 
        "Plus tard dans la soirée, une violente altercation éclate entre plusieurs participants. "
        "Les cris résonnent dans la salle sombre, étouffés par l'épaisseur des murs de pierre. "
        "Lorsque tout redevient silencieux, quatre corps sans vie jonchent le sol, leurs visages figés dans l'horreur. "
        "Qu'ils soient morts par ivresse ou par cupidité, leur sort est désormais lié à la tour.", 
        font, clock
    )

    display_dialogue_box(screen, 
        "La porte s’ouvre lentement après cela. Le prix de l’étage… a été payé.", 
        font, clock
    )

    display_dialogue_box(screen, 
        "Un vent glacial s'engouffre dans la salle lorsque la porte s'entrouvre, comme si la tour elle-même "
        "se nourrissait de la tragédie humaine. L'obscurité de l'étage suivant semble plus pesante encore.", 
        font, clock
    )

    # Dialogue - Réactions des personnages
    display_dialogue_with_sprite(screen, 
        "Kael (murmurant, observant les corps) : 4 vies pour ouvrir la porte de l'étage 4.. L’énigme était littérale. La tour ne plaisante pas.", 
        font, clock, sprite_kael
    )

    display_dialogue_box(screen, 
        "Aldric fixe la porte ouverte, un voile d’inquiétude passant brièvement dans ses yeux. "
        "L'air paraît plus lourd, chargé d'un sentiment qu'il n'arrive pas à chasser.", 
        font, clock
    )

    display_dialogue_with_sprite(screen, 
        "Aldric (à voix basse, presque pour lui-même) : La tour... j’ai l’impression qu’elle veut dévorer nos âmes... nos vies... "
        "C’est donc ça le prix de la cupidité ?", 
        font, clock, sprite_aldric
    )

    display_dialogue_box(screen, 
        "Garen détourne le regard des corps, serrant nerveusement ses poigts. "
        "Ses mains tremblent légèrement, mais il garde le silence.", 
        font, clock
    )
    # Début des interactions
    display_dialogue_with_sprite(screen, 
    "Garen (voix basse, hésitant) : C’est pas de la cupidité... c’est...", 
    font, clock, sprite_garen
    )

    display_dialogue_box(screen, 
    "Kael éclate d’un rire bref et amer, ses yeux reflétant une lassitude grandissante.", 
    font, clock
    )

    display_dialogue_with_sprite(screen, 
    "Kael (ricanant) : Ah oui ? Et c’est quoi alors ? On n’est pas là pour apprendre à traire les vaches, paysan !", 
    font, clock, sprite_kael
    )

    display_dialogue_box(screen, 
    "Garen lève les yeux vers Kael, mais les mots restent coincés dans sa gorge. "
    "Ses épaules s'affaissent légèrement, incapable de trouver une réponse.", 
    font, clock
    )

    display_dialogue_with_sprite(screen, 
    "Ayela (croisant les bras, lançant un regard à Garen) : Kael a raison, Garen…", 
    font, clock, sprite_ayela
    )

    display_dialogue_box(screen, 
    "Ayela détourne rapidement les yeux, consciente de la cruauté des mots, mais incapable de les retirer. "
    "Ils doivent avancer. Les morts sont déjà derrière eux.", 
    font, clock
    )

    display_dialogue_with_sprite(screen, 
    "Garen (baisse la tête, ses doigts se crispant sur sa ceinture) : Trop de gens meurs...", 
    font, clock, sprite_garen
    )

# Transition vers l'étage suivant
    display_dialogue_box(screen, 
    "Le silence s'étire, seulement brisé par le grincement de la porte qui s'ouvre complètement. "
    "La bande franchit la porte, pleine de doutes mais aussi de motivation pour affronter l’étage 5.", 
    font, clock
    )

# Clotaire, Velm et Brando entrent en scène
    display_dialogue_box(screen, 
    "Alors que le calme semble revenir, Clotaire s'avance lentement, suivi de Velm et Brandio. "
    "Leur démarche est décontractée, mais leurs yeux scrutent les environs avec une lueur dangereuse.", 
    font, clock
    )

    display_dialogue_with_sprite(screen, 
    "Clotaire (avec un sourire en coin) : Eh bien, certains n’ont pas su contenir leur soif de sang… Dommage pour eux, "
    "mais au moins la porte s'est ouverte, n’est-ce pas ?", 
    font, clock, sprite_clotaire
    )

    display_dialogue_with_sprite(screen, 
    "Velm (souriant narquoisement) : Ils ont voulu jouer aux héros. La tour n’aime pas ce genre de personne, c'est bien connu !", 
    font, clock, sprite_velm
    )

    display_dialogue_with_sprite(screen, 
    "Brandio (calme, regard sombre) : Alimenter leur differents pour les faire s'entretuer, c'etait bien vu dame Emphyr !", 
    font, clock, sprite_brandio
    )
    
    display_dialogue_with_sprite(screen, 
    "Emphyr (avec un regard futé) : Le prix de l'etage, quand la tour parle de prix c'est forcément en terme d'àme.", 
    font, clock, sprite_emphyr
    )

    display_dialogue_with_sprite(screen, 
    "Ayela (fronçant les sourcils) : C'était vous, n'est-ce pas ? Vous les avez poussés à se battre.", 
    font, clock, sprite_ayela
    )

    display_dialogue_with_sprite(screen, 
    "Clotaire (haussement d'épaules) : Je n’ai rien fait. Ils ont choisi leur destin.", 
    font, clock, sprite_clotaire
    )

    display_dialogue_box(screen, 
    "Son regard croise celui d'Aldric, un éclat de défi dans les yeux.", 
    font, clock
    )

    display_dialogue_with_sprite(screen, 
    "Kael (serrant les poings) : Tss... Évidemment.", 
    font, clock, sprite_kael
    )

# Interaction entre Emphyr et Kael
    display_dialogue_with_sprite(screen, 
    "Emphyr (caressant le cou de Kael) : Hm détends-toi, sans ça la grille ne se serait pas ouverte...puis il serait mort à la prochaine salle de toute façon..", 
    font, clock, sprite_emphyr
    )

# Garen mal à l’aise
    display_dialogue_with_sprite(screen, 
    "Garen (visiblement mal à l’aise) : On aurait pu les arrêter…", 
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen, 
    "Emphyr : Un conseil... Laisse ta pitié à cet étage, Garen ! Car sinon à un moment donné ça va te coûter cher !", 
    font, clock, sprite_emphyr
    )

    display_dialogue_with_sprite(screen, 
    "Garen (rougissant) : Mais je...", 
    font, clock, sprite_garen
    )
    
    # Dialogue de Brando
    display_dialogue_with_sprite(screen, 
    "Brando (calmement) : Tu te serais fait tuer, paysan. Crois-moi, la tour n’a pas de place pour la pitié. C'est déjà un miracle que tu sois si haut.", 
    font, clock, sprite_brandio
    )

# Dialogue de Clotaire
    display_dialogue_with_sprite(screen, 
    "Clotaire (calmement, s'éloignant) : Les faibles tomberont comme toi, paysan. La tour nous façonne à sa manière. Il est temps que vous vous en rendiez compte.", 
    font, clock, sprite_clotaire
    )
    # Options de réponse pour Aldric
    display_dialogue_box(screen, "Comment réagissez-vous ?", font, clock)
    options_reponse = [
    ("Prendre le parti de Garen", -5, "Clotaire", -5, "Velm", -5, "Brandio"),
    ("Défendre Clotaire", +10, "Clotaire", +10, "Velm", +10, "Brandio"),
    ("Pragmatique, soutenir Emphyr", 0, None, 0, None, 0, None)
    ]
    choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_reponse], clock)

# Conséquences des choix
    if choix == 0:  # Prendre le parti de Garen
        hero.get_relation("Garen").adjust_score(+5)
        hero.get_relation("Clotaire").adjust_score(-5)
        hero.get_relation("Velm").adjust_score(-5)
        hero.get_relation("Brandio").adjust_score(-5)
        display_dialogue_with_sprite(screen, 
        "Aldric (ferme) : Garen est quelqu'un de juste. Tout le monde mérite une chance, même dans cette tour.", 
        font, clock, sprite_aldric
        )
        display_dialogue_box(screen, 
        "Clotaire et ses alliés vous lancent un regard méprisant, mais Garen semble regagner un peu de confiance.", 
        font, clock
        )
        display_dialogue_with_sprite(screen, 
        "Clotaire : Ohh tu defend la veuve et l'orphelin...comme c'est mignon, les mercenaires font ca maintenant ?", 
        font, clock, sprite_clotaire
        )
        display_dialogue_with_sprite(screen, 
        "Aldric (avec un regard assassin) : Pas que..On fait plein d'autres trucs aussi..", 
        font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen, 
        "Clotaire (calmement, s'éloignant) : Relax blondinet ! Relax...(Clotaire, Velm, Brandio -5, Garen +5)", 
        font, clock, sprite_clotaire
        )

    elif choix == 1:  # Défendre Clotaire
        hero.get_relation("Clotaire").adjust_score(+10)
        hero.get_relation("Velm").adjust_score(+10)
        hero.get_relation("Brandio").adjust_score(+10)
        display_dialogue_with_sprite(screen, 
        "Aldric (regardant Clotaire) : Il a raison, Garen. La tour ne pardonne pas. Si tu veux survivre, tu dois accepter ça.", 
        font, clock, sprite_aldric
        )
        display_dialogue_box(screen, 
        "Clotaire est visiblement surpris par vos paroles, mais il incline légèrement la tête en signe de respect.", 
        font, clock
        )
        display_dialogue_with_sprite(screen, 
        "Clotaire (calmement, s'éloignant) : Comme quoi, tout arrive ! Tu remonte dans estime blondinet, je reconnais bien la le mercenaire en toi !", 
        font, clock, sprite_clotaire
        )
        display_dialogue_with_sprite(screen, 
        "Aldric (avec un regard assassin) : T'habitue pas trop, tu avais raison c'est tout.(Clotaire, Velm, Brandio +10)", 
        font, clock, sprite_kael
        )

    elif choix == 2:  # Soutenir Emphyr
        hero.get_relation("Garen").adjust_score(5)
        hero.get_relation("Emphyr").adjust_score(10)
        display_dialogue_with_sprite(screen, 
        "Aldric (pragmatique) : Ce qu'ils disent est dur, Garen, mais Emphyr a raison. Vu leur carrure, ils n'auraient surement pas passé la prochaine salle.", 
        font, clock, sprite_aldric
        )
        display_dialogue_box(screen, 
        "Garen hoche la tête, bien qu'il semble touché par vos paroles. Emphyr s'approche pour lui donner une tape amicale sur l'épaule.", 
        font, clock
        )
        display_dialogue_with_sprite(screen, 
        "Emphyr (essayant de détendre l'atmosphère) : Allez, Garen, relève la tête. On a tous nos moments de faiblesse, mais c'est pas ça qui nous définit.", 
        font, clock, sprite_emphyr
        )
        display_dialogue_box(screen, 
        "Un léger sourire traverse le visage de Garen, qui semble retrouver un peu d'énergie.(Emphyr +10, Garen +5)", 
        font, clock
        )

# Narration - Clotaire disparaît
    display_dialogue_box(screen, 
    "Aldric observe Clotaire disparaître dans l’ombre. La porte reste ouverte, mais la salle est plus silencieuse que jamais. "
    "Le poids des pertes pèse lourdement sur les épaules des survivants.", 
    font, clock
    )
    
    
    fade_out_music(fade_duration=4000)
    fade_in_text(screen, "Fin du Chapitre 5 - Il reste 35 participants sur 99 et 95 étages", font, (WIDTH // 2, HEIGHT // 2), duration=2000)
    fade_out_text(screen, 1000)
    game_menu(screen, font, clock, WIDTH, HEIGHT, hero)
    
def chapitre_6(hero, screen, font, clock,sprites):
    
    global background
    
    sprites = load_sprites()

    sprite_aldric = sprites["Aldric"]
    sprite_garen = sprites["Garen"]
    sprite_mysterieux = sprites["Homme_mysterieux"]
    sprite_kael = sprites["Kael"]
    sprite_brandio = sprites["Brandio"]
    sprite_archeon = sprites["Archeon"]
    sprite_ayela = sprites["Ayela"]
    sprite_clotaire = sprites["Clotaire"]
    sprite_durnir = sprites["Durnir"]
    sprite_emphyr = sprites["Emphyr"]
    sprite_gallius = sprites["Gallius"]
    sprite_velm = sprites["Velm"]
    sprite_yohna = sprites["Yohna"]
    sprite_zyn = sprites["Zyn"]
    sprite_random_participant = sprites["Participant"]
    sprite_creature = sprites["Creature"]
    
    fade_in_music("graphics/resources/music/study.mp3", max_volume=0.2, fade_duration=1000)
    clear_screen(screen)
    fade_in_text(screen, 
             "Chapitre 6 : Nous ne sommes que des pions - Etage 5/99", 
             font, 
             (WIDTH // 2, HEIGHT // 2),  # Centré sur l'écran
             duration=3000)
    fade_out_text(screen, 3000, fade_speed=2)
    pygame.time.wait(1000)
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/escalier5.webp", WIDTH, HEIGHT)
    
    # Description de l'arrivée dans la salle
    display_dialogue_box(screen,
    "Le cœur est lourd tandis que vous pénétrez dans la salle du cinquième étage. "
    "Devant vous, un plateau de pierre s'étend à perte de vue, divisé en dalles semblables à un gigantesque échiquier. "
    "Cependant, contrairement aux jeux que vous connaissez, celui-ci est différent…,"
    "Des torches de flammes vertes éclairent la salle, projetant des ombres sinistres sur les murs. "
    "Au fond, perchées sur des piédestaux, des statues de gargouilles de bronze observent silencieusement la scène.",
    font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/dalle5.webp", WIDTH, HEIGHT)
# Réactions initiales des personnages
    display_dialogue_with_sprite(screen,
    "Kael (pince son menton en fixant le plateau) : Voilà qui sort de l'ordinaire… Je déteste déjà cet étage.",
    font, clock, sprite_kael
    )
    display_dialogue_with_sprite(screen,
    "Garen (les yeux plissés, sourire nerveux) : Attendez… Ce damier...ca me dit quelque chose..ca me rappel un jeu d'enfance.",
    font, clock, sprite_garen
    )
    display_dialogue_with_sprite(screen,
    "Ayela (serrant la corde de son arc, inquiète) : Je doute que ce soit aussi simple qu'un jeu d'enfants, Garen.",
    font, clock, sprite_ayela
    )

# Apparition d'Archeon
    display_dialogue_box(screen,
    "Un léger souffle balaie la salle.",
    font, clock
    )
    display_dialogue_with_sprite(screen,
    "Perché sur une passerelle de pierre en hauteur, une silhouette familière apparaît. "
    "Archeon, baigné par la lumière des torches, arbore un sourire charmeur. "
    "Son long manteau noir flotte tandis qu'il marche lentement et s'arrête au centre de la passerelle, bras croisés.",
    font, clock, sprite_archeon
    )
    display_dialogue_with_sprite(screen,
    "Archeon (calme) : Je vous félicite d'être arrivés jusqu'ici. Peu de candidats franchissent le seuil du cinquième étage…",
    font, clock, sprite_archeon
    )
    display_dialogue_with_sprite(screen,
    "Ayela (voix basse, tremblante) : Chaque fois qu'il apparaît, c'est pour annoncer une nouvelle façon de mourir…",
    font, clock, sprite_ayela
    )
    display_dialogue_with_sprite(screen,
    "Archeon (souriant) : Mais ne vous méprenez pas. Ce n'est pas un cadeau.",
    font, clock, sprite_archeon
    )

# Explication des règles
    display_dialogue_with_sprite(screen,
    "Archeon : Vous devez former des équipes de sept. Le but est simple : atteindre la dalle rouge dans le camp adverse. Voici les règles",
    font, clock, sprite_archeon
    )
    display_dialogue_box(screen,
    "• Formez des équipes de sept joueurs. "
    "• L'objectif est de traverser le plateau et d'atteindre la dalle rouge dans le camp adverse. "
    "• Chaque joueur peut avancer de 1, 2 ou 3 cases vers l'avant ou sur le côté. ",
    font, clock
    )
    display_dialogue_box(screen,
    "• Si un joueur avance de deux cases sur le côté, le dernier personnage ayant avancé recule d'une case. "
    "• Chaque mouvement réduit le nombre de cases que peut parcourir le joueur suivant. "
    "Exemple : Si un joueur avance de 3 cases, le suivant de son équipe doit passer son tour. ",
    font, clock
    )
    
    display_dialogue_with_sprite(screen,
    "Archeon (voix sombre) : Ces statues de bronze ne sont pas que des pions… ce sont vos adversaires. "
    "Elles avancent avec les mêmes règles que vous.",
    font, clock, sprite_archeon
    )

# Clotaire s'impose
    display_dialogue_box(screen,
    "Avant que vous ne puissiez rassembler vos alliés pour former une équipe de 7, une voix forte s'élève au-dessus des autres.",
    font, clock
    )
    display_dialogue_with_sprite(screen,
    "Clotaire (d’une voix narquoise) : Nous serons avec eux. Ahah !",
    font, clock, sprite_clotaire
    )
    display_dialogue_with_sprite(screen,
    "Kael (serrant les dents) : Sérieusement… ? Ce type…",
    font, clock, sprite_kael
    )

# Réaction d'Archeon
    display_dialogue_with_sprite(screen,
    "Archeon (regardant Aldric) :Parfait ! Alors vous serez les premiers à jouer !",
    font, clock, sprite_archeon
    )
# Réactions des personnages
    display_dialogue_with_sprite(screen,
    "Kael (murmurant à Aldric) : Ce type est un parasite…",
    font, clock, sprite_kael
    )
    display_dialogue_with_sprite(screen,
    "Aldric (avec un regard serieux) : Plus pour longtemps, Va falloir s'en debarasser et vite !",
    font, clock, sprite_aldric
    )
    display_dialogue_with_sprite(screen,
    "Kael : Aldric...",
    font, clock, sprite_kael
    )
    display_dialogue_box(screen,
    "Aldric et son équipe prennent place sur le damier. Les regards sont tendus, chacun sent le poids de l'épreuve qui les attend.",
    font, clock
    )
    display_dialogue_with_sprite(screen,
    "Archeon (claquant des doigts) : Que la partie commence.",
    font, clock, sprite_archeon
    )
    display_dialogue_box(screen,
    "Phase 1 : Début de partie : Premier Mouvement d'Aldric et son équipe",
    font, clock
    )

    display_dialogue_box(screen,
    "Vous vous positionnez sur la ligne de départ. En face, les gargouilles restent immobiles, mais vous sentez "
    "leurs yeux d’acier braqués sur vous.",
    font, clock
    )
    display_dialogue_with_sprite(screen,
    "Garen (confiant, souriant) : C'est l'imperius Dex, mon frère et moi y jouions ensemble !",
    font, clock, sprite_garen
    )

    display_dialogue_box(screen,
    "Les équipes prennent place sur les premières rangées du plateau. L'écho de vos pas résonne dans la salle silencieuse. "
    "De l'autre côté, les gargouilles de bronze fixent leur piédestal, mais leur menace est palpable.",
    font, clock
    )
    display_dialogue_with_sprite(screen,
    "Kael (regard noir à Clotaire) : T’as intérêt à pas nous foutre dedans…",
    font, clock, sprite_kael
    )
    display_dialogue_with_sprite(screen,
    "Clotaire (souriant en coin) : Détends-toi, noble. Ce n’est qu’un jeu.",
    font, clock, sprite_clotaire
    )
    display_dialogue_with_sprite(screen,
    "Ayela (murmure, anxieuse) : Ce jeu va nous tuer si on ne fait pas attention…",
    font, clock, sprite_ayela
    )
    display_dialogue_with_sprite(screen,
    "Garen (sérieux) : Je connais bien ce jeu. Si on suit un rythme stable, on peut traverser sans perdre personne.",
    font, clock, sprite_garen
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/Archeon.webp", WIDTH, HEIGHT)
# Archeon - Déclaration de début de partie
    display_dialogue_with_sprite(screen,
    "Archeon (depuis la passerelle) : Rappelez-vous… seuls ceux qui atteignent la dalle rouge survivront.",
    font, clock, sprite_archeon
    )
    display_dialogue_with_sprite(screen,
    "Archeon (ton froid) : Et si une gargouille atteint une dalle rouge avant vous… un joueur sera sacrifié.",
    font, clock, sprite_archeon
    )

    display_dialogue_box(screen,
    "Un silence pesant s'installe dans la salle. Lentement, les participants prennent place sur leur dalles respectives."
    "Le contact froid de la pierre sous vos pieds semble vouloir aspirer toute votre énergie. "
    "Face à vous, les statues de gargouilles restent figées, mais leur présence est écrasante. Chaque battement de cœur résonne comme un écho dans cette immense arène.",
    font, clock
    )
    display_dialogue_box(screen,
    "Archeon observe la scène depuis la passerelle, son regard perçant ne laissant rien passer. Un léger rictus effleure ses lèvres. "
    "Il lève lentement la main, marquant l'instant où tout basculera. Puis, dans un geste sec, sa main s'abaisse.",
    font, clock
    )
    display_dialogue_with_sprite(screen,
    "Archeon (voix forte) : Que le jeu commence !!!",
    font, clock, sprite_archeon
    )
    display_dialogue_box(screen, 
    "Au même moment, des grilles se lèvent, entourant et enfermant les joueurs au sein du damier. "
    "Le bruit métallique résonne dans toute la salle, amplifiant la gravité de la situation. "
    "Les joueurs échangent des regards, certains empreints de détermination, d'autres d'inquiétude.", 
    font, clock
    )

# Transition musicale et visuelle
    fade_out_music(fade_duration=1000)
    fade_in_music("graphics/resources/music/Eldrvak.mp3", max_volume=0.2, fade_duration=1000)
    background = fade_in_background(screen, "graphics/resources/backgrounds/dalle4.webp", WIDTH, HEIGHT)

    # Narration d'ambiance
    display_dialogue_box(screen, 
    "La lumière violette des torches vacille sur les murs de pierre, projetant des ombres qui dansent sur le damier. "
    "Chaque dalle semble chargée d’une énergie ancienne et menaçante, comme si elle observait les joueurs. "
    "Le silence est brisé par le craquement des bottes sur les pierres froides et les respirations lourdes des participants.", 
    font, clock
    )

    # Premiers échanges d'Aldric et Garen
    display_dialogue_with_sprite(screen, 
    "Aldric : Je prends la main !", 
    font, clock, sprite_aldric
    )
    display_dialogue_with_sprite(screen, 
    "Garen : Fais attention Al' ! Ce n'est pas un jeu de course, analyse bien le damier.", 
    font, clock, sprite_garen
    )
    display_dialogue_with_sprite(screen, 
    "Aldric (levant le pouce avec un sourire) : T'en fais pas Garen !", 
    font, clock, sprite_aldric
    )

    # Ajout de narration après les échanges
    display_dialogue_box(screen, 
    "Alors qu'Aldric se prépare à faire son premier mouvement, le silence devient oppressant. "
    "Les regards des autres joueurs se tournent vers lui, certains curieux, d’autres méfiants. "
    "Les gargouilles immobiles au fond du plateau semblent elles aussi le fixer, comme prêtes à bondir au moindre faux pas.", 
    font, clock
    )

    # Clôture de la narration initiale
    display_dialogue_box(screen, 
    "Le premier tour commence, et le damier devient un terrain de stratégie et de survie. "
    "Chaque mouvement est crucial, chaque décision peut sceller le destin des joueurs. "
    "La tension est palpable, et la tour semble se réjouir de cette nouvelle épreuve.", 
    font, clock
)

# Pensée d'Archeon
    display_dialogue_box(screen,
    "Archeon, du haut de la passerelle, fixe Aldric avec un sourire en coin.",
    font, clock
    )
    def premier_mouvement(hero, screen, font, clock, sprites):
    # Afficher le choix initial
        display_dialogue_box(screen, 
        "Vous vous tenez devant la première rangée. Comment souhaitez-vous avancer ?", 
        font, clock
        )

    # Options de mouvement
        options_mouvement = [
        ("Avancer d'une case (prudent).", +5, "Kael"),
        ("Avancer de deux cases (équilibré).", +5, "Garen"),
        ("Avancer de trois cases (risqué).", -10, "Kael", +5, "Clotaire")
        ]

        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_mouvement], clock)

    # Branches pour chaque choix
        if choix == 0:  # Avancer d'une case (prudent)
            display_dialogue_with_sprite(screen, "Kael (hochant la tête) : Prudent. Tu joues la sécurité.", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Aldric : Pas le choix.", font, clock, sprite_aldric)
            display_dialogue_with_sprite(screen, "Clotaire : Peu importe, c'est à moi !", font, clock, sprite_clotaire)
            display_dialogue_with_sprite(screen, "Ayela (regardant autour) : Mmh, on reste groupés. Ça devrait aller.", font, clock, sprite_ayela)
            display_dialogue_with_sprite(screen, "Velm (amusé) : Toujours à jouer la prudence… ça va pas nous faire avancer vite.", font, clock, sprite_velm)
            display_dialogue_with_sprite(screen, "Brandio (calme) : Moins vite mais en vie. C'est ça l'idée.", font, clock, sprite_brandio)
            display_dialogue_with_sprite(screen, 
            "Clotaire (ironique) : Ah, l’éternel Brandio et sa philosophie… Velm, oublie pas de leur mettre trois cases dans les dents, ahah !(Kael +5)", 
            font, clock, sprite_clotaire
        )
            hero.get_relation("Kael").adjust_score(+5)

        elif choix == 1:  # Avancer de deux cases (équilibré)
            display_dialogue_with_sprite(screen, "Garen (souriant) : Bonne stratégie. Restons sur ce rythme.", font, clock, sprite_garen)
            display_dialogue_with_sprite(screen, "Clotaire : À moi, paysan ! 3 cases !", font, clock, sprite_clotaire)
            display_dialogue_with_sprite(screen, "Kael : Enflure ! Tssss.", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Velm : Alors on fait du surplace ? Muahahah !", font, clock, sprite_velm)
            display_dialogue_with_sprite(screen, "Ayela : À moi ! J'avance de trois cases ! Alors, qui fait du surplace maintenant ?", font, clock, sprite_ayela)
            display_dialogue_with_sprite(screen, "Brandio : Salope !", font, clock, sprite_brandio)
            display_dialogue_with_sprite(screen, "Kael (soupirant) : Je te jure… cette bande de guignols...", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Aldric (fixant Velm) : Arrête de provoquer, tu ferais mieux de te concentrer.", font, clock, sprite_aldric)
            display_dialogue_with_sprite(screen, "Velm (ricane) : Allez, je plaisante. On va s'en sortir… ou pas.", font, clock, sprite_velm)
            display_dialogue_with_sprite(screen, "Garen (léger stress) : Restez attentifs. On avance trop vite à mon goût…", font, clock, sprite_garen)
            display_dialogue_with_sprite(screen, 
            "Clotaire (calme) : L'avance est l'avantage, Garen. Mais bon… on verra. Si tu préfères le surplace et meurs, ça m'est égal.(Garen +5)", 
            font, clock, sprite_clotaire
            )
            hero.get_relation("Garen").adjust_score(+5)

        elif choix == 2:  # Avancer de trois cases (risqué)
            display_dialogue_with_sprite(screen, "Kael (furieux) : Tu veux nous faire tuer ?", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Aldric : Je sais ce que je fais !", font, clock, sprite_aldric)
            display_dialogue_with_sprite(screen, "Kael : J'ai pas envie de crever, pas si près du but, t'entends !", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Garen : Ça va le faire ! Ça va le faire...", font, clock, sprite_garen)
            display_dialogue_with_sprite(screen, "Ayela (chuchotant à Aldric) : T'es sûr ? Ces gargouilles vont pas nous laisser passer.", font, clock, sprite_ayela)
            display_dialogue_with_sprite(screen, "Brandio (avançant derrière) : Si elles bougent, on s'en occupe.", font, clock, sprite_brandio)
            display_dialogue_with_sprite(screen, "Clotaire (sarcastique) : Brandio en héros, là je te reconnais.", font, clock, sprite_clotaire)
            display_dialogue_with_sprite(screen, "Garen (calmant Ayela) : On est ensemble. On avance tous.", font, clock, sprite_garen)
            display_dialogue_with_sprite(screen, 
            "Velm (regard vers la dalle rouge) : Peu importe… ils n'attaqueront pas tant qu'on n'est pas trop proches.", 
            font, clock, sprite_velm
            )
            display_dialogue_with_sprite(screen, "Ayela (grimace) : J'espère que tu dis vrai.(Kael -10, Clotaire +5)", font, clock, sprite_ayela)
            hero.get_relation("Kael").adjust_score(-10)
            hero.get_relation("Clotaire").adjust_score(+5)

# Appel de la fonction
    premier_mouvement(hero, screen, font, clock, sprites)
    
    display_dialogue_box(screen, 
        "Phase 2 : Mouvement des Gargouilles", 
        font, clock
    )
    display_dialogue_box(screen, 
    "Deux gargouilles de bronze avancent en miroir à votre progression, se déplaçant de 2 cases. "
    "Elles se rapprochent lentement, prêtes à bloquer votre avancée.", 
    font, clock
    )
# Narration de la tension
    display_dialogue_box(screen, 
    "Leur mouvement est précis, mécanique, mais empreint d’une menace palpable. "
    "Chaque pas résonne sur le damier, amplifiant l’impression que ces créatures de bronze ne sont pas de simples pions. "
    "Elles semblent dotées d’une volonté propre, comme si elles analysaient vos mouvements.", 
    font, clock
    )
    display_dialogue_with_sprite(screen, "Ayela (murmurant) : Elles bougent… C’est comme si elles attendaient qu’on se rapproche.", font, clock, sprite_ayela)
    display_dialogue_with_sprite(screen, "Kael (sarcastique) : Logique. Elles veulent nous voir tomber un à un.", font, clock, sprite_kael)
    display_dialogue_with_sprite(screen, "Garen (inquiet) : Elles avancent vite… Trop vite.", font, clock, sprite_garen)
    display_dialogue_with_sprite(screen, "Brandio (fixant les gargouilles) : On dirait qu’elles anticipent nos mouvements.", font, clock, sprite_brandio)
    display_dialogue_with_sprite(screen, "Velm (amusé) : Oh, allez… Elles ne font que se dégourdir les jambes.", font, clock, sprite_velm)
    display_dialogue_with_sprite(screen, "Ayela (regard noir à Velm) : Tu trouves ça drôle ? Elles pourraient nous tuer à tout moment.", font, clock, sprite_ayela)
    display_dialogue_with_sprite(screen, 
        "Clotaire (calme) : Elles suivent les règles du jeu. Rien de plus. Il suffit de ne pas paniquer. Ok, beauté ? (simule un baiser avec sa bouche)", 
        font, clock, sprite_clotaire
    )
    display_dialogue_with_sprite(screen, "Kael (grognant) : C’est facile à dire… Jusqu’à ce que tu sois la cible. Si c'est toi, ça ne me dérangerait pas.", font, clock, sprite_kael)
    display_dialogue_with_sprite(screen, 
        "Aldric (posant la main sur son épée) : Restons concentrés. Tant qu’on garde notre formation, on a une chance. Sinon, sacrifions ces trois guignols.", 
        font, clock, sprite_aldric
    )
    display_dialogue_with_sprite(screen, 
        "Velm (ricanant) : Enfoiré ! On est dans la même équipe ! On verra si ta 'formation' te sauve quand elles te fonceront dessus.", 
        font, clock, sprite_velm
    )
    display_dialogue_with_sprite(screen, "Garen (fixant Velm) : Tu devrais moins parler et plus regarder où tu mets les pieds si tu veux vivre.", font, clock, sprite_garen)
    display_dialogue_with_sprite(screen, 
        "Brandio (avançant d’un pas lent) : Elles n’attaquent pas encore. Profitons-en pour avancer avec précipitation, Clotaire !", 
        font, clock, sprite_brandio
    )
    display_dialogue_with_sprite(screen, "Ayela (hochant la tête) : L'enflure, il a avancé de trois cases… Je fais du surplace… grrrrrrrrr.", font, clock, sprite_ayela)
   
    def kael_mouvement(hero, screen, font, clock, sprites):
        display_dialogue_box(screen, 
        "Kael se tient sur une dalle, hésitant sur son prochain mouvement. "
        "Devant lui, une gargouille bloque le passage à deux cases, "
        "tandis qu’une autre semble se déplacer en miroir de son prochain pas. "
        "Il sait que chaque mouvement pourrait affecter le reste de l’équipe. "
        "L’avancée prudente pourrait préserver leurs forces, mais ralentir leur progression. "
        "Un mouvement plus audacieux pourrait créer une ouverture, mais aussi augmenter les risques pour les suivants.", 
        font, clock
    )

# Réactions des personnages pour orienter les choix
        display_dialogue_with_sprite(screen, 
        "Garen (fronçant les sourcils) : Kael, réfléchis bien. On ne peut pas se permettre de perdre du terrain… mais reste en vie.", 
        font, clock, sprite_garen
    )
        display_dialogue_with_sprite(screen, 
        "Ayela (inquiète) : Si tu avances trop vite, tu risques de les attirer tous les deux. Fais attention.", 
        font, clock, sprite_ayela
    )
        display_dialogue_with_sprite(screen, 
        "Velm (ricanant) : Hésite pas à passer ton tour, nobliaud. Laisse-nous régler ça à ta place.", 
        font, clock, sprite_velm
    )
        display_dialogue_with_sprite(screen, 
        "Clotaire (calme, mais incisif) : Si tu veux avancer, fais-le. Mais ne ralentis pas le reste de l’équipe.", 
        font, clock, sprite_clotaire
    )

    # Options de mouvement pour Kael
        options_kael = [
        ("Avancer de 1 case (prudence).", +5, "Kael"),
        ("Avancer de 2 cases (équilibre).", +5, "Garen"),
        ("Passer son tour.", -5, "Clotaire")
        ]
        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_kael], clock)

        if choix == 0:  # Avancer de 1 case
            display_dialogue_with_sprite(screen, "Kael (avançant prudemment) : J'avance. On reste sur ce rythme.", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Velm (ricanant derrière) : T’as peur d’une gargouille, noblieau ?", font, clock, sprite_velm)
            display_dialogue_with_sprite(screen, "Kael (jetant un regard noir) : Je ne parle pas aux crétins puants de ton espèce.", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Brandio (sec) : Suffit. Qu'il tombe ou avance, peu m'importe.", font, clock, sprite_brandio)
            display_dialogue_with_sprite(screen, "Ayela (serrant son arc) : Ignore-les, Kael… Restons concentrés.", font, clock, sprite_ayela)
            display_dialogue_with_sprite(screen, "Clotaire (en souriant) : Concentrés ? C'est une belle manière de dire 'lents'.", font, clock, sprite_clotaire)
            display_dialogue_with_sprite(screen, "Aldric : Garen ! Je fais quoi, toi qui connais le jeu ?", font, clock, sprite_aldric)
            display_dialogue_with_sprite(screen, "Garen : Un pas à droite pour faire reculer Brandio et un pas en avant.", font, clock, sprite_garen)
            hero.get_relation("Kael").adjust_score(+5)

        elif choix == 1:  # Avancer de 2 cases
            display_dialogue_with_sprite(screen, "Kael (avançant rapidement) : J'avance de deux. Suivez-moi.", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Garen (hochant la tête) : On garde la cadence. C'est bien.", font, clock, sprite_garen)
            display_dialogue_with_sprite(screen, "Velm (ironique) : Oh, comme c'est inspirant. On devrait tous écrire ça sur nos tombes.", font, clock, sprite_velm)
            display_dialogue_with_sprite(screen, "Kael (grognant) : Personne ne t'a demandé ton avis, Velm.", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Clotaire (calme) : Continue de parler, Velm. J’aime bien quand tu les distrais.", font, clock, sprite_clotaire)
            display_dialogue_with_sprite(screen, "Brandio (se rapprochant) : Les distractions coûtent cher ici…", font, clock, sprite_brandio)
            display_dialogue_with_sprite(screen, "Aldric : J'ai hâte de voir ta tête voler.", font, clock, sprite_aldric)
            hero.get_relation("Garen").adjust_score(+5)

        elif choix == 2:  # Passer son tour
            display_dialogue_with_sprite(screen, "Clotaire (ricanant) : Dommage, pauvre con. Tu vas attendre ici pendant qu’on avance. Muhaha.", font, clock, sprite_clotaire)
            display_dialogue_with_sprite(screen, "Kael (serrant les poings) : Tsss… J’vais te laisser crever devant, Clotaire.", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Velm (moqueur) : Ooooh… ça sent la frustration. Fais gaffe, noble, tu vas nous ralentir.", font, clock, sprite_velm)
            display_dialogue_with_sprite(screen, "Ayela (croisant les bras) : Laissez-le tranquille. C'est pas le moment pour vos petites querelles.", font, clock, sprite_ayela)
            display_dialogue_with_sprite(screen, "Brandio (imperturbable) : Clotaire, Velm ! Vous parlez trop… et vous avancez trop peu.", font, clock, sprite_brandio)
            display_dialogue_with_sprite(screen, "Clotaire (en avançant de trois cases) : Continuez à discuter. Moi, je gagne. En avant les gars !", font, clock, sprite_clotaire)
            display_dialogue_with_sprite(screen, "Aldric : Pas si vite.", font, clock, sprite_aldric)
            display_dialogue_with_sprite(screen, "Clotaire : Tsss fait chier une gargouille ! Tu es content de toi hein !", font, clock, sprite_clotaire)
            hero.get_relation("Clotaire").adjust_score(-5)

# Appels des fonctions
    kael_mouvement(hero, screen, font, clock, sprites)
    def clotaire_mouvement(hero, screen, font, clock, sprites):
    # Phase 4 : Avancée de Clotaire
        display_dialogue_box(screen, 
        "Phase 4 : Tour de Clotaire ", 
        font, clock
        )
        display_dialogue_box(screen, 
        "À mi-chemin, Clotaire avance de 3 cases, réduisant à zéro la marge de mouvement du joueur suivant.", 
        font, clock
        )
        display_dialogue_with_sprite(screen, "Garen (paniqué) : Hé ! Pourquoi t’avances autant ?", font, clock, sprite_garen)
        display_dialogue_with_sprite(screen, "Clotaire (calme) : Je fais ce qui est nécessaire.", font, clock, sprite_clotaire)
        display_dialogue_with_sprite(screen, "Ayela (énervée, elle bande son arc) : Enfoiré.", font, clock, sprite_ayela)
        display_dialogue_with_sprite(screen, 
        "Archeon (souriant) : Rappel… attaquer un allié est interdit.", 
        font, clock, sprite_archeon
        )

        display_dialogue_box(screen, 
        "Les gargouilles avancent lentement, suivant l'élan de Clotaire.", 
        font, clock
        )
        display_dialogue_with_sprite(screen, 
        "Velm (observant les gargouilles) : Oh, elles ont l’air de t’apprécier, Clotaire. Peut-être qu’elles vont t’escorter jusqu’à la sortie.", 
        font, clock, sprite_velm
        )
        display_dialogue_with_sprite(screen, "Kael (serrant les poings) : Il nous ralentit volontairement. C’est évident.", font, clock, sprite_kael)
        display_dialogue_with_sprite(screen, 
        "Brandio (fixant les gargouilles) : Les statues ne plaisantent pas. Elles avancent chaque fois qu’il le fait.", 
        font, clock, sprite_brandio
        )
        display_dialogue_with_sprite(screen, "Ayela (les yeux rivés sur les dalles) : On va finir par se faire coincer à ce rythme…", font, clock, sprite_ayela)
        display_dialogue_with_sprite(screen, "Garen (frustré) : Pourquoi tu fais ça ? On est censés avancer ensemble !", font, clock, sprite_garen)
        display_dialogue_with_sprite(screen, 
        "Clotaire (légèrement amusé) : Je suis ici pour gagner. Pas pour tenir la main de tout le monde.", 
        font, clock, sprite_clotaire
        )
        display_dialogue_with_sprite(screen, "Velm (murmurant à Kael) : Je commence à l’apprécier, ce Garen. Il comprend le jeu.", font, clock, sprite_velm)
        display_dialogue_with_sprite(screen, "Kael (à Velm) : Touche pas au paysan !", font, clock, sprite_kael)
        display_dialogue_with_sprite(screen, "Velm (souriant) : Il joue pour nous. Ça me plaît.", font, clock, sprite_velm)

        display_dialogue_box(screen, 
        "Les gargouilles atteignent presque votre rangée.", 
        font, clock
        )
        display_dialogue_with_sprite(screen, "Ayela (nerveuse) : Si elles avancent encore, quelqu’un va y passer…", font, clock, sprite_ayela)
        display_dialogue_with_sprite(screen, "Garen (soupirant) : On doit avancer vite… avant qu’il soit trop tard. La dalle rouge ! Elle est là !", font, clock, sprite_garen)

    # Combat d'Aldric contre une gargouille
        display_dialogue_with_sprite(screen, 
        "Aldric (faisant face à une gargouille et prenant son épée) : Dégage !", 
        font, clock, sprite_aldric
        )
        display_dialogue_box(screen, 
        "La gargouille fut tranchée en deux sans broncher.", 
        font, clock
        )
        display_dialogue_with_sprite(screen, "Clotaire : Pfiouuu ! Il rigole pas, le blondinet.", font, clock, sprite_clotaire)
        display_dialogue_with_sprite(screen, "Kael : Pas mal...", font, clock, sprite_kael)

    # Réaction d'Archeon
        display_dialogue_box(screen, 
        "Archeon observe la scène avec un rictus amusé. hm… C'est presque trop simple pour toi, pas vrai Aldric, pensa-t-il.", 
        font, clock
        )

# Appel de la fonction
    clotaire_mouvement(hero, screen, font, clock, sprites)
    def clotaire_reaction(hero, screen, font, clock, sprites):
    # Afficher le titre de la phase
        display_dialogue_box(screen, 
        "Aldric se tient sur une dalle, les yeux fixés sur le plateau devant lui. "
        "Une gargouille se trouve à trois cases, positionnée de manière à intercepter un mouvement direct. "
        "À sa gauche, une dalle semble moins surveillée, mais reculer ou hésiter pourrait ralentir le groupe. "
        "L'équipe compte sur lui pour ouvrir une voie, mais chaque choix pourrait changer le cours de la partie. "
        "Une approche prudente garantirait sa sécurité, mais un mouvement audacieux pourrait perturber les gargouilles, "
        "donnant un avantage stratégique au groupe.", 
        font, clock
    )

# Réactions des personnages pour orienter les choix
        display_dialogue_with_sprite(screen, 
        "Kael (murmurant) : Ne fais rien de stupide, Aldric. Les gargouilles sont trop proches.", 
        font, clock, sprite_kael
    )
        display_dialogue_with_sprite(screen, 
        "Ayela (observant les gargouilles) : Si tu peux les détourner, ça nous donnerait un peu d’air… mais c’est risqué.", 
        font, clock, sprite_ayela
    )
        display_dialogue_with_sprite(screen, 
        "Garen (prudemment) : Analyse bien le damier, Al'. Ce jeu ne pardonne pas les erreurs.", 
        font, clock, sprite_garen
    )
        display_dialogue_with_sprite(screen, 
        "Velm (sarcastique) : Allez, héroïque Aldric ! Montre-nous ton génie tactique.", 
        font, clock, sprite_velm
    )
    # Options de réaction face à Clotaire
        options_reaction = [
        ("Intervenir (forcer Clotaire à reculer).", -5, "Clotaire", +10, "Kael"),
        ("Laisser faire.", +5, "Clotaire", -10, "Kael"),
        ("Laisser Garen gérer.", +5, "Garen")
        ]

        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_reaction], clock)

    # Conséquences pour chaque choix
        if choix == 0:  # Intervenir
            display_dialogue_box(screen, 
            "La tension dans la salle monte d'un cran. Clotaire recule d'une case à contrecœur, "
            "obéissant à contrecœur aux règles implicites du groupe. "
            "La lumière vertes des torches vacille légèrement, comme pour souligner l'importance de chaque mouvement.", 
            font, clock
        )
            display_dialogue_with_sprite(screen, 
            "Clotaire (agacé) : Tss... Fais comme tu veux.", 
            font, clock, sprite_clotaire
            )
            display_dialogue_box(screen, 
            "Kael croise les bras, un léger sourire satisfait étirant ses lèvres. Il semble apprécier que quelqu’un mette enfin Clotaire à sa place, même si la menace des gargouilles reste palpable.", 
            font, clock
            )
            display_dialogue_with_sprite(screen, 
            "Kael (croisant les bras, satisfait) : Enfin… Quelqu’un qui sait s’imposer.", 
            font, clock, sprite_kael
        )
            display_dialogue_box(screen, 
            "Ayela esquisse un sourire rassurant, bien qu’un éclat de méfiance reste dans ses yeux. Elle sait que la moindre division dans le groupe pourrait leur coûter cher.", 
            font, clock
        )
            display_dialogue_with_sprite(screen, 
            "Ayela (souriant légèrement) : On avance ensemble ou pas du tout.", 
            font, clock, sprite_ayela
        )   

        # Transition vers les moqueries de Velm
            display_dialogue_box(screen, 
            "Derrière, Velm ricane doucement. Son ton moqueur brise momentanément la lourdeur de l’atmosphère, mais la pique qu’il lance n’échappe à personne.", 
            font, clock
        )
            display_dialogue_with_sprite(screen, 
            "Velm (ricanant doucement) : Toujours en train de jouer les héros, hein Aldric ?", 
            font, clock, sprite_velm
        )

# Brandio observe en silence, ajoutant une perspective différente
            display_dialogue_box(screen, 
            "Brandio, plus calme, observe la scène avec un air indéchiffrable. Ses paroles tranchent avec celles de Velm, exprimant une lassitude face à la longueur et à la difficulté de ce jeu.", 
            font, clock
        )
            display_dialogue_with_sprite(screen, 
            "Brandio (calme, observant) : Ce jeu commence à durer trop longtemps.", 
            font, clock, sprite_brandio
        )
            display_dialogue_box(screen, 
            "Le plateau semble s’étirer à l’infini, chaque dalle devenant une épreuve de patience et de stratégie. "
            "Les gargouilles immobiles ajoutent une tension sourde, leur silence pesant comme une menace constante.", 
            font, clock
        )
            hero.get_relation("Clotaire").adjust_score(-5)
            hero.get_relation("Kael").adjust_score(+10)

        elif choix == 1:  # Laisser faire
            display_dialogue_with_sprite(screen, "Kael (furieux) : Tu le laisses vraiment faire ça ?", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Garen (fronçant les sourcils) : On risque de perdre à ce rythme…", font, clock, sprite_garen)
            display_dialogue_with_sprite(screen, "Ayela (regard inquiet) : Les gargouilles ne nous attendront pas…", font, clock, sprite_ayela)
            display_dialogue_with_sprite(screen, "Clotaire (avec un sourire en coin) : Je fais avancer le jeu, c’est tout.", font, clock, sprite_clotaire)
            display_dialogue_with_sprite(screen, "Velm (haussement d’épaules) : Un jeu dangereux… Mais intéressant.", font, clock, sprite_velm)
            hero.get_relation("Kael").adjust_score(-10)
            hero.get_relation("Clotaire").adjust_score(+5)

        elif choix == 2:  # Laisser Garen gérer
            display_dialogue_with_sprite(screen, "Garen (souriant) : Je vais m'en sortir.", font, clock, sprite_garen)
            display_dialogue_box(screen, 
            "Garen avance et atteint la dalle rouge !", 
            font, clock
            )
            display_dialogue_with_sprite(screen, "Ayela (le rejoignant rapidement) : Bien joué, Garen. On est passés.", font, clock, sprite_ayela)
            display_dialogue_with_sprite(screen, "Kael (restant derrière) : Tch… Il nous laisse tous en plan.", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Velm (souriant) : C’est chacun pour soi. Vous le savez.", font, clock, sprite_velm)
            display_dialogue_with_sprite(screen, 
            "Brandio (immobile) : Il reste encore des dalles à franchir…", 
            font, clock, sprite_brandio
            )
            display_dialogue_box(screen, 
            "Les autres participants restent bloqués, les gargouilles avançant lentement derrière eux.", 
            font, clock
            )
            hero.get_relation("Garen").adjust_score(+5)

# Appel de la fonction
    clotaire_reaction(hero, screen, font, clock, sprites)
    

# Ajouter une narration finale pour intensifier l'atmosphère
    display_dialogue_box(screen, 
    "L’atmosphère dans la salle devient de plus en plus lourde. Chaque mouvement des joueurs est suivi de près par les gargouilles, "
    "toujours immobiles mais terriblement menaçantes. La lumière vertes des torches vacille, projetant des ombres dansantes qui semblent donner vie aux murs de pierre.", 
    font, clock
    )
    display_dialogue_box(screen, 
    "Dans ce silence oppressant, même un simple craquement de dalle résonne comme une explosion. Le groupe avance, mais l’ombre du doute et de la peur plane sur chacun.", 
    font, clock
    )

# Ambiance - Tension dans la salle
    display_dialogue_box(screen, 
    "Dans l'ombre, les autres participants, spectateurs silencieux, observent avec nervosité. "
    "Leur regard oscille entre les gargouilles de bronze, immobiles mais menaçantes, et les joueurs encore coincés sur le plateau. "
    "Certains serrent les poings, d'autres échangent des murmures étouffés. Le poids de la tension semble étouffer la pièce, "
    "comme si le moindre son pouvait réveiller une force tapie dans l'obscurité.", 
    font, clock
    )
    display_dialogue_box(screen, 
    "Un participant à l’arrière recule d’un pas, murmurant à son voisin : Ils n’y arriveront pas tous… C’est impossible.", 
    font, clock
    )
    display_dialogue_box(screen, 
    "Une femme, les bras croisés, fixe Kael et Aldric : On verra s'ils sont vraiment aussi bons qu'ils en ont l'air.", 
    font, clock
    )
    display_dialogue_box(screen, 
    "Les flammes vertes des torches vacillent faiblement, projetant des ombres mouvantes sur les murs sculptés. "
    "Chaque craquement de pierre sous le pied d'une gargouille résonne comme une menace silencieuse.", 
    font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/dalle3.webp", WIDTH, HEIGHT)
# Focus sur Archeon
    display_dialogue_box(screen, 
    "Depuis la passerelle en hauteur, Archeon observe, appuyé nonchalamment contre la rambarde de pierre. "
    "Ses yeux suivent les mouvements des joueurs, mais son regard semble s'attarder plus longuement sur Aldric et Clotaire. "
    "Un sourire discret étire ses lèvres, presque imperceptible, tandis qu'il tapote lentement ses doigts contre le rebord de la rambarde.", 
    font, clock
    )
    display_dialogue_with_sprite(screen, 
    "Archeon (murmurant, pour lui-même) : Ce groupe est intéressant… Un grand cru. "
    "Ils possèdent cette étincelle que je n'avais pas vue depuis longtemps.", 
    font, clock, sprite_archeon
    )
    display_dialogue_box(screen, 
    "Son regard s’assombrit légèrement lorsqu’il aperçoit Kael hésiter avant d’avancer. "
    "Il se redresse doucement, croisant les bras avec intérêt.", 
    font, clock
    )

# Les gargouilles continuent leur progression
    display_dialogue_box(screen, 
    "Tour des gargouilles", 
    font, clock
    )
    display_dialogue_box(screen, 
    "Les statues de bronze progressent lentement sur les dalles, réduisant l’espace entre elles et l'équipe'. "
    "Les regards se tournent vers Clotaire, qui semble toujours aussi détendu malgré la menace imminente.", 
    font, clock
    )
    display_dialogue_with_sprite(screen, 
    "Clotaire (avec un sourire) : Allons-y. Plus vite on termine, mieux c'est.", 
    font, clock, sprite_clotaire
    )
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/gargouille.webp", WIDTH, HEIGHT)
    def clotare_sacrifice(hero, screen, font, clock, sprites):
        fade_out_music(fade_duration=1000)
        
    # Phase 5 : Sacrifice Imminent
        display_dialogue_box(screen, 
        "Phase 5 : Sacrifice...", 
        font, clock
    )

        # Narration avant les dialogues
        display_dialogue_box(screen, 
            "Le groupe avance prudemment, mais l’ambiance est tendue. Garen déjà qualifié, connaissant parfaitement les règles, "
            "observe les mouvements avec une attention presque maniaque. Il remarque immédiatement le danger potentiel dans les choix de Clotaire.", 
            font, clock
        )

        display_dialogue_with_sprite(screen, 
            "Garen (sérieux, presque suppliant) : Avance d'une case, Clotaire ! Si tu fais plus, ça fera avancer la gargouille… et elle atteindra la dalle rouge !", 
            font, clock, sprite_garen
        )

        # Narration sur le mépris de Clotaire
        display_dialogue_box(screen, 
            "Clotaire, comme à son habitude, ne supporte pas qu’un paysan lui donne des ordres. Son sourire arrogant trahit son mépris, "
            "et il rejette immédiatement le conseil de Garen, convaincu de mieux savoir.", 
            font, clock
        )

        display_dialogue_with_sprite(screen, 
            "Clotaire (avec un sourire) : La ferme, paysan ! Je…", 
            font, clock, sprite_clotaire
        )

        # Narration sur l’erreur fatale
        display_dialogue_box(screen, 
            "Sans écouter, Clotaire avance de trois cases d’un pas assuré. Mais à peine sa botte touche la troisième dalle, "
            "un bruit mécanique sinistre se fait entendre. Une gargouille, en réponse à son mouvement, avance brutalement de trois cases, "
            "atteignant une dalle rouge. La salle semble retenir son souffle.", 
            font, clock
        )

        display_dialogue_with_sprite(screen, 
            "Clotaire (réalisant son erreur) : Merde...le paysan avait raison..Je pensais qu'il voulais me piéger.", 
            font, clock, sprite_clotaire
        )

        # Archeon intervient
        display_dialogue_box(screen, 
            "Malheureusement, la gargouille atteint la dalle rouge. Archeon, observant depuis sa passerelle, affiche un sourire froid et calculateur. "
            "Le poids de l'erreur de Clotaire retombe immédiatement sur le groupe.", 
            font, clock
        )

        display_dialogue_with_sprite(screen, 
            "Archeon (froidement) : Un joueur doit être sacrifié cela ne peut pas etre celui qui vient de joué donc Clotaire est intouchable. C'est le prochain joueur qui joue qui doit décider... donc Aldric !", 
            font, clock, sprite_archeon
        )

        # Narration finale
        display_dialogue_box(screen, 
            "La tension dans la salle est palpable. Tous les regards se tournent vers Aldric, chacun cherchant à deviner son choix. "
            "Clotaire serre les poings, un mélange de colère et de honte sur son visage, mais il reste silencieux, incapable de nier sa faute. "
            "Garen, de son côté, observe avec une déception amère, son conseil ayant été ignoré au détriment de tous.", 
            font, clock
        )
        display_dialogue_with_sprite(screen, 
        "Aldric (pointant du doigt) : Toi..", 
        font, clock, sprite_aldric
        )
        
        fade_in_music("graphics/resources/music/sad.mp3", max_volume=0.2, fade_duration=1000)
    # Choix du joueur pour le sacrifice
        options_sacrifice = [
        ("Sacrifier Velm.", -20, "Clotaire", -30, "Brandio", "Velm"),
        ("Proposer Brandio comme sacrifice.", -20, "Clotaire", -30, "Velm", "Brandio")
        ]
        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_sacrifice], clock)

        if choix == 0:  # Sacrifier Velm
            display_dialogue_box(screen, 
            "Velm se fige petit à petit, un rictus de défi sur les lèvres alors que la lumière de la gargouille l'engloutit. "
            "Le craquement sinistre de la pierre enveloppant son corps résonne dans toute la salle, "
            "comme un glas marquant une perte irréparable.", 
            font, clock
        )

            display_dialogue_with_sprite(screen, 
            "Velm (souriant à Clotaire) : Clotaire...C'est fini pour moi...Promet moi...Promet moi de.. "
            "...Trouve cette île dont tu m'as tant parlé, realise notre rêve à tout les trois !... Clot...", 
            font, clock, sprite_velm
        )

            display_dialogue_box(screen, 
            "Sa voix s’éteint alors que son corps devient une statue immobile. "
            "La lumière de la gargouille s'éteint progressivement, laissant derrière elle une figure pétrifiée, "
            "figée dans un ultime sourire de défi.", 
            font, clock
        )

# Réaction de Clotaire
            display_dialogue_with_sprite(screen, 
            "Clotaire (Regardant Velm pétrifié…) : Je ferai ce qu'il faut... pour toi aussi.", 
            font, clock, sprite_clotaire
        )

            display_dialogue_box(screen, 
                "Clotaire reste un moment immobile, ses poings serrés à s'en faire blanchir les jointures. "
                "Son regard oscille entre la rage et une douleur qu’il tente de masquer. "
                "Il détourne finalement les yeux, mais l'éclat de vengeance qui brille dans son regard est indéniable.", 
                font, clock
            )

            # Réaction de Brandio
            display_dialogue_with_sprite(screen, 
                "Brandio (la voix tremblante, fixant la statue de Velm) : Tu… tu aurais pu le sauver…", 
                font, clock, sprite_brandio
            )
            display_dialogue_box(screen, 
                "Les mots de Brandio sont lourds de reproche, mais aussi de désespoir. "
                "Il recule légèrement, son regard hanté par l'image de son camarade disparu.", 
                font, clock
            )

            # Réaction d’Aldric et Kael
            display_dialogue_with_sprite(screen, 
                "Aldric (durement) : C'est vous ou nous !", 
                font, clock, sprite_aldric
            )
            display_dialogue_with_sprite(screen, 
                "Kael : Bien dit, je commence presque à peut-être t'apprécier !", 
                font, clock, sprite_kael
            )

            # Explosion de rage de Clotaire
            display_dialogue_with_sprite(screen, 
                "Clotaire (en détruisant une gargouille) : Enfant de putain !!! JE VAIS TE SAIGNER !", 
                font, clock, sprite_clotaire
            )

            display_dialogue_box(screen, 
                "Clotaire abat sa lame sur la gargouille la plus proche, la brisant en morceaux dans un élan de rage incontrôlable. "
                "Son cri de colère résonne dans toute la salle, glaçant le sang des survivants. "
                "Même les gargouilles semblent marquer un temps d'arrêt, comme pour observer cet éclat de fureur humaine.", 
                font, clock
            )

            # Conclusion de la scène
            display_dialogue_box(screen, 
                "Brandio détourne les yeux, incapable de soutenir plus longtemps la vision de son camarade pétrifié. "
                "Clotaire, lui, fixe le damier, sa respiration haletante, et murmure presque pour lui-même : "
                "Je trouverai cette île, Velm. Je te le promets.", 
                font, clock
            )
            hero.get_relation("Clotaire").adjust_score(-30)
            hero.get_relation("Brandio").adjust_score(-20)
            hero.remove_relation("Velm")

        elif choix == 1:  # Proposer Brandio comme sacrifice
            display_dialogue_box(screen, 
            "Brandio baisse la tête en silence et s'avance vers son destin face à la gargouille. "
            "Chaque pas résonne sur les dalles comme un dernier adieu, lourd de résignation.", 
            font, clock
            )
            display_dialogue_with_sprite(screen, 
                "Brandio : C'est pas la fin que j'imaginais… désolé Clotaire, mais ça sent la fin du voyage...", 
                font, clock, sprite_brandio
            )

            # Réaction de Velm
            display_dialogue_with_sprite(screen, 
                "Velm (furieux, les poings serrés) : Tu pouvais choisir quelqu'un d'autre, Aldric! Pourquoi lui ?", 
                font, clock, sprite_velm
            )

            # Clotaire réagit avec désespoir
            display_dialogue_with_sprite(screen, 
                "Clotaire (l'air sombre, la voix brisée) : Brandio... NOOOON !!", 
                font, clock, sprite_clotaire
            )

            # Brandio offre un dernier mot
            display_dialogue_with_sprite(screen, 
                "Brandio : Merci, mon pote... pour tout... pour le voyage... pour m'avoir sorti de la...", 
                font, clock, sprite_brandio
            )

            display_dialogue_box(screen, 
                "La lumière de la gargouille engloutit lentement Brandio. "
                "Sa silhouette se fige, laissant derrière elle une statue pétrifiée, le visage marqué par une assurance presque apaisée.", 
                font, clock
            )

            # Réaction d'Aldric et Clotaire
            display_dialogue_with_sprite(screen, 
                "Aldric (regardant Clotaire) : Tu aurais préféré que ça soit toi ?!", 
                font, clock, sprite_aldric
            )
            display_dialogue_with_sprite(screen, 
                "Clotaire (hurlant de rage, les yeux remplis de larmes) : Fumier... OUAAAAAAAAAH !", 
                font, clock, sprite_clotaire
            )

            # Velm et Clotaire évoquent leur rêve commun
            display_dialogue_box(screen, 
                "Velm, le regard fixé sur la statue de Brandio, murmure d'une voix tremblante : "
                "C'était notre rêve… Tous les trois. Trouver cette île, commencer une nouvelle vie. Maintenant... c'est trop tard pour lui.", 
                font, clock
            )
            display_dialogue_with_sprite(screen, 
                "Clotaire (le visage ravagé par la rage et la peine) : Ce n’est pas fini, Velm. Nous trouverons cette île. Pour lui. Pour Brandio. "
                "Même si la tour doit nous briser, on réalisera ce rêve.", 
                font, clock, sprite_clotaire
            )

            # Clôture dramatique
            display_dialogue_box(screen, 
                "La statue de Brandio reste immobile, marquant le sacrifice d’un camarade et l’échec d’un rêve partagé. "
                "Les gargouilles continuent d’avancer, insensibles à la douleur humaine. "
                "L’équipe reprend lentement son chemin, mais le poids de la perte pèse lourd sur leurs épaules.", 
                font, clock
            )

            hero.get_relation("Clotaire").adjust_score(-30)
            hero.get_relation("Velm").adjust_score(-20)
            hero.remove_relation("Brandio")

# Appel de la fonction
    clotare_sacrifice(hero, screen, font, clock, sprites)
    fade_out_music(fade_duration=1000)
    # Fin de l'épreuve après le sacrifice
    display_dialogue_box(screen, 
    "Le sacrifice est accompli. La gargouille sort du damier. "
    "Les flammes vertes des torches vacillent, marquant la fin de cette épreuve.", 
    font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/pierre.webp", WIDTH, HEIGHT)
    display_dialogue_box(screen, 
    "Aldric, suivi de près par Kael, avance prudemment mais avec détermination. "
    "Leur concentration est totale alors qu'ils franchissent enfin la dernière dalle rouge. "
    "Un soupir de soulagement échappe à Kael alors qu'il s'effondre presque sur ses genoux, épuisé mais satisfait.", 
    font, clock
    )
    display_dialogue_with_sprite(screen, 
    "Kael (soufflant) : On l’a fait… Enfin. Mais je me demande combien d’autres peuvent en dire autant.", 
    font, clock, sprite_kael
    )
    display_dialogue_with_sprite(screen, 
    "Aldric (regardant en arrière) : Ne relâche pas ta garde. Ce n’est pas encore fini.", 
    font, clock, sprite_aldric
    )

# Clotaire et son allié éliminent une gargouille
    display_dialogue_box(screen, 
    "De l’autre côté du plateau, Clotaire et son allié avancent avec agressivité. Une gargouille tente de leur bloquer le passage, "
    "mais Clotaire, avec une précision redoutable, frappe à la base de la créature. "
    "Son allié termine l’assaut d’un coup puissant, brisant la statue en morceaux.", 
    font, clock
    )
    display_dialogue_with_sprite(screen, 
    "Clotaire (avec un sourire en coin) :Je savais que ça finirait comme ça...Aldric...Tu as raison, Nous ne sommes que des pions...des putain de pions dans ce monde..", 
    font, clock, sprite_clotaire
    )
    display_dialogue_box(screen, 
    "Les deux hommes avancent alors sur la dalle rouge, leur qualification assurée. Clotaire jette un regard vers Aldric, un sourire de défi sur le visage.", 
    font, clock
    )
    fade_out_music(fade_duration=1000)
    fade_in_music("graphics/resources/music/study.mp3", max_volume=0.2, fade_duration=1000)

# Réactions des autres personnages
    display_dialogue_with_sprite(screen, 
    "Garen (depuis la dalle rouge) : Ils se sont qualifiés aussi… Je n’aime pas ça.", 
    font, clock, sprite_garen
    )
    display_dialogue_with_sprite(screen, 
    "Ayela (inquiète) : Clotaire ne s’arrêtera pas là. Ce genre de victoire ne le satisfait jamais.", 
    font, clock, sprite_ayela
    )
    display_dialogue_with_sprite(screen, 
    "Kael (haussant les épaules) : Qu’il tente quelque chose… Il n’aura pas l’avantage éternellement.", 
    font, clock, sprite_kael
    )

    display_dialogue_with_sprite(screen, 
    "Archeon (souriant) : Bravo. Vous avez respecté les règles… et payé le prix nécessaire.", 
    font, clock, sprite_archeon
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/clotaire.webp", WIDTH, HEIGHT)
# Réactions des personnages
    display_dialogue_with_sprite(screen, 
    "Clotaire détourne le regard, impassible. Velm (ou Brandio) reste figé, le visage dur, fixant la silhouette pétrifiée de son camarade.", 
    font, clock, sprite_clotaire
    )
    display_dialogue_with_sprite(screen, 
    "Ayela (voix basse, la gorge serrée) : Nous devions continuer… mais pas comme ça…", 
    font, clock, sprite_ayela
    )
    display_dialogue_with_sprite(screen, 
    "Garen (sombre) : Il est mort pour rien… mais c'était eux ou Kael alors...", 
    font, clock, sprite_garen
    )

# Intervention d'Emphyr
    display_dialogue_with_sprite(screen, 
    "Emphyr : Il connaissait les règles de la tour ! N'aie point de pitié pour lui...", 
    font, clock, sprite_emphyr
    )
    display_dialogue_with_sprite(screen, 
    "Garen : Mais c'était ton ami !", 
    font, clock, sprite_garen
    )
    display_dialogue_with_sprite(screen, 
    "Emphyr (en se passant la main dans les cheveux) : Mon ami ? Ne te méprends pas, la bande à Clotaire me servait simplement d'escorte… je savais qu'ils ne survivraient pas.", 
    font, clock, sprite_emphyr
    )
    display_dialogue_with_sprite(screen, 
    "Garen : Je… je vois…", 
    font, clock, sprite_garen
    )

    # Interaction entre Emphyr et Garen
    display_dialogue_with_sprite(screen, 
    "Emphyr : Toi, tu t'es bien mieux débrouillé qu'eux !", 
    font, clock, sprite_emphyr
    )
    display_dialogue_with_sprite(screen, 
    "Emphyr (avec un clin d'œil à Garen) :Puis Tu es mignon avec tes bottes trop grandes ahah!", 
    font, clock, sprite_emphyr
    )
    display_dialogue_with_sprite(screen, 
    "Garen (rougissant légèrement) : Euh..", 
    font, clock, sprite_garen
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/dalle5.webp", WIDTH, HEIGHT)
    def cloture_jeu(hero, screen, font, clock, sprites):
    # Clôture du Jeu des Dalles Cryptiques
        display_dialogue_box(screen, 
        "Clôture du Jeu des Dalles Cryptiques", 
        font, clock
        )
        display_dialogue_box(screen, 
        "Lentement, la pression retombe alors qu'Aldric, suivi de ses alliés, franchit la dernière dalle rouge. "
        "Un léger frisson parcourt l'échine de chacun tandis que l'éclat spectral du plateau s'estompe, signe que leur épreuve est terminée.", 
        font, clock
        )
        display_dialogue_with_sprite(screen, 
        "Archeon (d'une voix résonnante) : Félicitations. Vous faites partie des rares à avoir franchi cette étape. "
        "Mais ne vous réjouissez pas trop vite. Ce n'était qu'une epreuve... et la tour n'a pas encore révélé toutes ses etages.", 
        font, clock, sprite_archeon
        )
        fade_out_music(fade_duration=1000)
        fade_in_music("graphics/resources/music/study.mp3", max_volume=0.2, fade_duration=1000)

    # Description de l'arrivée des personnages
        display_dialogue_box(screen, 
        "Aldric s'arrête, regardant derrière lui.", 
        font, clock
        )

    
        display_dialogue_with_sprite(screen, 
            "Kael (le souffle court) : On l'a fait… Enfin. Notre équipe est passé !.", 
            font, clock, sprite_kael
            )
        
        display_dialogue_with_sprite(screen, 
            "Ayela (à voix basse) : Oui la pression est derière nous..", 
            font, clock, sprite_ayela
            )

        if hero.get_relation("Velm"):
            display_dialogue_with_sprite(screen, 
            "Velm (calmement, observant les autres joueurs) : Brandio...Mon pote..Je vais te venger..", 
            font, clock, sprite_velm
            )

        if hero.get_relation("Brandio"):
            display_dialogue_with_sprite(screen, 
            "Brandio (croisant les bras) : Peu importe. Velm...Mon ami...", 
            font, clock, sprite_brandio
            )

        display_dialogue_with_sprite(screen, 
        "Clotaire (Baissant la tête) : Il connaissait les risques...Putain...", 
        font, clock, sprite_clotaire
        )
        cloture_jeu(hero, screen, font, clock, sprites)

    # Ambiance de la salle et des participants
    display_dialogue_box(screen, 
        "Autour d'eux, les autres participants commencent leur partie prudemment sur le plateau, certains suivant les traces d'Aldric, "
        "d'autres formant leurs propres équipes. Chaque mouvement semble pesé, chaque dalle foulée porte le poids du doute.", 
        font, clock
        )
    display_dialogue_box(screen, 
        "Le vieux mage joue bien son coup, l'assassin aux dagues aussi, quant aux deux invocateurs, leur partie est tendue mais ils y arrivent.", 
        font, clock
        )
    display_dialogue_with_sprite(screen, 
        "Garen (de l'autre côté, observant depuis la dalle rouge) : Ils ont compris le jeu. Mieux vaut tard que jamais…", 
        font, clock, sprite_garen
    )
    display_dialogue_with_sprite(screen, 
        "Ayela (regardant au loin) : Espérons qu'ils aient le temps de la mettre en pratique.", 
        font, clock, sprite_ayela
    )

    display_dialogue_box(screen, 
        "Finalement, après des manœuvres et des sacrifices, seize participants atteignent la dalle rouge. "
        "Les autres sont pétrifiés ou sacrifiés par leurs équipes..", 
        font, clock
    )
    display_dialogue_with_sprite(screen, 
        "Archeon (souriant) : Bravo. Ceux qui restent peuvent avancer... Les autres leur ascension s'arrete ici...Nous devons respecter les morts..", 
        font, clock, sprite_archeon
    )

    display_dialogue_box(screen, 
        "La bande d'Aldric avance vers la porte suivante, le cinquieme étage est derrière eux. Il passe a coté de Archeon qui lui murmure..", 
        font, clock
    )
    display_dialogue_with_sprite(screen, 
        "Archeon (calme) : Continue d'avancer...Tu finira par trouver les réponses que tu cherche", 
        font, clock, sprite_archeon
    )

    display_dialogue_box(screen, 
        "Le claquement sourd de la dernière dalle résonne. Seize participants tiennent debout, la sueur coulant sur leurs fronts. "
        "Les perdants sont transformés en statues de pierre figés dans la panique, ou mort executés par leurs équipes.", 
        font, clock
    )
    display_dialogue_with_sprite(screen, 
        "Garen (voix tremblante) : Ils... ils sont vraiment tous...", 
        font, clock, sprite_garen
    )
    display_dialogue_with_sprite(screen, 
        "Ayela (voix basse) : On n'aurait rien pu faire.", 
        font, clock, sprite_ayela
    )
    display_dialogue_with_sprite(screen, 
        "Kael (murmure) : C'est une erreur de l'avoir laissé s'en sortir...", 
        font, clock, sprite_kael
    )
    display_dialogue_with_sprite(screen, 
        "Aldric (murmure) : On les a amputé d'un membre..C'est deja ca..", 
        font, clock, sprite_aldric
    )
    display_dialogue_with_sprite(screen, 
        "Ayela (surprise) : Aldric...", 
        font, clock, sprite_ayela
    )
    display_dialogue_with_sprite(screen, 
        "Aldric (murmure) : Nous ne sommes que des pions...Cette endroit s'amuse avec nous..", 
        font, clock, sprite_aldric
    )
    display_dialogue_with_sprite(screen, 
        "Clotaire (Bloquant Aldric) : Tu as tué un de mes vieux ami...Je ne l'oublierais pas...Ca non ! ", 
        font, clock, sprite_clotaire
        )

# Appel de la fonction
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/escalier6.PNG", WIDTH, HEIGHT)
    def clotaire_reaction_finale(hero, screen, font, clock, sprites):
    # Afficher le titre de la phase


    # Options de réaction face à Clotaire après le jeu
            options_clotaire = [
            ("Ignorer Clotaire et continuer en silence.", +5, "Garen", +5, "Ayela", -5, "Kael"),
            ("Confronter Clotaire discrètement.", +10, "Kael", -5, "Clotaire"),
            ("Menacer ouvertement Clotaire.", +15, "Kael", -10, "Clotaire", -5, "Ayela")
            ]
            choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_clotaire], clock)

            if choix == 0:  # Ignorer Clotaire
                display_dialogue_box(screen, 
                "Vous ignorez Clotaire et poursuivez votre chemin.", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Kael (marmonnant, mécontent) : Tch… Laisser passer ça… Mauvaise idée.", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Garen (à voix basse) : Parfois, il vaut mieux éviter l'escalade.", 
                font, clock, sprite_garen
                )
                display_dialogue_with_sprite(screen, 
                "Ayela (regardant Clotaire du coin de l'œil) : Il ne s'arrêtera pas là. Je le sens…", 
                font, clock, sprite_ayela
                )
                hero.get_relation("Garen").adjust_score(+5)
                hero.get_relation("Ayela").adjust_score(+5)
                hero.get_relation("Kael").adjust_score(-5)

            elif choix == 1:  # Confronter Clotaire discrètement
                display_dialogue_box(screen, 
                "Vous confrontez Clotaire discrètement, un échange de regards pesants suffit à faire passer votre message.", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Kael (approbateur) : Enfin, quelqu'un le remet à sa place.", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Ayela (soupirant de soulagement) : Je commençais à me demander si tu comptais le laisser faire…", 
                font, clock, sprite_ayela
                )
                display_dialogue_with_sprite(screen, 
                "Clotaire (légèrement amusé) : Tant d'efforts pour me défier en silence… Intéressant.", 
                font, clock, sprite_clotaire
                )
                hero.get_relation("Kael").adjust_score(+10)
                hero.get_relation("Clotaire").adjust_score(-5)

            elif choix == 2:  # Menacer Clotaire ouvertement
                display_dialogue_box(screen, 
                "Vous menacez Clotaire ouvertement, attirant l'attention de tout le groupe. "
                "La tension monte rapidement, chaque joueur sentant que l’épreuve n’a pas seulement laissé des marques physiques, "
                "mais aussi des fractures profondes entre les survivants.", 
                font, clock
            )

            # Clotaire défie Aldric
                display_dialogue_with_sprite(screen, 
                    "Clotaire (vous dévisageant, un sourire froid aux lèvres) : Tente ta chance, Aldric. Je suis prêt.", 
                    font, clock, sprite_clotaire
                )

                # Narration sur la culpabilité de Clotaire
                display_dialogue_box(screen, 
                    "Malgré son calme apparent, les poings de Clotaire tremblent légèrement. Il refuse de croiser le regard de quiconque, "
                    "mais son obstination à ignorer les conséquences de ses actes est évidente. "
                    "Il sait, au fond, que c'est son excès de confiance qui a causé la mort de Velm, mais il est incapable de l'accepter. "
                    "Pour lui, Aldric est un bouc émissaire idéal, un exutoire pour sa propre culpabilité.", 
                    font, clock
                )

                # Kael soutient Aldric
                display_dialogue_with_sprite(screen, 
                    "Kael (croisant les bras, un regard dur sur Clotaire) : Je suis avec toi, Aldric. Ce type nous ralentira un jour.", 
                    font, clock, sprite_kael
                )

                # Garen cherche à calmer la situation
                display_dialogue_with_sprite(screen, 
                    "Garen (fronçant les sourcils, sa voix ferme) : On n'a pas besoin de ça maintenant…", 
                    font, clock, sprite_garen
                )
                display_dialogue_box(screen, 
                    "Garen jette un regard chargé de reproche à Clotaire, clairement frustré par son incapacité à reconnaître ses erreurs. "
                    "Mais même Garen sait que ce n'est pas le moment pour une confrontation ouverte.", 
                    font, clock
                )

                # Ayela tente de désamorcer la tension
                display_dialogue_with_sprite(screen, 
                    "Ayela (visiblement mal à l'aise, sa voix hésitante) : Vous deux, calmez-vous. On vient de survivre de peu.", 
                    font, clock, sprite_ayela
                )

                # Narration sur la dynamique du groupe
                display_dialogue_box(screen, 
                    "Le groupe semble divisé. Kael et Aldric s'opposent clairement à Clotaire, tandis que Garen et Ayela cherchent à maintenir une fragile unité. "
                    "Mais au fond, tous savent que cette épreuve a révélé des fractures irréparables. Clotaire, figé dans son déni, "
                    "fixe Aldric avec une haine grandissante, incapable de supporter le poids de ses propres actions.", 
                    font, clock
                )

                # Clotaire ajoute au drame
                display_dialogue_with_sprite(screen, 
                    "Clotaire (hurlant, ses yeux remplis de rage) : Tu crois que c’est ma faute ?! C’est toi, Aldric, avec tes choix de leader à la noix !", 
                    font, clock, sprite_clotaire
                )

                display_dialogue_box(screen, 
                    "Sa voix résonne dans la salle silencieuse. Le groupe reste figé, chacun conscient que cette querelle pourrait éclater à tout moment en une confrontation irréparable.", 
                    font, clock
                )
                hero.get_relation("Kael").adjust_score(+15)
                hero.get_relation("Clotaire").adjust_score(-10)
                hero.get_relation("Ayela").adjust_score(-5)

# Appel de la fonction
    clotaire_reaction_finale(hero, screen, font, clock, sprites)
    
    display_dialogue_box(screen, 
        "Vous franchissez enfin la porte, laissant derrière vous les corps de pierre des perdants. "
        "Les survivants avancent, mais l'ombre du sacrifice pèse encore.", 
        font, clock
    )

    # Dialogue entre Emphyr et Clotaire
    display_dialogue_with_sprite(screen, 
    "Emphyr (en caressant l'épaule de Clotaire, un sourire narquois aux lèvres) : Sois pas si tendu... on est presque à l'étage 7 !", 
    font, clock, sprite_emphyr
        )
    display_dialogue_box(screen, 
            "Le ton d’Emphyr est à la fois rassurant et condescendant, laissant transparaître qu’elle savoure pleinement son ascendant sur Clotaire.", 
            font, clock
        )

    display_dialogue_with_sprite(screen, 
            "Clotaire (les dents serrées) : Tu ne peux pas comprendre, tu nous considères comme tes larbins...", 
            font, clock, sprite_clotaire
        )

    display_dialogue_box(screen, 
            "Clotaire détourne les yeux, mais son expression trahit plus que de la colère. Une tension sous-jacente semble peser sur ses épaules, "
            "comme s’il portait un poids que seule Emphyr connaissait vraiment.", 
            font, clock
        )

        # Sous-entendus d’Emphyr
    display_dialogue_with_sprite(screen, 
            "Emphyr (doucement, presque murmurant) : Larbins, peut-être… mais des larbins avec des rêves, non ? Cette fameuse île…", 
            font, clock, sprite_emphyr
        )

    display_dialogue_box(screen, 
            "Le sourire d’Emphyr s’élargit légèrement, comme si elle jouait avec une vérité qu’elle connaissait mais que Clotaire refusait d’admettre.", 
            font, clock
        )

    display_dialogue_with_sprite(screen, 
            "Clotaire (froidement) : Ne joue pas à ça avec moi.", 
            font, clock, sprite_clotaire
        )

    display_dialogue_with_sprite(screen, 
            "Emphyr : Pourquoi pas ? Après tout, tu es ici pour ça, non ? L’Empereur t’a promis la carte… si tu fais ta part.", 
            font, clock, sprite_emphyr
        )

    display_dialogue_box(screen, 
            "Le silence de Clotaire est éloquent. Sa mâchoire se serre, ses poings tremblent légèrement, mais il ne répond pas. "
            "Le regard d’Emphyr brille de satisfaction, comme si elle savourait cette victoire implicite.", 
            font, clock
        )

    display_dialogue_with_sprite(screen, 
            "Clotaire (détournant le regard, d’une voix amère) : Tu as interet a tenir parole...", 
            font, clock, sprite_clotaire
        )

    # Dialogue conditionnel en fonction des relations
    if hero.get_relation("Velm"):
        display_dialogue_with_sprite(screen, 
            "Velm : Oui, on va venger Brando... je te le promets.", 
            font, clock, sprite_velm
        )
    if hero.get_relation("Brandio"):
        display_dialogue_with_sprite(screen, 
            "Brandio : Velm... Clotaire... Velm était notre ami...", 
            font, clock, sprite_brandio
        )

    # Clôture du dialogue
    display_dialogue_with_sprite(screen, 
        "Clotaire (avec un sourire déterminé) : Fait chier...", 
        font, clock, sprite_clotaire
    )


    fade_out_music(fade_duration=4000)
    fade_in_text(screen, "Fin du Chapitre 6 - Il reste 16 participants sur 99 et 94 étages", font, (WIDTH // 2, HEIGHT // 2), duration=2000)
    fade_out_text(screen, 1000)
    game_menu(screen, font, clock, WIDTH, HEIGHT, hero)

def chapitre_7(hero, screen, font, clock,sprites):
    
    global background
    
    sprites = load_sprites()

    sprite_aldric = sprites["Aldric"]
    sprite_garen = sprites["Garen"]
    sprite_mysterieux = sprites["Homme_mysterieux"]
    sprite_kael = sprites["Kael"]
    sprite_brandio = sprites["Brandio"]
    sprite_archeon = sprites["Archeon"]
    sprite_ayela = sprites["Ayela"]
    sprite_clotaire = sprites["Clotaire"]
    sprite_durnir = sprites["Durnir"]
    sprite_emphyr = sprites["Emphyr"]
    sprite_gallius = sprites["Gallius"]
    sprite_velm = sprites["Velm"]
    sprite_yohna = sprites["Yohna"]
    sprite_zyn = sprites["Zyn"]
    sprite_random_participant = sprites["Participant"]
    sprite_creature = sprites["Creature"]
    
    fade_in_music("graphics/resources/music/Medusa.mp3", max_volume=0.2, fade_duration=1000)
    clear_screen(screen)
    fade_in_text(screen, 
             "Chapitre 7 : Elément perturbateur - Etage 6/99", 
             font, 
             (WIDTH // 2, HEIGHT // 2),  # Centré sur l'écran
             duration=3000)
    fade_out_text(screen, 3000, fade_speed=2)
    pygame.time.wait(1000)
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/salle6.PNG", WIDTH, HEIGHT)
    gallius = Character("Gallius", "graphics/resources/sprites/Gallius.webp", 
                  "Assassin chevroné.", 
                  "Ombre", gender="garçon")

    hero.add_relation(gallius, "Neutre")
    # Description initiale de l'étage
    display_dialogue_box(screen,
            "Les marches du sixième étage semblent plus longues, plus lourdes. Chaque pas fait craquer les vieilles pierres "
            "comme si elles se plaignaient de votre présence. Le silence qui vous entoure devient presque assourdissant.", 
            font, clock
        )

    display_dialogue_box(screen,
            "Lorsque vous atteignez enfin la porte massive, un courant d’air glacé s’en échappe, "
            "comme si l’étage vous jaugeait avant de vous laisser entrer. Derrière la porte, une vaste salle circulaire s’étend. "
            "Au centre, une stèle de pierre noire trône, pulsant faiblement sous la lueur des torches accrochées au mur. "
            "Quatre portes se tiennent également là : rouge et verte à gauche, bleue et marron à droite.", 
            font, clock
        )

        # Premières réactions
    display_dialogue_with_sprite(screen,
            "Kael (croisant les bras, appuyé contre un pilier) : Encore une stèle… À ce rythme, je vais finir archéologue.", 
            font, clock, sprite_kael
        )
    display_dialogue_with_sprite(screen,
            "Ayela (plissant les yeux) : Ne plaisante pas. Cette fois, ça sent vraiment mauvais.", 
            font, clock, sprite_ayela
        )
    display_dialogue_with_sprite(screen,
            "Garen (fixant la stèle) : Elle… regarde à travers nous. Vous ne trouvez pas ?", 
            font, clock, sprite_garen
        )

        # Présence de Clotaire, Emphyr et les autres
    display_dialogue_box(screen,
            "Clotaire se tient un peu à l’écart avec Emphyr et les survivants de la salle précédente. "
            "Un vide tangible semble hanter leur groupe, le poids d’une perte récente encore palpable.", 
            font, clock
        )

    if hero.get_relation("Velm"):
        display_dialogue_with_sprite(screen,
                "Velm (à Clotaire, à voix basse) : Quatre équipes… On va être séparés. J'espère rester en vie cette fois…", 
                font, clock, sprite_velm
            )
        display_dialogue_with_sprite(screen,
                "Emphyr (glissant un regard vers Velm) : On s'en sortira, Velm. Ne t'inquiète pas.", 
                font, clock, sprite_emphyr
            )

    if hero.get_relation("Brandio"):
        display_dialogue_with_sprite(screen,
                "Brandio (ricanant) : Quatre équipes ? Ça tombe bien, il reste moins de monde pour nous ralentir. Pas vrai, Clotaire ?", 
                font, clock, sprite_brandio
            )
        display_dialogue_with_sprite(screen,
                "Emphyr (regard doux mais ferme) : Brandio… Velm méritait mieux que ça.", 
                font, clock, sprite_emphyr
            )
        display_dialogue_with_sprite(screen,
                "Brandio (haussant les épaules) : Mieux ou pas, il est plus là.", 
                font, clock, sprite_brandio
            )

        # Activation de la stèle
    display_dialogue_box(screen,
            "Un frisson traverse la pièce lorsque les runes de la stèle s’animent. Elles s’élèvent, tourbillonnent, "
            "avant de se graver lentement dans l’air, projetant une lumière étrange sur les visages attentifs.", 
            font, clock
        )
    display_dialogue_box(screen,
            "Stèle : Quatre chemins. Quatre épreuves. Quatre équipes. L’unité seule triomphera des éléments. "
            "L’échec entraînera la chute.", 
            font, clock
        )
    display_dialogue_with_sprite(screen,
            "Kael (sifflant) : Ah, enfin un peu de mystère… Je commençais à m'ennuyer.", 
            font, clock, sprite_kael
        )
    display_dialogue_with_sprite(screen,
            "Ayela (chuchotant, tendue) : Ce n'est pas un jeu, Kael…", 
            font, clock, sprite_ayela
        )

        # Lignes lumineuses et portes
    display_dialogue_box(screen,
            "Soudain, des lignes dorées s’étendent au sol, formant quatre chemins distincts. "
            "À l’extrémité de chaque chemin, une porte se matérialise, marquée d’un symbole élémentaire : "
            "Feu, Air, Terre, Eau.", 
            font, clock
        )

    display_dialogue_with_sprite(screen,
            "Kael (plaisantant) : Laissez-moi deviner… Je suis condamné à l’Air. Un symbole.", 
            font, clock, sprite_kael
        )
    display_dialogue_with_sprite(screen,
            "Garen (glissant un regard vers Kael) : Au moins, tu ne risques pas de fondre dans la salle du Feu.", 
            font, clock, sprite_garen
        )

    display_dialogue_box(screen,
            "Vous sentez vos pas vous guider vers la salle du Feu. Ayela se tient à vos côtés, l'arc en main. "
            "Clotaire s'arrête devant la porte de la salle de l'Air, Emphyr à ses côtés.", 
            font, clock
        )
    # Échange initial entre Emphyr et Clotaire
    display_dialogue_with_sprite(screen, 
        "Emphyr (calme, regardant la porte de l’Air) : Peut-être qu'il est temps que certains d'entre nous apprennent à s'entraider…", 
        font, clock, sprite_emphyr
    )
    display_dialogue_with_sprite(screen, 
        "Clotaire (esquissant un sourire en coin) : L'entraide… Un mot qui a tué Velm, non ?", 
        font, clock, sprite_clotaire
    )
    display_dialogue_with_sprite(screen, 
        "Emphyr (le regard perçant) : Non. C'est l'orgueil qui l'a tué.", 
        font, clock, sprite_emphyr
    )

    # Description de Gallius
    display_dialogue_box(screen, 
        "Un jeune garçon se tient près de l’entrée de la salle, le dos appuyé contre le mur. "
        "Ses cheveux noirs, courts et bouclés, sont légèrement ébouriffés, et ses yeux verts perçants scrutent la pièce avec calme. "
        "Son torse nu est orné de tatouages mystiques noirs qui s’entrelacent harmonieusement. Une écharpe couvre partiellement son torse, "
        "montant jusqu’au haut de ses pectoraux, et il porte un pantalon de combat ajusté avec des bottes en cuir robustes.", 
        font, clock
    )

    display_dialogue_with_sprite(screen, 
        "Gallius (calme) : Feu, hein… Ça me va.", 
        font, clock, sprite_gallius
    )

    # Réaction des personnages
    display_dialogue_with_sprite(screen, 
        "Ayela (regarde la porte) : On va vraiment entrer là-dedans ?", 
        font, clock, sprite_ayela
    )
    display_dialogue_with_sprite(screen, 
        "Aldric (calme) : On n’a pas le choix.", 
        font, clock, sprite_aldric
    )

    # Introduction de Gallius par le dialogue
    display_dialogue_with_sprite(screen, 
        "Gallius (à voix basse) : Tu tremble archère ?", 
        font, clock, sprite_gallius
    )
    display_dialogue_with_sprite(screen, 
        "Ayela : Qui es-tu au fait ? Attend c'est pas toi qui a traversé l'étage 3 contre les créatures a pleine vitesse et sans peur ?", 
        font, clock, sprite_ayela
    )
    display_dialogue_with_sprite(screen, 
        "Gallius (nettoyant sa dague) : Hm oui, Gallius... Je suis rapide… invisible.", 
        font, clock, sprite_gallius
    )
    display_dialogue_box(screen, 
        "Avant même qu’Ayela ne puisse répondre, Gallius place sa lame sous sa gorge avec une précision déconcertante, "
        "puis la retire aussitôt avec un sourire presque imperceptible.", 
        font, clock
    )
    # Réaction d’Ayela et Garen
    display_dialogue_with_sprite(screen, 
        "Ayela : Héééé, ne fais pas ça !", 
        font, clock, sprite_ayela
    )
    display_dialogue_with_sprite(screen, 
        "Garen : Aldric ! Tâche de survivre… Toi aussi, Ayela.", 
        font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen, 
        "Aldric : Promis, Garen. Ça vaut pour vous aussi !", 
        font, clock, sprite_aldric
    )

    # Clôture avant l’épreuve
    display_dialogue_box(screen, 
        "Un bruit sourd résonne lorsque les portes se referment derrière chaque groupe. "
        "L’épreuve commence. L’air devient lourd, chargé d’une tension palpable.", 
        font, clock
    )
    def floor6_fire(hero, screen, font, clock,sprites):
    # Narration d'entrée
        global background
        background = fade_in_background(screen,"graphics/resources/backgrounds/feu.webp", WIDTH, HEIGHT)
        display_dialogue_box(screen, 
            "La porte claque violemment derrière vous, coupant toute possibilité de retour. "
            "L’air brûlant de la salle vous frappe de plein fouet, comme si chaque respiration enflammait vos poumons. "
            "Des gerbes de flammes dansent autour de vous, illuminant brièvement les visages crispés de vos compagnons.", 
            font, clock
        )

        display_dialogue_with_sprite(screen, 
            "Ayela (s’essuyant le front rapidement) : On vient à peine d’entrer et je sens déjà mes vêtements coller à ma peau…", 
            font, clock, sprite_ayela
        )

        display_dialogue_with_sprite(screen, 
            "Gallius (calme, observant la pièce) : Bienvenue en enfer. L’épreuve du feu… Je m’attendais à pire.", 
            font, clock, sprite_gallius
        )

        # Conflits internes - Velm
        if hero.get_relation("Velm"):
            display_dialogue_with_sprite(screen, 
                "Velm (fixant les flammes avec amertume) : Il aurait dû être là…", 
                font, clock, sprite_velm
            )
            display_dialogue_with_sprite(screen, 
                "Velm (lourdement) : Tu sais, Aldric… Chaque seconde passée avec toi est une insulte à Brandio.", 
                font, clock, sprite_velm
            )
            display_dialogue_with_sprite(screen, 
                "Velm (détournant à peine les yeux des flammes) : Tu aurais pu sacrifier cet imbécile de Kael…!", 
                font, clock, sprite_velm
            )
            display_dialogue_with_sprite(screen, 
                "Aldric (le regard ferme) : Et toi, aurais-tu sacrifié Brandio ou Clotaire pour sauver mon équipier si tu avais été à ma place ?", 
                font, clock, sprite_aldric
            )
            display_dialogue_with_sprite(screen, 
                "Velm (soupirant, le regard fuyant) : Je… tsss… Brandio voulait sauver sa sœur… Maintenant, elle va mourir… "
                "Nous devions voyager avec elle, voir le monde !", 
                font, clock, sprite_velm
            )
            display_dialogue_with_sprite(screen, 
                "Aldric : Désolé… On a tous un but ici. J’ai dû faire un choix… La Tour est cruelle, et tu le sais. Fais ton deuil.", 
                font, clock, sprite_aldric
            )

        # Conflits internes - Brandio
        if hero.get_relation("Brandio"):
            display_dialogue_with_sprite(screen, 
                "Brandio (serrant les poings) : Velm n’aurait jamais hésité…", 
                font, clock, sprite_brandio
            )
            display_dialogue_with_sprite(screen, 
                "Brandio (fixant Aldric) : C’est toi qui as choisi, Aldric. Ne l’oublie jamais.", 
                font, clock, sprite_brandio
            )
            display_dialogue_with_sprite(screen, 
                "Brandio (amèrement) : On avance… Mais cette foutue tour prendra son dû un jour. Peut-être même avant la fin de cet étage.", 
                font, clock, sprite_brandio
            )
            display_dialogue_with_sprite(screen, 
                "Brandio (détournant à peine les yeux des flammes) : Tu aurais pu sacrifier cet imbécile de noble…!", 
                font, clock, sprite_brandio
            )
            display_dialogue_with_sprite(screen, 
                "Aldric (ferme) : Et toi, aurais-tu sacrifié Velm ou Clotaire pour sauver mon équipier si tu avais été à ma place ?", 
                font, clock, sprite_aldric
            )
            display_dialogue_with_sprite(screen, 
                "Brandio (la voix tremblante) : Velm était un petit con… mais il… il… Nous venions des bas-fonds d’Austravia, la capitale... "
                "On devait s’offrir une autre vie avec lui et Clotaire !", 
                font, clock, sprite_brandio
            )
            display_dialogue_with_sprite(screen, 
                "Aldric : Désolé… On a tous un but ici. J’ai dû faire un choix… La Tour est cruelle, et tu le sais. Fais ton deuil.", 
                font, clock, sprite_aldric
            )
        fade_out_music(fade_duration=1000)
        fade_in_music("graphics/resources/music/wolf.mp3", max_volume=0.3, fade_duration=1000)
        # Progression dans la salle
        display_dialogue_box(screen, 
            "Le groupe avance lentement à travers la salle, chaque pas résonnant sur les dalles brûlantes. "
            "L’air semble vibrer de manière étrange, comme si quelque chose d’ancien attendait de se manifester.", 
            font, clock
        )
        background = fade_in_background(screen,"graphics/resources/backgrounds/feu2.webp", WIDTH, HEIGHT)
        # Apparition du Gardien de Flamme
        display_dialogue_box(screen, 
            "Alors que vous atteignez le centre de la pièce, une forme titanesque se détache des flammes. "
            "Elle s'élève, ses traits flous et instables, entièrement composée de flammes noires et pourpres. "
            "Son torse laisse apparaître par intermittence un cœur brillant, pulsant à travers les flammes tourbillonnantes.", 
            font, clock
        )
        

        display_dialogue_with_sprite(screen, 
            "Ayela (à voix basse, bandant son arc) : C’est… vivant, non ?", 
            font, clock, sprite_ayela
        )
        display_dialogue_with_sprite(screen, 
            "Gallius (impassible, prêtant attention à la créature) : Vivant ou non, peu importe. Ça bloque notre chemin.", 
            font, clock, sprite_gallius
        )
        
        # Transition pour la suite
        display_dialogue_box(screen, 
            "Les flammes autour de vous rugissent, et le Gardien de Flamme se met en mouvement. "
            "La chaleur devient insoutenable, et la lumière vacillante des flammes projette des ombres terrifiantes sur les murs. "
            "Le combat pour avancer commence.", 
            font, clock
        )
        display_dialogue_box(
        screen,
        "Le Gardien de Flamme se dresse devant vous, sa chaleur intense envahissant la pièce. "
        "Il brandit un bras gigantesque, prêt à attaquer.",font,clock
        )
    
        display_dialogue_with_sprite(
            screen,
            "Gallius (calme) : On dirait que ce truc ne plaisante pas…",
            font,
            clock,
            sprite_gallius
        )
        display_dialogue_with_sprite(
            screen,
            "Ayela (prête à tirer) : C’est notre chance. Il doit avoir un point faible…",
            font,
            clock,
            sprite_ayela
        )

        # Present choices
        options_combat = [
            ("Attaque directe (Aldric mène l'assaut).", -15, "Aldric", -5, "Gallius", -5, "Velm", +10, "Brandio"),
            ("Observer et attendre une faille.", +0, "Aldric", +10, "Velm", -5, "Brandio"),
            ("Demander à Ayela de tirer une flèche.", +0, "Ayela", +5, "Velm", -5, "Brandio")
        ]
        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_combat], clock)

        if choix == 0:  # Attaque directe
            display_dialogue_box(
                screen,
                "Aldric s'élance, mais la chaleur intense le repousse brutalement, le projetant au sol. (-15 PV Aldric)",
                font,
                clock,
            )
            hero.adjust_health(-15)
            display_dialogue_with_sprite(
                screen,
                "Gallius (se plaçant devant Aldric) : Recule. C'est suicidaire.",
                font,
                clock,
                sprite_gallius
            )
            hero.get_relation("Gallius").adjust_score(-5)

            if hero.get_relation("Velm"):
                display_dialogue_with_sprite(
                    screen,
                    "Velm (sombre) : Exactement ce que tu as fait à Brandio. Tu n'as pas hésité… (-5 relation Velm)",
                    font,
                    clock,
                    sprite_velm
                )
                hero.get_relation("Velm").adjust_score(-5)

            if hero.get_relation("Brandio"):
                display_dialogue_with_sprite(
                    screen,
                    "Brandio (ricanant) : Continue, Aldric… Peut-être que cette fois, ce sera toi. (+10 relation Brandio)",
                    font,
                    clock,
                    sprite_brandio
                )
                hero.get_relation("Brandio").adjust_score(+10)

        elif choix == 1:  # Observer et attendre une faille
            display_dialogue_box(
                screen,
                "Aldric observe attentivement la créature et remarque que son cœur s'illumine à intervalles réguliers.",
                font,
                clock,
            )
            display_dialogue_with_sprite(
                screen,
                "Aldric (calme) : Attendez. Son cœur. Il y a une ouverture…",
                font,
                clock,
                sprite_aldric
            )

            if hero.get_relation("Velm"):
                display_dialogue_with_sprite(
                    screen,
                    "Velm (grommelant) : On n'aurait pas eu besoin d'attendre si Brandio était là… (+10 relation Velm)",
                    font,
                    clock,
                    sprite_velm
                )
                hero.get_relation("Velm").adjust_score(+10)

            if hero.get_relation("Brandio"):
                display_dialogue_with_sprite(
                    screen,
                    "Brandio (grinçant des dents) : Velm aurait frappé sans réfléchir. C'est pour ça qu'il est mort… (-5 relation Brandio)",
                    font,
                    clock,
                    sprite_brandio
                )
                hero.get_relation("Brandio").adjust_score(-5)

        elif choix == 2:  # Demander à Ayela de tirer une flèche
            display_dialogue_box(
                screen,
                "Ayela tire une flèche, mais elle traverse les flammes sans causer de dommage visible.",
                font,
                clock
            )
            display_dialogue_with_sprite(
                screen,
                "Ayela (frustrée) : C'était pourtant bien visé…",
                font,
                clock,
                sprite_ayela
            )

            if hero.get_relation("Velm"):
                display_dialogue_with_sprite(
                    screen,
                    "Velm (haussant les épaules) : Ça vaut toujours mieux que de foncer sans réfléchir. Continue. (+5 relation Velm)",
                    font,
                    clock,
                    sprite_velm
                )
                hero.get_relation("Velm").adjust_score(+5)

            if hero.get_relation("Brandio"):
                display_dialogue_with_sprite(
                    screen,
                    "Brandio (sarcastique) : Tu veux pas essayer un lance-pierre, Ayela ! Tsss Je déteste les archers… (-5 relation Brandio)",
                    font,
                    clock,
                    sprite_brandio
                )
                hero.get_relation("Brandio").adjust_score(-5)
                hero.get_relation("Ayela").adjust_score(+5)

        # Post-choice
        display_dialogue_box(
        screen,
        "Le Gardien de Flamme recule légèrement, ses yeux incandescents fixant vos moindres gestes. "
        "La chaleur oppressante dans la salle semble encore augmenter, comme si elle répondait à son humeur.",
        font, clock
        )

        # Lore ajouté : Origine du Gardien
        display_dialogue_box(
        screen,
        "Autour de vous, les murs de la salle semblent vibrer légèrement, émettant un faible bourdonnement. "
        "Selon les légendes, le Gardien de Flamme est une entité née des premiers forgerons qui ont défié les dieux, "
        "scellant leur essence dans une flamme éternelle. Aujourd'hui, il juge ceux qui osent s'aventurer dans la Tour.",
        font, clock
        )

        # Narration immersive
        display_dialogue_box(
        screen,
        "Le Gardien lève lentement les bras, ses mouvements fluides malgré son apparence massive. "
        "Une lumière rougeoyante s'intensifie au-dessus de lui, prenant la forme d'un orbe en fusion. "
        "Soudain, des flammes sombres se concentrent dans une spirale tourbillonnante avant de s’abattre dans votre direction. Que faites-vous ?",
        font, clock
        )  
            # Présentation des choix
        options_combat = [
        ("Esquiver.", +0, "Gallius", +0, "Ayela", -5, "Velm"),
        ("Bloquer avec votre manteau.", -3, "Aldric", +5, "Ayela", -5, "Velm"),
        ("Contre-attaquer avec Gallius.", +5, "Gallius", +5, "Velm", -5, "Brandio")
        ]
        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_combat], clock)

        if choix == 0:  # Esquiver
            display_dialogue_box(
                screen,
                "Aldric s'élance sur le côté, entraînant Ayela par le bras. Gallius se faufile habilement entre les flammes.",
                font, clock
            )
            display_dialogue_box(screen, "Aucune blessure n'est infligée.", font, clock)
            display_dialogue_with_sprite(screen, "Gallius : Tu devrais suivre son exemple. La tour ne pardonne pas la lenteur.", font, clock, sprite_gallius)

            if hero.get_relation("Velm"):
                display_dialogue_with_sprite(screen, "Velm (grinçant des dents) : Je n'ai pas besoin de conseils, surtout pas de sa part.", font, clock, sprite_velm)
                hero.get_relation("Velm").adjust_score(-5)

            if hero.get_relation("Brandio"):
                display_dialogue_with_sprite(screen, "Brandio (murmurant) : Velm aurait couru droit dans le feu… Et il aurait survécu, lui.", font, clock, sprite_brandio)

        elif choix == 1:  # Bloquer avec votre manteau
            display_dialogue_box(
                screen,
                "Aldric lève son manteau, l'utilisant comme un bouclier contre les flammes. Une partie est déviée, mais la chaleur brûle sa peau (-3 PV).",
                font, clock
            )
            hero.adjust_health(-3)
            display_dialogue_with_sprite(screen, "Ayela (soulagée) : Merci Aldric…", font, clock, sprite_ayela)
            hero.get_relation("Ayela").adjust_score(+5)

            if hero.get_relation("Velm"):
                display_dialogue_with_sprite(screen, "Velm (regardant Aldric) : Ça n'aurait pas suffi pour sauver Brandio.", font, clock, sprite_velm)
                hero.get_relation("Velm").adjust_score(-5)

            if hero.get_relation("Brandio"):
                display_dialogue_with_sprite(screen, "Brandio (à voix basse) : Tu prends des coups… Mais c'est trop tard pour Velm.", font, clock, sprite_brandio)
                hero.get_relation("Brandio").adjust_score(-5)

        elif choix == 2:  # Contre-attaquer avec Gallius
            display_dialogue_box(
                screen,
                "Gallius bondit sous la vague et frappe la créature à la jambe. Des éclats de flammes s'envolent sous l'impact, révélant une plaie luisante.",
                font, clock
            )
            display_dialogue_with_sprite(screen, "Gallius : Il saigne… du feu ?", font, clock, sprite_gallius)
            hero.get_relation("Gallius").adjust_score(+5)

            if hero.get_relation("Velm"):
                display_dialogue_with_sprite(screen, "Velm : Il aurait aimé cette phrase, tu sais.", font, clock, sprite_velm)
                hero.get_relation("Velm").adjust_score(+5)

            if hero.get_relation("Brandio"):
                display_dialogue_with_sprite(screen, "Brandio (croisant les bras) : Tsss… Quand je pense que Velm est mort par ta faute...J'espere sortir vivant pour te le faire payer.", font, clock, sprite_brandio)
                hero.get_relation("Brandio").adjust_score(-5)
            
        # Post-choix narration enrichie
        display_dialogue_box(
            screen,
            "Le Gardien de Flamme recule légèrement, ses yeux semblables à des braises vivantes scrutant vos moindres mouvements. "
            "La chaleur dans la salle augmente encore d’un cran, rendant l’air difficile à respirer. "
            "Vous sentez une pression sourde peser sur vos épaules, comme si la Tour elle-même participait à cette épreuve.",
            font, clock
        )

        # Lore ajouté : Présence du Gardien
        display_dialogue_box(
            screen,
            "Autour de vous, les gravures sur les murs scintillent faiblement, projetant des ombres mouvantes. "
            "Gallius murmure pour lui-même, rappelant une légende : 'On dit que le Gardien ne protège pas seulement cette salle... "
            "il est le dernier rempart contre ceux qui ne méritent pas de continuer l’ascension.'",
            font, clock
        )

        # Réactions des compagnons
        if hero.get_relation("Brandio"):
            display_dialogue_with_sprite(
                screen,
                "Brandio (resserrant son arme) : Si cette chose bouge encore, je le tranche en deux ! Je n’ai pas traversé tout ça pour mourir ici !",
                font, clock, sprites["Brandio"]
            )
        if hero.get_relation("Velm"):
            display_dialogue_with_sprite(
                screen,
                "Velm (calme mais tendu) : Les flammes dansent selon sa volonté. Il attend que nous fassions une erreur. Restons sur nos gardes.",
                font, clock, sprites["Velm"]
            )

        # Dialogues spécifiques à Ayela et Gallius
        display_dialogue_with_sprite(
            screen,
            "Ayela (serrant son arc) : Cette chaleur est insoutenable... mais il doit avoir une faiblesse. "
            "Chaque créature en a une, même celles forgées par le feu.",
            font, clock, sprites["Ayela"]
        )

        display_dialogue_with_sprite(
            screen,
            "Gallius (plissant les yeux) : Aldric, cette créature n'est pas qu'un simple gardien. "
            "Elle juge notre valeur... ou peut-être notre volonté. Nous devons rester unis.",
            font, clock, sprites["Gallius"]
        )

        # Interaction avec Aldric
        display_dialogue_with_sprite(
            screen,
            "Aldric (hésitant) : Alors nous devons agir vite. Si cette chaleur continue d'augmenter, nous ne tiendrons pas longtemps.",
            font, clock, sprites["Aldric"]
        )

        # Nouvelle phase du combat
        display_dialogue_box(
            screen,
            "Le Gardien de Flamme pousse un rugissement guttural. Une lumière aveuglante jaillit de son torse, et le sol sous vos pieds "
            "commence à briller d’un rouge intense. Des fissures apparaissent, laissant entrevoir une lave incandescente.",
            font, clock
        )

        # Ajout d’un choix interactif
        choix = display_choices_box(screen, font, [
            ("Contourner le Gardien et frapper depuis les flancs.", 0),
            ("Tirer une flèche vers son orbe lumineux avec Ayela.", 1),
            ("Utiliser la vitesse de Gallius pour qu'il frappe sans relâche.", 2),
        ], clock)

        # Résolution des choix
        if choix == 0:
            display_dialogue_box(
                screen,
                "Vous signalez à vos compagnons de distraire le Gardien pendant que vous contournez par le flanc. "
                "Vos pas rapides sur les pierres brûlantes attirent son attention, et dans un moment d’ouverture, "
                "vous portez un coup précis. Le Gardien titube, mais reste debout.",
                font, clock
            )
        elif choix == 1:
            display_dialogue_box(
                screen,
                "Ayela bande son arc, fixant l’orbe lumineux au centre de la poitrine du Gardien. "
                "La flèche s’élance, perçant la lumière incandescente. Une explosion de flammes aveugle la salle, "
                "forçant le Gardien à reculer. Une partie de son armure se brise, révélant un noyau fragile.",
                font, clock
            )
            hero.get_relation("Ayela").adjust_score(+5)  # Relation renforcée
        elif choix == 2:
            display_dialogue_box(
            screen,
                "Gallius se met à courir, ses dagues brillantes dans la pénombre. "
                "Il bondit sur la créature avec agilité, tourbillonnant autour de l’ancien Gardien des flammes. "
                "La chaleur devient presque insoutenable, l’air lourd et étouffant. "
                "Gallius enchaîne des attaques rapides, ses dagues traçant des arcs scintillants dans l’air, "
                "taillant le Gardien avec la précision d’une roue tranchante.",
                font, clock
            )
            hero.get_relation("Gallius").adjust_score(+5)  # Relation renforcée
            # Transition vers une nouvelle phase ou conclusion
        display_dialogue_box(
            screen,
            "Le Gardien recule une dernière fois, laissant échapper un grondement sourd. "
            "Les flammes autour de lui vacillent, et l’air devient légèrement plus supportable. Vous sentez que le combat touche à sa fin, "
            "mais une ultime attaque pourrait sceller votre sort.",
            font, clock
            )

        options_combat_final = [
        ("Aldric frappe directement le cœur.", +15, "Ayela", +15, "Gallius", +15, "Velm"),
        ("Ayela tire une flèche au cœur.", -20, "Aldric", +25, "Ayela", +10, "Brandio"),
        ("Gallius se hâte sur le cœur et donne une pluie de coups.", +20, "Gallius", +20, "Velm", +20, "Brandio")
        ]
        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_combat_final], clock)

        if choix == 0:  # Aldric frappe directement le cœur
            display_dialogue_box(
                screen,
                "Aldric fonce, ignorant la chaleur brûlante qui envahit la pièce. Son épée courte s'enfonce profondément dans le cœur incandescent. La créature laisse échapper un dernier cri avant de s'effondrer dans un torrent de cendres.",
                font, clock
            )
            display_dialogue_with_sprite(screen, "Ayela (soulagée) : Tu es cinglé… mais c'était magnifique.", font, clock, sprite_ayela)
            display_dialogue_with_sprite(screen, "Gallius (léger sourire) : Direct, J'aime ça...", font, clock, sprite_gallius)
            hero.get_relation("Ayela").adjust_score(+15)
            hero.get_relation("Gallius").adjust_score(+15)

            if hero.get_relation("Velm"):
                display_dialogue_with_sprite(screen, "Velm (hésitant) : Je suppose que Brandio aurait approuvé ce genre de folie…", font, clock, sprite_velm)
                hero.get_relation("Velm").adjust_score(+15)

            if hero.get_relation("Brandio"):
                display_dialogue_with_sprite(screen, "Brandio (fixant les cendres du gardien) : Velm aurait ri… Je crois qu'il te pardonnerait aussi.", font, clock, sprite_brandio)
                hero.get_relation("Brandio").adjust_score(+15)

        elif choix == 1:  # Ayela tire une flèche au cœur
            display_dialogue_box(
                screen,
                "Ayela recule de quelques pas, tend son arc avec précision et décoche une flèche éclatante. La flèche fend l'air et transperce le cœur du gardien, déclenchant une explosion de flammes. Aldric est projeté en arrière. (-20 PV Aldric)",
                font, clock
            )
            hero.adjust_health(-20)
            display_dialogue_with_sprite(screen, "Ayela (accourant vers Aldric) : Aldric ! Ça va ?", font, clock, sprite_ayela)
            hero.get_relation("Ayela").adjust_score(+25)

            if hero.get_relation("Velm"):
                display_dialogue_with_sprite(screen, "Velm (observant Ayela) : Ça, c'est du tir.", font, clock, sprite_velm)
                hero.get_relation("Velm").adjust_score(+10)

            if hero.get_relation("Brandio"):
                display_dialogue_with_sprite(screen, "Brandio (amusé) : Ah, cette fille est dangereuse… Je suppose que Velm aurait applaudi.", font, clock, sprite_brandio)
                hero.get_relation("Brandio").adjust_score(+10)

        elif choix == 2:  # Gallius se hâte sur le cœur et donne une pluie de coups
            display_dialogue_box(
                screen,
                "Gallius bondit sans hésitation, ses dagues traçant des arcs lumineux autour du cœur du gardien. Les flammes s'éparpillent alors qu'il frappe sans relâche. Une fissure apparaît soudainement sur le cœur.",
                font, clock
            )
            display_dialogue_with_sprite(screen, "Gallius (grimaçant) : C'est maintenant ou jamais, Aldric !", font, clock, sprite_gallius)
            hero.get_relation("Gallius").adjust_score(+20)

            if hero.get_relation("Velm"):
                display_dialogue_with_sprite(screen, "Velm (fonçant) : Je suis pas aveugle !", font, clock, sprite_velm)
                hero.get_relation("Velm").adjust_score(+20)

            if hero.get_relation("Brandio"):
                display_dialogue_with_sprite(screen, "Brandio (grinçant des dents) : J'arrive. Pas besoin de me presser.", font, clock, sprite_brandio)
                hero.get_relation("Brandio").adjust_score(+20)

        # Post-choix narration
        # Narration de la victoire
        display_dialogue_box(
        screen,
        "Le cœur du Gardien explose, remplissant la salle d'une lumière incandescente qui vous éblouit tous. "
        "Un hurlement guttural résonne, et la chaleur oppressante disparaît soudainement, remplacée par une brise légère et apaisante. "
        "Le colosse de flammes vacille, puis s’effondre lourdement au sol dans un fracas assourdissant. "
        "Son corps, bien qu’immobile, ne disparaît pas, ses flammes vacillantes laissant place à une masse noire et calcinée. "
        "Alors que le silence s’installe, une lueur attire votre attention : une gemme brillante émerge lentement de son torse. "
        "Elle tombe avec un léger tintement et rebondit sur le sol de pierre avant de s’immobiliser, scintillant faiblement dans la pénombre.",
        font, clock)

        # Réactions des personnages
        if hero.get_relation("Brandio"):
            display_dialogue_with_sprite(
                screen,
                "Brandio (laissant échapper un soupir de soulagement) : Hah… C’est fini. Enfin. "
                "Je vais être honnête, Aldric… Je t’ai rarement trouvé inutile.",
                font, clock, sprites["Brandio"]
            )

            display_dialogue_with_sprite(
                screen,
                "Aldric (calme, relevant légèrement la tête) : Toujours aussi direct, Brandio. Mais je suppose que tu as plus à dire, non ?",
                font, clock, sprites["Aldric"]
            )

            display_dialogue_with_sprite(
                screen,
                "Brandio (baissant légèrement la tête) : Oui, écoute… Je t’ai jugé trop vite. Maintenant, je vois que c’est Clotaire qui a causé la perte de Velm. "
                "Et je comprends… Tu ne pouvais pas sacrifier Kael. Ce choix… c’était impossible à faire.",
                font, clock, sprites["Brandio"]
            )

            display_dialogue_with_sprite(
            screen,
            "Aldric (soupirant légèrement) : Velm… Pour être honnête, c’était un imbécile. Je ne le connaissais pas vraiment. "
            "Et Kael… il n’est pas mieux. Peut-être encore plus insupportable. Pour être franc, je ne sais moi même pas pourquoi je l’ai préservé. je le connais a peine...",
            font, clock, sprites["Aldric"]
            )

            display_dialogue_with_sprite(
                screen,
                "Brandio (tendant la main) : Alors, trêve de rancune. On avance ensemble, d’accord ?",
                font, clock, sprites["Brandio"]
            )

            display_dialogue_with_sprite(
                screen,
                "Aldric (saisissant sa main) : Ensemble. On est tous dans cette tour pour une raison. Et la prochaine fois… on essaiera de ne plus perdre personne.",
                font, clock, sprites["Aldric"]
            )
        if hero.get_relation("Velm"):
            display_dialogue_with_sprite(
                screen,
                "Velm (essuyant son front) : Enfin ! Je n’en peux plus de cette chaleur… Mais écoute, Aldric, on doit parler.",
                font, clock, sprites["Velm"]
            )

            display_dialogue_with_sprite(
                screen,
                "Aldric (calme, croisant les bras) : Parler de quoi, Velm ? Si c’est pour m’accuser encore, je n’ai ni le temps ni l’envie.",
                font, clock, sprites["Aldric"]
            )

            display_dialogue_with_sprite(
                screen,
                "Velm (secouant la tête) : Non, pas cette fois. Écoute, je dois être honnête. Clotaire a fait n’importe quoi dans cette épreuve avec les gargouilles. "
                "Et Kael… franchement, c’est un abruti. Mais malgré ça, tu l’as préservé. Pourquoi ?",
                font, clock, sprites["Velm"]
            )

            display_dialogue_with_sprite(
                screen,
                "Aldric (soupirant légèrement) : Velm, pour être honnête, je ne sais même pas moi-même pourquoi j’ai fait ça. Peut-être que c’était instinctif. "
                "Peut-être parce que, aussi insupportable soit-il, Kael avait encore une chance de s’en sortir. Ou peut-être que je suis juste idiot.",
                font, clock, sprites["Aldric"]
            )

            display_dialogue_with_sprite(
                screen,
                "Velm (le regard fixe) : Peut-être un peu des deux. Mais ce n’est pas le point. Clotaire a causé la perte de beaucoup, et j’ai été injuste envers toi. "
                "Maintenant, je vois que tu fais ce que tu peux avec ce qu’on te donne.",
                font, clock, sprites["Velm"]
            )

            display_dialogue_with_sprite(
                screen,
                "Aldric (haussant un sourcil) : Est-ce que c’est toi qui essaies de me dire que tu me fais confiance maintenant ?",
                font, clock, sprites["Aldric"]
            )

            display_dialogue_with_sprite(
                screen,
                "Velm (soupirant) : Pas complètement. Mais on n’a pas le luxe de se méfier les uns des autres. Si on veut survivre dans cette Tour, on doit travailler ensemble.",
                font, clock, sprites["Velm"]
            )

            display_dialogue_with_sprite(
                screen,
                "Aldric (avec un léger sourire) : C’est un début. Je peux vivre avec ça.",
                font, clock, sprites["Aldric"]
            )

        # Réactions générales
        display_dialogue_box(
            screen,
            "Le groupe laisse échapper un soupir collectif de soulagement. Gallius range ses dagues, "
            "et Ayela s’adosse au mur, reprenant son souffle. L’épreuve a laissé des traces, mais vous avez survécu… ensemble.",
            font, clock
        )

        display_dialogue_with_sprite(
            screen,
            "Aldric (calme) : Merci… à tous. Je sais que parfois je peux être imbuvable.. je parle peu, et j’agis souvent dans mon interet. "
            "Mais sans vous, je n’aurais jamais réussi à aller si haut. "
            "Avec ceux qui restent en vie, on peut aller loin dans la Tour… tant qu’on arrive à s’entendre.",
            font, clock, sprites["Aldric"]
        )

        display_dialogue_with_sprite(
            screen,
            "Ayela (souriant légèrement) : Tu parles comme un chef, Aldric. J'ai bien fait de te suivre !",
            font, clock, sprites["Ayela"]
        )

        display_dialogue_with_sprite(
            screen,
            "Gallius (regardant autour de lui) : La Tour ne nous laissera pas beaucoup de temps pour célébrer. "
            "Préparons-nous pour ce qui nous attend au prochain étage.",
            font, clock, sprites["Gallius"]
        )
        
        if hero.get_relation("Velm"):
            display_dialogue_box(
            screen,
            "Velm s’avance prudemment vers la gemme, la ramassant du bout des doigts.",
            font, clock
            )
            display_dialogue_box(
                screen,
                "Un faible éclat rouge danse à sa surface. Velm la lève un instant à la lumière, son regard perdu dans ses pensées.",
                font, clock
            )

        if hero.get_relation("Brandio"):
            display_dialogue_box(
                screen,
                "Brandio s’approche de la gemme écarlate, son sourire habituel effacé, laissant place à une gravité rare.",
                font, clock
            )
            display_dialogue_box(
                screen,
                "Il l’observe un moment, comme s’il voyait enfin quelque chose au-delà des murs de cette tour maudite.",
                font, clock
            )

            

        if hero.get_relation("Velm"):
            display_dialogue_box(
                screen,
                "Velm ne répond pas immédiatement. Il fixe la gemme, la serrant dans sa paume, avant de se retourner lentement, faisant quelques pas vers Aldric.",
                font, clock
            )
            display_dialogue_with_sprite(screen, "Velm (d’une voix rauque) : Aldric...Mefie toi de Clotaire, il est fourbe..", font, clock, sprite_velm)
            display_dialogue_with_sprite(screen, "Velm (tendant la gemme à Aldric) : Ensemble on peut gravir la tour !", font, clock, sprite_velm)
            display_dialogue_with_sprite(
                screen, 
                "Gallius (sombre) : Hé… Ne tourne pas le dos à cette chose. On sait pas si elle est morte, tsss.", 
                font, clock, sprites["Gallius"]
            )

            display_dialogue_box(
                screen, 
                "Velm, inconscient du danger, baisse son arme et commence à s’éloigner. "
                "Derrière lui, le corps du Gardien émet une lueur sinistre. "
                "Soudain, une main massive et calcinée surgit, se refermant autour de lui dans un mouvement brutal et implacable. "
                "Velm se débat, frappant frénétiquement la main du Gardien, mais l’étreinte est trop puissante.",
                font, clock
            )

            display_dialogue_with_sprite(
                screen, 
                "Velm (hurlant) : Aidez-moi ! Je… je ne peux pas m’échapper !", 
                font, clock, sprites["Velm"]
            )

            display_dialogue_box(
                screen, 
                "Le Gardien, dans un dernier acte de vengeance, lève son bras, soulevant Velm dans les airs. "
                "Une chaleur écrasante entoure Velm alors que la lumière de la salle semble s’intensifier. ",
                font, clock
            )

            display_dialogue_with_sprite(
                screen, 
                "Gallius (abasourdi) : Tsss… Je t’avais prévenu, Velm. Cette tour n’a pas de pitié.", 
                font, clock, sprites["Gallius"]
            )
           
            display_dialogue_box(
                screen,
                "Trop tard pour réagir, la créature empoigne Velm, le soulevant dans les airs dans un cri de douleur.",
                font, clock
            )
            display_dialogue_with_sprite(screen, "Velm (hurlant) :Aaaa.. Aldric ! Attrape ça !", font, clock, sprite_velm)
            display_dialogue_box(
                screen,
                "(Il jette la gemme vers Aldric, juste avant que ses cris ne soient étouffés par la poigne du gardien.)",
                font, clock
            )
            display_dialogue_box(
                screen,
                "La créature tire sur Velm avec une force inhumaine. Son corps se disloque avant de retomber de façon brutal, sans vie, sur le sol noirci. Le gardien disparait.",
                font, clock
            )

        if hero.get_relation("Brandio"):
            display_dialogue_box(
                screen,
                "Brandio fait tournoyer la gemme dans sa main, levant un sourcil vers Aldric.",
                font, clock
            )
            display_dialogue_with_sprite(screen, "Brandio : Écoute, Aldric… Clotaire est un crétin, fait attention à lui, il ne te pardonnera pas...", font, clock, sprite_brandio)
            display_dialogue_with_sprite(screen, "Brandio (lui lançant doucement la gemme) : Tiens… T'es un bon Aldric, On va aller au bout !", font, clock, sprite_brandio)
            display_dialogue_with_sprite(
                screen, 
                "Gallius (sombre) : Hé… Ne tourne pas le dos à cette chose. On sait pas si elle est morte, tsss.", 
                font, clock, sprites["Gallius"]
            )

            display_dialogue_box(
                screen, 
                "Alors que Gallius termine sa phrase, un grondement sourd secoue la pièce. "
                "Le corps calciné du Gardien tremble, puis se redresse brusquement, projetant un torrent de flammes autour de lui. "
                "Brandio, pris au dépourvu, se retrouve directement dans la trajectoire des flammes. "
                "Il essaie désespérément de résister, son bouclier levé pour se protéger, mais les flammes l’enveloppent rapidement. "
                "Dans un dernier regard, il fixe le groupe, réalisant qu’il ne pourra pas s’échapper.",
                font, clock
            )

            display_dialogue_with_sprite(
                screen, 
                "Brandio (criant) : Continuez… finissez cette maudite épreuve ! Vous n’avez pas le choix !", 
                font, clock, sprites["Brandio"]
            )

            display_dialogue_box(
                screen, 
                "Les flammes dévorent Brandio, son cri s’éteignant dans le rugissement du feu. "
                "Quand le Gardien retombe à genoux, immobile cette fois, il ne reste plus qu’un silence pesant et une odeur de cendres.",
                font, clock
            )
            display_dialogue_box(
                screen,
                "Une ultime flamme jaillit des cendres, enveloppant Brandio dans une explosion brutale.",
                font, clock
            )
            display_dialogue_box(
                screen,
                "Brandio se redresse un instant, un sourire fataliste aux lèvres, avant de disparaître dans le brasier.",
                font, clock
            )
            display_dialogue_with_sprite(screen, "Brandio (en riant malgré les flammes) : Hé, Aldric… Garde ça précieusement. On dirait que j’vais enfin faire mon fameux voyage...adieu petit gars...Va au bout pour Velm et moi !", font, clock, sprite_brandio)
            
            display_dialogue_box(
                screen,
                "Brandio disparaît dans une volée de cendres, son rire s’éteignant en même temps que les flammes autour de lui. Le gardien disparait.",
                font, clock
            )
        
        fade_out_music(fade_duration=1000)
        fade_in_music("graphics/resources/music/nature.mp3", max_volume=0.2, fade_duration=1000)
        # Réactions des survivants
        background = fade_in_background(screen,"graphics/resources/backgrounds/feu.webp", WIDTH, HEIGHT)
        display_dialogue_with_sprite(
            screen, 
            "Ayela (les larmes aux yeux) : Pourquoi faut-il toujours que quelqu’un…", 
            font, clock, sprite_ayela
        )
        display_dialogue_box(
            screen, 
            "(Sa voix s’étrangle dans un sanglot qu’elle tente de cacher.)", 
            font, clock
        )
        display_dialogue_with_sprite(
            screen, 
            "Aldric (fixant la gemme dans sa main) : Pauvre gars, il s'est bien battu.. ! J'espère qu'ils voyageront ensemble avec son ami là où ils sont...", 
            font, clock, sprite_aldric
        )
        display_dialogue_with_sprite(
            screen, 
            "Ayela : Aldric...", 
            font, clock, sprite_ayela
        )
        display_dialogue_box(
            screen, 
            "Aldric serre la gemme dans sa paume, son expression impassible masquant la lourdeur de la perte.", 
            font, clock
        )
        display_dialogue_with_sprite(
            screen, 
            "Gallius (croisant les bras, fixant les cendres) : C’est la tour. Elle prend tout. Même ceux qui font la paix trop tard.", 
            font, clock, sprite_gallius
        )
        display_dialogue_box(
            screen, 
            "Il détourne les yeux et s’approche de la porte, prêt à quitter cette salle funeste.", 
            font, clock
        )

        # Clôture de la scène
        display_dialogue_with_sprite(
            screen, 
            "Ayela (murmurant) : Il ne devait pas mourir comme ça…", 
            font, clock, sprite_ayela
        )
        display_dialogue_box(
            screen, 
            "(Elle regarde Aldric, cherchant ses mots.)", 
            font, clock
        )
        display_dialogue_with_sprite(
            screen, 
            "Aldric (d’un ton ferme) : Non… Mais on doit continuer. Il ne voudrait pas qu’on s’arrête ici.", 
            font, clock, sprite_aldric
        )

        # Choix face à Ayela
        options_confort = [
            ("Prendre Ayela dans ses bras pour la réconforter.", +30, "Ayela"),
            ("Tourner le dos à la salle et l’encourager à avancer.", 0, None)
        ]
        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_confort], clock)

        if choix == 0:  # Prendre Ayela dans ses bras
            display_dialogue_box(
                screen, 
                "Aldric s'approche doucement et serre Ayela dans ses bras. Elle se crispe d'abord, puis finit par s'abandonner un instant, posant sa tête contre son épaule.", 
                font, clock
            )
            display_dialogue_with_sprite(
                screen, 
                "Ayela (d’une voix tremblante) : Aldric...Je..", 
                font, clock, sprite_ayela
            )
            display_dialogue_box(
                screen, 
                "Elle reste ainsi quelques secondes, reprenant lentement ses esprits. Lorsqu’elle se recule, ses yeux sont plus fermes, plus décidés.", 
                font, clock
            )
            display_dialogue_with_sprite(
                screen, 
                "Ayela (avec un léger sourire) : Tu es plus tendre que tu n’en as l’air", 
                font, clock, sprite_ayela
            )
            display_dialogue_with_sprite(
                screen, 
                "Aldric (souriant) : Hm...T'habitue pas trop..", 
                font, clock, sprite_aldric
            )
            hero.get_relation("Ayela").adjust_score(+30)

        elif choix == 1:  # Tourner le dos
            display_dialogue_box(
                screen, 
                "Aldric détourne les yeux des cendres et avance vers la porte.", 
                font, clock
            )
            display_dialogue_with_sprite(
                screen, 
                "Aldric (calmement, sans se retourner) : Viens, Ayela. On a déjà trop perdu de temps ici.", 
                font, clock, sprite_aldric
            )
            display_dialogue_box(
                screen, 
                "Ayela essuie une larme discrète avant de le suivre en silence.", 
                font, clock
            )
            

        # Clôture finale
            display_dialogue_box(
            screen, 
            "La porte de sortie s’ouvre lentement dans un souffle de braise. Vous quittez la salle, laissant derrière vous les cendres de votre compagnon tombé.", 
            font, clock
            )
            fade_out_music(fade_duration=1000)
    floor6_fire(hero, screen, font, clock, sprites)
    def floor6_air(hero, screen, font, clock, sprites):
        global background
        background = fade_in_background(screen,"graphics/resources/backgrounds/air.webp", WIDTH, HEIGHT)
        display_dialogue_box(
        screen,
        "Pendant ce temps - Étage 6 : Épreuve de la Salle de l'Air",
        font, clock
        )
        fade_in_music("graphics/resources/music/elysium.mp3", max_volume=0.2, fade_duration=1000)

        # Narration de l'entrée
        display_dialogue_box(
            screen,
            "La porte glisse lentement derrière vous, se refermant dans un silence pesant. "
            "L’air devient frais et vibrant, presque vivant. Vous vous retrouvez dans une salle cylindrique, plus étroite que les autres. "
            "Un immense cylindre métallique tourne lentement au centre, entouré de tuyaux de cuivre soufflant des brises irrégulières.",
            font, clock
        )

        # Présentation des personnages
        display_dialogue_with_sprite(screen, "Kael (serrant les dents) : Parfait… une salle musicale. On va jouer de la flûte géante maintenant ?", font, clock, sprite_kael)
        display_dialogue_with_sprite(screen, "Clotaire (ricanant) : Je suis sûr que tu es un virtuose. Après tout, la noblesse adore ce genre de raffinement.", font, clock, sprite_clotaire)
        display_dialogue_with_sprite(screen, "Kael (jetant un regard noir à Clotaire) : Tu devrais plutôt écouter. C’est la seule chose que tu maîtrises...et encore..", font, clock, sprite_kael)
        display_dialogue_with_sprite(screen, "Garen (fixant le cylindre) : Ce n’est pas de la musique. C’est une énigme sonore.", font, clock, sprite_garen)
        display_dialogue_with_sprite(screen, "Emphyr (calme, posant une main sur un tuyau) : Il y a de la magie ici. L’air vibre différemment. Nous allons devoir harmoniser ces vents.", font, clock, sprite_emphyr)

        # Description du cylindre
        display_dialogue_box(
            screen,
            "Un cylindre gravé tourne au centre de la salle. Cinq tuyaux soufflent des brises discordantes, créant une cacophonie. "
            "Quatre valves entourent le cylindre, suggérant une manipulation nécessaire.",
            font, clock
        )

        # Apparition du sablier
        display_dialogue_box(
            screen,
            "Un sablier noir descend du plafond, suspendu au-dessus du cylindre. "
            "Du sable doré s’écoule lentement, mais chaque note discordante accélère son flux.",
            font, clock
        )
        display_dialogue_box(
            screen,
            "Inscription sur le sablier : Lorsque le dernier grain tombera, la mélodie du vent cessera, emportant ceux qui n’ont pas su l’écouter.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Kael (fronçant les sourcils) : On est pressés… évidemment.", font, clock, sprite_kael)
        display_dialogue_with_sprite(screen, "Clotaire (d’un ton moqueur, observant Garen) : Un peu de pression… c’est justement ce qu’il faut pour voir qui craque en premier.", font, clock, sprite_clotaire)
        display_dialogue_with_sprite(screen, "Garen (croisant les bras) : Tu crois vraiment que tes provocations vont aider ?", font, clock, sprite_garen)
        display_dialogue_with_sprite(screen, "Emphyr (d’un ton posé, mais ferme) : Ça suffit. Plus on se trompe, plus le sablier s’accélère. Évitez de vous disputer.", font, clock, sprite_emphyr)
        
        # Phase 1 – Premiers essais
        display_dialogue_box(
            screen,
            "Phase 1 : Observation et Premiers Essais",
            font, clock
        )
        display_dialogue_box(
            screen,
            "Garen s’approche et tourne doucement une valve. Un son grave résonne harmonieusement avant d’être perturbé par un autre tuyau.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Kael (hausse un sourcil) : Et Paysan tu crois vraiment pouvoir régler ça tout seul ?", font, clock, sprite_kael)
        display_dialogue_with_sprite(screen, "Clotaire (souriant en coin) : Laisse-le. C’est toujours amusant de voir des trayeurs de vaches essayer de bricoler.", font, clock, sprite_clotaire)
        display_dialogue_with_sprite(screen, "Garen (jetant un regard irrité) : Je n’ai pas besoin de vos commentaires.", font, clock, sprite_garen)
        display_dialogue_with_sprite(screen, "Kael (ricanant doucement) : Pour une fois, je suis d’accord avec Garen. Ferme-la, Clotaire.", font, clock, sprite_kael)
        display_dialogue_with_sprite(screen, "Garen : Ca vaut aussi pour toi !", font, clock, sprite_garen)
        display_dialogue_with_sprite(screen, "Emphyr (croisant les bras, essayant de rester diplomate) : Vous trois… vous pouvez vous disputer après que la salle soit résolue.", font, clock, sprite_emphyr)

        # Clôture de la phase
        display_dialogue_box(
            screen,
            "Clotaire hausse les épaules avec nonchalance, mais son sourire ne disparaît pas. "
            "Kael et Garen échangent des regards furtifs, la tension palpable. "
            "Pendant ce temps, Emphyr continue d’analyser silencieusement le mécanisme du cylindre.",
            font, clock
        )
        
        # Début des choix d'observation
        options_observation = [
            ("Laisser Garen continuer seul.", 0),
            ("Intervenir et proposer à Kael d’aider.", 1),
            ("Demander à Emphyr de prendre la tête.", 2)
        ]

        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_observation], clock)

        if choix == 0:  # Laisser Garen continuer seul
            display_dialogue_box(
                screen,
                "Garen persiste malgré les moqueries, ajustant la valve à nouveau. Une note harmonieuse retentit, mais une autre valve siffle immédiatement en retour.",
                font, clock
            )
            display_dialogue_with_sprite(screen, "Garen (serrant les poings) : C’est plus compliqué que prévu…", font, clock, sprite_garen)
            display_dialogue_with_sprite(screen, "Clotaire (ricanant) : Sans blague. Peut-être qu’on devrait te laisser seul gérer tout ça.", font, clock, sprite_clotaire)

        elif choix == 1:  # Intervenir et proposer à Kael d’aider
            display_dialogue_box(
                screen,
                "Kael s’approche à contrecœur, lançant un regard ennuyé à Garen.",
                font, clock
            )
            display_dialogue_with_sprite(screen, "Kael : Bon… ça m’ennuie, mais autant que ce soit fait correctement.", font, clock, sprite_kael)
            display_dialogue_with_sprite(screen, "Garen (soufflant) : Fais ce que tu veux, mais ne gêne pas.", font, clock, sprite_garen)

        elif choix == 2:  # Demander à Emphyr de prendre la tête
            display_dialogue_box(
                screen,
                "Emphyr hoche la tête et s’avance, tournant une valve elle-même.",
                font, clock
            )
            display_dialogue_with_sprite(screen, "Emphyr : Il faut écouter attentivement… Les tuyaux ne mentent pas.", font, clock, sprite_emphyr)
            display_dialogue_box(
                screen,
                "Kael et Garen échangent un regard mais ne s’opposent pas.",
                font, clock
            )
            # Début de la Phase 2 : Manipulation des Valves
        display_dialogue_box(screen, 
            "Phase 2 : Manipulation des Valves", 
            font, clock
        )

        # Narration
        display_dialogue_box(screen, 
            "Un silence tendu s'installe alors que le sablier continue de s’écouler lentement. "
            "Les brises discordantes s’entrelacent dans l’air, formant un mélange désagréable qui semble refléter "
            "l’ambiance entre les membres de l’équipe.", 
            font, clock
        )

        # Dialogue des personnages
        display_dialogue_with_sprite(screen, 
            "Kael (les bras croisés, fixant le cylindre) : On ne va pas rester là à admirer le décor. Quelqu’un doit tourner ces fichues valves.", 
            font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen, 
            "Garen (lui lançant un regard en biais) : Tu es soudain motivé à aider ? Je pensais que tu préférais regarder de loin.", 
            font, clock, sprite_garen
        )
        display_dialogue_with_sprite(screen, 
            "Clotaire (ricanant doucement) : Continuez… vous êtes presque aussi divertissants que cette énigme.", 
            font, clock, sprite_clotaire
        )

        # Narration
        display_dialogue_box(screen, 
            "Emphyr pousse un léger soupir, détournant les yeux du sablier pour observer chacun d’eux en silence.", 
            font, clock
        )

        display_dialogue_with_sprite(screen, 
            "Emphyr (calme mais ferme) : Il va falloir que vous coopériez, ou on ne passera jamais cette épreuve.", 
            font, clock, sprite_emphyr
        )

        display_dialogue_with_sprite(screen, 
            "Kael (levant un sourcil) : Et qui t’a désignée comme chef, Emphyr ?", 
            font, clock, sprite_kael
        )
        display_dialogue_with_sprite(
        screen,
        "Emphyr (croisant les bras) : Personne. Mais si vous continuez à vous engueuler, ce cylindre ne bougera pas d’un pouce, "
        "et nous resterons enfermés dans cette salle pour toujours.",
        font, clock, sprite_emphyr
        )
        # Narration
        display_dialogue_box(screen, 
            "Les mots d’Emphyr semblent résonner un instant. Kael détourne le regard, visiblement peu enclin à argumenter davantage.", 
            font, clock
        )

        display_dialogue_with_sprite(screen, 
            "Garen (se redressant, posant la main sur une valve) : Je vais commencer par celle du centre. Ça ira plus vite que d’attendre que vous vous décidiez.", 
            font, clock, sprite_garen
        )
        display_dialogue_with_sprite(screen, 
            "Clotaire (ricane, adossé à un pilier) : Oh, voilà qu’il se donne des airs de héros… Mais vas-y, ça pourrait être amusant.", 
            font, clock, sprite_clotaire
        )

        # Narration
        display_dialogue_box(screen, 
            "Kael finit par s’approcher, posant nonchalamment la main sur une valve, bien qu’il évite de croiser le regard de Garen.", 
            font, clock
        )

        display_dialogue_with_sprite(screen, 
            "Kael : Je suppose que je n’ai pas le choix. Plus vite c’est fait, plus vite on pourra sortir d’ici.", 
            font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen, 
            "Emphyr (hochant la tête) : Je prendrai celle du haut. Concentrez-vous, ce n’est pas un simple jeu.", 
            font, clock, sprite_emphyr
        )

        # Narration pour clôturer la phase
        display_dialogue_box(screen, 
            "Les membres de l’équipe se positionnent autour du cylindre, prêts à manipuler les valves. "
            "Le bruit du sablier et des brises discordantes continue de hanter la salle, leur rappelant que chaque erreur pourrait être fatale.", 
            font, clock
        )
        # Présentation des choix
        options_valve = [
            ("Garen – Valve centrale (leader).", 0),
            ("Kael – Valve gauche.", 1),
            ("Emphyr – Valve supérieure.", 2)
        ]

        choix = display_choices_box(screen, font, options_valve, clock)

        # Résolution des choix
        if choix == 0:  # Garen – Valve centrale
            display_dialogue_with_sprite(screen, 
                "Garen (déterminé, serrant la valve) : Je vais m’en charger. Ça ne peut pas être si compliqué.", 
                font, clock, sprite_garen
            )
            display_dialogue_box(screen, 
                "Les tuyaux commencent à s'aligner, bien qu'ils tournent tous dans des directions différentes.", 
                font, clock
            )

        elif choix == 1:  # Kael – Valve gauche
            display_dialogue_with_sprite(screen, 
                "Kael (jetant un regard à Clotaire) : Je suppose que je suis coincé ici.", 
                font, clock, sprite_kael
            )
            display_dialogue_with_sprite(screen, 
                "Clotaire (moqueur) : Coincé, oui. À ton habitude. Noble ahah, coincé, tu l’as ?!", 
                font, clock, sprite_clotaire
            )
            display_dialogue_with_sprite(screen, 
                "Kael : J’ai envie de trancher ta langue, maudit voleur de ruelle !", 
                font, clock, sprite_kael
            )
            display_dialogue_with_sprite(screen, 
                "Clotaire : Oooh il m’a insulté ! Emphyr au secours (mimant être triste).", 
                font, clock, sprite_clotaire
            )

        elif choix == 2:  # Emphyr – Valve supérieure
            display_dialogue_with_sprite(screen, 
                "Emphyr (calmement) : Très bien, je prends celle-ci. Restez concentrés.", 
                font, clock, sprite_emphyr
            )
            display_dialogue_with_sprite(screen, 
                "Garen : Allons-y ! En même temps !", 
                font, clock, sprite_garen
            )
            display_dialogue_with_sprite(screen, 
                "Emphyr : Je te suis, Garen (dit-elle avec un sourire charmeur, alors que Garen tourne la valve en rougissant).", 
                font, clock, sprite_emphyr
            )

        # Clôture de la phase
        display_dialogue_box(screen, 
            "Les valves commencent à tourner simultanément, générant une série de notes qui résonnent dans la salle. "
            "Le sablier ralentit légèrement, indiquant que vous progressez, mais le mécanisme reste instable.", 
            font, clock
        )
        # Présentation des dialogues et narration
        display_dialogue_box(screen, 
            "Alors que les valves sont manipulées, une cinquième valve s’active d’elle-même, provoquant une rafale soudaine. "
            "Le sablier s’accélère, les grains chutant rapidement. L’air devient oppressant, et la tension monte.",
            font, clock
        )

        display_dialogue_with_sprite(screen, 
            "Kael (en reculant légèrement) : Ah… génial. Il en fallait une de plus.", 
            font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen, 
            "Garen (fronçant les sourcils) : On n’a pas le temps de tergiverser. Quelqu’un doit s’en occuper.", 
            font, clock, sprite_garen
        )
        display_dialogue_with_sprite(screen, 
            "Clotaire (amusé, regardant Kael) : Tu veux essayer, noble ? Après tout, tu aimes bien tout contrôler.", 
            font, clock, sprite_clotaire
        )
        display_dialogue_with_sprite(screen, 
            "Kael (agacé) : Ce n’est pas le moment, Roi des Voleurs.", 
            font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen, 
            "Emphyr (s’approchant) : Je vais m’en occuper. Concentrez-vous sur les vôtres.", 
            font, clock, sprite_emphyr
        )

        # Ajout de tension
        display_dialogue_box(screen, 
            "Un éclat de colère traverse brièvement le regard de Garen, mais il reste concentré sur la valve. "
            "Emphyr jette un regard glacial à Clotaire sans répondre.",
            font, clock
        )

        # Présentation des choix
        options_valve_finale = [
            ("Garen force seul sur la valve.", -5, "Garen"),
            ("Emphyr aide Garen avec la valve.", +10, "Emphyr", +5, "Garen"),
            ("Clotaire propose sarcastiquement son aide, mais refuse d'agir.", -10, "Clotaire")
        ]

        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_valve_finale], clock)

        # Résolution des choix
        if choix == 0:  # Garen force seul
            display_dialogue_with_sprite(screen, 
                "Garen (poussant sur la valve) : Allez… tourne… !", 
                font, clock, sprite_garen
            )
            display_dialogue_box(screen, 
                "Malgré ses efforts, la valve reste bloquée. La rafale devient plus intense, et le sablier accélère davantage.", 
                font, clock
            )
            hero.get_relation("Garen").adjust_score(-5)

        elif choix == 1:  # Emphyr aide Garen
            display_dialogue_with_sprite(screen, 
                "Emphyr (calme) : Garen, à deux, on peut y arriver.", 
                font, clock, sprite_emphyr
            )
            display_dialogue_with_sprite(screen, 
                "Garen (hochant la tête) : Merci… c’est parti !", 
                font, clock, sprite_garen
            )
            display_dialogue_box(screen, 
                "Ensemble, ils tournent la valve, et une note harmonieuse résonne enfin. Le sablier ralentit légèrement.", 
                font, clock
            )
            hero.get_relation("Emphyr").adjust_score(+10)
            hero.get_relation("Garen").adjust_score(+5)

        elif choix == 2:  # Clotaire sarcastique
            display_dialogue_with_sprite(screen, 
                "Clotaire (sarcastique, adossé au mur) : Je pourrais peut-être essayer… mais ce n’est pas vraiment mon style d’effort inutile.", 
                font, clock, sprite_clotaire
            )
            display_dialogue_with_sprite(screen, 
                "Kael (furieux) : Toujours aussi utile, Clotaire ! Tu es vraiment le pire des lâches !", 
                font, clock, sprite_kael
            )
            display_dialogue_box(screen, 
                "Les tensions montent entre Kael et Clotaire, mais personne n’intervient. La valve reste bloquée, et le sablier s’accélère.", 
                font, clock
            )
            hero.get_relation("Clotaire").adjust_score(-10)

        # Conclusion
        display_dialogue_box(screen, 
            "La salle entière semble vibrer sous la pression. Le groupe doit maintenant redoubler d’efforts pour résoudre l’énigme avant que le sablier ne se vide complètement.",
            font, clock
        )
        display_dialogue_box(
            screen,
            "La tension est palpable alors que la cinquième valve continue de tourner seule, provoquant des rafales imprévisibles. "
            "Le groupe doit agir rapidement pour éviter une catastrophe.",
            font, clock
        )

        # Clotaire exprime sa rancune
        display_dialogue_with_sprite(
            screen,
            "Clotaire (furieux) : Vous croyez vraiment qu’on va s’en sortir comme ça ? J'ai perdu un de mes meilleurs pote à cause de vous ! "
            "Si vous aviez écouté mes consignes, on n’en serait pas là !",
            font, clock, sprites["Clotaire"]
        )

        # Kael tient tête à Clotaire
        display_dialogue_with_sprite(
            screen,
            "Kael (froidement) : Ton arrogance te coûte cher, Clotaire. Peut-être que si tu passais moins de temps à aboyer des ordres "
            "et plus à réfléchir, ton ami serait encore là.",
            font, clock, sprites["Kael"]
        )

        # Emphyr tente de calmer les tensions
        display_dialogue_with_sprite(
            screen,
            "Emphyr (croisant les bras) : Ça suffit, tous les deux ! Ce sablier s’accélère, et si vous continuez, on restera enfermés ici. "
            "On n’a pas le temps pour vos querelles !",
            font, clock, sprites["Emphyr"]
        )

        # La tension monte malgré Emphyr
        display_dialogue_box(
            screen,
            "Malgré les avertissements d’Emphyr, Clotaire et Kael continuent de se défier du regard, leurs mots tranchants résonnant "
            "dans la salle. Le sablier, lui, semble s’accélérer encore, les grains tombant à une vitesse alarmante.",
            font, clock
        )

        # Garen intervient brusquement
        display_dialogue_with_sprite(
            screen,
            "Garen (élevant la voix) : Ça suffit ! ",
            font, clock, sprites["Garen"]
        )
        display_dialogue_box(
            screen,
            "Dans un élan inattendu, Garen, habituellement discret et peu confiant, s’avance vers Clotaire. "
            "Son poing s’abat violemment sur le visage de ce dernier, l’envoyant au sol.",
            font, clock
        )
        display_dialogue_with_sprite(
            screen,
            "Garen (hurlant) : Tout ça, c’est ta faute, Clotaire ! Si tu m’avais écouté lors de l’épreuve de l’Imperius Dex, ton ami serait encore en vie ! "
            "Mais non, tu devais faire à ta manière ! Tu es incapable d’assumer tes erreurs !",
            font, clock, sprites["Garen"]
        )

        # Clotaire refuse de se calmer
        display_dialogue_with_sprite(
            screen,
            "Clotaire (se relevant lentement) : Tu crois que crier et jouer les héros va changer quelque chose, paysan ? "
            "Il est mort parce que vous êtes tous des incapables !",
            font, clock, sprites["Clotaire"]
        )

        # Emphyr intervient à nouveau
        display_dialogue_with_sprite(
            screen,
            "Emphyr (impérieuse) : ASSEZ ! Nous n’avons pas le luxe de perdre plus de temps. "
            "Clotaire, si tu veux nous aider, libre à toi, mais ce sablier ne va pas nous attendre !",
            font, clock, sprites["Emphyr"]
        )

        # Le groupe reprend le contrôle
        display_dialogue_box(
            screen,
            "Malgré la tension, le groupe reprend la manipulation des valves. "
            "Les rotations ralentissent progressivement le sablier, et l’atmosphère oppressante dans la salle commence à s’atténuer légèrement. "
            "Mais la rancune de Clotaire demeure palpable.",
            font, clock
        )

    # Choix possibles pour résoudre le dilemme
        options_choix_final = [
            ("Garen force la valve seul.", 0),
            ("Kael aide Garen à tourner la valve.", 1),
            ("Clotaire sabote discrètement la valve.", 2),
            ("Emphyr agit rapidement seule.", 3)
        ]

        choix = display_choices_box(screen, font, [(option[0], option[1]) for option in options_choix_final], clock)

        # Résolution des choix
        if choix == 0:  # Garen force seul
            display_dialogue_with_sprite(
                screen,
                "Garen (grimaçant) : Je vais… y arriver…",
                font, clock, sprite_garen
            )
            display_dialogue_box(
                screen,
                "Il force de toutes ses forces, mais la valve ne cède qu’au dernier moment, "
                "envoyant une puissante bourrasque dans la salle. Il titube mais reste debout.",
                font, clock
            )
            display_dialogue_with_sprite(
                screen,
                "Emphyr (soupirant) : Têtu… mais efficace.",
                font, clock, sprite_emphyr
            )
            display_dialogue_with_sprite(
                screen,
                "Kael (croisant les bras) : Bien joué, Garen. Pas mal pour un fermier.",
                font, clock, sprite_kael
            )

        elif choix == 1:  # Kael aide Garen
            display_dialogue_with_sprite(
                screen,
                "Kael (soupire, s’approchant) : Bouge-toi… je vais t’aider.",
                font, clock, sprite_kael
            )
            display_dialogue_box(
                screen,
                "Kael attrape la valve avec Garen. Ensemble, ils parviennent à la faire tourner, réduisant la pression dans la salle.",
                font, clock
            )
            display_dialogue_with_sprite(
                screen,
                "Garen (léger sourire) : Merci…",
                font, clock, sprite_garen
            )
            display_dialogue_with_sprite(
                screen,
                "Kael (moqueur) : Ne t’habitue pas trop. Je ne suis pas ton acolyte.",
                font, clock, sprite_kael
            )

        elif choix == 2:  # Clotaire sabote
            display_dialogue_with_sprite(
                screen,
                "Clotaire (avec un sourire) : Oups… Quelle maladresse.",
                font, clock, sprite_clotaire
            )
            display_dialogue_box(
                screen,
                "Il fait semblant d’aider mais relâche volontairement son effort au dernier moment. "
                "Une bourrasque brutale souffle Garen contre le mur.",
                font, clock
            )
            display_dialogue_with_sprite(
                screen,
                "Emphyr (furieuse) : Clotaire !",
                font, clock, sprite_emphyr
            )
            display_dialogue_with_sprite(
                screen,
                "Clotaire (détendu) : Oh, c’était un accident…",
                font, clock, sprite_clotaire
            )

        elif choix == 3:  # Emphyr agit seule
            display_dialogue_with_sprite(
                screen,
                "Emphyr (se glissant près de Garen) : Je vais le régler. Écartez-vous.",
                font, clock, sprite_emphyr
            )
            display_dialogue_box(
                screen,
                "D’une main habile, Emphyr tourne la valve avec agilité, dissipant la bourrasque "  
                "avant qu’elle n’atteigne le reste du groupe.",
                font, clock
            )
            display_dialogue_with_sprite(
                screen,
                "Garen (lui jetant un regard reconnaissant) : Merci, Emphyr.",
                font, clock, sprite_garen
            )

        # Clôture de la scène
        display_dialogue_box(
            screen,
            "La dernière note résonne harmonieusement, et le sablier ralentit avant de s’immobiliser complètement. "
            "La cinquième valve cesse de tourner, et un silence apaisant s’installe dans la salle.",
            font, clock
        )
        
        # Fin de l'épreuve
        display_dialogue_box(
            screen,
            "Alors que la dernière valve est tournée, le cylindre ralentit, laissant place à une mélodie douce et envoûtante. "
            "Le sablier s’immobilise, ses derniers grains suspendus, signalant leur réussite.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Emphyr (léger sourire) : C’est terminé.", font, clock, sprite_emphyr)
        display_dialogue_with_sprite(screen, "Kael (croisant les bras) : On s’en est sorti… malgré quelques boulets.", font, clock, sprite_kael)
        display_dialogue_box(screen,
        "Clotaire ne répond pas. Il fixe silencieusement le cylindre, ses pensées ailleurs.",
        font, clock
        )

        # Développement de Clotaire
        display_dialogue_box(
            screen,
            "Dans le silence, Clotaire observe les autres, se tenant à l'écart. Son esprit retourne à des souvenirs lointains – "
            "des années de survie seul, volant pour manger, trahi à plusieurs reprises, jusqu’à ce qu’il rencontre Velm et Brandio. "
            "Pour la première fois, il avait eu des compagnons… mais la tour avait fini par en emporter un.",
            font, clock
        )

        display_dialogue_with_sprite(screen, "Garen (soufflant, s’adossant au mur) : On l’a fait…", font, clock, sprite_garen)
        display_dialogue_box(
            screen,
            "Il jette un regard furtif à Emphyr, un léger sourire aux lèvres, mais détourne rapidement les yeux.",
            font, clock
        )

        display_dialogue_box(
            screen,
            "La porte s’ouvre lentement, révélant un passage vers l’étage suivant. "
            "Alors que Kael et Garen passent devant, Emphyr s’attarde un instant aux côtés de Clotaire.",
            font, clock
        )

        # Interaction entre Clotaire et Emphyr
        display_dialogue_with_sprite(screen, "Emphyr (doucement) : Tu aurais pu nous aider, Clotaire.", font, clock, sprite_emphyr)
        
        display_dialogue_box(
        screen,"Clotaire ne la regarde pas, les yeux rivés sur la sortie.",
        font, clock
        )
        display_dialogue_with_sprite(screen, "Clotaire (voix basse) : J’ai appris à ne compter que sur moi-même. C’est plus sûr. Mais j'ai oublié que je suis ton larbin.", font, clock, sprite_clotaire)
        display_dialogue_with_sprite(screen, "Emphyr (le regardant avec compassion) : Tu n’es pas seul. Pas cette fois. Et tu aura ta carte et bien plus, sois patient", font, clock, sprite_emphyr)

        display_dialogue_box(
            screen,
            "Clotaire ne répond rien et se contente de marcher en silence, laissant derrière lui les ombres de son passé. "
            "La salle s’efface lentement derrière eux, ne laissant que l’écho d’une mélodie harmonieuse.",
            font, clock
        )

        # Interaction entre Emphyr et Garen
        display_dialogue_box(
            screen,
            "Garen ralentit légèrement, laissant Emphyr marcher à ses côtés. Il glisse un regard furtif dans sa direction, "
            "Mais la jeune femme ne réagit pas, Garen baisse la tête et continue d'avancer",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Garen (timidement) : Tu sais… merci d’avoir pris les devants.", font, clock, sprite_garen)
        display_dialogue_with_sprite(screen, "Emphyr (sec) : Tu aurais fait pareil pour moi.", font, clock, sprite_emphyr)
        display_dialogue_box(
            screen,
            "Kael, marchant en avant, lève les yeux au ciel en entendant l’échange mais ne dit rien.",
            font, clock
        )
        fade_out_music(fade_duration=1000)
    floor6_air(hero, screen, font, clock, sprites)
    def floor6_conclusion(hero, screen, font, clock, sprites):
            # Narration - Sortie des équipes
        global background
        background = fade_in_background(screen,"graphics/resources/backgrounds/salle6.PNG", WIDTH, HEIGHT)
        display_dialogue_box(
                screen,
                "La porte de la salle de l’air s’ouvre lentement, laissant sortir Kael, Garen, Emphyr et Clotaire. "
                "Clotaire sort en premier, époussetant son manteau nonchalamment, mais son regard trahit une tension intérieure.",
                font, clock
            )
        display_dialogue_with_sprite(screen, "Clotaire (souriant) : Voilà qui n’était pas si compliqué. Je commençais à m’ennuyer.", font, clock, sprites["Clotaire"])
        display_dialogue_with_sprite(screen, "Kael (regard sombre) : Tu as surtout failli nous ralentir.", font, clock, sprites["Kael"])
        display_dialogue_with_sprite(screen, "Garen (voix basse) : Ne recommencez pas…", font, clock, sprites["Garen"])
        fade_in_music("graphics/resources/music/path.mp3", max_volume=0.2, fade_duration=1000)

        # Retrouvailles avec l'équipe d'Aldric
        display_dialogue_box(
            screen,
            "En avançant vers la salle centrale, vous apercevez Aldric, Ayela et Gallius près du mur. "
            "Ayela essuie discrètement ses yeux rougis, accroupie contre une colonne. Gallius joue distraitement avec sa dague.",
            font, clock
        )

        display_dialogue_with_sprite(screen, "Clotaire (s’approchant) : Oh… des pleurs ?", font, clock, sprites["Clotaire"])
        display_dialogue_with_sprite(screen, "Clotaire (narquois) : On dirait que tout le monde n’a pas eu notre chance. Qui est mort, cette fois ?", font, clock, sprites["Clotaire"])
        display_dialogue_with_sprite(screen, "Garen (posant une main sur Ayela) : Laisse-la.", font, clock, sprites["Garen"])

        if hero.get_relation("Velm"):
            display_dialogue_with_sprite(screen, "Aldric (voix basse, évitant le regard de Clotaire) : Velm…", font, clock, sprites["Aldric"])
        if hero.get_relation("Brandio"):
            display_dialogue_with_sprite(screen, "Aldric (voix basse) : Brandio n’a pas survécu. La créature l’a réduit en cendres. Désolé Clotaire.", font, clock, sprites["Aldric"])

        display_dialogue_box(
            screen,
            "Clotaire s’arrête net, son sourire disparaissant immédiatement. Un silence lourd s’installe tandis qu’il fixe Aldric intensément.",
            font, clock
        )

        if hero.get_relation("Velm"):
            display_dialogue_with_sprite(screen, "Clotaire (voix rauque) : Velm… ?", font, clock, sprites["Clotaire"])
        if hero.get_relation("Brandio"):
            display_dialogue_with_sprite(screen, "Clotaire (le regard s’assombrissant) : Brandio…", font, clock, sprites["Clotaire"])

        display_dialogue_with_sprite(screen, "Kael (sombre) : ...", font, clock, sprites["Kael"])
        display_dialogue_with_sprite(
        screen, 
        "Clotaire (hautain, mais avec une lueur tremblante) : Évidemment, tu l’as tué, c’est ça ? Tu avais dit plus tôt à Kael qu’il fallait se débarrasser de nous… Avoue !", 
        font, clock, sprites["Clotaire"]
        )


        # Provocation de Clotaire
        display_dialogue_box(
            screen,
            "Clotaire s’approche lentement d’Aldric, les yeux flamboyants d’une colère contenue.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Clotaire (froidement) : C’est toi, non ? Leur chef. Peut-être que tu n’es pas si doué pour les garder en vie…", font, clock, sprites["Clotaire"])

        if hero.get_relation("Velm"):
            display_dialogue_with_sprite(screen, "Clotaire : Ou peut-être que tu as laissé Velm mourir exprès… pour éliminer un rival, un concurrent.", font, clock, sprites["Clotaire"])
            hero.remove_relation("Velm")
        if hero.get_relation("Brandio"):
            display_dialogue_with_sprite(screen, "Clotaire : Tu as aussi tué Brandio… Comme c’était pratique. Il te gênait aussi, c’est ça ?", font, clock, sprites["Clotaire"])
            hero.remove_relation("Brandio")

        display_dialogue_box(
        screen,
        "L’atmosphère devient lourde tandis qu’Aldric lève lentement les yeux vers Clotaire. "
        "Kael et Ayela se redressent instinctivement, prêts à intervenir.",
        font, clock
        )
        display_dialogue_with_sprite(screen, "Aldric (calme mais ferme) : Va savoir…", font, clock, sprites["Aldric"])

        display_dialogue_box(
            screen,
            "En un éclair, Clotaire dégaine sa lame, pointant Aldric avec défi. Gallius esquisse un mouvement rapide, ses dagues prêtes, "
            "tandis qu’Ayela tend son arc vers Clotaire.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Clotaire (froidement) : Baisse ton arc, Ayela. Ce n’est pas pour toi.", font, clock, sprites["Clotaire"])
        display_dialogue_with_sprite(screen, "Aldric (calmant d’un geste Ayela et Gallius) : Laissez. Il veut un duel ? Il l’aura.", font, clock, sprites["Aldric"])
        display_dialogue_with_sprite(screen, "Gallius : Laisse-moi le buter, il me saoule depuis un moment (léchant sa lame) promis... ça sera comme s’endormir.", font, clock, sprites["Gallius"])
        display_dialogue_with_sprite(screen, "Aldric (se battant) : Non, t’en mêle pas. Je le gère.", font, clock, sprites["Aldric"])

        # Début de l’affrontement
        display_dialogue_box(
            screen,
            "Les lames jaillissent dans un éclat métallique. Clotaire et Aldric s’affrontent sous les regards attentifs des autres participants.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Kael (murmurant à Garen) : Je me demande qui va gagner… Aldric a sûrement une chance.", font, clock, sprites["Kael"])
        display_dialogue_with_sprite(screen, "Garen (inquiet) : Ils vont s’entretuer…", font, clock, sprites["Garen"])
        display_dialogue_with_sprite(screen, "Clotaire (attaquant vivement) : Tu crois que tu es meilleur que nous tous ?!", font, clock, sprites["Clotaire"])
        display_dialogue_with_sprite(screen, "Aldric (bloquant habilement) : Je crois surtout que je m’emmerde…", font, clock, sprites["Aldric"])

        # Intensité du duel
        display_dialogue_box(
            screen,
            "Les coups s’enchaînent, mais aucun des deux ne parvient à prendre l’avantage. Clotaire est rapide et précis, "
            "mais Aldric pare chaque attaque avec calme. Petit à petit, le duel semble perdre en intensité.",
            font, clock
        )

        # Intervention de Garen
        display_dialogue_box(
            screen,
            "Alors que les lames s’entrechoquent encore, Garen s’interpose brusquement, écartant les deux hommes.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Garen (criant) : Assez ! Vous voulez vraiment mourir ici ?!", font, clock, sprites["Garen"])
        display_dialogue_box(
            screen,
            "Clotaire abaisse lentement sa lame, un sourire amer aux lèvres.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Clotaire : Je voulais juste voir s’il avait du mordant…", font, clock, sprites["Clotaire"])
                # Apparition d'Archeon
        display_dialogue_box(
        screen,
        "Un claquement sec interrompt le duel. Une silhouette descend lentement de la passerelle supérieure.",
        font, clock
        )
        display_dialogue_with_sprite(screen, "Archeon (calme mais puissant) : Je crois que... ça suffira...", font, clock, sprites["Archeon"])
        display_dialogue_box(
            screen,
            "Clotaire et Aldric abaissent leurs lames alors qu’Archeon s’approche.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Archeon (pose ses mains sur les épaules des deux duellistes et murmure) : Si vous souhaitez mourir, attendez. D’autres étages vous attendent.", font, clock, sprites["Archeon"])
        display_dialogue_with_sprite(screen, "Clotaire (haussant les épaules) : Comme vous voulez, maître de la tour.", font, clock, sprites["Clotaire"])
        display_dialogue_with_sprite(screen, "Archeon : Maître de la tour ??? Ahahah ! Rien que ça ! Non, je ne suis rien… du moins pas pour vous. (dit-il en regardant Aldric)", font, clock, sprites["Archeon"])

        # Clôture du duel
        display_dialogue_box(
            screen,
            "Les tensions s’apaisent tandis que la porte menant à l’étage suivant s’ouvre lentement. "
            "Mais Clotaire garde ses pensées sombres, ses yeux se perdant un instant vers l’obscurité au-dessus.",
            font, clock
        )
        display_dialogue_box(
            screen,
            "Archeon balaie la salle du regard, ses yeux s’attardant sur Aldric et Clotaire. "
            "L’atmosphère est lourde, marquée par la fatigue et les pertes récentes.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Archeon : Seize d’entre vous ont débuté cette épreuve. Mais celle-ci n'est pas finie !", font, clock, sprites["Archeon"])
        display_dialogue_with_sprite(
            screen,
            "Archeon (lentement) : Sans les quatre gemmes, cette porte pour le 7ème étage ne s’ouvrira pas. "
            "Si l’une des gemmes élémentaires manque à l’appel… vous devrez retourner dans les salles où les autres ont échoué et ramener les pierres... "
            "Encore… et encore.",
            font, clock, sprites["Archeon"]
        )
        display_dialogue_box(
            screen,
            "Les paroles d'Archeon résonnent comme une sentence. Un frisson parcourt les survivants, "
            "le poids de cette réalité s’ancrant dans leur esprit.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Kael (détournant le regard) : Magnifique. Encore une bonne raison de ne pas dormir cette nuit.", font, clock, sprites["Kael"])
        display_dialogue_with_sprite(screen, "Garen (baissant les yeux) : Il doit bien y avoir un autre moyen…", font, clock, sprites["Garen"])
        display_dialogue_box(
            screen,
            "Le silence s'étire, jusqu'à ce qu'un bruit de mécanisme retentisse. "
            "La porte de la salle de l’eau s’ouvre lentement, laissant s’échapper un torrent d’eau glaciale.",
            font, clock
        )

            # Entrée de Durnir – Archimage
        display_dialogue_box(
            screen,
            "De la vague émerge une silhouette solitaire. Un vieil homme aux cheveux gris courts et à la barbe fournie, "
            "vêtu d’une longue robe bleu nuit brodée de symboles anciens, avance avec une dignité glaciale malgré l’eau ruisselant de sa tenue. "
            "Chaque pas qu'il fait semble marquer l’eau autour de lui, comme si même les éléments hésitaient à le défier. "
            "Son regard acéré, presque perçant, glisse sur les survivants sans un mot, évaluant leur valeur d’un simple coup d’œil.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Kael (abasourdi, écarquillant les yeux) : Par tous les dieux… L’Archimage Durnir d’Urdragen ?", font, clock, sprites["Kael"])
        display_dialogue_box(
            screen,
            "Kael recule d’un pas, incapable de cacher son étonnement. Même Clotaire semble afficher une rare expression de surprise.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Kael (murmurant) : Je savais bien que ce vieux me disait quelque chose… mais je croyais qu’il était mort il y a des années.", font, clock, sprites["Kael"])
        display_dialogue_with_sprite(screen, "Durnir (calme, secouant lentement sa manche trempée) : Les rumeurs de ma mort étaient prématurées… comme toujours.", font, clock, sprites["Durnir"])
        display_dialogue_with_sprite(screen, "Garen (intrigué) : Tu le connais ? Qui est-ce ?", font, clock, sprites["Garen"])
        display_dialogue_with_sprite(screen, "Kael (s’approchant légèrement) : L’Académie d’Urdragen… c’était la plus prestigieuse école de magie de l’Empire, bien avant ma naissance.", font, clock, sprites["Kael"])
        display_dialogue_box(
            screen,
            "Kael désigne Durnir d’un léger geste de la main, presque comme s’il s’adressait à une légende vivante. "
            "Même Clotaire semble garder le silence, ce qui n’échappe pas à Garen. Emphyr, de son côté, observe l’archimage avec un mélange d’intérêt et de méfiance.",
            font, clock
        )
        display_dialogue_with_sprite(screen, "Kael : Urdragen était le centre de l’érudition magique il y a plusieurs siècles. Les plus grands sorciers, invocateurs et enchanteurs venaient de là. Durnir…", font, clock, sprites["Kael"])
        display_dialogue_with_sprite(screen, "Kael (marquant une pause) : Il était considéré comme le dernier grand Archimage avant que l’Académie…", font, clock, sprites["Kael"])
        display_dialogue_with_sprite(screen, "Durnir (l’interrompant) : …Ne s’effondre sous son propre poids.", font, clock, sprites["Durnir"])
        display_dialogue_box(
            screen,
            "Durnir croise les bras, son expression ne montrant ni regret ni tristesse. Il semble accepter ce passé comme une fatalité qu’il ne cherche plus à contester.",
            font, clock
        )
        
        display_dialogue_box(
            screen,
            "Derrière lui, la vague qui l’a porté déverse trois corps inertes, leurs visages figés par l’effroi. "
            "Ils glissent le long du sol en pierre, s’arrêtant à quelques mètres des autres survivants. "
            "Durnir ne leur accorde pas un regard, son attention toute entière tournée vers Archeon, à qui il tend une gemme azurée brillante.",
            font, clock
        )
        display_dialogue_with_sprite(screen, 
            "Durnir (calmement) : L’eau n’a laissé que moi. Comme souvent.", 
            font, clock, sprites["Durnir"]
        )
        display_dialogue_with_sprite(screen, 
            "Archeon (hochant la tête, un léger sourire en coin) : L’Urdragen devait être fière.", 
            font, clock, sprites["Archeon"]
        )
        display_dialogue_with_sprite(screen, 
            "Durnir (ricanant doucement) : L’Académie d’Urdragen n'est plus qu'une ombre. Mes succès, récents ou passés, n'y changeront rien.", 
            font, clock, sprites["Durnir"]
        )
        display_dialogue_with_sprite(screen, 
            "Kael (avec une pointe de respect) : Mais vous êtes toujours là. L’Empire vous doit au moins cela.", 
            font, clock, sprites["Kael"]
        )

        # Entrée de Yohna et Zyn – Jumeaux Invocateurs
        display_dialogue_box(
            screen,
            "Presque aussitôt, un second bruit résonne. La porte de la salle de la terre s’ouvre dans un grincement sinistre. "
            "Deux jeunes silhouettes émergent, blessées mais vivantes.",
            font, clock
        )
        display_dialogue_with_sprite(screen, 
            "Zyn (soufflant) : Encore debout, Yohna ?", 
            font, clock, sprites["Zyn"]
        )
        display_dialogue_with_sprite(screen, 
            "Yohna (léger sourire) : Toujours, petit frère. Ce n'est pas aujourd'hui qu'on crève.", 
            font, clock, sprites["Yohna"]
        )

        display_dialogue_box(
        screen,
        "Ils avancent lentement jusqu’à Archeon, chacun soutenant l’autre, mais avec une dignité farouche. "
        "Ils tendent ensemble la gemme terrestre, mais leurs mains tremblent légèrement, trahissant la fatigue accumulée.",
        font, clock
        )

        # Narration - Interaction avec Yohna et Zyn
        display_dialogue_with_sprite(screen, 
            "Archeon (calmement) : Yzunfarl donne encore des enfants à cette tour…", 
            font, clock, sprites["Archeon"]
        )
        display_dialogue_box(
            screen,
            "Un silence s'installe. Le nom d'Yzunfarl évoque des souvenirs sombres pour certains. "
            "L'ancienne cité, jadis bastion des invocateurs, n'est aujourd'hui qu'une terre de ruines, marquée par la peur et le rejet. "
            "Durant la dernière décennie, un génocide avait presque éteint l’ordre des invocateurs, poussant les survivants à l’exil.",
            font, clock
        )
        display_dialogue_with_sprite(screen, 
            "Garen (curieux, s’approchant prudemment) : Vous... Vous êtes vraiment des invocateurs d’Yzunfarl…?", 
            font, clock, sprites["Garen"]
        )
        display_dialogue_box(
            screen,
            "Le ton de Garen est maladroit, oscillant entre admiration et méfiance. "
            "Les invocateurs sont redoutés dans l'Empire, perçus comme des anomalies vivantes, des sorciers dont le pouvoir peut éveiller les éléments eux-mêmes.",
            font, clock
        )
        display_dialogue_with_sprite(screen, 
            "Durnir : Les invocateurs... Un ersatz de magicien... mais j'ai néanmoins du respect pour vous.", 
            font, clock, sprites["Durnir"]
        )
        display_dialogue_with_sprite(screen, 
            "Ayela : J'ai entendu tout un tas de choses sur eux...", 
            font, clock, sprites["Ayela"]
        )
        display_dialogue_with_sprite(screen, 
            "Aldric (les bras croisés adossé au pilier) : Hm mon intuition était bonne… Je les avais repérés dès l'extérieur de la tour...", 
            font, clock, sprites["Aldric"]
        )
        display_dialogue_with_sprite(screen, 
            "Yohna (haussant les épaules, sans se détourner) : Il semble qu’on se fasse encore remarquer.", 
            font, clock, sprites["Yohna"]
        )
        display_dialogue_with_sprite(screen, 
            "Zyn (sèchement) : L’Empire ne nous oublie pas, non. Mais ça n’a jamais été pour les bonnes raisons.", 
            font, clock, sprites["Zyn"]
        )
        display_dialogue_with_sprite(screen, 
            "Garen (bafouillant légèrement) : Je... Je n'ai jamais rencontré d'invocateurs auparavant. On raconte que…", 
            font, clock, sprites["Garen"]
        )
        display_dialogue_with_sprite(screen, 
            "Yohna (coupant Garen) : Que nous sommes dangereux, instables… C'est vrai. Si tu veux des histoires, cherche ailleurs.", 
            font, clock, sprites["Yohna"]
        )
        display_dialogue_with_sprite(screen, 
            "Zyn (moqueur) : Fais attention, Garen. Les invocateurs d’Yzunfarl n'ont pas la patience des paysans.", 
            font, clock, sprites["Zyn"]
        )
        display_dialogue_box(
            screen,
            "Garen s’apprête à répondre, mais Emphyr pose doucement une main sur son épaule, l'arrêtant dans son élan. "
            "Elle secoue légèrement la tête en direction de Garen, lui signifiant que ce n'est ni le lieu ni le moment pour discuter davantage.",
            font, clock
        )
        display_dialogue_with_sprite(screen, 
            "Emphyr (calmement) : Ils ont survécu à cette tour, comme nous. C'est tout ce qui importe pour l’instant.", 
            font, clock, sprites["Emphyr"]
        )
        display_dialogue_with_sprite(screen, 
            "Yohna (relevant la tête) : Exact. Ce qui nous sépare, c’est la force. Pas les histoires passées.", 
            font, clock, sprites["Yohna"]
        )

        display_dialogue_box(
        screen,
        "Garen recule légèrement, détournant le regard. Malgré son malaise, il sent que Yohna et Zyn ne le rejettent pas totalement. "
        "Ce n'est qu'une méfiance naturelle, forgée par la souffrance et la nécessité de survivre. "
        "Il comprend que la confiance de ces deux invocateurs devra être gagnée par des actes, et non par des mots.",
        font, clock
        )
        display_dialogue_box(
            screen,
            "Avec les quatre gemmes rassemblées, la porte centrale commence à s’illuminer, gravée de symboles anciens. "
            "La tension s’apaise à peine, laissant place à une fatigue écrasante.",
            font, clock
        )
        display_dialogue_with_sprite(screen, 
            "Archeon (solennellement) : Dix survivants… Sur près d’une centaine hm.", 
            font, clock, sprites["Archeon"]
        )
        display_dialogue_with_sprite(screen, 
            "Clotaire (murmurant) : Dix survivants… et plus aucun ami ni compagnons de beuverie…", 
            font, clock, sprites["Clotaire"]
        )
        display_dialogue_box(
            screen,
            "Alors que tout semble se calmer, Clotaire s'approche d'Aldric, son regard dur. "
            "Les pertes de Velm et Brandio pèsent lourdement sur ses épaules.",
            font, clock
        )
        display_dialogue_with_sprite(screen, 
            "Clotaire (serrant les poings) : Brandio et Velm n’auraient pas dû mourir. Tu en es le responsable.", 
            font, clock, sprites["Clotaire"]
        )
        display_dialogue_box(
            screen,
            "Gallius ajuste ses dagues, prêt à intervenir, tandis qu’Ayela pointe discrètement son arc. "
            "Mais Aldric lève la main pour les calmer, fixant Clotaire sans ciller.",
            font, clock
        )
        display_dialogue_with_sprite(screen, 
            "Aldric (froidement) : C'est toi Clotaire ! Par ton egoisme.", 
            font, clock, sprites["Aldric"]
        )
        display_dialogue_box(
            screen,
            "Les lames s’entrechoquent brièvement, un duel silencieux sous les yeux des autres survivants.",
            font, clock
        )
        display_dialogue_with_sprite(screen, 
            "Gallius : Laisse-moi intervenir ! Je vais l’avoir… Et Clotaire, rends-moi la pomme que tu m’as volée à l’entrée… c’était mon goûter.", 
            font, clock, sprites["Gallius"]
        )
        display_dialogue_box(
            screen,
            "Gallius fixe Clotaire avec son regard de tueur, prêt à en découdre.",
            font, clock
        )

        # Intervention de Garen
        display_dialogue_with_sprite(screen, 
            "Garen (s'interposant) : Assez ! Vous voulez encore vous battre, après tout ça ?", 
            font, clock, sprites["Garen"]
        )
        choix_duel = [
            (
            "Écouter Garen et Archeon, calmer la situation (+10 Garen, +10 Archeon).",
            lambda h: h.get_relation("Garen").score > 30,
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (calme, baissant sa lame) : Tu as raison, Garen… Ça suffit pour aujourd'hui.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Garen (soulagé) : Merci… Je savais que tu étais plus sage que Clotaire.", 
                    font, clock, sprites["Garen"]
                ),
                display_dialogue_box(screen, 
                    "Archeon observe la scène sans intervenir, hochant légèrement la tête en signe d'approbation.", 
                    font, clock
                ),
                h.get_relation("Garen").adjust_score(+10),
                h.get_relation("Archeon").adjust_score(+10)
            ]
            ),
            (
                "Ignorer Garen et répondre à la provocation de Clotaire (+20 Clotaire, +20 Kael, -20 Ayela, Archeon, Garen).",
                lambda h: h.get_relation("Clotaire").score < -40,
                lambda h: [
                    display_dialogue_with_sprite(screen, 
                        "Aldric (froidement) : Clotaire… Tu veux voir jusqu’où ça peut aller ?", 
                        font, clock, sprites["Aldric"]
                    ),
                    display_dialogue_with_sprite(screen, 
                        "Clotaire (souriant) : Enfin quelqu'un avec du mordant !", 
                        font, clock, sprites["Clotaire"]
                    ),
                    display_dialogue_box(screen, 
                        "Vos lames s'entrechoquent à nouveau, ignorant les avertissements de Garen et d'Archeon.", 
                        font, clock
                    ),
                    display_dialogue_with_sprite(screen, 
                        "Kael (croisant les bras) : Il fallait bien que quelqu'un le fasse.", 
                        font, clock, sprites["Kael"]
                    ),
                    display_dialogue_with_sprite(screen, 
                        "Ayela (déçue) : Tu es plus imprévisible que je pensais…", 
                        font, clock, sprites["Ayela"]
                    ),
                    display_dialogue_box(screen, 
                        "Archeon ne montre aucune émotion, mais l'éclat dans son regard s'estompe.", 
                        font, clock
                    ),
                    display_dialogue_with_sprite(screen, 
                        "Garen (secouant la tête) : Aldric… Je pensais que tu valais mieux que ça.", 
                        font, clock, sprites["Garen"]
                    ),
                    display_dialogue_box(screen, 
                        "Durnir lève calmement une main, et une barrière d'énergie s'interpose, arrêtant le combat.", 
                        font, clock
                    ),
                    display_dialogue_with_sprite(screen, 
                        "Durnir (calme) : Les enfants… Arrêtez cette folie. Ce n'est ni le lieu ni le moment.", 
                        font, clock, sprites["Durnir"]
                    ),
                    h.get_relation("Clotaire").adjust_score(+20),
                    h.get_relation("Kael").adjust_score(+20),
                    h.get_relation("Ayela").adjust_score(-20),
                    h.get_relation("Archeon").adjust_score(-20),
                    h.get_relation("Garen").adjust_score(-20)
                ]
            ),
            (
                "Ignorer les deux et simplement reculer.",
                None,
                lambda h: [
                    display_dialogue_with_sprite(screen, 
                        "Aldric (calmement) : Ce duel a été interrompu, il y aura une suite.", 
                        font, clock, sprites["Aldric"]
                    ),
                    display_dialogue_box(screen, 
                        "Clotaire recule, mais son sourire narquois demeure, tandis que Garen soupire de soulagement.", 
                        font, clock
                    ),
                ]
            )
        ]

        # Affichage des choix et gestion de la sélection
        options = [(option[0], index) for index, option in enumerate(choix_duel)]
        choix = display_choices_box(screen, font, options, clock)

        if choix is not None and (choix_duel[choix][1] is None or choix_duel[choix][1](hero)):
            choix_duel[choix][2](hero)


        display_dialogue_with_sprite(screen, 
            "Archeon (calme) : Gardez votre colère. Elle vous sera utile.", 
            font, clock, sprites["Archeon"]
        )
        display_dialogue_box(screen, 
            "La porte vers l'étage supérieur s'ouvre lentement…", 
            font, clock
        )
        display_dialogue_box(screen, 
            "Il reste 10 participants. L’étage suivant s’annonce plus impitoyable encore.", 
            font, clock
        )

    floor6_conclusion(hero, screen, font, clock, sprites)

        
    fade_out_music(fade_duration=4000)
    fade_in_text(screen, "Fin du Chapitre 7 - Il reste 10 participants sur 99 et 94 étages", font, (WIDTH // 2, HEIGHT // 2), duration=2000)
    fade_out_text(screen, 1000)
    game_menu(screen, font, clock, WIDTH, HEIGHT, hero)
    
    
def chapitre_7(hero, screen, font, clock,sprites):
    
    global background
    
    sprites = load_sprites()

    sprite_aldric = sprites["Aldric"]
    sprite_garen = sprites["Garen"]
    sprite_mysterieux = sprites["Homme_mysterieux"]
    sprite_kael = sprites["Kael"]
    sprite_brandio = sprites["Brandio"]
    sprite_archeon = sprites["Archeon"]
    sprite_ayela = sprites["Ayela"]
    sprite_clotaire = sprites["Clotaire"]
    sprite_durnir = sprites["Durnir"]
    sprite_emphyr = sprites["Emphyr"]
    sprite_gallius = sprites["Gallius"]
    sprite_velm = sprites["Velm"]
    sprite_yohna = sprites["Yohna"]
    sprite_zyn = sprites["Zyn"]
    sprite_random_participant = sprites["Participant"]
    sprite_creature = sprites["Creature"]
    
    fade_in_music("graphics/resources/music/Medusa.mp3", max_volume=0.2, fade_duration=1000)
    clear_screen(screen)
    fade_in_text(screen, 
             "Chapitre 8 : La boite noire - Etage 7/99", 
             font, 
             (WIDTH // 2, HEIGHT // 2),  # Centré sur l'écran
             duration=3000)
    fade_out_text(screen, 3000, fade_speed=2)
    pygame.time.wait(1000)
    
    
    
    yohna = Character(
    "Yohna", 
    "graphics/resources/sprites/Yohna.webp", 
    "Invocatrice expérimentée et protectrice de son frère cadet Zyn.", 
    "Invocateur", 
    gender="fille"
    )

    zyn = Character(
    "Zyn", 
    "graphics/resources/sprites/Zyn.webp", 
    "Jeune invocateur talentueux, vif d'esprit mais souvent impulsif.", 
    "Invocateur", 
    gender="garçon"
    )

    durnir = Character(
    "Durnir", 
    "graphics/resources/sprites/Durnir.webp", 
    "Archimage légendaire d'Urdragen, mystérieux et distant.", 
    "Mage", 
    gender="homme"
    )

    # Ajout des relations pour le héros
    hero.add_relation(yohna, "Neutre")
    hero.add_relation(zyn, "Neutre")
    hero.add_relation(durnir, "Neutre")
        
    # Entrée dans la salle du chapitre 8
    display_dialogue_box(
        screen,
        "Lorsque la porte de l'étage 6 se referme derrière vous, le froid glacial de la tour cède la place à une chaleur inattendue. "
        "Devant vous s'étend une vaste salle richement décorée. Des tapis soyeux couvrent le sol, des canapés moelleux sont disposés en cercle, "
        "et des tables chargées de fruits, de viande et de vin s'étendent jusqu'à l'horizon de cette pièce circulaire. "
        "Des lanternes suspendues diffusent une lumière dorée et dansante, projetant des ombres accueillantes sur les murs gravés d'arabesques anciennes.",
        font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/etage7.webp", WIDTH, HEIGHT)

    display_dialogue_box(
        screen,
        "L'ambiance y est étrangement chaleureuse. Après les épreuves mortelles, cette salle ressemble à un mirage, "
        "une parenthèse de calme au milieu du chaos impitoyable de la tour.",
        font, clock
    )

    # Réactions des personnages
    display_dialogue_with_sprite(screen, "Kael (s'étirant) : Enfin un endroit qui ne cherche pas à nous tuer… pour le moment.", font, clock, sprites["Kael"])
    display_dialogue_with_sprite(screen, "Ayela (méfiante) : C'est trop beau pour être vrai… On ne devrait pas baisser notre garde.", font, clock, sprites["Ayela"])
    display_dialogue_with_sprite(screen, "Garen (admiratif) : On dirait les salons des nobles de l'Empire… Je pourrais m'habituer à ça.", font, clock, sprites["Garen"])
    display_dialogue_with_sprite(screen, "Clotaire (sarcastique) : Savourez tant que vous pouvez. Je doute que la tour nous offre ce luxe gratuitement.", font, clock, sprites["Clotaire"])
    display_dialogue_with_sprite(screen, "Emphyr (s'approchant d'une table) : Il y a de la nourriture… et elle semble fraîche. Étrange.", font, clock, sprites["Emphyr"])

    # Apparition d'Archeon
    display_dialogue_box(
        screen,
        "Archeon descend lentement d'une passerelle qui surplombe la salle. Son regard impassible balaie les participants.",
        font, clock
    )
    display_dialogue_with_sprite(screen, "Archeon (calme) : Reposez-vous, participants. Vous en aurez besoin. Cette salle est un répit… mais éphémère.", font, clock, sprites["Archeon"])

    display_dialogue_box(
        screen,
        "Il s'arrête devant une boîte en pierre noire, posée juste devant la porte scellée menant à l'étage 8. "
        "Aucune inscription ne l'orne, mais elle dégage une aura inquiétante.",
        font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/boitenoire.webp", WIDTH, HEIGHT)

    display_dialogue_with_sprite(screen, "Kael (croisant les bras) : Et cette boîte… ? Qu'est-ce que c'est ?", font, clock, sprites["Kael"])
    display_dialogue_with_sprite(screen, "Archeon (avec gravité) : Cette boîte renferme tout ce que tu peux imaginer, Kael. Pour l'instant, elle reste close. Jusqu'à nouvel ordre.", font, clock, sprites["Archeon"])
    display_dialogue_with_sprite(screen, "Garen (intrigué) : Jusqu'à nouvel ordre ? Cela signifie que nous pouvons vraiment… nous reposer ?", font, clock, sprites["Garen"])
    display_dialogue_with_sprite(screen, "Archeon : Oui, reposez-vous. La tour peut paraître impitoyable, mais en réalité elle est… juste… Elle sait aussi récompenser.", font, clock, sprites["Archeon"])

    # Description de la boîte
    display_dialogue_box(
        screen,
        "La boîte semble vivante, vibrante, comme si quelque chose en son sein attendait patiemment. "
        "Mais pour l'heure, elle reste immobile, une ombre menaçante parmi la lumière chaleureuse de la salle.",
        font, clock
    )
    # Introduction aux choix autour de la boîte noire
    display_dialogue_box(
        screen,
        "Alors que vous approchez de la boîte noire, une étrange sensation vous envahit. Que faites-vous ?",
        font, clock
    )

    # Définition des choix concernant la boîte noire
    choix_boite = [
        (
            "Examiner la boîte et parler de l’aura étrange qui s’en dégage.",
            None,  # Pas de condition préalable
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (fronçant les sourcils) : Cette boîte… Je ressens quelque chose. Une sorte de pouvoir. Ni bon ni mauvais… juste là.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_box(
                    screen,
                    "Un silence s'installe alors que Zyn et Yohna échangent un regard surpris. Même Durnir arrête de lisser sa barbe un instant.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Zyn : Hm… Tu perçois ça ? Étrange. Seuls ceux qui pratiquent l’invocation ou la magie y sont généralement sensibles.", 
                    font, clock, sprites["Zyn"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Yohna (curieuse) : Tu n’es pourtant pas de ceux qui manipulent ces forces… intéressant.", 
                    font, clock, sprites["Yohna"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Durnir (regardant Aldric fixement) : La tour… amplifie certaines âmes. Peut-être est-ce là son premier effet sur toi.", 
                    font, clock, sprites["Durnir"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Archeon (en observant la boîte) : Cela n’arrive pas souvent. Garde cela à l’esprit, Aldric.", 
                    font, clock, sprites["Archeon"]
                ),
                h.get_relation("Zyn").adjust_score(+10),
                h.get_relation("Yohna").adjust_score(+10),
                h.get_relation("Durnir").adjust_score(+10),
                h.get_relation("Archeon").adjust_score(+10)
            ]
        ),
        (
            "Se méfier et exprimer votre suspicion sur un potentiel piège.",
            None,  # Pas de condition préalable
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (croisant les bras) : Je ne sens rien, mais cette boîte crie le mot piège. Rien n’est gratuit dans cette tour.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_box(
                    screen,
                    "Garen acquiesce rapidement, se rapprochant d’Aldric.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Garen (hochant la tête) : Je suis d’accord… Ça sent l’embrouille à plein nez.", 
                    font, clock, sprites["Garen"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Kael (léger sourire) : Pour une fois, je suis de ton côté. Cette tour ne nous a jamais offert un festin sans un prix.", 
                    font, clock, sprites["Kael"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Ayela (inquiète) : C’est vrai… Cette atmosphère est bien trop calme pour être honnête.", 
                    font, clock, sprites["Ayela"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Clotaire (narquois) : Ah ! Pour une fois, Aldric dit quelque chose d’intelligent.", 
                    font, clock, sprites["Clotaire"]
                ),
                h.get_relation("Garen").adjust_score(+5),
                h.get_relation("Kael").adjust_score(+5),
                h.get_relation("Ayela").adjust_score(+5),
                h.get_relation("Clotaire").adjust_score(+5)
            ]
        )
    ]

    # Affichage des choix et gestion de la sélection
    options = [(option[0], index) for index, option in enumerate(choix_boite)]
    choix = display_choices_box(screen, font, options, clock)

    if choix is not None:
        choix_boite[choix][2](hero)
    background = fade_in_background(screen,"graphics/resources/backgrounds/etage7.webp", WIDTH, HEIGHT)
    # Narration : Archeon s'approche
    display_dialogue_box(
        screen,
        "Archeon s'approche doucement, s'arrêtant à quelques pas d'Aldric. L'air autour semble s'alourdir par sa simple présence.",
        font, clock
    )

    # Répartition et dialogues personnels
    display_dialogue_box(
        screen,
        "Certains s'installent immédiatement sur les canapés, d'autres préfèrent rester debout, jetant des regards méfiants autour d'eux.",
        font, clock
    )
    display_dialogue_with_sprite(screen, "Ayela (s'asseyant sur un fauteuil près d'Aldric) : C'est peut-être notre dernière chance de profiter d'un moment de calme…", font, clock, sprites["Ayela"])
    display_dialogue_with_sprite(screen, "Kael (au loin, servant du vin) : Aussi bien en profiter. Si c'est un piège, autant mourir en savourant quelque chose de bon.", font, clock, sprites["Kael"])
    display_dialogue_with_sprite(screen, "Clotaire (chuchotant à Emphyr) : Observe bien, Emphyr. Chaque visage ici cache quelque chose. Même la tour teste notre confiance.", font, clock, sprites["Clotaire"])
    display_dialogue_with_sprite(screen, "Emphyr (hochant la tête) : Je sais… mais parfois, il vaut mieux profiter du silence plutôt que de l'interroger.", font, clock, sprites["Emphyr"])

    # Introduction des nouveaux personnages dans la scène
    display_dialogue_box(
        screen,
        "Durnir s'approche lentement d'une table, remplissant une coupe de thé fumant. Zyn et Yohna s'installent à l'écart, près de la cheminée, silencieux mais observateurs.",
        font, clock
    )

    # Durnir observe le groupe
    display_dialogue_with_sprite(screen, "Durnir (fixant Garen) : Je suis curieux… Ce garçon. Garen, n'est-ce pas ?", font, clock, sprites["Durnir"])
    display_dialogue_with_sprite(screen, "Kael (sourire en coin) : Oui, c'est bien lui. Il est monté jusqu'ici, ce qui en soi… est un exploit.", font, clock, sprites["Kael"])
    display_dialogue_with_sprite(screen, "Durnir (haussant un sourcil) : Et pourtant, il n’a ni magie, ni talent particulier à l’épée.", font, clock, sprites["Durnir"])
    display_dialogue_with_sprite(screen, "Garen (entendant cela) : Merci pour la remarque… Je fais de mon mieux.", font, clock, sprites["Garen"])
    display_dialogue_with_sprite(screen, "Durnir (calme, approchant Garen) : Le fait que tu sois encore là en dit long. Peut-être que la tour perçoit en toi ce que nous ne voyons pas encore.", font, clock, sprites["Durnir"])

    # Zyn et Yohna restent en retrait
    display_dialogue_box(
        screen,
        "Non loin de là, Zyn fait glisser un petit fragment de pierre sur la table, traçant des symboles anciens du bout des doigts.",
        font, clock
    )
    display_dialogue_with_sprite(screen, "Yohna (regardant Zyn) : Tu es nerveux ?", font, clock, sprites["Yohna"])
    display_dialogue_with_sprite(screen, "Zyn (calme, sans lever les yeux) : Je n’aime pas cet endroit. On dirait qu’il respire avec nous.", font, clock, sprites["Zyn"])
    display_dialogue_with_sprite(screen, "Yohna : Ce n'est pas la première fois qu’on se sent observés. Les invocateurs ne sont jamais les bienvenus, même parmi d’autres survivants.", font, clock, sprites["Yohna"])
    display_dialogue_with_sprite(screen, "Garen (tentant de détendre l’atmosphère) : Ce n’est pas vrai… Vous avez sauvé des vies avec vos créatures, non ?", font, clock, sprites["Garen"])
    display_dialogue_with_sprite(screen, "Yohna (souriant légèrement mais gardant ses distances) : C’est ce que nous faisons. Mais cela ne change pas ce que nous sommes pour eux.", font, clock, sprites["Yohna"])

    # Gallius s'approche d'Aldric
    display_dialogue_box(
        screen,
        "Gallius s'appuie contre une colonne, regardant Aldric de loin avant de s’approcher doucement.",
        font, clock
    )
    display_dialogue_with_sprite(screen, "Gallius (à voix basse) : Ces deux invocateurs. Tu crois qu’on peut leur faire confiance ?", font, clock, sprites["Gallius"])
    display_dialogue_with_sprite(screen, "Aldric (calme) : Ils sont encore là. Mais je crois qu'on ne peut faire confiance à personne ici.", font, clock, sprites["Aldric"])
    display_dialogue_with_sprite(screen, "Gallius (souriant en coin) : Tu es plus pragmatique que je pensais. Mais j’imagine que c’est comme ça qu’on survit ici.", font, clock, sprites["Gallius"])
    display_dialogue_with_sprite(screen, "Aldric : Retiens ça. La tour teste tout, même notre naïveté.", font, clock, sprites["Aldric"])
    # Durnir partage sa sagesse
    display_dialogue_with_sprite(screen, "Durnir (posant sa tasse) : Les jeunes ont raison de se méfier. Mais parfois, les alliances improbables sont les plus durables.", font, clock, sprites["Durnir"])
    display_dialogue_with_sprite(screen, "Kael (souriant) : La sagesse de l'archimage d'Urdragen… Je suppose que tu as vu des choses bien pires que cette tour.", font, clock, sprites["Kael"])
    display_dialogue_with_sprite(screen, "Durnir : Des décennies d’élèves trop sûrs d’eux, oui. Mais peu ont eu votre persévérance. Profitez du repos tant qu'il dure.", font, clock, sprites["Durnir"])

    # Conflit sous-jacent de Clotaire
    display_dialogue_box(
        screen,
        "Un peu plus loin, Clotaire reste à l'écart du groupe, le regard fixé sur la boîte noire. "
        "Son esprit semble ailleurs, peut-être perdu dans les souvenirs de Velm et Brandio.",
        font, clock
    )
    display_dialogue_with_sprite(screen, "Emphyr (se tenant près de Clotaire) : Tu n’es pas obligé de rester seul.", font, clock, sprites["Emphyr"])
    display_dialogue_with_sprite(screen, "Clotaire (sans détourner les yeux) : Je le suis depuis le début. Même avant la tour.", font, clock, sprites["Clotaire"])
    display_dialogue_box(
        screen,
        "Le silence s'installe un instant, avant qu'Emphyr ne lui pose doucement une main sur l'épaule. Clotaire ne bouge pas, mais il ne la repousse pas non plus.",
        font, clock
    )

    # Conclusion du moment de repos
    display_dialogue_box(
        screen,
        "Alors que les survivants s’installent un peu plus confortablement, la lumière du jour s’atténue lentement. "
        "La boîte noire demeure immobile, mais son ombre s’étend peu à peu sur le sol, annonçant l’approche du crépuscule… et des épreuves à venir.",
        font, clock
    )
    display_dialogue_box(screen, "Pour la première fois depuis longtemps, le silence s'installe sans menace immédiate.", font, clock)

    # Interdiction d'attaquer un participant
    display_dialogue_with_sprite(screen, "Archeon (d’un ton grave) : Avant que vous ne vous reposiez… écoutez bien.", font, clock, sprites["Archeon"])
    display_dialogue_with_sprite(screen, "Archeon : À partir de maintenant, toute tentative de tuer un autre participant sera sanctionnée par une mort immédiate.", font, clock, sprites["Archeon"])
    display_dialogue_with_sprite(screen, "Archeon (balayant la salle du regard) : La tour est assez impitoyable. Elle n'a pas besoin de votre aide pour réduire le nombre de survivants.", font, clock, sprites["Archeon"])
    display_dialogue_box(
        screen,
        "Un silence pesant s’installe. Clotaire croise les bras en jetant un regard furtif vers Aldric. Durnir hoche lentement la tête, tandis que Zyn et Yohna échangent un regard complice.",
        font, clock
    )
    display_dialogue_with_sprite(screen, "Archeon (calme mais ferme) : Je reviendrai à l’aube. Jusque-là, reposez-vous et récupérez vos forces. L’étage suivant réclamera plus que votre force physique.", font, clock, sprites["Archeon"])

    # Archeon quitte le centre de la salle
    display_dialogue_box(
        screen,
        "Archeon s’éloigne, laissant les survivants profiter du silence. Aldric, ressentant le besoin d’air, s’avance jusqu’à une large terrasse adjacente.",
        font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/balcon.webp", WIDTH, HEIGHT)
    # Scène du balcon
    display_dialogue_box(
        screen,
        "Depuis cette hauteur, la vue est vertigineuse. L'empire s'étend à perte de vue, baigné dans la lumière du crépuscule. "
        "Les montagnes au loin sont teintées d’orange malgré une fine pluie, et les toits des cités en contrebas scintillent faiblement.",
        font, clock
    )
    display_dialogue_box(
        screen,
        "Aldric s’appuie contre la rambarde du balcon, laissant son regard errer sur l’horizon. "
        "Des pas discrets résonnent derrière lui. Archeon l’a rejoint, le visage impassible.",
        font, clock
    )

    # Dialogue conditionnel avec Archeon
    display_dialogue_box(
        screen,
        "Archeon s'approche doucement, s'arrêtant à quelques pas d'Aldric. L'air autour semble s'alourdir par sa simple présence.",
        font, clock
    )
    # Archeon fixe l’horizon en silence
    display_dialogue_box(
        screen,
        "Archeon fixe l’horizon en silence pendant un moment, puis prend la parole d’une voix posée.",
        font, clock
    )

    # Dialogue entre Archeon et Aldric
    display_dialogue_with_sprite(screen, 
        "Archeon (regardant l'Empire en contrebas) : Je ne suis pas surpris de te voir ici, Aldric. La tour attire ceux qui n'ont plus rien à perdre.", 
        font, clock, sprites["Archeon"]
    )
    display_dialogue_with_sprite(screen, 
        "Archeon (calme mais grave) : Regarde cette vue. L’Empire s’effrite lentement. Ses fondations se fissurent… Les villes s'affaiblissent. "
        "Et pourtant, en bas, ils continuent à vivre comme si tout était éternel.", 
        font, clock, sprites["Archeon"]
    )

    display_dialogue_box(
        screen,
        "Archeon inspire lentement, comme pour savourer l’air froid de l'altitude.",
        font, clock
    )

    display_dialogue_with_sprite(screen, 
        "Archeon : Ceux qui montent la tour ne sont que des fragments de cette ruine. Des âmes perdues, venues ici par désespoir, "
        "par orgueil ou par nécessité… Et ils parient ce qui leur reste. Leur vie.", 
        font, clock, sprites["Archeon"]
    )

    display_dialogue_box(
        screen,
        "Il se tourne vers Aldric, le scrutant attentivement.",
        font, clock
    )

    display_dialogue_with_sprite(screen, 
        "Archeon (doucement) : Toi… Quel est ton pari ?", 
        font, clock, sprites["Archeon"]
    )
    # Introduction des choix avec Archeon
    display_dialogue_box(
        screen,
        "Archeon s'arrête à côté de vous. Que lui dites-vous ?",
        font, clock
    )

    # Définition des choix concernant Archeon
    choix_archeon = [
        (
            "Pourquoi nous donner un tel répit après ces épreuves mortelles ?",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (croisant les bras) : Pourquoi cette salle… cette boîte ? Vous jouez avec nous.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Archeon (gardant les yeux sur l'horizon) : Il faut parfois briser un guerrier pour voir ce qu'il vaut. "
                    "Ce répit est une illusion. Ce que vous y verrez dépendra de vous.", 
                    font, clock, sprites["Archeon"]
                ),
                display_dialogue_box(
                    screen,
                    "Archeon semble mesurer chaque mot, comme s'il testait Aldric.",
                    font, clock
                ),
            ]
        ),
        (
            "Vous semblez trop calme… Vous cachez quelque chose.",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (fixant Archeon) : Vous cachez vos intentions. Qui êtes-vous réellement ?", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Archeon (un léger sourire aux lèvres) : Je suis le gardien de cette tour. Mais tu le sais déjà, n'est-ce pas ?", 
                    font, clock, sprites["Archeon"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (fronçant les sourcils) : Vous avez une drôle de façon de me parler…", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Archeon (évasif) : Peut-être est-ce simplement la tour qui murmure en toi.", 
                    font, clock, sprites["Archeon"]
                ),
            ]
        ),
        (
            "(Relation Archeon : Ami) Vous avez vu ces épreuves des centaines de fois… Que suis-je censé apprendre ?",
            lambda h: h.get_relation("Archeon").score >= 20,
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Archeon (baissant légèrement la tête) : Les épreuves sont des fenêtres sur vous-mêmes. "
                    "Elles révèlent ce que vous refusez de reconnaître.", 
                    font, clock, sprites["Archeon"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric : Et que dois-je voir ?", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Archeon (calmement) : Toi-même. Tu portes un fardeau, Aldric. Un poids que tu n’es pas prêt à admettre.", 
                    font, clock, sprites["Archeon"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (interloqué) : Comment savez-vous cela…?", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Archeon (avec un soupçon de chaleur) : Parce que ce n’est pas la première fois que nous nous croisons, même si tu l’as oublié.", 
                    font, clock, sprites["Archeon"]
                ),
                display_dialogue_box(
                    screen,
                    "Aldric ressent une étrange familiarité dans ces paroles, comme si un souvenir lointain effleurait sa mémoire.",
                    font, clock
                ),
                h.get_relation("Archeon").adjust_score(+10)
            ]
        ),
        (
            "(Relation Archeon : Ennemi) Vous pensez que je ne mérite pas de continuer, n’est-ce pas ?",
            lambda h: h.get_relation("Archeon").score <= -20,
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Archeon (le regard froid) : Certains montent par nécessité, d'autres par erreur. "
                    "Je ne suis pas sûr que la tour t'ait choisi pour les bonnes raisons.", 
                    font, clock, sprites["Archeon"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (froidement) : Je suis encore là.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Archeon (impassible) : La tour est patiente. Elle tolère ceux qui n’ont pas leur place… un temps.", 
                    font, clock, sprites["Archeon"]
                ),
                display_dialogue_box(
                    screen,
                    "Archeon ne détourne pas son regard, et Aldric sent une tension sourde dans l'air.",
                    font, clock
                ),
                h.get_relation("Archeon").adjust_score(-5)
            ]
        ),
        (
            "Observer Archeon en silence.",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_box(
                    screen,
                    "Aldric se contente de fixer Archeon, laissant les mots suspendus dans l'air. "
                    "L'homme en rouge semble apprécier ce silence respectueux.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Archeon (calmement) : Le silence est souvent plus éloquent que les paroles. La tour l'enseigne à ceux qui savent écouter.", 
                    font, clock, sprites["Archeon"]
                ),
                display_dialogue_box(
                    screen,
                    "Archeon s'éloigne lentement, laissant Aldric méditer en paix.",
                    font, clock
                ),
            ]
        )
    ]

    # Affichage des choix et gestion de la sélection
    options = [(option[0], index) for index, option in enumerate(choix_archeon) if option[1] is None or option[1](hero)]
    choix = display_choices_box(screen, font, options, clock)

    if choix is not None:
        choix_archeon[choix][2](hero)
        
    
    

    # Archeon s'éloigne
    display_dialogue_box(
        screen,
        "Alors qu'Archeon s’éloigne, Aldric sent un étrange frisson, comme si quelque chose d’important venait de lui échapper.",
        font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/boitenoire.webp", WIDTH, HEIGHT)
    # Transition vers la suite de l'étage
    display_dialogue_box(
        screen,
        "Alors que la nuit tombe doucement, la boîte noire semble vibrer doucement... en attente.",
        font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/balcon.webp", WIDTH, HEIGHT)
    # Séquence du balcon - 15 minutes après la discussion avec Archeon
    display_dialogue_box(
        screen,
        "15 Minutes Après la Discussion avec Archeon",
        font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/balcon.webp", WIDTH, HEIGHT)
    # Narration d'entrée
    display_dialogue_box(
        screen,
        "Aldric est accoudé à la rambarde du balcon, contemplant les plaines de l’Empire qui s’étendent sous l’étage 7. "
        "La lumière tamisée du crépuscule teinte les montagnes lointaines de reflets orangés.",
        font, clock
    )

    # Arrivée de Garen
    display_dialogue_box(
        screen,
        "Des pas légers s’approchent derrière Aldric. Garen, mains dans les poches, évite son regard en s’approchant du balcon.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Garen (doucement) : Tu crois qu’on peut voir chez moi d’ici…? Je crois que c’est par là-bas.",
        font, clock, sprites["Garen"]
    )
    display_dialogue_box(
        screen,
        "Il désigne une vallée lointaine, cachée par la brume du soir.",
        font, clock
    )

    # Réponse initiale d'Aldric
    display_dialogue_with_sprite(
        screen,
        "Aldric : Pourquoi tu viens me raconter ça, Garen ?",
        font, clock, sprites["Aldric"]
    )

    # Garen se confie
    display_dialogue_with_sprite(
        screen,
        "Garen (voix basse) : Je… Je t’ai vaguement dit pourquoi je suis là à l'étage 4. Pas pour echapper à un marriage, ni l’argent… C’est mon père.",
        font, clock, sprites["Garen"]
    )
    display_dialogue_with_sprite(
        screen,
        "Aldric (sérieux) : Ton père ?",
        font, clock, sprites["Aldric"]
    )
    display_dialogue_with_sprite(
        screen,
        "Garen (hésitant) : Mon frère est mort à la guerre. Depuis, c’est moi qui aurais dû… enfin, tu vois. "
        "Mais mon père… il boit trop. Il frappe ma mère et ma petite sœur. Il vend des morceaux de la ferme pour rembourser ses dettes… "
        "Bientôt, ils n’auront plus rien.",
        font, clock, sprites["Garen"]
    )
    display_dialogue_with_sprite(
        screen,
        "Garen (s'arrêtant un instant) : Je suis monté dans cette tour pour trouver le courage… "
        "Le courage de le chasser et protéger ma famille. Mais je sais pas si j’en suis capable. Aldric, je sais même pas si je vais y survivre…",
        font, clock, sprites["Garen"]
    )
    # Introduction des choix avec Garen
    display_dialogue_box(
        screen,
        "Comment répondez-vous à Garen ?",
        font, clock
    )

    # Définition des choix concernant Garen
    choix_garen = [
        (
            "(Relation Garen +50) Tu es plus fort que tu ne le penses, Garen.",
            lambda h: h.get_relation("Garen").score >= 50,
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (avec sincérité) : Tu as déjà fait tout ce chemin. C’est pas pour rien.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_box(
                    screen,
                    "Aldric s’approche de Garen et pose une main ferme sur son épaule, forçant doucement son regard vers l’horizon brumeux.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (posant sa main sur les cheveux de Garen) : Regarde… aux jeux des dalles, c'est grâce à toi. "
                    "Kael m'a raconté pour la salle de l'air aussi.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (souriant légèrement) : T’as plus de courage que tu crois. Tu crois que c'est rien, mais…", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (fixant l’horizon) : Quand cette tour sera derrière nous, tu auras la force qu’il te manque. "
                    "Tu l’as déjà en toi. Ce qui te manque, c’est de le reconnaître.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_box(
                    screen,
                    "Garen baisse les yeux, un sourire sincère naissant sur ses lèvres.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Garen (souriant faiblement) : Merci… Je suis sûr que je vais mourir ici, mais ça va. "
                    "T’es le seul ami que j’ai jamais eu, Aldric. Je regrette pas d'avoir tenté la tour.", 
                    font, clock, sprites["Garen"]
                ),
                display_dialogue_box(
                    screen,
                    "Un silence s'installe. Aldric détourne légèrement le regard, un souvenir fugace effleurant sa mémoire. "
                    "Les dix survivants... une lueur de nostalgie traverse son esprit.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (murmurant) : On est dix. Je… je crois que ça ira.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Garen (riant nerveusement) : J’espère que tu dis vrai ! Merci, mon ami.", 
                    font, clock, sprites["Garen"]
                ),
                h.get_relation("Garen").adjust_score(+10)
            ]
        ),
        (
            "T’es pas si mauvais. T’as un bon cœur.",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (léger sourire) : Je plaisante pas. T’es quelqu’un de bien, Garen. T’as juste besoin d’y croire toi aussi.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_box(
                    screen,
                    "Garen relève la tête, surpris par la sincérité d’Aldric. Il détourne les yeux, gêné, mais un sourire apaisé éclaire son visage.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Garen (soulagé) : Merci… Ça fait du bien de l’entendre. Je crois que c’est ça qui me manquait.", 
                    font, clock, sprites["Garen"]
                ),
                display_dialogue_box(
                    screen,
                    "Les deux fixent l’horizon en silence, profitant du rare moment de tranquillité.",
                    font, clock
                ),
            ]
        ),
        (
            "(Relation Garen -20) Tu devrais pas trop espérer. La tour prend tout.",
            lambda h: h.get_relation("Garen").score <= -20,
            lambda h: [
                display_dialogue_box(
                    screen,
                    "Aldric reste immobile, perdu dans ses pensées. Son regard sombre embrasse la vallée lointaine, "
                    "mais il ne semble pas la voir.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (froidement) : Y’en a pas beaucoup qui ressortent de cette tour vivants, Garen. "
                    "Tu devrais pas trop espérer.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_box(
                    screen,
                    "Garen baisse les yeux, mâchoire serrée, la confiance s'effilochant un peu plus.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Garen (affecté, murmurant) : …Ouais. Peut-être.", 
                    font, clock, sprites["Garen"]
                ),
                display_dialogue_box(
                    screen,
                    "Il s'éloigne sans ajouter un mot, laissant Aldric seul, plongé dans ses réflexions silencieuses.",
                    font, clock
                ),
                h.get_relation("Garen").adjust_score(-10)
            ]
        )
    ]
    

    # Affichage des choix et gestion de la sélection
    options = [(option[0], index) for index, option in enumerate(choix_garen) if option[1] is None or option[1](hero)]
    choix = display_choices_box(screen, font, options, clock)

    if choix is not None:
        choix_garen[choix][2](hero)
    
    # Narration : Garen quitte le balcon
    display_dialogue_box(
        screen,
        "Alors que Garen s'éloigne du balcon, Aldric reste là, scrutant l’horizon sombre de l’Empire. "
        "Le vent nocturne souffle doucement, comme pour rappeler aux survivants que la tour n’a pas encore livré tous ses secrets.",
        font, clock
    )
    display_dialogue_box(
        screen,
        "Au loin, la boîte noire au centre de la salle vibre faiblement, pulsant au rythme du crépuscule naissant.",
        font, clock
    )

    # Rencontre avec Kael sur le balcon
    display_dialogue_box(
        screen,
        "Kael s'approche lentement du balcon, s'arrêtant à quelques pas d'Aldric. "
        "Le vent nocturne souffle doucement, soulevant les mèches de ses cheveux châtains. "
        "Il fixe l’horizon, là où la lumière de l’Empire s’étale faiblement, voilée par la brume.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Kael (d’un ton calme, presque distant) : Tu regardes ces terres… Ces terres pourries et déchues. "
        "Il fut un temps où elles nous appartenaient.",
        font, clock, sprites["Kael"]
    )
    display_dialogue_with_sprite(
        screen,
        "Aldric (intrigué) : Tu m’as dit que ta maison avait disparu après la guerre contre l'Empire du Nord…",
        font, clock, sprites["Aldric"]
    )
    display_dialogue_with_sprite(
        screen,
        "Kael (un rictus amer sur le visage) : Disparue ? Non. La Maison Sielmarr n’a jamais disparu… "
        "Elle a été effacée, morceau par morceau. Quand la guerre a été perdue, mon oncle a plié genou devant l’Empire. "
        "Il a signé la reddition et offert nos terres…",
        font, clock, sprites["Kael"]
    )
    display_dialogue_with_sprite(
        screen,
        "Kael (les poings serrés) : L’empereur Vilmar II a juré qu’il protégerait nos frontières. Il nous a trahis. "
        "Mes sœurs… Mariées de force aux seigneurs vainqueurs. Mon frère aîné, exécuté… Et ma mère, elle est morte sous les coups des soldats "
        "qu’on lui a infligés au palais. Pendant que l’Empire festoyait.",
        font, clock, sprites["Kael"]
    )
    display_dialogue_box(
        screen,
        "Kael détourne les yeux, l’air plus dur qu’à son habitude.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Kael (froidement) : Nous avons servi, pourtant. Mon père a levé des hommes pour l’Empire. "
        "Mais Vilmar II a préféré vendre nos terres pour acheter la paix. "
        "L’honneur de ma famille s’est éteint dans les banquets des vainqueurs.",
        font, clock, sprites["Kael"]
    )
    display_dialogue_with_sprite(
        screen,
        "Kael (d’une voix plus basse) : Je ne suis pas ici par hasard, Aldric. "
        "Je suis entré dans cette tour en espérant y trouver quelque chose… "
        "Un pouvoir, un artefact, n’importe quoi. "
        "Quelque chose qui pourra rendre aux Sielmarr la place qu’ils méritent. Je ne partirai pas les mains vides.",
        font, clock, sprites["Kael"]
    )
    display_dialogue_box(
        screen,
        "Kael se tait, laissant le vent emporter ses paroles. Il semble fragile, presque brisé, mais l’étincelle de colère brûle encore dans ses yeux.",
        font, clock
    )
    # Introduction des choix avec Kael
    display_dialogue_box(
        screen,
        "Que répondez-vous à Kael ?",
        font, clock
    )

    # Définition des choix concernant Kael
    choix_kael = [
        (
            "(Relation +35) Ta famille a encore une chance, Kael. Et toi aussi.",
            lambda h: h.get_relation("Kael").score >= 35,
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (souriant doucement) : Tu portes plus que leur nom, Kael. Tu portes leur mémoire. "
                    "Si tu es encore debout, c’est parce que leur héritage est vivant en toi.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Kael (le regard baissé) : Je veux y croire… mais c’est dur. "
                    "Chaque minute dans cette tour me rappelle ce que j’ai perdu.", 
                    font, clock, sprites["Kael"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (posant une main sur son épaule) : Tu n’as pas tout perdu. "
                    "Regarde jusqu’où tu es allé. Si cette tour peut donner quelque chose, "
                    "je suis certain que tu seras là pour le prendre.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Kael (un sourire discret) : Merci… J’espère que tu dis vrai. On est parti du mauvais pied toi et moi... "
                    "Je ne pensais pas te considérer comme un allié un jour, mais il semble que cette tour "
                    "réserve bien des surprises.", 
                    font, clock, sprites["Kael"]
                ),
                display_dialogue_box(
                    screen,
                    "(Relation Kael +10)",
                    font, clock
                ),
                h.get_relation("Kael").adjust_score(+10)
            ]
        ),
        (
            "T’as de l’ambition. C’est bien. Mais ne te laisse pas bouffer par ça.",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (le regard sévère) : L’ambition peut te guider, Kael. Mais ne la laisse pas te consumer. "
                    "La tour a une façon bien particulière de tester ce genre de choses.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Kael (hésitant) : Tu crois que je vais finir comme ces nobles déchus, ivres de pouvoir ?", 
                    font, clock, sprites["Kael"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric : Je crois que tu sais mieux que moi ce que ça coûte. Ne perds pas ça de vue.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Kael (hochement de tête) : Hm… Tu n’as peut-être pas tort. Merci, Aldric.", 
                    font, clock, sprites["Kael"]
                ),
            ]
        ),
        (
            "(Relation -20) Garde tes illusions. L’honneur ne remplit pas les tombes.",
            lambda h: h.get_relation("Kael").score <= -20,
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (sèchement) : Tu crois que l’honneur sauvera ta maison ? Ce n’est qu’un mirage.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Kael (les poings serrés) : Tu crois que je ne le sais pas ?! "
                    "Je n’ai rien d’autre à quoi m’accrocher.", 
                    font, clock, sprites["Kael"]
                ),
                display_dialogue_box(
                    screen,
                    "Aldric tourne les talons, laissant Kael seul face à ses démons. "
                    "Le noble serre les dents, dissimulant sa colère.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Kael (voix basse) : Tu n’as jamais eu à perdre tout ce que tu aimais, toi…", 
                    font, clock, sprites["Kael"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric : Tu ne sais rien de moi.", 
                    font, clock, sprites["Aldric"]
                ),
                h.get_relation("Kael").adjust_score(-10)
            ]
        )
    ]

    # Affichage des choix et gestion de la sélection
    options = [(option[0], index) for index, option in enumerate(choix_kael) if option[1] is None or option[1](hero)]
    choix = display_choices_box(screen, font, options, clock)

    if choix is not None:
        choix_kael[choix][2](hero)

    # Narration : Rencontre avec Zyn et Yohna
    display_dialogue_box(
        screen,
        "Alors qu'ils s'apprêtent à traverser la salle, Aldric et Kael s'arrêtent devant Zyn et Yohna. "
        "Les deux jumeaux, adossés à une colonne, semblent les observer depuis un moment.",
        font, clock
    )

    # Dialogue avec Yohna et Zyn
    display_dialogue_with_sprite(
        screen,
        "Yohna (croisant les bras, fixant Aldric) : Dis-moi, Aldric… Comment tu fais pour arriver jusqu'ici avec juste une épée ?",
        font, clock, sprites["Yohna"]
    )
    display_dialogue_with_sprite(
        screen,
        "Zyn (reniflant) : Ouais. T'as même pas une égratignure. Tu triches, c'est ça ?",
        font, clock, sprites["Zyn"]
    )
    display_dialogue_box(
        screen,
        "Kael esquisse un léger sourire tandis qu’Aldric hausse les épaules.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Aldric (amusé) : Va savoir. Peut-être que la tour m'aime bien.",
        font, clock, sprites["Aldric"]
    )
    display_dialogue_with_sprite(
        screen,
        "Yohna (ricanant doucement) : Hm, je doute que la tour aime qui que ce soit.",
        font, clock, sprites["Yohna"]
    )
    display_dialogue_with_sprite(
        screen,
        "Zyn (jetant un regard à sa sœur) : Pas même nous…",
        font, clock, sprites["Zyn"]
    )

    # Background Invokeurs
    display_dialogue_box(
        screen,
        "Yohna détourne le regard vers le feu de la cheminée au centre de la pièce. "
        "Sa voix s’adoucit, mais reste teintée d’amertume.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Yohna : Nous venons d’Yzunfarl… Là-bas, les invokeurs étaient autrefois respectés. "
        "Mais ça, c’était avant la chute. Avant la folie de Vilmar II.",
        font, clock, sprites["Yohna"]
    )
    display_dialogue_with_sprite(
        screen,
        "Kael (serrant les poings) : Encore ce foutu empereur…",
        font, clock, sprites["Kael"]
    )
    display_dialogue_with_sprite(
        screen,
        "Zyn (d’une voix grave, fixant Aldric droit dans les yeux) : Quand les barbares du Nord ont attaqué l'Empire, "
        "Vilmar II nous a tenus pour responsables. Il disait que nos pactes avec les esprits avaient attiré la malchance…",
        font, clock, sprites["Zyn"]
    )
    display_dialogue_box(
        screen,
        "Zyn serre les poings, la colère suintant dans sa voix.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Zyn : L'Empereur a envoyé ses armées sur nous. Yzunfarl, la cité des nôtres, a été réduite en cendres. "
        "Nos anciens ont été brûlés vifs, et ceux qui restaient ont fui dans les montagnes.",
        font, clock, sprites["Zyn"]
    )
    display_dialogue_with_sprite(
        screen,
        "Yohna (hoche la tête) : Nous étions des héros, et du jour au lendemain, nous sommes devenus des traîtres.",
        font, clock, sprites["Yohna"]
    )
    display_dialogue_with_sprite(
        screen,
        "Zyn : La tour est notre seule chance. On n’a pas de chez nous où retourner. On est ici pour nous endurcir.",
        font, clock, sprites["Zyn"]
    )
    display_dialogue_with_sprite(
        screen,
        "Kael (calmement, d’une voix emplie de compassion) : Je sais ce que c’est... de tout perdre à cause d'un souverain fou et sénile…",
        font, clock, sprites["Kael"]
    )
    display_dialogue_box(
        screen,
        "Un silence lourd retombe. Zyn et Yohna observent Kael avec un mélange de curiosité et de méfiance.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Zyn (voix basse) : Nous, on ne veut pas survivre. On veut voir l’Empire brûler comme Yzunfarl.",
        font, clock, sprites["Zyn"]
    )
    # Introduction des choix avec les jumeaux
    display_dialogue_box(
        screen,
        "Que répondez-vous aux jumeaux ?",
        font, clock
    )

    # Définition des choix concernant les jumeaux
    choix_invokeurs = [
        (
            "C’est suicidaire. Vous devriez penser à vivre.",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (avec sincérité) : Je comprends votre colère. Mais mourir ne vous ramènera pas Yzunfarl. "
                    "Vous êtes jeunes. Vous devriez penser à vivre, à reconstruire ailleurs.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Yohna (baissant les yeux, un léger sourire triste aux lèvres) : Tu crois qu’on peut juste… abandonner tout ça ?", 
                    font, clock, sprites["Yohna"]
                ),
                display_dialogue_box(
                    screen,
                    "Elle semble réfléchir, mais son regard brille encore d’une flamme vacillante.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Zyn (froid, regard perçant) : Ce monde ne nous a laissé que la haine. "
                    "Tant que Vilmar II respirera, aucune vie ne sera possible pour nous.", 
                    font, clock, sprites["Zyn"]
                ),
                display_dialogue_box(
                    screen,
                    "(Zyn -10 Yohna +20)",
                    font, clock
                ),
                h.get_relation("Yohna").adjust_score(+20),
                h.get_relation("Zyn").adjust_score(-10)
            ]
        ),
        (
            "Personne n’aime l’Empereur… mais il est intouchable.",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (croisant les bras) : Même si je partage votre haine, Vilmar II n'est pas qu’un homme. "
                    "Il est un symbole protégé par l’Empire. Si vous l’attaquez, vous signerez votre arrêt de mort.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Yohna (secouant la tête, déçue) : Toujours la même rengaine…", 
                    font, clock, sprites["Yohna"]
                ),
                display_dialogue_box(
                    screen,
                    "(Yohna -10)",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Zyn (plissant les yeux, plus déterminé que jamais) : Quelqu’un doit bien finir par essayer. "
                    "On préfère mourir en défiant l’Empire que de vivre en mendiants et en amuseur de cirque.", 
                    font, clock, sprites["Zyn"]
                ),
                display_dialogue_box(
                    screen,
                    "(Zyn +10)",
                    font, clock
                ),
                h.get_relation("Yohna").adjust_score(-10),
                h.get_relation("Zyn").adjust_score(+10)
            ]
        ),
        (
            "Vous devriez vous venger. C’est votre droit.",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (posant sa main sur la garde de son épée) : Je ne vous dirai pas de renoncer. "
                    "La vengeance est parfois la seule chose qui nous maintient debout.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Yohna (souriant faiblement) : Tu es plus honnête que je pensais. Ça fait du bien d’entendre ça.", 
                    font, clock, sprites["Yohna"]
                ),
                display_dialogue_box(
                    screen,
                    "(Yohna +10)",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Zyn (hoche la tête, un éclat sombre dans les yeux) : Tu comprends… mieux que beaucoup ici.", 
                    font, clock, sprites["Zyn"]
                ),
                display_dialogue_box(
                    screen,
                    "(Zyn +10)",
                    font, clock
                ),
                h.get_relation("Yohna").adjust_score(+10),
                h.get_relation("Zyn").adjust_score(+10)
            ]
        )
    ]

    # Affichage des choix et gestion de la sélection
    options = [(option[0], index) for index, option in enumerate(choix_invokeurs) if option[1] is None or option[1](hero)]
    choix = display_choices_box(screen, font, options, clock)

    if choix is not None:
        choix_invokeurs[choix][2](hero)
        
    # Narration : Les jumeaux s'éloignent
    display_dialogue_box(
        screen,
        "Alors que les jumeaux s'éloignent, Kael s'approche légèrement d'Aldric, le regard pensif.",
        font, clock
    )

    # Dialogue entre Kael et Aldric
    display_dialogue_with_sprite(
        screen,
        "Kael (murmure) : Ils ont de la hargne. Je leur reconnais ça. Mais ils finiront par se brûler.",
        font, clock, sprites["Kael"]
    )
    display_dialogue_with_sprite(
        screen,
        "Aldric (calme, fixant la cheminée) : Peut-être. Mais parfois, il faut laisser brûler ce qui ne peut plus être éteint.",
        font, clock, sprites["Aldric"]
    )
    display_dialogue_box(
        screen,
        "Kael ne répond pas, et les deux hommes rejoignent le reste du groupe, laissant derrière eux la chaleur du feu et la froideur de la vengeance des invokeurs.",
        font, clock
    )

    # Narration : Aldric réfléchit à Archeon
    display_dialogue_box(
        screen,
        "Aldric s’installe seul près d’une table basse, jouant distraitement avec une miche de pain tout en observant la flamme dans la cheminée. "
        "Ses pensées dérivent vers Archeon. Ce regard... cette familiarité. Avait-il vraiment déjà vu cet homme ailleurs ? Ou était-ce une illusion savamment tissée par la tour ?",
        font, clock
    )
    display_dialogue_box(
        screen,
        "Chaque mot d'Archeon résonne encore dans son esprit, éveillant un malaise qu'il ne parvient pas à chasser.",
        font, clock
    )

    # Rencontre avec Durnir
    display_dialogue_with_sprite(
        screen,
        "Durnir (calme) : Les questions qui te rongent ne trouveront pas toutes de réponse ce soir.",
        font, clock, sprites["Durnir"]
    )
    display_dialogue_box(
        screen,
        "Aldric lève les yeux. Le vieux mage s’est approché en silence, s’installant en face de lui avec une tasse fumante dans la main.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Aldric (curieux) : Je ne vous ai pas vu approcher…",
        font, clock, sprites["Aldric"]
    )
    display_dialogue_with_sprite(
        screen,
        "Durnir (souriant doucement) : Je marche avec le poids des ans, jeune homme. Il m’arrive d’être aussi léger qu’un souffle.",
        font, clock, sprites["Durnir"]
    )

    # Silence et observation
    display_dialogue_box(
        screen,
        "Un silence confortable s'installe. Seul le crépitement du feu emplit l’espace, jusqu’à ce que Durnir rompe à nouveau le silence.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Durnir : Je ne suis pas surpris que tu sois arrivé si haut dans la tour. Je t’ai observé, étage après étage. Tu as cet esprit…",
        font, clock, sprites["Durnir"]
    )
    display_dialogue_with_sprite(
        screen,
        "Aldric (fronçant les sourcils) : Quel esprit ?",
        font, clock, sprites["Aldric"]
    )
    display_dialogue_with_sprite(
        screen,
        "Durnir : Celui qui continue de grimper même quand tout s’effondre autour de lui. Ce genre d’âme finit toujours par se démarquer.",
        font, clock, sprites["Durnir"]
    )
    # Introduction des choix avec Durnir
    display_dialogue_box(
        screen,
        "Que demandez-vous à Durnir ?",
        font, clock
    )

    # Définition des choix concernant Durnir
    choix_durnir = [
        (
            "Que savez-vous de cette tour ?",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (le regard fixé sur Durnir) : Vous semblez en savoir plus que vous ne le laissez entendre. "
                    "Que savez-vous vraiment de cette tour ?", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Durnir (penchant la tête) : Pas plus que ce que les vieux livres racontent. La tour a toujours été là. "
                    "Mais sa construction ne relève d’aucune ingénierie humaine.", 
                    font, clock, sprites["Durnir"]
                ),
                display_dialogue_box(
                    screen,
                    "Son regard s'assombrit légèrement.",
                    font, clock
                ),
                display_dialogue_with_sprite(screen, 
                    "Durnir : Même l'Empereur et les seigneurs de l’Empire redoutent cette tour. "
                    "C'est là la preuve de sa longévité millénaire.", 
                    font, clock, sprites["Durnir"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (pensif) : Vous parlez comme si la tour avait sa propre volonté.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Durnir (souriant faiblement) : Peut-être que c'est le cas… Peut-être pas. Les légendes laissent souvent de la place au doute.", 
                    font, clock, sprites["Durnir"]
                ),
                display_dialogue_box(
                    screen,
                    "(Relation Durnir +15)",
                    font, clock
                ),
                h.get_relation("Durnir").adjust_score(+15)
            ]
        ),
        (
            "Avez-vous encore ce livre qui parle de la tour ?",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (intéressé) : Vous aviez mentionné des livres. En avez-vous encore un sur la tour ?", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Durnir (secouant la tête) : Non, malheureusement. Les livres anciens ont été saisis… ou brûlés. "
                    "La peur de ce que nous ne comprenons pas pousse souvent les puissants à détruire ce qui pourrait les éclairer.", 
                    font, clock, sprites["Durnir"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric : Quel dommage…", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Durnir (d’une voix posée) : Les réponses sont peut-être ailleurs, Aldric. "
                    "Ce n’est pas toujours dans les pages que nous trouvons ce que nous cherchons.", 
                    font, clock, sprites["Durnir"]
                ),
                display_dialogue_box(
                    screen,
                    "(Relation Durnir +10)",
                    font, clock
                ),
                h.get_relation("Durnir").adjust_score(+10)
            ]
        ),
        (
            "Êtes-vous déjà venu ici auparavant ?",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (observant Durnir avec insistance) : Vous semblez étrangement familier avec cet endroit. "
                    "Est-ce la première fois que vous gravissez la tour ?", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Durnir (sourire énigmatique) : Le temps est un étrange compagnon, Aldric. "
                    "Parfois, il semble nous ramener à des lieux que l’on croyait oubliés…", 
                    font, clock, sprites["Durnir"]
                ),
                display_dialogue_box(
                    screen,
                    "Le vieux mage ne répond pas directement, laissant planer le doute. "
                    "Aldric choisit de ne pas insister, sentant qu'il n'obtiendra rien de plus pour l'instant.",
                    font, clock
                ),
            ]
        )
    ]

    # Affichage des choix et gestion de la sélection
    options = [(option[0], index) for index, option in enumerate(choix_durnir) if option[1] is None or option[1](hero)]
    choix = display_choices_box(screen, font, options, clock)

    if choix is not None:
        choix_durnir[choix][2](hero)

    # Narration post-dialogue
    display_dialogue_with_sprite(screen, 
        "Aldric (se grattant la tête) : Durnir, j'ai encore une question...", 
        font, clock, sprites["Aldric"]
    )
    display_dialogue_with_sprite(screen, 
        "Durnir : Dites-moi !", 
        font, clock, sprites["Durnir"]
    )
    # Introduction des choix : Motivation de Durnir
    display_dialogue_box(
        screen,
        "Que voulez-vous savoir d’autre ?",
        font, clock
    )

    # Définition des choix concernant la motivation de Durnir
    choix_motivation = [
        (
            "Pourquoi êtes-vous ici ? Que cherchez-vous vraiment ?",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric : Vous semblez avoir vos propres raisons de grimper cette tour. "
                    "Qu’espérez-vous y trouver, Durnir ?", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Durnir (posant sa tasse) : L’Académie d’Urdragen s’effondre. La magie perd du terrain. "
                    "Les décrets anti-magie de l’Empire affaiblissent nos rangs. "
                    "Je crains que bientôt, les mages ne soient plus que des reliques chassées.", 
                    font, clock, sprites["Durnir"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Aldric (froid) : Vous pensez que l’Empire vous traquera jusqu’au dernier ?", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Durnir (calme) : Ils ont peur de ce qu’ils ne contrôlent pas. La tour… pourrait cacher "
                    "un artefact qui redonnera espoir. Ou du moins, une raison de croire.", 
                    font, clock, sprites["Durnir"]
                )
            ]
        ),
        (
            "Vous croyez qu’il existe réellement quelque chose au sommet de cette tour ?",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(screen, 
                    "Aldric (dubitatif) : Tout le monde monte ici dans l’espoir de trouver quelque chose. "
                    "Mais peut-être qu’il n’y a rien.", 
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(screen, 
                    "Durnir (souriant doucement) : L’existence même de cette tour est déjà un miracle. "
                    "Elle défie les lois du monde, Aldric. Et parfois, c’est suffisant pour espérer.", 
                    font, clock, sprites["Durnir"]
                )
            ]
        )
    ]

    # Affichage des choix et gestion de la sélection
    options = [(option[0], index) for index, option in enumerate(choix_motivation) if option[1] is None or option[1](hero)]
    choix = display_choices_box(screen, font, options, clock)

    if choix is not None:
        choix_motivation[choix][2](hero)
    # Dialogue entre Durnir et Aldric
    display_dialogue_with_sprite(
        screen,
        "Durnir (se levant avec son thé) : Sur ce, mon jeune ami, j'ai un bon vieux grimoire qui m'attend, vous m'excuserez hehe !",
        font, clock, sprites["Durnir"]
    )
    display_dialogue_with_sprite(
        screen,
        "Aldric : Bien sûr !",
        font, clock, sprites["Aldric"]
    )

    # Narration : Clotaire en deuil
    display_dialogue_box(
        screen,
        "Clotaire est assis seul près d’une colonne, le regard plongé dans la danse des flammes. "
        "Son visage est marqué par l’ombre du deuil. Emphyr l’observe de loin un instant, puis s’approche silencieusement.",
        font, clock
    )

    # Dialogue entre Clotaire et Emphyr
    display_dialogue_with_sprite(
        screen,
        "Emphyr (calme) : Ça te ressemble pas de rester silencieux aussi longtemps…",
        font, clock, sprites["Emphyr"]
    )
    display_dialogue_box(
        screen,
        "Clotaire ne lève pas les yeux. Il se contente de hausser les épaules, un sourire amer étirant brièvement ses lèvres.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Clotaire : C’est juste que… y’a plus personne pour parler à ma place, maintenant.",
        font, clock, sprites["Clotaire"]
    )
    display_dialogue_with_sprite(
        screen,
        "Emphyr (s’installant à côté de lui) : Brandio et Velm, c’est ça ?",
        font, clock, sprites["Emphyr"]
    )

    # Flashback : Rencontre avec Velm et Brandio
    display_dialogue_box(
        screen,
        "Clotaire hoche lentement la tête. Il fixe ses mains calleuses, comme si elles portaient encore les traces du sang de ses compagnons perdus.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Clotaire (d’un ton distant) : Je les ai rencontrés y’a longtemps. Des années, même. J’étais un môme des bas-fonds… "
        "Un orphelin qui volait pour survivre. C’était ça, ou crever de faim.",
        font, clock, sprites["Clotaire"]
    )
    display_dialogue_box(
        screen,
        "Clotaire (perdu dans ses souvenirs) : Je vivais dans un bordel. C’étaient les filles là-bas qui m’ont élevé… "
        "Elles m’appelaient “leur petit voleur”.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Clotaire (souriant tristement) : Elles disaient que j’avais des doigts de fée, parfaits pour détrousser les nobles distraits. "
        "Elles m’ont appris à parler, à charmer, et à survivre.",
        font, clock, sprites["Clotaire"]
    )
    display_dialogue_box(
        screen,
        "Il marque une pause, son regard se durcissant légèrement.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Clotaire : Un jour, y’avait ce bateau qui accostait au port. J’vois Velm… enfermé dans une cage. "
        "Ils allaient l’exécuter pour vol. Un simple môme qui essayait juste de bouffer.",
        font, clock, sprites["Clotaire"]
    )
    display_dialogue_with_sprite(
        screen,
        "Emphyr (curieuse) : Tu l’as libéré, pas vrai ?",
        font, clock, sprites["Emphyr"]
    )
    display_dialogue_box(
        screen,
        "Clotaire hoche la tête avec un éclat fugace dans les yeux.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Clotaire : Ouais… Je m’suis infiltré dans le fort cette nuit-là. Mais pendant que j’ouvrais sa cage, "
        "j’suis tombé sur un garde… Brandio.",
        font, clock, sprites["Clotaire"]
    )
    display_dialogue_box(
        screen,
        "Un sourire nostalgique éclaire brièvement son visage.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Clotaire : Brandio était pas comme les autres. Il m’a pas arrêté. Je crois qu’il s’est juste laissé emporter par mon baratin. "
        "Ou alors, il avait besoin d’une excuse pour quitter cette foutue garde. Il était déjà corrompu jusqu’à l’os de toute façon.",
        font, clock, sprites["Clotaire"]
    )
    display_dialogue_with_sprite(
        screen,
        "Emphyr (amusée) : Tu l’as convaincu de déserter sur-le-champ, c’est ça ?",
        font, clock, sprites["Emphyr"]
    )
    display_dialogue_with_sprite(
        screen,
        "Clotaire : J’lui ai parlé d’un rêve. D’une terre au-delà des mers… Une femme du bordel m’avait raconté ça quand j’étais gosse. "
        "Des contrées lointaines pleines de richesses, où les bêtes sont plus grandes que des chevaux, où les bâtiments sont faits d'or ! "
        "Je leur ai dit qu’on quitterait cet Empire désolant et en lambeaux et qu’on irait là-bas ensemble.",
        font, clock, sprites["Clotaire"]
    )
    display_dialogue_box(
        screen,
        "Clotaire laisse échapper un rire sans joie.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Clotaire : On y croyait. On a passé des années à amasser de quoi fuir. Sauf qu’on n’aura pas quitté cette tour tous les trois. "
        "On devait récupérer l'artefact, si il existe... et partir loin... ni vu, ni connu... peu importe le moyen.",
        font, clock, sprites["Clotaire"]
    )
    # Retour au présent – Emphyr tente de raisonner Clotaire
    display_dialogue_with_sprite(
        screen,
        "Emphyr (doucement) : Ce rêve… il vit encore en toi ?",
        font, clock, sprites["Emphyr"]
    )
    display_dialogue_box(
        screen,
        "Clotaire ne répond pas immédiatement. Il fixe la flamme, l’ombre de Velm et Brandio flottant derrière ses yeux.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Clotaire : Non. Il est mort avec eux. Ici... dans cette tour...",
        font, clock, sprites["Clotaire"]
    )
    display_dialogue_box(
        screen,
        "Emphyr pose une main légère sur son épaule.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Emphyr (doucement) : Ils ne voudraient pas te voir abandonner, Clotaire.",
        font, clock, sprites["Emphyr"]
    )
    display_dialogue_with_sprite(
        screen,
        "Clotaire (amèrement) : Peut-être. Mais ce monde, il n’a jamais eu de place pour nous. "
        "On était juste trois rêveurs qui essayaient de s’en sortir. 10 ans plus tard ils sont morts et moi je radote de vieux souvenirs.",
        font, clock, sprites["Clotaire"]
    )
    display_dialogue_box(
        screen,
        "Un silence s’installe à nouveau, mais cette fois, il semble plus léger, comme si Emphyr avait réussi à alléger "
        "ne serait-ce qu’une partie du fardeau de Clotaire.",
        font, clock
    )

    # Gallius et Aldric – Introduction
    display_dialogue_box(
        screen,
        "Gallius est adossé contre un pilier près de la fenêtre, jouant distraitement avec l’une de ses dagues. "
        "Aldric s’approche, et sans lever les yeux, Gallius devine sa présence.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Gallius (sans détourner le regard) : T’as fini tes discours de héros avec tout le monde ?",
        font, clock, sprites["Gallius"]
    )
    display_dialogue_with_sprite(
        screen,
        "Aldric (souriant) : Je tue le temps. Et j'écoutais Clotaire et Emphyr, discrètement.",
        font, clock, sprites["Aldric"]
    )
    display_dialogue_box(
        screen,
        "Gallius fait tourner sa dague entre ses doigts, un éclat d’amusement dans les yeux.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Gallius : Ah… Il s’accroche encore. Je suppose qu’on doit tous porter nos fantômes d’une manière ou d’une autre.",
        font, clock, sprites["Gallius"]
    )

    # Gallius se livre
    display_dialogue_box(
        screen,
        "Un silence s’installe alors qu’ils regardent l’Empire à travers l’arche qui mène à la terrasse. "
        "Aldric s’appuie contre le même pilier, observant Gallius du coin de l’œil.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Aldric (curieux) : Et toi ? Pourquoi tu es là ?",
        font, clock, sprites["Aldric"]
    )
    display_dialogue_box(
        screen,
        "Gallius ricane doucement, levant finalement les yeux vers Aldric.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Gallius : Tu veux vraiment savoir ? Je suis un assassin. Rien de plus.",
        font, clock, sprites["Gallius"]
    )
    display_dialogue_with_sprite(
        screen,
        "Gallius (léger sourire) : Je viens du sud, de Nauxziq'Aa. Là-bas, on dit que tant qu’il y a des hommes, il y aura toujours du travail.",
        font, clock, sprites["Gallius"]
    )
    display_dialogue_box(
        screen,
        "Il marque une pause, jouant distraitement avec la lame.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Gallius : J’ai tué des généraux en pleine bataille. Des seigneurs dans leurs châteaux. Des prêtres devant leurs autels. "
        "Certains m’appellent “l'ombre de Qaziera”. Mais pour moi… c’est juste un boulot.",
        font, clock, sprites["Gallius"]
    )
    display_dialogue_with_sprite(
        screen,
        "Aldric (fronçant les sourcils) : Et maintenant ?",
        font, clock, sprites["Aldric"]
    )
    display_dialogue_with_sprite(
        screen,
        "Gallius (en baillant) : Hm… Maintenant, les contrats manquent. J’ai tellement “fait le ménage” que je suis à court de cibles.",
        font, clock, sprites["Gallius"]
    )
    display_dialogue_box(
        screen,
        "Il rit brièvement, un rire sec et sans joie.",
        font, clock
    )
    display_dialogue_with_sprite(
        screen,
        "Gallius : Alors je suis venu ici. J’me suis dit que la tour, c’était comme des congés. Tu vois, un peu de repos… au sommet du chaos.",
        font, clock, sprites["Gallius"]
    )
    # Dialogue avec Gallius : choix
    display_dialogue_box(
        screen,
        "Que répondez-vous à Gallius ?",
        font, clock
    )

    # Définition des choix pour la conversation avec Gallius
    choix_gallius = [
        (
            "Tu prends ça à la légère… Mais ça pourrait bien te tuer.",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(
                    screen,
                    "Aldric (croisant les bras) : La tour n’est pas un terrain de jeu. "
                    "Tu sais que tu risques ta vie à chaque étage.",
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(
                    screen,
                    "Gallius (haussement d’épaules) : Je risque ma vie chaque fois que je respire. "
                    "Mais t’inquiète pas pour moi. J’ai survécu à pire.",
                    font, clock, sprites["Gallius"]
                ),
                display_dialogue_box(
                    screen,
                    "Gallius semble amusé, mais une lueur plus sérieuse traverse brièvement ses yeux.",
                    font, clock
                ),
                h.get_relation("Gallius").adjust_score(+5)
            ]
        ),
        (
            "Tu dois vraiment aimer ça… Le sang, la chasse.",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(
                    screen,
                    "Aldric : On dirait que t’as pas besoin d’une raison pour tuer. "
                    "C’est naturel, chez toi.",
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(
                    screen,
                    "Gallius (sourire en coin) : Peut-être bien. "
                    "La chasse, c’est comme respirer. Facile. Mais tu sais ce qui est difficile ? Arrêter.",
                    font, clock, sprites["Gallius"]
                ),
                display_dialogue_box(
                    screen,
                    "Gallius s’appuie contre le pilier, l’air détendu, mais ses yeux restent perçants.",
                    font, clock
                ),
                h.get_relation("Gallius").adjust_score(+10)
            ]
        ),
        (
            "Tu crois que la tour peut vraiment t’apporter quelque chose ?",
            None,  # Pas de condition requise
            lambda h: [
                display_dialogue_with_sprite(
                    screen,
                    "Aldric (calmement) : Tu parles comme si tout ça n’avait aucune importance. "
                    "Mais au fond, pourquoi tu grimpes encore plus haut ?",
                    font, clock, sprites["Aldric"]
                ),
                display_dialogue_with_sprite(
                    screen,
                    "Gallius (baisse les yeux un instant) : Je me le demande moi-même. "
                    "Peut-être qu’au sommet, y’aura plus rien à chasser. "
                    "Ou peut-être que je trouverai enfin quelque chose d’assez fort pour m’arrêter.",
                    font, clock, sprites["Gallius"]
                ),
                display_dialogue_box(
                    screen,
                    "Un silence s’installe. Gallius garde un air impassible, mais Aldric sent un éclat de vérité dans ses mots.",
                    font, clock
                ),
                h.get_relation("Gallius").adjust_score(+15)
            ]
        )
    ]

    # Affichage des choix et gestion de la sélection
    options = [(option[0], index) for index, option in enumerate(choix_gallius) if option[1] is None or option[1](hero)]
    choix = display_choices_box(screen, font, options, clock)

    if choix is not None:
        choix_gallius[choix][2](hero)




    




    
    fade_out_music(fade_duration=4000)
    fade_in_text(screen, "Fin du Chapitre 7 - Il reste 10 participants sur 99 et 94 étages", font, (WIDTH // 2, HEIGHT // 2), duration=2000)
    fade_out_text(screen, 1000)
    game_menu(screen, font, clock, WIDTH, HEIGHT, hero)

def main():
    clock = pygame.time.Clock()
    hero = None

    while True:
        option = main_menu(screen, font, clock)

        if option == 0:
            hero = Heros()
            hero.chapter_reached = 1
            start_chapter(hero, screen, font, clock)
        elif option == 1:
            hero = load_game()
            if hero:
                start_chapter(hero, screen, font, clock)
        elif option == 2:
            pygame.quit()
            sys.exit()

def start_chapter(hero, screen, font, clock):
    chapitre_nom = f"chapitre_{hero.chapter_reached}"
    if chapitre_nom in globals():
        sprites = load_sprites()  # Charge les sprites
        chapter_func = globals()[chapitre_nom]
        
        # Vérifie si la fonction du chapitre attend des sprites
        if chapter_func.__code__.co_argcount == 5:
            chapter_func(hero, screen, font, clock, sprites)
        else:
            chapter_func(hero, screen, font, clock)
    else:
        print(f"Le chapitre {hero.chapter_reached} n'est pas encore implémenté.")
        
        
        
def game_menu(screen, font, clock, width, height, hero=None):
    options = ["Continuer", "Afficher Relations", "Sauvegarder", "Quitter"]
    selected = 0

    while True:
        # Efface l'écran pour éviter des éléments persistants
        screen.fill((0, 0, 0))

        # Affiche le menu et récupère l'option sélectionnée
        selected = display_game_menu(screen, font, clock, options)

        # Affichage de la santé en bas de l'écran
        if hero:  # Vérifie que le héros est défini
            health_text = f"Santé : {hero.health}/100"
            health_surface = font.render(health_text, True, (255, 50, 50))
            health_rect = health_surface.get_rect(center=(width // 2, 30))  # Position en haut
            screen.blit(health_surface, health_rect)
            
            
        # Met à jour l'écran après affichage
        pygame.display.flip()

        # Actions en fonction de l'option sélectionnée
        if selected == 0:  # Continuer au prochain chapitre
            hero.chapter_reached += 1
            save_game(hero)
            start_chapter(hero, screen, font, clock)

        elif selected == 1:  # Afficher Relations avec retour au menu
            display_relations_screen(screen, font, clock, hero)

        elif selected == 2:  # Sauvegarder la Partie avec confirmation
            save_game(hero)
            display_save_confirmation(screen, font, "Partie sauvegardée avec succès.")

        elif selected == 3:  # Retour au menu principal
            menu_stack.clear()  # Vide la pile pour s'assurer de revenir au main_menu
            main_menu(screen, font, clock)  # Relance le menu principal

def game_over(self, screen, font, clock):
        # Écran de game over
        screen.fill((0, 0, 0))
        game_over_font = pygame.font.Font("graphics/resources/font/CinzelDecorative-Bold.otf", 70)
        message_font = pygame.font.Font("graphics/resources/font/Cinzel-Regular.otf", 40)

        game_over_text = game_over_font.render("Game Over", True, (255, 50, 50))
        message_text = message_font.render("Aldric a trépassé dans la Tour...", True, (255, 255, 255))
        continue_text = message_font.render("Appuyez sur Entrée pour continuer", True, (200, 200, 200))

        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, 200))
        screen.blit(message_text, (screen.get_width() // 2 - message_text.get_width() // 2, 300))
        screen.blit(continue_text, (screen.get_width() // 2 - continue_text.get_width() // 2, 450))

        pygame.display.flip()

        # Attente de l'entrée pour revenir au menu principal
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                        main_menu(screen, font, clock)  # Retour au menu principal         
if __name__ == "__main__":
    main()




