class Heros:
    def __init__(self):
        self.name = "Aldric"
        self.description = (
            "Un jeune mercenaire de 16 ans, vivant dans un monde brutal où il n'a pas eu "
            "le choix de prendre les armes pour survivre. Maintenant, il participe au "
            "tournoi de la Tour Divine pour atteindre la pierre de Cygide, dont le pouvoir "
            "est encore inconnu."
        )
        self.health = 100
        self.is_alive = True
        self.inventory = []
        self.relations = []
        self.choices_made = []
        self.floor_reached = 0
        
        
    def adjust_health(self, amount):
        self.health += amount
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            self.trigger_death()
        print(f"[Héros] {self.name} : Points de vie actuels : {self.health} / 100.")

    def trigger_death(self):
        print("\n[bold red]Aldric succombe à ses blessures...[/bold red]")
        print(
            f"Aldric s'est arrêté à l'étage {self.floor_reached} de la Tour Divine. "
            "Dans l'obscurité, les murmures d'âmes perdues résonnent. Son épopée devient une légende, "
            "portée par ceux qui écoutent les vents de la Tour."
        )

    def add_relation(self, character, relationship_type="neutral"):
        existing_relation = self.get_relation(character.name)
        if existing_relation:
            existing_relation.adjust_score(10 if relationship_type == "friend" else -10)
        else:
            if isinstance(character, str):
                character = Character(character, "Description inconnue", "inconnu")
            new_relation = Relation(character, relationship_type)
            self.relations.append(new_relation)
        # Ajustement initial du score
            if relationship_type == "friend":
                new_relation.adjust_score(10)
            elif relationship_type == "enemy":
                new_relation.adjust_score(-10)


    def get_relation(self, character_name):
        for relation in self.relations:
            if relation.character.name == character_name:
                return relation
        return None
    
    def remove_relation(self, character_name):
        for relation in self.relations:
            if relation.character.name == character_name:
                self.relations.remove(relation)
                print(f"[Relation] {character_name} a été retiré de vos relations.")
                return
        print(f"[Relation] {character_name} n'est plus dans vos relation, il/elle est surement partie ou mort...")
    

class Relation:
    def __init__(self, character, relationship_type="Neutre"):
        self.character = character
        self.score = 0
        self.relationship_type = relationship_type

    def adjust_score(self, amount):
        self.score += amount
        self.score = max(-100, min(100, self.score))
        self.update_relationship_type()
    
    def set_relationship_type(self, new_type):
        self.relationship_type = new_type
        print(f"[Relation] La relation avec {self.character.name} est maintenant '{new_type}'.")

    def update_relationship_type(self):
        if self.score <= -20:
            self.relationship_type = "Ennemi"
        elif -10 < self.score <= 19:
            self.relationship_type = "Neutre"
        elif 20 < self.score <= 80:
            self.relationship_type = "Ami"
        elif self.score > 80:
            # Vérification robuste pour éviter les erreurs si 'gender' n'existe pas
            if hasattr(self.character, 'gender') and self.character.gender.lower() == "fille":
                self.relationship_type = "Romance"
            else:
                self.relationship_type = "Frere d'armes"
            
        
        
class Character:
    def __init__(self, name, description, gender, role="neutral", ):
        self.name = name
        self.description = description
        self.gender = gender  # "fille" ou "garçon"
        self.role = role
        
           
        

class Dialogue:
    def __init__(self, text, choices, character=None):
        self.text = text
        self.choices = choices
        self.character = character

    def display(self, hero):
        from rich.console import Console
        console = Console()

        relation = hero.get_relation(self.character.name) if self.character else None

        console.print(f"[bold cyan]{self.text}[/bold cyan]")

    # Filtrer les choix selon la relation
        filtered_choices = []
        for choice in self.choices:
            if "condition" in choice:
                if not choice["condition"](hero):
                    console.print(f"[bold red]Option verrouillée : {choice['text']}[/bold red]")
                    continue
            filtered_choices.append(choice)

    # Affiche uniquement les choix filtrés
        for i, choice in enumerate(filtered_choices):
            console.print(f"{i + 1}. {choice['text']}")

        while True:
            try:
                selected = int(input("\nQuel est votre choix ? : ")) - 1
                if 0 <= selected < len(filtered_choices):
                    consequence = filtered_choices[selected]["consequence"]
                    consequence(hero)
                    if relation:
                        status = relation.relationship_type
                        console.print(f"\n[bold cyan]{relation.character.name} : Relation {relation.score} ({status})[/bold cyan]")
                    break
            except (ValueError, IndexError):
                console.print("[bold red]Choix invalide, réessayez.[/bold red]")

