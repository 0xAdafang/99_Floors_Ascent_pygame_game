from classes import *

# Debut histoire

# Chapitre 0 - L’arrivée à la tour        
def prologue(hero):
    """Introduction immersive à l'arrivée de la Tour."""
    from rich.console import Console
    console = Console()

    # Narration d'introduction
    console.print("\n[bold cyan]=== Introduction : L'arrivée à la Tour ===[/bold cyan]")
    
    console.print("[bold magenta]« À ceux qui ont tenté, tenteront encore et échoueront... »[/bold magenta]")
    console.print(
        "[italic]Je marche encore et encore, village après village, route après route... Chaque sentier m'éloigne un peu plus du monde que je connaissais, "
        "me rapprochant d'un destin incertain. On dit que la Tour des Épreuves n'apparaît qu'à ceux qui sont prêts à sacrifier leur âme. "
        "Certains prétendent qu'elle juge l'ambition... d'autres y voient un défi divin. Mais au sommet, c'est la légende : une récompense inimaginable. "
        "Combien sont morts pour la voir de leurs propres yeux ? Et combien y parviendront réellement ?[/italic]"
    )
    
    console.print(
        "[italic]La nuit tombe lentement sur l’horizon, déchirée par des teintes de pourpre et de bleu. Une brume épaisse danse au pied de la tour, "
        "comme si la terre elle-même cherchait à cacher ce monstre de pierre. L’air est dense, presque suffocant… "
        "Chaque pas résonne comme si la Tour respirait, comme si elle se nourrissait de la présence de ceux qui osaient s'en approcher.[/italic]\n"
    )
    
    console.print(
        "[bold]Devant toi, elle se dresse, silhouette d'obsidienne luisante, projetant son ombre jusqu'aux étoiles. "
        "Chaque pierre semble polie par des siècles de tempêtes et de sang versé. Pourtant, malgré cette noirceur, elle attire inexorablement. "
        "Elle n'est pas seulement une tour... c'est une promesse. Un piège. Et elle appelle ceux dont le cœur est rongé par le désir.[/bold]"
    )

    console.print("Aldric (murmurant) : 'La voilà… comme dans mes rêves…'") 
    console.print(
        "[italic]Perché sur une colline, Aldric contemple la Tour depuis les hauteurs. Le vent balaie son manteau clair, "
        "et ses cheveux blonds tombent en mèches éparses sur son front. L'épée à sa ceinture semble légère, mais ses doigts la frôlent par réflexe.[/italic]\n"
    )
    
    # Ambiance autour de la Tour
    console.print(
        "[bold yellow]=== Autour de la Tour ===[/bold yellow]"
    )
    console.print(
        "[italic]En contrebas, une masse de silhouettes s'agite. Des dizaines de participants, guerriers, voleurs, mages, et aventuriers se tiennent "
        "devant l’entrée béante de la Tour. Des visages creusés par la fatigue, des regards pleins d'espoir… et de peur. "
        "Certains rient nerveusement, d'autres prient en silence. Des bras affûtent des lames à la lueur des torches, tandis que quelques-uns s'éloignent déjà, renonçant avant même d'avoir commencé.[/italic]"
    )
    
    console.print(
        "[italic]Dans un coin, un vieil homme vêtu d'une cape poussiéreuse murmure en boucle des avertissements. 'La Tour dévore tout… Le sommet ? "
        "Un mensonge. Personne ne revient jamais…' Mais peu lui prêtent attention. Ils sont là pour une raison. Ils ont des comptes à régler.[/italic]"
    )
    
    # Interactions avec d'autres personnages
    console.print("??? (une voix rauque s’élève derrière Aldric) : 'C’est la première fois que tu viens ici ?'")
    console.print("Aldric (se retournant légèrement) : 'Oui. C’est aussi impressionnant que dans les récits…'")
    console.print(
        "[italic]La voix appartient à un homme massif, vêtu d’une armure cabossée. Son visage est marqué par d’anciennes cicatrices, "
        "et ses yeux sont d’un gris pâle, presque fantomatique.[/italic]"
    )
    console.print("L’homme (hochant la tête) : 'Impressionnant, hein… ? Jusqu’à ce que tu sois là-dedans. Garde ton épée prête, gamin. Certains ici n’attendront pas que la Tour vous tue.'")
    console.print(
        "[italic]Devant toi, des dizaines de participants forment des groupes dispersés, certains adossés aux parois rocheuses, d'autres concentrés "
        "dans des cercles discrets. Quelques torches éclairent faiblement les visages tendus et les reflets métalliques des lames. "
        "Aldric porte une tenue simple : un pantalon de combat gris, un maillot sans manches noir et un manteau marron clair. Son épée courte est à portée de main du jeune homme blond.[/italic]\n"
    )

    # Interaction avec Garen
    garen = Character("Garen", "Un jeune homme sincère mais maladroit.", "garçon", "allié")
    hero.add_relation(garen, "Neutre")
   
    
    console.print(
    "Garen : 'Salut… Euh… toi aussi, tu participes ? Haha, évidemment, sinon tu ne serais pas là, hein ?'\n"
    "[italic]La voix semble amicale mais vacille légèrement, signe d’un mélange de nervosité et d’excitation contenue.[/italic]\n"
    "Garen : 'Moi, c'est Garen. Je pensais qu'il serait peut-être utile d'avoir un allié ? "
    "Juste pour commencer, hein ? Héhé, on ne sait jamais... Cette tour... apparemment, c'est difficile, mais j'aimerais aller le plus loin possible.' "
    "[italic]Son sac en bandoulière semble lourd, rempli d’armes trop neuves, et son armure brille encore sous la lueur des torches.[/italic]"
)
    console.print(
    "[italic]Derrière Garen, quelques participants observent la scène avec curiosité. Certains échangent des murmures. "
    "Un homme encapuchonné ricane doucement, comme s'il devinait déjà le destin du jeune guerrier inexpérimenté.[/italic]"
    )
    console.print(
    "[bold]Aldric[/bold] : [italic]'Je ne savais pas que les fermiers souhaitrait participer à la tour...'[/italic] "
    "[italic](Vous croisez les bras, jaugeant rapidement Garen de la tête aux pieds.)[/italic]"
    )
    console.print(
    "Garen (rougissant légèrement) : 'Je... Je ne suis pas un fermier ! enfin certes peut-etre un peu...j'ai bouffé toutes mes economies pour m'équiper. C'est tout.'"
    )
    console.print(
    "Aldric (calme) : 'Oh, vraiment ? Et tu comptes survivre combien de temps dans cette Tour avec des bottes trop grandes et une épée que tu ne sais pas tenir ?'"
    )
    console.print(
    "Garen (gêné) : 'Tout le monde commence quelque part, non ? Je me débrouillerai ! Je suis peut-être pas aussi expérimenté que toi, mais… j’ai ma place ici. puis on pourrait faire equipe...non ?'"
    )


# Ajout d'un échange supplémentaire
    console.print(
        "[italic]Garen baisse brièvement les yeux, visiblement mal à l'aise.[/italic]\n"
        "Garen : 'On dit que les premiers étages sont mortels… mais je suppose que tu le sais déjà.'\n"
        "Aldric : [italic]'Il paraît... mais personnellement, ça ne me fait ni chaud ni froid.'[/italic]\n"
        "[italic]Vos doigts se resserrent sur le manche de votre épée courte, et vous levez les yeux vers la Tour imposante.[/italic]\n"
    )     
    console.print(
        "Garen : 'Cette épée... elle ne vient pas d'ici, n'est-ce pas ? Je... je n'en ai jamais vu des comme ça.'\n"
        "Aldric (sourcils froncés) : 'Ne la touche pas.'\n"
        "Garen (levant les mains en signe d'excuse) : 'Je sais, pardon ahah... Je pose trop de questions.'\n"
        "Garen (murmure) : 'Tu as l'air de savoir ce que tu fais… contrairement à moi.'"
    )

    console.print(
        "Aldric (observant Garen du coin de l'œil) : 'Ton épée est neuve et ton armure mal ajustée... Tu es soit un fils de noble, "
        "soit tu as dépensé toutes les économies de ta famille pour t'équiper. Dans tous les cas, tu risques de le regretter, l'ami.'\n"
    )
    console.print(
        "Garen (riant nerveusement) : 'Comment tu... Ça se voit tant que ça ?'\n"
        "Aldric (détaché) : 'Un peu.'"
    )

    garen_dialogue = Dialogue(
    "Que répondez-vous à Garen ?",
    [
        {
            "text": "Garen, hein ? Hm… On verra. Ça pourrait marcher. Pour combien de temps ça…  (+10 Amical)",
            "consequence": lambda h: [
                hero.get_relation("Garen").adjust_score(10),
                console.print("Garen [bold green]esquisse un sourire sincère[/bold green], visiblement soulagé."),
                console.print("Garen (souriant) : 'Tu verras, je suis pas si inutile que ça !'"),
                console.print("Aldric (calme) : 'Hm. Espérons que tu dises vrai.'"),
                console.print("Kael (à voix basse) : 'J'espère qu'il tiendra plus de deux étages.'")
            ]
        },
        {
            "text": "Si tu me ralentis, je te laisse derrière. Compris ?  (+5 Pragmatique)",
            "consequence": lambda h: [
                hero.get_relation("Garen").adjust_score(5),
                console.print("Garen [bold yellow]hoche la tête avec résolution. Il vous suit tout en regardant la Tour qui surplombe toutes ces jeunes âmes.[/bold yellow]"),
                console.print("Garen (gêné) : 'Je ferai de mon mieux…'"),
                console.print("Aldric (froidement) : 'Pas de place pour l'erreur.'"),
                console.print("Kael (ricanant) : 'Tiens donc, un cœur de pierre.'")
            ]
        },
        {
            "text": "Ignorer Garen. (-5 Distant)",
            "consequence": lambda h: [
                hero.get_relation("Garen").adjust_score(-5),
                console.print("Garen (tristement) : 'Ah… je comprends…'"),
                console.print("Kael (amusé) : 'Eh bien, tu n'auras pas de fan club ce soir.'"),
                console.print("Aldric : 'C'est pas un jeu d'enfant. Tâche de t'y faire.'")
            ]
        }
    ],
    character=garen
)
    garen_dialogue.display(hero)
    
    console.print(
            "[italic]Garen baisse brièvement les yeux, visiblement mal à l'aise.[/italic]\n"
            "Garen : 'On dit que les premiers étages sont mortels… mais je suppose que tu le sais déjà.'\n"
            "Aldric : 'Il paraît... mais personnellement je m'en fiche,' dites-vous tout en tenant le manche de votre épée courte...\n"
            "Garen : 'Cette épée... elle ne vient pas d'ici, n'est-ce pas... Je... je n'en ai jamais vu des comme ça...'\n"
            "Aldric : Vous regardez Garen du coin de l'œil...\n"
            "Garen : 'Je sais, pardon ahah... je pose trop de questions. Je suis juste un peu tendu... contrairement à toi qui as l'air de savoir quoi faire...'\n"
            "Aldric : 'Ton épée est neuve et ton armure mal ajustée... Tu es soit un fils de noble, soit tu as dépensé toutes les économies de ta famille pour t'équiper et venir ici... Dans tous les cas, tu risques de le regretter, l'ami.'\n"
            "Garen : 'Comment tu... ça se voit tant que ça ?'\n"
            "Aldric : 'Hm...'\n"
        )

    # Interaction avec Kael
    kael = Character("Kael", "Un homme élégant et provocant.", "garçon", "rival")
    hero.add_relation(kael, "Neutre")

    console.print("\n[bold blue]Le vent se lève alors qu'Aldric poursuit son chemin vers la Tour. "
              "Garen marche maladroitement derrière, peinant à suivre. Autour de vous, des participants silencieux "
              "échangent des regards méfiants.[/bold blue]")

    console.print("\n[bold red]Plus loin, adossé à un rocher imposant, un jeune homme observe la scène avec amusement. "
              "Son allure raffinée contraste avec l'ambiance oppressante. Il porte une rapière, une chemise blanche de noble, "
              "et ses cheveux blancs sont soigneusement coiffés vers l'arrière.[/bold red]")

    console.print(
        "Kael : 'Eh bien, voilà un spectacle intéressant... Un mercenaire accompagné d'un fermier. "
        "Dites-moi, vous espérez vraiment survivre au-delà du premier étage ?'\n"
        "Kael : 'Essaie au moins de ne pas salir ce sol avec ton sang. Ce serait dommage de tacher ma future victoire.'"
)

# Dialogue interactif avec Kael
    kael_dialogue = Dialogue(
    "Quelle réponse faites-vous à Kael ?",
    [
        {
            "text": "« Et toi ? Tu comptes fanfaronner jusqu'à l'entrée ? » (+5 Antagonique)",
            "consequence": lambda h: [
                hero.get_relation("Kael").adjust_score(+5),
                console.print("Kael (rire moqueur) : 'Hah ! Intéressant… Je vais apprécier cette ascension, je le sens.'"),
                console.print("Aldric : 'Ne t'attends pas à ce que je te sauve si tu tombes.'"),
                console.print("Kael : 'Oh, je n'ai jamais eu besoin d'aide... et surtout pas de toi.'")
            ]
        },
        {
            "text": "« Tu parles beaucoup pour quelqu'un qui n'a pas encore posé un pied dans la Tour. » (-10 Provocateur)",
            "consequence": lambda h: [
                hero.get_relation("Kael").adjust_score(-10),
                console.print("Kael (perd brièvement son sourire) : 'Ah… Un chien qui aboie. Espérons que tu mordes aussi fort.'"),
                console.print("Kael (s'éloigne légèrement) : 'On verra qui de nous deux atteindra le sommet.'")
            ]
        },
        {
            "text": "Ignorer Kael et passer votre chemin. (-15 Indifférent)",
            "consequence": lambda h: [
                hero.get_relation("Kael").adjust_score(-15),
                console.print("Kael (hausse les épaules) : 'Trop lâche pour répondre ? Peu importe, tu finiras comme les autres.'"),
                console.print("Garen (regardant Kael d'un air irrité) : 'Quel sale type…'"),
                console.print("Aldric (froidement) : 'Ignore-le. Il ne vaut pas notre énergie.'")
            ]
        }
    ],
    character=kael
    )   
    kael_dialogue.display(hero)

# Scène de clôture après la rencontre
    console.print(
        "\n[italic]Kael s'éloigne lentement vers l'entrée de la Tour, laissant derrière lui un léger ricanement. "
        "Garen secoue la tête, visiblement frustré.[/italic]"
    )
    console.print("Garen (marmonnant) : 'On dirait qu'il adore se faire des ennemis.'")
    console.print("Aldric (calme) : 'Ce genre de personne est souvent la première à tomber… ou la dernière à rester debout.'")

    # Interaction avec l'observateur
    observer = Character("Homme mystérieux", "Un homme en cape sombre et silencieux.", "inconnu")
    hero.add_relation(observer, "Neutre")

    console.print("[bold blue]La pluie commence à tomber alors qu'Aldric et Garen s'avancent vers la Tour. "
              "Les braseros alignés de part et d'autre de l'escalier s'embrasent lentement, illuminant les visages "
              "des participants à travers les gouttes d'eau.[/bold blue]")

    console.print("\n[bold magenta]Non loin de l'entrée, une silhouette encapuchonnée se tient immobile, adossée à la paroi. "
              "Ses yeux, dissimulés sous l'ombre de sa capuche, vous suivent silencieusement.[/bold magenta]")

    console.print(
    "Homme mystérieux (calme) : '[italic]Tu va donc tenter la tour alors...hmpf[/italic]'"
)

# Dialogue interactif avec l'observateur
    observer_dialogue = Dialogue(
    "Comment réagissez-vous face à cet homme mystérieux ?",
    [
        {
            "text": "Hocher la tête respectueusement. (+10 Respectueux)",
            "consequence": lambda h: [
                hero.get_relation("Homme mystérieux").adjust_score(10),
                console.print("Aldric (calmement) : 'On se connait ?'"),
                console.print("Homme mystérieux (hochant légèrement la tête) : '[italic]Hm..[/italic]'")
            ]
        },
        {
            "text": "Rester silencieux et attendre. (Neutre)",
            "consequence": lambda h: [
                console.print("Aldric (gardant son calme) : 'Vous restez immobile, observant l'homme sans répondre.'"),
                console.print("Homme mystérieux (sourire en coin) : '[italic]Je vois. Tu veux la jouer comme ca...interessant ![/italic]'")
            ]
        },
        {
            "text": "Lui répondre avec défiance. (-15 Provocateur)",
            "consequence": lambda h: [
                hero.get_relation("Homme mystérieux").adjust_score(-15),
                console.print("Aldric (fronçant les sourcils) : 'Ca te pose un problème qu'est ce que ca peut te faire ?'"),
                console.print("Homme mystérieux (sombre) : '[italic]La curiosité excessive peut coûter cher dans cette tour…tu le sais deja..[/italic]'"),
                console.print("Garen (inquiet) : 'Laissons-le tranquille.'")
            ]
        }
    ],
    character=observer
)
    observer_dialogue.display(hero)

# Scène de clôture après la rencontre
    console.print(
    "\n[italic]L'homme mystérieux disparaît lentement dans l'ombre de la Tour, laissant derrière lui une atmosphère pesante. "
    "Garen jette un regard nerveux dans sa direction, avant de détourner les yeux.[/italic]"
)
    console.print("Garen (chuchotant) : 'Ce type… il dégage quelque chose de bizarre. Tu crois qu'il va participer ?'")
    console.print("Aldric (sombre) : 'Il n'est pas comme les autres… Il observe.'")
    console.print("Garen (tremblant) : 'C'est qui alors ?'")
    
    console.print("Homme mystérieux : 'Je suis sur que nous nous reverrons Aldric...'")
    console.print("Aldric : 'Hm... ? On sais deja vu ?? (dites vous d'un air mefiant)'")
    console.print("L'homme mysterieux disparu sans un mot dans l'obscurité qui commencé a tomber")
    console.print("Garen : 'Tu...tu t'appelle Aldric ? '")
    console.print("Aldric :' Oui mais ca n'a pas d'importance...en route'")
    console.print("Garen : 'Euh d'accord...je ne voulait pas etre intrusif...'")

    # Clôture de l'introduction
    console.print(
        "[bold cyan]L'entrée béante de la tour se dresse devant toi, avalant la lumière du jour. "
        "Tu franchis lentement le seuil, laissant derrière toi les murmures et la brume du monde extérieur. "
        "L'ascension commence...[/bold cyan]\n"
        "[bold cyan]Aldric : 'La tour...te voila...quoi qu'il en soit je ne reculerais pas...tu ne m'impressione pas...pas cette fois...plus jamais..."
        "Garen : Pas cette fois ? tu veux dire que.."
        "Aldric continua a gravir les marches sans preter attention a ce que dit Garen.."
        "Garen vous suit, la gorge nouée... Kael est déjà entré, et l'homme mystérieux a disparu. "
        "La terrible ascension peut enfin commencer.[/bold cyan]"
    )
    game_menu = GameMenu(hero)
    game_menu.display()
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Chapitre 1 : la porte de la discorde

def floor1(hero, game_menu):
    from rich.console import Console
    console = Console()
    
    console.print("\n[bold cyan]=== Étage 1 : La Porte de la Discorde ===[/bold cyan]")
    console.print(
        "[italic]La lourde porte de pierre se referme derrière vous dans un grondement sourd. L’intérieur de la tour est sombre, "
        "éclairé seulement par quelques torches vacillantes. L’air est froid, chargé de l’odeur de pierre humide.[/italic]\n"
    )
    
    console.print(
        "[italic]Un silence pesant s’installe, comme si la tour elle-même retenait son souffle. "
        "Les bruits de pas résonnent à chaque mouvement, amplifiés par l’architecture de la salle. "
        "Chaque écho semble étirer l’espace, donnant l’impression que les murs vous observent en silence.[/italic]\n"
    )
    
    console.print(
        "[italic]Un vaste hall circulaire s’étend devant vous, orné de statues de guerriers alignées le long des murs. "
        "Leur regard semble peser sur chaque nouvel arrivant. Garen reste proche de vous, tandis que Kael s’avance légèrement en tête.[/italic]"
    )
    
    console.print(
        "[bold yellow]Une immense porte de fer se dresse au fond du hall. Une grille d’acier noirci la barre. Devant elle, "
        "une inscription brille faiblement à la lumière des torches :[/bold yellow]\n"
        "[italic]« Seuls ceux qui abandonnent peuvent passer. Mais que perdez-vous vraiment ? »[/italic]"
    )
    
    console.print(
        "[italic]L’inscription semble danser sous l’effet de la flamme vacillante des torches. L’air devient plus dense, comme si la pièce attendait votre décision. "
        "Au loin, un léger craquement se fait entendre, mais rien ne semble bouger. Pourtant, cette salle dégage une énergie sourde… presque vivante.[/italic]"
    )

    # Dialogue
    console.print("\nKael : 'Hah. Quelle plaisanterie. Il suffit d’abandonner pour avancer ? Je pensais que cette tour serait plus créative.'")
    console.print(
        "[italic]Kael croise les bras, jetant un regard dédaigneux à l’inscription. Malgré ses mots, son regard s’attarde un instant de trop sur les statues, "
        "comme s’il s’attendait à ce qu’elles bougent.[/italic]"
    )
    
    console.print("Garen : 'Abandonner… ça veut dire qu’on doit sacrifier quelque chose ?'")
    console.print(
        "[italic]Garen fronce les sourcils, cherchant un sens plus profond dans ces quelques mots. Ses doigts tapotent nerveusement la poignée de son épée. "
        "Il n’aime pas ce qu’il ressent ici, et ça se voit.[/italic]"
    )
    
    console.print("Aldric : 'Il y a forcément un piège. Rien n’est gratuit ici.'")
    console.print(
        "[italic]Votre propre voix résonne dans l’obscurité. En avançant d’un pas, vous sentez la présence des statues peser davantage. "
        "Elles semblent vous scruter, jaugeant chaque mot, chaque hésitation.[/italic]"
    )
    
    console.print(
        "[italic]Un courant d’air glacial traverse la salle. La lumière des torches vacille légèrement, projetant des ombres tremblantes sur le sol de pierre. "
        "L’instant est suspendu, comme si quelque chose attendait de voir si vous oserez défier la tour ou courber l’échine.[/italic]"
    )
    actions = [
        "Inspecter la porte de plus près.",
        "Examiner les statues alignées sur les murs.",
        "Observer la réaction des autres participants.",
        "Tenter de forcer la porte avec ton épée."
    ]
    
    while True:
        console.print("\n[bold]Que décides-tu de faire ?[/bold]")
        for i, action in enumerate(actions):
            console.print(f"{i + 1}. {action}")
        
        choix = input("\nVotre choix : ")
        
        if choix == "1":
            console.print(
            "\n[italic]En t’approchant de la porte, tu remarques des gravures représentant des silhouettes agenouillées, "
            "déposant des objets devant une entité obscure.[/italic]"
        )
            console.print("Aldric : 'Intéressant. Ce n’est pas un simple abandon matériel. C’est… plus profond.'")
            console.print("Kael : 'Oh tu te met a la philosophie maintenant ?'")
            console.print("Aldric : 'Tu devrais essayer ca te ferai pas de mal..'")
            console.print("Kael : 'Ahah bien repondu ! (Kael +5)'")
            hero.get_relation("Kael").adjust_score(+5)
            break  
        
        elif choix == "2":
            console.print(
            "\n[italic]Les statues semblent représenter d’anciens guerriers. Certaines ont des fissures profondes au niveau de leur cœur "
            "ou de leurs mains. Sur l’une d’elles, il manque une arme.[/italic]"
        )
            console.print("Aldric : 'Ces statues… Ce ne sont peut-être pas que des œuvres d’art.'")
            console.print("Garen : 'Tu crois qu’ils étaient… comme nous ?'")
            console.print("Aldric : 'Je ne sais pas...ma théorie serait que c'est les anciens héros de la tour ou bien...les fondateurs !'")
            console.print("Garen : 'Oooh mais oui ! ca serai sensé..(Garen +5)'")
            hero.get_relation("Garen").adjust_score(+5)
            break  # Sort de la boucle après ce choix
        
        elif choix == "3":
            console.print(
            "\n[italic]Certains participants chuchotent entre eux. L’un d’eux dépose son épée devant la porte… sans succès.[/italic]"
        )
            console.print("Kael : 'Pfff. La moitié va rester bloquée ici à essayer de comprendre.'")
            console.print("Garen : 'Au lieu de te plaindre tu ferai mieux de nous aider...mais tu est trop noble pour ca hein ?'")
            console.print("Kael : 'Un problème paysan ? avec ton equipement d'occasion et de seconde main...le marchand a du faire une bonne affaire..'  ")
            console.print("Garen : 'Tu aime ca hein ? Rabaissé les plus demunis...vous me degouter vous les nobles...'")
            console.print("Aldric : 'Ca suffit tout les deux...par pitié...concentrons nous ca n'a n'en pas l'air mais c'est bel et bien une epreuve.'")
            break  # Sort de la boucle après ce choix
    
        elif choix == "4":
            console.print(
            "\n[italic]Tu dégaines ton épée et frappes la grille, mais une lumière repousse la lame.[/italic]"
        )
            console.print("Kael (ricanant) : 'C’était… spectaculaire. Bravo.'(+5 Impétueux)")
            hero.get_relation("Kael").adjust_score(+5)
            actions.remove("Tenter de forcer la porte avec ton épée.")
            continue  # Reste dans la boucle pour faire d'autres choix après ce choix
    
        else: 
            console.print("[bold red]Choix invalide. Veuillez réessayer.[/bold red]")
            continue
    
    console.print(
        "\nAprès plusieurs minutes, un participant s’agenouille devant la porte, une main sur son cœur. La grille se lève lentement.\n"
    )
    console.print("Kael : 'Hm. Alors c’est ça… s’abandonner soi-même.'")
    console.print("Garen : 'On… on fait quoi ?, je pense qu'on devrait s'agenouiller...c'est...c'est une epreuve d'humilité !!'")

    console.print("\n[bold]Que fais-tu ?[/bold]")
    console.print("1. S’agenouiller et traverser la porte.")
    console.print("2. Observer et attendre.")
    
    final_choice = input("\nVotre choix : ")
    
    if final_choice == "1":
        console.print("\n[italic]Tu t’agenouilles devant la porte. Une chaleur étrange envahit ton corps. La grille s'ouvre lentement.[/italic](Garen +5 a suivi son conseil)")
        hero.get_relation("Garen").adjust_score(+5)
    
    elif final_choice == "2":
        console.print("\n[italic]Tu observes les autres participants. Kael traverse après hésitation, Garen te suit de loin.[/italic]")
        
    else:
        console.print("[bold red]Choix invalide. Vous attendez.[/bold red]")
        
    console.print(
        "\n[bold cyan]Après avoir franchi la porte, vous montez les escaliers menant à l’étage suivant. "
        "Derrière vous, la porte se referme lourdement.[/bold cyan]"
    )
    console.print(
        "[italic]La lumière des torches s’amenuise. Les ombres dansantes sur les murs vous tiennent compagnie tandis que le groupe de participants s’étire. "
        "Certains gravissent les marches rapidement, d’autres hésitent après l’épreuve.[/italic]"
    )
    
    console.print("Kael (marchant devant, jetant un regard par-dessus son épaule) :\n"
                 "« Hah… Je me demande combien sont restés bloqués là-bas. J’espère pour eux que l’épreuve suivante ne sera pas trop difficile… »")
    
    console.print("Garen (haletant légèrement) :\n« Tu parles comme si c’était une promenade… J’ai cru que cette porte ne s’ouvrirait jamais… »")
    
    console.print("Aldric (calme) :\n« Si ce genre de test te fait peur, tu n’iras pas loin. C’était juste une mise en bouche. »")
    
    console.print("\nPlus loin dans l'étage 1 un groupe regaderent Aldric et les autres poursuivre leur chemin")
    
    console.print(
        "\n[italic]Clotaire était un homme élancé à l’allure noble malgré ses vêtements usés. "
        "Sa veste en cuir noir était ornée de plusieurs boucles argentées et un foulard bordeaux enroulait négligemment son cou. "
        "Ses cheveux noirs tombaient jusqu'à ses épaules, encadrant un visage affûté et un regard perçant qui trahissait une intelligence calculatrice. "
        "Une épée fine et bien entretenue pendait à sa taille, signe qu’il ne comptait pas se reposer uniquement sur des manipulations.[/italic]"
    )

    console.print(
        "\n[italic]Emphyr, la seule femme du groupe, contrastait avec les autres par sa prestance calme mais autoritaire et aussi par sa beauté. "
        "De longs cheveux mauve clair descendaient jusqu’au milieu de son dos, flottant avec des decorations dedans"
        "Elle portait une cape légère par-dessus une tunique bleue sombre et un pantalon de cuir ajusté, laissant transparaître "
        "son aisance au combat. Une dague pendait à sa ceinture, et son sourire en coin témoignait d’un esprit vif et confiant.[/italic]"
    )

    console.print(
        "\n[italic]Velm, quant à lui, était plus petit que ses camarades mais dégageait une énergie débordante. "
        "Son regard malicieux et ses mouvements rapides faisaient de lui un opportuniste né. "
        "Il portait une veste rouge écarlate qui jurait avec l’austérité des autres, et ses bottes crissantes trahissaient son goût "
        "pour le spectacle. Un rouquin aux cheveux courts, souvent en bataille, avec une cicatrice discrète sur la joue gauche. "
        "Deux dagues croisées pendaient dans son dos, prêtes à l’usage.[/italic]"
    )

    console.print(
        "\n[italic]Brandio, en revanche, était le colosse du groupe. Plus grand d’une tête que Clotaire, il portait une armure partielle "
        "renforcée de cuir épais, marquée par les combats. Sa carrure imposante rendait inutile toute tentative de discrétion. "
        "il la le crane rasé et son expression taciturne faisaient de lui l’antithèse de Velm. "
        "Il ne parlait que rarement, mais lorsque sa voix grave résonnait, personne ne remettait en question ses paroles. "
        "Il se battait avec poings de fer ![/italic]"
    )
    
    console.print("\nClotaire : 'Bien joué Emphyr...t'agenouiller était donc la clef...tu est si maligne'")
    console.print("Emphyr : Oh je t'en prie c'est parce que Velm l'a dit en plaisantant ")
    console.print("Velm : Ahah je suis pas si bête hein ?")
    console.print("Brandio : Si tu est bête on appele cela la chance imbécile...")
    console.print("Emphyr : C'est bon les gars vous m'avez épuisée moi j'avance...")
    console.print("Clotaire : Vous avez entendu la demoiselle ? On avance !")
    console.print("Velm et Brandio : Oui boss !!!")
    

    game_menu.display()  
 
  
 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 # chapitre 2 :   
 
