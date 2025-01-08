import pygame
import sys
from classes import *
from pygame.locals import *
from graphics import *
from save_manager import *

menu_stack = []

WIDTH, HEIGHT = 800, 600


def display_text(screen, text, pos, font, max_width=700, delay=25):
    x, y = pos
    line_height = font.get_linesize() + 5
    lines = wrap_text(text, font, max_width)

    for line in lines:
        word_surface = font.render(line, True, (255, 255, 255))
        screen.blit(word_surface, (x, y))
        y += line_height
        pygame.display.flip()
        pygame.time.wait(delay)


def afficher_dialogues(screen, font, clock, dialogues):
    dialogue_index = 0
    in_dialogue = True

    while in_dialogue:
        clear_screen(screen)
        display_dialogue_box(screen, dialogues[dialogue_index], font, clock)

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    dialogue_index += 1
                    if dialogue_index >= len(dialogues):
                        in_dialogue = False
                    waiting = False
                
                
def display_delay(screen, font, text, clock, speed=30, max_width=700):
    screen.fill((0, 0, 0))
    lines = wrap_text(text, font, max_width)
    
    y = 300
    line_height = font.get_linesize() + 5
    rendered_text = ""

    for line in lines:
        for char in line:
            rendered_text += char
            screen.fill((0, 0, 0))
            text_surface = font.render(rendered_text, True, (255, 255, 255))
            screen.blit(text_surface, (50, y))
            pygame.display.flip()
            clock.tick(speed)
        rendered_text = ""
        y += line_height

    pygame.time.wait(1000)




def wrap_text(text, font, max_width):
    if isinstance(text, tuple):  # Si c'est un tuple, récupère seulement le texte
        text = text[1]

    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        test_line = current_line + word + ' '
        if font.size(test_line)[0] > max_width:
            lines.append(current_line)
            current_line = word + ' '
        else:
            current_line = test_line

    if current_line:
        lines.append(current_line)
    return lines




