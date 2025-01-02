from classes import *
from story import *
from save_manager import *
from rich.console import Console
import json

console = Console()


def load_game():
    try:
        with open("savegame.json", "r") as file:
            save_data = json.load(file)
            hero = Heros()
            hero.name = save_data["name"]
            hero.health = save_data["health"]
            hero.floor_reached = save_data["floor_reached"]
            
            # Restaurer les relations
            for relation_data in save_data.get("relations", []):
                char = Character(relation_data["name"], "Ancien compagnon", "inconnu")
                hero.add_relation(char, relation_data["type"])
                hero.get_relation(char.name).adjust_score(relation_data["score"])
            
            console.print("[bold green]Partie chargée avec succès ![/bold green]")
            return hero
    except FileNotFoundError:
        console.print("[bold red]Aucune sauvegarde trouvée.[/bold red]")
        return None


def new_game():
    hero = Heros()
    console.print("[bold green]Nouvelle partie commencée.[/bold green]")
    prologue(hero)
    return hero


def main_menu():
    while True:
        console.print("\n[bold cyan]=== Menu Principal ===[/bold cyan]")
        console.print("1. Nouvelle Partie")
        console.print("2. Charger une Partie")
        console.print("3. Quitter")

        choix = input("\nQue voulez-vous faire ? : ")

        if choix == "1":
            hero = new_game()
            return hero
        elif choix == "2":
            hero = load_game()
            if hero:
                return hero
        elif choix == "3":
            console.print("[bold red]Fin du jeu. À bientôt ![/bold red]")
            exit()
        else:
            console.print("[bold red]Choix invalide, réessayez.[/bold red]")


# ===== Lancement du jeu =====
hero = main_menu()
tower = Tower()

# Création des étages de la tour
for i in range(1, tower.MAX_FLOORS + 1):
    floor_events = [
        Event(f"Défi de l'étage {i}", f"Un défi mystérieux vous attend à l'étage {i}.", lambda h: None)
    ]
    tower.add_floor(floor_events)

game_menu = GameMenu(hero, tower)

# Continuer l'aventure à partir de l'étage atteint
if hero.floor_reached > 0:
    console.print(f"\n[bold green]Vous êtes à l'étage {hero.floor_reached}.[/bold green]")
else:
    console.print("\n[bold yellow]Bienvenue dans la Tour Divine. L'aventure commence ![/bold yellow]")

while hero.is_alive and tower.current_floor <= hero.floor_reached:
    game_menu.display()
    tower.advance(hero)

    if tower.current_floor == 1:
        floor1(hero, game_menu)
    elif tower.current_floor == 2:
        floor2(hero, game_menu)
    elif tower.current_floor == 3:
        floor3(hero, game_menu)
    elif tower.current_floor == 4:
        floor4(hero, game_menu)
    elif tower.current_floor == 5:
        floor5(hero, game_menu)
    elif tower.current_floor == 6:
        floor6(hero, game_menu)
    elif tower.current_floor == 7:
        floor7(hero, game_menu)

    # Sauvegarde automatique après chaque étage
    save_game(hero)

console.print("[bold red]Votre aventure s'arrête ici.[/bold red]") if not hero.is_alive() else console.print(
    "[bold green]Vous atteignez le sommet de la Tour Divine.[/bold green]"
)

