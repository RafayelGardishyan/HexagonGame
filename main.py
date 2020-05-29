from game.game_logic import GameLogic
from game.objects.hexagon import Hexagon
from game.renderer import Renderer

if __name__ == "__main__":
    logic = GameLogic()
    Hexagon.create_grid(22, 15, 25, logic)
    game = Renderer("Nature Zen 2", size=(800, 600), game_logic=logic)
    while game.running:
        game.update()
    game.cleanup()
