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
    
    console.print("Kael : 'Plus de retour en arrière possible hein ?'")
    
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
                    console.print("[italic]Archeon semble mesurer chaque mot, comme s'il testait Aldric.[/italic]"),
                ]
            },
            {
                "text": "Vous semblez trop calme… Vous cachez quelque chose.",
                "consequence": lambda h: [
                    console.print("Aldric (fixant Archeon) : 'Vous cachez vos intentions. Qui êtes-vous réellement ?'"),
                    console.print("Archeon (un léger sourire aux lèvres) : 'Je suis le gardien de cette tour. Mais tu le sais déjà, n'est-ce pas ?'"),
                    console.print("Aldric (fronçant les sourcils) : 'Vous avez une drôle de façon de me parler…'"),
                    console.print("Archeon (évasif) : 'Peut-être est-ce simplement la tour qui murmure en toi.'"),
                ]
            },
            {
                "text": "[bold yellow](Relation Archeon : Ami)[/bold yellow] Vous avez vu ces épreuves des centaines de fois… Que suis-je censé apprendre ?",
                "condition": lambda h: h.get_relation("Archeon").score >= 20,
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
                "text": "[bold red](Relation Archeon : Ennemi)[/bold red] Vous pensez que je ne mérite pas de continuer, n’est-ce pas ?",
                "condition": lambda h: h.get_relation("Archeon").score <= -20,
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
            "text": "[bold yellow](Relation Garen + 50)[/bold yellow] 'Tu es plus fort que tu ne le penses, Garen.'",
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
            "text": "[bold red](Relation Garen -20)[/bold red] 'Tu devrais pas trop espérer. La tour prend tout.'",
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
            "text": "[bold yellow](Relation + 35)[/bold yellow] 'Ta famille a encore une chance, Kael. Et toi aussi.'",
            "condition": lambda h: h.get_relation("Kael").score >= 35,
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
            "text": "[bold red](Relation -20)[/bold red] 'Garde tes illusions. L’honneur ne remplit pas les tombes.'",
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
    
    console.print(
    "\n[bold cyan]Alors qu'ils s'apprêtent à traverser la salle, Aldric et Kael s'arrêtent devant Zyn et Yohna. "
    "Les deux jumeaux, adossés à une colonne, semblent les observer depuis un moment.[/bold cyan]"
    )
    console.print("Yohna (croisant les bras, fixant Aldric) : 'Dis-moi, Aldric… Comment tu fais pour arriver jusqu'ici avec juste une épée ?'")  
    console.print("Zyn (reniflant) : 'Ouais. T'as même pas une égratignure. Tu triches, c'est ça ?'")  
    console.print("[italic]Kael esquisse un léger sourire tandis qu’Aldric hausse les épaules.[/italic]")  
    console.print("Aldric (amusé) : 'Va savoir. Peut-être que la tour m'aime bien.'")  
    console.print("Yohna (ricanant doucement) : 'Hm, je doute que la tour aime qui que ce soit.'")  
    console.print("Zyn (jetant un regard à sa sœur) : 'Pas même nous…'")  

# 🎴 Background Invokeurs  
    console.print(
    "\n[bold yellow]Yohna détourne le regard vers le feu de la cheminée au centre de la pièce. "
    "Sa voix s’adoucit, mais reste teintée d’amertume.[/bold yellow]"
    )
    console.print("Yohna : 'Nous venons d’Yzunfarl… Là-bas, les invokeurs étaient autrefois respectés. "
              "Mais ça, c’était avant la chute. Avant la folie de Vilmar II.'")  
    console.print("Kael (serrant les poings) : 'Encore ce foutu empereur…'")  
    console.print("Zyn (d’une voix grave, fixant Aldric droit dans les yeux) : 'Quand les barbares du Nord ont attaqué l'Empire, "
              "Vilmar II nous a tenus pour responsables. Il disait que nos pactes avec les esprits avaient attiré la malchance…'")  
    console.print("[italic]Zyn serre les poings, la colère suintant dans sa voix.[/italic]")  
    console.print("Zyn : 'L'Empereur a envoyé ses armées sur nous. Yzunfarl, la cité des nôtres, a été réduite en cendres. "
              "Nos anciens ont été brûlés vifs, et ceux qui restaient ont fui dans les montagnes.'")  
    console.print("Yohna (hoche la tête) : 'Nous étions des héros, et du jour au lendemain, nous sommes devenus des traîtres.'")  
    console.print("Zyn : 'La tour est notre seule chance. On n’a pas de chez nous où retourner. On est ici pour nous endurcir.'")  
    console.print("Kael (calmement, d’une voix emplie de compassion) : 'Je sais ce que c’est... de tout perdre à cause d'un souverain fou et sénile…'")  

    console.print("[italic]Un silence lourd retombe. Zyn et Yohna observent Kael avec un mélange de curiosité et de méfiance.[/italic]")  
    console.print("Zyn (voix basse) : 'Nous, on ne veut pas survivre. On veut voir l’Empire brûler comme Yzunfarl.'")  



    choix_invokeurs = Dialogue(
     "Que répondez-vous aux jumeaux ?",
    [
        {
            "text": "C’est suicidaire. Vous devriez penser à vivre.",
            "consequence": lambda h: [
                console.print("Aldric (avec sincérité) : 'Je comprends votre colère. Mais mourir ne vous ramènera pas Yzunfarl. "
                              "Vous êtes jeunes. Vous devriez penser à vivre, à reconstruire ailleurs.'"),
                console.print("Yohna (baissant les yeux, un léger sourire triste aux lèvres) : 'Tu crois qu’on peut juste… abandonner tout ça ?'"),
                console.print("[italic]Elle semble réfléchir, mais son regard brille encore d’une flamme vacillante.[/italic]"),
                console.print("Zyn (froid, regard perçant) : 'Ce monde ne nous a laissé que la haine. "
                              "Tant que Vilmar II respirera, aucune vie ne sera possible pour nous.' (Zyn -10 Yohna +20 )"),
                h.get_relation("Yohna").adjust_score(+20),
                h.get_relation("Zyn").adjust_score(-10)
            ]
        },
        {
            "text": "Personne n’aime l’Empereur… mais il est intouchable.",
            "consequence": lambda h: [
                console.print("Aldric (croisant les bras) : 'Même si je partage votre haine, Vilmar II n'est pas qu’un homme. "
                              "Il est un symbole protégé par l’Empire. Si vous l’attaquez, vous signerez votre arrêt de mort.'"),
                console.print("Yohna (secouant la tête, déçue) : 'Toujours la même rengaine…' (Yohna -10)"),
                console.print("Zyn (plissant les yeux, plus déterminé que jamais) : 'Quelqu’un doit bien finir par essayer. "
                              "On préfère mourir en défiant l’Empire que de vivre en mendiants et en amuseur de cirque.' (Zyn +10)"),
                h.get_relation("Yohna").adjust_score(-10),
                h.get_relation("Zyn").adjust_score(+10)
            ]
        },
        {
            "text": "Vous devriez vous venger. C’est votre droit.",
            "consequence": lambda h: [
                console.print("Aldric (posant sa main sur la garde de son épée) : 'Je ne vous dirai pas de renoncer. "
                              "La vengeance est parfois la seule chose qui nous maintient debout.'"),
                console.print("Yohna (souriant faiblement) : 'Tu es plus honnête que je pensais. Ça fait du bien d’entendre ça.' (Yohna +10)"),
                console.print("Zyn (hoche la tête, un éclat sombre dans les yeux) : 'Tu comprends… mieux que beaucoup ici.' (Zyn +10)"),
                h.get_relation("Yohna").adjust_score(+10),
                h.get_relation("Zyn").adjust_score(+10)
            ]
        }
    ]
    )

    choix_invokeurs.display(hero)


    console.print("[italic]Alors que les jumeaux s'éloignent, Kael s'approche légèrement d'Aldric, le regard pensif.[/italic]")
    console.print("Kael (murmure) : 'Ils ont de la hargne. Je leur reconnais ça. Mais ils finiront par se brûler.'")  
    console.print("Aldric (calme, fixant la cheminée) : 'Peut-être. Mais parfois, il faut laisser brûler ce qui ne peut plus être éteint.'")  
    console.print("[italic]Kael ne répond pas, et les deux hommes rejoignent le reste du groupe, laissant derrière eux la chaleur du feu et la froideur de la vengeance des invokeurs.[/italic]")  


    console.print("\n[bold yellow]Aldric s’installe seul près d’une table basse, jouant distraitement avec une miche de pain tout en observant la flamme dans la cheminée. "
              "Ses pensées dérivent vers Archeon. Ce regard... cette familiarité. Avait-il vraiment déjà vu cet homme ailleurs ? Ou était-ce une illusion savamment tissée par la tour ?[/bold yellow]")  
    console.print("[italic]Chaque mot d'Archeon résonne encore dans son esprit, éveillant un malaise qu'il ne parvient pas à chasser.[/italic]")  

    console.print("[bold cyan]Durnir[/bold cyan] (calme) : 'Les questions qui te rongent ne trouveront pas toutes de réponse ce soir.'")  
    console.print("[italic]Aldric lève les yeux. Le vieux mage s’est approché en silence, s’installant en face de lui avec une tasse fumante dans la main.[/italic]")  

    console.print("Aldric (curieux) : 'Je ne vous ai pas vu approcher…'")  
    console.print("Durnir (souriant doucement) : 'Je marche avec le poids des ans, jeune homme. Il m’arrive d’être aussi léger qu’un souffle.'")  

    console.print("[italic]Un silence confortable s'installe. Seul le crépitement du feu emplit l’espace, jusqu’à ce que Durnir rompe à nouveau le silence.[/italic]")  
    console.print("Durnir : 'Je ne suis pas surpris que tu sois arrivé si haut dans la tour. Je t’ai observé, étage après étage. Tu as cet esprit…'")  
    console.print("Aldric (fronçant les sourcils) : 'Quel esprit ?'")  
    console.print("Durnir : 'Celui qui continue de grimper même quand tout s’effondre autour de lui. Ce genre d’âme finit toujours par se démarquer.'")  


    choix_durnir = Dialogue(
        "Que demandez-vous à Durnir ?",
    [
        {
            "text": "Que savez-vous de cette tour ?",
            "consequence": lambda h: [
                console.print("Aldric (le regard fixé sur Durnir) : 'Vous semblez en savoir plus que vous ne le laissez entendre. "
                              "Que savez-vous vraiment de cette tour ?'"),
                console.print("Durnir (penchant la tête) : 'Pas plus que ce que les vieux livres racontent. La tour a toujours été là. "
                              "Mais sa construction ne relève d’aucune ingénierie humaine.'"),
                console.print("[italic]Son regard s'assombrit légèrement.[/italic]"),
                console.print("Durnir : 'Même l'Empereur et les seigneurs de l’Empire redoutent cette tour. "
                              "C'est là la preuve de sa longévité millénaire.'"),
                console.print("Aldric (pensif) : 'Vous parlez comme si la tour avait sa propre volonté.'"),
                console.print("Durnir (souriant faiblement) : 'Peut-être que c'est le cas… Peut-être pas. Les légendes laissent souvent de la place au doute.'(Durnir +15)"),
                h.get_relation("Durnir").adjust_score(+15)
            ]
        },
        {
            "text": "Avez-vous encore ce livre qui parle de la tour ?",
            "consequence": lambda h: [
                console.print("Aldric (intéressé) : 'Vous aviez mentionné des livres. En avez-vous encore un sur la tour ?'"),
                console.print("Durnir (secouant la tête) : 'Non, malheureusement. Les livres anciens ont été saisis… ou brûlés. "
                              "La peur de ce que nous ne comprenons pas pousse souvent les puissants à détruire ce qui pourrait les éclairer.'"),
                console.print("Aldric : 'Quel dommage…'"),
                console.print("Durnir (d’une voix posée) : 'Les réponses sont peut-être ailleurs, Aldric. "
                              "Ce n’est pas toujours dans les pages que nous trouvons ce que nous cherchons.'(Durnir +10)"),
                h.get_relation("Durnir").adjust_score(+10)
            ]
        },
        {
            "text": "Êtes-vous déjà venu ici auparavant ?",
            "consequence": lambda h: [
                console.print("Aldric (observant Durnir avec insistance) : 'Vous semblez étrangement familier avec cet endroit. "
                              "Est-ce la première fois que vous gravissez la tour ?'"),
                console.print("Durnir (sourire énigmatique) : 'Le temps est un étrange compagnon, Aldric. "
                              "Parfois, il semble nous ramener à des lieux que l’on croyait oubliés…'"),
                console.print("[italic]Le vieux mage ne répond pas directement, laissant planer le doute. "
                              "Aldric choisit de ne pas insister, sentant qu'il n'obtiendra rien de plus pour l'instant.[/italic]")
                
            ]
        }
    ]
    )

    choix_durnir.display(hero)
    console.print("Aldric (se gratte la tête) : Durnir j'ai encore une question..")
    console.print("Durnir : Dites moi !")
    choix_motivation = Dialogue(
        "Que voulez-vous savoir d’autre ?",
    [
        {
            "text": "Pourquoi êtes-vous ici ? Que cherchez-vous vraiment ?",
            "consequence": lambda h: [
                console.print("Aldric : 'Vous semblez avoir vos propres raisons de grimper cette tour. "
                              "Qu’espérez-vous y trouver, Durnir ?'"),
                console.print("Durnir (posant sa tasse) : 'L’Académie d’Urdragen s’effondre. La magie perd du terrain. "
                              "Les décrets anti-magie de l’Empire affaiblissent nos rangs. "
                              "Je crains que bientôt, les mages ne soient plus que des reliques chassées.'"),
                console.print("Aldric (froid) : 'Vous pensez que l’Empire vous traquera jusqu’au dernier ?'"),
                console.print("Durnir (calme) : 'Ils ont peur de ce qu’ils ne contrôlent pas. La tour… pourrait cacher "
                              "un artefact qui redonnera espoir. Ou du moins, une raison de croire.'")
            ]
        },
        {
            "text": "Vous croyez qu’il existe réellement quelque chose au sommet de cette tour ?",
            "consequence": lambda h: [
                console.print("Aldric (dubitatif) : 'Tout le monde monte ici dans l’espoir de trouver quelque chose. "
                              "Mais peut-être qu’il n’y a rien.'"),
                console.print("Durnir (souriant doucement) : 'L’existence même de cette tour est déjà un miracle. "
                              "Elle défie les lois du monde, Aldric. Et parfois, c’est suffisant pour espérer.'")
            ]
        }
    ]
    )

    choix_motivation.display(hero)
    
    console.print("Durnir (se levant avec son thé) : 'Sur ceux mon jeune ami, j'ai un bon vieux grimoir qui m'attend, vous m'en excuserais hehe !'")
    console.print("Aldric : 'Bien sur !'")
    
    console.print("\n[bold red]Clotaire est assis seul près d’une colonne, le regard plongé dans la danse des flammes. "
              "Son visage est marqué par l’ombre du deuil. Emphyr l’observe de loin un instant, puis s’approche silencieusement.[/bold red]")  
    console.print("Emphyr (calme) : 'Ça te ressemble pas de rester silencieux aussi longtemps…'")  
    console.print("[italic]Clotaire ne lève pas les yeux. Il se contente de hausser les épaules, un sourire amer étirant brièvement ses lèvres.[/italic]")  
    console.print("Clotaire : 'C’est juste que… y’a plus personne pour parler à ma place, maintenant.'")  
    console.print("Emphyr (s’installant à côté de lui) : 'Brandio et Velm, c’est ça ?'")  

    console.print("[italic]Clotaire hoche lentement la tête. Il fixe ses mains calleuses, comme si elles portaient encore les traces du sang de ses compagnons perdus.[/italic]")  
    console.print("Clotaire (d’un ton distant) : 'Je les ai rencontrés y’a longtemps. Des années, même. J’étais un môme des bas-fonds… "
              "Un orphelin qui volait pour survivre. C’était ça, ou crever de faim.'")  

#Flashback – Rencontre avec Velm et Brandio : 
    console.print("\n[bold cyan]Clotaire (perdu dans ses souvenirs) : 'Je vivais dans un bordel. C’étaient les filles là-bas qui m’ont élevé… "
              "Elles m’appelaient “leur petit voleur”.'[/bold cyan]")  
    console.print("Clotaire (souriant tristement) : 'Elles disaient que j’avais des doigts de fée, parfaits pour détrousser les nobles distraits. "
              "Elles m’ont appris à parler, à charmer, et à survivre.'")  
    console.print("[italic]Il marque une pause, son regard se durcissant légèrement.[/italic]")  
    console.print("Clotaire : 'Un jour, y’avait ce bateau qui accostait au port. J’vois Velm… enfermé dans une cage. "
              "Ils allaient l’exécuter pour vol. Un simple môme qui essayait juste de bouffer.'")  
    console.print("Emphyr (curieuse) : 'Tu l’as libéré, pas vrai ?'")  

    console.print("[italic]Clotaire hoche la tête avec un éclat fugace dans les yeux.[/italic]")  
    console.print("Clotaire : 'Ouais… Je m’suis infiltré dans le fort cette nuit-là. Mais pendant que j’ouvrais sa cage, "
              "j’suis tombé sur un garde… Brandio.'")  

    console.print("[italic]Un sourire nostalgique éclaire brièvement son visage.[/italic]")  
    console.print("Clotaire : 'Brandio était pas comme les autres. Il m’a pas arrêté. Je crois qu’il s’est juste laissé emporter par mon baratin. "
              "Ou alors, il avait besoin d’une excuse pour quitter cette foutue garde. Il était déjà corrompu jusqu’à l’os de toute façon.'")  

    console.print("Emphyr (amusée) : 'Tu l’as convaincu de déserter sur-le-champ, c’est ça ?'")  
    console.print("Clotaire : 'J’lui ai parlé d’un rêve. D’une terre au-delà des mers… Une femme du bordel m’avait raconté ça quand j’étais gosse. "
              "Des contrées lointaines pleines de richesses, où les bêtes sont plus grandes que des chevaux, ou les batiments sont fait d'or ! "
              "Je leur ai dit qu’on quitterait cet Empire desolant et en lambeaux et qu’on irait là-bas ensemble.'")  

    console.print("[italic]Clotaire laisse échapper un rire sans joie.[/italic]")  
    console.print("Clotaire : 'On y croyait. On a passé des années à amasser de quoi fuir. Sauf qu’on n’aura pas quitté cette tour tout les trois'"
                "On devait recupéré l'artefact, si il existe...et partir loin...ni vu....ni connu...peu importe le moyen")



#Retour au Présent – Emphyr Tente de Le Raisonner :**  

    console.print("Emphyr (doucement) : 'Ce rêve… il vit encore en toi ?'")  
    console.print("[italic]Clotaire ne répond pas immédiatement. Il fixe la flamme, l’ombre de Velm et Brandio flottant derrière ses yeux.[/italic]")  
    console.print("Clotaire : 'Non. Il est mort avec eux. ici...dans cette tour...'")  

    console.print("[italic]Emphyr pose une main légère sur son épaule.[/italic]")  
    console.print("Emphyr (doucement) : 'Ils ne voudraient pas te voir abandonner, Clotaire.'")  
    console.print("Clotaire (amèrement) : 'Peut-être. Mais ce monde, il n’a jamais eu de place pour nous. "
              "On était juste trois reveurs qui essayaient de s’en sortir. 10 ans plus tard ils sont mort et moi je radote de vieux souvenirs'")  

    console.print("[italic]Un silence s’installe à nouveau, mais cette fois, il semble plus léger, comme si Emphyr avait réussi à alléger "
              "ne serait-ce qu’une partie du fardeau de Clotaire.[/italic]")  

    console.print("\n[bold green]Gallius est adossé contre un pilier près de la fenêtre, jouant distraitement avec l’une de ses dagues. "
              "Aldric s’approche, et sans lever les yeux, Gallius devine sa présence.[/bold green]")  
    console.print("Gallius (sans détourner le regard) : 'T’as fini tes discours de héros avec tout le monde ? ?'")  
    console.print("Aldric (souriant) : 'Je tue le temps. Et j'ecouter Clotaire et Emphyr, discretement.'")  
    console.print("[italic]Gallius fait tourner sa dague entre ses doigts, un éclat d’amusement dans les yeux.[/italic]")  
    console.print("Gallius : 'Ah… Il s’accroche encore. Je suppose qu’on doit tous porter nos fantômes d’une manière ou d’une autre.'")  

#Gallius se Livre :**  
    console.print("[italic]Un silence s’installe alors qu’ils regardent l’Empire à travers l'arche qui mene à la terasse' "
              "Aldric s’appuie contre le même pilier, observant Gallius du coin de l’œil.[/italic]")  
    console.print("Aldric (curieux) : 'Et toi ? Pourquoi tu es là ?'")  

    console.print("[italic]Gallius ricane doucement, levant finalement les yeux vers Aldric.[/italic]")  
    console.print("Gallius : 'Tu veux vraiment savoir ? Je suis un assassin. Rien de plus.'")  
    console.print("Gallius (léger sourire) : 'Je viens du sud, de Qaziera. Là-bas, on dit que tant qu’il y a des hommes, il y aura toujours du travail.'")  
    console.print("[italic]Il marque une pause, jouant distraitement avec la lame.[/italic]")  
    console.print("Gallius : 'J’ai tué des généraux en pleine bataille. Des seigneurs dans leurs châteaux. Des prêtres devant leurs autels. "
                "Certains m’appellent “l'ombre de Qaziera”. Mais pour moi… c’est juste un boulot.'")  

    console.print("Aldric (fronçant les sourcils) : 'Et maintenant ?'")  
    console.print("Gallius (en baillant): 'Hm… Maintenant, les contrats manquent. J’ai tellement “fait le ménage” que je suis à court de cibles.'")  
    console.print("[italic]Il rit brièvement, un rire sec et sans joie.[/italic]")  
    console.print("Gallius : 'Alors je suis venu ici. J’me suis dit que la tour, c’était comme des congés. Tu vois, un peu de repos… au sommet du chaos.'")  


    choix_gallius = Dialogue(
        "Que répondez-vous à Gallius ?",
    [
        {
            "text": "Tu prends ça à la légère… Mais ça pourrait bien te tuer.",
            "consequence": lambda h: [
                console.print("Aldric (croisant les bras) : 'La tour n’est pas un terrain de jeu. "
                              "Tu sais que tu risques ta vie à chaque étage.'"),
                console.print("Gallius (haussement d’épaules) : 'Je risque ma vie chaque fois que je respire. "
                              "Mais t’inquiète pas pour moi. J’ai survécu à pire.'"),
                console.print("[italic]Gallius semble amusé, mais une lueur plus sérieuse traverse brièvement ses yeux.[/italic](Gallius +5)"),
                h.get_relation("Gallius").adjust_score(+5)
            ]
        },
        {
            "text": "Tu dois vraiment aimer ça… Le sang, la chasse.",
            "consequence": lambda h: [
                console.print("Aldric : 'On dirait que t’as pas besoin d’une raison pour tuer. "
                              "C’est naturel, chez toi.'"),
                console.print("Gallius (sourire en coin) : 'Peut-être bien. "
                              "La chasse, c’est comme respirer. Facile. Mais tu sais ce qui est difficile ? Arrêter.'"),
                console.print("[italic]Gallius s’appuie contre le pilier, l’air détendu, mais ses yeux restent perçants.[/italic](Gallius +10)"),
                h.get_relation("Gallius").adjust_score(+10)
            ]
        },
        {
            "text": "Tu crois que la tour peut vraiment t’apporter quelque chose ?",
            "consequence": lambda h: [
                console.print("Aldric (calmement) : 'Tu parles comme si tout ça n’avait aucune importance. "
                              "Mais au fond, pourquoi tu grimpes encore plus haut ?'"),
                console.print("Gallius (baisse les yeux un instant) : 'Je me le demande moi-même. "
                              "Peut-être qu’au sommet, y’aura plus rien à chasser. "
                              "Ou peut-être que je trouverai enfin quelque chose d’assez fort pour m’arrêter.'"),
                console.print("[italic]Un silence s’installe. Gallius garde un air impassible, mais Aldric sent un éclat de vérité dans ses mots.[/italic]"),
                h.get_relation("Gallius").adjust_score(+15)
            ]
        }
    ]
    )

    choix_gallius.display(hero)
    
    console.print("[italic]Gallius range finalement sa dague, se redressant lentement.[/italic]")  
    console.print("Gallius : 'Allez, c’est assez de confidences pour aujourd’hui. "
              "Je vais jeter un œil à cette fameuse boîte… Peut-être qu’elle a quelque chose à m’offrir.'")  
    console.print("Aldric (en souriant) : 'Si elle cache un contrat, je te le laisse.'")  
    console.print("[italic]Gallius éclate de rire en s’éloignant, laissant Aldric seul avec ses pensées.[/italic]")  

    console.print("\n[bold magenta]Emphyr est assise près de la cheminée, les flammes projetant des ombres dansantes sur son visage. "
              "Elle tend ses mains vers le feu, l’air pensif, tandis que la pluie martèle doucement les vitres.[/bold magenta]")  
    console.print("[italic]Aldric s’approche lentement, cherchant à se réchauffer lui aussi. Emphyr lève brièvement les yeux vers lui, mais ne dit rien.[/italic]")  
    console.print("Aldric : 'Clotaire va bien ?'")  
    console.print("Emphyr (soupirant doucement) : 'Il s’en remettra. Mais tu sais que ce n’est pas à moi de dire ça.'")  
    console.print("Aldric (baissant les yeux) : 'Je n’ai pas voulu tuer un de ses amis… Ça s’est imposé.'")  
    console.print("Emphyr (légère amertume) : 'Je sais. La tour impose ses choix. Et toi, tu les exécutes.'")  

#Les Secrets d'Emphyr :**  
    console.print("[italic]Un silence s’installe, seulement brisé par le crépitement du feu. Aldric observe la femme, intrigué par cette aura raffinée et distante.[/italic]")  
    console.print("Aldric (curieux) : 'Je me demande… Pourquoi une femme comme toi s’engagerait dans la tour ?'")  
    console.print("[italic]Emphyr sourit légèrement, posant son menton sur sa main, son regard se perdant dans les flammes.[/italic]")  
    console.print("Emphyr : 'J’ai mes petits secrets.'")  
    console.print("Aldric : 'Oh, je n’en doute pas.'")  

    console.print("[italic]Elle glisse son regard vers lui, l’ombre d’un amusement dans les yeux.[/italic]")  
    console.print("Emphyr (doucement) : 'Mais si tu veux savoir… Je travaille pour l’Empereur.'")  
    console.print("[italic]Aldric marque une pause, surpris. Il fronce les sourcils, cherchant à déceler si elle plaisante.[/italic]")  
    console.print("Aldric : 'L’Empire a envoyé quelqu’un dans la tour. Ça ne me surprend pas. "
              "Quand il s’agit de cupidité, Vilmar et ses courtisans savent y faire.'")  
    console.print("Emphyr (amusée) : 'Tu parles comme si tu connaissais l’Empire mieux que moi.'")  

    console.print("Aldric : 'Je l’ai vu s’effondrer, en même temps que l’état mental de Vilmar II. "
              "Et toi, comment tu as survécu jusque-là ? Tu n’as rien montré de… remarquable.'")  
    console.print("[italic]Emphyr se redresse, et du bout des doigts, elle caresse doucement la joue d’Aldric, "
              "son sourire s’étirant mystérieusement.[/italic]")  
    console.print("Emphyr (souriante) : 'C’est un autre de mes secrets.'")  



#Dialogue – Approfondir ou Rompre la Distance :

    choix_emphyr = Dialogue(
        "Que répondez-vous à Emphyr ?",
    [
        {
            "text": "[bold magenta] 'Tu es pleine de mystères… Mais ça me plaît.' (Flirt) [/bold magenta]",
            "consequence": lambda h: [
                console.print("Aldric (léger sourire) : 'J'aime garder le mystere autour de moi'"),
                console.print("[italic]Emphyr arque un sourcil, un éclat joueur dans le regard.[/italic]"),
                console.print("Emphyr (doucement) : 'Ce genre de garçons, avec un regard déterminé… Je les aime bien.' (Emphyr +20)"),
                h.get_relation("Emphyr").adjust_score(+20)
            ]
        },
        {
            "text": "[bold yellow] 'Je doute que l’Empire cherche quoi que ce soit d’altruiste ici.' [/bold yellow]",
            "consequence": lambda h: [
                console.print("Aldric : 'L’Empire n’a jamais agi sans raison cachée. Toi non plus, j’imagine.'"),
                console.print("[italic]Emphyr esquisse un sourire fin.[/italic]"),
                console.print("Emphyr : 'Tu apprends vite. Mais parfois, la survie impose des alliances.'"),
                h.get_relation("Emphyr").adjust_score(+5)
            ]
        },
        {
            "text": "[bold red] 'Tu dois vraiment beaucoup à l’Empereur pour risquer ta vie ici.' [/bold red]",
            "consequence": lambda h: [
                console.print("Aldric (sérieusement) : 'Il t’a envoyé ici, mais qu’est-ce qu’il t’a donné en échange ?'"),
                console.print("[italic]Emphyr détourne brièvement les yeux, jouant avec une mèche de ses cheveux.[/italic]"),
                console.print("Emphyr (à voix basse) : 'Il m’a recueillie. Pas directement… mais un prince électeur l’a fait.'"),
                h.get_relation("Emphyr").adjust_score(-5)
            ]
        }
    ]
    )   
    choix_emphyr.display(hero)
    
    console.print("[italic]Aldric se redresse, mais il sent que la confidence d’Emphyr n’est pas passée inaperçue.[/italic]")  
    console.print("Kael (restant dans l’ombre) : '[italic]Hm… Elle travaille pour l’Empire…[/italic]'")  
    console.print("[italic]Kael ne dit rien de plus, mais Aldric devine que son ancien rival ne manquera pas de garder ça à l’esprit.[/italic]")  

    console.print("[italic]Plus tard, Ayela s’approche d’Aldric, les bras croisés, une lueur de jalousie dans le regard.[/italic]")  
    console.print("Ayela : 'Tu passes beaucoup de temps avec cette fille… Je devrais m’inquiéter ?'")  

    choix_ayela = Dialogue(
        "Comment répondez-vous à Ayela ?",
    [
        {
            "text": "Ce n’est rien, juste une conversation.",
            "consequence": lambda h: [
                console.print("Aldric (souriant) : 'Tu sais que tu es la seule à m’inquiéter, Ayela.'"),
                console.print("[italic]Ayela rougit légèrement mais détourne le regard.[/italic]"),
                h.get_relation("Ayela").adjust_score(+10)
            ]
        },
        {
            "text": "J’ai besoin de connaître tout le monde ici. Y compris Emphyr.",
            "consequence": lambda h: [
                console.print("Aldric (calmement) : 'On doit tous s’entendre. Je m’assure que personne ne nous poignarde dans le dos.'"),
                console.print("Ayela (hochant la tête) : 'Hm… Ouais. Ça se tient.'"),
                h.get_relation("Ayela").adjust_score(+0)
            ]
        }
    ]
    )
    choix_ayela.display(hero)
    
    console.print("\n[bold green]Ayela attrape discrètement la main d’Aldric, l’entraînant à l’écart des autres. "
              "Ils s’arrêtent dans un coin sombre de la salle, près d’une fenêtre donnant sur la pluie battante.[/bold green]")  
    console.print("Ayela (à voix basse) : 'Je voulais te parler… sans qu’on soit dérangés.'")  
    console.print("[italic]Aldric croise son regard. L’inquiétude se lit dans ses yeux verts, voilée par une ombre de mélancolie.[/italic]")  
    console.print("Aldric (calme) : 'Qu’est-ce qui te tracasse ?'")  
    console.print("Ayela (hésitante) : 'J’ai peur… Je ne veux pas mourir ici. Je sais que c’est stupide…'")  

    console.print("[italic]Elle s’appuie contre le mur, jouant nerveusement avec une mèche de ses cheveux.[/italic]")  
    console.print("Ayela : 'Je pensais que… fuir dans cette tour était la solution. J’espérais trouver un remède… "
              "Mais je crois que j’étais juste une gamine effrayée qui voulait fuir la réalité.'")  
    console.print("Aldric (doucement) : 'Tu es plus forte que tu ne le crois. Tu as survécu jusqu’ici.'")  
    console.print("Ayela (léger sourire) : 'Peut-être… mais tu me connais. J’ai toujours été impulsive. "
              "Petite, je rêvais de quitter la forêt. Je voulais chasser des créatures légendaires comme le cerf doré de Hurfal…'")  
    console.print("[italic]Son regard s’illumine brièvement, mais s’assombrit presque aussitôt.[/italic]")  
    console.print("Ayela : 'Mais maintenant… Je me demande si je verrai encore un matin.'")  


##Dialogue – Romance ou Amitié :**  

    choix_ayela_intime = Dialogue(
        "Que répondez-vous à Ayela ?",
    [
        {
            "text": "[bold magenta](Relation +80) 'Tu n’as pas à affronter ça seule…' (Romance) [/bold magenta]",
            "condition": lambda h: h.get_relation("Ayela").score >= 80,
            "consequence": lambda h: [
                console.print("[italic]Aldric s’approche doucement, glissant ses doigts le long de la joue d’Ayela.[/italic]"),
                console.print("Aldric (chuchotant) : 'Je suis là. On affrontera cette tour ensemble.'"),
                console.print("[italic]Ayela s’appuie contre lui, fermant brièvement les yeux comme pour savourer ce moment éphémère.[/italic]"),
                console.print("Ayela (souriant) : 'Tu devrais savoir… Je suis tombée amoureuse d’un idiot impulsif qui fonce toujours tête baissée.'"),
                console.print("[italic]Aldric ne répond pas, se contentant de glisser une main autour d’elle, partageant la chaleur du moment.[/italic](Ayela +10)"),
                h.get_relation("Ayela").set_relationship_type("Romance"),
                h.get_relation("Ayela").adjust_score(+10)
            ]
        },
        {
            "text": "[bold yellow](Relation +80) 'Je préfère qu’on reste amis. Mais je serai toujours là.' [/bold yellow]",
            "condition": lambda h: h.get_relation("Ayela").score >= 80,
            "consequence": lambda h: [
                console.print("Aldric (doucement) : 'Je tiens à toi, Ayela. Mais pour l’instant, mieux vaut qu’on se concentre sur la tour.'"),
                console.print("[italic]Ayela baisse les yeux un instant, puis hoche doucement la tête, compréhensive.[/italic]"),
                console.print("Ayela (souriante mais résignée) : 'Je comprends… La tour ne nous laisse pas vraiment le temps pour autre chose.'"),
                console.print("[italic]Malgré tout, Aldric sent qu’un lien profond s’est formé entre eux.[/italic](Ayela -5)"),
                h.get_relation("Ayela").set_relationship_type("Ami"),
                h.get_relation("Ayela").adjust_score(-5)
            ]
        },
        {
            "text": "[bold yellow] 'Tu n’es pas seule. Tu es plus forte que tu le crois.' [/bold yellow]",
            "condition": lambda h: h.get_relation("Ayela").score < 80,
            "consequence": lambda h: [
                console.print("Aldric (souriant) : 'Je sais que tu n’aimes pas l’admettre, mais tu es bien plus forte que tu ne le crois.'"),
                console.print("Ayela (légèrement émue) : 'C’est gentil… Je suis contente de t’avoir rencontré, Aldric.'"),
                console.print("[italic]Aldric tape doucement sur l’épaule d’Ayela, ramenant une atmosphère plus légère entre eux.[/italic]"),
                h.get_relation("Ayela").adjust_score(+0)
            ]
        }
    ]
    )
    choix_ayela_intime.display(hero)
    
    console.print("[italic]Alors qu’ils retournent près du feu, Aldric remarque Kael appuyé contre une colonne, observant la scène sans un mot.[/italic]")  
    console.print("Kael (calme) : '[italic]Hm… Elle s’attache trop facilement…[/italic]'")  
    console.print("[italic]Kael détourne rapidement le regard lorsqu’Ayela s’approche.[/italic]")  

    console.print("Ayela (bousculant légèrement Aldric) : 'Tu sais… Je commence à me demander ce que tu fais vraiment avec Emphyr. "
              "Tu devrais peut-être faire attention.'")  

    choix_jalousie = Dialogue(
        "Que répondez-vous à Ayela ?",
    [
        {
            "text": "Tu es la seule dont je me soucie vraiment.",
            "consequence": lambda h: [
                console.print("Aldric (amusé) : 'Emphyr, hein ? Tu n’as rien à craindre. "
                              "Tu es la seule personne dont je me soucie vraiment ici.'"),
                console.print("[italic]Ayela sourit malicieusement, clairement satisfaite de la réponse.[/italic]"),
                h.get_relation("Ayela").adjust_score(+5)
            ]
        },
        {
            "text": "Ne sois pas jalouse. On est tous du même côté.",
            "consequence": lambda h: [
                console.print("Aldric (léger sourire) : 'Tu n’as pas à t’inquiéter. "
                              "On survit mieux quand on s’entend bien avec tout le monde.'"),
                console.print("Ayela (levant un sourcil) : 'Hmph. J’espère que c’est vrai…'"),
                h.get_relation("Ayela").adjust_score(+0)
            ]
        }
    ]
    )
    choix_jalousie.display(hero)
    
    console.print("\n[bold cyan]Les heures passent lentement. Chacun des participants s’occupe comme il peut, savourant ce court répit offert par la tour.[/bold cyan]")

    console.print("[italic]Assis près de l’âtre, Garen retire ses bottes usées, étendant ses pieds endoloris. "
              "Les semelles abîmées témoignent du long périple qu’il a enduré jusqu’ici.[/italic]")

    console.print("[bold]Kael[/bold] (souriant légèrement) : 'Des bottes pareilles… Tu devrais les laisser ici. Elles n'atteindront pas l'étage suivant.'")
    console.print("[bold]Garen[/bold] (grognant) : 'Elles sont pas belles, mais elles tiennent. Ça me suffit.'")
    console.print("[italic]Kael secoue la tête, amusé, mais il n’y a plus cette pointe de condescendance habituelle dans sa voix.[/italic]")
    console.print("[bold]Kael[/bold] (d'un ton sincère) : 'Je plaisante, gamin. Respect pour être allé aussi loin. T’aurais pu abandonner depuis longtemps.'")
    console.print("Garen (souriant timidement) : 'Tant qu’on avance…'")

    console.print("[italic]Pendant ce temps, Durnir s’approche silencieusement de la boîte au centre de la salle. "
              "Ses doigts glissent sur la surface froide et lisse, traçant les lignes gravées presque invisibles à l’œil nu.[/italic]")
    console.print("[bold]Durnir[/bold] (murmurant) : 'Quel genre de magie êtes-vous… ?'")
    
    console.print("\n[italic]Tandis que les flammes crépitent doucement, Yohna se dirige discrètement vers Aldric, s’asseyant à ses côtés.[/italic]")
    console.print("[bold]Yohna[/bold] (curieuse) : 'Tu n’as jamais dit pourquoi tu es venu ici. On parle tous de nos raisons… sauf toi.'")

    console.print("[italic]Ayela, adossée contre un mur proche, lève la tête et acquiesce doucement.[/italic]")
    console.print("[bold]Ayela[/bold] : 'C’est vrai… Même Garen s’est confié. Mais toi, Aldric, tu gardes tout pour toi.'")
    console.print("[bold]Garen[/bold] (hochant la tête) : 'Ouais, c’est louche ça. T’as pas envie de parler ?'")

    console.print("[italic]Aldric hésite un instant, observant les flammes comme s’il cherchait ses mots. "
              "Il ouvre la bouche, mais avant qu’il ne puisse dire quoi que ce soit, une voix cynique s’élève derrière lui.[/italic]")

    console.print("[bold]Clotaire[/bold] (sarcastique) : 'Laissez-moi deviner. Il est venu ici pour savourer son petit droit de vie ou de mort. "
              "Ce genre de tour attire toujours les sadiques dans son genre.'")
    
    choix_tension = Dialogue(
        "Que faites-vous face à la provocation de Clotaire ?",
    [
        {
            "text": "Écouter Yohna, Ayela et Garen et apaiser la situation.",
            "consequence": lambda h: [
                console.print("[bold]Yohna[/bold] (se levant) : 'Ça suffit, Clotaire. Personne n’a besoin de ça maintenant.'"),
                console.print("[bold]Ayela[/bold] (croisant les bras) : 'Tu n'es pas le seul à avoir perdu des proches ici. Laisse-le tranquille.'"),
                console.print("[bold]Garen[/bold] (plus ferme) : 'On est dans la même galère. Inutile de chercher des ennemis supplémentaires.'"),
                console.print("[italic]Le regard de Clotaire s’assombrit, mais il détourne finalement les yeux, murmurant pour lui-même.[/italic](Ayela, Yohna et Garen +10)"),
                console.print("[bold]Emphyr[/bold] : 'Oh encore...Ca suffit Clotaire...tes provocations ne riment a rien désormais..'"),
                h.get_relation("Yohna").adjust_score(+10),
                h.get_relation("Ayela").adjust_score(+10),
                h.get_relation("Garen").adjust_score(+10)
            ]
        },
        {
            "text": "Laisser Clotaire provoquer et se rapprocher de Kael et Gallius.",
            "consequence": lambda h: [
                console.print("[bold]Kael[/bold] (haussant les épaules) : 'Il n’a pas tort. Cette tour transforme tout le monde.'"),
                console.print("[bold]Gallius[/bold] (calme, sans lever les yeux) : 'Le droit de vie ou de mort, c’est pas si mal comme distraction.'"),
                console.print("[italic]Aldric garde le silence, se rapprochant instinctivement de Kael et Gallius, laissant Clotaire poursuivre.(Clotaire,Gallius et Kael +10)[/italic]"),
                console.print("[bold]Zyn[/bold]: 'Oui entretuait vous ! je commencer a m'ennuyer !'"),
                h.get_relation("Kael").adjust_score(+10),
                h.get_relation("Gallius").adjust_score(+10),
                h.get_relation("Clotaire").adjust_score(+10),
                h.get_relation("Zyn").adjust_score(+10)
            ]
        }
    ]
    )

    choix_tension.display(hero)


    console.print("\n[italic]Avant que les tensions ne puissent s’envenimer davantage, une présence imposante s’élève derrière eux.[/italic]")
    console.print("[bold red]Archeon[/bold red] (s’approchant lentement) : 'Hm… Juste à temps, n’est-ce pas ?'")

    console.print("[italic]Il se tient derrière la boîte, posant ses mains dessus. "
              "Le simple contact semble insuffler une énergie étrange à la salle.[/italic]")
    console.print("[bold]Archeon[/bold] (calme) : 'Gardez vos forces pour ce qui vient. Vous en aurez besoin.'")
    console.print("[italic]Clotaire lance un dernier regard à Aldric avant de se détourner en silence. "
              "Les conversations s’estompent peu à peu alors que chacun retourne à sa place, prêt pour ce qui se profile à l’horizon.[/italic]")
    
    console.print("\n[italic]Le crépitement du feu est le seul bruit qui persiste alors qu'Archeon reste immobile, "
              "les mains toujours posées sur la boîte, comme s'il écoutait ce que personne d'autre ne pouvait entendre.[/italic]")
    console.print("[bold]Archeon[/bold] (sans se retourner) : 'Reposez-vous. À l’aube… tout changera.'")


    console.print("\n[italic]La nuit s’épaissit autour de la salle, et la fatigue finit par peser sur chaque participant. "
              "Certains s’étendent sur les tapis, d'autres s’assoupissent adossés aux colonnes ou près de la cheminée.[/italic]")

    console.print("[bold]Ayela[/bold] (doucement) : 'Aldric… Tu comptes rester debout toute la nuit ?'")
    console.print("[italic]Elle s’approche, posant une main légère sur l’épaule d’Aldric. "
              "Son regard cherche quelque chose, une réponse silencieuse.[/italic]")

    choix_repos = Dialogue(
        "Que faites-vous pour la nuit ?",
    [
        {
            "text": "[bold yellow](Relation +80) Passer la nuit avec Ayela.[/bold yellow]",
            "condition": lambda h: h.get_relation("Ayela").score >= 80 and h.get_relation("Ayela").relationship_type == "Romance",
            "consequence": lambda h: [
                console.print("[italic]Aldric se tourne vers Ayela, croisant son regard sous la lueur du feu. "
                              "Il hoche lentement la tête, et elle l’accompagne vers un coin plus isolé de la salle.[/italic]"),
                console.print("[bold]Ayela[/bold] (souriant doucement) : 'Je n’ai jamais aimé dormir seule.'"),
                console.print("[italic]Les deux s’installent côte à côte, partageant la chaleur et le réconfort de leur présence mutuelle.[/italic]"),
                console.print("[italic]Pour un court instant, la tour n’existe plus.[/italic](Ayela +10)"),
                h.get_relation("Ayela").adjust_score(+10)
            ]
        },
        {
            "text": "Dormir près de vos compagnons d’infortune (Garen, Gallius, Yohna, Zyn, Kael).",
            "consequence": lambda h: [
                console.print("[italic]Aldric s’approche du cercle formé près du feu où Garen, Yohna, Zyn et Kael sont déjà installés.[/italic]"),
                console.print("[bold]Garen[/bold] (lui lançant une couverture) : 'Tiens. Ça te fera du bien aussi.'"),
                console.print("[italic]Gallius s’appuie contre un pilier, un sourire discret au coin des lèvres.[/italic]"),
                console.print("[bold]Gallius[/bold] : 'On dirait une bande de survivants. Pas mal, hein ?'"),
                console.print("[bold]Kael[/bold] (moqueur) : 'On finira peut-être par apprécier ce répit, pour une fois.'"),
                console.print("[italic]Les derniers mots échappent à Yohna, sa voix s’éteignant alors qu’elle s’endort paisiblement, "
                              "tandis que Zyn veille silencieusement, comme toujours.[/italic]"),
                console.print("[italic]Dans ce cercle fragile, Aldric trouve une paix inattendue, même si ce n'est que pour quelques heures.[/italic](Gallius, Kael, Garen, Zyn et Yohna +10)"),
                h.get_relation("Garen").adjust_score(+10),
                h.get_relation("Kael").adjust_score(+10),
                h.get_relation("Gallius").adjust_score(+10),
                h.get_relation("Yohna").adjust_score(+10),
                h.get_relation("Zyn").adjust_score(+10)
            ]
        }
    ]
    )

    choix_repos.display(hero)
    
    console.print("\n[italic]Tandis que chacun trouve enfin le sommeil, Archeon reste éveillé. "
              "Seul, face à la boîte mystérieuse, il semble murmurer quelque chose que personne d’autre n’entend.[/italic]")

    console.print("[bold red]Archeon[/bold red] (murmurant) : 'L’aube approche. Certains resteront… d'autres non.'")
    console.print("[italic]Et lentement, la salle s’enfonce dans un silence profond, seulement troublé par le crépitement des braises mourantes.[/italic]")
    
    console.print("\n[bold cyan]=== L'Aube Silencieuse ===[/bold cyan]")
    console.print(
        "[italic]Les premiers rayons du soleil, voilés par des nuages gris, filtrent à travers les hautes fenêtres. "
        "La fine pluie tapote doucement contre les vitres, créant une atmosphère paisible mais lourde.[/italic]"
    )
    console.print("[bold]Archeon[/bold] (assis près de la boîte, un livre entre les mains) : 'Lève-toi… Le jour commence.'")

    console.print("[italic]Un à un, les participants émergent lentement de leur sommeil. "
              "Certains s'étirent, d'autres restent silencieux, l'esprit encore embué par la fatigue.[/italic]")
    console.print("[bold]Kael[/bold] (regardant Garen enlever ses bottes trouées) : 'Heh… Tu pourrais faire fortune en vendant ces trucs comme antiquités.'")
    console.print("[bold]Garen[/bold] (soupirant) : 'Elles ont fait du chemin… Mais je ne suis pas sûr qu’elles iront beaucoup plus loin.'")
    console.print("[italic]Kael sourit, mais il n'y a pas la même arrogance qu'avant. "
              "Un respect discret s’installe entre eux, forgé par les épreuves passées.[/italic]")
    
    console.print(
    "[italic]Les participants se rassemblent progressivement autour de la boîte noire. "
    "Archeon referme calmement son livre, levant les yeux vers eux.[/italic]"
    )   
    console.print("[bold]Archeon[/bold] : 'Vous viendrez chacun votre tour dans la salle d’à côté. '")
    console.print("Archeon (posant une main sur la boîte) : 'Une fois cela fait, vous pourrez prendre quelque chose ici, "
              "et continuer vers la salle suivante.'")
    console.print("Archeon (regardant la porte) : 'L’étage suivant… est une charnière. Vous serez préparés.'")

    console.print("[italic]Un silence pesant accompagne ses mots. "
              "La boîte semble vibrer doucement sous ses mains, comme si elle attendait ce moment depuis longtemps.[/italic]")
    
    console.print("[bold]Archeon[/bold] (calmement) : 'Durnir. À toi.'")
    console.print("[italic]L'archimage Durnir s'avance, sa robe froissée par la nuit, mais son regard reste vif. "
              "Il entre dans la salle sans un mot.[/italic]")

    console.print("Archeon : 'Zyn. Yohna.'")
    console.print("[italic]Les jumeaux s’échangent un regard, puis disparaissent à leur tour derrière la porte.[/italic]")

    console.print("Archeon : 'Kael.'")
    console.print("[italic]Kael avance lentement, jetant un regard vers Aldric, comme pour dire 'à plus tard'.[/italic]")

    console.print("Archeon : 'Emphyr.'")
    console.print("[italic]Emphyr passe à son tour, laissant derrière elle une légère fragrance de parfum ancien.[/italic]")

    console.print("Archeon : 'Ayela. Gallius. Clotaire.'")
    console.print("[italic]Un à un, les autres participants passent, jusqu'à ce qu'il ne reste plus qu'Aldric et Garen dans la salle principale.[/italic]")
    console.print("[bold]Garen[/bold] (inquiet, pieds nus) : 'Tu crois… qu’il va se passer quoi là-dedans ?'")

    choix_garen = Dialogue(
        "Que dites-vous à Garen ?",
    [
        {
            "text": "L'encourager. 'Tu peux le faire, Garen. T’es allé trop loin pour reculer maintenant.'",
            "consequence": lambda h: [
                console.print("[bold]Aldric[/bold] (tapotant l’épaule de Garen) : 'Fais-moi confiance. Ça ira.'"),
                console.print("[italic]Garen inspire profondément, puis hoche la tête avec un faible sourire.[/italic]"),
                console.print("[bold]Garen[/bold] (faiblement) : 'Merci… T’es le seul qui croit encore en moi.'"),
                h.get_relation("Garen").adjust_score(+10)
            ]
        },
        {
            "text": "Se montrer distant. 'Si tu n’y vas pas, quelqu’un d’autre prendra ta place.'",
            "consequence": lambda h: [
                console.print("[italic]Garen baisse les yeux, secouant doucement la tête.[/italic]"),
                console.print("[bold]Garen[/bold] (murmure) : 'Ouais… Adieu, Aldric. Juste au cas où.'"),
                h.get_relation("Garen").adjust_score(-10)
            ]
        }
    ]
    )

    choix_garen.display(hero)
    
    console.print("[italic]Aldric entend son il rentre dans la piece voisine, une salle de marbre elcairée a la torce, Archeon se tient devant lui avec la boite[/italic]")
    console.print("Archeon : 'Le meilleur pour la fin n'est ce pas ? Aldric...vas y c'est a ton tour de piocher dans la boite'")
    
    console.print("[italic]Garen franchit lentement la porte, disparaissant à son tour. "
              "Son adieu résonne encore dans l'esprit d'Aldric alors qu'il reste seul dans la salle.[/italic]")

    console.print("[bold]Archeon[/bold] (légèrement amusé) : 'Le meilleur pour la fin… n'est-ce pas, Aldric ?'")

    console.print("[italic]Aldric s'approche lentement, l'air méfiant. "
              "Les flammes vacillantes des torches projettent l’ombre d’Archeon sur les murs de pierre. "
              "La boîte noire trône devant eux, comme un vestige oublié.[/italic]")

    console.print("[bold]Archeon[/bold] : 'Tu sens cette aura, n'est-ce pas ? Cette boîte ne t'est pas étrangère.'")
    console.print("[bold]Aldric[/bold] (fronçant les sourcils) : 'Pourquoi dites-vous ça ?'")

    console.print("[bold]Archeon[/bold] (regardant fixement Aldric) : 'Parce que tu es déjà venu ici… "
              "Il y a longtemps. Avec ton père.'")

    console.print("[italic]Le cœur d’Aldric manque un battement. "
              "Des fragments de mémoire éclatent dans son esprit : un homme aux cheveux bruns et un sourire franc, "
              "portant une épée trop grande pour un simple voyageur… et un autre homme, plus sombre, toujours à ses côtés.[/italic]")

    console.print("[bold]Aldric[/bold] (voix basse) : 'Je… je ne me souviens que d'ombres. Vous insinuez que mon père a atteint cet étage ?'")
    console.print("[bold]Archeon[/bold] (calme) : 'Oui. Lui… et son compagnon.'")

    console.print("[italic]Aldric observe Archeon, scrutant ses moindres gestes. "
              "Il sent qu'il y a plus dans ces paroles qu'Archeon ne laisse paraître.[/italic]")

    choix_pere = Dialogue(
        "Que demandez-vous à Archeon ?",
    [
        {
            "text": "Que s’est-il passé lors de leur ascension ?",
            "consequence": lambda h: [
                console.print("Aldric (fixant Archeon) : 'Ils sont allés plus loin que cet étage, n'est-ce pas ?'"),
                console.print("Archeon (avec un sourire énigmatique) : 'Ils ont gravé leur nom et même leur sang dans la pierre de cette tour… "
                              "Mais seuls les véritables survivants en parlent encore.'"),
                console.print("Aldric : 'Vous les avez connus. Je le vois dans vos yeux.'"),
                console.print("Archeon (se tournant légèrement) : 'Je connais beaucoup d'histoires… "
                              "Mais celle-là est la tienne désormais.'"),
                h.get_relation("Archeon").adjust_score(+10)
            ]
        },
        {
            "text": "Pourquoi ne pas me dire la vérité ?",
            "consequence": lambda h: [
                console.print("Aldric (plus froidement) : 'Vous savez ce qui est arrivé à mon père. "
                              "Pourquoi tourner autour du pot ?'"),
                console.print("Archeon (croisant les bras) : 'La vérité n’est pas un don gratuit, Aldric. "
                              "Elle se mérite… comme tout dans cette tour.'"),
                console.print("Aldric (le regard perçant) : 'Je finirai par la découvrir. Même si vous refusez de me la donner.'"),
                console.print("Archeon (avec un rictus) : 'Je n’en doute pas.'"),
                h.get_relation("Archeon").adjust_score(-5)
            ]
        },
        {
            "text": "Je ne veux pas savoir. Le passé est mort.",
            "consequence": lambda h: [
                console.print("Aldric (détournant le regard) : 'Ce qui est arrivé avant n’a plus d’importance.'"),
                console.print("Archeon (calme) : 'Tu dis cela maintenant… Mais la tour a une façon bien à elle de réveiller les fantômes.'"),
                console.print("[italic]Archeon observe Aldric un moment, puis désigne la boîte du menton.[/italic]"),
                console.print("[bold]Archeon[/bold] : 'Va. Pioche ton destin. Comme ton père l’a fait avant toi.'")
            ]
        }
    ]
    )
    choix_pere.display(hero)
    
    console.print("[italic]Aldric plonge la main dans la boîte. Lorsqu'il la retire, un frisson glacial parcourt son bras. "
              "Sa vision vacille un instant, comme si le monde autour de lui ralentissait, les bruits devenant lointains.[/italic]")

    console.print("[bold cyan]Vous obtenez le Margith'r de Blink.[/bold cyan]")

    console.print("[italic]Une lueur bleutée danse brièvement autour des doigts d'Aldric. "
              "Il ressent une étrange légèreté dans ses muscles, comme si son corps était en décalage avec l’espace qui l’entoure.[/italic]")

    console.print("[bold]Archeon[/bold] (observant calmement) : 'Blink… Un don rare. Celui de franchir l'instant, de traverser l'espace comme si le temps lui-même se contractait.'")

    console.print("Aldric (testant la sensation) : 'C’est… déroutant. Je sens que je peux me déplacer en un clin d’œil. Mais ce pouvoir me paraît… limité.'")

    console.print("[bold]Archeon[/bold] (hochement de tête) : 'Il l’est. Blink ne te permettra pas de traverser des murs ou de fuir un destin inévitable…' "
              "[italic](Son regard s'assombrit un bref instant.)[/italic] "
              "'Mais utilisé au bon moment, il peut changer l’issue d’un combat. Un souffle, une fraction de seconde peut suffire pour survivre.'")

    console.print("[italic]Aldric serre le poing, ressentant cette pulsation nouvelle parcourir ses veines. "
              "Il comprend que Blink n’est pas simplement une capacité… c’est une arme qui, entre de bonnes mains, peut déjouer la mort.[/italic]")

    console.print("[bold]Archeon[/bold] (pointant du doigt une porte latérale) : 'Avant de poursuivre, équipe-toi. L’étage suivant… n’aura aucune pitié pour ceux qui sont mal préparés.'")

    console.print("[italic]Aldric suit la direction indiquée et aperçoit une large salle de pierre, éclairée par des lanternes magiques. "
              "Des étagères s'étendent le long des murs, remplies de lames affûtées, d’armures légères et lourdes, ainsi que divers artefacts scintillants. "
              "Des mannequins de cuir portent des équipements marqués de symboles oubliés.[/italic]")

    console.print("Aldric (en observant la salle) : 'Est-ce là une autre épreuve ?'")

    console.print("[bold]Archeon[/bold] (léger sourire) : 'Non. Ici, tu peux prendre ce dont tu as besoin. "
              "Considère cela comme une offrande de la tour… pour ceux qui sont dignes d'atteindre cet étage.'")

    console.print("[italic]Aldric s’avance lentement, effleurant du bout des doigts une épée d'obisienne d'une conception inconnue et d'une forme unique "
              "Il se souvient des paroles d’Archeon… et de cette étrange sensation de déjà-vu.[/italic]")

    console.print("[italic]Aldric prend le pantalon noir de combat ainsi qu'un haut de corps moulant noir avec des bettelles en cuir"
                  "Il pris aussi un bandeau a motif qu'il attache sur ses cheveux blond mi-long, il pris l'epée d'obisienne et la rangea"
                  "c'etait une épée legere rapide qui se tenait devant soi et horizontalement, parfait pour le blink"
                  "Il pris aussi des couteaux de lancer et enfila des bottes noir de combat renformcé et des gants en cuir laissant passer ses doigts [/italic]")

    console.print("[italic]Aldric s’équipe en silence. Il ressent le poids des décisions qu'il prend, "
              "chaque vetements et armes semblant lier son avenir à la tour. "
              "Derrière lui, Archeon observe sans mot dire.[/italic]")

    console.print("[bold]Archeon[/bold] (calmement) : 'Tu poursuis l’ascension, Aldric…'")

    console.print("Aldric (relevant la tête) : 'Pourquoi cette tour m’appelle-t-elle ? Je n’ai jamais compris pourquoi j’ai mis les pieds ici.'")

    console.print("[bold]Archeon[/bold] (voix basse) : 'Parce que tu connaissais déjà ton but, même avant de poser un pied sur le premier étage. "
              "Ton père t’a laissé des questions sans réponses. Tu cherches des vérités enfouies. La tour a vu cet écho dans ton cœur…'")

    console.print("[italic]Aldric sent une pression invisible autour de lui. "
              "Les paroles d'Archeon résonnent, éveillant un sentiment étrange qu'il peine à identifier.[/italic]")

    console.print("[bold]Archeon[/bold] (le regard perçant) : 'Tu es exactement là où tu dois être.'")

    console.print("[italic]Aldric ne répond pas immédiatement. Il ajuste son équipement, prêt à affronter l’étage suivant. "
              "Le regard d’Archeon ne le quitte pas, comme s’il évaluait quelque chose de plus profond… quelque chose qu’Aldric ignore encore lui-même.[/italic]")
    
    console.print("\n[bold cyan]=== Fin de l'Étage 7 : Le Silence Avant l'Orage ===[/bold cyan]")  

    console.print("[italic]Aldric franchit la porte menant à l’étage suivant, laissant derrière lui la chaleur du feu et la sérénité éphémère de la salle de repos. "
              "Devant lui s’étend un long corridor menant à une salle ouverte où l’escalier vers l’étage 8 se dresse, imposant et silencieux.[/italic]")  

    console.print("[italic]Il retrouve les autres participants, rassemblés devant l’escalier. "
              "Certains ajustent leurs nouvelles armes, d’autres contemplent leur reflet dans l’acier poli de leurs lames. "
              "L’atmosphère légère de la veille s’est dissipée, laissant place à une tension palpable.[/italic]")  

    console.print("[bold]Kael[/bold] (examinant une dague finement ouvragée) : 'Hmph… Ça devrait suffire. "
              "Les vrais guerriers n’ont pas besoin de s’en vanter.'")  
    console.print("[italic]Zyn fait tourner une sphère en cristal dans sa main, murmurant quelques incantations discrètes tandis que Yohna reajuste ses brassieres, "
              "observant les autres avec prudence. Même Garen, fraîchement équipé d’une armure legere neuve, semble différent. "
              "Ses bottes, cette fois à sa taille, ne grincent plus sous son poids.[/italic]")  

    console.print("Garen (ajustant ses brassards) : 'C’est la première fois que j’ai un équipement neuf… Ça change tout.'")  
    console.print("Aldric (lui donnant une tape sur l’épaule) : 'Il était temps. Peut-être que tu ressembleras enfin à un vrai combattant.'")  
    console.print("Garen (riant doucement) : 'J’espère. Merci, Aldric.'")  

    console.print("[italic]Pourtant, malgré les sourires discrets, chacun garde pour lui la nature exacte de ce qu’il a reçu dans la salle de la boîte. "
              "Le Margith’r est un pouvoir personnel, et dans cette tour, tout secret peut être une arme précieuse.[/italic]")  

    console.print("[bold]Archeon[/bold] (s’avançant devant l’escalier) : 'Ceux qui se tiennent ici ont été choisis. "
              "Mais vous n’êtes pas les seuls à avoir foulé ces marches.'")  
    console.print("[italic]Il marque une pause, laissant ses mots s'imprimer dans l'esprit des survivants.[/italic]")  

    console.print("[bold]Archeon[/bold] (voix grave) : 'Priez pour les 87 âmes tombées avant vous durant votre ascension"
              "Ils ont été brisés par la tour, mais leur sacrifice vous a mené jusqu’ici. "
              "Remerciez la chance qui vous a permis de survivre. Chaque pas de plus est un privilège que beaucoup n’auront jamais.'")  

    console.print("[italic]Les participants restent silencieux, certains baissant la tête, d’autres fixant l’escalier en réfléchissant aux camarades perdus en chemin.[/italic]")  
    console.print("[bold]Clotaire[/bold] (murmurant) : 'Brandio… Velm…'")  
    console.print("Yohna (fermant brièvement les yeux) : 'Les morts ne reviennent pas. Ne les oublions pas, mais avançons.'")  

    console.print("[italic]Durnir incline légèrement la tête, murmurant une prière en ancien dialecte, tandis qu’Ayela serre son arc contre sa poitrine.[/italic]")  

    console.print("[bold]Archeon[/bold] (calme, mais ferme) : 'Vous êtes dix. C’est ce nombre qui gravira l’étage 8.'")  
    console.print("[italic]D’un geste lent, il s’écarte de l’entrée, posant une main sur la rambarde de l’escalier.[/italic]")  
    console.print("[bold]Archeon[/bold] : 'Je vous retrouverai là-haut. Continuez d’avancer… car c’est exactement là où vous devez être.'")  

    console.print("[italic]Un frisson parcourt Aldric. Ces mots semblent l’atteindre d’une manière qu’il ne peut expliquer. "
              "Il croise le regard perçant d’Archeon une dernière fois avant de se détourner, posant un pied sur la première marche.[/italic]")  

    console.print("[bold]Il reste 10 participants.[/bold]")

    game_menu.display()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#chapitre 8 Le Tournoi 

def floor8_tournament(hero):
    from rich.console import Console
    console = Console()

    console.print("\n[bold cyan]=== Étape 8 : L'Arène du Jugement ===[/bold cyan]")
    
    # Entrée dans la salle
    console.print(
        "[italic]Les lourdes portes de l'étage 8 s'ouvrent lentement, laissant échapper un courant d’air glacial. "
        "Derrière, l’obscurité règne. Les dix survivants avancent à pas mesurés dans la pièce silencieuse.[/italic]"
    )

    console.print("Kael (regardant autour) : 'Pourquoi est-ce toujours aussi sinistre…?'")
    console.print("Ayela (voix basse) : 'C'est fait exprès. Ça nous met sous pression avant même de commencer.'")
    console.print("Garen (frémissant légèrement) : 'On vient de passer une nuit à peine reposante et maintenant… ça recommence déjà.'")

    # Archeon fait son entrée
    console.print(
        "[bold red]Archeon[/bold red] (sa voix résonne) : 'Bienvenue... dans l'épreuve du duel. "
        "Vous êtes montés haut… mais jusqu’où irez-vous vraiment ?'"
    )
    console.print("[italic]Sa silhouette surgit lentement des ombres, drapée dans son manteau rouge. "
                  "Son regard acéré balaye chacun des participants, s'arrêtant brièvement sur Aldric.[/italic]")

    # Les torches s'allument
    console.print(
        "[italic]D’un claquement de doigts, Archeon fait s’illuminer une à une des torches fixées aux murs. "
        "Elles dévoilent progressivement une vaste arène de pierre suspendue au-dessus d’un gouffre insondable. "
        "Deux ponts étroits relient la plateforme à la salle principale.[/italic]"
    )
    
    console.print("Garen (fixant l'arène) : 'Une… arène ?'")
    console.print("Durnir (fronçant les sourcils) : 'Un terrain de duel… Voilà une épreuve archaïque, mais efficace.'")
    console.print("Zyn (croisant les bras) : 'Ça va être intéressant.'")

    # Présence des deux portes
    console.print(
        "[italic]Deux portes massives se dressent au fond de la pièce, gardant leur mystère. "
        "Elles restent scellées, mais l’intuition des participants sent qu’elles joueront un rôle crucial.[/italic]"
    )
    console.print("Kael (désignant les portes) : 'Et ça ?'")

    # Explication du tournoi
    console.print("[bold red]Archeon[/bold red] (calme) : 'Ces portes s’ouvriront… quand vous aurez prouvé votre valeur. "
                  "Cette épreuve est simple : un tournoi.'")
    console.print(
        "[bold red]Archeon[/bold red] : 'Chacun d'entre vous devra affronter un autre participant. "
        "Le but n'est pas nécessairement de tuer, mais de vaincre. Si votre adversaire abandonne, concède sa défaite "
        "ou est jugé hors de combat par moi… alors le combat prend fin.'"
    )
    
    console.print("Archeon (laissant un silence planer) : 'Cependant…' [italic]Il marque une pause, laissant le silence s'épaissir.[/italic]")
    console.print(
        "Archeon (lentement) : 'La mort n'est pas interdite. Si vous tuez votre adversaire avant la fin du duel, cela ne sera pas puni. "
        "Mais… après la fin du combat, tout acte de meurtre entraînera votre propre élimination.'"
    )

    # Réactions des participants
    console.print("[italic]Le groupe échange des regards lourds. Le poids de cette règle est clair : ce tournoi est une démonstration de force et de maîtrise… pas de massacre.[/italic]")
    console.print("Ayela (calme mais sérieuse) : 'Il va falloir se retenir…'")
    console.print("Garen (toussotant nerveusement) : 'Et si on ne tient pas ? Je veux dire… j’ai jamais fait ça. Pas contre vous tous…'")
    console.print("Kael (moqueur) : 'Relax, Garen. Je suis sûr que tu survivras… peut-être un tour ou deux.'")
    console.print("Garen (baissant la tête) : 'C’est pas drôle.'")

    # Clotaire se montre provocateur
    console.print("Clotaire (sourire en coin) : 'Oh, c’est très drôle. J’ai hâte de voir certains tomber. Ça fait longtemps que j’attends ça…'")
    console.print("Emphyr (croisant les bras) : 'Arrête, Clotaire. Ce genre de provocation est inutile maintenant.'")
    console.print("Clotaire (sec) : 'Ce n’est pas une provocation. Juste une observation. Certains ici sont là par accident. Il est temps de faire du tri.'")

    # Tension montante
    console.print("[italic]L’atmosphère devient plus pesante. Garen baisse la tête, mais serre les poings. "
                  "Zyn jette un regard amusé à Clotaire, tandis qu’Ayela se rapproche d’Aldric en silence.[/italic]")

    # Archeon calme la situation
    console.print(
        "[bold red]Archeon[/bold red] (froidement) : 'Gardez votre colère pour l’arène. Ce soir, vous devrez prouver ce que vous valez.'"
    )
    
    console.print(
        "[italic]Les participants s’éloignent lentement du bord de l’arène. Certains murmurent entre eux, tandis que d'autres s’isolent, se préparant mentalement.[/italic]"
    )
    
    # Ajout après l'explication d'Archeon
    console.print("[italic]Alors que les participants se dispersent lentement, Ayela et Garen s’approchent d’Aldric. "
              "Le regard de Garen est anxieux, tandis qu'Ayela semble plus pensive.[/italic]")

    console.print("Ayela (doucement) : 'Aldric… Tu penses quoi de tout ça ? Ce tournoi… C’est absurde non ?'")
    console.print("Garen (fronçant les sourcils) : 'Ouais… Et si on perd, mais qu’on reste en vie… Qu’est-ce qui va se passer ?'")

# Choix de dialogue
    choix_tournoi = Dialogue(
        "Que répondez-vous à Ayela et Garen ?",
    [
        {
            "text": "Rassurer Garen : 'Tant qu’on ne meurt pas, on peut encore avancer.'",
            "consequence": lambda h: [
                console.print("Aldric (souriant légèrement) : 'Ne t’inquiète pas, Garen. Tant qu’on est debout, on avance. "
                              "Perdre un duel ici n’est sans doute pas la fin du chemin.'"),
                console.print("Garen (soulagé) : 'Ouais… T’as peut-être raison. Merci Aldric.' (Garen +10)"),
                h.get_relation("Garen").adjust_score(+10)
            ]
        },
        {
            "text": "Honnêteté : 'Ce tournoi va nous séparer… Certains n’iront pas plus loin.'",
            "consequence": lambda h: [
                console.print("Aldric (voix basse) : 'Soyons réalistes… Tout le monde n’ira pas jusqu’au bout. "
                              "Ce tournoi est une sélection. Ceux qui perdent resteront derrière.'"),
                console.print("Ayela (inquiète) : 'Je m’en doutais… Ça fait peur.'"),
                console.print("Garen (baissant la tête) : 'J’aurais aimé ne pas l’entendre…' (Ayela -5, Garen -5)"),
                h.get_relation("Ayela").adjust_score(-5),
                h.get_relation("Garen").adjust_score(-5)
            ]
        },
        {
            "text": "Déterminé : 'On ne perdra pas. Peu importe qui se dresse sur mon chemin.'",
            "consequence": lambda h: [
                console.print("Aldric (avec détermination) : 'Peu importe qui je dois affronter. Je gagnerai.'"),
                console.print("Ayela (sourire en coin) : 'T’as l’air sûr de toi… Je compte bien voir ça.' (Ayela +10)"),
                console.print("Garen (timidement) : 'C’est… rassurant de t’entendre dire ça.' (Garen +5)"),
                h.get_relation("Ayela").adjust_score(+10),
                h.get_relation("Garen").adjust_score(+5)
            ]
        }
    ]
    )

    choix_tournoi.display(hero)
    
    # 🎴 Tirage au sort des participants
    console.print("\n[bold cyan]Archeon claque des doigts. Un vase de cristal orné de runes anciennes apparaît au centre de la salle, "
              "posé sur un piédestal de pierre noire. À l'intérieur, des boules gravées tournent lentement, "
              "comme si elles réagissaient à la présence de chacun des participants.[/bold cyan]")

    console.print("[bold]Archeon[/bold] (d’une voix grave) : 'La tour observe… Elle juge. Ce tournoi est plus qu’une simple épreuve. "
              "Il vous confronte à vous-même, à vos désirs et à vos faiblesses. Ce n’est pas le plus fort qui l’emporte toujours, "
              "mais celui qui sait lire au-delà des lames.'")

    console.print("[italic]Un silence pesant s’installe. Les participants échangent des regards furtifs, pesant chaque mot. "
              "Clotaire, en retrait, fixe le vase comme s’il connaissait déjà l’issue du tirage. "
              "Ayela serre son arc avec une légère nervosité, tandis que Garen détourne les yeux, cherchant réconfort auprès d’Aldric.[/italic]")

    console.print("[bold]Archeon[/bold] : 'L’issue du combat vous appartient. Les règles sont simples :"
              "\n- Vaincre ou se rendre."
              "\n- Un duel ne se termine que par l’abandon, la mise hors de combat… ou la mort.'")
    console.print("[italic]Il laisse sa dernière phrase flotter un instant, s’assurant que tous comprennent les implications de cet affrontement.[/italic]")

    console.print("[bold]Archeon[/bold] : 'Je n’interviendrai qu’en cas de victoire claire. Ceux qui attaquent après la défaite de leur adversaire… "
              "se condamneront eux-mêmes.'")

    console.print("[italic]D’un geste fluide, Archeon fait tournoyer les boules dans le vase. "
              "Elles s’élèvent une à une, dans une danse silencieuse, avant que l’une d’elles ne s’immobilise.[/italic]")

    console.print("[bold yellow]La première boule s’ouvre lentement… et révèle le nom d’Ayela.[/bold yellow]")
    console.print("[bold]Archeon[/bold] : 'Ayela.'")

    console.print("[italic]Ayela prend une profonde inspiration et s’avance vers l’arène. "
              "Son regard balaie la salle, s’arrêtant brièvement sur Aldric avant de se poser sur l’arène vide.[/italic]")

    console.print("[bold yellow]La deuxième boule s’élève doucement, lévitant devant les yeux de tous… Clotaire.[/bold yellow]")
    console.print("[bold]Archeon[/bold] : 'Clotaire.'")

# 🎴 Réactions de Clotaire et Emphyr
    console.print("[italic]Clotaire se redresse, un sourire en coin. Il échange un regard discret avec Emphyr.[/italic]")
    console.print("Emphyr (chuchotant) : 'Je pensais que tu espérais affronter Aldric.'")
    console.print("Clotaire (voix basse) : 'Pourquoi gâcher ce plaisir tout de suite ? Ayela suffira. Je n’ai pas besoin d’y aller fort.'")
    console.print("Emphyr (fronçant les sourcils) : 'Tu prends ça trop à cœur.'")
    console.print("Clotaire : 'Allons allons ce n'est qu'un duel ! J'aimerais ne pas trop m'épuiser pour la suite.'")

# 🎴 Dialogue avec Ayela avant le combat
    console.print("[italic]Avant qu'elle ne descende dans l'arène, Ayela s'approche discrètement d'Aldric. "
              "Ses yeux trahissent une certaine inquiétude, mais elle masque cela sous un sourire léger.[/italic]")

    choix_ayela_duel = Dialogue(
    "Que dites-vous à Ayela avant son duel contre Clotaire ?",
    [
        {
            "text": "[bold yellow](Relation +50)[/bold yellow] 'Ne sous-estime pas Clotaire. Garde tes distances et sois rapide.'",
            "condition": lambda h: h.get_relation("Ayela").score >= 50,
            "consequence": lambda h: [
                console.print("Aldric (calme) : 'Clotaire a changé. Ce duel ne sera pas simple.'"),
                console.print("Ayela (hochement de tête) : 'Je sais… mais je peux le battre. Je ne me laisserai pas avoir.' (Ayela +10)"),
                h.get_relation("Ayela").adjust_score(+10)
            ]
        },
        {
            "text": "'Tu n’as aucune chance. Abandonne.'",
            "consequence": lambda h: [
                console.print("Aldric (croisant les bras) : 'Ne fais pas l’idiote. Tu sais que Clotaire ne te fera aucun cadeau.'"),
                console.print("Ayela (fixant Aldric) : 'Je croyais que tu avais plus de foi en moi…' (Ayela -20)"),
                h.get_relation("Ayela").adjust_score(-20)
            ]
        },
        {
            "text": "[bold yellow](Romance)[/bold yellow] 'Ne prends aucun risque. Reviens vers moi après ce duel.'",
            "condition": lambda h: h.get_relation("Ayela").relationship_type == "Romance",
            "consequence": lambda h: [
                console.print("Aldric (glissant sa main dans la sienne) : 'Je t’attendrai. Ne fais pas de folies.'"),
                console.print("Ayela (souriant tendrement) : 'Tu pourrais me donner envie de survivre, tu sais…' (Ayela +15)"),
                h.get_relation("Ayela").adjust_score(+15)
            ]
        },
        {
            "text": "[bold yellow](Romance)[/bold yellow] 'Si tu te sens en danger… abandonne. Je préfère te savoir en vie.'",
            "condition": lambda h: h.get_relation("Ayela").relationship_type == "Romance",
            "consequence": lambda h: [
                console.print("Aldric (d’une voix plus douce) : 'Promets-moi que si ça tourne mal, tu n’hésiteras pas à abandonner.'"),
                console.print("Ayela (le regard brillant) : 'Je… je ne veux pas te décevoir. Mais si c’est ce que tu veux…'"),
                console.print("[italic]Elle presse doucement la main d’Aldric avant de s’éloigner, sans se retourner.[/italic] (Ayela +20)"),
                h.get_relation("Ayela").adjust_score(+20)
            ]
        }
    ]
)

    choix_ayela_duel.display(hero)

# 🎴 Tension croissante
   # Début du Duel - Arène de l'Étage 8
    console.print("\n[bold red]Archeon[/bold red] (d’une voix forte, levant le bras) : 'Le duel commence… maintenant !'")

    console.print(
    "[italic]Les torches s'embrasent une à une autour de l’arène. "
    "Ayela avance calmement, mais la tension dans ses épaules trahit sa nervosité. "
    "Clotaire, de l'autre côté, ajuste son épée à sa ceinture sans se presser, ses yeux rivés sur elle avec une intensité glaciale.[/italic]"
    )

    console.print("Clotaire (sourire en coin) : 'On va bien s’amuser, Ayela… Je vais te faire danser comme Brandio et Velm n’ont jamais pu le faire.'")
    console.print("[italic]Ayela ne répond pas, mais sa prise sur son arc se raffermit.[/italic]")

    console.print("Garen (inquiet) : 'Tu crois qu'elle peut gagner ?'")
    console.print("Kael (croisant les bras) : 'Elle n'a pas le choix, Clotaire est surement le plus mauvais choix pour elle...'")

    console.print("[bold cyan]Ayela[/bold cyan] (sans quitter Clotaire des yeux) : 'Je suis prête. Il ne me fera pas tomber aussi facilement.'")

# Première Salve
    console.print(
    "[italic]Ayela lève son arc dans un éclair doré et décoche trois flèches de lumière d'un tir précis. "
    "Les projectiles illuminent l’arène, filant à une vitesse vertigineuse vers Clotaire.[/italic]"
        )

    console.print(
    "[italic]Mais Clotaire bondit à gauche, ses mouvements fluides comme une ombre, laissant les flèches frapper dans le vide.[/italic]"
    )
    console.print("Clotaire (ricanant) : 'Vraiment ? C'est tout ce que tu as ?'")
    console.print("[italic]Il s’élance vers Ayela et, en un battement de cils, se dédouble. "
              "Ses illusions frappent sans relâche.[/italic]")

    console.print("[bold red]Clotaire[/bold red] : 'Trop lente !'")

    console.print("[italic]Ayela vacille sous l’impact. Du sang coule de sa lèvre, mais elle garde son arc levé.[/italic]")
    console.print("Garen (inquiet) : 'AYELA !!'")

# Illusions et Pression
    console.print("[italic]Clotaire se multiplie à nouveau. Vingt silhouettes de lui encerclent Ayela, "
              "se moquant dans une cacophonie déstabilisante.[/italic]")

    console.print("Clotaire (provoquant) : 'Allez, tire encore. Peut-être que tu toucheras quelque chose cette fois.'")
    console.print("[italic]Ayela n’écoute pas. Ses yeux balayent les illusions, cherchant la faille.[/italic]")

    console.print("Durnir (à voix basse) : 'Ses illusions… ce n’est pas qu’un tour de passe-passe. "
              "Elles sont réelles… mais il y a une faiblesse.'")

# Choix de Dialogue - Analyser Clotaire
    choix_analyse_clotaire = Dialogue(
        "Garen (désespéré) : 'Aldric… tu vois quelque chose ? Il doit bien avoir une faille !'",
    [
        {
            "text": "C'est une question de chance. (Kael hoche la tête)",
            "consequence": lambda h: [
                console.print("Aldric (haussant les épaules) : 'Il suffit d’un bon tir… Si Ayela est rapide, elle pourra le toucher.'"),
                console.print("Kael (soufflant) : 'Ouais… mais contre Clotaire, ça relèverait du miracle.'"),
            ]
        },
        {
            "text": "Il faut le frapper partout en même temps. (Zyn et Gallius approuvent)",
            "consequence": lambda h: [
                console.print("Aldric : 'S’il se multiplie, frappons chaque illusion. Il n’est qu’un parmi les autres.'"),
                console.print("Zyn : 'Exact. Une solution brutale… mais efficace.'"),
                console.print("Gallius (hochement de tête) : 'Simple, mais ça pourrait marcher.'"),
            ]
        },
        {
            "text": "Il y a un tressaillement quand il échange sa place… (Durnir approuve)",
            "consequence": lambda h: [
                console.print("Aldric (focalisé) : 'Quand il se transpose dans l'une de ses illusions… il y a un bref flottement. Une faille.'"),
                console.print("Durnir (hochant la tête) : 'Hm… belle observation. Voyons si Ayela pourra l'exploiter." 
                              "ses illusions ne font pas de degats mais sa materialisation oui..c'est la tout le secret"
                              "il se transpose rapidement, un pouvoir fourbe mais puisant si bien utilisé'"),
                h.get_relation("Durnir").adjust_score(+10)
            ]
        }
    ]
    )
    choix_analyse_clotaire.display(hero)

# Ayela Contre-Attaque
    # Contre-Attaque d'Ayela – Frappe Ciblée
    console.print("[italic]Ayela, respirant lourdement, frotte violemment l’extrémité de sa flèche contre la pierre de l’arène. "
              "Des étincelles s’élèvent alors qu’elle traîne la pointe lumineuse au sol, traçant un cercle incandescent.[/italic]")

    console.print("Kael (fronçant les sourcils) : 'Qu’est-ce qu’elle fait… ?'")

    console.print("[italic]Ayela s’agenouille, adoptant une posture stable, la corde de son arc tendue au maximum. "
              "Clotaire la fixe, intrigué, mais amusé par ce geste inattendu.[/italic]")

    console.print("Clotaire (ricanant) : 'Quoi, tu pries maintenant ? Ce ne sont pas des dieux qui vont te sauver, Ayela.'")

    console.print("[italic]Mais Ayela ne répond pas. Ses yeux sont rivés sur Clotaire et ses illusions. "
              "Lorsque la flèche quitte la corde, une salve de projectiles éclatants jaillit à sa suite, "
              "se divisant en une pluie de lumière. Les flèches se dispersent, traquant chaque illusion dans leur sillage.[/italic]")

    console.print("Garen (ébloui) : 'Regarde ça… Elle détruit toutes les illusions d’un seul coup !'")

    console.print("[italic]Les doubles de Clotaire explosent un à un, réduits en fragments de lumière. "
              "Une des flèches effleure l’épaule de Clotaire, lui laissant une entaille fine et fumante.[/italic]")

    console.print("Kael (soupirant, avec un léger sourire) : 'C’est fini… Elle l’a eu. Clotaire ne peut plus se cacher derrière ses illusions.'")

    console.print("Clotaire (grimaçant, serrant les dents) : 'Tch… Pas mal, mais pas suffisant.'")

    console.print("[italic]Clotaire s’immobilise, mais une fraction de seconde plus tard, il disparaît de la trajectoire. "
              "Ayela reste concentrée sur ce qu’il reste des illusions devant elle, ignorant un détail crucial…[/italic]")

    console.print("[bold red]Clotaire[/bold red] (d’une voix calme derrière elle) : 'Je suis là… Ayela.'")


    console.print("[italic]Avant qu’elle ne puisse réagir, Clotaire, apparu derrière elle, enfonce sa lame dans son dos. "
              "La flèche qu’elle tenait glisse de ses doigts alors qu’elle vacille lentement, la douleur se lisant dans ses yeux.[/italic]")
    
    Console.print("Aylea : 'Arrrg...aahh'")

    console.print("Kael (hurlant) : 'Merde !!!'")

    console.print("Garen (effondré) : 'AAAAAAAAAAAAAAAAAAAAAAH AYELAAAAAAAAA !!!!!")

    console.print("[italic]Clotaire relâche lentement Ayela qui tombe à genoux, puis s’effondre sur les dalles froides. "
              "Il la regarde silencieusement, une ombre de regret passant brièvement dans son regard.[/italic]")

    console.print("[bold red]Clotaire[/bold red] (murmurant) : 'Tu étais trop dangereuse.'")

# Réactions du Groupe
    console.print("[italic]Kael détourne le regard, les poings serrés, tandis que Garen tombe à genoux, le regard vide. "
              "Aldric reste figé, incapable de détourner les yeux du corps sans vie d’Ayela.[/italic]")

    console.print("Durnir (voix grave) : 'Elle a failli l’avoir… Une guerrière jusqu’au bout.'")

    console.print("Clotaire (s’adressant au groupe, d’un ton neutre) : 'C’est la tour qui décide. Et elle ne fait jamais de cadeaux.'")

    console.print("[italic]Clotaire recule lentement, laissant la dépouille d’Ayela derrière lui. "
              "La flamme des torches semble vaciller sous le poids du silence. "
              "Archeon, impassible, lève simplement la main pour annoncer la fin du duel.[/italic]")

    console.print("[bold red]Archeon[/bold red] : 'Clotaire est vainqueur. Le duel est terminé.'")
    
    # Après la mort d’Ayela – Atmosphère pesante
    console.print("[italic]Un silence pesant enveloppe l’arène. Même les flammes des torches semblent vaciller faiblement, comme si elles respectaient ce moment de deuil.[/italic]")

    console.print("Garen (la voix brisée et a genoux) : 'Non… Ayela…'")

    console.print("Kael (froid, fixant Clotaire) : 'Il n’y avait… aucune raison d’aller aussi loin.'")

    console.print("[italic]Clotaire n’adresse aucun regard à ses compagnons d'infortune,  Il s’éloigne de l’arène, allant s’asseoir dans l’ombre, loin des autres. "
              "Ses mains tremblent légèrement, mais il les serre pour masquer ce trouble. Loin d’un sourire arrogant, son expression semble figée, impassible.[/italic]")

    console.print("[bold red]Clotaire[/bold red] (murmurant pour lui-même) : 'Je… je l’ai fait. C’est ce qu’il fallait...Je crois..'")

    console.print("[italic]Pourtant, au fond de lui, une vague de malaise grandit. "
              "C’était la première fois qu’il ôtait une vie. Malgré ses paroles tranchantes, la victoire n’avait rien d’agréable.[/italic]")
    
    console.print("Emphyr (s'approchant de Clotaire): Premiere fois que tu tue hein ? Tu jouer les gros dur finalement...")
    
    console.print("Clotaire : 'Hm..'")
    
    console.print("Emphyr : 'Ca te passera, faut une premiere fois a tout même si elle meritait pas ça la pauvre..'")
    
    console.print("Clotaire : Je...je ne voulait pas...je crois...je ne sais plus Emphyr...")

# Aldric s’approche du corps d’Ayela
    console.print("[italic]Aldric avance lentement, les poings serrés. Il s’agenouille près du corps inerte d’Ayela, posant une main sur son épaule froide. "
              "Son cœur est lourd, et pour la première fois depuis longtemps, il sent la colère monter, brûlante mais maîtrisée.[/italic]")

    console.print("Aldric (à voix basse) : 'Je suis désolé… Je t’avais promis…'")

    console.print("[italic]Sans un mot de plus, il soulève doucement Ayela, l’éloignant de l’arène pour l’allonger avec soin à l’écart. "
              "Kael et Garen le rejoignent silencieusement, baissant la tête en guise de respect.[/italic]")

    console.print("Garen (poings tremblants) : 'Je… je vais le tuer…'")

    console.print("Kael (posant une main sur son épaule) : 'Ce n’est pas le moment… Je sais ce que tu ressens, mais on doit rester en vie.'")

    console.print("[italic]Garen détourne les yeux, mais il n’ajoute rien. L’atmosphère est pesante, chaque souffle semble un fardeau.[/italic]")

# Archeon observe discrètement
    console.print("[italic]Archeon, jusqu’alors spectateur impassible, détourne légèrement le regard. "
              "Si ses traits restent figés, un observateur attentif pourrait y déceler une lueur fugace d’inconfort. "
              "Un sentiment qu’il enterre rapidement.[/italic]")

    console.print("[bold red]Archeon[/bold red] (après un instant de silence) : 'Le tournoi doit continuer…'")

    console.print("[italic]Avec un geste mesuré, il tend la main vers le vase de cristal. "
              "Les boules recommencent à flotter lentement en cercle, attirant l’attention des participants encore sous le choc.[/italic]")

# Prochain tirage – Durnir contre Yohna
    console.print("[italic]La première boule s’élève lentement, baignée dans une faible lumière bleue. "
              "Les participants lèvent les yeux vers elle, alors qu’une voix résonne.[/italic]")

    console.print("[bold cyan]Archeon[/bold cyan] : 'Durnir…'")

    console.print("[italic]Durnir avance calmement, sans afficher la moindre émotion. "
              "Le vieil archimage ajuste sa cape d’un geste lent, ses yeux s’attardant brièvement sur Aldric, comme s’il évaluait sa réaction.[/italic]")

    console.print("[italic]La seconde boule s’élève aussitôt, se teintant cette fois d’un éclat vert doux.[/italic]")

    console.print("[bold cyan]Archeon[/bold cyan] : 'Yohna…'")

    console.print("Zyn (fronçant les sourcils) : 'Fais attention… Ne le sous-estime pas, Yohna. Si tu sens que ça chauffe abandonne'")

    console.print("Yohna (lui jetant un regard en coin) : 'Je sais. Je ne suis pas aussi tête brûlée que toi.'")

    console.print("[italic]Les deux adversaires avancent vers l’arène, se positionnant face à face. "
              "Durnir observe calmement Yohna, tandis que la jeune invocatrice frappe dans ses mains face a face, concentrée.[/italic]")

    console.print("[bold red]Archeon[/bold red] : 'Que ce duel commence.'")
    
    console.print("[italic]Les deux adversaires avancent vers l’arène, se positionnant face à face. "
              "Durnir ajuste calmement les plis de sa robe, tandis que Yohna frappe doucement dans ses mains, "
              "comme pour s’échauffer. L’éclat du sceptre qu’elle tient miroite légèrement sous les torches.[/italic]")

    console.print("Durnir (avec un sourire bienveillant) : 'Je te promets, jeune fille, que je ne te tuerai pas. "
              "Je n’aime pas utiliser la magie pour ôter des vies inutilement.'")

    console.print("Yohna (roulant des yeux) : 'Pas besoin de me ménager, le vieux. Je suis pas là pour jouer à papi-gateau.'")

    console.print("[italic]Un éclat malicieux traverse les yeux de Yohna. Sans attendre, elle lève son bras "
              "et une bourrasque d’air vert prend la forme d’un faucon, fondant droit sur Durnir.[/italic]")

    console.print("Zyn (souriant) : 'Bien envoyé, Yohna ! Montre-lui ce que tu sais faire !'")

    console.print("[italic]Durnir lève simplement la main, traçant un cercle dans l’air. Une barrière translucide se forme, "
              "dissipant l’attaque du faucon en une pluie d’étincelles d’air.[/italic]")

    console.print("Durnir (ricanant) : 'Ah, tu commences fort ! Hah… la jeunesse et son insouciance.'")

    console.print("Emphyr (bras croisés) : 'C’est trop simple… Ce vieux bougre ne va pas s’avouer vaincu si facilement.'")

# Yohna riposte immédiatement
    console.print("[italic]Yohna recule d’un bond et, sans perdre de temps, invoque un dragon-serpent d’eau. "
              "La créature serpente rapidement à travers l’arène, se jetant sous les pieds de Durnir avant "
              "de refermer ses mâchoires gigantesques dans un fracas d’eau rugissant.[/italic]")

    console.print("[bold cyan]Zyn[/bold cyan] (fier) : 'Bien joué, Yohna ! Ça devrait le ralentir !'")

    console.print("[italic]Les spectateurs retiennent leur souffle, s’attendant à ce que l’archimage soit immobilisé… "
              "Mais au même moment, une lumière bleue éclate à travers les crocs du serpent aqueux.[/italic]")

# Durnir contre-attaque
    console.print("[italic]Durnir récite lentement une incantation dans une langue ancienne, "
              "sa voix devient progressivement plus forte et assourdissante. "
              "Tous se bouchent les oreilles face à cette vibration magique, même Yohna grimace de douleur.[/italic]")

    console.print("[bold]Durnir[/bold] (voix tonitruante) : '[bold yellow]Lour gan di vouuuuuuuuuuuur ![/bold yellow]'")

    console.print("[italic]Une tête gigantesque, réplique magique de Durnir lui-même, surgit dans les airs "
              "au-dessus de Yohna. La créature hurlante projette des ondes de choc, balayant le sol de l’arène.[/italic]")

    console.print("Kael (fronçant les sourcils) : 'Ce n’est pas normal… Il maîtrise la magie avec une précision chirurgicale.'")
    
    console.print("Aldric (encore sous tension suite a la mort de l'archère) : Hm..")

# Yohna esquive
    console.print("[italic]Yohna glisse sous la projection magique, évitant de justesse les ondes destructrices. "
              "Elle roule sur le côté, mais à peine redressée, une rivière de flammes jaillit du sol, "
              "lancées par Durnir d’un geste fluide. Des braises tourbillonnent dangereusement autour d’elle.[/italic]")

    console.print("Durnir (calme) : 'Ne baisse jamais ta garde. La magie, c’est comme une danse. "
              "Une seconde de distraction suffit pour t’embraser.'")

    console.print("[italic]Les flammes courent vers Yohna, l’entourant lentement. "
              "Son regard devient plus sérieux, et elle commence à invoquer un nouvel esprit d'eau pour contrer l’assaut.[/italic]")

# Réactions des spectateurs
    console.print("Garen (inquiet) : 'Elle va s’en sortir, non… ?'")

    console.print("Zyn (confident) : 'Ne t’en fais pas. Ma sœur a plus d’un tour dans son sac.'")

    console.print("Emphyr (regardant Durnir) : 'Peut-être… Mais ce vieil homme est un archimage. "
              "S’il le voulait, il pourrait la réduire en cendres. Il s'amuse, crois moi il a deja gagné...(dit elle en s'eloignant...)'")

    console.print("[italic]Le duel continue, mais la tension dans la salle est palpable. "
              "Yohna semble repoussée dans ses retranchements, tandis que Durnir reste stoïque, "
              "prêt à enchaîner ses sorts comme s’il s’agissait d’un simple exercice.[/italic]")
    console.print("[italic]Durnir, un sourire joueur aux lèvres, tend la main vers l'avant. "
              "Dans un claquement de doigts, une rafale de flammes s'élève devant lui, tourbillonnant "
              "en un serpent incandescent. Durnir, comme porté par un vent invisible, glisse sur cette "
              "vague de feu, s’approchant dangereusement de Yohna.[/italic]")

    console.print("Durnir (souriant) : 'Toi, ton frère et moi… Nous sommes différents des autres. "
              "La boîte ne nous a rien donné parce que la nature elle-même s'en était déjà chargée. "
              "Je respecte votre clan, Yohna. Ce que vous représentez.'")

    console.print("Yohna (crispée, plissant les yeux) : 'N'essaie même pas de m’amadouer, vieux croûton.'")

    console.print("[italic]D’un geste vif, Yohna lève les bras et frappe le sol avec sa main. "
              "L’air se charge de magie et une silhouette massive prend forme derrière elle. "
              "Un immense esprit en forme de baleine, éthérée et scintillante, s’élève majestueusement. "
              "Elle ouvre grand sa gueule, projetant un torrent d’eau en direction de Durnir, éteignant "
              "instantanément sa flamme.[/italic]")

    console.print("[bold cyan]Zyn[/bold cyan] (poing levé) : 'Ouais, Yohna ! Éteins-le pour de bon !'")

    console.print("[italic]Durnir trébuche légèrement, glissant sur le sol trempé. "
              "Il s’arrête en riant doucement, secouant la tête.[/italic]")

    console.print("Durnir (amusé) : 'Malin… ahah ! Pas mal, jeune fille. Pas mal du tout.'")

    console.print("[italic]Mais son sourire s’efface lentement, laissant place à une expression plus sérieuse.[/italic]")

    console.print("Durnir (baissant légèrement la tête) : '…Mais c'est déjà trop tard.'")

    console.print("Yohna (fronçant les sourcils) : 'Quoi… ?'")

# Durnir retourne la situation
    console.print("[italic]Soudain, l’eau invoquée par Yohna semble frémir. "
              "Sous les yeux écarquillés de l’invocatrice, la silhouette de la baleine disparaît progressivement, "
              "alors que l’eau s’élève lentement, prenant la forme d’une bulle géante. "
              "Durnir, les deux mains ouvertes, manipule aisément ce globe liquide, le faisant léviter au-dessus de Yohna.[/italic]")

    console.print("Durnir (calme, concentré) : 'C’est une belle invocation… mais l’eau, c’est aussi mon domaine.'")

    console.print("[italic]D’un mouvement sec, il projette la bulle vers le sol. "
              "Yohna se retrouve piégée à l’intérieur, incapable de briser cette prison aqueuse. "
              "Le globe s'élève puis s’écrase lourdement contre la pierre, laissant Yohna inconsciente au centre de l’arène.[/italic]")

    console.print("[bold cyan]Zyn[/bold cyan] (hurlant) : 'YOHNA !!!'")

    console.print("Emphyr (croisant les bras, regard méprisant) : 'Pathétique… Je l’avais bien dit. "
              "Les invocateurs sont d’une stupidité sans nom.'")

    console.print("[italic]Zyn serre les poings, mais Durnir lève calmement la main pour désamorcer la tension.[/italic]")

    console.print("Durnir (clin d’œil malicieux) : 'Du calme, gamin. Elle va juste roupiller un peu. "
              "T’en fais pas pour elle.'")

    console.print("[italic]Durnir fait quelques pas vers Yohna, traçant un petit symbole dans l’air. "
              "La bulle éclate doucement en laissant l’invocatrice roulée sur le sol, inconsciente mais indemne.[/italic]")

    console.print("[bold red]Archeon[/bold red] (d’une voix forte) : 'Durnir remporte ce duel.'")

    console.print("[italic]Le silence retombe brièvement dans la salle. Zyn rejoint sa sœur, la relevant doucement, "
              "tandis que Durnir retourne vers le côté de l’arène, bras croisés, observant les torches "
              "avec un regard pensif.[/italic]")

    console.print("Kael (calmement) : 'Il s’est retenu… Mais il aurait pu la tuer à tout moment.'")

    console.print("Garen (soulagé mais tendu) : 'Je préfère qu’il se soit retenu… Ce vieil homme me fait peur.'")
    
    console.print("Gallius : 'Hmm.. Fortiche le vieux, je lui aurait deja trancher la gorge (dit-il en mimant le geste)'")
    
    # Garen s'interroge sur son futur adversaire
    console.print("[italic]Garen détourne le regard vers Aldric, l'air inquiet et incertain.[/italic]")

    console.print("Garen (nerveux) : 'Aldric… Tu crois que je vais devoir affronter qui ?'")

    choix_adversaire_garen = Dialogue(
    "Que répondez-vous à Garen ?",
    [
        {
            "text": "Zyn",
            "consequence": lambda h: [
                console.print("Aldric (calmement) : 'Si c'est Zyn, tu vas devoir rester sur tes gardes. "
                              "Il invoque des créatures rapides et puissantes. Mais il est impulsif, tu pourrais en tirer avantage.'"),
                console.print("Garen (baissant les yeux) : 'Ouais… Impulsif ou pas, il a plus d’expérience que moi.'(Zyn +5)"),
                h.get_relation("Zyn").adjust_score(+5)
            ]
        },
        {
            "text": "Gallius",
            "consequence": lambda h: [
                console.print("Aldric (léger sourire) : 'Si c’est Gallius… Ne laisse pas sa nonchalance te tromper. "
                              "C'est un assassin. Il frappe vite et sans prévenir.'"),
                console.print("Gallius (amusé, à voix basse en jouant avec sa dague avec un sourire) : 'Je te briserai comme du verre, mon pote..'"),
                console.print("Garen (pâle) : 'Euh… Je préférerais éviter Gallius.'(Gallius +5)"),
                h.get_relation("Gallius").adjust_score(+5)
            ]
        },
        {
            "text": "Emphyr",
            "consequence": lambda h: [
                console.print("Aldric (réfléchissant) : 'Emphyr est rapide, méthodique. Elle ne te laissera pas respirer.'"),
                console.print("Emphyr (croisant les bras, avec un sourire en coin) : 'Oh, ne t’en fais pas. "
                              "Je ferai en sorte que ça soit rapide…'"),
                console.print("Garen (grimace) : 'Super… Vraiment rassurant.'(Emphyr + 5)"),
                h.get_relation("Emphyr").adjust_score(+5)
            ]
        },
        {
            "text": "Kael",
            "consequence": lambda h: [
                console.print("Aldric (léger rire) : 'Si tu tombes contre Kael… prépare-toi à souffrir. Il ne plaisante pas en duel.'"),
                console.print("Kael (arrogant) : 'Je t’apprendrai quelques leçons, Garen. Ne t’inquiète pas.'"),
                console.print("Garen (déglutit) : 'C’est bien ce qui me fait peur.'(Kael +5)"),
                h.get_relation("Kael").adjust_score(+5)
            ]
        },
        {
            "text": "Moi-même",
            "consequence": lambda h: [
                console.print("Aldric (souriant) : 'Si c’est moi… Je te ménagerai peut-être. Ou pas.'"),
                console.print("Garen (riant nerveusement) : 'Tu plaisantes j’espère ?'"),
                console.print("Aldric (clin d’œil) : 'Va savoir…'(Garen +5)"),
                h.get_relation("Garen").adjust_score(+5)
            ]
        }
    ]
    )

    choix_adversaire_garen.display(hero)

    console.print("[italic]Garen se frotte nerveusement les mains, observant l’arène encore marquée par le duel précédent.[/italic]")
    console.print("Garen (murmurant) : 'J'espère juste que je vais survivre à ce foutu tournoi…'")
    
    console.print("[italic]L’atmosphère est pesante alors que le vase de cristal brille sous la lueur des torches. "
              "Chaque dueliste restant observe le récipient, guettant le tirage, incertain de leur prochain adversaire.[/italic]")

    console.print("Garen (murmurant à lui-même) : 'C’est bien ma veine… Peu importe contre qui je tombe, je suis fichu…'")

    console.print(
    "[italic]Tous les regards se posent sur Garen, qui se tient légèrement en retrait, "
    "serrant nerveusement la lanière de son épée. Il n’a pas encore utilisé son Margith’r, "
    "et cela le hante. Il sait que d’autres, comme Kael ou Emphyr, cachent aussi des capacités inconnues.[/italic]")

    console.print("[italic]Mais aucun d’eux n’égale Gallius, dont la simple présence semble peser sur la salle. "
              "Ce tueur professionnel reste appuyé nonchalamment contre un pilier, l’air détaché, "
              "mais son ombre s’étire, menaçante.[/italic]")

    console.print("[bold red]Archeon[/bold red] (voix forte) : 'Le prochain combat va commencer.'")

    console.print("[italic]Archeon plonge une main ouverte au-dessus du vase, et par magie, une sphère s’élève lentement. "
              "Elle brille d’une douce lueur, révélant un nom que tous attendaient avec appréhension.[/italic]")

    console.print("[bold yellow]Archeon[/bold yellow] : 'Garen.'")

    console.print("[italic]Le cœur de Garen manque un battement. Ses jambes faiblissent un instant tandis qu’il avance vers l’arène, "
              "comme si son destin venait d’être scellé.[/italic]")

    console.print("Garen (frissonnant) : 'Non… Pourquoi moi ?'")

    console.print("[italic]Ses yeux parcourent la pièce. Il y a encore un espoir. Peut-être tombera-t-il contre quelqu’un… de plus clément ?"
              "Mais ce n’est qu’un maigre mensonge qu’il se raconte pour apaiser sa peur.[/italic]")

    console.print("[bold red]Archeon[/bold red] (reprenant avec amusement) : 'Face à… Kael.'")

    console.print(
    "[italic]Un silence s’installe. Kael s’avance sans précipitation, l’ombre d’un sourire aux lèvres. "
    "Il se place devant Garen, observant son vieil adversaire de haut.[/italic]")

    console.print("Kael (doucement) : 'Eh bien… le destin nous a réunis, paysan.'")
    console.print("Garen (nerveux): 'Hm...c'etait ecrit...'")

    console.print("[italic]Les deux se toisent un instant. C’est plus qu’un duel de tournoi. "
              "C’est une rivalité qui remonte à l’extérieur de cette tour, a tout début – "
              "la noblesse contre le peuple, l'éxcellence contre l’endurance.[/italic]")

    console.print("Garen (tentant de masquer sa nervosité) : 'Tu vas voir… je suis plus coriace que tu le penses.'")
    console.print("Kael : 'Ne t'en fait Garen je ne ferai pas l'erreur de te sous estimé, même si ma victoire est deja assuré..'")

    console.print("[italic]Mais malgré ses paroles, ses mains tremblent. Kael le remarque, mais ne dit rien. "
              "Il se contente de dégainer lentement sa rapière, l’acier reflétant la lumière des torches.[/italic]")

    console.print("[bold red]Archeon[/bold red] (levant la main) : 'Que le combat commence !'")
    
    console.print("[italic]Le duel va bientôt commencer. Zyn s’approche d’Aldric, les bras croisés, fixant les deux combattants qui prennent position.[/italic]")

    console.print("Zyn (curieux) : 'Alors, Aldric ? Qui tu vois gagner ce combat ? Le bourge ou le bouseux ?'")

# Choix de dialogue
    choix_duel_garen_kael = Dialogue(
    "Que répondez-vous à Zyn ?",
    [
        {
            "text": "Kael est clairement le favori. Garen a peu de chances.",
            "consequence": lambda h: [
                console.print("Aldric (calme) : 'Kael est redoutable, c’est évident. Garen… a du courage, mais ça ne suffira peut-être pas.'"),
                console.print("Zyn (hochant la tête) : 'Je suis d’accord. Kael est méthodique. Garen va devoir se surpasser.' (Zyn +10, Kael +10, Garen -10)"),
                h.get_relation("Zyn").adjust_score(+10),
                h.get_relation("Kael").adjust_score(+10),
                h.get_relation("Garen").adjust_score(-10)
            ]
        },
        {
            "text": "Je crois en Garen. Il a plus de ressources qu’on ne le pense.",
            "consequence": lambda h: [
                console.print("Aldric (convaincu) : 'Garen a un cœur solide. Je pense qu’il peut surprendre Kael.'"),
                console.print("Zyn (sceptique) : 'Hm… On verra. Mais s’il gagne, ça sera de justesse.' (Garen +10, Kael -10)"),
                h.get_relation("Garen").adjust_score(+10),
                h.get_relation("Kael").adjust_score(-10)
            ]
        }
    ]
    )

    choix_duel_garen_kael.display(hero)

    console.print("\n[bold red]Archeon[/bold red] (d’un ton grave) : 'En place.'")

    console.print("[italic]Kael ajuste sa rapière, effectuant quelques mouvements fluides. La lame brille légèrement d’une aura bleutée, signe du Margith’r qui pulse en lui.[/italic]")

    console.print("Kael (à Garen) : 'Je vais rendre ça rapide. Tu devrais abandonner.'")

    console.print("Garen (serrant les poings) : 'On verra ça… Je ne suis pas venu ici pour fuir.'")

    console.print("[italic]Archeon lève lentement le bras, puis l’abaisse brusquement.[/italic]")

    console.print("[bold red]Archeon[/bold red] : 'Que le combat commence !'")

# Début du duel
    console.print("[italic]Kael bondit immédiatement en arrière, balançant sa rapière dans le vide. "
              "Des pointes invisibles de force jaillissent devant lui, projetant des impacts rapides en direction de Garen.[/italic]")

    console.print("Kael (criant) : 'Distance, toujours la distance !'")

    console.print("[italic]Garen lève ses bras en croix, mais les projectiles le frappent sans relâche. "
              "Il glisse en arrière, peinant à trouver une ouverture.[/italic]")

    console.print("Garen (frustré) : 'Je ne peux même pas m’approcher !'")

    console.print("[italic]Mais alors que Kael continue son mitraillage, Garen serre les dents. "
              "Un bouclier de bois apparaît soudain devant lui, absorbant partiellement les coups.[/italic]")

    console.print("Kael (haussant un sourcil) : 'Oh ? Tu caches quelque chose, après tout…'")

    console.print("Garen (grimaçant) : 'Je ne comprends pas encore ce pouvoir… mais ça fera l’affaire !'")

    console.print("[italic]Kael éclate de rire et projette un nouvel assaut. "
              "Le bouclier de Garen se fend sous l’impact, mais il tient bon.[/italic]")

    console.print("[bold cyan]Zyn[/bold cyan] (croisant les bras) : 'Pas trop mal pour un début… Mais ça ne suffira pas face à Kael.'")

    console.print("[bold cyan]Gallius[/bold cyan] (calmement) : 'Il doit encaisser et frapper au bon moment… S’il peut s’approcher, Kael n’aura aucune chance.'")

    console.print("[italic]Durnir observe silencieusement, un léger sourire en coin, intrigué par la ténacité de Garen.[/italic]")
    
    console.print("[italic]Kael fait glisser sa rapière dans l’air, déclenchant une nouvelle série de pointes invisibles. "
              "Garen invoque un rempart de bois fragile, mais chaque impact fait trembler la structure jusqu’à ce qu’elle s’effrite et cède entièrement.[/italic]")

    console.print("Kael (sèchement) : 'C’est déjà fini ? Je vais pas te ménager sous prétexte qu’on a fait un bout de chemin ensemble. "
              "Tu restes le plus faible ici, Garen. Le meilleur tirage pour moi.'")

    console.print("[italic]Garen baisse légèrement son bouclier, la tête baissée. Ses poings tremblent.[/italic]")

    console.print("Garen (murmurant) : '…hm…'")

    console.print("[italic]Kael ne lui laisse aucun répit et bondit en arrière pour augmenter la distance, déclenchant une nouvelle salve de projectiles tranchants. "
              "Garen, paniqué, matérialise un autre rempart, mais il est encore plus fragile que le précédent. "
              "Les coups fusent et brisent le bouclier en éclats, comme si la confiance de Garen se décomposait peu à peu.[/italic]")

# Choix de dialogue - Influence d'Aldric
    choix_duel_kael_garen = Dialogue(
    "Aldric comprend quelque chose… Que lui dites-vous ?",
    [
        {
            "text": "Kael, finis-en. Il n’a même pas envie de se battre.",
            "consequence": lambda h: [
                console.print("Aldric (croisant les bras) : 'Termine-le, Kael. Il n’a pas l’envie de se battre.'"),
                console.print("Kael (souriant froidement) : 'Je vois ça. Tu as raison, Aldric.' (Garen -20)"),
                console.print("[italic]Garen baisse encore plus les yeux, les mots d’Aldric résonnant lourdement dans son esprit.[/italic]"),
                console.print("Kael (à Garen) : 'Tu aurais dû rester à traire les vaches. Ton frère aurait eu plus de chance ici que toi.'"),
                h.get_relation("Garen").adjust_score(-20)
            ]
        },
        {
            "text": "Garen, tu dois te rapprocher ! Tu n’as pas le choix. Ses coups deviennent plus puissants à distance !",
            "consequence": lambda h: [
                console.print("Aldric (avec intensité) : 'Garen ! La distance le rend plus fort. Tu dois te rapprocher, maintenant !'"),
                console.print("Kael (jetant un regard vers Aldric) : 'Bien vu, Aldric. Observateur, mais…'"),
                console.print("Kael (plissant les yeux) : 'C’est trop tard pour lui.' (Kael +10)"),
                console.print("[italic]Kael s’avance, rapière prête à fondre sur Garen pour finir le combat.[/italic]"),
                h.get_relation("Kael").adjust_score(+10)
            ]
        }
    ]
    )

    choix_duel_kael_garen.display(hero)

# Transition - Réveil de Garen
    console.print("[italic]Kael s’apprête à lancer une nouvelle rafale. Son regard est impassible tandis qu’il fait un pas en avant, la pointe de sa rapière scintillant sous la lueur des torches.[/italic]")

    console.print("Kael : 'Tu aurais dû laisser ta place à ton frère…tu ne sera jamais comme lui...(Garen lui avait raconté son, histoire)'")

    console.print("[italic]Ces mots déclenchent quelque chose en Garen. Il serre les poings jusqu’à ce que ses articulations blanchissent, puis il hurle.[/italic]")

    console.print("[bold yellow]Garen (hurlant) : 'Ne parle jamais de mon frère ! Jamais !'[/bold yellow]")

    console.print("[italic]Un éclat doré jaillit de ses mains, et un immense écu de chêne massif apparaît, arrêtant net la prochaine salve de Kael. "
              "Les projectiles se dispersent comme s’ils rebondissaient sur une muraille impénétrable.[/italic]")

    console.print("Kael (étonné) : 'Oh ? Je crois que j’ai touché une corde sensible.'")

    console.print("[italic]Garen avance, lentement mais sûrement. À chaque pas, il repousse les assauts répétés de Kael, les projectiles perdant en force. "
              "Kael recule instinctivement, mais l’avancée de Garen est inexorable.[/italic]")

    console.print("Garen (voix grave) : 'Tu n’as pas le droit de parler de lui. Pas toi.'")

    console.print("Kael (avec un sourire nerveux) : 'Hah… Ça devient intéressant.'")

    console.print("[italic]La dynamique du combat s’inverse progressivement. Garen, protégé par son bouclier, gagne du terrain tandis que Kael, d’habitude implacable, semble chercher une nouvelle stratégie.[/italic]")

    console.print("[italic]Garen, le souffle court, maintient son bouclier de chêne fermement, repoussant les assauts répétés de Kael. "
              "Mais quelque chose change. Le bois du bouclier semble vibrer, scintillant légèrement sous la lumière des torches. "
              "Une lueur dorée l’enveloppe, se teignant lentement d’orange à chaque coup absorbé.[/italic]")

    console.print("[bold yellow]Durnir[/bold yellow] (le regard perçant) : 'Gamin… Ton Margith'r est sûrement l’un des plus beaux que j’ai vus. "
              "Plus ton cœur est fort et vaillant, plus ton rempart deviendra indestructible.'")

    console.print("[italic]Il plisse les yeux, une larme presque imperceptible au coin de l’œil. "
              "L’émotion qu’il ressent est sincère, comme s’il assistait à la naissance d’un prodige. "
              "Mais son attention se détourne rapidement vers l’aura qui s’intensifie autour de Garen.[/italic]")

    console.print("Emphyr (croisant les bras, intriguée) : 'Hmmm… Intéressant.'")
    console.print("Gallius (grinçant des dents avec un sourire) : 'Ooooh ? Le bouseux rigole plus ! "
              "Allez, défends-toi, écrase ce coincé de noble ! Hahaha !'")

    console.print("Aldric (murmurant, observant attentivement) : '…Garen…'")
    console.print("Zyn (fixant la lueur autour de Garen) : 'Aldric… cette lumière… C’est quoi, ça ?'")

# Choix de dialogue - Révélation du pouvoir de Garen
    choix_margithr_garen = Dialogue(
    "Que répondez-vous à Zyn ?",
    [
        {
            "text": "J’ai l’impression que ça absorbe les coups. Étrange…",
            "consequence": lambda h: [
                console.print("Aldric (calme) : 'On dirait que chaque coup que Garen reçoit renforce ce bouclier… comme s’il stockait cette force.'"),
                console.print("Durnir (souriant doucement) : 'C’est exact. Le Margith'r de ce gamin repose sur un principe simple : "
                              "plus il endure, plus il pourrait riposter fort. Fascinant…ce pouvoir est a son image"
                              "'Il a dit encaissé beaucoup de choses dans sa vie...'"),
            ]
        },
        {
            "text": "C’est une manifestation de sa volonté.",
            "consequence": lambda h: [
                console.print("Aldric (les yeux rivés sur Garen) : 'Ce n’est pas qu’une capacité. "
                              "Son pouvoir est une extension de sa volonté. Plus il croit en sa victoire, plus il devient fort.'"),
                console.print("Durnir (riant doucement, levant un doigt) : 'Pas seulement… C’est encore plus intéressant que ça, jeune homme.'"),
            ]
        }
    ]
    )

    choix_margithr_garen.display(hero)

# Kael intensifie son offensive
    console.print("[italic]Kael, remarquant le changement dans l’attitude de Garen, plisse les yeux. "
              "Sa rapière fend l’air avec encore plus de vitesse, déclenchant des rafales de coups à distance. "
              "Mais Garen ne faiblit pas. Il avance lentement, bloquant chaque salve avec son bouclier renforcé.[/italic]")

    console.print("Kael (agacé, haussant la voix) : 'Ce n’est pas suffisant. Je vais te briser.'")

    console.print("[italic]D’un bond rapide, Kael s’élève dans les airs, abattant sa rapière en direction du sol. "
              "Un arc d’énergie jaillit, créant une onde de choc sous Garen, cherchant à le déséquilibrer. "
              "Mais Garen, impassible, frappe le sol de son bouclier avec force.[/italic]")

    console.print("[bold cyan]Garen[/bold cyan] (hurlant) : 'Tu ne me feras pas tomber !'")

    console.print("[italic]L’impact de son coup crée une onde inverse, propulsant Garen dans les airs pour rejoindre Kael. "
              "Les deux combattants échangent alors des coups dans une pluie d’étincelles, "
              "Garen repoussant chaque attaque avec une précision nouvelle. "
              "L’aura autour de son bouclier passe du doré à l’orange, puis au rouge vif, bouillonnant d’énergie.[/italic]")

    console.print("Kael (tentant de masquer sa surprise) : 'Hmph… Je vois. Tu es plus coriace que prévu. Mais ça ne suffira pas.'")

    console.print("Garen (d’une voix ferme, les yeux brillants de détermination) : 'Ne me prend plus jamais de haut Kael. Jamais !!'")
    
    console.print("Aldric (se rememore sa recontre avec Garen au pied de la tour...): Garen....ahahah...Tu as changé ! bravo mon pote !")

    console.print("[italic]Kael enchaîne rapidement, mais ses coups, bien que rapides, semblent moins efficaces. "
              "Chaque impact contre le bouclier de Garen est absorbé, et la tension grimpe. "
              "Kael recule instinctivement, tandis que Garen continue d’avancer, implacable.[/italic]")

    console.print("Durnir (dans un souffle, observant) : 'Quel pouvoir fascinant… Ce gamin pourrait aller loin.'")
    
    console.print("[italic]Garen baisse légèrement son bouclier, laissant apparaître son regard déterminé sous la lueur rougeâtre de son Margith'r.[/italic]")  
    console.print("Kael (criant, avec frénésie) : 'N'essaie même pas ! YAYAYAYAYAYAYA !'")  

    console.print("[italic]Kael enchaîne des coups rapides, projetant des rafales de lames de vent. Garen ne recule pas. "
              "Son bouclier absorbe les attaques, faisant trembler l’arène sous leurs échanges intenses.[/italic]")  
    console.print("Garen (hurlant avec rage) : 'Ça suffit ! Crève !!!'")  

    console.print("[italic]Dans une explosion de force, Garen bondit en avant. "
              "Il abat son bouclier avec une puissance colossale contre Kael, qui ne peut qu’écarquiller les yeux.[/italic]")  
    console.print("Kael (surpris) : 'Meeeeerde… !'")  

    console.print("[italic]Kael est projeté violemment vers le sol, son corps rebondissant lourdement sur les dalles de pierre.[/italic]")  
    console.print("Garen (retombant, haletant) : 'Kael… ? Je…Je...suis désolé…'")  

    console.print("[italic]Mais alors que Garen s’approche, son bouclier perd peu à peu son éclat, s’adoucissant comme si sa volonté s’était calmée. "
              "Il s’inquiète pour Kael… oubliant l’enjeu du combat.[/italic]")  
    console.print("Kael (grimaçant, se redressant légèrement et bléssé) : '[bold]Erreur fatale.[/bold] Regle numéro 1… ne jamais baisser sa garde.'")  

    console.print("[italic]Dans un éclair, Kael frappe d’un coup vif avec sa rapière. La lame fend l’air et brise le bouclier affaibli de Garen, "
              "le projetant à terre. Kael chancelle mais parvient à se redresser, la lame pointée vers son ami, encore sonné.[/italic]")  

    console.print("[bold red]Archeon[/bold red] (d’une voix forte et impassible) : 'Kael est vainqueur.'")  

    console.print("[italic]Kael reste silencieux, son regard fixé sur Garen, réalisant à peine la fin du duel. "
              "Il semble presque aussi choqué que son adversaire.[/italic]")  

    console.print("Garen (à voix basse, tremblant) : 'J’ai… j’ai perdu…'")  
    console.print("[italic]Il se retourne lentement, s’effondrant sur le sol face contre terre. Des sanglots éclatent, brisant le silence pesant de l’arène.[/italic]")  
    console.print("Garen (murmurant, brisé) : 'Snif...Kael…! tue-moi…! Je suis une honte. Je… Je ne mérite pas de vivre. Mon frère aurait dû être là, "
                  "pas moi… Je suis incapable de protéger quoi que ce soit, ni même ma satané ferme...'")  

    console.print("[italic]Kael baisse la tête pour masquer l’émotion qui traverse son visage. "
              "Sa main tremble légèrement autour de la garde de sa rapière.[/italic]")  
    console.print("Kael (d’une voix calme et douce) : 'Arrête… Tu es bien plus fort que tu ne le crois. Ce combat n’a rien changé à ça.'")  

    console.print("[italic]Kael tend la main à Garen pour l’aider à se relever, mais ce dernier reste prostré, incapable de lever les yeux.[/italic]")  
    console.print("Kael (soupirant, en murmurant) : 'Ton frère aurait été fier de toi. Je l’aurais été aussi…'")  

    console.print("[italic]Archeon observe la scène sans un mot, les mains jointes dans son dos. "
              "Son regard perçant s’attarde un instant sur Garen, avant de détourner les yeux vers la suite du tournoi.[/italic]")  
    console.print("Archeon (calme) : 'Relevez-le. Les épreuves ne sont pas terminées.'")  
    
    console.print("[italic]Le silence qui suit le duel est lourd, presque oppressant. Garen reste à terre, le front appuyé sur la pierre froide, tandis que Kael s’éloigne lentement, le regard bas. "
              "Archeon observe sans dire un mot, laissant cette tension imprégner l’arène.[/italic]")  

    console.print("Durnir (hochant la tête, bras croisés) : 'Hm… Je suis déçu de cette fin. Mais pas surpris.'")  
    console.print("Durnir (souriant en coin) : 'Garen… Tu es un bon gars. Et surtout, t’es encore vivant.'")  

    console.print("Emphyr (froide, adossée contre un pilier) : 'Les faibles finissent toujours par tomber. C’était couru d’avance.'")  

    console.print("[italic]Kael regagne lentement son siège du côté des vainqueurs, sans adresser un regard à personne. "
              "Clotaire, assis dans l’ombre, lève brièvement la tête et affiche un léger signe de respect en direction des deux combattants.[/italic]")  

    console.print("Clotaire (calme) : 'Ils se sont bien battus. Même un combat déséquilibré mérite d’être salué.'")  

    console.print("[italic]Gallius ricane en s'étirant, passant une main dans ses cheveux.[/italic]")  
    console.print("Gallius (moqueur) : 'Dommage… Le fermier aurait dû l’achever. Ça aurait fait du spectacle. "
              "Quant à toi, noble… ta victoire est loin d’être méritée. Sache-le.'")  

# Yohna se réveille
    console.print("[italic]De l’autre côté de l’arène, Yohna, qui avait été laissée sous la surveillance de Zyn après son duel contre Durnir, ouvre lentement les yeux.[/italic]")  
    console.print("Yohna (faiblement) : 'Zyn… Je…'")  

    console.print("[italic]Zyn se précipite à ses côtés, le visage tendu mais soulagé de la voir consciente.[/italic]")  
    console.print("Zyn (soufflant, inquiet) : 'Repose-toi. T’es encore là, c’est l’essentiel.'")  

# Garen s’isole
    console.print("[italic]Pendant ce temps, Garen s’assoit à l’écart, dans l’ombre d’une colonne. "
              "Il s’enfonce dans ses pensées, honteux et abattu. Il évite le regard des autres participants.[/italic]")  

    console.print("[bold]Durnir[/bold] (lui lançant un regard chaleureux) : 'Bravo, gamin. Sois fier de toi. De tous ici, "
              "tu es celui qui a le plus grand cœur.'")  
    console.print("[italic]Durnir frappe sa poitrine d’un poing ferme, signe de respect sincère, avant d’ajouter dans un sourire franc.[/italic]")  
    console.print("Durnir : 'Et crois-moi… ça vaut plus qu’une victoire.'")  

    console.print("Aldric (calme mais sincère) : 'Il a raison. Je suis fier de t’avoir rencontré… et encore plus d’être ton ami.'")  

    console.print("[italic]Garen lève à peine les yeux, mais un léger tremblement trahit l’émotion qui l’envahit.[/italic]")  
    console.print("Garen (murmurant) : 'Merci… Aldric…Durnir..'")  

# Kael affiche de l’émotion
    console.print("[italic]Kael, toujours assis du côté des vainqueurs, serre les poings un instant, avant de relâcher la pression. "
              "Il détourne le regard, peinant à cacher la légère culpabilité qui le traverse.[/italic]")  
    console.print("Kael (à voix basse) : 'Garen…'")  

    console.print("[italic]Mais Kael se tait, sachant que ses mots n’apporteraient rien de plus pour le moment et se contente de soigner ses blessures.[/italic]")  


    







    
    









