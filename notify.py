import pygame
import sys
&
active_notifications = []


def wrap_text(text, font, max_width):
    """
    Divise le texte en lignes pour s'adapter à une largeur donnée.

    Args:
        text: Texte à afficher.
        font: Police utilisée.
        max_width: Largeur maximale pour chaque ligne.

    Returns:
        Liste de lignes adaptées à la largeur.
    """
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines


def notify_change(screen, font, text, color, clock, duration=3000, box_width=700, box_height=150, sound_path="graphics/resources/music/earn.mp3"):
    """
    Affiche une notification dans une boîte centrée à l'écran, avec gestion des chevauchements et un son.

    Args:
        screen: surface pygame
        font: police pygame
        text: texte de la notification
        color: couleur du texte
        clock: horloge pygame
        duration: durée d'affichage (ms)
        box_width: largeur de la boîte
        box_height: hauteur de la boîte
        sound_path: Chemin du fichier audio.
    """
    global active_notifications

    # Charger et jouer le son
    try:
        earn_sound = pygame.mixer.Sound("graphics/resources/music/earn.mp3")
        earn_sound.set_volume(0.3)
        earn_sound.play()
    except Exception as e:
        print(f"Erreur lors du chargement du son : {e}")

    width, height = screen.get_size()
    wrapped_text = wrap_text(text, font, box_width - 40)

    # Ajuster la hauteur de la boîte si plusieurs lignes
    adjusted_height = max(box_height, 30 + len(wrapped_text) * font.get_linesize())

    # Calcul de la position verticale basée sur les notifications actives
    y_offset = height // 2 - adjusted_height // 2 + len(active_notifications) * (adjusted_height + 10)

    # Créer une surface pour la boîte
    box_surface = pygame.Surface((box_width, adjusted_height), pygame.SRCALPHA)
    pygame.draw.rect(box_surface, (30, 30, 30, 180), (0, 0, box_width, adjusted_height))
    pygame.draw.rect(box_surface, (255, 255, 255), (0, 0, box_width, adjusted_height), 3)

    # Rendre chaque ligne de texte
    y_text = 20
    for line in wrapped_text:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(box_width // 2, y_text + font.get_linesize() // 2))
        box_surface.blit(text_surface, text_rect)
        y_text += font.get_linesize()

    # Ajouter la notification à la liste active
    active_notifications.append((box_surface, y_offset))

    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Afficher toutes les notifications actives
        for i, (surface, y) in enumerate(active_notifications):
            screen.blit(surface, (width // 2 - box_width // 2, y))

        pygame.display.flip()
        clock.tick(30)

    # Retirer la notification actuelle après affichage
    active_notifications.pop(0)
