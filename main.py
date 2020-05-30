import os

from game.game_logic import GameLogic
from game.objects.hexagon import Hexagon
from game.objects.tile_objects.grass import Grass
from game.renderer import Renderer

if __name__ == "__main__":
    Renderer.set_asset_path(os.path.join(os.getcwd(), "assets"))
    logic = GameLogic()
    game = Renderer("Nature Zen 2", size=(800, 600), game_logic=logic)
    # Hexagon.create_grid(22, 15, 50, logic)
    Hexagon.create_grid(22, 10, 50, logic)
    while game.running:
        game.update()
    game.cleanup()
