from project.animals.animal import Mammal


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ != "Vegetable" and food.__class__.__name__ != "Fruit":
            return f"Mouse does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * 0.1
        self.food_eaten += food.quantity


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"Dog does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ != "Vegetable" and food.__class__.__name__ != "Meat":
            return f"Cat does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"Tiger does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * 1
        self.food_eaten += food.quantity