class Event:
    
    def __init__(self, name, description, action):
        
        self.name = name
        self.description = description
        self.action = action 
        
    def trigger(self, hero):
        
        print(f"Événement: {self.name}") 
        print(self.description)
        self.action(hero)
        



class Tower:
    MAX_FLOORS = 99  # Limite explicite pour le nombre d'étages

    def __init__(self):
        self.floors = []  # Chaque étage contient une liste d'événements ou défis
        self.current_floor = 0
       

    def add_floor(self, floor_events):
        """Ajoute une liste d'événements à un étage."""
        if len(self.floors) < self.MAX_FLOORS:
            self.floors.append(floor_events)
        else:
            print(f"Impossible d'ajouter un étage : la tour est limitée à {self.MAX_FLOORS} étages.")

    def advance(self, hero):
        """Passe à l'étage suivant et déclenche les événements."""
        if self.current_floor < len(self.floors):
            self.current_floor += 1  # Problème ici
            hero.floor_reached = self.current_floor
            print(f"\nVous êtes maintenant à l'étage {self.current_floor} de la Tour Divine.")

            # Déclencher les événements de l'étage
            for event in self.floors[self.current_floor - 1]:
                event.trigger(hero)
                if not hero.is_alive:
                    return
        else:
            print(f"\nVous avez atteint le sommet de la Tour. Étage {self.MAX_FLOORS}.")
            print("La pierre de Cygide repose ici, mystérieuse et pleine de promesses...")




class SafeRoom:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def rest(self, hero):
        hero.adjust_health(100)
        print(f"Vous vous reposez dans la {self.name}.")
        print("Un murmure à peine audible flotte dans l'air : 'La lumière éclaire parfois l'ombre.' vos blessures ont disparues...")



class GameMenu:
    def __init__(self, hero, tower=None):
        self.hero = hero
        self.tower = tower  # La tour est désormais directement passée au menu
    
    def display(self):
        from rich.console import Console
        console = Console()
        
        while True:
            console.print("\n[bold cyan]=== Menu ===[/bold cyan]")
            console.print("1. Continuer l'aventure")
            console.print("2. Afficher les relations")
            console.print("3. Voir la santé du héros")
            console.print("4. Sauvegarder la partie")
            console.print("5. Quitter le jeu")

            choix = input("\nQue voulez-vous faire ? : ")
            
            if choix == "1":
                console.print("[bold green]Vous poursuivez votre aventure...[/bold green]")
                break
            elif choix == "2":
                self.show_relations()
            elif choix == "3":
                self.show_health()
            elif choix == "4":
                self.save_game()
            elif choix == "5":
                self.exit_game()
            else:
                console.print("[bold red]Choix invalide, réessayez.[/bold red]") 
    
    def show_relations(self):
        from rich.console import Console
        console = Console()
        
        console.print("\n[bold cyan]Relations actuelles :[/bold cyan]")
        if not self.hero.relations:
            console.print("Aucune relation pour l'instant.")
        else:
            for relation in self.hero.relations:
                console.print(f"{relation.character.name} : {relation.relationship_type} ({relation.score})")
        input("\n[italic]Appuyez sur Entrée pour revenir au menu...[/italic]")
    
    def show_health(self):  
        from rich.console import Console  
        
        console = Console()
        
        console.print(f"\n[bold cyan]{self.hero.name} : Santé actuelle : {self.hero.health} / 100[/bold cyan]")
        input("\n[italic]Appuyez sur Entrée pour revenir au menu...[/italic]")
    
    
    def save_game(self):
        import json
        from rich.console import Console
        save_data = {
            "name": self.hero.name,
            "health": self.hero.health,
            "floor_reached": self.hero.floor_reached,
            "relations": [
                {"name": relation.character.name, "score": relation.score, "type": relation.relationship_type}
                for relation in self.hero.relations
            ]
        }
        with open("savegame.json", "w") as file:
            json.dump(save_data, file)
        console = Console()
        console.print("[bold green]Partie sauvegardée avec succès ![/bold green]")
        input("\n[italic]Appuyez sur Entrée pour revenir au menu...[/italic]")
    
    def exit_game(self):
        from rich.console import Console
        from main import main_menu  # Import du menu principal
    
        console = Console()
        console.print("[bold yellow]Retour au menu principal...[/bold yellow]")
        main_menu()  # Retour au menu principal au lieu de quitter
        

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    
    
    

            
            
