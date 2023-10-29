from project.knight import Knight


class DarkKnight(Knight):

    def __init__(self, name, level):
        super().__init__(name, level)

    def __str__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"