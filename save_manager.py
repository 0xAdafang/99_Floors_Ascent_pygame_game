import json
import os
import pygame
from classes import *
from classes import Heros, Relation, Character



SAVE_DIR = "saves"  # Dossier de sauvegarde

def ensure_save_dir():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
        print(f"Dossier de sauvegarde créé : {SAVE_DIR}")


SAVE_DIR = "saves"

def save_game(hero):
    ensure_save_dir()
    save_name = "sauvegarde"
    save_path = os.path.join(SAVE_DIR, f"{save_name}.json")

    save_data = {
        "name": hero.name,
        "health": hero.health,
        "karma": hero.karma,
        "dalgs": hero.dalgs,  # Ajout des Dalgs ici
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


def list_saves():
    ensure_save_dir()
    saves = [f for f in os.listdir(SAVE_DIR) if f.endswith(".json")]
    return saves


def load_game():
    try:
        ensure_save_dir()
        save_path = os.path.join(SAVE_DIR, "sauvegarde.json")

        if not os.path.exists(save_path):
            print("Aucune sauvegarde trouvée. Création d'une nouvelle partie.")
            return None

        with open(save_path, "r") as file:
            data = json.load(file)

        # Création du héros à partir des données de sauvegarde
        hero = Heros()
        hero.name = data.get("name", "Aldric")
        hero.health = data.get("health", 100)
        hero.karma = data.get("karma", 0)
        hero.dalgs = data.get("dalgs", 0)  # Lecture des Dalgs
        hero.chapter_reached = data.get("chapter_reached", 1)

        # Chargement des relations à partir de la sauvegarde
        relations_data = data.get("relations", [])
        for rel in relations_data:
            sprite_path = rel.get("sprite_path", "graphics/resources/sprites/default.webp")
            if not os.path.exists(sprite_path):
                print(f"Sprite manquant pour {rel['name']}. Utilisation d'un sprite par défaut.")
                sprite_path = "graphics/resources/sprites/placeholder.jpg"

            # Créer le personnage
            char = Character(
                rel["name"],
                sprite_path,
                rel.get("description", "Ancienne relation"),
                rel.get("role", "Inconnu"),
                rel.get("gender", "inconnu")
            )
            
            # Ajouter la relation en prenant en compte le score
            relation = Relation(char, rel.get("type", "Neutre"), rel["score"])
            relation.score = rel["score"]  # Fixe correctement le score
            hero.relations.append(relation)

        print(f"Partie chargée avec succès depuis {save_path}. Chapitre : {hero.chapter_reached}")
        return hero

    except Exception as e:
        print(f"Erreur lors du chargement de la sauvegarde : {e}")
        return None