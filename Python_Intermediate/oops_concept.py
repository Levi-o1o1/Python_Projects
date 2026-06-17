class char:
    def __init__(self, name, health, attack, blood):
        self.name = name
        self.health = health
        self.attack = attack
        self.blood = blood

    def attack_enemy(self):
        print(f'{self.name} attack with power {self.attack} {self.blood}')

war = char('thor', 100 , 50 ,'red')
mage = char('rio',90,30,'blue')
iron = char('iron-man',50,70,'yellow')

war.attack_enemy()
mage.attack_enemy()
iron.attack_enemy()