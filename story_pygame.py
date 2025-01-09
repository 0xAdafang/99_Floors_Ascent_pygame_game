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
    fade_in_music("graphics/resources/music/AmbientHecate.mp3", max_volume=0.2, fade_duration=4000)
    
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
             "Chapitre 5 : La lueur d'un répis - Etage 4/99", 
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
        archeon = Character("Archeon", "Un homme énigmatique à la présence magnétique.", "inconnu")
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
    
    background = fade_in_background(screen, "graphics/resources/backgrounds/banquet.webp", WIDTH, HEIGHT)
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
                hero.get_relation("Garen").adjust_score(15)
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
                "Aldric  : Possible que non..il reste 95 étages et on deja plus que 39 mais je crois que nous savions tous que c'etait un aller simple.", 
                font, clock, sprite_aldric
                )
                display_dialogue_box(screen,
                "A qui voulez vous parler ?",                     
                font, clock)

            elif choix_garen == 1:  # Réponse négative
                hero.get_relation("Garen").adjust_score(-5)
                display_dialogue_with_sprite(screen, 
                "Garen (déçu, baissant la tête encore plus bas) : Tu... tu as sûrement raison. Je ne suis qu'un boulet… "
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
                "A qui voulez vous parler ?",                     
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
            "Tu comprends ça, non ?", 
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
                hero.get_relation("Kael").adjust_score(-5)
                display_dialogue_with_sprite(screen,
                "Kael (hausse un sourcil, amusé) : Hm… sans doute. Qui sait ?", 
                font, clock, sprite_kael
                )
                display_dialogue_box(screen, 
                "Il prend une nouvelle gorgée, sans se départir de ce sourire narquois.", 
                font, clock
                )
                display_dialogue_with_sprite(screen, 
                "Kael : Tu es bien plus malin que tu en as l'air, Aldric.", 
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
                "Aldric : Il a disparu quand j'etait gamin...j'en ai des souvenirs mais eparsse..", 
                font, clock, sprite_aldric
                )
                display_dialogue_with_sprite(screen, 
                "Kael : Tu pense qu'il est ici ?", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Aldric : C'est ma dernière théorie...", 
                font, clock, sprite_aldric
                )
                display_dialogue_box(screen,
                "A qui voulez vous parler ?",                     
                font, clock)

            elif choix_kael == 1:  # Réponse : Tu mens mal
                hero.get_relation("Kael").adjust_score(15)
                display_dialogue_with_sprite(screen,
                "Kael (sourire effacé, l'air surpris) : …Hah, t'es un petit futé toi. "
                "Je l'avais deviné dès qu'on s'est croisés à l'extérieur de la tour.", 
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
                display_dialogue_with_sprite(screen, 
                "Kael : Mais je te respecte. Contrairement à d'autres ici…même si je ne sais pas ce qui te motive a tenter l'ascension..", 
                font, clock, sprite_kael
                )
                display_dialogue_with_sprite(screen, 
                "Aldric : Hm..mon à disparu quand j'etait gamin...je suis tombé sur son journal il a mentionné la tour ", 
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
                "Kael (souriant à nouveau) : Alors Tâchons de ne pas mourir trop bas dans cette foutue tour pour trouver ce qu'on cherche..", 
                font, clock, sprite_kael
                )
                display_dialogue_box(screen, 
                "Les deux hommes échangent une poignée de main ferme. La tension entre eux s'atténue légèrement.", 
                font, clock
                )
                display_dialogue_box(screen,
                "A qui voulez vous parler ?",                     
                font, clock)


        elif personnage == "Parler à Ayela.":
            display_dialogue_with_sprite(screen,
            "Aldric (vous approchez Ayela, assise à l'écart des autres, fixant le vide) : "
            "Et toi, alors, pourquoi tenter cette aventure presque suicidaire ?", 
            font, clock, sprite_aldric
            )
            display_dialogue_box(screen, 
            "Ayela détourne légèrement les yeux, cherchant ses mots. Ses mains tremblent légèrement sur son arc posé à ses côtés.", 
            font, clock
            )
            display_dialogue_with_sprite(screen, 
            "Ayela (voix douce, presque murmurée) : Mon village est frappé par une épidémie. Personne ne sait d'où ça vient…", 
            font, clock, sprite_ayela
            )
            display_dialogue_box(screen, 
            "Sa voix se brise un instant, trahissant une fragilité qu'elle s'efforce de masquer. J'ai pensé… que cette tour pourrait m'apporter des réponses.", 
            font, clock
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
            "Ayela (à voix basse) : C'était stupide, je le sais… Peut-être que je ne fais que courir vers ma mort.", 
            font, clock, sprite_ayela
            )

    # Options de réponse pour Ayela
            display_dialogue_box(screen, "Que dites-vous à Ayela ?", font, clock)
            options_ayela = [
            ("Ce n'est pas stupide. Tu fais ce que tu peux.", 5),
            ("Les chances sont faibles. Ne te fais pas d'illusions.", -15)
            ]
            choix_ayela = display_choices_box(screen, font, options_ayela, clock)

    # Branches des réponses
            if choix_ayela == 0:  # Réponse : Ce n'est pas stupide
                hero.get_relation("Ayela").adjust_score(5)
                display_dialogue_box(screen, 
                "Ayela lève les yeux vers vous, rougissante et légèrement surprise par votre réponse.", 
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
                "A qui voulez vous parler ?",                     
                font, clock)

            elif choix_ayela == 1:  # Réponse : Les chances sont faibles
                hero.get_relation("Ayela").adjust_score(-15)
                display_dialogue_box(screen, 
                "Ayela baisse brusquement la tête, ses épaules s'affaissant sous le poids de vos mots.", 
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
                "A qui voulez vous parler ?",                     
                font, clock)


    # Supprimer le personnage des interactions après discussion
        interactions.pop(choix_index)

# Fin des interactions
    display_dialogue_box(screen, "Vous avez discuté avec tout le monde.", font, clock)
    
    background = fade_in_background(screen,"graphics/resources/backgrounds/banquet2.webp", WIDTH, HEIGHT)
    # Clôture de l'étage 4
    display_dialogue_box(screen, 
        "Plus tard dans la soirée, une violente altercation éclate entre plusieurs participants. "
        "Les cris résonnent dans la salle sombre, étouffés par l'épaisseur des murs de pierre. "
        "Lorsque tout redevient silencieux, quatre corps sans vie jonchent le sol, leurs visages figés dans l'horreur. "
        "Qu'ils soient morts par ivresse ou par cupidité, leur sort est désormais lié à la tour.", 
        font, clock
    )

    display_dialogue_box(screen, 
        "La porte s’ouvre lentement après cela. Le prix de l’étage… payé.", 
        font, clock
    )

    display_dialogue_box(screen, 
        "Un vent glacial s'engouffre dans la salle lorsque la porte s'entrouvre, comme si la tour elle-même "
        "se nourrissait de la tragédie humaine. L'obscurité de l'étage suivant semble plus pesante encore.", 
        font, clock
    )

    # Dialogue - Réactions des personnages
    display_dialogue_with_sprite(screen, 
        "Kael (murmurant, observant les corps) : Quatre vies pour ouvrir la porte… L’énigme était littérale. La tour ne plaisante pas.", 
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
        "Garen détourne le regard des corps, serrant nerveusement le pommeau de son épée. "
        "Ses mains tremblent légèrement, mais il garde le silence.", 
        font, clock
    )
    # Début des interactions
    display_dialogue_with_sprite(screen, 
    "Garen (voix basse, hésitant) : C’est pas de la cupidité... c’est…", 
    font, clock, sprite_garen
    )

    display_dialogue_box(screen, 
    "Kael éclate d’un rire bref et amer, ses yeux reflétant une lassitude grandissante.", 
    font, clock
    )

    display_dialogue_with_sprite(screen, 
    "Kael (ricanant) : Ah oui ? Et c’est quoi alors ? On n’est pas là pour apprendre à tricoter, paysan !", 
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
    "Garen (baisse la tête, ses doigts se crispant sur sa ceinture) : ...", 
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
    "Alors que le calme semble revenir, Clotaire s'avance lentement, suivi de Velm et Brando. "
    "Leur démarche est décontractée, mais leurs yeux scrutent les environs avec une lueur dangereuse.", 
    font, clock
    )

    display_dialogue_with_sprite(screen, 
    "Clotaire (avec un sourire en coin) : Eh bien, certains n’ont pas su contenir leur soif de sang… Dommage pour eux, "
    "mais au moins la porte s'est ouverte, n’est-ce pas ?", 
    font, clock, sprite_clotaire
    )

    display_dialogue_with_sprite(screen, 
    "Velm (souriant narquoisement) : Ils ont voulu jouer aux héros. La tour n’aime pas les héros…", 
    font, clock, sprite_velm
    )

    display_dialogue_with_sprite(screen, 
    "Brando (calme, regard sombre) : On a juste laissé faire. Ils se sont entre-tués tout seuls.", 
    font, clock, sprite_brandio
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
    "Emphyr (caressant le cou de Kael) : Hm détends-toi beau gosse, sans ça la grille ne se serait pas ouverte...", 
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

# Narration - Clotaire disparaît
    display_dialogue_box(screen, 
    "Aldric observe Clotaire disparaître dans l’ombre. La porte reste ouverte, mais la salle est plus silencieuse que jamais. "
    "Le poids des pertes pèse lourdement sur les épaules des survivants.", 
    font, clock
    )




    
    
    fade_out_music(fade_duration=4000)
    fade_in_text(screen, "Fin du Chapitre 4 - Il reste 39 participants sur 99 et 96 étages", font, (WIDTH // 2, HEIGHT // 2), duration=2000)
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




