import json

def save_game(self):
    save_data = {
        "name": self.hero.name,
        "health": self.hero.health,
        "floor_reached": self.hero.floor_reached
    }
    with open("savegame.json", "w") as file:
        json.dump(save_data, file)
    print("[bold green]Partie sauvegardée avec succès ![/bold green]")
    input("\n[italic]Appuyez sur Entrée pour revenir au menu...[/italic]")
