class Camera:
    def __init__(self):
        self.x_offset, self.y_offset = 0, 0

    def move_camera(self, x_offset, y_offset):
        self.x_offset += x_offset
        self.y_offset += y_offset

    def get_offset(self):
        return self.x_offset, self.y_offset
