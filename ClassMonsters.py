

import random
import inspect

class Dragon :
    def __init__(self,name, health,  attack_power, defense,  magic = 0,poison = 0, wealth = 0 ,armorshield = 0, weapon = 0, tools= 0,
                 tradegoods = 0, fire = 0, freeze = 0, healing = 0, damage = 0, spells= 0):
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







    def mag(self):
        self.magic = True
        print("I have magic!")

    def pois(self):
        self.poison = True
        print("I have poison!")

    def wealt(self):
        self.wealth = True
        print("I have wealth")

    def spel(self, **spells):
        print("The spells are " , spells )

    def Wealt(self, delt_value):
        value  = 100 + delt_value
        return value

    def attack(self, target):
        damage = self.attack_power - target.defense
        if damage > 0:
            target.health -= damage
            print(f"{self.name} attacks {target.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack is ineffective against {target.name}!")

    import inspect



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
        else:
            print(f"{attacker.name}'s attack is ineffective against {target.name} in {domain} domain.")

    # Example usage


    #


    # Example usage
'''
def get_class_arguments(Dragon):
    signature = inspect.signature(Dragon.__init__)
    return list(signature.parameters.keys())[1:] # exclude self
def get_argument_value(instance, argument):
    if hasattr(instance, argument):
        return getattr(instance, argument)
    return None
def attacm_now(attcker, target,  x):
    domain = get_class_arguments(Dragon)[x]
    damage = get_argument_value(attcker,domain)- get_argument_value(target,domain)
    target.domain -= damage
    if damage > 0:
        print(f"{attcker}attacks {target.name} for {attcker.domanin} ")
    else:
        print(f"{attcker.name} cannot heal {target.name}!")
'''
herro = Dragon("Jessy",100, 100, 100, 80, 90, 25, 15, 0, 0, 10000, 1000)
Magic_l = ["invisible","drain life" , "protection", "wisdom"]



d2 = Dragon("Colombre",20,20,20,)
d2.mag()

if bool(d2.magic):

    ma = random.randint( 0, 3)
    print(ma)
    print(Magic_l[ma])
    print("I have magic ", Magic_l[ma])

if bool(d2.pois()):
    print("The poison is bad for you")
else :
    print("No poison baby!")

print(d2)
print(bool(d2.mag()))

print(d2.spel(spell1 = "Tardy", spell2 = "In time"))


print(d2.damage)

if herro.wealth == True and d2.wealth == False:
    print((herro.Wealt(20)))
elif herro.wealth == False and d2.wealth == False:
    print(herro.Wealt(0))
else:
    print( "Herro ", herro.Wealt(-20))
    print("Dragon ", d2.Wealt(20))

dragon1 = Dragon("Fire Dragon", 200, 30, 20, fire=40, freeze=20, healing=15)
dragon2 = Dragon("Ice Dragon", 180, 25, 25, fire=20, freeze=40, damage=25)

Dragon.attack_now(dragon1, dragon2, 4)  # Attack using 'fire' domain
Dragon.attack_now(dragon2, dragon1, 5)  # Attack using 'freeze' domain