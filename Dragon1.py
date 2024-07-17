import inspect

class Dragon:
    def __init__(self, name, health, attack_power, defense, magic=0, poison=0, wealth=0, armorshield=0, weapon=0, tools=0,
                 tradegoods=0, fire=0, freeze=0, healing=0, damage=0, spells=0):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.magic = magic
        self.poison = poison
        self.wealth = wealth
        self.armorshield = armorshield
        self.weapon = weapon
        self.tools = tools
        self.tradegoods = tradegoods
        self.fire = fire
        self.freeze = freeze
        self.healing = healing
        self.damage = damage
        self.spells = spells

def get_class_arguments(Dragon):
    signature = inspect.signature(Dragon.__init__)
    return list(signature.parameters.keys())[1:]  # exclude self

def get_argument_value(instance, argument):
    if hasattr(instance, argument):
        return getattr(instance, argument)
    return None

def attack_now(attacker, target, x):
    domain = get_class_arguments(Dragon)[x]
    damage = get_argument_value(attacker, domain) - get_argument_value(target, domain)
    setattr(target, domain, getattr(target, domain) - damage)
    if damage > 0:
        print(f"{attacker.name} attacks {target.name} for {damage} damage in {domain} domain.")
        print(f"{attacker.name} has now {getattr(attacker, domain)}")
        print(f"{target.name} got  {target.name} 's damage of {damage} in {domain} domain")
        print(f"{target.name} has now {getattr(target, domain)}")
    else:
        print(f"{attacker.name}'s attack is ineffective against {target.name} in {domain} domain.")
        print(f"{target.name} has now {getattr(target, domain)}")
        print(f"{attacker.name} has now {getattr(attacker, domain)}")

# Example usage
dragon1 = Dragon("Fire Dragon", 200, 30, 20, fire=40, freeze=20, healing=15)
dragon2 = Dragon("Ice Dragon", 180, 25, 25, fire=20, freeze=40, damage=25)
herro = Dragon('Herro',100,100, 100, 100, 100, 100, 100, 100, 100, 100 , 100, 100, 100 , 100 , 100)
attack_now(dragon1, dragon2, 4)  # Attack using 'fire' domain
attack_now(dragon2, dragon1, 5)  # Attack using 'freeze' domain
attack_now(herro,dragon2,7)
attack_now(dragon2, dragon1, 7)
attack_now(herro, dragon1, 7)
attack_now(dragon2,herro, 1)

