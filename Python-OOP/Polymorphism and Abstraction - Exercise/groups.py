class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, group_two):
        new_group_people = self.people.copy()
        new_group_people.extend(group_two.people)

        return Group(name=f"{self.name} {group_two.name}", people=new_group_people)

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"

    def __iter__(self):
        return iter(f"Person {index}: {self.people[index]}" for index in range(len(self.people)))

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(f'{personal.name} {personal.surname}' for personal in self.people)}"
      
