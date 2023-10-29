class Hero:
    def __init__(self, name, level):
        self.username = name
        self.level = level

    def __str__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"
