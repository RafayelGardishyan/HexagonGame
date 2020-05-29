class GameLogic:
    def __init__(self):
        self.objects = []

    def add_object(self, n_object):
        self.objects.append(n_object)

    def update(self, dt):
        for n_object in self.objects:
            n_object.update(dt)
