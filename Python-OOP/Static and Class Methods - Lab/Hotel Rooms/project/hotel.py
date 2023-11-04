from typing import List

from Restaurant.project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next(filter(lambda x: x.number == room_number, self.rooms))
        result = room.take_room(people)

        if result:
            return result

        self.guests += people

    def free_room(self, room_number):
        room = next(filter(lambda x: x.number == room_number, self.rooms))
        guests = room.guests

        result = room.free_room()

        if result:
            return result

        self.guests -= guests

    def status(self):
        result = [
            f"Hotel {self.name} has {self.guests} total guests",
            f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}",
            f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"
        ]

        return "\n".join(result)


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
