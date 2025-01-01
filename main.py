from classes import *
from story import *

hero = Heros()    

1
tower = Tower()

for i in range(1, tower.MAX_FLOORS + 1):
    floor_events = [
        Event(f"Défi de l'étage {i}", f"Un défi mystérieux vous attend à l'étage {i}.", lambda h: None)
    ]
    tower.add_floor(floor_events)

# Exécution du prologue
prologue(hero)

tower.advance(hero)
if tower.current_floor == 1:
    floor1(hero, GameMenu(hero, tower))
    tower.advance(hero)
if tower.current_floor == 2:
    floor2(hero, GameMenu(hero, tower))
    tower.advance(hero)
if tower.current_floor == 3:
    floor3(hero, GameMenu(hero, tower))
    tower.advance(hero)
if tower.current_floor == 4:
    floor4(hero, GameMenu(hero, tower))
    tower.advance(hero)
if tower.current_floor == 5:
    floor5(hero, GameMenu(hero, tower))
    tower.advance(hero)
if tower.current_floor == 6:
    floor6(hero, GameMenu(hero, tower))
    tower.advance(hero)
if tower.current_floor == 7:
    floor7(hero, GameMenu(hero, tower))
    tower.advance(hero)

game_menu = GameMenu(hero, tower)

while hero.is_alive and tower.current_floor < tower.MAX_FLOORS:
    print(f"\n=== Etage {tower.current_floor} ===")
    game_menu.display()
    tower.advance(hero)

if hero.is_alive:
    print("\nVous avez atteint le sommet de la Tour Divine. La pierre de Cygide vous attend.")
else:
    print("\nVotre aventure s'arrête ici. Alderic sera une légende oubliée.")