def floor2(hero, game_menu):
    from rich.console import Console
    console = Console()
    
    clotaire = Character(
        "Clotaire", "Un combattant expérimenté, au regard fourbe et pret a tout pour reussir.", "garçon", "antagoniste"
    )
    velm = Character(
        "Velm", "Un jeune homme rusé et discret, à l'aura mystérieuse.", "garçon", "antagoniste"
    )
    brandio = Character(
        "Brandio", "Un colosse loyal et protecteur, peu bavard.", "garçon", "antagoniste"
    )
    emphyr = Character(
        "Emphyr", "Une espionne seduisante et féline", "fille", "neutre"
    )

    if not hero.get_relation("Clotaire"):
        hero.add_relation(clotaire, "Neutre")
    if not hero.get_relation("Velm"):
        hero.add_relation(velm, "Neutre")
    if not hero.get_relation("Brandio"):
        hero.add_relation(brandio, "Neutre")
    if not hero.get_relation("Emphyr"):
        hero.add_relation(emphyr, "Neutre")

    console.print("\n[bold cyan]=== Étage 2 : La Salle du Gardien Miroir ===[/bold cyan]")
    console.print(
        "[italic]L'escalier s'étire interminablement, chaque pas résonnant lourdement contre la pierre froide. "
        "L'air devient plus lourd à mesure que vous grimpez, comme si l'étage suivant vous oppressait déjà de sa simple présence. "
        "Chaque respiration semble gagner en densité, et même Garen, pourtant d’ordinaire bavard, se contente de serrer la poignée de son arme. "
        "Un courant d'air glacé descend de l'étage supérieur, comme pour vous prévenir de ce qui vous attend.[/italic]\n"
    )

    console.print(
        "[italic]Finalement, la volée de marches s'ouvre sur une salle circulaire immense. Des torches fixées aux murs diffusent une lumière bleutée étrange, "
        "projetant des ombres mouvantes. Le silence est pesant, comme si cet endroit était figé dans une attente interminable.[/italic]"
    )

    console.print(
        "[bold yellow]Un chevalier d'une taille inhumaine – plus de trois mètres de haut – se tient immobile, tel une sculpture d'acier. "
        "Sa silhouette massive domine la salle entière, et chaque reflet de sa lourde armure semble danser sous la lumière des torches. "
        "Mais c'est son bouclier qui capte véritablement l'attention : immense, poli comme un miroir parfait, "
        "il reflète non seulement les visages, mais aussi l'essence même de ceux qui osent s'en approcher. "
        "Lorsque vous vous en approchez, il semble que ce n'est pas seulement votre image qui apparaît… mais votre double, armé et prêt à vous défier.[/bold yellow]"
    )

    console.print(
        "Kael (bras croisés, observant l'imposant gardien) : 'C'est quoi ce truc… un colosse qui garde la porte ? "
        "On dirait que la tour commence à s'amuser. J’ai presque envie de lui demander son nom.'"
    )
    console.print(
        "Garen (visiblement tendu, regardant autour de lui) : 'Tu crois… qu'il va nous attaquer ? Je n'aime pas ce silence…'"
    )
    console.print(
        "Aldric (les yeux fixés sur le chevalier) : 'Pas besoin de croire. Il est là pour ça.'"
    )

    console.print(
        "[italic]Un grincement métallique brise soudain le silence, résonnant à travers toute la salle comme une alarme funeste. "
        "Le chevalier à genoux prend lentement vie, ses plaques d’armure raclant contre la pierre. Il se lève dans un mouvement lent mais précis, "
        "brandissant son gigantesque bouclier. Sur sa surface, des formes fantomatiques émergent, "
        "chaque silhouette prenant progressivement forme pour devenir des doubles parfaits des participants.[/italic]"
    )

    console.print(
        "Kael (plissant les yeux) : '…Génial. Des copies conformes. Et je parie qu'ils frappent aussi fort que nous.'"
    )
    console.print(
        "Garen (prenant une posture défensive) : 'Tu crois qu’on peut les battre ?' "
        "Son regard ne quitte pas son reflet dans le bouclier. Son double, de l'autre côté, le fixe en retour, impassible."
    )
    
    console.print(
        "Aldric (s'approchant légèrement) : 'Ils ne sont pas invincibles… mais on ne sortira pas indemnes.'"
    )

    console.print(
        "[italic]Alors que le chevalier avance de quelques pas, les doubles bondissent en avant, fondant sur les participants. "
        "Les premières lames s'entrechoquent dans une cacophonie d'acier et de cris. "
        "Certains attaquent directement le colosse, mais leurs coups rebondissent sans laisser la moindre égratignure.[/italic]"
    )

    console.print(
        "Kael (frappant du pied avec frustration) : 'Rien ne passe ! Qu'est-ce que c'est que ce foutu truc ?!'"
    )
    console.print(
        "Garen (haletant, après avoir paré une attaque) : 'On va se faire massacrer si on continue comme ça…' "
        "Son souffle est court, et chaque coup semble peser davantage sur lui."
    )

    console.print(
        "[italic]Les doubles se multiplient, encerclant les participants. "
        "Aldric se tient dos à dos avec Kael et Garen, leurs armes levées. Autour d'eux, les cris de ceux qui tombent sous les lames des reflets "
        "se mêlent aux bruits sourds des coups portés sur l’armure du chevalier. Il semble inébranlable, "
        "et ses doubles se battent avec une coordination parfaite, comme un funeste ballet orchestré dans l'ombre.[/italic]"
    )
    console.print(
    "[italic]Un silence pesant s'installe pendant une fraction de seconde, seulement brisé par le bruit métallique des doubles qui avancent. "
    "Soudain, une flèche fend l'air avec une précision chirurgicale, transperçant l'un des reflets qui s'effondre dans un éclat d'énergie vaporeuse.[/italic]"
    )
    console.print(
    "[italic]Vous suivez la trajectoire de la flèche et apercevez une femme blonde perchée sur une colonne brisée, son arc toujours tendu. "
    "Elle scrute le terrain de bataille avec calme, détachée du chaos environnant.[/italic]"
    )
    console.print(
    "Ayela (calme, abaissant légèrement son arc) : 'Si vous continuez à frapper comme des brutes, vous allez tous mourir.'"
    "\nAyela (esquissant un léger sourire, assurée) : 'Je suis Ayela, mais on fera les présentations plus tard. On a plus urgent.'"
    "\n[italic]Ayela était une jeune archère à la silhouette athlétique et élancée, sa peau claire parsemée de taches de rousseur discrètes. "
    "Ses cheveux mi long noir attaché avec une barrette, "
    "Son regard perçant, d’un bleu clair presque glacial, trahissait une vigilance constante et une détermination farouche. malgré une certaine naiveté "
    "Elle portait une brassière de cuir vert foncé renforcée de coutures épaisses, épousant son buste avec souplesse, "
    "ainsi qu’un short moulant noir qui laissait entrevoir des jambes puissantes et entraînées. "
    "Des bottes de chasse hautes et des gants blancs usés complétaient sa tenue, "
    "contrastant avec le carquois en bandoulière accroché à sa hanche. "
    "L’arc qu’elle tenait était finement sculpté, décoré de motifs elfiques, trahissant une certaine élégance malgré sa robustesse. "
    "Chaque mouvement d'Ayela semblait mesuré, précis, comme si elle dansait avec le danger, prête à décocher une flèche à la moindre menace.[/italic]"
)   
    
    console.print(
    "[italic]Sa voix, bien que posée, résonne comme une mise en garde glaciale. "
    "Derrière son air serein, vous devinez une combattante habituée à survivre dans des situations désespérées.[/italic]"
    )
    console.print(
    "Kael (esquissant un sourire tout en esquivant une attaque) : 'Hah… Voilà qui devient intéressant. J’aime quand quelqu’un d’autre fait le sale boulot.'"
    )
    console.print(
    "Garen (haletant, relevant son bouclier) : 'Elle a réussi à en abattre un… Mais comment ?!'"
    )
    console.print(
    "Ayela (préparant une autre flèche) : 'Vous vous obstinez à frapper l’armure. Visez les reflets dans le bouclier… C’est là qu’ils naissent.'"
    )
    console.print(
    "[italic]À ces mots, une nouvelle salve part et frappe un autre double en plein cœur, le réduisant en cendres. "
    "Kael échange un regard rapide avec Aldric, hochant la tête avec un rictus satisfait.[/italic]"
    )
    console.print(
    "Kael : 'Eh bien, au moins l’un de nous réfléchit. C’est bon à savoir. Je commençais à désespérer de notre équipe.'"
    )
    console.print(
    "Aldric : 'Tu devrais plutôt te concentrer, Kael… ou tu risques d’être le prochain reflet.'"
    )
    console.print(
    "Ayela (tirant une flèche supplémentaire sans même détourner le regard) : 'Il pourrait s’avérer utile… s’il survit assez longtemps.'"
    )
    console.print(
    "[italic]Kael éclate de rire, mais il s’interrompt immédiatement en esquivant de justesse une attaque venant d’un double. "
    "L’expression moqueuse laisse place à une grimace déterminée. Le combat ne fait que commencer, et la salle semble vibrer sous l’intensité des affrontements.[/italic]"
)

    ayela = Character("Ayela", "Une archère blonde espiègle et maligne.", "fille", "alliée")
    hero.add_relation(ayela, "Neutre")
    
    console.print("\nAlya (s'approchant) : 'Écoutez. Son point faible, c'est lui-même. Il faut lui renvoyer un coup en utilisant ses doubles. J'ai... juste besoin d'un angle... j'ai besoin de vous hihi,' [italic]dit-elle avec un sourire charmeur et gêné[/italic]. "
                  "'Je peux envoyer une flèche enchantée, mais vous devrez me couvrir et trouver le bon angle.'")

    actions = [
        "Aider Ayela à viser.",
        "Tenter une attaque frontale avec Kael.",
        "Protéger Garen et les autres participants."
    ]
    
    while True:
        console.print("\n[bold]Que faites-vous ?[/bold]")
        for i, action in enumerate(actions):
            console.print(f"{i + 1}. {action}")
            
        choix = input("\nVotre choix : ")
        
        if choix == "1":
            console.print(
                "\n[italic]Vous vous placez aux côtés d'Ayela, vos yeux suivant la trajectoire des créatures à travers la salle. "
                "D'un geste rapide, vous pointez une faille dans l'illusion du bouclier.[/italic]"
            )
            console.print("Aldric (calme) : 'Là. Tire juste à cet angle.'")
            console.print(
                "[italic]Ayela hoche la tête, retenant son souffle alors que la corde de son arc se tend avec un léger grincement. "
                "Sa flèche fuse comme un éclair argenté et frappe le bouclier du chevalier. Une lumière vive éclate, "
                "déchirant l’ombre et projetant une onde qui fait reculer l’adversaire.[/italic]"
            )
            console.print("Kael (visiblement impressionné) : 'Ça fonctionne ! Refais-le encore, archère !'")
            console.print(
                "Ayela (gardant son calme, mais avec un léger sourire) : 'Tant qu’ils ne touchent pas à mes flèches, ça ira.'"
            )
            console.print(
                "[italic]Kael échange un regard rapide avec Aldric, reconnaissant silencieusement l'efficacité du tir. "
                "Garen, resté en retrait, pousse un soupir de soulagement.[/italic]"
            )
            console.print("Garen (souriant nerveusement) : 'Rappelle-moi de toujours écouter l'archère.'")
            hero.get_relation("Kael").adjust_score(+5)
            hero.get_relation("Ayela").adjust_score(+5)
            break
            
        elif choix == "2":
            console.print(
                "\n[italic]Vous suivez Kael dans une attaque frontale, vos lames scintillant à la lumière bleutée des torches. "
                "Avec un cri de défi, vous vous précipitez aux côtés de Kael, tentant de percer les défenses du chevalier. "
                "Mais à peine vos coups s’abattent-ils sur l’armure que vous sentez la vibration dans votre épée. "
                "Le métal semble indestructible.[/italic]"
            )
            console.print(
                "[italic]Kael jure entre ses dents, s’élançant plus vite encore. Un double émerge du reflet du bouclier et frappe soudainement. "
                "Kael recule, mais trop tard. La lame traverse légèrement son flanc, et il s’effondre au sol dans un bruit sourd.[/italic]"
            )
            console.print("Kael (crachant du sang, mais souriant) : 'Bordel… Je crois qu’il n’aime pas qu’on joue de trop près…' (-10 Kael blessé)")
            console.print(
                "Garen (horrifié) : 'Kael ! Ça va ? Tu peux te relever ?!'"
            )
            console.print(
                "[italic]Kael esquisse un sourire en coin, tentant de se redresser malgré la douleur visible. "
                "Ayela, toujours perchée sur une colonne brisée, grimace en silence, observant la scène.[/italic]"
            )
            console.print(
                "Ayela (froide) : 'Et c’est moi qu’on traite de prudente… Évitez de mourir bêtement.'"
            )
            hero.get_relation("Kael").adjust_score(-10)
            if "Tenter une attaque frontale avec Kael." in actions:
                actions.remove("Tenter une attaque frontale avec Kael.")
            continue
        
        elif choix == "3":
            console.print(
                "\n[italic]Vous écartez Garen de justesse alors qu'un double s'élance vers lui. Ayela bande son arc rapidement, mais dans la précipitation, "
                "sa flèche dévie et vous frôle, laissant une coupure fine le long de votre bras.[/italic]"
            )
            console.print("Ayela (agacée) : 'Je vous ai dit de ne pas bouger !'")
            console.print("Aldric (grimaçant en serrant la blessure) : 'Et moi je t'ai dit de viser correctement…'")  
            console.print(
                "[italic]Garen, figé par la peur, recule lentement en tenant son épée de manière désordonnée. Les doubles se rapprochent, l'encerclant.[/italic]"
            )
            console.print(
                "Garen (haletant, tremblant) : 'Ils sont partout… Je vais crever… Je vais crever !!!' "
            )
            console.print(
                "Kael (jetant un regard agacé) : 'Si tu continues à crier comme ça, t'as raison, ils vont tous te tomber dessus… Calme-toi !'"
            )
            console.print(
                "Ayela (regard bas, un peu coupable) : 'Je… Je suis désolée… Je pensais que… Je voulais juste éviter ça.'"
            )
            console.print(
                "[italic]Des figurants s’effondrent autour de vous sous les assauts répétés des doubles. "
                "Les grognements métalliques du chevalier résonnent dans la salle, emplissant l'air d'une pression presque suffocante. "
                "Le combat semble s’éterniser, chaque seconde coûtant davantage de vies.[/italic]"
            )
            console.print(
                "Kael (serrant la garde de son épée) : 'On ne tiendra pas à ce rythme… Si t'as un plan Aldric, c’est le moment de nous éclairer.'"
            )
            console.print(
                "Aldric (fixant le chevalier) : 'Je réfléchis… Continuez à les retenir. Ayela, visez mieux cette fois.'"
            )
            console.print(
                "Ayela (détournant les yeux) : 'Je vais essayer…' "
            )

            
            hero.adjust_health(-22)
            actions.remove("Protéger Garen et les autres participants.")
            continue
        
        else:
            console.print("[bold red]Choix invalide. Réessayez.[/bold red]")
            continue
            
   # Clôture du combat
    console.print(
        "\n[italic]Finalement, le renvoi de lumière de la dernière flèche d'Ayela frappe directement le chevalier. L'armure s'effondre, "
        "et son bouclier se brise en éclats de lumière, se dissipant dans l'air comme des fragments d'étoiles mourantes.[/italic]"
    )
    console.print(
        "[bold cyan]Sur les 97 participants initiaux, seuls 72 restent debout… La tour, impitoyable, commençait déjà son tri.[/bold cyan]"
    )

    console.print(
        "Kael (essuyant sa lame) : 'Je déteste admettre ça, mais… bien joué. Tu sers à quelque chose après tout…' "
        "[italic]Son regard se détourne rapidement, comme pour masquer une pointe de respect.[/italic]"
    )
    hero.get_relation("Kael").adjust_score(+5)

    console.print(
        "Garen (s'écroulant au sol, haletant) : 'On est vivant... c'est tout ce qui compte. J'en ai eu deux ! J'en ai eu deux... je... je crois...' "
        "[italic]Un rire nerveux s'échappe alors qu'il regarde ses mains trembler.[/italic] (+10 Garen)"
    )
    hero.get_relation("Garen").adjust_score(+10)

    console.print(
        "Aldric (croisant les bras) : 'Ne crie pas victoire trop vite. Ce n'était que la porte d'entrée…' "
        "[italic]Il fixe la porte du troisième étage qui s'entrouvre lentement devant eux, laissant apparaître l'escalier sinueux.[/italic]"
    )

    console.print(
        "Kael (tape dans le dos de Garen, moqueur) : 'T’as survécu… Pour l’instant. Mais vu ton état, t’as l’air prêt à t’effondrer, paysan. "
        "T’as encore du chemin à faire avant de ressembler à un combattant…'"
    )

    console.print(
        "Garen (soufflant, mais souriant faiblement) : 'Ouais… ouais… Je vais m’améliorer, promis. Merci… à vous deux.'"
    )

    console.print(
        "Ayela (s'approche d'Aldric, un sourire en coin) : 'Tu n'es pas comme les autres. Ce regard… Je l'ai déjà vu. "
        "Tu sais ce que tu fais… Et j'aime ça. Je suis Ayela. Tu n'as pas le choix, faisons équipe.' "
        "[italic]Elle lui fait un clin d'œil avant de se placer à ses côtés.[/italic] (+5 Ayela)"
    )
    hero.get_relation("Ayela").adjust_score(+5)

    console.print(
        "Garen (timidement) : 'Je suis Garen. Enchanté, Ayela. Lui, c'est Aldric… Et le gars là-bas qui se prend pour un prince, c'est Kael.'"
    )

    console.print(
        "Kael (plissant les yeux) : 'Essaye de ne pas postillonner quand tu parles de moi, paysan. Je suis Kael. "
        "[italic]Et évite de me toucher, ça vaut mieux pour toi…[/italic]'"
    )

    console.print(
        "Ayela (ricanant) : 'Oh, toi t’es du genre « monsieur parfait ». Tu devrais redescendre un peu…'"
    )

    console.print(
        "Kael (avec fierté) : 'Ce n’est pas de l’arrogance… Juste un constat. Je suis raffiné, vous trois… disons… moins.'"
    )

    console.print(
        "Garen (boueux et fatigué) : 'Raffiné, hein ? Ça te dit de vérifier qui est le plus raffiné si je te colle dans la boue ?!'"
    )

    console.print(
        "Kael (dégaine lentement son épée, un sourire provocateur) : 'Oh ? Tu veux croiser le fer maintenant ? Fais attention, tu trembles encore.'"
    )

    console.print(
        "[italic]Alors que les deux hommes s’apprêtent à se battre, Aldric fait un pas entre eux et bloque leurs lames avec la sienne.[/italic]"
    )

    console.print(
        "Aldric (calme, mais ferme) : 'Ça suffit. Si vous voulez mourir, attendez l'étage suivant. "
        "Mais arrêtez ces gamineries. J'ai pas de temps à perdre avec ça.'"
    )

    console.print(
        "Ayela (amusée, mains sur les hanches) : 'Le beau gosse ténébreux a raison. "
        "Se battre ici ne servira à rien. Gardez votre énergie… La tour nous attend.'"
    )

    console.print(
        "[italic]Kael et Garen rangent leurs lames, mais l'animosité demeure palpable. "
        "Chacun garde une certaine distance alors que le groupe s’avance en direction de la porte suivante.[/italic]"
    )

    console.print(
        "\n[italic]Les participants se dirigent vers la prochaine épreuve, mais certains restent en arrière… "
        "Quelques-uns commencent à piller des morceaux du chevalier défait, croyant y trouver des reliques précieuses. "
        "D’autres, encore tremblants, s'assoient et réfléchissent à abandonner.[/italic]"
    )

    console.print(
        "[italic]Alors qu’Aldric, Ayela, Kael et Garen s’éloignent, une silhouette encapuchonnée apparaît brièvement en haut d'une meurtrière… "
        "L’homme mystérieux qui avait salué Aldric les observe silencieusement, avant de disparaître dans l’ombre.[/italic]"
    )

    console.print(
        "[italic]Derrière eux, la porte du deuxieme étage se referme, et les derniers bruits des pilleurs résonnent… "
        "jusqu'à ce qu'ils comprennent que la porte ne s’ouvrira plus. "
    "Leurs cris s’élèvent alors, tambourinant contre la pierre froide.[/italic]"
    )

    console.print("\n[bold cyan]Participants restants : 67 sur 97.[/bold cyan]")
    
    console.print("Vous remarquer un groupe d'individus suspects près de la grille qui vous toise")
    
    console.print("Clotaire : Hm sera tu une menace ? pas toi paysan bien sur que tu n'est la avec pas tes bottes trop grandes")
    
    clotaire_dialogue = Dialogue(
        "Comment réagissez-vous face à Clotaire et sa bande ?",
        [
            {
                "text": "« J'ai remarrqué que tu nous espionnais... Moi aussi je te surveille. Si tu deviens une menace, je te tue. » (+10 Kael, +5 Garen, -10 Clotaire)",
                "consequence": lambda h: [
                    console.print("Kael (approuvant) : 'Enfin quelqu’un qui parle. C’est pas trop tôt.'"),
                    console.print("Garen (hoche la tête, soulagé) : 'C’est bien… Il faut leur montrer qu’on n’est pas des proies faciles.'"),
                    console.print("Clotaire (plissant les yeux) : 'Oh ? Menace-moi encore, petit homme.. J’adore ça.'"),
                    hero.get_relation("Kael").adjust_score(+10),
                    hero.get_relation("Garen").adjust_score(+5),
                    hero.get_relation("Clotaire").adjust_score(-10)
                ]
            },
            {
                "text": "« Ils ont raison. Garen tes bottes sont trop grandes...comment fait tu pour marcher avec. » (+10 Clotaire, -10 Garen, -5 Ayela, -5 Kael)",
                "consequence": lambda h: [
                    console.print("Clotaire (souriant) : 'Ahahahah il a de l'humour ! j'aime ca et les gars vous avez entendu ! Ahahah je me marre !'"),
                    console.print("Garen (déçu) : 'Aldric… Tu penses vraiment ça ?'"),
                    console.print("Ayela (froide) : 'C’est une façon de voir les choses… mais ne t’attends pas à ce que je cautionne ça.'"),
                    console.print("Kael (soupire) : 'Garen...il a pas tort...'"),
                    hero.get_relation("Clotaire").adjust_score(+10),
                    hero.get_relation("Garen").adjust_score(-10),
                    hero.get_relation("Ayela").adjust_score(-5),
                    hero.get_relation("Kael").adjust_score(+5)
                ]
            },
            {
                "text": "« On n’a pas besoin de s’attarder. Venez, on continue. » (+5 Ayela, +5 Garen, neutre Clotaire)",
                "consequence": lambda h: [
                    console.print("Ayela (hoche la tête) : 'Tu as raison. Ils ne valent pas notre temps.'"),
                    console.print("Garen (souriant) : 'Ouais… Il vaut mieux ne pas les provoquer inutilement.'"),
                    console.print("Clotaire (amusé) : 'Hah, regarde-les fuir. Classique. (renifle) Vous sentez ca ? ca sens la mort...'"),
                    hero.get_relation("Ayela").adjust_score(+5),
                    hero.get_relation("Garen").adjust_score(+5)
                ]
            }
        ]
    )

    clotaire_dialogue.display(hero)
    
    console.print("Une fois la bande de Aldric partie la bande a Clotaire discute entre elle \n")
    console.print("\nClotaire : 'Cette bande de joyeux lurons sont pas si mauvais je propose qu'on les laisse agir...'")
    console.print("Emphyr : 'Je suis du même avis pourquoi mettre nos propres vies en jeu alors qu'ils le font pour nous..'")
    console.print("Velm : 'Bien vu !'")
    console.print("Brandio : 'On a qu'a attendre derriere eux !'")
    console.print("Emphyr : 'Attention toutes fois ! Ca a marché pour cet étage...mais rien nous dit que ca le sera pour les autres !' ")
    console.print("Clotaire : Emphyr a raison tachons juste d'adopter leur stratégie !")
    console.print("Velm et Brandio : compris boss !!!")

    game_menu.display()
            
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Chapitre 3 

