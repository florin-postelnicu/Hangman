

import random

class Game:
    def __init__(self):
        self.game_state = "start"  # Default game state
        self.players = []          # List of players
        self.current_room = None   # Reference to the current room
        self.game_map = {}         # Game world map
        self.game_settings = {}    # Game settings

    def start_game(self):
        # Initialize the game and start gameplay
        print("Starting the game...")

    def end_game(self):
        # End the game and perform cleanup tasks
        print("Ending the game...")

    def save_game(self):
        # Save the current game state
        print("Saving the game...")

    def load_game(self):
        # Load a previously saved game state
        print("Loading the game...")

    def update_game_state(self):
        # Update the game state based on player actions or events
        print("Updating game state...")

    def display_game_info(self):
        # Display information about the current game state
        print("Displaying game info...")

    def handle_player_input(self):
        # Handle player input and execute corresponding game actions
        print("Handling player input...")

    def generate_random_event(self):
        # Generate random events or encounters within the game
        print("Generating random event...")

class Character(Game):
    def __init__(self, name, health, attack_power, defense):
        super().__init__()
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

class Room(Game):
    def __init__(self, description, dragon=None, choices=None, gain=None):
        super().__init__()
        self.game_instance = None
        self.description = description
        self.dragon = dragon
        self.choices = choices or []
        self.gain = gain or {}
        
    def explore_room(self):
        print("You explore the room.")
        self.game_instance.start_game()

    def save_game(self):
        print("Save the game for later.")
        self.game_instance.save_game()

# Generate random dragons
def generate_random_dragon():
    name = random.choice(["Fire Dragon", "Venomous Dragon", "Ice Dragon", "Electric Dragon", "Rock Dragon", "Puffy "
                                                                                                        "Pooph",
                          "The Last Witness"])
    health = random.randint(150, 250)
    attack_power = random.randint(20, 40)
    defense = random.randint(10, 30)
    magic = random.randint(0, 50)
    poison = random.randint(0, 50)
    return Dragon(name, health, attack_power, defense, magic=magic, poison=poison)

# Generate random choices
def generate_random_choices():
    print("1. Explore the Room")
    print("2. Save the Game.")
    choices = ["1. Explore the Room","2. Save the Game." ]
    for _ in range(random.randint(3, 5)):
        choices.append(
            random.choice(["Fight the dragon", "Search for treasure", "Rest and recover", "Continue exploring", "Put "
                                                                                                            "invisible clock"]))
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

# Generate 100 random rooms
rooms = []
for _ in range(100):
    description = "You enter a mysterious room."
    dragon = generate_random_dragon() if random.random() < 0.5 else None
    choices = generate_random_choices() if random.random() < 0.5 else None
    gain = generate_random_gains() if random.random() < 0.3 else None
    rooms.append(Room(description, dragon, choices, gain))

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
        current_room_index += 1
    else:
        print("Congratulations! You have reached the end of the labyrinth!")

# Example usage
player1 = Player("Hero", 100, 300, 1000, gold=5000, inventory=["Sword", "Potion","Magic"])
game = Game()
game.start_game()
play_game(player1, rooms)
game.end_game()
