class Party:
  def __init__(self):
    self.people = []


party = Party()

name = input()

while name != "End":
  party.people.append(name)
  name = input()
  
people = ", ".join(party.people)
total_people_going = len(party.people)

print(f"Going: {people}\nTotal: {total_people_going}")