def floor3(hero, game_menu):
    from rich.console import Console
    console = Console()
    
    kael = hero.get_relation("Kael").character
    
    console.print("\n[bold cyan]=== Étage 3 : La Marche des Murmures Noirs ===[/bold cyan]")
    console.print(
        "[italic]L’ascension vers le troisième étage se fait dans un silence oppressant. "
        "Les marches semblent s’étirer plus que nécessaire, comme si la tour elle-même cherchait à vous retenir. "
        "Le moindre bruit semble résonner plus fort qu'il ne devrait. Le simple battement de votre cœur devient assourdissant.[/italic]\n"
    )
    
    console.print(
        "[italic]Enfin, la porte s’ouvre lentement sur une vaste salle sombre. "
        "Un frisson glacé vous parcourt l’échine au moment où vous franchissez le seuil. "
        "L’air est glacial, et une brume noire s’enroule autour de vos chevilles, "
        "rampant tel un serpent silencieux. La sensation est étrange, comme si cette brume cherchait à s’accrocher à vous… "
        "Le plafond disparaît dans une obscurité insondable, et seuls quelques piliers brisés se dressent çà et là, "
        "comme les vestiges d’un temple oublié, témoin silencieux d’un passé depuis longtemps effacé.[/italic]\n"
    )
    
    console.print(
        "[bold yellow]Des voix s’élèvent doucement dans l’air. Des murmures. Incompréhensibles, mais omniprésents. "
        "C’est comme si la salle entière chuchotait des secrets que vous n’étiez pas censé entendre. "
        "À la lueur d’une faible torche, des silhouettes apparaissent lentement dans la pénombre… "
        "Des créatures fines et décharnées, vêtues de robes en lambeaux, "
        "tenant des lanternes irradiant une lumière noire, une lumière qui semble absorber plutôt qu’éclairer.[/bold yellow]"
    )

    console.print(
        "[italic]Les créatures flottent plus qu’elles ne marchent, glissant silencieusement entre les piliers comme des ombres arrachées à un autre monde. "
        "Elles semblent appartenir à cet endroit, leur existence même fondue dans la tour. "
        "Leurs visages sont cachés sous des capuches déchirées. "
        "Elles n’ont pas d’yeux… mais elles écoutent. Chaque souffle trop fort, chaque pas imprudent pourrait attirer leur attention.[/italic]"
    )

    console.print(
        "[italic]Un des murmures s’amplifie soudain, devenant presque perceptible à l’oreille, comme un soupir à la limite du langage. "
        "La lumière des lanternes noires semble pulser au rythme de ce murmure grandissant, comme un avertissement.[/italic]"
    )
    
    # Dialogue
    console.print("Kael (murmure, les yeux fixés sur les créatures) : 'C’est quoi ces choses ?... Aldric avait raison, ça va empirer…'")
    console.print(
        "[italic]Kael se déplace lentement, ses doigts effleurant la garde de sa rapière, "
        "comme s'il s'attendait à devoir se défendre à tout moment, bien qu’il sache probablement que l’acier n’y changerait rien.[/italic]"
    )
    
    console.print("Garen (la gorge nouée) : 'Ce sont… des démons ? On ne peut pas combattre ça…'")
    console.print(
        "[italic]Garen recule légèrement derrière vous, évitant soigneusement de marcher sur une pierre craquelée qui pourrait trahir sa présence. "
        "Il s’efforce de contrôler sa respiration, mais ses doigts tremblants trahissent sa peur grandissante.[/italic]"
    )
    
    console.print("Aldric (calme) : 'Ce ne sont pas des démons. Mais elles ne sont pas vivantes non plus.'")
    console.print(
        "[italic]Votre voix se fait basse, mesurée. Inutile de montrer la moindre hésitation. "
        "Vous avancez avec précaution, observant ces entités sans vie, espérant que leur attention reste ailleurs.[/italic]"
    )
    
    console.print("Ayela (tremblante, en serrant son arc) : 'Je… Je n’ai jamais vu… rien de tel…'")
    console.print(
        "[italic]Ayela s’accroche nerveusement à son arc, mais ses mains tremblent trop pour bander correctement une flèche. "
        "Vous sentez qu’elle lutte contre l’envie de fuir, mais ses pieds restent ancrés au sol, malgré la peur qui tord ses traits.[/italic]"
    )
    
    console.print(
        "[italic]L’air devient de plus en plus froid. Chaque pas semble pesé et surveillé. "
        "Les créatures poursuivent leur ronde, ignorant encore votre présence, mais combien de temps cela durera-t-il… ?[/italic]"
    )
    # Première épreuve : Traverser la salle sans être détecté
    console.print(
        "\n[italic]La salle est vaste, mais les créatures sont nombreuses. "
        "Elles avancent lentement, balayant l’espace de leur lanterne noire. "
        "Il n’y a que deux options : avancer lentement et en silence, ou détourner leur attention.[/italic]"
    )

    actions = [
        "Avancer lentement (Discrétion totale).",
        "Créer une diversion (Prendre un risque calculé)."
    ]
    
    while True:
        console.print("\n[bold]Que décides-tu de faire ?[/bold]")
        for i, action in enumerate(actions):
            console.print(f"{i + 1}. {action}")
            
        choix = input("\nVotre choix : ")
        
        if choix == "1":
            console.print(
            "\n[italic]Vous avancez à pas feutrés, chaque souffle retenu, évitant soigneusement les lanternes funestes. "
            "L'air est si dense que même vos propres battements de cœur semblent résonner contre les piliers antiques. "
            "Les murmures des créatures, bien que lointains, glissent jusqu'à vos oreilles, tissant une toile d'angoisse palpable.[/italic]"
            )
        
            console.print(
                "[italic]Mais alors que vous progressez en ligne serrée, un cri retentit. "
                "Derrière vous, l’un des participants trébuche, son pied heurtant violemment une pierre dissimulée par la brume. "
                "Le bruit résonne dans toute la salle comme une cloche funèbre.[/italic]"
            )
        
            console.print(
                "[bold red]Cri déchirant.[/bold red] [italic]Avant même qu'il ne puisse se relever, la lumière noire s'élève, "
                "enveloppant son corps frêle comme un linceul. Son cri s'étouffe rapidement, remplacé par un silence terrifiant. "
                "Clotaire : 'Merci bien pour la couverture !'"
                "Garen : 'Enfoiré !!!' "
                "Velm : 'La ferme paysan ! on veux gagner !'"
                "Son visage figé dans une grimace de terreur disparaît sous une couche de pierre sombre.[/italic]"
            )
        
            console.print(
                "Kael (à voix basse, un regard sombre) : 'Mort. Il n'aurait pas dû venir dos a lui… Continue de marcher. Ce Clotaire...'"
                "Aldric : 'Il est pret a tout les coup bas attention !'"
                "Kael : 'Garen ! Si tu t'arrêtes pour pleurer, tu seras le suivant.'"
                "Emphyr : Pauvre bébé...endurcis toi un peu ! "
                "Garen : 'Je...(Garen etait subjugé par la beauté de Emphyr il sentait une part d'honneté en elle)'"
            )
        
            console.print(
                "Garen (les poings serrés, regard fixé au sol) : 'Il était juste… il voulais juste reussir !!!…' "
                "Brandio : Ouin Ouin tout le monde il est gentil hein ahahahah ! "
                "[italic]Sa voix tremble, mais il n'ose pas s'arrêter.[/italic]"
            )
        
            console.print(
                "[italic]Les statues silencieuses continuent de veiller sur leur victime nouvelle, tandis que vous poursuivez votre marche, "
                "les épaules plus lourdes qu'avant.[/italic]"
            )
            break
        
        elif choix == "2":
            console.print(
            "\n[italic]Tu t’accroupis lentement, cherchant du bout des doigts une pierre lisse et froide. "
            "En la serrant dans ta paume, tu ressens toute la tension pesant sur tes épaules. "
            "Le regard des créatures semble peser sur toi sans même qu'elles ne t’aient repéré. "
            "Tu inspires profondément… et lances la pierre au loin, vers un amas de piliers brisés.[/italic]"
            )
        
            console.print(
                "[italic]Un bruit sourd résonne. Presque aussitôt, la créature la plus proche lève lentement la tête. "
                "Son capuchon tressaille, et elle glisse silencieusement vers l’origine du son, ses mouvements aussi fluides que l’ombre.[/italic]"
            )
        
            console.print(
                "[italic]Vous profitez de cette diversion pour avancer rapidement. "
                "Mais à quelques pas de l’autre côté, Kael et Garen se retrouvent soudain bloqués. "
                "Un autre groupe de créatures s’est déplacé et les encercle partiellement, "
                "laissant très peu d’espace pour passer.[/italic]"
            )
        
            console.print(
                "Kael (à voix basse, le regard froid) : 'Fantastique. Piégés. Juste quand ça devenait intéressant…' "
                "[italic]Il serre la garde de son épée, mais la relâche presque aussitôt, sachant que l’acier ne leur servira à rien ici.[/italic]"
            )
        
            console.print(
                "Garen (le souffle court, regard anxieux) : 'On peut pas rester là. "
                "Si on bouge pas ensemble… ils nous auront l’un après l’autre.'"
                "Emphyr : 'Bouge maintenant ! C'est le bon timing !'"
                "Clotaire : Et Emphyr pourquoi tu aide le paysan ?"
                "Garen : M...merci.."
                
            )
        
            console.print(
                "Kael (regardant Garen du coin de l'œil) : 'C’est toi ou moi… Et je ne compte pas mourir aujourd’hui.'"
            )
        
            console.print(
                "Aldric (calme, mais ferme) : 'Alors bougez. Suivez-moi. On traverse ensemble ou personne ne passe.'"
                "Clotaire : 'Oh ca oui on va te suivre le blondinet !'"
                "Garen : 'Degage !'"
                "Brandio : 'Les gars le paysan nous a dit de degager ! c'est bon je rentre chez moi !'"
                "Velm : 'Ahahah tu est con Brandio ! me fait pas rire pas maintenant'"
                "Emphyr : 'Concentrez vous ! '"
            )
        
            console.print(
                "[italic]Kael finit par hocher la tête, et Garen s’accroche à l’épée qu’il tient maladroitement. "
                "Vous attendez un court instant, puis glissez silencieusement à travers les ombres, "
                "espérant que la tour détourne son regard un instant de plus.[/italic]"
            )
            break
        
        else:
            console.print("[bold red]Choix invalide. Réessayez.[/bold red]")
            continue

    console.print(
        "\n[italic]À mi-chemin, l’une des créatures s’arrête et lève sa lanterne, "
        "comme si elle percevait quelque chose. Ayela recule d’un pas involontaire…[/italic]"
    )
    console.print("Cri assourdissant. La créature se tourne vers vous, levant sa lanterne noire vers Ayela.")

    console.print("\n[bold]Que fais-tu ?[/bold]")
    console.print("1. Tirer Ayela hors du faisceau.")
    console.print("2. Utiliser un objet pour bloquer la lumière.")
    
    choix_ayela = input("\nVotre choix : ")
    
    if choix_ayela == "1":
        console.print(
        "\n[italic]Voyant le danger s'approcher d'Ayela, tu réagis instinctivement. "
        "Tu l'attrapes fermement par le bras et la tires violemment en arrière, hors du faisceau noir. "
        "La lumière effleure la bordure de ton manteau, brûlant le tissu et marquant ta peau d'une vive douleur.[/italic]"
        )
    
        console.print(
            "[italic]Ayela trébuche contre toi, ses mains agrippant ton bras avec force. "
            "Son souffle est saccadé, et ses yeux, écarquillés de terreur, croisent les tiens dans un silence pesant.[/italic]"
        )
    
        console.print(
            "Ayela (voix tremblante) : 'Merci… Je… Je te dois la vie...' [bold green](+5 relation avec Ayela).[/bold green]"
        )
    
        console.print(
            "Aldric (sérieux, gardant son calme) : 'Reste concentrée. La prochaine fois, je ne pourrai peut-être pas t’aider.'"
        )
    
        console.print(
            "[italic]Ayela hoche la tête faiblement, reprenant lentement ses esprits. "
            "Malgré la brûlure qui te lance, tu reprends la marche en silence, sentant le regard d'Ayela peser sur toi.[/italic]"
        )
    
        hero.get_relation("Ayela").adjust_score(+5)
        hero.adjust_health(-15)

    elif choix_ayela == "2":
        console.print(
            "\n[italic]Calme et méthodique, tu plonges la main dans ta sacoche, sortant un petit miroir poli. "
            "Sans hésitation, tu l'élèves devant toi, capturant brièvement la lumière noire. "
            "Un faisceau inversé se propage, attirant l'attention de la créature vers un autre groupe.[/italic]"
        )
    
        console.print(
            "[italic]Trois participants, plus lents à réagir, se retrouvent pris au piège du faisceau. "
            "Leur corps se raidit, leurs cris s'étouffent et bientôt ils ne sont plus que des statues figées dans l'horreur.[/italic]"
        )
    
        console.print(
            "Garen (abasourdi, la voix brisée) : 'On aurait pu les sauver…' [bold red](-15 relation avec Garen).[/bold red]"
        )
    
        console.print(
            "Ayela (les larmes aux yeux, secouée) : 'C'est ma faute... Je suis trop conne... Si je n'avais pas… je… je…'"
        )
        
        console.print(
            "Emphyr : 'On ne peut pas sauvé tout le monde !'"
        )
    
        console.print(
            "Kael (calme, mais tranchant) : 'Hé, la demoiselle… C’est pas le moment de chialer. "
            "C'était eux ou toi. La tour ne fait pas de cadeaux. Pas vrai, Aldric ?'"
        )
    
        console.print(
            "Aldric (froid, détaché) : 'Ils savaient les risques. Si c'était nous à leur place, ils n'auraient pas hésité non plus.'"
        )
    
        console.print(
            "Kael (souriant légèrement) : 'Bien parlé. J'apprécie ton sens des priorités.' [bold green](Kael +10 relation pragmatique).[/bold green]"
        )
    
        console.print(
            "[italic]Ayela serre les poings, les yeux rivés au sol. Garen reste en retrait, le regard hanté par la scène. "
            "Le poids des décisions prises pèse lourdement sur le groupe alors que vous reprenez lentement votre marche vers l’inconnu.[/italic]"
        )
    
        hero.get_relation("Garen").adjust_score(-15)
        hero.get_relation("Kael").adjust_score(+10)
    
    else:
        console.print("[bold red]Choix invalide.[/bold red]")
        
          # Clôture de l'étage
    console.print(
    "\n[italic]Finalement, après une progression lente et douloureuse, vous atteignez l’autre côté de la salle. "
    "Les créatures cessent de vous poursuivre dès que vous franchissez la porte suivante, "
    "comme retenues par une barrière invisible. Derrière vous, l’obscurité s’étend, avalant les silhouettes des malheureux restés derrière.[/italic]"
    )
    
    console.print(
        "[italic]Ayela s’appuie un instant contre le mur froid, la respiration encore irrégulière. "
        "Ses doigts tremblants effleurent son arc alors qu’elle tente de retrouver son calme. "
        "Une larme solitaire glisse sur sa joue avant qu’elle ne l’essuie rapidement, évitant tout regard prolongé.[/italic]"
    )
    
    console.print(
        "Ayela (à voix basse, esquissant un faible sourire malgré elle) : 'Merci… Tu as fait ce qu’il fallait…'"
    )
    
    console.print(
        "Kael (croisant les bras, jetant un regard amusé à Garen) : 'On a survécu. C’est tout ce qui compte. "
        "Tant que je suis en vie, la tour devra essayer plus fort pour me mettre à genoux.'"
    )
    
    console.print(
        "Aldric (glissant son épée dans son fourreau, haussant un sourcil) : 'C’était plus simple que je ne le pensais. "
        "Elles ne semblent pas vouloir franchir cette porte…' [italic]Le jeune guerrier observe l'obscurité derrière lui, pensif.[/italic]"
    )
    
    console.print(
        "Garen (haletant, les mains sur les genoux) : 'Parle pour toi… Moi, j’ai cru que c’était fini à trois reprises. "
        "Ces créatures… elles… elles n’ont même pas d’yeux, mais elles savent où nous sommes.'"
    )
    
    console.print(
        "[italic]Un silence pesant s’installe alors que le groupe reprend la marche. "
        "Aldric ne peut s’empêcher de se demander où il a déjà vu ces créatures. "
        "Un souvenir lointain, brouillé, refait surface… une sensation de déjà-vu inquiétante.[/italic]"
    )
    
    console.print(
        "[italic]Les pas du groupe résonnent dans l’escalier en colimaçon, les ombres des torches dansant sur les murs humides. "
        "Garen marche en silence, jetant des regards nerveux derrière lui à chaque grincement. "
        "Kael, en revanche, semble détendu, ses mains dans les poches, mais son regard ne quitte pas Aldric.[/italic]"
    )
    
    console.print(
        "Kael (légèrement moqueur, un sourire en coin) : 'À quoi tu penses ? D’ailleurs… je ne suis pas le seul à le remarquer, n’est-ce pas ?' "
        "[italic]Kael incline la tête vers Garen, qui acquiesce silencieusement.[/italic]"
    )
    
    console.print(
        "Kael : 'Tu es dans ton élément ici… c’est presque… trop naturel pour toi. "
        "Tu n’as pas peur, tu avances d’un pas assuré… C’est suspect…'"
    )
    
    console.print(
        "[italic]Aldric ne répond pas immédiatement, ses yeux fixés sur les marches devant lui. "
        "Il sent le poids du regard de Kael, mais il ne détourne pas le sien de la torche vacillante qui guide leur ascension.[/italic]"
    )
    
    console.print(
        "Aldric (calme, mais distant) : 'Peut-être que la peur m’a quitté il y a longtemps.'"
    )
    
    console.print(
        "Kael (ricanant doucement) : 'Hah. Peut-être… ou peut-être que tu es juste aussi fou que cette tour.'"
    )
    
    console.print(
        "[italic]Garen reste silencieux, préférant garder ses pensées pour lui. "
        "Ayela serre la sangle de son carquois, jetant un dernier regard vers Aldric. "
        "Tous ressentent que ce n’est que le début… et que plus ils montent, plus la tour se montrera cruelle.[/italic]"
    )

    # Dialogue – Réponse d'Aldric
    kael_dialogue_3 = Dialogue(
    "Comment répondez-vous à Kael ?",
    [
        {
            "text": "« Un conseil, je suis pas comme Garen. Joue au malin avec moi et tu redescendras aussi vite que tu es monté. » (-5 relation Kael, Garen).",
            "consequence": lambda h: [
                hero.get_relation("Kael").adjust_score(-5),
                hero.get_relation("Garen").adjust_score(-5)
            ]
        },
        {
            "text": "« Pense ce que tu veux. Rien ne t’oblige à me suivre. Si ma tête vous revient pas, vous êtes libres de continuer sans moi. » (+5 relation Kael, Garen, Ayela).",
            "consequence": lambda h: [
                hero.get_relation("Kael").adjust_score(+5),
                hero.get_relation("Garen").adjust_score(+5),
                hero.get_relation("Ayela").adjust_score(+5)
            ]
        }
    ],
        character=kael
    )
    kael_dialogue_3.display(hero)

# Réactions en fonction du choix
    if hero.get_relation("Kael").score >= 0:
        console.print(
            "Kael (soupirant, baissant légèrement les yeux) : 'Tu as... raison après tout. "
            "Ce n’est pas comme si tu m’avais forcé, hein ?'"
            )
        console.print(
            "Garen (hochant la tête, avec assurance) : 'J’ai confiance en Aldric. "
            "Il parle peu mais c’est quelqu’un de fiable, même dans le pire des cas.'"
        )
        console.print(
            "[italic]Garen se tient un peu plus droit, tentant de se rassurer lui-même autant que les autres. "
            "Kael, malgré son arrogance habituelle, détourne brièvement le regard, comme s'il évitait d'admettre qu'il partage ce sentiment.[/italic]"
        )
        console.print(
            "Ayela (taquinant légèrement, croisant les bras) : '...Et puis, il est plutôt beau garçon, non ? "
            "Courageux, ténébreux… Un vrai protagoniste de conte.' [italic]Elle lance un clin d'œil exagéré vers Aldric.[/italic]"
        )
        console.print(
            "Kael (gêné, agitant la main) : 'Ok, ça suffit. Je suis là pour survivre, pas pour écouter tes fantasmes.'"
        )
        console.print(
            "[italic]Ayela rit doucement, mais son regard se pose un instant sur Aldric, comme si ses mots étaient moins légers qu'ils n'y paraissaient.[/italic]"
        )
    else:
        console.print(
            "Kael (froidement, baissant la voix) : 'Je vais te le dire une fois, Aldric. "
            "Si tu deviens une menace pour ma survie… je te neutraliserai. "
            "Je n’hésiterai pas.' [italic]Son regard perçant s'attarde sur Aldric, pesant.[/italic]"
        )
        console.print(
            "[italic]L’air devient plus lourd, et même Garen semble le ressentir. "
            "Le jeune homme déglutit difficilement, jetant un regard inquiet vers Aldric.[/italic]"
        )
        console.print("Garen (inquiet) : 'Aldric… Fais attention à lui.'")

        console.print(
            "[italic]Le groupe continue son ascension, les tensions flottant dans l’air comme des ombres invisibles. "
            "Chacun surveille ses arrières, mais une chose est claire : la tour teste non seulement leur force, "
            "mais aussi leur cohésion. Et tous savent que les épreuves à venir ne feront qu'empirer.[/italic]"
        )
    
    console.print("\nJuste avant de partir Garen tombe sur Emphyr")
    
    console.print("Garen : 'M...merci pour tout a l'heure...'")
    
    console.print("Emphyr : 'Te fait d'idée... et ne te fait pas tué...compris (Emphyr fit un clin d'oeil a Garen qui rougit)'")
    
    console.print("\n[bold cyan]Participants restants : 39 sur 97.[/bold cyan]")
    
    

    game_menu.display()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#chapitre 4

def floor4(hero, game_menu):
    from rich.console import Console
    console = Console()

    # Transformation de l'observateur en Archeon
    observer_relation = hero.get_relation("Homme mystérieux")
    if observer_relation:
        archeon = observer_relation.character
        archeon.name = "Archeon"
        archeon.description = "Un homme énigmatique à la présence magnétique."
    else:
        archeon = Character("Archeon", "Un homme énigmatique à la présence magnétique.", "inconnu")
        hero.add_relation(archeon, "neutral")

    console.print("\n[bold cyan]=== Étage 4 : L'Illusion du Repos ===[/bold cyan]")

    console.print(
        "[italic]La porte s'ouvre lentement, laissant place à une scène qui semble tout droit sortie d'un rêve. "
        "Des tapis d’un velours pourpre tapissent le sol, des tables en bois massif couvertes de plats fumants s’étendent à perte de vue. "
        "Les lanternes suspendues flottent doucement dans l’air, projetant une lumière dorée qui danse sur les murs de pierre. "
        "L’odeur sucrée du vin et des fruits frais envahit vos narines, tranchant radicalement avec la lourdeur des étages précédents.[/italic]"
    )

    console.print("Kael (méfiant, scrutant la salle) : 'Une blague ? Je n'y crois pas une seconde. Trop beau pour être vrai.'")
    console.print("Garen (haletant, s’essuyant le front) : 'Est-ce... réel ? Je n’ai jamais vu ça... même chez les nobles du village…'")

    console.print(
        "Ayela (voix basse, yeux plissés) : 'Après tout ce qu’on a traversé, tu crois vraiment qu’on peut juste s’asseoir et manger ?' "
        "[italic]Sa main serre instinctivement son arc, comme si elle s’attendait à ce que la moindre bouchée fasse surgir un piège.[/italic]"
    )

    console.print(
        "[italic]Autour de vous, d’autres participants s’approchent timidement des tables. Certains échangent des regards inquiets, "
        "tandis que d’autres, trop fatigués, s’effondrent sans même poser de questions, attrapant des morceaux de pain ou des coupes de vin. "
        "Les murmures se répandent dans la salle, mais une chose est claire : personne ne fait confiance à cette apparente hospitalité.[/italic]"
    )

# Apparition d'Archeon
    console.print(
        "[italic]Un frisson parcourt la pièce alors qu’une silhouette se détache lentement de l’ombre. "
        "Adossé à un pilier au fond de la salle, l’homme mystérieux de l’entrée vous observe en silence. "
        "Ses yeux brillent dans la pénombre, et sans un bruit, il s’avance au milieu de la pièce, un sourire indéchiffrable au coin des lèvres.[/italic]"
    )
    console.print("Archeon (d'une voix suave) : 'Qu’attendez-vous ? Mangez. La tour récompense ceux qui survivent.'")

    console.print(
        "[italic]Il abaisse sa capuche avec une lenteur calculée, laissant apparaître de longs cheveux écarlates qui retombent sur ses épaules. "
        "Ses traits sont fins, presque trop parfaits, mais quelque chose dans son regard vous met mal à l’aise. "
        "Il dégage une confiance implacable, comme si chaque mouvement de cette tour était orchestré par sa volonté.[/italic]"
    )
    console.print("Garen (murmurant, incapable de détourner les yeux) : 'C’est qui… ? Il dégage une drôle d’aura…'")

    console.print(
        "Kael (croisant les bras, un rictus nerveux au coin des lèvres) : 'Ce type me plaît pas. Son genre d’individu finit toujours par avoir du sang sur les mains…' "
        "[italic]Kael ne quitte pas Archeon du regard, ses doigts effleurant discrètement la garde de sa rapière.[/italic]"
    )

    console.print(
        "Archeon (regardant Kael, sourire amusé) : 'Tu n’as pas besoin de m’aimer. Écoute seulement. "
        "C’est tout ce que je demande.'"
    )

    console.print(
        "[italic]Le silence s’installe alors qu’Archeon s’avance, passant lentement entre les tables. "
        "Chacun de ses pas semble échoir plus lourdement que les autres. "
        "Les participants détournent les yeux, mais vous pouvez sentir que tous retiennent leur souffle.[/italic]"
    )

    console.print(
        "Archeon (voix calme, presque bienveillante) : 'Vous êtes trente-neuf. Peu atteindront le sommet. "
        "Les deux prochains étages seront impitoyables.'"
    )
    console.print(
        "Archeon (marquant une pause) : 'D’ailleurs, avant que je ne parte… Pour ouvrir la porte, vous devrez en payer le prix. "
        "Le prix de l’étage…' "
        "[italic]Il s’arrête un instant, laissant les mots planer dans l’air, savourant la confusion qui s’installe.[/italic]"
    )

    console.print(
        "Kael (haussant un sourcil, bras croisés) : 'Poétique. Mais ça ne nous avance à rien.' "
        "[italic]Kael ricane doucement, mais son rire sonne creux. "
        "Même lui n’arrive pas à cacher l’anxiété qui monte à mesure qu’Archeon parle.[/italic]"
    )

    console.print(
        "[italic]Archeon sourit légèrement avant de se détourner, disparaissant lentement dans l’ombre du pilier d’où il était venu. "
        "Son absence laisse un vide étrange dans la salle, comme si la chaleur de la lumière avait quitté l’endroit avec lui.[/italic]"
    )

   # Interaction avec Archeon
    console.print(
        "[italic]Alors qu'Archeon s'apprête à se retirer dans l'ombre, il s'arrête un bref instant près d'Aldric. "
        "Son regard, perçant et presque amusé, s'attarde sur vous plus longtemps que nécessaire. "
        "Là, dans cette fraction de seconde, vous sentez qu'il vous observe d'une manière différente… Comme s'il voyait quelque chose que les autres ignorent.[/italic]"
    )

    console.print(
        "Archeon (d'un ton bas et presque conspirateur) : '[italic]Prends des forces. Je t'attends plus haut... Ne me déçois pas.[/italic]'"
        "[italic]Son murmure s’infiltre comme un frisson désagréable, laissant derrière lui une étrange impression de déjà-vu.[/italic]"
    )

    console.print(
        "[italic]Son ombre glisse au loin alors que ses pas disparaissent dans l'obscurité du pilier. Pourtant, même en son absence, "
        "l'aura d'Archeon semble planer dans la pièce, imprégnant chaque coin du regard des autres participants.[/italic]"
    )

    console.print(
        "Ayela (inquiète, fronçant les sourcils) : '[bold yellow]Tu le connais ?[/bold yellow]' "
        "[italic]Sa voix est plus basse qu’à l’accoutumée, comme si elle craignait qu’Archeon puisse encore l’entendre.[/italic]"
    )

    console.print(
        "Aldric (après une longue pause, fixant l'endroit où Archeon se tenait) : '[bold cyan]Je ne crois pas.[/bold cyan]' "
        "[italic]Mais même en prononçant ces mots, une part de vous doute. Comme si, quelque part, son visage vous était familier… "
        "Sans savoir pourquoi.[/italic]"
    )

    console.print(
        "[italic]Les regards de Kael et Garen se tournent vers vous, mais aucun d'eux ne parle. "
        "Kael détourne rapidement les yeux, comme agacé par la scène, tandis que Garen semble simplement troublé par l’échange silencieux.[/italic]"
    )

    hero.get_relation("Archeon").adjust_score(+5)

    console.print(
        "[italic]Aldric peut sentir quelque chose changer en lui, un mélange d’excitation et d’appréhension… "
        "Car dans les profondeurs de la tour, il sait que ce n'est pas la dernière fois qu'il croise Archeon.[/italic]"
    )
    # Moment de repos – Interaction avec le groupe
    console.print("\n[bold]Vous vous installez autour d'une table. Qui souhaitez-vous interroger ?[/bold]")
    
    interactions = [
        "Parler à Garen.",
        "Parler à Kael.",
        "Parler à Ayela.",
    ]

    while interactions:
        console.print("\n[bold]Options disponibles :[/bold]")
        for i, interaction in enumerate(interactions):
            console.print(f" {i + 1}. {interaction}")
        
        choix = input("\nAvec qui voulez-vous discuter ? : ")
        
        if not choix.isdigit() or int(choix) < 1 or int(choix) > len(interactions):
            console.print("[bold red]Choix invalide. Veuillez sélectionner une option existante.[/bold red]")
            continue
    
        choix = int(choix) - 1
        action = interactions[choix]
        
        # Dialogue avec Garen
        if action == "Parler à Garen.":
            console.print("\nAldric (Vous vous approchez de Garen, le voyant pensif à l'écart des autres) : "
                 "'Au fait, tu m'as jamais dit pourquoi tu avais tenté la tour... ?'")

            console.print("Garen (baisse les yeux, triturant l'anneau en cuir de son gantelet) : "
                 "'Ah ça... eh bien... J'ai quitté la ferme. Mon père voulait me marier pour un prêt… parce que la ferme fait faillite.'")
    
            console.print("Garen (légèrement tremblant) : "
                 "'Je voulais prouver à mon père que je pouvais subvenir... sauver la ferme. Mais je crois que j'ai surtout voulu me prouver à moi-même… "
                 "que je ne suis pas l'incapable qu'il prétend.'")
    
            console.print("[italic]Sa voix est lourde de regrets et d'espoir. Il semble gêné, incapable de croiser votre regard.[/italic]")
    
            console.print("Garen (riant nerveusement) : 'J'ai alors dépensé toutes mes économies… pour cette armure et cette épée. "
                 "Regarde-moi ça, du toc. Je crois que je me suis fait avoir…'")

            console.print("Garen (voix basse) : '[italic]Le pire dans tout ça, c'est que ma mère m'a dit au revoir... comme si elle savait que je ne reviendrais jamais.[/italic]'")

            garen_dialogue = Dialogue(
            "Comment répondez-vous à Garen ?",
            [
                {
                    "text": "« Tu te bats pour eux, certes... mais aussi pour toi. C'est ce qui compte. Tu veux te prouver que tu es capable. »",
                    "consequence": lambda h: [
                        hero.get_relation("Garen").adjust_score(+15),
                        console.print("Garen (souriant sincèrement, levant enfin la tête) : "
                                "'Tu le penses vraiment ?'"),
                        console.print("[italic]Il vous regarde avec une sincérité touchante, un sourire timide aux lèvres.[/italic]"),
                        console.print("Garen : 'Merci Aldric. C'est grâce à toi si j'ai pu survivre jusqu'ici. "
                                "Je vais sûrement mourir ici, mais au moins… je suis content de te connaître.'"),
                        console.print("Aldric (croisant les bras avec un léger sourire) : "
                                "'Je m'attendais pas à faire équipe non plus... mais je suis content aussi de te connaître, Garen.'"),
                        console.print("Garen (regardant la porte suivante, déterminé) : 'J'espère que nous survivrons à tout ça... "
                                "Merci Aldric.' [italic](Relation Garen +5)[/italic]")
                    ]
                },
                {
                    "text": "« Peut-être que tu n'aurais pas dû venir… »",
                    "consequence": lambda h: [
                        hero.get_relation("Garen").adjust_score(-5),
                        console.print("Garen (déçu, baissant la tête encore plus bas) : "
                                "'Tu... tu as sûrement raison. Je ne suis qu'un boulet… "
                                "et en plus de ça, je vais sûrement mourir.'"),
                        console.print("[italic]Un silence inconfortable s'installe. Garen essaie de masquer sa peine, mais vous devinez facilement ses pensées.[/italic]"),
                        console.print("Aldric (tapant doucement l'épaule de Garen) : "
                                "'Je m'attendais pas à faire équipe non plus... mais je suis content aussi de te connaître.'"),
                        console.print("Aldric (en se levant) : 'C'est trop tard pour faire demi-tour maintenant. Assume.'"),
                        console.print("Garen (hochant doucement la tête) : '[italic]Ouais… T'as raison.[/italic]'")
                    ]
                }
            ]
        )
            garen_dialogue.display(hero)
            interactions.pop(choix)

        elif action == "Parler à Kael.":
            console.print("\nAldric (vous approchez Kael, installé nonchalamment près d'une table, une chope à la main) : "
                 "'Alors tu es un noble, hein ? Dis-moi... Qu'est-ce qu'un type comme toi fait ici ?'")

            console.print("[italic]Kael, le dos appuyé contre une poutre, lève à peine les yeux de sa boisson. Son sourire en coin trahit un amusement non dissimulé.[/italic]")
    
            console.print("Kael (ricane en buvant sa bière) : "
                 "'Un noble, oui. Mais pas assez riche pour éviter de finir ruiné.' "
                 "[italic](Il fixe Aldric du coin de l'œil, l'air plus sérieux qu'il n'y paraît.)[/italic]")
    
            console.print("Kael : '[italic]Mon domaine viticole est en mauvais état. Je veux le sauver... "
                 "Pour ne pas perdre mon titre et mon honneur. Tu comprends ça, non ?[/italic]'")
    
            console.print("[italic]Il tourne la chope entre ses doigts, pensif, mais son regard ne vous quitte pas. "
                 "Un voile d'ironie couvre ses paroles, mais vous devinez qu'il en dit moins qu'il ne pense.[/italic]")

            kael_dialogue = Dialogue(
            "Comment répondez-vous à Kael ?",
            [
                {
                    "text": "« Ça semble crédible. Mais tu caches autre chose. » ",
                    "consequence": lambda h: [
                        hero.get_relation("Kael").adjust_score(-5),
                        console.print("Kael (hausse un sourcil, amusé) : 'Hm… sans doute. Qui sait ?'"),
                        console.print("[italic]Il prend une nouvelle gorgée, sans se départir de ce sourire narquois.[/italic]"),
                        console.print("Kael : 'Tu es bien plus malin que tu en as l'air, Al'.'"),
                        console.print("Aldric (fronçant les sourcils) : 'M'appelle pas comme ça.'"),
                        console.print("Kael (riant) : '[italic]Oooh, j'ai touché une corde sensible ahah ![/italic]'"),
                        console.print("Kael (le regard taquin) : '[italic]Part pas, je plaisantais. T'es susceptible...[/italic]'"),
                        console.print("[italic](Aldric secoue la tête, préférant s'éloigner. Kael l'observe partir en silence.)[/italic]")
                    ]
                },
                {
                    "text": "« Tu mens mal, Kael. » ",
                    "consequence": lambda h: [
                        hero.get_relation("Kael").adjust_score(+15),
                        console.print("Kael (sourire effacé, l'air surpris) : '…Hah, t'es un petit futé toi. "
                                "Je l'avais deviné dès qu'on s'est croisés à l'extérieur de la tour.'"),
                        console.print("Kael : 'Tu es le genre de gars dont il faut se méfier, "
                                "et c'est toujours mon cas.'"),
                        console.print("[italic]Il pose sa chope et tend la main, son regard sincère pour une fois.[/italic]"),
                        console.print("Kael : '[italic]Mais je te respecte. Contrairement à d'autres ici…[/italic]'"),
                        console.print("Aldric (hésitant avant de serrer sa main) : 'Hm. Je dois bien l'admettre, c'est pareil.'"),
                        console.print("Kael (souriant à nouveau) : 'Tâchons de ne pas mourir trop bas dans cette foutue tour !'"),
                        console.print("[italic](Les deux hommes échangent une poignée de main ferme. La tension entre eux s'atténue légèrement.)[/italic]")
                    ]
                }
            ],
            character=hero.get_relation("Kael").character
        )
            kael_dialogue.display(hero)
            interactions.pop(choix)

        elif action == "Parler à Ayela.":
            console.print("\nAldric (vous approchez Ayela, assise à l'écart des autres, fixant le vide) : "
                 "'Et toi, alors, pourquoi tenter cette aventure presque suicidaire ?'")

            console.print("[italic]Ayela détourne légèrement les yeux, cherchant ses mots. Ses mains tremblent légèrement sur son arc posé à ses côtés.[/italic]")

            console.print("Ayela (voix douce, presque murmurée) : "
                 "'Mon village est frappé par une épidémie. Personne ne sait d'où ça vient…' "
                 "[italic](Sa voix se brise un instant, trahissant une fragilité qu'elle s'efforce de masquer.)[/italic] "
                 "'J'ai pensé… que cette tour pourrait m'apporter des réponses.'")

            console.print("Aldric (calme mais direct) : 'Tu espères pouvoir sauver ton village, c'est ça ?'")

            console.print("[italic]Ayela hoche doucement la tête. Ses yeux humides reflètent la lumière tremblante des torches, mais elle s'efforce de retenir ses larmes.[/italic]")

            console.print("Ayela (à voix basse) : '[italic]C'était stupide, je le sais… Peut-être que je ne fais que courir vers ma mort.[/italic]'")

            ayela_dialogue = Dialogue(
                "Que dites-vous à Ayela ?",
            [
                {
                    "text": "« Ce n'est pas stupide. Tu fais ce que tu peux. » ",
                    "consequence": lambda h: [
                        hero.get_relation("Ayela").adjust_score(+5),
                        console.print("[italic]Ayela lève les yeux vers vous, rougissante et légèrement surprise par votre réponse.[/italic]"),
                        console.print("Ayela (d'une voix tremblante) : 'Tu crois ? Mais… Et si je meurs ?'"),
                        console.print("[italic]Elle détourne à nouveau le regard, jouant nerveusement avec la corde de son arc.[/italic]"),
                        console.print("Ayela (souffle un rire nerveux) : 'Je suis tellement idiote parfois…'"),
                        console.print("[italic]Aldric s'approche et pose doucement sa main sur son épaule, parlant d'une voix posée.[/italic]"),
                        console.print("Aldric : 'Tu es une fille bien. Peu de gens risqueraient leur vie pour les autres. "
                                "Si tu meurs dans cette tour… alors meurs en sachant que tu auras tout fait pour ceux que tu aimes. C'est ce qui compte.'"),
                        console.print("[italic]Ayela cligne des yeux plusieurs fois, essayant de retenir ses larmes avant de vous adresser un sourire discret.[/italic]"),
                        console.print("Ayela (rougissant légèrement) : 'Aldric…' (Elle vous fixe un moment) "
                                "'Merci…' (Elle vous lance un sourire charmeur malgré ses yeux humides)(+5 relation Ayela)")
                    ]
                },
                {
                    "text": "« Les chances sont faibles. Ne te fais pas d'illusions. » ",
                    "consequence": lambda h: [
                        hero.get_relation("Ayela").adjust_score(-15),
                        console.print("[italic]Ayela baisse brusquement la tête, ses épaules s'affaissant sous le poids de vos mots.[/italic]"),
                        console.print("Ayela (voix brisée) : '[italic]J'avais déjà pas le moral… mais là… merci Aldric…[/italic]'"),
                        console.print("[italic]Elle se détourne sans ajouter un mot, s'isolant un peu plus loin, essuyant une larme discrète du revers de sa main. (-15 relation Ayela)[/italic]")
                    ]
                }
            ],
            character=hero.get_relation("Ayela").character
        )
            ayela_dialogue.display(hero)
            interactions.pop(choix)

