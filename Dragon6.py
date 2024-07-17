import random

import requests

class Chatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.openai.com/v1/completions"

    def send_prompt(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "prompt": prompt,
            "max_tokens": 50,  # Adjust based on desired response length
            "temperature": 0.7,  # Adjust based on desired creativity vs. coherence
            "top_p": 1,
            "stop": "\n"
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["text"].strip()
        else:
            print(f"Error: {response.text}")
            return None
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
    def __init__(self, description, dragon=None, choices=None, puzzle=None, gain=None):
        self.description = description
        self.dragon = dragon
        self.choices = choices or []
        self.puzzle = puzzle
        self.gain = gain or {}


# Generate random dragons
def generate_random_dragon():
    name = random.choice(["Fire Dragon", "Venomous Dragon", "Ice Dragon", "Electric Dragon", "Rock Dragon"])
    health = random.randint(150, 250)
    attack_power = random.randint(20, 40)
    defense = random.randint(10, 30)
    magic = random.randint(0, 50)
    poison = random.randint(0, 50)
    return Dragon(name, health, attack_power, defense, magic=magic, poison=poison)


# Generate random choices
def generate_random_choices():
    choices = []
    for _ in range(random.randint(1, 3)):
        choices.append(
            random.choice(["Fight the dragon", "Search for treasure", "Rest and recover", "Continue exploring"]))
    return choices


# Generate random gains for the player
def generate_random_gains():
    gains = {
        "health": random.randint(0, 20),
        "attack_power": random.randint(0, 10),
        "gold": random.randint(0, 50),
        "inventory": random.choice([["Sword"], ["Potion"], ["Gold", "Gem"]])
    }
    return gains


# Generate random puzzles
def generate_random_puzzle():
    puzzle_type = random.choice(["Math", "Riddle", "Logic"])
    if puzzle_type == "Math":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
        solution = eval(f"{num1} {operator} {num2}")
        return f"Solve the math problem: {num1} {operator} {num2}", solution
    elif puzzle_type == "Riddle":
        riddles = {
            "What has keys but can't open locks?": "Piano",
            "What comes once in a minute, twice in a moment, but never in a thousand years?": "M",
            "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?": "Echo"
        }
        riddle, answer = random.choice(list(riddles.items()))
        return riddle, answer
    elif puzzle_type == "Logic":
        logic_puzzles = [
            ("Mary's father has 5 daughters: 1. Nana, 2. Nene, 3. Nini, 4. Nono. What is the name of the 5th daughter?",
             "Mary"),
            ("How can you drop a raw egg onto a concrete floor without cracking it?",
             "Concrete floors are very hard to crack!"),
            ("What has a neck but no head?", "A bottle")
        ]
        return random.choice(logic_puzzles)


# Generate 100 random rooms
rooms = []
for _ in range(100):
    description = "You enter a mysterious room."
    dragon = generate_random_dragon() if random.random() < 0.5 else None
    choices = generate_random_choices() if random.random() < 0.5 else None
    puzzle = generate_random_puzzle() if random.random() < 0.3 else None
    gain = generate_random_gains() if random.random() < 0.3 else None
    rooms.append(Room(description, dragon, choices, puzzle, gain))


# Define game loop
# Define game loop
def play_game(player, rooms):
    current_room_index = 0
    while current_room_index < len(rooms):
        current_room = rooms[current_room_index]
        print("\n" + current_room.description)
        if current_room.dragon:
            print(f"The {current_room.dragon.name} appears!")
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
            print(f"You chose: {current_room.choices[choice_index - 1]}")
            # Apply gains for the player
            if current_room.gain:
                for attribute, value in current_room.gain.items():
                    if hasattr(player, attribute):
                        setattr(player, attribute, getattr(player, attribute) + value)
                    elif attribute == "inventory":

                        player.inventory.extend(value)
        if current_room.puzzle:
            puzzle_description, puzzle_solution = current_room.puzzle
            print("\n{}".format(puzzle_description))
            player_guess = input("Enter your guess: ")
            if player_guess.lower() == puzzle_solution.lower():
                print("Congratulations! You solved the puzzle!")
                if current_room.gain:
                    for attribute, value in current_room.gain.items():
                        if hasattr(player, attribute):
                            setattr(player, attribute, getattr(player, attribute) + value)
                        elif attribute == "inventory":
                            player.inventory.extend(value)
            else:
                print("Incorrect guess. The correct answer was: {}".format(puzzle_solution))

        current_room_index += 1
    else:
        print("Congratulations! You have reached the end of the labyrinth!")
player1 = Player("Hero", 100, 1000, 10000, gold=50000, inventory=["Sword", "Potion"])
play_game(player1, rooms)
