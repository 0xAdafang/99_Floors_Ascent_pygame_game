import json
import os
from classes import *
from story import *


SAVE_DIR = "saves"


def ensure_save_dir():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)


def save_game(hero):
    ensure_save_dir()
    save_name = input("Entrez un nom pour la sauvegarde : ")
    save_path = os.path.join(SAVE_DIR, f"{save_name}.json")

    save_data = {
        "name": hero.name,
        "health": hero.health,
        "floor_reached": hero.floor_reached,
        "relations": [
            {"name": r.character.name, "score": r.score, "type": r.relationship_type}
            for r in hero.relations
        ]
    }

    with open(save_path, "w") as file:
        json.dump(save_data, file, indent=4)
    print(f"[bold green]Partie sauvegardée sous '{save_name}' avec succès ![/bold green]")
    input("\n[italic]Appuyez sur Entrée pour revenir au menu...[/italic]")


def list_saves():
    ensure_save_dir()
    saves = [f for f in os.listdir(SAVE_DIR) if f.endswith(".json")]
    return saves


def load_game(hero=None):
    saves = list_saves()

    if not saves:
        print("[bold red]Aucune sauvegarde disponible.[/bold red]")
        return None

    print("\n[bold cyan]Sauvegardes disponibles :[/bold cyan]")
    for i, save in enumerate(saves, 1):
        print(f"{i}. {save.replace('.json', '')}")

    choix = input("\nChoisissez une sauvegarde (entrez le numéro) : ")
    if not choix.isdigit() or int(choix) < 1 or int(choix) > len(saves):
        print("[bold red]Choix invalide.[/bold red]")
        return None

    save_path = os.path.join(SAVE_DIR, saves[int(choix) - 1])

    with open(save_path, "r") as file:
        save_data = json.load(file)
        if hero is None:
            hero = Heros()
        hero.name = save_data["name"]
        hero.health = save_data["health"]
        hero.floor_reached = save_data["floor_reached"]

        hero.relations = []
        for rel in save_data["relations"]:
            char = Character(rel["name"], "Ancienne relation", "inconnu")
            relation = Relation(char, rel["type"])
            relation.score = rel["score"]
            hero.relations.append(relation)

        print(f"[bold cyan]Partie '{saves[int(choix) - 1].replace('.json', '')}' chargée avec succès ![/bold cyan]")
        return hero
    
def load_existing_game(hero):
    return load_game(hero)