# Sortie si plus d'interactions
        if not interactions:
            console.print("\n[italic]Vous avez discuté avec tout le monde. L'histoire peut continuer.[/italic]")
            break
        
        # Clôture de l'étage 4
    console.print(
        "\n[italic]Plus tard dans la soirée, une violente altercation éclate entre plusieurs participants. "
        "Les cris résonnent dans la salle sombre, étouffés par l'épaisseur des murs de pierre. "
        "Lorsque tout redevient silencieux, quatre corps sans vie jonchent le sol, leurs visages figés dans l'horreur. "
        "Qu'ils soient morts par ivresse ou par cupidité, leur sort est désormais lié à la tour.[/italic]"
    )

    console.print("\n[bold]La porte s’ouvre lentement après cela. Le prix de l’étage… payé.[/bold]")

    console.print(
        "[italic]Un vent glacial s'engouffre dans la salle lorsque la porte s'entrouvre, comme si la tour elle-même "
        "se nourrissait de la tragédie humaine. L'obscurité de l'étage suivant semble plus pesante encore.[/italic]"
    )   

    console.print("Kael (murmurant, observant les corps) : 'Quatre vies pour ouvrir la porte… L’énigme était littérale. La tour ne plaisante pas.'")

    console.print(
        "[italic]Aldric fixe la porte ouverte, un voile d’inquiétude passant brièvement dans ses yeux. "
        "L'air paraît plus lourd, chargé d'un sentiment qu'il n'arrive pas à chasser.[/italic]"
    )

    console.print(
        "Aldric (à voix basse, presque pour lui-même) : 'La tour... j’ai l’impression qu’elle veut dévorer nos âmes... nos vies... "
        "C’est donc ça le prix de la cupidité ?'")

    console.print(
        "[italic]Garen détourne le regard des corps, serrant nerveusement le pommeau de son épée. "
        "Ses mains tremblent légèrement, mais il garde le silence.[/italic]"
    )

    console.print("Garen (voix basse, hésitant) : 'C’est pas de la cupidité... c’est…'")

    console.print(
        "[italic]Kael éclate d’un rire bref et amer, ses yeux reflétant une lassitude grandissante.[/italic]"
    )

    console.print("Kael (ricanant) : 'Ah oui ? Et c’est quoi alors ? On n’est pas là pour apprendre à tricoter, paysan !'")

    console.print(
        "[italic]Garen lève les yeux vers Kael, mais les mots restent coincés dans sa gorge. "
        "Ses épaules s'affaissent légèrement, incapable de trouver une réponse.[/italic]"
    )

    console.print("Ayela (croisant les bras, lançant un regard à Garen) : 'Kael a raison, Garen…'")

    console.print(
        "[italic]Ayela détourne rapidement les yeux, consciente de la cruauté des mots, mais incapable de les retirer. "
        "Ils doivent avancer. Les morts sont déjà derrière eux.[/italic]"
    )

    console.print("Garen (baisse la tête, ses doigts se crispant sur sa ceinture) : '...'")

    console.print(
        "\n[italic]Le silence s'étire, seulement brisé par le grincement de la porte qui s'ouvre complètement. "
        "La bande franchit la porte, pleine de doutes mais aussi de motivation pour affronter l’étage 5.[/italic]"
    )
        
    console.print("\n[italic]Alors que le calme semble revenir, Clotaire s'avance lentement, suivi de Velm et Brando. "
            "Leur démarche est décontractée, mais leurs yeux scrutent les environs avec une lueur dangereuse.[/italic]")

    console.print("Clotaire (avec un sourire en coin) : 'Eh bien, certains n’ont pas su contenir leur soif de sang… Dommage pour eux, "
            "mais au moins la porte s'est ouverte, n’est-ce pas ?'")

    console.print("Velm (souriant narquoisement) : 'Ils ont voulu jouer aux héros. La tour n’aime pas les héros…'")

    console.print("Brando (calme, regard sombre) : 'On a juste laissé faire. Ils se sont entre-tués tout seuls.'")

    console.print("Ayela (fronçant les sourcils) : 'C'était vous, n'est-ce pas ? Vous les avez poussés à se battre.'")

    console.print("Clotaire (haussement d'épaules) : 'Je n’ai rien fait. Ils ont choisi leur destin. '")
    console.print("'[italic]Son regard croise celui d'Aldric, un éclat de défi dans les yeux.[/italic]'")

    console.print("Kael (serrant les poings) : 'Tss... Évidemment.'")
        
    console.print("Emphyr (caressant le cou de Kael) : Hm detend toi beau gosse, sans ca la grille ne se serait pas ouverte...")

    console.print("Garen (visiblement mal à l’aise) : 'On aurait pu les arrêter…'")
        
    console.print("Emphyr : 'un conseil..Laisse ta pitié a cette étage Garen ! Car sinon a un moment donnée ca va te couter cher !'")
        
    console.print("Garen (rougit): 'Mais je...")

    console.print("Brando (calmement) : 'Tu te serais fait tuer, paysan. Crois-moi, la tour n’a pas de place pour la pitié. C'est deja un miracle que tu sois si haut'")

    console.print("Clotaire (calmement, s'éloignant) : 'Les faibles tomberont comme toi paysan. La tour nous façonne à sa manière. Il est temps que vous vous en rendiez compte.'")

    console.print("[italic]Aldric observe Clotaire disparaître dans l’ombre. La porte reste ouverte, mais la salle est plus silencieuse que jamais. "
              "Le poids des pertes pèse lourdement sur les épaules des survivants.[/italic]")

    console.print("[bold cyan]Il reste 35 participants sur 97.[/bold cyan]")

    game_menu.display()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#chapitre 5
def floor5(hero, game_menu):
    from rich.console import Console
    console = Console()


    console.print("\n[bold cyan]=== Étage 5 : Le Jeu des Dalles Cryptiques ===[/bold cyan]")
     
    # Introduction à l'étage
    console.print(
        "[italic]L'air est lourd tandis que vous pénétrez dans la salle du cinquième étage. "
        "Devant vous, un plateau de pierre s'étend à perte de vue, divisé en dalles semblables à un gigantesque échiquier. "
        "Cependant, contrairement aux jeux que vous connaissez, celui-ci est différent… plus ancien, plus complexe. "
        "Des torches de flammes violettes éclairent la salle, projetant des ombres sinistres sur les murs. "
        "Au fond, perchées sur des piédestaux, des statues de gargouilles de bronze observent silencieusement la scène.[/italic]"
    )

    console.print("\nKael (pince son menton en fixant le plateau) : 'Voilà qui sort de l'ordinaire… Je déteste déjà cet étage.'")
    console.print("Garen (les yeux plissés, sourire nerveux) : 'Attendez… Je connais ce jeu. C'est le Frondeur. "
                  "Mon frère et moi y jouions souvent, mais… c'est rare d'en voir un plateau aussi grand.'")
    console.print("Ayela (serrant la corde de son arc, inquiète) : 'Je doute que ce soit aussi simple qu'un jeu d'enfants, Garen.'")

    # Apparition d'Archeon
    console.print("\n[bold]Un léger souffle balaie la salle…[/bold]")
    console.print(
        "Perché sur une passerelle de pierre en hauteur, une silhouette familière apparaît. "
        "Archeon, baigné par la lumière des torches, arbore un sourire charmeur. "
        "Son long manteau noir flotte tandis qu'il marche lentement et s'arrête au centre de la passerelle, bras croisés."
    )
    console.print("Archeon (calme) : 'Je vous félicite d'être arrivés jusqu'ici. Peu de candidats franchissent le seuil du cinquième étage…'")
    console.print("Ayela (voix basse, tremblante) : 'Chaque fois qu'il apparaît, c'est pour annoncer une nouvelle façon de mourir…'")
    console.print("Archeon (souriant) : 'Mais ne vous méprenez pas. Ce n'est pas un cadeau.'")

    console.print(
        "\nArcheon : 'Vous devez former des équipes de sept. Le but est simple : atteindre la dalle rouge dans le camp adverse. Cependant…'\n"
        "Il s'arrête un instant, laissant son regard balayer la salle avant de reprendre."
    )
    console.print("Archeon (voix profonde) : 'Voici le Jeu des Dalles Cryptiques. Simple, mais cruel.'")

    # Explication des règles
    console.print("\n[bold yellow]=== Règles du Jeu ===[/bold yellow]")
    console.print(
        "  • Formez des équipes de sept joueurs.\n"
        "  • L'objectif est de traverser le plateau et d'atteindre la dalle rouge dans le camp adverse.\n"
        "  • Chaque joueur peut avancer de 1, 2 ou 3 cases vers l'avant ou sur le côté.\n"
        "  • Si un joueur avance de deux cases sur le côté, le dernier personnage ayant avancé recule d'une case.\n"
        "  • Chaque mouvement réduit le nombre de cases que peut parcourir le joueur suivant.\n"
        "  Exemple : Si un joueur avance de 3 cases, le suivant de son équipe doit passer son tour. "
        "Si un joueur avance de 1 case, le suivant peut avancer de 2 cases."
        "Les règles s'appliquent aussi aux gargouilles.\n"
    )

    console.print("Archeon (voix sombre) : 'Ces statues de bronze ne sont pas que des pions… ce sont vos adversaires. "
                  "Elles avancent avec les mêmes règles que vous.'")
    console.print("\n[bold yellow]=== Formation des équipes ===[/bold yellow]")
    console.print(
        "\nAvant que vous ne puissiez rassembler vos alliés, une voix forte s'élève au-dessus des autres."
    )
    console.print("Clotaire (d’une voix autoritaire) : 'Nous serons avec eux.'")

    # Ajout des personnages Clotaire, Velm et Brando
   

    # Réactions des personnages
    console.print("Kael (serrant les dents) : 'Sérieusement… ? Ce type…'")
    console.print("Kael (murmurant à Aldric) : 'Ce type est un parasite…'")
    console.print("Archeon (claquant des doigts) : 'Que la partie commence.'")

    # Déroulement du jeu - Premier mouvement d'Aldric
    console.print("\n[bold cyan]=== Phase 1 : Premier Mouvement d'Aldric ===[/bold cyan]")

    console.print(
        "Vous vous positionnez sur la ligne de départ. En face, les gargouilles restent immobiles, mais vous sentez "
        "leurs yeux d’acier braqués sur vous."
    )
    console.print("Garen (confiant, souriant) : 'Ça va aller. Je connais ce jeu, je peux vous guider.'")

    console.print(
        "\nLes équipes prennent place sur les premières rangées du plateau. L'écho de vos pas résonne dans la salle silencieuse. "
        "De l'autre côté, les gargouilles de bronze fixent leur piédestal, mais leur menace est palpable."
    )
    console.print("Kael (regard noir à Clotaire) : 'T’as intérêt à pas nous foutre dedans…'")
    console.print("Clotaire (souriant en coin) : 'Détends-toi, noble. Ce n’est qu’un jeu.'")
    console.print("Ayela (murmure, anxieuse) : 'Ce jeu va nous tuer si on ne fait pas attention…'")
    console.print("Garen (sérieux) : 'Je connais bien ce jeu. Si on suit un rythme stable, on peut traverser sans perdre personne.'")

    # Archeon - Déclaration de début de partie
    console.print("\nArcheon (depuis la passerelle) : 'Rappelez-vous… seuls ceux qui atteignent la dalle rouge survivront.'")
    console.print(
        "Archeon (ton froid) : 'Et si une gargouille atteint une dalle rouge avant vous… un joueur sera sacrifié.'"
    )

    console.print(
    "\n[italic]Un silence pesant s'installe dans la salle. Lentement, les participants prennent place sur les premières dalles du plateau. "
    "Le contact froid de la pierre sous vos pieds semble vouloir aspirer toute votre énergie. "
    "Face à vous, les statues de gargouilles restent figées, mais leur présence est écrasante. Chaque battement de cœur résonne comme un écho dans cette immense arène.[/italic]"
    )
    console.print(
    "[italic]Archeon observe la scène depuis la passerelle, son regard perçant ne laissant rien passer. Un léger rictus effleure ses lèvres. "
    "Il lève lentement la main, marquant l'instant où tout basculera. Puis, dans un geste sec, sa main s'abaisse.[/italic]"
    )
    console.print("\nArcheon (voix forte) : 'Que le jeu commence.'")
    
    console.print("Aldric : Je commence ! ")
    console.print("Garen : Fait attention Al' c'est pas un jeu de course analyse bien le damier")
    console.print("Aldric (en lever mon pouce vers le haut avec un sourire) : T'en fait pas Garen ! ")
    
    console.print("Archeon : Que va tu faire Aldric (pensa Archeon)")
    


    def premier_mouvement(hero):
        from rich.console import Console
        console = Console()

        console.print("\n[bold yellow]=== Déplacement d'Aldric ===[/bold yellow]")

        mouvement = Dialogue(
            "Vous vous tenez devant la première rangée. Comment souhaitez-vous avancer ?",
            [
                {
                    "text": "Avancer d'une case (prudent).",
                    "consequence": lambda h: [
                        console.print("Kael (hochant la tête) : 'Prudent. Tu joues la sécurité.'(Kael +5)"),
                        console.print("Aldric : Pas le choix"),
                        console.print("Clotaire : peut importe c'est a moi !"),
                        console.print("Ayela (regardant autour) : 'Mmh, on reste groupés. Ça devrait aller.'"),
                        console.print("Velm (amusé) : 'Toujours à jouer la prudence… ça va pas nous faire avancer vite.'"),
                        console.print("Brandio (calme) : 'Moins vite mais en vie. C'est ça l'idée.'"),
                        console.print("Clotaire (ironique) : 'Ah, l’éternel Brandio et sa philosophie…et Velm oublie pas de leur mettre trois cases dans les dents ahah'"),
                        h.get_relation("Kael").adjust_score(+5)
                    ]
                },
                {
                    "text": "Avancer de deux cases (équilibré).",
                    "consequence": lambda h: [
                        console.print("Garen (souriant) : 'Bonne stratégie. Restons sur ce rythme.'(Garen +5)"),
                        console.print("Clotaire : a moi paysan ! (Clotaire avance de trois case)"),
                        console.print("Kael : Enflure ! tssss"),
                        console.print("Velm : Alors on fait du surplace ? Muahahah ! (dit-il a Kael en avancant de deux cases)"),
                        console.print("Ayela : A moi ! j'avance de trois cases ! alors qui fait du surplace maintenant ?"),
                        console.print("Brandio : Salope ! "),
                        console.print("Kael (soupirant) : 'Je te jure… cette bande de guignols...'"),
                        console.print("Aldric (fixant Velm) : 'Arrête de provoquer, tu ferais mieux de te concentrer.'"),
                        console.print("Velm (ricane) : 'Allez, je plaisante. On va s'en sortir… ou pas.'"),
                        console.print("Garen (léger stress) : 'Restez attentifs. On avance trop vite à mon goût…'"),
                        console.print("Clotaire (calme) : 'L'avance est l'avantage, Garen. Mais bon… on verra. tu prefere sans doute le surplace si tu meurs bah je m'en fous'"),
                        h.get_relation("Garen").adjust_score(+5)
                    ]
                },
                {
                    "text": "Avancer de trois cases (risqué).",
                    "consequence": lambda h: [
                        console.print("Kael (furieux) : 'Tu veux nous faire tuer ?'"),
                        console.print("Aldric : Je sais ce que je fait ! "),
                        console.print("Kael : j'ai pas envie de crever pas si pres du but t'entend !"),
                        console.print("Garen : Ca va le faire ! ca va le faire..."),
                        console.print("Ayela (chuchotant à Aldric) : 'T'es sûr ? Ces gargouilles vont pas nous laisser passer.'"),
                        console.print("Brandio (avançant derrière) : 'Si elles bougent, on s'en occupe.'"),
                        console.print("Clotaire (sarcastique) : 'Brandio en héros, la je te reconnais.'"),
                        console.print("Garen (calmant Ayela) : 'On est ensemble. On avance tous.'"),
                        console.print("Velm (regard vers la dalle rouge) : 'Peu importe… ils n'attaqueront pas tant qu'on n'est pas trop proches.'"),
                        console.print("Ayela (grimace) : 'J'espère que tu dis vrai.'"),
                        h.get_relation("Kael").adjust_score(-10),
                        h.get_relation("Clotaire").adjust_score(+5)
                    ]
                }
            ]
        )
        mouvement.display(hero)
    premier_mouvement(hero)
        
        
    def mouvement_gargouilles(hero):

        console.print("\n[bold yellow]=== Phase 2 : Mouvement des Gargouilles ===[/bold yellow]")
        console.print(
            "Deux gargouilles de bronze avancent en miroir à votre progression, se déplaçant de 2 cases. "
            "Elles se rapprochent lentement, prêtes à bloquer votre avancée."
        )
        console.print("Ayela (murmurant) : 'Elles bougent… C’est comme si elles attendaient qu’on se rapproche.'")
        console.print("Kael (sarcastique) : 'Logique. Elles veulent nous voir tomber une à une.'")
        console.print("Garen (inquiet) : 'Elles avancent vite… Trop vite.'")
        console.print("Brandio (fixant les gargouilles) : 'On dirait qu’elles anticipent nos mouvements.'")
        console.print("Velm (amusé) : 'Oh, allez… Elles ne font que se dégourdir les jambes.'")
        console.print("Ayela (regard noir à Velm) : 'Tu trouves ça drôle ? Elles pourraient nous tuer à tout moment.'")
        console.print("Clotaire (calme) : 'Elles suivent les règles du jeu. Rien de plus. Il suffit de ne pas paniquer. ok beauté ? (simule un bisous avec sa bouche)'")
        console.print("Kael (grognant) : 'C’est facile à dire… Jusqu’à ce que tu sois la cible. si c'est toi ca me derangerai pas'")
        console.print("Aldric (posant la main sur son épée) : 'Restons concentrés. Tant qu’on garde notre formation, on a une chance. sinon sacrifier ces trois nigauds'")
        console.print("Velm (ricanant) : 'Enfoiré on est trois equipe en realité… On verra si ta 'formation' te sauve quand elles te fonceront dessus.'")
        console.print("Garen (fixant Velm) : 'Tu devrais moins parler et plus regarder où tu mets les pieds si tu veux vivre..'")
        console.print("Brandio (avançant d’un pas lent) : 'Elles n’attaquent pas encore. Profitons-en pour avancer avec précipitation Clotaire !'")
        console.print("Ayela (hochant la tête) : 'L'enflure il a avancé de trois cases...je fait du surplace...grrrrrrrrr'")

    mouvement_gargouilles(hero)
    


    def kael_mouvement(hero):

        console.print("\n[bold yellow]=== Phase 3 : Mouvement de Kael ===[/bold yellow]")

        mouvement_kael = Dialogue(
            "Kael est le suivant à bouger. Quelle stratégie applique-t-il ?",
            [
                {
                    "text": "Avancer de 1 case (prudence).",
                    "consequence": lambda h: [
                        console.print("Kael (avançant prudemment) : 'J'avance. On reste sur ce rythme.'"),
                        console.print("Velm (ricanant derrière) : 'T’as peur d’une gargouille, noblieau ?'"),
                        console.print("Kael (jetant un regard noir) : 'Je ne parle pas aux cretins puant de ton espece (dit-il avec un regard arrogant).'"),
                        console.print("Brandio (sec) : 'Suffit. Qu'il tombe ou avance, peu m'importe. ca nous arrange presque'"),
                        console.print("Ayela (serrant son arc) : 'Ignore-les Kael… restons concentrés.'"),
                        console.print("Clotaire (en souriant) : 'Concentrés ? C'est une belle manière de dire 'lents'.'"),
                        console.print("Aldric : Garen ! Je fait quoi toi qui connait le jeu"),
                        console.print("Garen : un pas a droite pour faire reculer Brando et un pas en avant"),
                        
                        h.get_relation("Kael").adjust_score(+5)
                    ]
                },
                {
                    "text": "Avancer de 2 cases (équilibre).",
                    "consequence": lambda h: [
                        console.print("Kael (avançant rapidement) : 'J'avance de deux. Suivez-moi.'"),
                         console.print("Garen (hochant la tête) : 'On garde la cadence. C'est bien.'"),
                        console.print("Velm (ironique) : 'Oh, comme c'est inspirant. On devrait tous écrire ça sur nos tombes.'"),
                        console.print("Kael (grognant) : 'Personne ne t'a demandé ton avis, Velm.'"),
                        console.print("Clotaire (calme) : 'Continue de parler, Velm. J’aime bien quand tu les distrais.'"),
                        console.print("Brandio (se rapprochant) : 'Les distractions coûtent cher ici…' (il avance à son tour)"),
                        console.print("Aldric : j'ai hate de voir ta tete voler.."),
                        h.get_relation("Garen").adjust_score(+5)
                    ]
                },
                {
                    "text": "Passer son tour.",
                    "consequence": lambda h: [
                        console.print("Clotaire (ricanant) : 'Dommage, pauvre con. Tu vas attendre ici pendant qu’on avance. Muhaha'"),
                        console.print("Kael (serrant les poings) : 'Tsss… j’vais te laisser crever devant, Clotaire.'"),
                        console.print("Velm (moqueur) : 'Ooooh… ça sent la frustration. Fais gaffe, noble, tu vas nous ralentir.'"),
                        console.print("Ayela (croisant les bras) : 'Laissez-le tranquille. C'est pas le moment pour vos petites querelles.'"),
                        console.print("Brandio (imperturbable) : 'Clotaire, Velm ! Vous parlez trop… et vous avancez trop peu.'"),
                        console.print("Clotaire (en avançant de trois cases) : 'Continuez à discuter. Moi, je gagne. en avant les gars'"),
                        console.print("Aldric : pas si vite (Aldric avance de deux cases sur le coté...)"),
                        console.print("Clotaire : Tsss fait chier une gargouille ! Tu est content de toi hein !"),
                        h.get_relation("Clotaire").adjust_score(-5)
                    ]
                }
            ]
        )
        mouvement_kael.display(hero)
    kael_mouvement(hero)

    # Phase 4 : Trahison de Clotaire
        


    def clotaire_mouvement(hero):

        console.print("\n[bold red]=== Phase 4 : Avancée de Clotaire (Trahison) ===[/bold red]")

        console.print(
            "À mi-chemin, Clotaire avance de 3 cases, réduisant à zéro la marge de mouvement du joueur suivant."
        )
        console.print("Garen (paniqué) : 'Hé ! Pourquoi t’avances autant ?!'")
        console.print("Clotaire (calme) : 'Je fais ce qui est nécessaire.'")
        console.print("Ayela (énervée) : 'Enfoiré.'")
        console.print("Archeon (souriant) : 'Rappel… attaquer un allié est interdit.'")
        
        console.print("\n[bold yellow]Les gargouilles avancent lentement, suivant l'élan de Clotaire.[/bold yellow]")
        console.print("Velm (observant les gargouilles) : 'Oh, elles ont l’air de t’apprécier, Clotaire. Peut-être qu’elles vont t’escorter jusqu’à la sortie.'")
        console.print("Kael (serrant les poings) : 'Il nous ralentit volontairement. C’est évident.'")
        console.print("Brandio (fixant les gargouilles) : 'Les statues ne plaisantent pas. Elles avancent chaque fois qu’il le fait.'")
        console.print("Ayela (les yeux rivés sur les dalles) : 'On va finir par se faire coincer à ce rythme…'")
        console.print("Garen (frustré) : 'Pourquoi tu fais ça ? On est censés avancer ensemble !'")
        console.print("Clotaire (légèrement amusé) : 'Je suis ici pour gagner. Pas pour tenir la main de tout le monde.'")
        console.print("Velm (murmurant à Kael) : 'Je commence à l’apprécier, ce Garen. Il comprend le jeu.'")
        console.print("Kael (à Velm) : 'Touche pas au paysan !?'")
        console.print("Velm (souriant) : 'Il joue pour nous. Ça me plaît.'")

        console.print("\n[bold]Les gargouilles atteignent presque votre rangée.[/bold]")
        console.print("Ayela (nerveuse) : 'Si elles avancent encore, quelqu’un va y passer…'")  
        console.print("Garen (soupirant) : 'On doit avancer vite… avant qu’il soit trop tard. La dalle rouge ! Elle est la !'")
        
        console.print("Aldric (qui fait face a une gargouille et prend son épée) Degage ! (La gargouille fut tranchée en deux sans broncher)")
        console.print("Clotaire : Pfiouuu ! Il rigole pas le blondinet ")
        console.print("Kael : Pas mal...")
        
        console.print("Archeon : hm c'est presque trop simple pour toi hein ? pas vrai Aldric (pensa t'il)")

    clotaire_mouvement(hero)


    def clotare_reaction(hero):

        console.print("\n[bold yellow]=== Réaction d'Aldric ===[/bold yellow]")

        choix_reaction = Dialogue(
            "Comment réagissez-vous face à Clotaire ?",
            [
             {
                    "text": "Intervenir (forcer Clotaire à reculer).",
                    "consequence": lambda h: [
                        console.print("Clotaire recule d'une case à contrecœur."),
                        console.print("Clotaire (agacé) : 'Tss... Fais comme tu veux.'"),
                        console.print("Kael (croisant les bras, satisfait) : 'Enfin… Quelqu’un qui sait s’imposer.'"),
                        console.print("Ayela (souriant légèrement) : 'On avance ensemble ou pas du tout.'"),
                        console.print("Velm (ricanant doucement) : 'Toujours en train de jouer les héros, hein Aldric ?'"),
                        console.print("Brandio (calme, observant) : 'Ce jeu commence à durer trop longtemps.'"),
                        h.get_relation("Clotaire").adjust_score(-5),
                        h.get_relation("Kael").adjust_score(+10)
                    ]
                },
                {
                    "text": "Laisser faire.",
                    "consequence": lambda h: [
                        console.print("Kael (furieux) : 'Tu le laisses vraiment faire ça ?'"),
                        console.print("Garen (fronçant les sourcils) : 'On risque de perdre à ce rythme…'"),
                        console.print("Ayela (regard inquiet) : 'Les gargouilles ne nous attendront pas…'"),
                        console.print("Clotaire (avec un sourire en coin) : 'Je fais avancer le jeu, c’est tout.'"),
                        console.print("Velm (haussement d’épaules) : 'Un jeu dangereux… Mais intéressant.'"),
                        h.get_relation("Kael").adjust_score(-10),
                        h.get_relation("Clotaire").adjust_score(+5)
                    ]
                },
                {
                    "text": "Laisser Garen gérer.",
                    "consequence": lambda h: [
                        console.print("Garen (souriant) : 'Je vais m'en sortir.'"),
                        console.print("[bold green]Garen avance et atteint la dalle rouge ![/bold green]"),
                        console.print("Ayela (le rejoignant rapidement) : 'Bien joué, Garen. On est passés.'"),
                        console.print("Kael (restant derrière) : 'Tch… Il nous laisse tous en plan.'"),
                        console.print("Velm (souriant) : 'C’est chacun pour soi. Vous le savez.'"),
                        console.print("Brandio (immobile) : 'Il reste encore des dalles à franchir…'"),
                        console.print("[italic]Les autres participants restent bloqués, les gargouilles avançant lentement derrière eux.[/italic]"),
                        h.get_relation("Garen").adjust_score(+5)
                    ]
                }
            ]
        )
        choix_reaction.display(hero)
    clotare_reaction(hero)
    
    console.print("\n[bold green]=== Garen et Ayela atteignent la dalle rouge ===[/bold green]")
    console.print(
    "[italic]Garen est le premier à franchir une dalle rouge, suivi de près par Ayela. "
    "Ils se tiennent à l'écart, observant silencieusement les autres encore sur le damier.[/italic]"
    )
    
    console.print("Archeon : Garen et Ayela qualifiés !")
    console.print("Ayela (calme, mais inquiète) : 'Ils doivent se dépêcher…'")  
    console.print("Garen (croisant les bras) : 'Ils vont s'en sortir. Aldric sait ce qu'il fait.'")
    console.print("Kael (grommelant) : 'J’espère que tu as raison…'")

