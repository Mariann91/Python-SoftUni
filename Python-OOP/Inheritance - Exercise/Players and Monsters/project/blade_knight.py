from project.dark_knight import DarkKnight


class BladeKnight(DarkKnight):

    def __init__(self, name, level):
        super().__init__(name, level)

    def __str__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"