def display_choices_box(screen, font, options, clock, box_width=700, box_height=150, width=800, height=600, alpha=200):
    selected = 0
    dialogue_font = pygame.font.Font("graphics/resources/font/Cinzel-Regular.otf", 15)
    line_height = dialogue_font.get_linesize() + 10
    padding = 20

    # Chargement des sons de sélection et de clic
    select_sound = pygame.mixer.Sound("graphics/resources/music/menuselection.mp3")
    click_sound = pygame.mixer.Sound("graphics/resources/music/menuclick.mp3")

    box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
    pygame.draw.rect(box_surface, (30, 30, 30, alpha), (0, 0, box_width, box_height))
    pygame.draw.rect(box_surface, (255, 255, 255, 120), (0, 0, box_width, box_height), 3)

    while True:
        box_surface.fill((30, 30, 30, alpha))
        pygame.draw.rect(box_surface, (255, 255, 255, 120), (0, 0, box_width, box_height), 3)

        y = padding
        for i, option_text in enumerate([opt[0] for opt in options]):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            rendered_text = dialogue_font.render(f"> {option_text}" if i == selected else option_text, True, color)
            box_surface.blit(rendered_text, (padding, y))
            y += line_height

        screen.blit(box_surface, (width // 2 - box_width // 2, height - 370))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    select_sound.play()  # Son lors de la navigation
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    select_sound.play()  # Son lors de la navigation
                if event.key == pygame.K_RETURN:
                    click_sound.play()  # Son lors de la sélection
                    clear_screen(screen)
                    return selected

        clock.tick(30)

 
 
        
def fade_out(screen, width, height):
    fade_surface = pygame.Surface((width, height))
    fade_surface.fill((0, 0, 0))
    
    for alpha in range(0, 255, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(5)
    
    screen.fill((0, 0, 0))
    pygame.display.flip()




def fade_in_text(screen, text, font, pos=(400, 300), duration=3000, fade_speed=1, max_width=700):
    """
    Fait apparaître progressivement du texte avec un effet de fondu.

    Args:
        screen: surface pygame
        text: texte à afficher
        font: police pygame
        pos: tuple de position (x, y) du centre du texte
        duration: durée en millisecondes
        fade_speed: vitesse du fondu (plus petit = plus lent)
        max_width: largeur maximale pour éviter que le texte sorte de l'écran
    """
    # Divise le texte en lignes qui respectent la largeur max_width
    lines = wrap_text(text, font, max_width)
    x, y = pos

    # Ajuste la position verticale pour centrer toutes les lignes
    total_height = len(lines) * font.get_linesize()
    y -= total_height // 2

    # Effet de fondu en apparaissant progressivement
    for alpha in range(0, 255, fade_speed):
        screen.fill((0, 0, 0))  # Nettoie l'écran à chaque itération

        # Affiche chaque ligne de texte avec la transparence en cours
        for i, line in enumerate(lines):
            word_surface = font.render(line, True, (255, 255, 255))
            text_rect = word_surface.get_rect(center=(x, y + i * font.get_linesize()))
            temp_surface = word_surface.copy()
            temp_surface.set_alpha(alpha)
            screen.blit(temp_surface, text_rect)

        pygame.display.flip()
        pygame.time.delay(20)  # Délai pour ralentir l'effet de fondu

    # Maintient le texte visible après le fondu pendant la durée spécifiée
    pygame.time.wait(duration)




def fade_out_text(screen, duration=3000, fade_speed=2):
    current = screen.copy()  # Capture l'écran actuel
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((0, 0, 0))
    
    for alpha in range(0, 255, fade_speed):
        screen.blit(current, (0, 0))  # Restaure l'écran original
        fade_surface.set_alpha(alpha)  # Augmente progressivement l'opacité du noir
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)
    
    screen.fill((0, 0, 0))  # Assure que l'écran est complètement noir à la fin
    pygame.display.flip()
    pygame.time.wait(duration)



def clear_screen(screen):
    screen.fill((0, 0, 0))
    pygame.display.flip()


def display_save_confirmation(screen, font, message):
    width, height = screen.get_size()
    box_width, box_height = 800, 250

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (30, 30, 30), (width // 2 - box_width // 2,
                                            height // 2 - box_height // 2,
                                            box_width, box_height))
    pygame.draw.rect(screen, (255, 255, 255), (width // 2 - box_width // 2,
                                               height // 2 - box_height // 2,
                                               box_width, box_height), 3)

    text_surface = font.render(message, True, (255, 255, 255))
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2,
                               height // 2 - box_height // 2 + 30))

    return_text = font.render("Appuyez sur Entrée pour continuer", True, (255, 255, 0))
    screen.blit(return_text, (width // 2 - return_text.get_width() // 2,
                              height // 2 + box_height // 2 - 30))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False
                clear_screen(screen)  # Nettoyage après retour au menu


def wait_for_keypress(beep_sound=None, volume=0.2):
    if beep_sound is None:
        beep_sound = pygame.mixer.Sound("graphics/resources/music/beep.mp3")
    
    beep_sound.set_volume(volume)  # Ajuste le volume du bip

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()  # Joue le son lorsque "Entrée" est pressé
                waiting = False

        



def display_dialogue_with_sprite(screen, text, font, clock, sprite, box_width=700, box_height=150, width=800, height=600, alpha=200, speed=10):
    global background
    screen.blit(background, (0, 0))

    # Crée la surface de la boîte de dialogue
    box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
    pygame.draw.rect(box_surface, (30, 30, 30, alpha), (0, 0, box_width, box_height))
    pygame.draw.rect(box_surface, (255, 255, 255, 120), (0, 0, box_width, box_height), 3)

    # Redimensionne le sprite
    sprite = resize_sprite(sprite, max_width=110, max_height=110)
    sprite_rect = sprite.get_rect()

    # Centre verticalement le sprite à l'intérieur de la boîte
    sprite_rect.topleft = (20, (box_height - sprite_rect.height) // 2)

    dialogue_font = pygame.font.Font("graphics/resources/font/Cinzel-Regular.otf", 15)

    # Ajuste le texte pour laisser de la place au sprite
    text_x_offset = sprite_rect.width + 40
    lines = wrap_text(text, dialogue_font, box_width - text_x_offset - 40)
    x, y = text_x_offset, 20
    line_height = dialogue_font.get_linesize() + 5
    rendered_text = ""
    arrow_shown = False

    beep_sound = pygame.mixer.Sound("graphics/resources/music/beep.mp3")

    # Affiche progressivement le texte
    for line in lines:
        for char in line:
            rendered_text += char
            box_surface.fill((0, 0, 0, 0))
            pygame.draw.rect(box_surface, (30, 30, 30, alpha), (0, 0, box_width, box_height))
            pygame.draw.rect(box_surface, (255, 255, 255, 120), (0, 0, box_width, box_height), 3)

            # Blitte le sprite à l'intérieur de la boîte
            box_surface.blit(sprite, sprite_rect)

            # Dessin du texte progressivement
            y_offset = 20
            for l in wrap_text(rendered_text, dialogue_font, box_width - text_x_offset - 40):
                word_surface = dialogue_font.render(l, True, (255, 255, 255))
                box_surface.blit(word_surface, (x, y_offset))
                y_offset += line_height

            # Blitte la boîte avec texte et sprite sur l'écran
            screen.blit(box_surface, (width // 2 - box_width // 2, height - 200))
            pygame.display.flip()
            pygame.time.wait(speed)

        rendered_text += "\n"

    # Dessine la flèche après que tout le texte a été affiché
    pygame.draw.polygon(box_surface, (255, 255, 255), [
        (box_width - 30, box_height - 20),
        (box_width - 20, box_height - 10),
        (box_width - 40, box_height - 10)
    ])
    screen.blit(box_surface, (width // 2 - box_width // 2, height - 200))
    pygame.display.flip()

    # Attendre l'appui d'une touche
    wait_for_keypress(beep_sound)


 
            
def resize_sprite(sprite, max_width=110, max_height=110):
    if sprite.get_width() > max_width or sprite.get_height() > max_height:
        aspect_ratio = min(max_width / sprite.get_width(), max_height / sprite.get_height())
        new_width = int(sprite.get_width() * aspect_ratio)
        new_height = int(sprite.get_height() * aspect_ratio)
        return pygame.transform.scale(sprite, (new_width, new_height))
    return sprite



def display_dialogue_box(screen, text, font, clock, box_width=700, box_height=150, width=800, height=600, alpha=120, speed=10):
    global background
    screen.blit(background, (0, 0))  # Réaffiche le fond pour éviter d'effacer

    box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
    pygame.draw.rect(box_surface, (30, 30, 30, alpha), (0, 0, box_width, box_height))
    pygame.draw.rect(box_surface, (255, 255, 255, 120), (0, 0, box_width, box_height), 3)

    dialogue_font = pygame.font.Font("graphics/resources/font/Cinzel-Regular.otf", 15)
    lines = wrap_text(text, dialogue_font, box_width - 40)
    x, y = 20, 20
    line_height = dialogue_font.get_linesize() + 5

    rendered_text = ""

    beep_sound = pygame.mixer.Sound("graphics/resources/music/beep.mp3")

    # Affiche progressivement chaque caractère
    for line in lines:
        for char in line:
            rendered_text += char
            box_surface.fill((0, 0, 0, 0))  # Efface avec transparence
            pygame.draw.rect(box_surface, (30, 30, 30, alpha), (0, 0, box_width, box_height))
            pygame.draw.rect(box_surface, (255, 255, 255, 120), (0, 0, box_width, box_height), 3)

            y_offset = 20
            for l in wrap_text(rendered_text, dialogue_font, box_width - 40):
                word_surface = dialogue_font.render(l, True, (255, 255, 255))
                box_surface.blit(word_surface, (x, y_offset))
                y_offset += line_height

            screen.blit(box_surface, (width // 2 - box_width // 2, height - 200))
            pygame.display.flip()
            pygame.time.wait(speed)

        rendered_text += "\n"  # Passe à la ligne pour le texte suivant

    # Dessine la flèche une fois le texte affiché
    pygame.draw.polygon(box_surface, (255, 255, 255), [
        (box_width - 30, box_height - 20),
        (box_width - 20, box_height - 10),
        (box_width - 40, box_height - 10)
    ])
    screen.blit(box_surface, (width // 2 - box_width // 2, height - 200))
    pygame.display.flip()

    # Attend la pression d'une touche
    wait_for_keypress(beep_sound)




def process_dialogue(screen, font, hero, options, clock, relation_name):
    choice = display_choices_box(screen, font, options, clock)  # Boîte de choix interactifs

    score_adjustment = options[choice][1]
    dialogue_lines = options[choice][2]

    if relation_name and hasattr(hero, 'get_relation'):
        relation = hero.get_relation(relation_name)
        if relation:
            relation.adjust_score(score_adjustment)
    
    # Réaffiche l'image de fond après le choix
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Affiche les dialogues après le choix avec les sprites associés
    for sprite, line in dialogue_lines:
        if sprite:
            display_dialogue_with_sprite(screen, line, font, clock, sprite)
        else:
            display_dialogue_box(screen, line, font, clock)


     
def load_sprites():
    sprites = {}

    # Liste des sprites avec leur nom de fichier
    sprite_files = {
        "Aldric": "Aldric1.webp",
        "Ayela": "Ayela.webp",
        "Brandio": "Brandio.webp",
        "Clotaire": "Clotaire.webp",
        "Durnir": "Durnir.webp",
        "Emphyr": "Emphyr.webp",
        "Gallius": "Gallius.webp",
        "Garen": "Garen1.webp",
        "Homme_mysterieux": "hmystere.webp",
        "Kael": "Kael.webp",
        "Velm": "Velm.webp",
        "Yohna": "Yohna.webp",
        "Zyn": "Zyn.webp",
    }

    # Parcours et chargement des sprites
    for name, file in sprite_files.items():
        path = f"graphics/resources/sprites/{file}"
        sprite = pygame.image.load(path)
        sprite = resize_sprite(sprite)  # Redimensionner automatiquement
        sprites[name] = sprite

    return sprites



def display_background(screen, image_path, fade_speed=5):
    background = pygame.image.load(image_path)
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

    for alpha in range(0, 255, fade_speed):
        temp_surface = background.copy()
        temp_surface.set_alpha(alpha)
        screen.blit(temp_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)


def play_music(music_path, volume=0.3, loop=-1):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loop)



def set_background(image_path, width, height):
    global background  # Déclare la variable globale
    background = pygame.image.load(image_path)
    background = pygame.transform.scale(background, (width, height))
    return background



def fade_in_background(screen, image_path, width, height, duration=1500):
    global background
    background = pygame.image.load(image_path)
    background = pygame.transform.scale(background, (width, height))

    # Effet de fondu en 30 étapes (50 ms par étape pour atteindre 1,5 s)
    fade_steps = 30
    fade_delay = duration // fade_steps  # Délai entre chaque étape de fondu

    for alpha in range(0, 256, 256 // fade_steps):
        temp_surface = background.copy()
        temp_surface.set_alpha(alpha)
        screen.blit(temp_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(fade_delay)

    # Finalisation - affiche l'image finale
    screen.blit(background, (0, 0))
    pygame.display.flip()
    return background
 
 
    
def fade_in_music(music_path, max_volume=0.5, fade_duration=3000):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(-1)
    
    fade_steps = 50
    step_delay = fade_duration // fade_steps
    
    for i in range(fade_steps):
        volume = (i / fade_steps) * max_volume
        pygame.mixer.music.set_volume(volume)
        pygame.time.delay(step_delay)





def fade_out_music(fade_duration=3000):
    fade_steps = 50
    step_delay = fade_duration // fade_steps
    current_volume = pygame.mixer.music.get_volume()
    
    for i in range(fade_steps):
        volume = current_volume * (1 - (i / fade_steps))
        pygame.mixer.music.set_volume(volume)
        pygame.time.delay(step_delay)
    
    pygame.mixer.music.stop()
    
    
    
    
def display_game_menu(screen, font, clock, options):
    selected = 0
    width, height = screen.get_size()
    box_width, box_height = 600, 300
    padding = 30
    line_height = font.get_linesize() + 10

    # Chargement des sons de sélection et de clic
    select_sound = pygame.mixer.Sound("graphics/resources/music/menuselection.mp3")
    click_sound = pygame.mixer.Sound("graphics/resources/music/menuclick.mp3")

    box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)

    while True:
        box_surface.fill((0, 0, 0, 180))
        pygame.draw.rect(box_surface, (255, 255, 255, 150), (0, 0, box_width, box_height), 3)

        y = padding
        for i, option in enumerate(options):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            rendered_text = font.render(option, True, color)
            box_surface.blit(rendered_text, (padding, y))
            y += line_height

        screen.blit(box_surface, ((width - box_width) // 2, (height - box_height) // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    select_sound.play()  # Son de navigation
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    select_sound.play()  # Son de navigation
                if event.key == pygame.K_RETURN:
                    click_sound.play()  # Son de validation
                    return selected
        
        clock.tick(30)
  
  
        
def start_next_chapter(hero, screen, font, clock):
    if hero.chapter_reached <= chapitre_max_implémenté():  # Vérifie si le chapitre est implémenté
        hero.advance_chapter()  # Passe au chapitre suivant uniquement si implémenté
        save_game(hero)  # Sauvegarde immédiatement
        print(f"Début du Chapitre {hero.chapter_reached}")
        
        fade_in_text(screen, f"Chapitre {hero.chapter_reached} : L'aventure continue", font, (400, 300), 3000)
        fade_out_text(screen, 3000)
    else:
        print("Chapitre non implémenté. Rester au chapitre actuel.")


def chapitre_max_implémenté():
    chapters = [func for func in globals() if func.startswith("chapitre_")]
    return len(chapters)


def display_relations(screen, font, hero):
    relations_text = [f"{rel.character.name}: {rel.status} ({rel.score})" for rel in hero.relations]

    width, height = screen.get_size()  # Récupère la taille dynamique de l'écran

    display_text(screen, "\n".join(relations_text), (width // 2 - 300, height // 2 - 100), font)


def game_menu(screen, font, clock, width, height, hero):
    global menu_stack

    background = pygame.image.load("graphics/resources/backgrounds/tour3.webp")
    background = pygame.transform.scale(background, (width, height))
    title_font = pygame.font.Font("graphics/resources/font/CinzelDecorative-Bold.otf", 70)

    select_sound = pygame.mixer.Sound("graphics/resources/music/menuselection.mp3")
    click_sound = pygame.mixer.Sound("graphics/resources/music/menuclick.mp3")

    options = ["Continuer", "Afficher Relation", "Sauvegarder", "Quitter"]
    selected = 0
    box_width = 450
    box_height = 400
    line_height = font.get_linesize() + 20
    padding_top = 40

    # Empiler ce menu dans la pile
    menu_stack.append("game_menu")

    while menu_stack and menu_stack[-1] == "game_menu":
        screen.blit(background, (0, 0))
        title_surface = title_font.render("Menu de Jeu", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(width // 2, height // 6))
        screen.blit(title_surface, title_rect)

        menu_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        menu_surface.fill((0, 0, 0, 180))
        pygame.draw.rect(menu_surface, (255, 255, 255, 150), (0, 0, box_width, box_height), 3)

        y = padding_top
        for i, option in enumerate(options):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            text_surface = font.render(option, True, color)
            menu_surface.blit(text_surface, (60, y))
            y += line_height

        screen.blit(menu_surface, (width // 2 - box_width // 2, height // 2 - box_height // 2 + 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    select_sound.play()
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    select_sound.play()
                if event.key == pygame.K_RETURN:
                    click_sound.play()
                    pygame.time.wait(300)

                    if selected == 0:  # Continuer
                        start_next_chapter(hero, screen, font, clock)
                        menu_stack.pop()  # Enlève ce menu après action
                    elif selected == 1:  # Afficher Relations
                        display_relations_screen(screen, font, clock, hero)
                    elif selected == 2:  # Sauvegarder
                        save_game(hero)
                        display_save_confirmation(screen, font, "Partie sauvegardée avec succès")
                    elif selected == 3:  # Retour au menu principal
                        menu_stack.clear()  # Vide la pile pour s'assurer de revenir au main_menu
                        main_menu(screen, font, clock)  # Relance le menu principal

def display_relations_screen(screen, font, clock, hero):
    global menu_stack

    relations_text = [f"{rel.character.name} - {rel.relationship_type} ({rel.score})"
                      for rel in hero.relations]

    width, height = screen.get_size()
    box_width, box_height = 700, 400

    while True:
        screen.fill((0, 0, 0))  # Efface tout l'écran avant d'afficher
        pygame.draw.rect(screen, (30, 30, 30), (width // 2 - box_width // 2,
                                                height // 2 - box_height // 2,
                                                box_width, box_height))
        pygame.draw.rect(screen, (255, 255, 255), (width // 2 - box_width // 2,
                                                   height // 2 - box_height // 2,
                                                   box_width, box_height), 3)

        y = height // 2 - box_height // 2 + 50
        for relation_text in relations_text:
            text_surface = font.render(relation_text, True, (255, 255, 255))
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, y))
            y += font.get_linesize() + 10

        return_text = font.render("Appuyez sur Entrée pour revenir", True, (255, 255, 0))
        screen.blit(return_text, (width // 2 - return_text.get_width() // 2, height - 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if menu_stack:  # Vérification avant de faire pop
                        menu_stack.pop()
                    clear_screen(screen)  # Efface l'écran après retour
                    return
                
                

def return_to_main_menu(screen, font, clock):
    fade_out(screen, WIDTH, HEIGHT)
    main_menu(screen, font, clock)
    
    
    
    

def main_menu(screen, font, clock):
    # Chargement des ressources
    background = pygame.image.load("graphics/resources/backgrounds/tour3.webp")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # L'image prend tout l'écran
    
    # Utilisation de la nouvelle police CinzelDecorative-Bold avec une taille plus petite
    title_font = pygame.font.Font("graphics/resources/font/CinzelDecorative-Bold.otf", 70)
    select_sound = pygame.mixer.Sound("graphics/resources/music/menuselection.mp3")
    click_sound = pygame.mixer.Sound("graphics/resources/music/menuclick.mp3")
    pygame.mixer.music.load("graphics/resources/music/mystical.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # Boucle infinie de la musique

    options = ["Nouvelle Partie", "Charger Partie", "Quitter"]
    selected = 0
    width, height = screen.get_size()
    box_width = 450  # Réduction de la largeur du menu
    box_height = 250  # Réduction de la hauteur du menu

    while True:
        # Affichage de l'arrière-plan pleine taille
        screen.blit(background, (0, 0))
        
        # Affiche le titre avec une taille plus petite pour éviter le dépassement
        title_surface = title_font.render("99 FLOORS : ASCENT", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(width // 2, height // 6))  # Titre placé légèrement plus haut
        screen.blit(title_surface, title_rect)

        # Crée une surface semi-transparente pour le menu
        menu_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        menu_surface.fill((0, 0, 0, 150))  # Fond noir avec 150 de transparence

        # Dessine la boîte semi-transparente
        screen.blit(menu_surface, (width // 2 - box_width // 2, height // 2 - box_height // 2 + 100))
        pygame.draw.rect(screen, (255, 255, 255), 
                         (width // 2 - box_width // 2, height // 2 - box_height // 2 + 100, 
                          box_width, box_height), 3)
        
        # Affiche les options du menu
        for i, option in enumerate(options):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            text_surface = font.render(option, True, color)
            
            text_rect = text_surface.get_rect(center=(width // 2, height // 2 + 50 + i * 50))  # Réduction de l'espace entre les options
            screen.blit(text_surface, text_rect.topleft)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    select_sound.play()
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    select_sound.play()
                if event.key == pygame.K_RETURN:
                    click_sound.play()
                    pygame.time.wait(300)
                    return selected