# Ambiance - Tension dans la salle
    
    console.print(
    "[italic]Dans l'ombre, les autres participants, spectateurs silencieux, observent avec nervosité. "
    "Leur regard oscille entre les gargouilles de bronze, immobiles mais menaçantes, et les joueurs encore coincés sur le plateau. "
    "Certains serrent les poings, d'autres échangent des murmures étouffés. Le poids de la tension semble étouffer la pièce, "
    "comme si le moindre son pouvait réveiller une force tapie dans l'obscurité.[/italic]"
    )
    console.print(
    "Un participant à l’arrière recule d’un pas, murmurant à son voisin : 'Ils n’y arriveront pas tous… C’est impossible.'"
    )
    console.print("Une femme, les bras croisés, fixe Kael et Aldric : 'On verra s'ils sont vraiment aussi bons qu'ils en ont l'air.'")
    console.print(
    "[italic]Les flammes violettes des torches vacillent faiblement, projetant des ombres mouvantes sur les murs sculptés. "
    "Chaque craquement de pierre sous le pied d'une gargouille résonne comme une menace silencieuse.[/italic]"
    )

# Archeon observe depuis la passerelle
    console.print("\n[bold cyan]=== Focus : Archeon ===[/bold cyan]")
    console.print(
    "[italic]Depuis la passerelle en hauteur, Archeon observe, appuyé nonchalamment contre la rambarde de pierre. "
    "Ses yeux suivent les mouvements des joueurs, mais son regard semble s'attarder plus longuement sur Aldric et Clotaire. "
    "Un sourire discret étire ses lèvres, presque imperceptible, tandis qu'il tapote lentement ses doigts contre le rebord de la rambarde.[/italic]"
    )      
    console.print(
    "Archeon (murmurant, pour lui-même) : 'Ce groupe est intéressant… Un grand cru. "
    "Ils possèdent cette étincelle que je n'avais pas vue depuis longtemps.'"
    )   
    console.print("[italic]Son regard s’assombrit légèrement lorsqu’il aperçoit Kael hésiter avant d’avancer. "
              "Il se redresse doucement, croisant les bras avec intérêt.[/italic]")

    # Les gargouilles continuent leur progression
    console.print("\n[bold red]=== Les gargouilles continuent d'avancer ===[/bold red]")
    console.print(
    "[italic]Les statues de bronze progressent lentement sur les dalles, réduisant l’espace entre elles et les participants. "
    "Les regards se tournent vers Clotaire, qui semble toujours aussi détendu malgré la menace imminente.[/italic]"
    )
    console.print("Clotaire (avec un sourire) : 'Allons-y. Plus vite on termine, mieux c'est.'")

    
    def clotare_sacrifice(hero):

        console.print("\n[bold red]=== Phase 5 : Sacrifice Imminent ===[/bold red]")
        console.print(
            "Une gargouille atteint la dalle rouge. Archeon observe en silence.\n"
            "Archeon (froidement) : 'Un joueur doit être sacrifié. Qui sera-t-il ?'"
        )

        console.print("Tous les regards se tournent vers Clotaire.")
        console.print("Aldric (prêt à dégainer sa lame) : 'Toi.'")

        # Choix du joueur pour le sacrifice
        choix_sacrifice = Dialogue(
            "Qui allez-vous sacrifier ?",
            [
                {
                    "text": "Sacrifier Velm .",
                    "consequence": lambda h: [
                        console.print("[bold red]Velm se fige, un rictus de défi sur les lèvres alors que la lumière de la gargouille l'engloutit.[/bold red]"),
                        console.print("Velm (souriant à Clotaire) : 'Tu feras mieux que moi, hein ?... Je croyais qu'on irait ensemble.'"),
                        console.print("Clotaire (silence, puis froidement) : 'Je ferai ce qu'il faut... pour toi aussi.' (Clotaire -50 relation)"),
                        console.print("Brandio (la voix tremblante) : 'Tu… tu aurais pu le sauver…'(Brandio -50 relation )"),
                        console.print("Aldric : 'C'est vous ou nous !'"),
                        console.print("Kael : 'Bien dit je commence presque a peut etre t'apprecier !'"),
                        console.print("Clotaire (en detruisant une gargouille) 'Enfant de putain !!! JE VAIS TE SAIGNER !'"),
                        hero.get_relation("Clotaire").adjust_score(-50),
                        hero.get_relation("Brandio").adjust_score(-50),
                        hero.remove_relation("Velm")
                    ]
                },
                {
                    "text": "Proposer Brandio comme sacrifice.",
                    "consequence": lambda h: [
                        console.print("[bold red]Brandio hoche la tête en silence et s'avance.[/bold red]"),
                        console.print("Brandio : 'C'est pas la fin que j'imaginais… désolé Clotaire, mais ca sent la fin du voyage...'"),
                        console.print("Velm (furieux) : 'Tu pouvais choisir quelqu'un d'autre, Aldric! Pourquoi lui ?'"),
                        console.print("Clotaire (l'air sombre) : 'Brandio...NOOOON !!'"),
                        console.print("[italic]'Brandio se fige et disparaît, ne laissant qu'une silhouette pétrifiée derrière lui.'[/italic]"),
                        console.print("Aldric : 'Tu aurait prefere que ca sois toi ?' !"),
                        console.print("Clotaire : 'Fumier...OUAAAAAAAAAH !' (Clotaire et Velm -50)"),
                        hero.get_relation("Clotaire").adjust_score(-50),
                        hero.get_relation("Velm").adjust_score(-50),
                        hero.remove_relation("Brandio")
                    ]
                }
            ]
        )
        choix_sacrifice.display(hero)
    clotare_sacrifice(hero)
    
    console.print(
        "[italic]Le sacrifice est accompli. La gargouille recule lentement, reprenant sa position d'origine. "
        "Les flammes violettes des torches vacillent, marquant la fin de cette épreuve.[/italic]"
    )
    console.print(
        "Archeon (souriant) : 'Bravo. Vous avez respecté les règles… et payé le prix nécessaire.'"
    )
    console.print("Clotaire détourne le regard, impassible. Velm (ou Brando) reste figé, le visage dur, fixant la silhouette pétrifiée de son camarade.")
    console.print(
        "Ayela (voix basse, la gorge serrée) : 'Nous devions continuer… mais pas comme ça…'"
    )
    console.print("Garen (sombre) : 'Il est mort pour rien…mais c'etait eux ou Kael alors..'")
    
    console.print("Emphyr : 'Il connaissait les règles de la tour ! n'ai point de pitié pour lui...'")
    
    console.print("Garen : 'Mais c'etait ton ami !'")
    
    console.print("Emphyr : 'Mon ami ? oh non je le connaissait pas avant aujourd'hui je me suis simplement associée a Clotaire pour progresser.'")
    
    console.print("Garen : 'Je..je vois...'")
    
    console.print("Emphyr : Toi tu t'est bien mieux debrouillé qu'eux ! (Emphyr fit un clin d'oeil a Garen qui rougie) tu est mignon avec tes bottes trop grandes !")
    
    console.print("Garen : 'Hm...'")
    
    

        

    def cloture_jeu(hero):

        console.print("\n[bold cyan]=== Clôture du Jeu des Dalles Cryptiques ===[/bold cyan]")

        console.print(
        "[italic]Lentement, la pression retombe alors qu'Aldric, suivi de ses alliés, franchit la dernière dalle rouge. "
        "Un léger frisson parcourt l'échine de chacun tandis que l'éclat spectral du plateau s'estompe, signe que leur épreuve est terminée.[/italic]"
    )

        console.print(
        "Archeon, toujours perché sur sa passerelle, les observe avec ce sourire indéchiffrable, un mélange d'intrigue et de satisfaction.\n"
        "Archeon (d'une voix résonnante) : 'Félicitations. Vous faites partie des rares à avoir franchi cette étape. "
        "Mais ne vous réjouissez pas trop vite. Ce n'était qu'un jeu... et la tour n'a pas encore révélé toutes ses cartes.'"
    )

     # Description de l'arrivée des personnages
        console.print("\n[bold]Aldric s'arrête, regardant derrière lui.[/bold]")

        if hero.get_relation("Kael"):
            console.print("Kael (le souffle court) : 'On l'a fait… Enfin. J'espère qu'ils s'en sortiront aussi.'")
        else:
            console.print("Ayela (à voix basse) : 'Il aurait dû être là…'")

        if hero.get_relation("Velm"):
            console.print("Velm (calmement, observant les autres joueurs) : 'La partie continue pour eux. Ils devraient faire attention à leurs mouvements.'")
    
        if hero.get_relation("Brandio"):
            console.print("Brandio (croisant les bras) : 'Peu importe. Ce qui compte, c'est que nous soyons ici, pas eux.'")
    
        console.print("Clotaire (haussant les épaules) : 'Ils apprendront… Ou ils tomberont. C'est ainsi que fonctionne la tour.'")

    # Ambiance de la salle et des participants
        console.print(
        "\n[italic]Autour d'eux, les autres participants continuent de progresser prudemment sur le plateau, certains suivant les traces d'Aldric, "
        "d'autres formant leurs propres équipes. Chaque mouvement semble pesé, chaque dalle foulée porte le poids du doute.[/italic]"
    )

        console.print("Garen (de l'autre côté, observant depuis la dalle rouge) : 'Ils ont compris la leçon. Mieux vaut tard que jamais…'")
        console.print("Ayela (regardant au loin) : 'Espérons qu'ils aient le temps de la mettre en pratique.'")

        console.print(
            "[italic]Finalement, après des manœuvres et des sacrifices, seize participants atteignent la dalle rouge. "
            "Les autres sont pétrifiés ou exécutés par Archeon.[/italic]"
        )
        console.print(
            "Archeon (souriant) : 'Bravo. Ceux qui restent peuvent avancer... Les autres serviront de leçon.'"
        )

        console.print("La bande d'Aldric avancent vers la porte suivante, la mort derrière eux.")
        console.print("Archeon (calme) : 'Continuez d'avancer... ou mourrez en route.'")

        console.print(
            "\nLe claquement sourd de la dernière dalle résonne. Seize participants tiennent debout, la sueur coulant sur leurs fronts. "
            "Les perdants sont transformés en statues de pierre, figés dans la panique.\n"
        )
        console.print("Garen (voix tremblante) : 'Ils... ils sont vraiment tous...'")
        console.print("Ayela (voix basse) : 'On n'aurait rien pu faire.'")

    
        console.print("Kael (murmure) : 'C'est une erreur de l'avoir laissé s'en sortir...'")
       
        console.print("Ayela (jetant un regard triste) : 'Kael aurait dû survivre.'")

 
    cloture_jeu(hero)


    def clotare_reaction_finale(hero):

        console.print("\n[bold yellow]=== Après le Jeu : Clotaire ===[/bold yellow]")

        choix_reaction_clotaire = Dialogue(
            "Comment réagissez-vous face à Clotaire après le jeu ?",
            [
                {
                    "text": "Ignorer Clotaire et continuer en silence.",
                    "consequence": lambda h: [
                        console.print("Vous ignorez Clotaire et poursuivez votre chemin."),
                        console.print("Kael (marmonnant, mécontent) : 'Tch… Laisser passer ça… Mauvaise idée.'(Kael -5)"),
                        console.print("Garen (à voix basse) : 'Parfois, il vaut mieux éviter l'escalade.'(Garen +10)"),
                        console.print("Ayela (regardant Clotaire du coin de l'œil) : 'Il ne s'arrêtera pas là. Je le sens…'(Ayela +5)"),
                        h.get_relation("Garen").adjust_score(+5),
                        h.get_relation("Ayela").adjust_score(+5),
                        h.get_relation("Kael").adjust_score(-5) 
                    ]
                },
                {
                    "text": "Confronter Clotaire discrètement.",
                    "consequence": lambda h: [
                        console.print("Kael (approbateur) : 'Enfin, quelqu'un le remet à sa place.'(Kael +10)"),
                        console.print("Ayela (soupirant de soulagement) : 'Je commençais à me demander si tu comptais le laisser faire…'"),
                        console.print("Clotaire (légèrement amusé) : 'Tant d'efforts pour me défier en silence… Intéressant.'(Clotaire -5)"),
                        h.get_relation("Kael").adjust_score(+10),
                        h.get_relation("Clotaire").adjust_score(-5)
                    ]
                },
                {
                    "text": "Menacer ouvertement Clotaire.",
                    "consequence": lambda h: [
                        console.print("[bold red]Clotaire vous dévisage, un sourire froid aux lèvres.[/bold red]"),
                        console.print("Clotaire (calme) : 'Tente ta chance, Aldric. Je suis prêt.'(Clotaire -10)"),
                        console.print("Kael (croisant les bras) : 'Je suis avec toi, Aldric. Ce type nous ralentira un jour.'(Kael +15)"),
                        console.print("Garen (fronçant les sourcils) : 'On n'a pas besoin de ça maintenant…'"),
                        console.print("Ayela (visiblement mal à l'aise) : 'Vous deux, calmez-vous. On vient de survivre de peu.'(Ayela -5)"),
                        h.get_relation("Kael").adjust_score(+15) ,
                        h.get_relation("Clotaire").adjust_score(-10),
                        h.get_relation("Ayela").adjust_score(-5)
                    ]
                }
            ]
        )
        choix_reaction_clotaire.display(hero)
    clotare_reaction_finale(hero)

    console.print(
        "\n[italic]Vous franchissez enfin la porte, laissant derrière vous les corps de pierre des perdants. "
        "Les survivants avancent, mais l'ombre du sacrifice pèse encore.[/italic]"
        )
    
    console.print("Emphyr : '(en caressant l'epaule de Clotaire) : Sois pas si tendu...on est presque a l'étage 7 !'")
    console.print("Clotaire : 'Oui...il faut garder ses types a l'oeil...ils peuvent nous causer des problemes'")
    if hero.get_relation("Velm"):
        console.print("Velm : Oui on va venger Brando...je te le promet")
    if hero.get_relation("Brandio"):
        console.print("Brandio : Velm...Clotaire...Velm etait notre ami...")
    console.print("Cloraire (avec un sourire determiné) : Patience...je sens que notre occasion se presentera plus tôt qu'on le pense...")
    
    console.print("[bold]Il reste 16 participants.[/bold]")
    
    game_menu.display()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def floor6(hero, game_menu):
    from rich.console import Console
    console = Console()

    console.print("\n[bold cyan]=== Étage 6 : Les Salles des Épreuves Élémentaires ===[/bold cyan]")

    # Narration approfondie
    console.print(
        "[italic]Les marches du sixième étage semblent plus longues, plus lourdes. Chaque pas fait craquer les vieilles pierres "
        "comme si elles se plaignaient de votre présence. Le silence qui vous entoure devient presque assourdissant.[/italic]"
    )
    console.print(
        "[italic]Lorsque vous atteignez enfin la porte massive, un courant d’air glacé s’en échappe, "
        "comme si l’étage vous jaugeait avant de vous laisser entrer. Derrière la porte, une vaste salle circulaire s’étend. "
        "Au centre, une stèle de pierre noire trône, pulsant faiblement sous la lueur des torches accrochées au mur.[/italic]"
    )

    # Premières réactions
    console.print("\nKael (croisant les bras, appuyé contre un pilier) : 'Encore une stèle… À ce rythme, je vais finir archéologue.'")
    console.print("Ayela (plissant les yeux) : 'Ne plaisante pas. Cette fois, ça sent vraiment mauvais.'")
    console.print("Garen (fixant la stèle) : 'Elle… regarde à travers nous. Vous ne trouvez pas ?'")

    # Présence de Clotaire et ses compagnons (Emphyr ajoutée)
    console.print(
        "[italic]Clotaire se tient un peu à l’écart avec le survivant de la salle précédente, Emphyr se tient aussi près de lui."
        "Un vide tangible semble hanter leur groupe, le poids d’une perte récente encore palpable.[/italic]"
    )

    if hero.get_relation("Velm"):
        console.print("Velm (à Clotaire, à voix basse) : 'Quatre équipes… On va être séparés. J'espère rester en vie cette fois…'") 
        console.print("Emphyr (glissant un regard vers Velm) : '[italic]On s'en sortira, Velm. Ne t'inquiète pas.[/italic]'")
    if hero.get_relation("Brandio"):
        console.print("Brandio (ricane) : 'Quatre équipes ? Ça tombe bien, il reste moins de monde pour nous ralentir. Pas vrai, Clotaire ?'")  
        console.print("Emphyr (regard doux mais ferme) : '[italic]Brandio… Velm méritait mieux que ça.[/italic]'")
        console.print("Brandio (haussant les épaules) : 'Mieux ou pas, il est plus là.'")

    # Activation de la stèle
    console.print("\n[bold yellow]=== La Stèle s'active ===[/bold yellow]")
    console.print(
        "[italic]Un frisson traverse la pièce lorsque les runes de la stèle s’animent. Elles s’élèvent, tourbillonnent, "
        "avant de se graver lentement dans l’air, projetant une lumière étrange sur les visages attentifs.[/italic]"
    )

    console.print(
        "Stèle (inscription gravée) : [bold magenta]'Quatre chemins. Quatre épreuves. Quatre équipes. "
        "L’unité seule triomphera des éléments. L’échec entraînera la chute.'[/bold magenta]"
    )

    console.print("Kael (sifflant) : 'Ah, enfin un peu de mystère… Je commençais à m'ennuyer.'")
    console.print("Ayela (chuchotant, tendue) : 'Ce n'est pas un jeu, Kael…'")

    # Lignes lumineuses au sol
    console.print(
        "[italic]Soudain, des lignes dorées s’étendent au sol, formant quatre chemins distincts. "
        "À l’extrémité de chaque chemin, une porte se matérialise, marquée d’un symbole élémentaire : "
        "Feu, Air, Terre, Eau.[/italic]"
    )

    # Description des portes
    console.print(
        "[bold red]Salle du Feu :[/bold red] [italic]Des flammes dansent derrière la porte. La chaleur vous parvient déjà, oppressante.[/italic]\n"
        "[bold cyan]Salle de l'Air :[/bold cyan] [italic]Un vent glacial s’échappe des interstices, murmurant des sons incompréhensibles.[/italic]\n"
        "[bold green]Salle de la Terre :[/bold green] [italic]De fines racines serpentent autour de la porte, comme si elle était vivante.[/italic]\n"
        "[bold blue]Salle de l’Eau :[/bold blue] [italic]Une fine brume glisse sous la porte, rafraîchissant l’air ambiant.[/italic]"
    )

    # Répartition des équipes (ajout de tensions et interactions)
    console.print("\n[bold green]=== Répartition des équipes ===[/bold green]")

    console.print(
        "[italic]Une énergie invisible vous attire tous vers les chemins. Vous ressentez une étrange résistance, "
        "comme si la Tour elle-même décidait de la composition des groupes.[/italic]"
    )
    console.print("Kael (plaisantant) : 'Laissez-moi deviner… Je suis condamné à l’Air. Un symbole.'")
    console.print("Garen (glissant un regard vers Kael) : 'Au moins, tu ne risques pas de fondre dans la salle du Feu.'")

    console.print(
        "[italic]Vous sentez vos pas vous guider vers la salle du Feu. Ayela se tient à vos côtés, l'arc en main. "
        "Clotaire s'arrête devant la porte de la salle de l'Air, Emphyr à ses côtés.[/italic]"
    )
    
    console.print("Emphyr (calme, regardant la porte de l’Air) : '[italic]Peut-être qu'il est temps que certains d'entre nous apprennent à s'entraider…[/italic]'")
    console.print("Clotaire (esquissant un sourire en coin) : 'L'entraide… Un mot qui a tué Velm, non ?'")
    console.print("Emphyr (le regard perçant) : '[italic]Non. C'est l'orgueil qui l'a tué.[/italic]'")

    gallius = Character("Gallius", "Un jeune garçon discret et agile, maniant deux dagues avec une précision redoutable.", "garçon", "allié")
    hero.add_relation(gallius, "Neutre")

    console.print("[italic]Un jeune garçon se tient près de l’entrée de la salle, le dos appuyé contre le mur. "
              "Ses cheveux noirs retombent en mèches désordonnées, et ses yeux perçants scrutent la pièce avec calme.[/italic]")
    console.print("Gallius (calme) : 'Feu, hein… Ça me va.'")
    console.print("[italic]Vous remarquez qu’il porte des dagues croisées sur son dos et des vêtements usés mais pratiques, typiques des mercenaires des régions du sud.[/italic]")

    console.print("Ayela (regarde la porte) : 'On va vraiment entrer là-dedans ?'")
    console.print("Aldric (calme) : 'On n’a pas le choix.'")
    console.print("Gallius (à voix basse) : 'Feu… Ça me convient.'")
    console.print("Ayela : 'Qui est tu aufait ? Tu est si jeune...comme a tu fait pour survivre aussi loin ?'")
    console.print("Gallius : 'Gallius...Je suis rapide...Invisible...(dit il en placa sa lame sous la gorge d'Ayela juste avant de la retirer)'")
    console.print("Ayela : 'Heeee fait pas ca...'")
    
    console.print("Garen : 'Aldric ! Tache de survivre....Toi aussi Ayela...'")
    
    console.print("Aldric : 'Promis Garen ca vous pour vous aussi !'")
    

    console.print("[italic]Un bruit sourd résonne lorsque les portes se referment derrière chaque groupe. "
                  "L’épreuve commence.[/italic]")
    
    def floor6_fire(hero):
        from rich.console import Console
        console = Console()

        console.print("\n[bold red]=== Salle du Feu : L'Esprit Brûlant ===[/bold red]")

    # Narration d'entrée
        console.print(
        "[italic]La porte claque violemment derrière vous, coupant toute possibilité de retour. "
        "L’air brûlant de la salle vous frappe de plein fouet, comme si chaque respiration enflammait vos poumons. "
        "Des gerbes de flammes dansent autour de vous, illuminant brièvement les visages crispés de vos compagnons.[/italic]"
    )
    
        console.print("Ayela (s’essuyant le front rapidement) : 'On vient à peine d’entrer et je sens déjà mes vêtements coller à ma peau…'")
        console.print("Gallius (calme, observant la pièce) : 'Bienvenue en enfer. L’épreuve du feu… Je m’attendais à pire.'")

        if hero.get_relation("Velm"):
            console.print("Velm (fixant les flammes avec amertume) : '[italic](murmure)[/italic] Il aurait dû être là…' ")
            console.print("Velm (lourdement) : 'Tu sais, Aldric… Chaque seconde passé avec toi est une insulte à Brandio.'")
            console.print("Velm (détournant à peine les yeux des flammes) : 'Tu aurais pu sacrifié cet imbécile de Kael...!'")
            console.print("Aldric : 'Et toi aurais sacrifié Brandio ou Clotaire pour sauver mon équipier si tu avais etait a ma place ?'")
            console.print("Velm : 'Je...tsss Brandio voulait sauver sa soeur...maintenant...elle va mourir...on devait voyager avec elle ! Voir le monde !'")
            console.print("Aldric : 'Désolé...on a tous un but ici...je devait faire un choix...La tour est cruel et tu le sais...fait ton deuil'")

        if hero.get_relation("Brandio"):
            console.print("Brandio (serrant les poings) : '[italic](voix basse)[/italic] Velm n’aurait jamais hésité…'")
            console.print("Brandio (fixant Aldric) : 'C’est toi qui as choisi, Aldric. Ne l’oublie jamais.'")
            console.print("Brandio (amèrement) : 'On avance… Mais cette foutue tour prendra son dû un jour. Peut-être même avant la fin de cet étage.'")
            console.print("Brandio (détournant à peine les yeux des flammes) : 'Tu aurais pu sacrifié cet imbécile de noble...!'")
            console.print("Aldric : 'Et toi aurais sacrifié Velm ou Brandio pour sauver mon equipier si tu avais etait à ma place ?'")
            console.print("Brandio : 'Velm etait un petit con...mais il...il...On vient des bas fonds d'Austravia ! On devait s'offrit une autre vie avec lui et Clotaire !'")
            console.print("Aldric : 'Désolé...on a tous un but ici...je devait faire un choix...La tour est cruel et tu le sais...fait ton deuil'")

        console.print("[italic]Le groupe avance lentement à travers la salle, chaque pas résonnant sur les dalles brûlantes. "
                  "L’air semble vibrer de manière étrange, comme si quelque chose d’ancien attendait de se manifester.[/italic]")

    # Apparition du Gardien de Flamme
        console.print(
        "[italic]Alors que vous atteignez le centre de la pièce, une forme titanesque se détache des flammes. "
        "Elle s'élève, ses traits flous et instables, entièrement composée de flammes noires et pourpres. "
        "Son torse laisse apparaître par intermittence un cœur brillant, pulsant à travers les flammes tourbillonnantes.[/italic]"
        )

        console.print("Ayela (à voix basse, bandant son arc) : 'C’est… vivant, non ?'")
        console.print("Gallius (impassible, prêtant attention à la créature) : 'Vivant ou non, peu importe. Ça bloque notre chemin.'")

        if hero.get_relation("Velm"):
            console.print("Velm (voix froide) : 'S’il était là… il aurait chargé sans hésiter. Contrairement à toi, Aldric.'")
            console.print("Velm (le regard fixe) : 'Je ne vais pas mourir pour toi. Pas après ce que tu as fait.'")

        if hero.get_relation("Brandio"):
            console.print("Brandio (croisant les bras, mordant ses mots) : 'Velm aurait déjà foncé, tête baissée… Et il serait mort.'")
            console.print("Brandio (grinçant des dents) : 'Cette fois, c’est moi qui choisis. Et je t’assure que je ne vais pas couvrir tes erreurs, Aldric.'")

        console.print("Aldric (froidement) : 'Pour l’instant, concentre-toi. On doit survivre à ça d’abord.'")

    # Début du combat
        console.print("\n[bold red]Gardien de Flamme : 'Vous osez troubler mon sommeil… Il y'aura pas de repis...je prendrais mon offrande...'[/bold red]")

    # Phase 1 - Choix du premier mouvement
        combat_1 = Dialogue(
            "La créature élève un bras et prépare une attaque. Que faites-vous ?",
            [
                {
                    "text": "Attaque directe (Aldric mène l'assaut).",
                    "consequence": lambda h: [
                        console.print("Aldric s'élance, mais la chaleur intense le repousse brutalement. (-15 PV Aldric)"),
                        console.print("Gallius (se plaçant devant Aldric) : 'Recule. C'est suicidaire.'"),
                        hero.adjust_health(-15),
                        hero.get_relation("Gallius").adjust_score(-5)
                ] + ([
                        console.print("Velm (sombre) : 'Exactement ce que tu as fait à Brandio. Tu n'a pas hésité...' (-5 relation Velm)"),
                        hero.get_relation("Velm").adjust_score(-5)
                ]   if hero.get_relation("Velm") else []) + ([
                        console.print("Brandio (ricanant) : 'Continue, Aldric… Peut-être que cette fois, ce sera toi.' (+10 relation Brandio)"),
                        hero.get_relation("Brandio").adjust_score(+10)
                ]   if hero.get_relation("Brandio") else [])
            },
            {
                    "text": "Observer et attendre une faille.",
                    "consequence": lambda h: [
                        console.print("[italic]Aldric observe attentivement la créature et remarque que son cœur s'illumine à intervalles réguliers.[/italic]"),
                        console.print("Aldric (calme) : 'Attendez. Son cœur. Il y a une ouverture…'")
            ] + ([
                        console.print("Velm (grommelant) : 'On n'aurait pas eu besoin d'attendre si Brandio était là…' (+10 relation Velm)"),
                        hero.get_relation("Velm").adjust_score(+10)
                ] if hero.get_relation("Velm") else []) + ([
                        console.print("Brandio (grinçant des dents) : 'Velm aurait frappé sans réfléchir. C'est pour ça qu'il est mort…' (-5 relation Brandio)"),
                        hero.get_relation("Brandio").adjust_score(-5)
                ] if hero.get_relation("Brandio") else [])
            },
            {
                    "text": "Demander à Ayela de tirer.",
                    "consequence": lambda h: [
                        console.print("[italic]Ayela tire une flèche, mais elle traverse les flammes sans causer de dommage visible.[/italic]"),
                        console.print("Ayela (frustrée) : 'C'était pourtant bien visé…'")
            ] + ([
                        console.print("Velm (haussant les épaules) : 'Ça vaut toujours mieux que de foncer sans réfléchir. Continue.' (+5 relation Velm)"),
                        hero.get_relation("Velm").adjust_score(+5)
                    ] if hero.get_relation("Velm") else []) + ([
                        console.print("Brandio (sarcastique) : 'Tu veux pas essayer un lance-pierre, Ayela ? Je deteste les archers...' (-5 relation Brandio)"),
                        hero.get_relation("Brandio").adjust_score(-5),
                        hero.get_relation("Ayela").adjust_score(+5)
                    ] if hero.get_relation("Brandio") else [])
            }
            ]
        )
        combat_1.display(hero)

    # Phase 2 - Riposte du gardien
        combat_2 = Dialogue(
    "Le Gardien lève lentement les bras. Des flammes sombres s'amassent au-dessus de lui avant de s'abattre en une vague dévastatrice. Que faites-vous ?",
    [
        {
            "text": "Esquiver.",
            "consequence": lambda h: [
                console.print("[italic]Aldric s'élance sur le côté, entraînant Ayela par le bras. Gallius se faufile habilement entre les flammes, ses dagues prêtes à frapper.[/italic]"),
                console.print("Aucune blessure n'est infligée."),
            ] + ([
                console.print("Velm (crachant sur le sol, s'écartant des flammes) : 'T'es rapide… au moins pour sauver ta peau.'"),
                console.print("Gallius (calme, jetant un regard à Velm) : 'Tu devrais suivre son exemple. La tour ne pardonne pas la lenteur.'"),
                console.print("Velm (grinçant des dents) : 'Je n'ai pas besoin de conseils. Surtout pas de sa part.'"),
            ] if hero.get_relation("Velm") else []) + ([
                console.print("Brandio (murmurant en évitant de justesse l'attaque) : 'Velm aurait couru droit dans le feu… Et il aurait survécu, lui.'"),
                console.print("Gallius (calme) : 'Et pourtant, c'est lui qui n'est pas là aujourd'hui. Reste en vie, Brandio.'"),
                console.print("Brandio (sombre) : 'Je suis là… mais à quel prix ?'"),
            ] if hero.get_relation("Brandio") else [])
        },
        {
            "text": "Bloquer avec votre manteau.",
            "consequence": lambda h: [
                console.print("[italic]Aldric lève son manteau, l'utilisant comme un bouclier contre les flammes. Une partie de la vague est déviée, mais la chaleur brûle sa peau. (-3 PV Aldric)[/italic]"),
                hero.adjust_health(-3),
                console.print("Ayela (soulagée) : 'Merci Aldric…'(Ayela +5)"),
                hero.get_relation("Ayela").adjust_score(+5)
            ] + ([
                console.print("Velm (regardant Aldric) : '[italic](murmure)[/italic] Ça n'aurait pas suffi pour sauver Brandio…'"),
                console.print("Aldric (gardant son calme) : 'Je fais ce que je peux. C'est tout ce que nous avons ici.'"),
                console.print("Velm (détournant les yeux) : 'Ouais… Je vois ça.'"),
            ] if hero.get_relation("Velm") else []) + ([
                console.print("Brandio (à voix basse) : 'Tu prends des coups… Mais c'est trop tard pour Velm.'"),
                console.print("Aldric (fixant Brandio) : 'C'est pour que d'autres ne partent pas aussi. Je n'ai pas l'intention de refaire cette erreur.'"),
                console.print("Brandio (hésitant) : 'Hm… On verra bien.'"),
            ] if hero.get_relation("Brandio") else [])
        },
        {
            "text": "Contre-attaquer avec Gallius.",
            "consequence": lambda h: [
                console.print("[italic]Profitant d'une ouverture, Gallius bondit sous la vague et frappe la créature à la jambe. Des éclats de flammes s'envolent sous l'impact, révélant une plaie luisante. (+5 Gallius)[/italic]"),
                console.print("Gallius : 'Il saigne… du feu.'"),
                console.print("Aldric (serrant son épée) : '…Ce qui saigne...'(Gallius +5)"),
                console.print("Gallius : '...Peut mourir..'"),
                hero.get_relation("Gallius").adjust_score(+5)
            ] + ([
                console.print("Velm (inspirant profondément) : '…Il aurait aimé cette phrase, tu sais.'"),
                console.print("Aldric (doucement) : 'Hm alors butons cette engence en son honneur...'"),
                console.print("Velm (après une pause) : 'Je vais essayer de ne pas te ralentir. Pour lui. Mais ne crois pas que ça efface tout.'(Velm + 5)"),
                hero.get_relation("Velm").adjust_score(+5)
            ] if hero.get_relation("Velm") else []) + ([
                console.print("Brandio (croisant les bras, regardant Aldric) : 'Tsss… C'est bien beau les belles phrases. Mais Velm est mort. T'aurais pas dû hésiter à l'époque.'"),
                console.print("Gallius (froidement) : 'Et il sera pas le dernier si tu restes planté là.'"),
                console.print("Brandio (après un silence) : 'Ok… D'accord. Mais je fais ça pour moi, pas pour vous.'(Brandio +5)"),
                hero.get_relation("Brandio").adjust_score(+5)
            ] if hero.get_relation("Brandio") else [])
        }
    ]
)
        combat_2.display(hero)

    # Phase Finale - Attaque du cœur
        combat_3 = Dialogue(
    "Le cœur du gardien pulse violemment, irradiant une lumière aveuglante. La salle tremble, et la chaleur devient insoutenable. Il est temps d'agir. Que faites-vous ?",
    [
        {
            "text": "Aldric frappe directement le cœur.",
            "consequence": lambda h: [
                console.print("[italic]Aldric fonce, ignorant la chaleur brûlante qui envahit la pièce. Son épée s'enfonce profondément dans le cœur incandescent. La créature laisse échapper un dernier cri avant de s'effondrer dans un torrent de cendres.[/italic]"),
                console.print("Ayela (souffle de soulagement) : 'Tu es cinglé… mais c'était magnifique.'(Ayela +15)"),
                console.print("Gallius (léger sourire) : 'Direct, J'aime ca...'(Gallius +15)"),
                hero.get_relation("Ayela").adjust_score(+15),
                hero.get_relation("Gallius").adjust_score(+15)
            ] + ([
                console.print("Velm (hésitant) : '[italic](voix basse)[/italic] Je suppose que Brandio aurait approuvé ce genre de folie…'"),
                console.print("Aldric (l'essuyant son front) : 'Je ne cherche pas son approbation, Velm… Mais je suis sûr qu'il aurait voulu que tu sois là pour voir ça.'"),
                console.print("Velm (croisant les bras, détournant les yeux) : 'Ouais… Peut-être. Merci pour ça.'(Velm + 15)"),
                hero.get_relation("Velm").adjust_score(+15)
            ] if hero.get_relation("Velm") else []) + ([
                console.print("Brandio (fixant les cendres du gardien) : 'Velm aurait ri… Je crois qu'il te pardonnerait aussi.'"),
                console.print("Aldric (regardant Brandio) : 'C'est pas ce que je cherche. Mais ça compte.'"),
                console.print("Brandio (léger sourire) : 'C'est suffisant pour moi. On avance. Ahahah'(Brandio +15)"),
                hero.get_relation("Brandio").adjust_score(+15)
            ] if hero.get_relation("Brandio") else [])
        },
        {
            "text": "Ayela tire une flèche au cœur.",
            "consequence": lambda h: [
                console.print("[italic]Ayela recule de quelques pas, tend son arc avec précision et décoche une flèche éclatante. La flèche fend l'air et transperce le cœur du gardien, déclenchant une explosion de flammes. Aldric est projeté en arrière. (-20 PV Aldric)[/italic]"),
                console.print("Ayela (accourant vers Aldric) : 'Aldric ! Ça va ?'"),
                console.print("Aldric (se relevant péniblement) : 'Je suis vivant et c'est grâce a toi Ayela !'"),
                console.print("Ayela : 'Pas de quoi hihi ! (Ayela +25)'"),
                hero.adjust_health(-20),
                hero.get_relation("Ayela").adjust_score(+25)
            ] + ([
                console.print("Velm (observant Ayela) : '[italic](murmure)[/italic] Ça, c'est du tir.'"),
                console.print("Ayela (sourit faiblement) : 'Je m'entraîne depuis longtemps. Velm… Merci de reconnaître ça.'"),
                console.print("Velm (gêné) : 'Ne crois pas que c'est par sympathie. Mais… bon tir.'(Velm +10)"),
                hero.get_relation("Velm").adjust_score(+10)
            ] if hero.get_relation("Velm") else []) + ([
                console.print("Brandio (amusé) : 'Ah, cette fille est dangereuse… Je suppose que Velm aurait applaudi.'"),
                console.print("Ayela (faisant un clin d'œil) : 'Je prends ça comme un compliment.'(Brandio +10)"),
                hero.get_relation("Brandio").adjust_score(+10)
            ] if hero.get_relation("Brandio") else [])
        },
        {
            "text": "Gallius se hâte sur le cœur et donne une pluie de coups.",
            "consequence": lambda h: [
                console.print("[italic]Gallius bondit sans hésitation, ses dagues traçant des arcs lumineux autour du cœur du gardien. Les flammes s'éparpillent alors qu'il frappe sans relâche. Une fissure apparaît soudainement sur le cœur.[/italic]"),
                console.print("Gallius (grimaçant) : 'C'est maintenant ou jamais, Aldric !'(Gallius +20)"),
                hero.get_relation("Gallius").adjust_score(+20)
            ] + ([
                console.print("Gallius : 'Velm, ne reste pas planté là !'"),
                console.print("Velm (hésitant, puis fonçant) : 'Je suis pas aveugle !'"),
                console.print("[italic]Velm rejoint Aldric et enfonce sa lame dans la fissure. Ensemble, ils achèvent la créature dans une gerbe de flammes.[/italic]"),
                console.print("Velm (essoufflé, regardant Aldric) : '…Je suppose que t'es pas si mauvais. Pour aujourd'hui.'"),
                console.print("Aldric (lui tendant la main) : 'Tant que tu restes en vie.'"),
                console.print("Velm (après un silence, serre la main) : 'Pour Brandio… ouais.'(Velm +20)"),
                hero.get_relation("Velm").adjust_score(+20)
            ] if hero.get_relation("Velm") else []) + ([
                console.print("Gallius : 'Brandio, à toi de jouer !'"),
                console.print("Brandio (grinçant des dents) : 'J'arrive. Pas besoin de me presser.'"),
                console.print("[italic]Avec un cri rageur, Brandio enfonce sa lame profondément dans le cœur du gardien, aux côtés d'Aldric. La créature s'effondre sous leurs coups combinés.[/italic]"),
                console.print("Brandio (souriant) : 'C'est fini. Peut-être que Velm aurait aimé voir ça…'(Brandio +20)"),
                console.print("Aldric (calme) : 'Il a vu. À travers nous.'"),
                hero.get_relation("Brandio").adjust_score(+20)
            ] if hero.get_relation("Brandio") else [])
        }
    ]
)
        combat_3.display(hero)
    
    floor6_fire(hero)

   # Conclusion
    # Conclusion
    console.print("[italic]Alors que la créature s’effondre lentement, laissant derrière elle une gemme écarlate, "
              "un dernier rugissement s'élève du brasier mourant.[/italic]")

    if hero.get_relation("Velm"):
        console.print("[bold red]Velm s’avance prudemment vers la gemme, la ramassant du bout des doigts.[/bold red]")
        console.print("[italic]Un faible éclat rouge danse à sa surface. Velm la lève un instant à la lumière, "
                  "son regard perdu dans ses pensées.[/italic]")

    if hero.get_relation("Brandio"):
        console.print("[bold red]Brandio s’approche de la gemme écarlate, son sourire habituel effacé, laissant place à une gravité rare.[/bold red]")
        console.print("[italic]Il l’observe un moment, comme s’il voyait enfin quelque chose au-delà des murs de cette tour maudite.[/italic]")

    console.print("Gallius (sombre) : 'Hé… Ne tourne pas le dos à cette chose. Recule, lentement.'")

    if hero.get_relation("Velm"):
        console.print("[italic]Velm ne répond pas immédiatement. Il fixe la gemme, la serrant dans sa paume, "
                  "avant de se retourner lentement, faisant quelques pas vers Aldric.[/italic]")
        console.print("Velm (d’une voix rauque) : 'Tu sais… Peut-être que je t’en ai trop voulu.'")
        console.print("Velm (tendant la gemme à Aldric) : 'Brandio aurait sûrement voulu que je fasse la paix. Alors voilà… Je fais la paix.'")

    if hero.get_relation("Brandio"):
        console.print("[italic]Brandio fait tournoyer la gemme dans sa main, levant un sourcil vers Aldric.[/italic]")
        console.print("Brandio : 'Écoute, Aldric… Velm était un crétin, mais c’était mon crétin. Je crois que je comprends pourquoi tu as fait ce choix.'")
        console.print("Brandio (lui lançant doucement la gemme) : 'Tiens… T'est un bon Aldric, Va au bout...et veille sur Clotaire !'")

