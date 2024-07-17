import random


class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack(self, target, domain):
        if hasattr(self, domain):
            attack_value = getattr(self, domain)
            if attack_value > 0:
                damage = max(attack_value - target.defense, 0)
                target.take_damage(damage)
                print(f"{self.name} attacks {target.name} for {damage} damage in {domain} domain.")
            else:
                print(f"{self.name} cannot use {domain} for attack!")
        else:
            print(f"{self.name} does not have {domain} for attack!")


class Player(Character):
    def __init__(self, name, health, attack_power, defense, gold=0, inventory=None):
        super().__init__(name, health, attack_power, defense)
        self.gold = gold
        self.inventory = inventory or []


class Dragon(Character):
    def __init__(self, name, health, attack_power, defense, magic=0, poison=0):
        super().__init__(name, health, attack_power, defense)
        self.magic = magic
        self.poison = poison


class Room:
    def __init__(self, description, dragon=None, choices=None):
        self.description = description
        self.dragon = dragon
        self.choices = choices or []


# Define a list of rooms in the labyrinth
rooms = [
    Room("You enter a dark cave. You encounter a fierce fire-breathing dragon!",
         dragon=Dragon("Fire Dragon", 200, 30, 20, magic=40, poison=10),
         choices=["Fight the dragon", "Run away"]),
    Room("You find yourself in a mystical forest. A venomous dragon lurks in the shadows!",
         dragon=Dragon("Venomous Dragon", 180, 25, 25, magic=30, poison=20),
         choices=["Prepare to battle", "Sneak past"]),
    Room("You stumble upon an ancient ruin. A mighty ice dragon guards its treasure!",
         dragon=Dragon("Ice Dragon", 220, 35, 15, magic=20),
         choices=["Confront the dragon", "Search for hidden passage"]),
    Room( "This is the room of mirrors! Be careful , not everything you see is a reflection!", dragon=Dragon("Miror-Mirror_In_The_Wall", 100,15,25, magic=17, poison=25),
          choices=["Confront the dragon","Hide underneath the bed", "Run =Run as quick as you can"]),
    Room("You enter a dark cave. You encounter a fierce fire-breathing dragon!",
         dragon=Dragon("Fire Dragon", 200, 30, 20, magic=40, poison=10),
         choices=["Fight the dragon", "Run away", "Try to negotiate", "Hide behind rocks"]),
    Room("You step into a misty forest. A giant spider descends from the trees!",
         dragon=Dragon("Giant Spider", 150, 25, 15, magic=20, poison=30),
         choices=["Attack the spider", "Climb a tree", "Use fire magic", "Offer it food"]),
    Room("You find yourself in a swamp. A swamp monster emerges from the murky water!",
         dragon=Dragon("Swamp Monster", 180, 28, 18, magic=25, poison=25),
         choices=["Engage in combat", "Sneak past it", "Offer a sacrifice", "Ask for help"]),
    Room("You arrive at an ancient temple. A guardian spirit stands in your path!",
         dragon=Dragon("Guardian Spirit", 170, 26, 16, magic=35, poison=15),
         choices=["Invoke a protective spell", "Respectfully ask to pass", "Offer a gift",
                  "Challenge to a riddle contest"]),
    Room("You venture into a desolate graveyard. A group of undead skeletons shamble towards you!",
         dragon=Dragon("Undead Skeletons", 160, 27, 17, magic=30, poison=20),
         choices=["Fight the skeletons", "Turn undead", "Search for holy relics", "Make a deal with necromancy"]),
    Room("You find yourself in a bustling marketplace. A shady figure offers you a mysterious potion!",
         dragon=Dragon("Shady Figure", 140, 22, 12, magic=15, poison=35),
         choices=["Buy the potion", "Decline and move on", "Bargain for a lower price", "Report to the authorities"]),
    Room("You stumble upon a hidden cave filled with treasure. A greedy dragon guards its hoard!",
         dragon=Dragon("Greedy Dragon", 220, 35, 25, magic=45, poison=20),
         choices=["Steal the treasure", "Offer a trade", "Try to reason with the dragon", "Escape without disturbing"]),
    Room("You enter an enchanted forest. A mischievous fairy challenges you to a game of wits!",
         dragon=Dragon("Mischievous Fairy", 130, 20, 10, magic=25, poison=10),
         choices=["Accept the challenge", "Bribe the fairy", "Cast a charm spell", "Tell a joke"]),
    Room("You reach a crossroads in the mountains. A wise old sage offers you guidance on your journey!",
         dragon=Dragon("Wise Old Sage", 150, 24, 14, magic=30, poison=10),
         choices=["Listen to the sage's advice", "Ignore the sage and choose your own path",
                  "Ask for magical assistance", "Offer payment for information"]),
    Room("You stumble into a hidden chamber filled with traps. A treasure chest sits at the center!",
         dragon=Dragon("Trap-filled Chamber", 180, 28, 18, magic=20, poison=20),
         choices=["Attempt to disarm the traps", "Bypass the traps with magic", "Risk opening the chest",
                  "Leave the chamber untouched"])
]


# Define game loop
def play_game(player, rooms):
    current_room_index = 0
    while current_room_index < len(rooms):
        current_room = rooms[current_room_index]
        print("\n" + current_room.description)
        if current_room.dragon:
            print(f"The {current_room.dragon.name} appears!")
            # Implement combat or flee logic here
            # For simplicity, let's assume player always fights
            player.attack(current_room.dragon, "attack_power")
            if current_room.dragon.health > 0:
                current_room.dragon.attack(player, "magic")
                if player.health <= 0:
                    print("Game Over! You have been defeated.")
                    break
        if current_room.choices:
            print("\nChoices:")
            for i, choice in enumerate(current_room.choices, 1):
                print(f"{i}. {choice}")
            choice_index = int(input("Enter your choice (1 - {}): ".format(len(current_room.choices))))
            # Implement choice handling here
            # For simplicity, let's assume player always chooses the first option
            print(f"You chose: {current_room.choices[choice_index - 1]}")
        current_room_index += 1
    else:
        print("Congratulations! You have reached the end of the labyrinth!")


# Example usage
player1 = Player("Hero", 1000, 2000, 1000, gold=5000, inventory=["Sword", "Potion","Chocolate"])
play_game(player1, rooms)
