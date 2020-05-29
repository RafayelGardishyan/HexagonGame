import pygame


class Renderer:
    def __init__(self, window_name, fps=60, size=(800, 600), favicon=None, game_logic=None):
        self.running = True
        self.size = self.width, self.height = size
        self.game_logic = game_logic
        self.fps = fps
        self.clock = pygame.time.Clock()
        pygame.init()

        if favicon is not None:
            logo = pygame.image.load(favicon)
            pygame.display.set_icon(logo)

        pygame.display.set_caption(window_name)

        self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def update(self):
        dt = self.clock.tick(self.fps) / 1000.0

        for event in pygame.event.get():
            self.on_event(event)

        if self.game_logic is not None:
            self.game_logic.update(dt)
            
        self.draw()

        pygame.display.flip()

    @staticmethod
    def cleanup():
        pygame.quit()

    def draw(self):
        self._screen.fill((0, 0, 0))
        for m_object in self.game_logic.objects:
            m_object.draw(self._screen)