# Dernier sursaut du Gardien
    if hero.get_relation("Velm"):
        console.print("[bold red]Mais alors qu’il tend la gemme, une griffe noire surgit des cendres encore fumantes du gardien.[/bold red]")
        console.print("[italic]Trop tard pour réagir, la créature empoigne Velm, le soulevant dans les airs dans un cri de douleur.[/italic]")

    if hero.get_relation("Brandio"):
        console.print("[bold red]Une ultime flamme jaillit des cendres, enveloppant Brandio dans une explosion brutale.[/bold red]")
        console.print("[italic]Brandio se redresse un instant, un sourire fataliste aux lèvres, avant de disparaître dans le brasier.[/italic]")

    if hero.get_relation("Velm"):
        console.print("Velm (hurlant) : 'Aldric ! Attrape ça !' [italic](Il jette la gemme vers Aldric, juste avant que ses cris ne soient étouffés par la poigne du gardien.)[/italic]")

    if hero.get_relation("Brandio"):
        console.print("Brandio (en riant malgré les flammes) : 'Hé, Aldric… Garde ça précieusement. On dirait que j’vais devoir faire une petite sieste...adieu petit gars !.'")

# Suppression du personnage
    if hero.get_relation("Velm"):
        console.print("[italic]La créature tire sur Velm avec une force inhumaine. Son corps se disloque avant de retomber, sans vie, sur le sol noirci.[/italic]")
        
    elif hero.get_relation("Brandio"):
        console.print("[italic]Brandio disparaît dans une volée de cendres, son rire s’éteignant en même temps que les flammes autour de lui.[/italic]")
        

# Réactions des survivants
    console.print("Ayela (les larmes aux yeux) : 'Pourquoi faut-il toujours que quelqu’un…' [italic](Sa voix s’étrangle dans un sanglot qu’elle tente de cacher.)[/italic]")
    console.print("Aldric (fixant la gemme dans sa main) : 'Etait-ce la fameuse offrande de la créature...pauvre gars ! j'espere qu'il voyagerons ensemble la ou il sont...'")
    console.print("Ayela : 'Aldric...'")
    console.print("[italic]Aldric serre la gemme dans sa paume, son expression impassible masquant la lourdeur de la perte.[/italic]")

    console.print("Gallius (croisant les bras, fixant les cendres) : 'C’est la tour. Elle prend tout. Même ceux qui font la paix trop tard.'")
    console.print("[italic]Il détourne les yeux et s’approche de la porte, prêt à quitter cette salle funeste.[/italic]")

# Clôture de la scène
    console.print("Ayela (murmurant) : 'Ils ne devraient pas mourir comme ça…' [italic](Elle regarde Aldric, cherchant ses mots.)[/italic]")
    console.print("Aldric (d’un ton ferme) : 'Non… Mais on doit continuer. Il ne voudrait pas qu’on s’arrête ici.'")
    
    choix_confort = Dialogue(
        "[bold]Comment réagissez-vous face à Ayela ?[/bold]",
        [
            {
                "text": "Prendre Ayela dans ses bras pour la réconforter.",
                "consequence": lambda h: [
                    console.print("[italic]Aldric s'approche doucement et serre Ayela dans ses bras. "
                                 "Elle se crispe d'abord, puis finit par s'abandonner un instant, "
                                 "posant sa tête contre son épaule.[/italic]"),
                    console.print("Ayela (d’une voix tremblante) : 'Merci… J’en avais besoin.'"),
                    console.print("[italic]Elle reste ainsi quelques secondes, reprenant lentement ses esprits. "
                                 "Lorsqu’elle se recule, ses yeux sont plus fermes, plus décidés.[/italic]"),
                    console.print("Ayela (avec un léger sourire) : 'Tu es plus tendre que tu n’en as l’air…'(Ayela +30)"),
                    hero.get_relation("Ayela").adjust_score(+30)
                ]
            },
            {
                "text": "Tourner le dos à la salle et l’encourager à avancer.",
                "consequence": lambda h: [
                    console.print("[italic]Aldric détourne les yeux des cendres et avance vers la porte.[/italic]"),
                    console.print("Aldric (calmement, sans se retourner) : 'Viens, Ayela. On a déjà trop perdu de temps ici.'"),
                    console.print("[italic]Ayela essuie une larme discrète avant de le suivre en silence.[/italic]")
                ]
            }
        ]
    )
    choix_confort.display(hero)

    console.print("[italic]La porte de sortie s’ouvre lentement dans un souffle de braise. Vous quittez la salle, "
                  "laissant derrière vous les cendres de votre compagnon tombé.[/italic]")

    
    def floor6_air(hero):
        console.print("\n[bold cyan]=== Étage 6 : Épreuve de la Salle de l'Air ===[/bold cyan]")

    # Narration de l'entrée
        console.print(
        "[italic]La porte glisse lentement derrière vous, se refermant dans un silence pesant. "
        "L’air devient frais et vibrant, presque vivant. Vous vous retrouvez dans une salle cylindrique, plus étroite que les autres. "
        "Un immense cylindre métallique tourne lentement au centre, entouré de tuyaux de cuivre soufflant des brises irrégulières.[/italic]"
    )

    # Présentation des personnages
        console.print("Kael (serrant les dents) : 'Parfait… une salle musicale. On va jouer de la flûte géante maintenant ?'")
        console.print("Clotaire (ricanant) : 'Je suis sûr que tu es un virtuose. Après tout, la noblesse adore ce genre de raffinement.'")
        console.print("Kael (jetant un regard noir à Clotaire) : 'Tu devrais plutôt écouter. C’est la seule chose que tu maîtrises.'")
        console.print("Garen (fixant le cylindre) : 'Ce n’est pas de la musique. C’est une énigme sonore.'")
        console.print("Emphyr (calme, posant une main sur un tuyau) : 'Il y a de la magie ici. L’air vibre différemment. Nous allons devoir harmoniser ces vents.'")

    # Description du cylindre
        console.print(
        "[bold yellow]Un cylindre gravé tourne au centre de la salle. Cinq tuyaux soufflent des brises discordantes, "
        "créant une cacophonie. Quatre valves entourent le cylindre, suggérant une manipulation nécessaire.[/bold yellow]"
    )

    # Apparition du sablier
        console.print(
        "[italic]Un sablier noir descend du plafond, suspendu au-dessus du cylindre. "
        "Du sable doré s’écoule lentement, mais chaque note discordante accélère son flux.[/italic]"
    )
        console.print("Inscription sur le sablier : 'Lorsque le dernier grain tombera, la mélodie du vent cessera, emportant ceux qui n’ont pas su l’écouter.'")

        console.print("Kael (fronçant les sourcils) : 'On est pressés… évidemment.'")
        console.print("Clotaire (d’un ton moqueur, observant Garen) : 'Un peu de pression… c’est justement ce qu’il faut pour voir qui craque en premier.'")
        console.print("Garen (croisant les bras) : 'Tu crois vraiment que tes provocations vont aider ?'")

        console.print("Emphyr (d’un ton posé, mais ferme) : 'Ça suffit. Plus on se trompe, plus le sablier s’accélère. Évitez de vous disputer.'")

    # Phase 1 – Premiers essais
        console.print("[bold yellow]=== Phase 1 : Observation et Premiers Essais ===[/bold yellow]")
        console.print(
            "[italic]Garen s’approche et tourne doucement une valve. Un son grave résonne harmonieusement avant d’être perturbé par un autre tuyau.[/italic]"
    )
        console.print("Kael (hausse un sourcil) : 'Et Paysan tu crois vraiment pouvoir régler ça tout seul ?'")
        console.print("Clotaire (souriant en coin) : 'Laisse-le. C’est toujours amusant de voir des trayeurs de vaches essayer de bricoler.'")

        console.print("Garen (jetant un regard irrité) : 'Je n’ai pas besoin de vos commentaires.'")
        console.print("Kael (ricanant doucement) : 'Pour une fois, je suis d’accord avec Garen. Ferme-la, Clotaire.'")
        console.print("Garen : 'Ca vaut aussi pour toi !'")

        console.print("Emphyr (croisant les bras, essayant de rester diplomate) : 'Vous trois… vous pouvez vous disputer après que la salle soit résolue.'")
        console.print(
            "[italic]Clotaire hausse les épaules avec nonchalance, mais son sourire ne disparaît pas. Kael et Garen échangent des regards furtifs, la tension palpable. "
            "Pendant ce temps, Emphyr continue d’analyser silencieusement le mécanisme du cylindre.[/italic]"
    )

    # Choix initial pour le joueur
    choix_observation = Dialogue(
        "Que souhaitez-vous faire ?",
        [
            {
                "text": "Laisser Garen continuer seul.",
                "consequence": lambda h: [
                    console.print("[italic]Garen persiste malgré les moqueries, ajustant la valve à nouveau. "
                                 "Une note harmonieuse retentit, mais une autre valve siffle immédiatement en retour.[/italic]"),
                    console.print("Garen (serrant les poings) : 'C’est plus compliqué que prévu…'"),
                    console.print("Clotaire (ricanant) : 'Sans blague. Peut-être qu’on devrait te laisser seul gérer tout ça.'"),
                ]
            },
            {
                "text": "Intervenir et proposer à Kael d’aider.",
                "consequence": lambda h: [
                    console.print("[italic]Kael s’approche à contrecœur, lançant un regard ennuyé à Garen.[/italic]"),
                    console.print("Kael : 'Bon… ça m’ennuie, mais autant que ce soit fait correctement.'"),
                    console.print("Garen (soufflant) : 'Fais ce que tu veux, mais ne gêne pas.'"),
                ]
            },
            {
                "text": "Demander à Emphyr de prendre la tête.",
                "consequence": lambda h: [
                    console.print("[italic]Emphyr hoche la tête et s’avance, tournant une valve elle-même.[/italic]"),
                    console.print("Emphyr : 'Il faut écouter attentivement… Les tuyaux ne mentent pas.'"),
                    console.print("[italic]Kael et Garen échangent un regard mais ne s’opposent pas.[/italic]"),
                ]
            }
        ]
    )
    choix_observation.display(hero)
    console.print("[bold yellow]=== Phase 2 : Manipulation des Valves ===[/bold yellow]")

    console.print(
        "[italic]Un silence tendu s'installe alors que le sablier continue de s’écouler lentement. "
        "Les brises discordantes s’entrelacent dans l’air, formant un mélange désagréable qui semble refléter "
        "l’ambiance entre les membres de l’équipe.[/italic]"
        )
    console.print("Kael (les bras croisés, fixant le cylindre) : 'On ne va pas rester là à admirer le décor. Quelqu’un doit tourner ces fichues valves.'")
    console.print("Garen (lui lançant un regard en biais) : 'Tu es soudain motivé à aider ? Je pensais que tu préférais regarder de loin.'")
    console.print("Clotaire (ricanant doucement) : 'Continuez… vous êtes presque aussi divertissants que cette énigme.'")
    
    console.print("[italic]Emphyr pousse un léger soupir, détournant les yeux du sablier pour observer chacun d’eux en silence.[/italic]")
    console.print("Emphyr (calme mais ferme) : 'Il va falloir que vous coopériez, ou on ne passera jamais cette épreuve.'")
    console.print("Kael (levant un sourcil) : 'Et qui t’a désignée comme chef, Emphyr ?'")  
    console.print("Emphyr (croisant les bras) : 'Personne. Mais si vous vous entretuez, ce cylindre ne bougera pas d’un pouce.'")
    console.print("[italic]Les mots d’Emphyr semblent résonner un instant. Kael détourne le regard, visiblement peu enclin à argumenter davantage.[/italic]")

    console.print("Garen (se redressant, posant la main sur une valve) : 'Je vais commencer par celle du centre. Ça ira plus vite que d’attendre que vous vous décidiez.'")
    console.print("Clotaire (ricane, adossé à un pilier) : 'Oh, voilà qu’il se donne des airs de héros… Mais vas-y, ça pourrait être amusant.'")
    
    console.print("[italic]Kael finit par s’approcher, posant nonchalamment la main sur une valve, bien qu’il évite de croiser le regard de Garen.[/italic]")

    console.print("Kael : 'Je suppose que je n’ai pas le choix. Plus vite c’est fait, plus vite on pourra sortir d’ici.'")
    console.print("Emphyr (hochant la tête) : 'Je prendrai celle du haut. Concentrez-vous, ce n’est pas un simple jeu.'")

    # Choix pour la manipulation des valves
    choix_valve = Dialogue(
        "Qui placez-vous pour manipuler les valves ?",
        [
            {
                "text": "Garen – Valve centrale (leader).",
                "consequence": lambda h: [
                    console.print("Garen (déterminé, serrant la valve) : 'Je vais m’en charger. Ça ne peut pas être si compliqué.'"),
                    console.print("[italic]Les tuyeaux commence a s'alligner bien qu'ils tournent tous dans des directions diffrente[/italic]"),
                    
                ]
            },
            {
                "text": "Kael – Valve gauche.",
                "consequence": lambda h: [
                    console.print("Kael (jetant un regard à Clotaire) : 'Je suppose que je suis coincé ici.'"),
                    console.print("Clotaire (moqueur) : 'Coincé, oui. À ton habitude. Noble ahah, coincé, tu l'a ?!'"),
                    console.print("Kael : 'J'ai envie de trancher la langue maudit voleur de ruelle !'"),
                    console.print("Clotaire : 'Oooh il m'a insulté ! Emphyr au secours (mimant etre triste)'"),
                    
                ]
            },
            {
                "text": "Emphyr – Valve supérieure.",
                "consequence": lambda h: [
                    console.print("Emphyr (calmement) : 'Très bien, je prends celle-ci. Restez concentrés.'"),
                    console.print("Garen : 'Allons y ! En même temps !'"),
                    console.print("Emphyr : 'Je te suis Garen (dit-elle avec un sourire charmeur, Garen tourne la valve en etant rougissant)'"),
                    
                ]
            }
        ],
        character=hero.get_relation("Kael").character
    )
    choix_valve.display(hero)

    # Phase 3 : Le Dilemme du Vent Final
    console.print("[bold yellow]=== Phase 3 : Dilemme du Vent Final ===[/bold yellow]")
    console.print(
        "[italic]Alors que les valves sont manipulées, une cinquième valve s’active d’elle-même, "
        "provoquant une rafale soudaine qui déséquilibre Kael. Le sablier s’accélère, les grains chutant rapidement.[/italic]"
    )
    console.print("Kael (en reculant légèrement) : 'Ah… génial. Il en fallait une de plus.'")
    console.print("Garen (fronçant les sourcils) : 'On n’a pas le temps de tergiverser. Quelqu’un doit s’en occuper.'")
    console.print("Clotaire (amusé, regardant Kael) : 'Tu veux essayer, noble ? Après tout, tu aimes bien tout contrôler.'")
    console.print("Kael (agacé) : 'Ce n’est pas le moment, Clotaire.'")
    console.print("Emphyr (s’approchant) : 'Je vais m’en occuper. Concentrez-vous sur les vôtres.'")
    console.print("[italic]Un instant de silence passe, tandis que chacun reprend sa position, une tension toujours présente mais bridée par la nécessité.[/italic]")


    
    console.print("[bold yellow]=== Phase 3 : Dilemme du Vent Final ===[/bold yellow]")
    console.print(
        "[italic]Une cinquième valve s’active soudainement par elle-même, provoquant une rafale violente. "
        "Le sablier s’accélère drastiquement, et l’air devient plus lourd, oppressant.[/italic]"
    )

    console.print("Kael (s’écartant légèrement) : 'Il fallait bien qu’il y ait un piège…'")
    console.print("Garen (serrant les dents, posant une main ferme sur la valve) : 'On n'a pas le choix, il faut tourner.'")
    console.print("[italic]Garen force sur la valve, mais elle résiste, semblant se bloquer à mi-chemin.[/italic]")

    console.print("Emphyr (fronçant les sourcils) : 'Tu ne peux pas la tourner seul, Garen. Laisse-moi t’aider.'")
    console.print("Clotaire (adossé au mur, croisant les bras) : 'Oh, regardez-le. Le héros et sa belle. Mignon.'")
    
    console.print("[italic]Un éclat de colère traverse brièvement le regard de Garen, mais il reste concentré sur la valve. "
                  "Emphyr jette un regard glacial à Clotaire sans répondre.[/italic]")

    choix_final = Dialogue(
        "Que faites-vous ?",
        [
            {
                "text": "Garen force la valve seul.",
                "consequence": lambda h: [
                    console.print("Garen (grimaçant) : 'Je vais… y arriver…'"),
                    console.print("[italic]Il force de toutes ses forces, mais la valve ne cède qu’au dernier moment, "
                                 "envoyant une puissante bourrasque dans la salle. Il titube mais reste debout.[/italic]"),
                    console.print("Emphyr (soupirant) : 'Têtu… mais efficace.'"),
                    console.print("Kael (croisant les bras) : 'Bien joué, Garen. Pas mal pour un fermier.'"),
                    
                ]
            },
            {
                "text": "Kael aide Garen à tourner la valve.",
                "consequence": lambda h: [
                    console.print("Kael (soupire, s’approchant) : 'Bouge-toi… je vais t’aider.'"),
                    console.print("[italic]Kael attrape la valve avec Garen. Ensemble, ils parviennent à la faire tourner, "
                                 "réduisant la pression dans la salle.[/italic]"),
                    console.print("Garen (léger sourire) : 'Merci…'"),
                    console.print("Kael (moqueur) : 'Ne t’habitue pas trop. Je ne suis pas ton acolyte.'"),
                   
                ]
            },
            {
                "text": "Clotaire sabote discrètement la valve.",
                "consequence": lambda h: [
                    console.print("Clotaire (avec un sourire) : 'Oups… Quelle maladresse.'"),
                    console.print("[italic]Il fait semblant d’aider mais relâche volontairement son effort au dernier moment. "
                                 "Une bourrasque brutale souffle Garen contre le mur.[/italic]"),
                    console.print("Emphyr (furieuse) : 'Clotaire !'"),
                    console.print("Clotaire (détendu) : 'Oh, c’était un accident…'"),
                    
                ]
            },
            {
                "text": "Emphyr agit rapidement seule.",
                "consequence": lambda h: [
                    console.print("Emphyr (se glissant près de Garen) : 'Je vais le régler. Écartez-vous.'"),
                    console.print("[italic]D’une main habile, Emphyr tourne la valve avec agilité, dissipant la bourrasque "
                                 "avant qu’elle n’atteigne le reste du groupe.[/italic]"),
                    console.print("Garen (lui jetant un regard reconnaissant) : 'Merci, Emphyr.'"),
                   
                ]
            }
        ]
    )
    choix_final.display(hero)
    floor6_air(hero)

    # Conclusion de l'Épreuve
    console.print("[bold cyan]=== Fin de l'Épreuve ===[/bold cyan]")
    console.print("[italic]Alors que la dernière valve est tournée, le cylindre ralentit, laissant place à une mélodie douce et envoûtante. "
                  "Le sablier s’immobilise, ses derniers grains suspendus, signalant leur réussite.[/italic]")
    console.print("Emphyr (léger sourire) : 'C’est terminé.'")
    
    console.print("Kael (croisant les bras) : 'On s’en est sorti… malgré quelques boulets.'")
    console.print("[italic]Clotaire ne répond pas. Il fixe silencieusement le cylindre, ses pensées ailleurs.[/italic]")
    
    # Développement de Clotaire
    console.print("[italic]Dans le silence, Clotaire observe les autres, se tenant à l'écart. "
                  "Son esprit retourne à des souvenirs lointains – des années de survie seul, "
                  "volant pour manger, trahi à plusieurs reprises, jusqu’à ce qu’il rencontre Velm et Brandio. "
                  "Pour la première fois, il avait eu des compagnons… mais la tour avait fini par en emporter un.[/italic]")

    console.print("Garen (soufflant, s’adossant au mur) : 'On l’a fait…'")   
    console.print("[italic]Il jette un regard furtif à Emphyr, un léger sourire aux lèvres, mais détourne rapidement les yeux.[/italic]")

    console.print("[italic]La porte s’ouvre lentement, révélant un passage vers l’étage suivant. "
                  "Alors que Kael et Garen passent devant, Emphyr s’attarde un instant aux côtés de Clotaire.[/italic]")
    
    console.print("Emphyr (doucement) : 'Tu aurais pu nous aider, Clotaire.'")
    console.print("[italic]Clotaire ne la regarde pas, les yeux rivés sur la sortie.[/italic]")
    console.print("Clotaire (voix basse) : 'J’ai appris à ne compter que sur moi-même. C’est plus sûr.'")
    console.print("Emphyr (le regardant avec compassion) : 'Tu n’es pas seul. Pas cette fois.'")
    
    console.print("[italic]Clotaire ne répond rien et se contente de marcher en silence, laissant derrière lui les ombres de son passé."
                  " La salle s’efface lentement derrière eux, ne laissant que l’écho d’une mélodie harmonieuse.[/italic]")

    # Indication de relation croissante entre Emphyr et Garen
    console.print("[italic]Garen ralentit légèrement, laissant Emphyr marcher à ses côtés. Il glisse un regard furtif dans sa direction, "
                  "et pour la première fois depuis longtemps, la tension entre eux semble s’atténuer légèrement.[/italic]")
    console.print("Garen (timidement) : 'Tu sais… merci d’avoir pris les devants.'")
    console.print("Emphyr (souriant doucement) : 'Tu aurais fait pareil pour moi.'")
    console.print("[italic]Kael, marchant en avant, lève les yeux au ciel en entendant l’échange mais ne dit rien.[/italic]")


    def floor6_conclusion(hero):
        from rich.console import Console
        console = Console()

        console.print("\n[bold cyan]=== Étage 6 : Le Duel Sous les Flammes Éteintes ===[/bold cyan]")

    # Sortie des équipes
        console.print(
        "[italic]La porte de la salle de l’air s’ouvre lentement, laissant sortir Kael, Garen, Emphyr et Clotaire. "
        "Clotaire sort en premier, époussetant sa cape nonchalamment, mais son regard trahit une tension intérieure.[/italic]"
    )

        console.print("Clotaire (souriant) : 'Voilà qui n’était pas si compliqué. Je commençais à m’ennuyer.'")
        console.print("Kael (regard sombre) : 'Tu as surtout failli nous ralentir.'")
        console.print("Garen (voix basse) : 'Ne recommencez pas…'")

    # Retrouvailles avec l'équipe d'Aldric
        console.print(
        "[italic]En avançant vers la salle centrale, vous apercevez Aldric, Ayela et Gallius près du mur. "
        "Ayela essuie discrètement ses yeux rougis, accroupie contre une colonne. Gallius joue distraitement avec sa dague.[/italic]"
    )
        console.print("Clotaire (s’approchant) : 'Oh… des pleurs ?' [italic](Son regard se pose sur Ayela.)[/italic]")
        console.print("Clotaire (narquois) : 'On dirait que tout le monde n’a pas eu notre chance. Qui est mort, cette fois ?'")

        console.print("Garen (posant une main sur Ayela) : 'Laisse-la.'")
    
        if hero.get_relation("Velm"):
            console.print("Aldric (voix basse, évitant le regard de Clotaire) : 'Velm….'")
        if hero.get_relation("Brandio"):
            console.print("Aldric (voix basse) : 'Brandio n’a pas survécu. La créature l’a réduit en cendres. Désolé Clotaire.'")
    
        console.print("[italic]Clotaire s’arrête net, son sourire disparaissant immédiatement. Un silence lourd s’installe tandis qu’il fixe Aldric intensément.[/italic]")

        if hero.get_relation("Velm"):
            console.print("Clotaire (voix rauque) : 'Velm… ?' [italic](Il serre les poings.)[/italic]")
        if hero.get_relation("Brandio"):
            console.print("Clotaire (le regard s’assombrissant) : 'Brandio…'")

        console.print("Kael (sombre) : 'Tu pourrais au moins faire semblant d’avoir du respect, Clotaire.'")
        console.print("Clotaire (hautain, mais avec une lueur tremblante) : 'Pourquoi ? La tour décide. Il n’a pas su survivre.'")

    # Provocation de Clotaire
        console.print("[italic]Clotaire s’approche lentement d’Aldric, les yeux flamboyants d’une colère contenue.[/italic]")
        console.print("Clotaire (froidement) : 'C’est toi, non ? Leur chef. Peut-être que tu n’es pas si doué pour les garder en vie…'")
    
        if hero.get_relation("Velm"):
            console.print("Clotaire : 'Ou peut-être que tu as laissé Velm mourir exprès… pour éliminer un rival, un concurrent.'")
            hero.remove_relation("Velm")
        if hero.get_relation("Brandio"):
            console.print("Clotaire : 'Tu as aussi tué Brandio… Comme c’était pratique. Il te gênait aussi, c’est ça ?'")
            hero.remove_relation("Brandio")

        console.print("[italic]L’atmosphère devient lourde tandis qu’Aldric lève lentement les yeux vers Clotaire. "
                  "Kael et Ayela se redressent instinctivement, prêts à intervenir.[/italic]")

        console.print("Aldric (calme mais ferme) : 'Va savoir…'")

    # Duel commence
        console.print("[italic]En un éclair, Clotaire dégaine sa lame, pointant Aldric avec défi. Gallius esquisse un mouvement rapide, ses dagues prêtes, "
                  "tandis qu’Ayela tend son arc vers Clotaire.[/italic]")

        console.print("Clotaire (froidement) : 'Baisse ton arc, Ayela. Ce n’est pas pour toi.'")
        console.print("Aldric (calmant d’un geste Ayela et Gallius) : 'Laissez. Il veut un duel ? Il l’aura.'")
        console.print("Gallius : 'Laisse moi le buté,  il me saoul depuis un moment (lechant sa lame) promis...ca sera comme s'endormir.'")
        console.print("Aldric (se battant): Non t'en mêle pas je le gère.")

        console.print("[italic]Les lames jaillissent dans un éclat métallique. Clotaire et Aldric s’affrontent sous les regards attentifs des autres participants.[/italic]")
        console.print("Kael (murmurant à Garen) : 'Je me demande qui va gagner…Aldric a surement une chance..'")
        console.print("Garen (inquiet) : 'Ils vont s’entretuer…'")

    # Duel
        console.print("Clotaire (attaquant vivement) : 'Tu crois que tu es meilleur que nous tous ?!'")
        console.print("Aldric (bloquant habilement) : 'Je crois surtout que je m'emmerde...'")

    # Échange intense
        console.print("[italic]Les coups s’enchaînent, mais aucun des deux ne parvient à prendre l’avantage. Clotaire est rapide et précis, "
                  "mais Aldric pare chaque attaque avec calme. Petit à petit, le duel semble perdre en intensité.[/italic]")

    # Intervention de Garen
        console.print("[bold yellow]=== Intervention de Garen ===[/bold yellow]")
        console.print("[italic]Alors que les lames s’entrechoquent encore, Garen s’interpose brusquement, écartant les deux hommes.[/italic]")
        console.print("Garen (criant) : 'Assez ! Vous voulez vraiment mourir ici ?!'")

        console.print("[italic]Clotaire abaisse lentement sa lame, un sourire amer aux lèvres.[/italic]")
        console.print("Clotaire : 'Je voulais juste voir s’il avait du mordant…'")

    # Apparition d'Archeon
        console.print(
        "[bold red]Un claquement sec interrompt le duel. Une silhouette descend lentement de la passerelle supérieure.[/bold red]"
    )
        console.print("Archeon (calme mais puissant) : 'Je crois que...ca suffira...'")
        console.print("[italic]Clotaire et Aldric abaissent leurs lames alors qu’Archeon s’approche.[/italic]")

        console.print("Archeon (pose ses mains sur les épaules des deux duelistes et leur murmures): 'Si vous souhaitez mourir, attendez. D’autres étages vous attendent.'")
        console.print("Clotaire (haussant les épaules) : 'Comme vous voulez, maître de la tour.'")
        console.print("Archeon : Maitre de la tour ??? Ahahah ! Rien que ca ! Nooon je ne suis rien du moins pas pour vous (dit il en regardant Aldric)")

        console.print("[italic]Les tensions s’apaisent tandis que la porte menant à l’étage suivant s’ouvre lentement. "
                  "Mais Clotaire garde ses pensées sombres, ses yeux se perdant un instant vers l’obscurité au-dessus.[/italic]")


    # Fin de l'étage
    console.print("[bold cyan]=== Fin de l'Étage 6 ===[/bold cyan]")

