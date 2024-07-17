class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage

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


# Example usage
player1 = Player("Hero", 100, 20, 10, gold=50, inventory=["Sword", "Potion"])
dragon1 = Dragon("Fire Dragon", 200, 30, 20, magic=40, poison=10)


def attack_now(attacker, target, domain):
    attacker.attack(target, domain)


attack_now(player1, dragon1, "attack_power")  # Player attacks Dragon with attack power
attack_now(dragon1, player1, "magic")  # Dragon attacks Player with magic
