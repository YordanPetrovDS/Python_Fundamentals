class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.quests = []

    def add_quest(self, person):
        self.quests.append(person)

    def get_summary(self):
        quest_names = ", ".join([quest.name for quest in self.quests])
        return f"Going: {quest_names}\nTotal: {len(self.quests)}"


party = Party()

while True:
    command = input()
    if command == "End":
        break

    person_name = command
    person = Person(person_name)
    party.add_quest(person)

print(party.get_summary())