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
    "Garen : Salut… Euh… toi aussi, tu participes ? Haha, évidemment, sinon tu ne serais pas là, hein ?",
    font, clock, sprite_garen)
    
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
    background = fade_in_background(screen,"graphics/resources/backgrounds/Kael1.PNG", WIDTH, HEIGHT)
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
    
    clear_screen(screen)
    fade_in_text(screen, 
             "Chapitre 2 : L'ascension commence", 
             font, 
             (WIDTH // 2, HEIGHT // 2),  # Centré sur l'écran
             duration=3000)
    fade_out_text(screen, 3000, fade_speed=2)
    pygame.time.wait(1000)
    
    fade_in_music("graphics/resources/music/AmbientHades.mp3", max_volume=0.2, fade_duration=4000)
    
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
    "Kael croise les bras, jetant un regard dédaigneux à l’inscription. "
    "Malgré ses mots, son regard s’attarde un instant de trop sur les statues, "
    "comme s’il s’attendait à ce qu’elles bougent.",
    font, clock
    )
    background = fade_in_background(screen,"graphics/resources/backgrounds/stele1.webp", WIDTH, HEIGHT)
    display_dialogue_with_sprite(screen,
    "Garen : Abandonner… ça veut dire qu’on doit sacrifier quelque chose ?",
    font, clock, sprite_garen
    )

    display_dialogue_box(screen,
    "Garen fronce les sourcils, cherchant un sens plus profond dans ces quelques mots. "
    "Ses doigts tapotent nerveusement la poignée de son épée. "
    "Il n’aime pas ce qu’il ressent ici, et ça se voit.",
    font, clock
    )

    display_dialogue_with_sprite(screen,
    "Aldric : Il y a forcément un piège. Rien n’est gratuit ici.",
    font, clock, sprite_aldric
    )

    display_dialogue_box(screen,
    "Votre propre voix résonne dans l’obscurité. En avançant d’un pas, vous sentez la présence des statues peser davantage. "
    "Elles semblent vous scruter, jaugeant chaque mot, chaque hésitation.",
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
                "Kael : Le mercenaire a de la repartie. esperons que ca te serve",
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
    "Participant : Tu crois tout savoir, hein ? Pourquoi tu ne passes pas devant et ne nous montres pas comment faire, noble chevalier ?",
    font, clock, sprite_random_participant
    )
    fade_out_music(fade_duration=1000)
    display_dialogue_with_sprite(screen,
    "Kael (murmurant à Aldric) : Ça va mal finir…",
    font, clock, sprite_kael
    )
    background = fade_in_background(screen, "graphics/resources/backgrounds/attack.webp", WIDTH, HEIGHT)

    display_dialogue_with_sprite(screen,
    "Le participant se précipite soudain vers Garen, les poings levés, prêt à frapper.",
    font, clock, sprite_random_participant
    )

    # Choix du joueur : Intervenir ou non
    choix = display_choices_box(screen, font, [
    ("Intervenir et tuer l’assaillant", 0),
    ("Se mettre devant Garen", 1),
    ("Ne rien faire", 2)
    ], clock)

    if choix == 0:  # Intervenir et tuer l'assaillant
        display_dialogue_with_sprite(screen,
        "Aldric s’élance sans hésiter et intercepte l’assaillant. "
        "Dans un mouvement fluide, il dégaine son épée et abat l’homme sur place. "
        "Le silence retombe, lourd et pesant.",
        font, clock, sprite_aldric
        )
        display_dialogue_with_sprite(screen,
        "Kael : Eh bien… tu n’y es pas allé de main morte. Espérons que cela dissuadera les autres.",
        font, clock, sprite_kael
        )
        display_dialogue_with_sprite(screen,
        "Garen (tête baissée) : Tu n'etait pas obligé de le tuer...(Garen -5, Kael +10)",
        font, clock, sprite_kael
        )
        hero.get_relation("Kael").adjust_score(+10)  # Kael apprécie la fermeté
        hero.get_relation("Garen").adjust_score(+5)
        

    elif choix == 1:  # Se mettre devant Garen
        display_dialogue_with_sprite(screen,
        "Vous vous placez devant Garen, prêt à encaisser l’attaque. "
        "L’assaillant s’élance… mais s’effondre soudainement, une dague enfoncée dans son dos. ",
        font, clock, sprite_aldric
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
    "Garen : On… on fait quoi ? Je pense qu'on devrait s'agenouiller... c'est... c'est une épreuve d'humilité !!",
    font, clock, sprite_garen
    )

    # Présentation des choix
    def chapitre_2_final_choice(hero, screen, font, clock, sprites):
        global background
        display_dialogue_box(screen,
        "Que fais-tu ?\n",
        font, clock
        )

    # Définition des options de choix
        options = [
        ("S’agenouiller et traverser la porte.", 1),
        ("Observer et attendre.", 2)
        ]

    # Affiche la boîte de choix
        choix = display_choices_box(screen, font, options, clock)

    # Gestion des choix
        if choix == 0:  # S’agenouiller et traverser la porte
            display_dialogue_box(screen,
            "Aldric s’agenouille devant la porte. Une chaleur étrange envahit ton corps. "
            "La grille s'ouvre lentement. (Garen +5 : A suivi son conseil)",
            font, clock
            )
            hero.get_relation("Garen").adjust_score(+5)

        elif choix == 1:  # Observer et attendre
            display_dialogue_box(screen,
            "Aldric observe les autres participants. Kael traverse après hésitation, Garen te suit de loin.",
            font, clock
         )
        else:
            display_dialogue_box(screen,
            "Choix invalide. Aldric attend.",
            font, clock
        )
    chapitre_2_final_choice(hero, screen, font, clock, sprites)
    background = fade_in_background(screen,"graphics/resources/backgrounds/escalier.webp", WIDTH, HEIGHT)
    # Passage à l'étage suivant
    display_dialogue_box(screen,
    "Après avoir franchi la porte, vous montez les escaliers menant à l’étage suivant. "
    "Derrière vous, la porte se referme lourdement.",
    font, clock
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
    "Garen (haletant légèrement) : Tu parles comme si c’était une promenade… J’ai cru que cette porte ne s’ouvrirait jamais…",
    font, clock, sprite_garen
    )

    display_dialogue_with_sprite(screen,
    "Aldric (calme) : Si ce genre de test te fait peur, tu n’iras pas loin. C’était juste une mise en bouche.",
    font, clock, sprite_aldric
    )

    display_dialogue_box(screen,
    "Plus loin dans l'étage 1, un groupe regarde Aldric et les autres poursuivre leur chemin.",
    font, clock
    )
    
    # Description des personnages

    background = fade_in_background(screen,"graphics/resources/backgrounds/ClotaireE.PNG", WIDTH, HEIGHT)
    # Narration initiale
    display_dialogue_box(screen,
    "Dans un coin de la salle, Clotaire et son groupe échangent des regards complices. "
    "Ils parlent à voix basse, jetant de temps en temps des coups d'œil vers les autres participants. "
    "Leur comportement attire peu l’attention, mais quelque chose dans leur attitude semble… calculé.",
    font, clock
    )

    # Dialogue des personnages
    display_dialogue_with_sprite(screen,
    "Clotaire : Bien joué Emphyr... t'agenouiller était donc la clef... tu es si maligne.",
    font, clock, sprite_clotaire
    )

    display_dialogue_with_sprite(screen,
    "Emphyr : Oh je t'en prie, c'est parce que Velm l'a dit en plaisantant.",
    font, clock, sprite_emphyr
    )

    display_dialogue_with_sprite(screen,
    "Velm : Ahah je suis pas si bête hein ?",
    font, clock, sprite_velm
    )

    display_dialogue_with_sprite(screen,
    "Brandio : Si, tu es bête. On appelle cela la chance, imbécile.",
    font, clock, sprite_brandio
    )

    display_dialogue_with_sprite(screen,
    "Emphyr : C'est bon les gars, vous m'avez épuisée. Moi j'avance...",
    font, clock, sprite_emphyr
    )

    display_dialogue_with_sprite(screen,
    "Clotaire : Vous avez entendu la demoiselle ? On avance !",
    font, clock, sprite_clotaire
    )

    display_dialogue_with_sprite(screen,
    "Velm et Brandio : Oui boss !!!",
    font, clock, sprite_brandio
    )


    fade_out_music(fade_duration=4000)
    fade_in_text(screen, "Fin du Chapitre 2 - Il reste 93 participants sur 99.", font, (WIDTH // 2, HEIGHT // 2), duration=2000)
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
        selected = display_game_menu(screen, font, clock, options)
        
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
            
if __name__ == "__main__":
    main()




"""
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

"""    