# Archeon rassemble les survivants
    console.print(
    "[italic]Archeon balaie la salle du regard, ses yeux s’attardant sur Aldric et Clotaire. "
    "L’atmosphère est lourde, marquée par la fatigue et les pertes récentes.[/italic]"
    )
    console.print("Archeon : 'Seize d’entre vous ont debutés cette épreuve. Mais celle n'est pas finit !'")
    console.print("Archeon (lentement) : 'Sans les quatre gemmes, cette porte pour le 7ème étage ne s’ouvrira pas. "
             "Si l’une des gemmes élémentaire manque à l’appel… vous devrez retourner dans les salles ont les autres ont echoué et ramener les pierres.. "
             "Encore… et encore.'")

    console.print(
    "[italic]Les paroles d'Archeon résonnent comme une sentence. Un frisson parcourt les survivants, "
    "le poids de cette réalité s’ancrant dans leur esprit.[/italic]"
    )

    console.print("Kael (détournant le regard) : 'Magnifique. Encore une bonne raison de ne pas dormir cette nuit.'")
    console.print("Garen (baissant les yeux) : 'Il doit bien y avoir un autre moyen…'")

    console.print(
    "[italic]Le silence s'étire, jusqu'à ce qu'un bruit de mécanisme retentisse. "
    "La porte de la salle de l’eau s’ouvre lentement, laissant s’échapper un torrent d’eau glaciale.[/italic]"
    )

# Entrée de Durnir – Archimage
    console.print(
        "[italic]De la vague émerge une silhouette solitaire. Un vieil homme aux cheveux gris courts et à la barbe fournie, "
        "vêtu d’une longue robe bleu nuit brodée de symboles anciens, avance avec une dignité glaciale malgré l’eau ruisselant de sa tenue. "
        "Chaque pas qu'il fait semble marquer l’eau autour de lui, comme si même les éléments hésitaient à le défier. "
        "Son regard acéré, presque perçant, glisse sur les survivants sans un mot, évaluant leur valeur d’un simple coup d’œil.[/italic]"
    )
    console.print("Kael (abasourdi, écarquillant les yeux) : 'Par tous les dieux… L’Archimage Durnir d’Urdragen ?'")  
    console.print("[italic](Kael recule d’un pas, incapable de cacher son étonnement. Même Clotaire semble afficher une rare expression de surprise.)[/italic]")  

    console.print("Kael (murmurant) : 'Je savais bien que ce vieux me disait quelque chose… mais je croyais qu’il était mort il y a des années.'")  
    console.print("Durnir (calme, secouant lentement sa manche trempée) : 'Les rumeurs de ma mort étaient prématurées… comme toujours.'")  
    console.print("Garen (intrigué) : 'Tu le connais ? Qui est-ce ?'")  
    console.print("Kael (s’approchant légèrement) : 'L’Académie d’Urdragen… c’était la plus prestigieuse école de magie de l’Empire, bien avant ma naissance.'")  

    console.print(
        "[italic]Kael désigne Durnir d’un léger geste de la main, presque comme s’il s’adressait à une légende vivante. "
        "Même Clotaire semble garder le silence, ce qui n’échappe pas à Garen. Emphyr, de son côté, observe l’archimage avec un mélange d’intérêt et de méfiance.[/italic]"
    )  
    console.print("Kael : 'Urdragen était le centre de l’érudition magique il y a plusieurs siècles. Les plus grands sorciers, invocateurs et enchanteurs venaient de là. Durnir…'")  
    console.print("Kael (marquant une pause) : 'Il était considéré comme le dernier grand Archimage avant que l’Académie…'")  
    console.print("Durnir (l’interrompant) : '…Ne s’effondre sous son propre poids.'")  

    console.print(
        "[italic]Durnir croise les bras, son expression ne montrant ni regret ni tristesse. Il semble accepter ce passé comme une fatalité qu’il ne cherche plus à contester.[/italic]"
    )  

    console.print("Durnir (avec une pointe de sarcasme) : 'Urdragen a enseigné la magie pendant des siècles, mais l'or coule moins bien que les sortilèges. "
            "L’académie s’est noyée sous ses propres dettes, et ses mages se sont dispersés au vent. Je suis simplement l’un des derniers qui ont refusé de partir.'")  
    console.print("Garen (perplexe) : 'Alors pourquoi venir ici ?'")  
    console.print("Durnir (haussant un sourcil) : 'Parce que, jeune homme, il existe encore des secrets que même les anciens murs d’Urdragen n’ont jamais révélés. "
            "Et cette tour… semble généreuse en réponses, du moins pour ceux qui survivent assez longtemps hehe.'")  

    console.print(
        "[italic]Derrière lui, la vague qui l’a porté déverse trois corps inertes, leurs visages figés par l’effroi. "
        "Ils glissent le long du sol en pierre, s’arrêtant à quelques mètres des autres survivants. "
        "Durnir ne leur accorde pas un regard, son attention toute entière tournée vers Archeon, à qui il tend une gemme azurée brillante.[/italic]"
    )   

    console.print("Durnir (calmement) : 'L’eau n’a laissé que moi. Comme souvent.'")  
    console.print("Archeon (hochant la tête, un léger sourire en coin) : 'L’Urdragen devait être fière.'")  
    console.print("Durnir (ricanant doucement) : 'L’Académie d’Urdragen n'est plus que l'ombre d'elle même. Mes nombreux succès...récents,passés ou a venir n'y changeront rien..'")  
    console.print("Kael (avec une pointe de respect) : 'Mais vous êtes toujours là. L’Empire vous doit au moins cela.'")  

    console.print(
        "[italic]Durnir esquisse un sourire fatigué, mais il ne répond pas immédiatement. Il se contente de croiser les mains derrière le dos, "
        "observant les autres survivants. Derrière ce masque de calme se cache une détermination froide, typique des mages ayant survécu à des décennies d’épreuves.[/italic]"
    )  

    console.print("Durnir (fixant Kael) : 'L’Empire ne doit rien à personne. Et certainement pas à un vieil homme comme moi.'")  
    console.print("Emphyr (intervenant doucement) : 'Peut-être. Mais la tour, elle, semble encore avoir besoin de vous.'")  
    console.print("Durnir (incline légèrement la tête) : 'Je suis encore utile, pour le moment. Voyons combien de temps cela dure.'")  

    console.print(
        "[italic]Alors que Durnir rejoint les autres survivants, Archeon observe la gemme d’eau avec un air pensif. "
        "Malgré son âge et la disparition de l’Académie, l’Archimage est sans aucun doute l’un des plus dangereux et influents mages présents dans la tour.[/italic]"
)


# Entrée de Yohna et Zyn – Jumeaux Invocateurs
    console.print(
    "[italic]Presque aussitôt, un second bruit résonne. La porte de la salle de la terre s’ouvre dans un grincement sinistre. "
    "Deux jeunes silhouettes émergent, blessées mais vivantes.[/italic]"
    )
    console.print(
    "[italic]Yohna et Zyn, frère et sœur jumeaux, apparaissent vêtus d'un ensemble de peaux de bêtes et de lanières de cuir. "
    "Leurs vêtements semblent avoir été rafistolés à de nombreuses reprises. "
    "Leurs cheveux blanc ébouriffés – longs pour Yohna, courts pour Zyn – contrastent fortement avec la noirceur de la salle. "
    "Les cicatrices qui marquent leurs jeunes visages, alliées à leurs yeux rouges perçants, leur donnent une apparence presque animale. "
    "Ce sont des enfants forgés par et pour la survie, Pas comme les deux corps empalés sur des branches épineuses qui jonchaient l’entrée de la salle qu’ils viennent de franchir.[/italic]"
    )
    console.print("Zyn (soufflant) : 'Encore debout, Yohna ?'")
    console.print("Yohna (léger sourire) : 'Toujours, petit frère. C'est pas aujourd'hui qu'on crève.'")

    console.print(
        "[italic]Ils avancent lentement jusqu’à Archeon, chacun soutenant l’autre, mais avec une dignité farouche. "
        "Ils tendent ensemble la gemme terrestre, mais leurs mains tremblent légèrement, trahissant la fatigue accumulée.[/italic]"
        )

    console.print("Archeon (calmement) : 'Yzunfarl donne encore des enfants à cette tour…'")  
    console.print(
        "[italic]Un silence s'installe. Le nom d'Yzunfarl évoque des souvenirs sombres pour certains. "
        "L'ancienne cité, jadis bastion des invocateurs, n'est aujourd'hui qu'une terre de ruines, marquée par la peur et le rejet. "
        "Durant la dernière décennie, un génocide avait presque éteint l’ordre des invocateurs, poussant les survivants à l’exil.[/italic]"
    )   

    console.print("Garen (curieux, s’approchant prudemment) : 'Vous... Vous êtes vraiment des invocateurs d’Yzunfarl…?'")  
    console.print(
        "[italic]Le ton de Garen est maladroit, oscillant entre admiration et méfiance. "
        "Les invocateurs sont redoutés dans l'Empire, perçus comme des anomalies vivantes, des sorciers dont le pouvoir peut éveiller les éléments eux-mêmes.[/italic]"
    )
    
    console.print("Durnir : 'Les invocateurs...Un ersatz de magicien...mais j'ai néanmoins du respect pour vous'")
    console.print("Ayela : 'J'ai entendu tout un tas de choses sur eux...'")
    console.print("Aldric (les bras croisés adossé au pilier) : Hm mon intuition était bonne..je les avaient reparés dès l'exterieur de la tour...")

    console.print("Yohna (haussant les épaules, sans se détourner) : 'Il semble qu’on se fasse encore remarquer.'")  
    console.print("Zyn (sèchement) : 'L’Empire ne nous oublie pas, non. Mais ça n’a jamais été pour les bonnes raisons.'")  

    console.print(
    "[italic]Yohna esquisse un sourire en coin, mais celui-ci n'atteint pas ses yeux. "
    "Elle observe Garen du coin de l'œil, jaugeant son intention.[/italic]"
    )

    console.print("Garen (bafouillant légèrement) : 'Je... Je n'ai jamais rencontré d'invocateurs auparavant. On raconte que…'")  
    console.print("Yohna (coupant Garen) : 'Que nous sommes dangereux, instables… C'est vrai. Si tu veux des histoires, cherche ailleurs.'")  

    console.print(
    "[italic]Zyn ricane doucement, croisant les bras tout en observant Garen avec un regard amusé. "
    "Il semble apprécier la gêne du jeune fermier.[/italic]"
    )  

    console.print("Zyn (moqueur) : 'Fais attention, Garen. Les invocateurs d’Yzunfarl n'ont pas la patience des paysans.'")  
    console.print(
    "[italic]Garen s’apprête à répondre, mais Emphyr pose doucement une main sur son épaule, l'arrêtant dans son élan. "
    "Elle secoue légèrement la tête en direction de Garen, lui signifiant que ce n'est ni le lieu ni le moment pour discuter davantage.[/italic]"
    )  

    console.print("Emphyr (calmement) : 'Ils ont survécu à cette tour, comme nous. C'est tout ce qui importe pour l’instant.'")  
    console.print("Yohna (relevant la tête) : 'Exact. Ce qui nous sépare, c’est la force. Pas les histoires passées.'")  

    console.print(
    "[italic]Garen recule légèrement, détournant le regard. Malgré son malaise, il sent que Yohna et Zyn ne le rejettent pas totalement. "
    "Ce n'est qu'une méfiance naturelle, forgée par la souffrance et la nécessité de survivre. "
    "Il comprend que la confiance de ces deux invocateurs devra être gagnée par des actes, et non par des mots.[/italic]"
)
  

    console.print(
    "[italic]Avec les quatre gemmes rassemblées, la porte centrale commence à s’illuminer, gravée de symboles anciens. "
    "La tension s’apaise à peine, laissant place à une fatigue écrasante.[/italic]"
    )

# Moment de tension – Réaction de Clotaire
    console.print("Archeon (solennellement) : 'Dix survivants… Sur près d’une centaine hm.'")
    console.print("Clotaire (murmurant) : 'Dix survivants… et plus aucun ami ni compagnons de beuvrie...'")

    console.print(
    "[italic]Alors que tout semble se calmer, Clotaire s'approche d'Aldric, son regard dur. "
    "Les pertes de Velm et Brandio pèsent lourdement sur ses épaules.[/italic]"
    )
    
    console.print("Clotaire (serrant les poings) : 'Brandio et Velm n’aurait pas dû mourir. Tu en es le responsable.'")

    console.print(
    "[italic]Gallius ajuste ses dagues, prêt à intervenir, tandis qu’Ayela pointe discrètement son arc. "
    "Mais Aldric lève la main pour les calmer, fixant Clotaire sans ciller.[/italic]"
    )
    console.print("Aldric (froidement) : 'Tu veux des réponses ? Alors prends-les avec ta lame.'")
    console.print("[italic]Les lames s’entrechoquent brièvement, un duel silencieux sous les yeux des autres survivants.[/italic]")
    
    console.print("Gallius : laisse moi intevenir ! je vais l'avoir, et Clotaire rend moi la pomme que tu m'a volé a l'entré...c'etait mon gouter (dit-il avec son regard de tueur)")
    


# Intervention de Garen
    console.print("Garen (s'interposant) : 'Assez ! Vous voulez encore vous battre, après tout ça ?'")

# Ajout du choix interactif
    choix_duel = Dialogue(
        "Que faites-vous ?",
        [   
            {
            "text": "[bold yellow](Relation : Garen  +30)[/bold yellow] Écouter Garen et Archeon, calmer la situation (+10 Garen, +10 Archeon).",
            "condition": lambda h: h.get_relation("Garen").score > 30,
            "consequence": lambda h: [
                console.print("Aldric (calme, baissant sa lame) : 'Tu as raison, Garen… Ça suffit pour aujourd'hui.'"),
                console.print("Garen (soulagé) : 'Merci… Je savais que tu étais plus sage que Clotaire.' [italic](Relation Garen +10)[/italic]"),
                console.print("[italic]Archeon observe la scène sans intervenir, hochant légèrement la tête en signe d'approbation. (Relation Archeon +10)[/italic]"),
                h.get_relation("Garen").adjust_score(+10),
                h.get_relation("Archeon").adjust_score(+10)
            ]
        },
        {
            "text": "[bold red](Relation : Clotaire : ennemi -40)[/bold red] Ignorer Garen et répondre à la provocation de Clotaire (+20 Clotaire, +20 Kael, -20 Ayela, Archeon, Garen).",
            "condition": lambda h: h.get_relation("Clotaire").score < -40,
            "consequence": lambda h: [
                console.print("Aldric (froidement) : 'Clotaire… Tu veux voir jusqu’où ça peut aller ?'"),
                console.print("Clotaire (souriant) : 'Enfin quelqu'un avec du mordant ! [italic](Relation Clotaire +20)[/italic]'"),
                console.print("[italic]Vos lames s'entrechoquent à nouveau, ignorant les avertissements de Garen et d'Archeon.[/italic]"),
                console.print("Kael (croisant les bras) : 'Il fallait bien que quelqu'un le fasse. [italic](Relation Kael +20)[/italic]'"),
                console.print("Ayela (déçue) : 'Tu es plus imprévisible que je pensais… [italic](Relation Ayela -20)[/italic]'"),
                console.print("[italic]Archeon ne montre aucune émotion, mais l'éclat dans son regard s'estompe. (Relation Archeon -20)[/italic]"),
                console.print("[italic]Garen (secouant la tête) : 'Aldric… Je pensais que tu valais mieux que ça.' (Relation Garen -20)[/italic]"),
                console.print("[italic]Durnir lève calmement une main, et une barrière d'énergie s'interpose, arrêtant le combat.[/italic]"),
                console.print("Durnir (calme) : 'Les enfants… Arrêtez cette folie. Ce n'est ni le lieu ni le moment.'"),
                h.get_relation("Clotaire").adjust_score(+20),
                h.get_relation("Kael").adjust_score(+20),
                h.get_relation("Ayela").adjust_score(-20),
                h.get_relation("Archeon").adjust_score(-20),
                h.get_relation("Garen").adjust_score(-20)
            ]
        },
        {
            "text": "Ignorer les deux et simplement reculer.",
            "consequence": lambda h: [
                console.print("Aldric (calmement) : 'Ce duel a était interompu, il y aura une suite.'"),
                console.print("[italic]Clotaire recule, mais son sourire narquois demeure, tandis que Garen soupire de soulagement.[/italic]"),
            ]
        }
    ],
    character=hero.get_relation("Clotaire").character
    )

    choix_duel.display(hero)

    console.print("Archeon (calme) : 'Gardez votre colère. Elle vous sera utile.'")
    console.print("[italic]La porte vers l'étage supérieur s'ouvre lentement…[/italic]")
    console.print("[italic]Il reste 10 participants. L’étage suivant s’annonce plus impitoyable encore.[/italic]")

    floor6_conclusion(hero)

# Retour au menu du jeu
    game_menu.display()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Chapitre 7

