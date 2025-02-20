import pygame
import sys
from notify import notify_change

ip


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
        self.max_health = 100
        self.relations = []
        self.chapter_reached = 1
        self.karma = 0  # Nouvel attribut
        self.dalgs = 0

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
        
    def adjust_health(self, amount, screen=None, font=None, clock=None):
       
        self.health += amount

        # Limite la santé au maximum défini
        if self.health > self.max_health:
            self.health = self.max_health
        elif self.health <= 0:
            self.health = 0
            print(f"{self.name} est à 0 points de vie. Aldric est mort.")
            if screen and font and clock:  # Vérifie que les éléments nécessaires sont fournis
                self.game_over(screen, font, clock)  # Appelle la fonction de Game Over

        print(f"{self.name} a maintenant {self.health}/{self.max_health} points de vie.")
        
        
    def adjust_karma(self, amount, screen, font, clock):
        """Ajuste le karma et affiche une notification."""
        self.karma = max(-100, min(100, self.karma + amount))

        # Déterminer le palier de karma
        if self.karma <= -100:
            karma_label = "Maléfique"
        elif self.karma <= -75:
            karma_label = "Sans Cœur"
        elif self.karma <= -50:
            karma_label = "Impitoyable"
        elif self.karma <= -25:
            karma_label = "Pragmatique"
        elif self.karma <= 24:
            karma_label = "Neutre"
        elif self.karma <= 50:
            karma_label = "Conciliant"
        elif self.karma <= 75:
            karma_label = "Empathique"
        elif self.karma <= 100:
            karma_label = "Saint"
        else:
            karma_label = "Indéfini"

        label = "Augmenté" if amount > 0 else "Diminué"
        color = (0, 0, 255) if amount > 0 else (255, 0, 0)  # Bleu pour gain, rouge pour perte
        text = f"Karma {label} de {abs(amount)} (Actuel : {self.karma}, Niveau : {karma_label})"

        notify_change(screen, font, text, color, clock)

    def add_relation(self, character, relationship_type="Neutre", screen=None, font=None, clock=None):
        existing_relation = self.get_relation(character.name)
        if existing_relation:
            existing_relation.adjust_score(10 if relationship_type == "Ami" else -10, screen, font, clock)
        else:
            new_relation = Relation(character, relationship_type)
            self.relations.append(new_relation)
            score_change = 10 if relationship_type == "Ami" else -10
            new_relation.adjust_score(score_change, screen, font, clock)

    def adjust_dalgs(self, amount):
        self.dalgs += amount
        if self.dalgs < 0:
            self.dalgs = 0  # Pas de monnaie négative




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
        self.relationship_type = status  # Ajout de l'attribut

    def adjust_score(self, amount, screen=None, font=None, clock=None):
   
        old_score = self.score
        self.score = max(-100, min(100, self.score + amount))
        self.update_relationship_type()

        label = "gagné" if amount > 0 else "perdu"
        color = (255, 215, 0) if amount > 0 else (255, 102, 102)  # Jaune pour gain, rouge clair pour perte
        text = f"Relation avec {self.character.name} : {label} {abs(amount)} points (Score : {self.score})"

        print(f"Relation ajustée pour {self.character.name} : {old_score} -> {self.score}")

        if screen and font and clock:
            notify_change(screen, font, text, color, clock)
            
    def update_relationship_type(self):
        if self.score <= -20:
            self.relationship_type = "Ennemi"
        elif -19 < self.score <= 19:
            self.relationship_type = "Neutre"
        elif 20 <= self.score <= 80:  # Inclure exactement 20 dans "Ami"
            self.relationship_type = "Ami"
        elif self.score > 80 and hasattr(self.character, 'gender') and self.character.gender.lower() == "fille":
            self.relationship_type = "Romance"
        else:
            self.relationship_type = "Frere d'armes"

        self.status = self.relationship_type  # Mettre à jour également `status`






class DialogueChoice:
    def __init__(self, text, relation_required=None, min_score=-100, max_score=100, karma_required=None):
        self.text = text
        self.relation_required = relation_required  # Nom du personnage
        self.min_score = min_score
        self.max_score = max_score
        self.locked = False
        self.karma_required = karma_required
    
    def is_available(self, hero):
        if not self.relation_required:
            return True  # Pas de condition, toujours disponible
        
        relation = hero.get_relation(self.relation_required)
        if relation:
            return self.min_score <= relation.score <= self.max_score
        return False
    
    def is_available(self, hero):
        # Vérifie si le karma du joueur permet ce choix
        if self.karma_required and hero.karma < self.karma_required:
            return False
        if not self.relation_required:
            return True
        relation = hero.get_relation(self.relation_required)
        return relation and self.min_score <= relation.score <= self.max_score

    
class Quest:
    def __init__(self, name, description, quest_function, rewards=None):
        """
        Initialise une quête narrative.
        
        Args:
            name (str): Nom de la quête.
            description (str): Description de la quête.
            quest_function (callable): Fonction qui gère l'exécution de la quête.
            rewards (list): Récompenses (facultatif).
        """
        self.name = name
        self.description = description
        self.quest_function = quest_function  # Fonction qui contient l'arc narratif
        self.completed = False
        self.rewards = rewards or []

    def start(self, hero):
        """
        Lance la quête en exécutant sa fonction dédiée.
        
        Args:
            hero (Heros): Référence au héros pour l'exécution de la quête.
        """
        print(f"Quête lancée : {self.name}")
        self.quest_function(hero)
        self.completed = True
        self.give_rewards(hero)

    def give_rewards(self, hero):
        """
        Applique les récompenses après la quête.
        
        Args:
            hero (Heros): Référence au héros pour appliquer les récompenses.
        """
        for reward in self.rewards:
            reward(hero)
        print(f"Quête '{self.name}' terminée. Récompenses appliquées.")
