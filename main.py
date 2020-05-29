from game.game_logic import GameLogic
from game.objects.hexagon import Hexagon
from game.renderer import Renderer

if __name__ == "__main__":
    logic = GameLogic()
    Hexagon.create_grid(20, 10, 25, logic)
    game = Renderer("My Nice Game", size=(640, 400), game_logic=logic)
    while game.running:
        game.update()
    game.cleanup()