def floor7(hero, game_menu):
    from rich.console import Console
    console = Console()
    
    yohna = Character("Yohna", "Invocatrice maîtrisant les créatures d'eau et d'air.", "fille", "participant")
    zyn = Character("Zyn", "Invocateur lié au feu et à la terre.", "homme", "participant")
    hero.add_relation(yohna, "Neutre")
    hero.add_relation(zyn, "Neutre")
    durnir = Character("Durnir", "Archimage de l'Urdragen, une académie en déclin. Sage, mais impitoyable.", "homme", "participant")
    hero.add_relation(durnir, "Neutre")

    console.print("\n[bold cyan]=== Étage 7 : La Salle du Repos Éphémère ===[/bold cyan]")

    # Narration d'entrée
    console.print(
        "[italic]Lorsque la porte de l'étage 6 se referme derrière vous, le froid glacial de la tour cède la place à une chaleur inattendue. "
        "Devant vous s'étend une vaste salle richement décorée. Des tapis soyeux couvrent le sol, des canapés moelleux sont disposés en cercle, "
        "et des tables chargées de fruits, de viande et de vin s'étendent jusqu'à l'horizon de cette pièce circulaire. "
        "Des lanternes suspendues diffusent une lumière dorée et dansante, projetant des ombres accueillantes sur les murs gravés d'arabesques anciennes.[/italic]"
    )

    console.print(
        "[italic]L'ambiance y est étrangement chaleureuse. Après les épreuves mortelles, cette salle ressemble à un mirage, "
        "une parenthèse de calme au milieu du chaos impitoyable de la tour.[/italic]"
    )

    # Réactions des personnages
    console.print("\nKael (s'étirant) : 'Enfin un endroit qui ne cherche pas à nous tuer… pour le moment.'")
    console.print("Ayela (méfiante) : 'C'est trop beau pour être vrai… On ne devrait pas baisser notre garde.'")
    console.print("Garen (admiratif) : 'On dirait les salons des nobles de l'Empire… Je pourrais m'habituer à ça.'")
    console.print("Clotaire (sarcastique) : 'Savourez tant que vous pouvez. Je doute que la tour nous offre ce luxe gratuitement.'")
    console.print("Emphyr (s'approchant d'une table) : 'Il y a de la nourriture… et elle semble fraîche. Étrange.'")

    # Apparition d'Archeon
    console.print("\n[bold red]Archeon[/bold red] descend lentement d'une passerelle qui surplombe la salle. Son regard impassible balaie les participants.")
    console.print("Archeon (calme) : 'Reposez-vous, participants. Vous en aurez besoin. Cette salle est un répit… mais éphémère.'")
    
    console.print(
        "[italic]Il s'arrête devant une boîte en pierre noire, posée juste devant la porte scellée menant à l'étage 8. "
        "Aucune inscription ne l'orne, mais elle dégage une aura inquiétante.[/italic]"
    )

    console.print("Kael (croisant les bras) : 'Et cette boîte… ? Qu'est-ce que c'est ?'")
    console.print("Archeon (avec gravité) : 'Cette boîte renferme tout ce que tu peux imaginer Kael. Pour l'instant, elle reste close. Jusqu'a nouvel ordre.'")
    console.print("Garen (intrigué) : 'Jusqu'a nouvel ordre ? Cela signifie que nous pouvons vraiment… nous reposer ?'")
    console.print("Archeon : 'Oui reposerz vous, La tour peut paraitre impitoyable mais en réalité elle est...juste...elle sais aussi recompenser'")

    # Description de la boîte
    console.print(
        "[italic]La boîte semble vivante, vibrante, comme si quelque chose en son sein attendait patiemment. "
        "Mais pour l'heure, elle reste immobile, une ombre menaçante parmi la lumière chaleureuse de la salle.[/italic]"
    )
    
    # Ajout du choix concernant la boîte mystérieuse
    choix_boite = Dialogue(
        "Alors que vous approchez de la boîte noire, une étrange sensation vous envahit. Que faites-vous ?",
    [
        {
            "text": "[italic]Examiner la boîte et parler de l’aura étrange qui s’en dégage.[/italic] ",
            "consequence": lambda h: [
                console.print("Aldric (fronçant les sourcils) : 'Cette boîte… Je ressens quelque chose. Une sorte de pouvoir. Ni bon ni mauvais… juste là.'"),
                console.print("[italic]Un silence s'installe alors que Zyn et Yohna échangent un regard surpris. Même Durnir arrête de lisser sa barbe un instant.[/italic]"),
                console.print("Zyn : 'Hm… Tu perçois ça ? Étrange. Seuls ceux qui pratiquent l’invocation ou la magie y sont généralement sensibles.'"),
                console.print("Yohna (curieuse) : 'Tu n’es pourtant pas de ceux qui manipulent ces forces… intéressant.'"),
                console.print("Durnir (regardant Aldric fixement) : 'La tour… amplifie certaines âmes. Peut-être est-ce là son premier effet sur toi.'"),
                console.print("Archeon (en observant la boîte) : 'Cela n’arrive pas souvent. Garde cela à l’esprit, Aldric.'(+10 Zyn, Yohna, Durnir, Archeon)"),
                h.get_relation("Zyn").adjust_score(+10),
                h.get_relation("Yohna").adjust_score(+10),
                h.get_relation("Durnir").adjust_score(+10),
                h.get_relation("Archeon").adjust_score(+10)
            ]
        },
        {
            "text": "[italic]Se méfier et exprimer votre suspicion sur un potentiel piège.[/italic] ",
            "consequence": lambda h: [
                console.print("Aldric (croisant les bras) : 'Je ne sens rien, mais cette boîte crie le mot piège. Rien n’est gratuit dans cette tour.'"),
                console.print("[italic]Garen acquiesce rapidement, se rapprochant d’Aldric.[/italic]"),
                console.print("Garen (hochant la tête) : 'Je suis d’accord… Ça sent l’embrouille à plein nez.'"),
                console.print("Kael (léger sourire) : 'Pour une fois, je suis de ton côté. Cette tour ne nous a jamais offert un festin sans un prix.'"),
                console.print("Ayela (inquiète) : 'C’est vrai… Cette atmosphère est bien trop calme pour être honnête.'"),
                console.print("Clotaire (narquois) : 'Ah ! Pour une fois, Aldric dit quelque chose d’intelligent.'(+5 Garen, Kael, Ayela, Clotaire)"),
                h.get_relation("Garen").adjust_score(+5),
                h.get_relation("Kael").adjust_score(+5),
                h.get_relation("Ayela").adjust_score(+5),
                h.get_relation("Clotaire").adjust_score(+5)
            ]
        }
        ]
    )

    choix_boite.display(hero)

# Transition vers le dialogue avec Archeon
    console.print("\n[bold red]Archeon[/bold red] s'approche doucement, s'arrêtant à quelques pas d'Aldric. L'air autour semble s'alourdir par sa simple présence.")


    # Répartition et dialogues personnels
    console.print(
        "[italic]Certains s'installent immédiatement sur les canapés, d'autres préfèrent rester debout, jetant des regards méfiants autour d'eux.[/italic]"
    )
    console.print("Ayela (s'asseyant sur un fauteuil près d'Aldric) : 'C'est peut-être notre dernière chance de profiter d'un moment de calme…'")
    console.print("Kael (au loin, servant du vin) : 'Aussi bien en profiter. Si c'est un piège, autant mourir en savourant quelque chose de bon.'")
    console.print("Clotaire (chuchotant à Emphyr) : 'Observe bien, Emphyr. Chaque visage ici cache quelque chose. Même la tour teste notre confiance.'")
    console.print("Emphyr (hochant la tête) : 'Je sais… mais parfois, il vaut mieux profiter du silence plutôt que de l'interroger.'")
    

    # Introduction des nouveaux personnages dans la scène
    console.print("[italic]Durnir s'approche lentement d'une table, remplissant une coupe de thé fumant. Zyn et Yohna s'installent à l'écart, près de la cheminée, silencieux mais observateurs.[/italic]")

    # Durnir observe le groupe
    console.print("Durnir (fixant Garen) : 'Je suis curieux… Ce garçon. Garen, n'est-ce pas ?'")
    console.print("Kael (sourire en coin) : 'Oui, c'est bien lui. Il est monté jusqu'ici, ce qui en soi… est un exploit.'")
    console.print("Durnir (haussant un sourcil) : 'Et pourtant, il n’a ni magie, ni talent particulier à l’épée.'")
    console.print("Garen (entendant cela) : 'Merci pour la remarque… Je fais de mon mieux.'")
    console.print("Durnir (calme, approchant Garen) : 'Le fait que tu sois encore là en dit long. Peut-être que la tour perçoit en toi ce que nous ne voyons pas encore.'")

    # Zyn et Yohna restent en retrait
    console.print("[italic]Non loin de là, Zyn fait glisser un petit fragment de pierre sur la table, traçant des symboles anciens du bout des doigts.[/italic]")
    console.print("Yohna (regardant Zyn) : 'Tu es nerveux ?' ")
    console.print("Zyn (calme, sans lever les yeux) : 'Je n’aime pas cet endroit. On dirait qu’il respire avec nous.' ")
    console.print("Yohna : 'Ce n'est pas la première fois qu’on se sent observés. Les invokeurs ne sont jamais les bienvenus, même parmi d’autres survivants.'")
    console.print("Garen (tentant de détendre l’atmosphère) : 'Ce n’est pas vrai… Vous avez sauvé des vies avec vos créatures, non ?'")
    console.print("Yohna (souriant légèrement mais gardant ses distances) : 'C’est ce que nous faisons. Mais cela ne change pas ce que nous sommes pour eux.'")

    # Gallius s'approche d'Aldric
    console.print("[italic]Gallius s'appuie contre une colonne, regardant Aldric de loin avant de s’approcher doucement.[/italic]")
    console.print("Gallius (à voix basse) : 'Ces deux invokeurs. Tu crois qu’on peut leur faire confiance ?'")
    console.print("Aldric (calme) : 'Ils sont encore là. Je crois qu'on peut faire confiance a personne ici..'")
    console.print("Gallius (souriant en coin) : 'Tu es plus pragmatique que je pensais. Mais j’imagine que c’est comme ça qu’on survit ici.'")
    console.print("Aldric : 'Retiens ça. La tour teste tout, même notre naiveté.'")

    # Durnir se joint à la conversation
    console.print("Durnir (posant sa tasse) : 'Les jeunes ont raison de se méfier. Mais parfois, les alliances improbables sont les plus durables.'")
    console.print("Kael (souriant) : 'La sagesse de l'archimage d'Urdragen… Je suppose que tu as vu des choses bien pires que cette tour.'")
    console.print("Durnir : 'Des décennies d’élèves trop sûrs d’eux, oui. Mais peu ont eu votre persévérance. Profitez du repos tant qu'il dure.'")

    # Conflit sous-jacent de Clotaire
    console.print("[italic]Un peu plus loin, Clotaire reste à l'écart du groupe, le regard fixé sur la boîte noire. "
                  "Son esprit semble ailleurs, peut-être perdu dans les souvenirs de Velm et Brandio.[/italic]")

    console.print("Emphyr (se tenant près de Clotaire) : 'Tu n’es pas obligé de rester seul.'")
    console.print("Clotaire (sans détourner les yeux) : 'Je le suis depuis le début. Même avant la tour.'")
    console.print("[italic]Le silence s'installe un instant, avant qu'Emphyr ne lui pose doucement une main sur l'épaule. Clotaire ne bouge pas, mais il ne la repousse pas non plus.[/italic]")

    # Conclusion du moment de repos
    console.print("[italic]Alors que les survivants s’installent un peu plus confortablement, la lumière du jour s’atténue lentement. "
                  "La boîte noire demeure immobile, mais son ombre s’étend peu à peu sur le sol, annonçant l’approche du crépuscule… et des épreuves à venir.[/italic]")

    # Pause
    console.print("[italic]Pour la première fois depuis longtemps, le silence s'installe sans menace immédiate.[/italic]")
    
        # Interdiction d'attaquer un participant
    console.print("[bold red]Archeon (d’un ton grave) : 'Avant que vous ne vous reposiez… écoutez bien.'[/bold red]")
    console.print("Archeon : 'À partir de maintenant, toute tentative de tuer un autre participant sera sanctionnée par une mort immédiate.'")
    console.print("Archeon (balayant la salle du regard) : 'La tour est assez impitoyable. Elle n'a pas besoin de votre aide pour réduire le nombre de survivants.'")

    console.print("[italic]Un silence pesant s’installe. Clotaire croise les bras en jetant un regard furtif vers Aldric. Durnir hoche lentement la tête, tandis que Zyn et Yohna échangent un regard complice.[/italic]")
    console.print("Archeon (calme mais ferme) : 'Je reviendrai à l’aube. Jusque-là, reposez-vous et récupérez vos forces. L’étage suivant réclamera plus que votre force physique.'")

    # Archeon quitte le centre de la salle
    console.print("[italic]Archeon s’éloigne, laissant les survivants profiter du silence. Aldric, ressentant le besoin d’air, s’avance jusqu’à une large terrasse adjacente.[/italic]")

    # Scène du balcon
    console.print("\n[bold cyan]=== Terrasse du Septième Étage ===[/bold cyan]")
    console.print("[italic]Depuis cette hauteur, la vue est vertigineuse. L'empire s'étend à perte de vue, baigné dans la lumière du crépuscule. "
                  "Les montagnes au loin sont teintées d’orange malgré une fine pluie, et les toits des cités en contrebas scintillent faiblement.[/italic]")

    console.print("[italic]Aldric s’appuie contre la rambarde du balcon, laissant son regard errer sur l’horizon. "
                  "Des pas discrets résonnent derrière lui. Archeon l’a rejoint, le visage impassible.[/italic]")

    # Dialogue conditionnel basé sur la relation avec Archeon
        # Archeon rejoint Aldric sur la terrasse
    console.print("\n[bold red]Archeon[/bold red] s'approche doucement, s'arrêtant à quelques pas d'Aldric. L'air autour semble s'alourdir par sa simple présence.")
    

    
    console.print("[italic]Archeon fixe l’horizon en silence pendant un moment, puis prend la parole d’une voix posée.[/italic]")
    console.print("Archeon (regardant l'Empire en contrebas) : 'Je ne suis pas surpris de te voir ici, Aldric. La tour attire ceux qui n'ont plus rien à perdre.'")
    console.print("Archeon (calme mais grave) : 'Regarde cette vue. L’Empire s’effrite lentement. Ses fondations se fissurent… Les villes s'affaiblissent. "
                  "Et pourtant, en bas, ils continuent à vivre comme si tout était éternel.'")
    console.print("[italic]Archeon inspire lentement, comme pour savourer l’air froid de l'altitude.[/italic]")
    console.print("Archeon : 'Ceux qui montent la tour ne sont que des fragments de cette ruine. Des âmes perdues, venues ici par désespoir, "
                  "par orgueil ou par nécessité… Et ils parient ce qui leur reste. Leur vie.'")
    console.print("[italic]Il se tourne vers Aldric, le scrutant attentivement.[/italic]")
    console.print("Archeon (doucement) : 'Toi… Quel est ton pari ?'")



    choix_archeon = Dialogue(
        "Archeon s'arrête à côté de vous. Que lui dites-vous ?",
        [
            {
                "text": "Pourquoi nous donner un tel répit après ces épreuves mortelles ?",
                "consequence": lambda h: [
                    console.print("Aldric (croisant les bras) : 'Pourquoi cette salle… cette boîte ? Vous jouez avec nous.'"),
                    console.print("Archeon (gardant les yeux sur l'horizon) : 'Il faut parfois briser un guerrier pour voir ce qu'il vaut. "
                                  "Ce répit est une illusion. Ce que vous y verrez dépendra de vous.'"),
                    console.print("[italic]Archeon semble mesurer chaque mot, comme s'il testait Aldric.[/italic]")
                ]
            },
            {
                "text": "Vous semblez trop calme… Vous cachez quelque chose.",
                "consequence": lambda h: [
                    console.print("Aldric (fixant Archeon) : 'Vous cachez vos intentions. Qui êtes-vous réellement ?'"),
                    console.print("Archeon (un léger sourire aux lèvres) : 'Je suis le gardien de cette tour. Mais tu le sais déjà, n'est-ce pas ?'"),
                    console.print("Aldric (fronçant les sourcils) : 'Vous avez une drôle de façon de me parler…'"),
                    console.print("Archeon (évasif) : 'Peut-être est-ce simplement la tour qui murmure en toi.'")
                ]
            },
            {
                "text": "[bold yellow](Relation : Ami)[/bold yellow] Vous avez vu ces épreuves des centaines de fois… Que suis-je censé apprendre ?",
                "condition": lambda h: h.get_relation("Archeon") and 
                          h.get_relation("Archeon").score >= 20,
                "consequence": lambda h: [
                    console.print("Archeon (baissant légèrement la tête) : 'Les épreuves sont des fenêtres sur vous-mêmes. "
                                  "Elles révèlent ce que vous refusez de reconnaître.'"),
                    console.print("Aldric : 'Et que dois-je voir ?'"),
                    console.print("Archeon (calmement) : 'Toi-même. Tu portes un fardeau, Aldric. "
                                  "Un poids que tu n’es pas prêt à admettre.'"),
                    console.print("Aldric (interloqué) : 'Comment savez-vous cela…?'"),
                    console.print("Archeon (avec un soupçon de chaleur) : 'Parce que ce n’est pas la première fois que nous nous croisons, même si tu l’as oublié.'"),
                    console.print("[italic]Aldric ressent une étrange familiarité dans ces paroles, comme si un souvenir lointain effleurait sa mémoire.[/italic]"),
                    h.get_relation("Archeon").adjust_score(+10)
                ]
            },
            {
                "text": "[bold red](Relation : Ennemi)[/bold red] Vous pensez que je ne mérite pas de continuer, n’est-ce pas ?",
                "condition": lambda h: h.get_relation("Archeon") and h.get_relation("Archeon").score >= -20,
                "consequence": lambda h: [
                    console.print("Archeon (le regard froid) : 'Certains montent par nécessité, d'autres par erreur. "
                                  "Je ne suis pas sûr que la tour t'ait choisi pour les bonnes raisons.'"),
                    console.print("Aldric (froidement) : 'Je suis encore là.'"),
                    console.print("Archeon (impassible) : 'La tour est patiente. Elle tolère ceux qui n’ont pas leur place… un temps.'"),
                    console.print("[italic]Archeon ne détourne pas son regard, et Aldric sent une tension sourde dans l'air.[/italic]"),
                    h.get_relation("Archeon").adjust_score(-5)
                ]
            },
            {
                "text": "[italic]Observer Archeon en silence.[/italic]",
                "consequence": lambda h: [
                    console.print("[italic]Aldric se contente de fixer Archeon, laissant les mots suspendus dans l'air. "
                                  "L'homme en rouge semble apprécier ce silence respectueux.[/italic]"),
                    console.print("Archeon (calmement) : 'Le silence est souvent plus éloquent que les paroles. La tour l'enseigne à ceux qui savent écouter.'"),
                    console.print("[italic]Archeon s'éloigne lentement, laissant Aldric méditer en paix.[/italic]")
                ]
            }
        ],
    )
    

    choix_archeon.display(hero)


    console.print("[italic]Alors qu'Archeon s’éloigne, Aldric sent un étrange frisson, comme si quelque chose d’important venait de lui échapper.[/italic]")


    # Transition vers la suite de l'étage
    console.print("\n[bold cyan]Alors que la nuit tombe doucement, la boîte noire semble vibrer doucement... en attente.[/bold cyan]")
    
    # Séquence du Balcon - Conversation avec Garen
    console.print("\n[bold cyan]=== 15 Minutes Après la Discussion avec Archeon ===[/bold cyan]")

    # Narration d'entrée
    console.print(
    "[italic]Aldric est accoudé à la rambarde du balcon, contemplant les plaines de l’Empire qui s’étendent sous l’étage 7. "
    "La lumière tamisée du crépuscule teinte les montagnes lointaines de reflets orangés.[/italic]"
    )

    # Arrivée de Garen
    console.print(
    "[italic]Des pas légers s’approchent derrière Aldric. Garen, mains dans les poches, évite son regard en s’approchant du balcon.[/italic]"
    )
    console.print("Garen (doucement) : 'Tu crois qu’on peut voir chez moi d’ici…? Je crois que c’est par là-bas.'")
    console.print("[italic]Il désigne une vallée lointaine, cachée par la brume du soir.[/italic]")

    # Réponse initiale d'Aldric
    console.print("Aldric : 'Pourquoi tu viens me raconter ça, Garen ?'")

    # Garen se confie
    console.print("Garen (voix basse) : 'Je… Je t’ai vaguement dit pourquoi je suis là a l'étage 4. Pas pour la gloire, ni l’argent… C’est mon père.'")
    console.print("Aldric (sérieux) : 'Ton père ?'")
    console.print("Garen (hésitant) : 'Mon frère est mort à la guerre. Depuis, c’est moi qui aurais dû… enfin, tu vois. "
              "Mais mon père… il boit trop. Il frappe ma mère et ma petite sœur. Il vend des morceaux de la ferme pour rembourser ses dettes…'"
              "Bientôt, ils n’auront plus rien.'")
    console.print("Garen (s'arrêtant un instant) : 'Je suis monté dans cette tour pour trouver le courage… "
              "Le courage de le chasser et protéger ma famille. Mais je sais pas si j’en suis capable. Aldric je sais même pas si je vais y survivre..'")

# Dialogue - Choix conditionnels pour Aldric
    choix_garen = Dialogue(
        "Comment répondez-vous à Garen ?",
    [
        {
            "text": "[bold yellow](Relation + 50)[/bold yellow] 'Tu es plus fort que tu ne le penses, Garen.'",
            "condition": lambda h: h.get_relation("Garen").score >= 50,
            "consequence": lambda h: [
                console.print("Aldric (avec sincérité) : 'Tu as déjà fait tout ce chemin. C’est pas pour rien.'"),
                console.print("[italic]Aldric s’approche de Garen et pose une main ferme sur son épaule, "
                              "forçant doucement son regard vers l’horizon brumeux.[/italic]"),
                console.print("Aldric (posant sa main sur les cheveux de Garen) : 'Regarde… aux jeux des dalles, c'est grâce à toi. "
                              "Kael m'a raconté pour la salle de l'air aussi.'"),
                console.print("Aldric (souriant légèrement) : 'T’as plus de courage que tu crois. Tu crois que c'est rien, mais…'"),
                console.print("Aldric (fixant l’horizon) : 'Quand cette tour sera derrière nous, tu auras la force qu’il te manque. "
                              "Tu l’as déjà en toi. Ce qui te manque, c’est de le reconnaître.'"),
                console.print("[italic]Garen baisse les yeux, un sourire sincère naissant sur ses lèvres.[/italic]"),
                console.print("Garen (souriant faiblement) : 'Merci… Je suis sûr que je vais mourir ici, mais ça va. "
                              "T’es le seul ami que j’ai jamais eu, Aldric. Je regrette pas d'avoir tenté la tour..'"),
                console.print("[italic]Un silence s'installe. Aldric détourne légèrement le regard, un souvenir fugace effleurant sa mémoire. "
                              "Les dix survivants... une lueur de nostalgie traverse son esprit.[/italic]"),
                console.print("Aldric (murmurant) : 'On est dix. Je… je crois que ça ira.'"),
                console.print("Garen (riant nerveusement) : 'J’espère que tu dis vrai ! Merci, mon ami..' [italic](Relation Garen +10)[/italic]"),
                h.get_relation("Garen").adjust_score(+10)
            ]
        },
        {
            "text": "'T’es pas si mauvais. T’as un bon cœur.'", 
            "consequence": lambda h: [
                console.print("Aldric (léger sourire) : 'Je plaisante pas. T’es quelqu’un de bien, Garen. T’as juste besoin d’y croire toi aussi.'"),
                console.print("[italic]Garen relève la tête, surpris par la sincérité d’Aldric. "
                              "Il détourne les yeux, gêné, mais un sourire apaisé éclaire son visage.[/italic]"),
                console.print("Garen (soulagé) : 'Merci… Ça fait du bien de l’entendre. Je crois que c’est ça qui me manquait.'"),
                console.print("[italic]Les deux fixent l’horizon en silence, profitant du rare moment de tranquillité.[/italic]"),
                
            ]
        },
        {
            "text": "[bold red](Relation ≤ -20)[/bold red] 'Tu devrais pas trop espérer. La tour prend tout.'",
            "condition": lambda h: h.get_relation("Garen").score <= -20,
            "consequence": lambda h: [
                console.print("[italic]Aldric reste immobile, perdu dans ses pensées. Son regard sombre embrasse la vallée lointaine, "
                              "mais il ne semble pas la voir.[/italic]"),
                console.print("Aldric (froidement) : 'Y’en a pas beaucoup qui ressortent de cette tour vivants, Garen. "
                              "Tu devrais pas trop espérer.'"),
                console.print("[italic]Garen baisse les yeux, mâchoire serrée, la confiance s'effilochant un peu plus.[/italic]"),
                console.print("Garen (affecté, murmurant) : '…Ouais. Peut-être.'"),
                console.print("[italic]Il s'éloigne sans ajouter un mot, laissant Aldric seul, plongé dans ses réflexions silencieuses.[/italic]"),
                h.get_relation("Garen").adjust_score(-10)
            ]
        }
    ],
        character=hero.get_relation("Garen").character
    )

    choix_garen.display(hero)

# Conclusion de la scène
    console.print("[italic]Alors que Garen s'éloigne du balcon, Aldric reste là, "
              "scrutant l’horizon sombre de l’Empire. Le vent nocturne souffle doucement, "
              "comme pour rappeler aux survivants que la tour n’a pas encore livré tous ses secrets.[/italic]")
    console.print("[italic]Au loin, la boîte noire au centre de la salle vibre faiblement, pulsant au rythme du crépuscule naissant.[/italic]")
    
    # Rencontre avec Kael sur le balcon
    console.print(
    "\n[bold cyan]Kael s'approche lentement du balcon, s'arrêtant à quelques pas d'Aldric. "
    "Le vent nocturne souffle doucement, soulevant les mèches de ses cheveux chatin. "
    "Il fixe l’horizon, là où la lumière de l’Empire s’étale faiblement, voilée par la brume.[/bold cyan]"
    )
    console.print("Kael (d’un ton calme, presque distant) : 'Tu regardes ces terres… Ces terres pourries et déchues. "
              "Il fut un temps où elles nous appartenaient. '")
    console.print("Aldric (intrigué) : 'Tu m’as dit que ta maison avait disparu après la guerre contre l'Empire du Nord…'")
    console.print(
        "Kael (un rictus amer sur le visage) : 'Disparue ? Non. La Maison Sielmarr n’a jamais disparu… "
     "Elle a été effacée, morceau par morceau. Quand la guerre a été perdue, mon oncle a plié genou devant l’Empire. "
    "Il a signé la reddition et offert nos terres…'"
    )
    console.print(
    "Kael (les poings serrés) : 'L’empereur Vilmar II a juré qu’il protégerait nos frontières. Il nous a trahis. "
    "Mes sœurs… Mariées de force aux seigneurs vainqueurs. Mon frère aîné, exécuté… Et ma mère, elle est morte sous les coups des soldats"
    "qu’on lui a infligés au palais. Pendant que l’Empire festoyait.'"
    )
    console.print("[italic]Kael détourne les yeux, l’air plus dur qu’à son habitude.[/italic]")
    console.print(
    "Kael (froidement) : 'Nous avons servi, pourtant. Mon père a levé des hommes pour l’Empire. "
    "Mais Vilmar II a préféré vendre nos terres pour acheter la paix. "
    "L’honneur de ma famille s’est éteint dans les banquets des vainqueurs.'"
    )   
    console.print(
    "Kael (d’une voix plus basse) : 'Je ne suis pas ici par hasard, Aldric. "
    "Je suis entré dans cette tour en espérant y trouver quelque chose… "
    "Un pouvoir, un artefact, n’importe quoi. "
    "Quelque chose qui pourra rendre aux Sielmarr la place qu’ils méritent. Je ne partirai pas les mains vides.'"
    )
    console.print(
    "[italic]Kael se tait, laissant le vent emporter ses paroles. "
    "Il semble fragile, presque brisé, mais l’étincelle de colère brûle encore dans ses yeux.[/italic]"
    )

    choix_kael = Dialogue(
        "Que répondez-vous à Kael ?",
    [
        {
            "text": "[bold yellow](Relation + 50)[/bold yellow] 'Ta famille a encore une chance, Kael. Et toi aussi.'",
            "condition": lambda h: h.get_relation("Kael").score >= 50,
            "consequence": lambda h: [
                console.print("Aldric (souriant doucement) : 'Tu portes plus que leur nom, Kael. Tu portes leur mémoire. "
                              "Si tu es encore debout, c’est parce que leur héritage est vivant en toi.'"),
                console.print("Kael (le regard baissé) : 'Je veux y croire… mais c’est dur. "
                              "Chaque minute dans cette tour me rappelle ce que j’ai perdu.'"),
                console.print("Aldric (posant une main sur son épaule) : 'Tu n’as pas tout perdu. "
                              "Regarde jusqu’où tu es allé. Si cette tour peut donner quelque chose, "
                              "je suis certain que tu seras là pour le prendre.'"),
                console.print("Kael (un sourire discret) : 'Merci… J’espère que tu dis vrai. On est parti du mauvais pieds toi et moi..."
                              "Je ne pensais pas te considérer comme un allié un jour, mais il semble que cette tour "
                              "réserve bien des surprises. (Kael +10)'"),
                h.get_relation("Kael").adjust_score(+10)
            ]
        },
        {
            "text": "'T’as de l’ambition. C’est bien. Mais ne te laisse pas bouffer par ça.'",
            "consequence": lambda h: [
                console.print("Aldric (le regard sévère) : 'L’ambition peut te guider, Kael. Mais ne la laisse pas te consumer. "
                              "La tour a une façon bien particulière de tester ce genre de choses.'"),
                console.print("Kael (hésitant) : 'Tu crois que je vais finir comme ces nobles déchus, ivres de pouvoir ?'"),
                console.print("Aldric : 'Je crois que tu sais mieux que moi ce que ça coûte. Ne perds pas ça de vue.'"),
                console.print("Kael (hochement de tête) : 'Hm… Tu n’as peut-être pas tort. Merci, Aldric.'"),
                h.get_relation("Kael").adjust_score(+0)
            ]
        },
        {
            "text": "[bold red](Relation ≤ -20)[/bold red] 'Garde tes illusions. L’honneur ne remplit pas les tombes.'",
            "condition": lambda h: h.get_relation("Kael").score <= -20,
            "consequence": lambda h: [
                console.print("Aldric (sèchement) : 'Tu crois que l’honneur sauvera ta maison ? Ce n’est qu’un mirage.'"),
                console.print("Kael (les poings serrés) : 'Tu crois que je ne le sais pas ?! "
                              "Je n’ai rien d’autre à quoi m’accrocher.'"),
                console.print("[italic]Aldric tourne les talons, laissant Kael seul face à ses démons. "
                              "Le noble serre les dents, dissimulant sa colère.[/italic]"),
                console.print("Kael (voix basse) : 'Tu n’as jamais eu à perdre tout ce que tu aimais, toi…'"),
                console.print("Aldric : Tu ne sais rien de moi.."),
                h.get_relation("Kael").adjust_score(-10)
            ]
        }
    ]
    )
    choix_kael.display(hero)





    game_menu.display()





