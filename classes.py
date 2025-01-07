import pygame
import sys


import pygame


class Entity:
    def __init__(self, name, sprite_path, pos):
        self.name = name
        self.sprite = pygame.image.load(sprite_path)
        self.rect = self.sprite.get_rect(topleft=pos)
    
    def draw(self, screen):
        screen.blit(self.sprite, self.rect)

    def update(self):
        pass



class Heros(Entity):
    
    def __init__(self):
        super().__init__("Aldric", "graphics/resources/sprites/Aldric1.webp", (350, 450))
        self.health = 100
        self.relations = []
        self.chapter_reached = 1

    def advance_chapter(self):
        self.chapter_reached += 1

    def add_relation(self, character, relationship_type="Neutre"):
        existing_relation = self.get_relation(character.name)
        if existing_relation:
            existing_relation.adjust_score(10 if relationship_type == "Ami" else -10)
        else:
            if isinstance(character, str):
                character = Character(character, "Description inconnue", "inconnu")
            new_relation = Relation(character, relationship_type)
            self.relations.append(new_relation)
            if relationship_type == "Ami":
                new_relation.adjust_score(10)
            elif relationship_type == "Ennemi":
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
        print(f"[Relation] {character_name} n'est plus dans vos relations.")




class Character(Entity):
    def __init__(self, name, sprite_path, description, role, gender="inconnu"):
        super().__init__(name, sprite_path, (300, 450))
        self.description = description
        self.role = role
        self.gender = gender  # Ajout de l'attribut genre


class GameMenu:
    def __init__(self, hero):
        self.hero = hero
        self.options = [
            "Continuer",
            "Afficher Relations",
            f"Santé : {self.hero.health} HP",  # Ajout de la santé comme option dynamique
            "Quitter"
        ]
        self.selected = 0
    
    def update_options(self):
        # Mise à jour dynamique de la santé à chaque affichage
        self.options[2] = f"Santé : {self.hero.health} HP"

    def draw(self, screen, font):
        self.update_options()  # Met à jour la santé avant de dessiner le menu
        width, height = screen.get_size()
        menu_box = pygame.Surface((400, 400))
        menu_box.fill((0, 0, 0, 180))
        pygame.draw.rect(menu_box, (255, 255, 255), (0, 0, 400, 400), 3)

        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected else (255, 255, 255)
            text = font.render(option, True, color)
            menu_box.blit(text, (50, 100 + i * 50))

        screen.blit(menu_box, (width // 2 - 200, height // 2 - 200))
        pygame.display.flip()
    
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            if event.key == pygame.K_RETURN:
                return self.selected
        return -1



class Relation:
    def __init__(self, character, status="Neutre", score=0):
        self.character = character
        self.score = 0
        self.status = status

    def adjust_score(self, amount):
        self.score += amount
        self.score = max(-100, min(100, self.score))  # Score entre -100 et 100
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
            if hasattr(self.character, 'gender') and self.character.gender.lower() == "fille":
                self.relationship_type = "Romance"
        else:
            self.relationship_type = "Frere d'armes"

    # Met aussi à jour le statut de la relation pour compatibilité
        self.status = self.relationship_type



class DialogueChoice:
    def __init__(self, text, relation_required=None, min_score=-100, max_score=100):
        self.text = text
        self.relation_required = relation_required  # Nom du personnage
        self.min_score = min_score
        self.max_score = max_score
        self.locked = False
    
    def is_available(self, hero):
        if not self.relation_required:
            return True  # Pas de condition, toujours disponible
        
        relation = hero.get_relation(self.relation_required)
        if relation:
            return self.min_score <= relation.score <= self.max_score
        return False
