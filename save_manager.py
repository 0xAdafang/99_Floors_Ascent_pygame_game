import json
import os
import pygame
from classes import *
from classes import Heros, Relation, Character


SAVE_DIR = "saves"


def ensure_save_dir():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)


# save_manager.py
import json
import os
import pygame

SAVE_DIR = "saves"

def save_game(hero):
    from classes import Heros  # Import retardé
    ensure_save_dir()
    save_name = "sauvegarde"
    save_path = os.path.join(SAVE_DIR, f"{save_name}.json")

    save_data = {
        "name": hero.name,
        "health": hero.health,
        "chapter_reached": hero.chapter_reached,
        "relations": [
            {"name": r.character.name, "score": r.score, "type": r.relationship_type}
            for r in hero.relations
        ]
    }

    with open(save_path, "w") as file:
        json.dump(save_data, file, indent=4)
    
    print(f"Sauvegarde réussie : {save_name}")
    return f"Sauvegarde réussie : {save_name}"



def display_save_confirmation(screen, font, message, duration=2000):
    # Affiche un message de confirmation temporaire à l'écran
    box_width, box_height = 800, 150
    box_surface = pygame.Surface((box_width, box_height))
    box_surface.fill((30, 30, 30))
    pygame.draw.rect(box_surface, (255, 255, 255), (0, 0, box_width, box_height), 3)

    text_surface = font.render(message, True, (255, 255, 0))
    box_surface.blit(text_surface, (box_width // 2 - text_surface.get_width() // 2, box_height // 2 - 20))

    width, height = screen.get_size()
    screen.blit(box_surface, (width // 2 - box_width // 2, height // 2 - box_height // 2))
    pygame.display.flip()
    pygame.time.wait(duration)


def list_saves():
    ensure_save_dir()
    saves = [f for f in os.listdir(SAVE_DIR) if f.endswith(".json")]
    return saves


def load_game():
    try:
        with open("sauvegarde_automatique.json", "r") as file:
            data = json.load(file)

        hero = Heros()
        hero.name = data.get("name", "Aldric")
        hero.health = data.get("health", 100)
        hero.chapter_reached = data.get("chapter_reached", 1)

        relations_data = data.get("relations", [])
        for rel in relations_data:
            # Assurez-vous que "role" est fourni, sinon mettez une valeur par défaut
            role = rel.get("role", "Inconnu")  # "Inconnu" est un rôle par défaut
            char = Character(
                rel["name"],
                rel.get("sprite_path", "graphics/resources/sprites/default.webp"),
                rel.get("description", "Ancienne relation"),
                role,
                rel.get("gender", "inconnu")
            )
            relation = Relation(char, rel.get("relationship_type", "Neutre"), rel.get("score", 0))
            hero.relations.append(relation)

        print("Partie chargée avec succès.")
        return hero
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return None

