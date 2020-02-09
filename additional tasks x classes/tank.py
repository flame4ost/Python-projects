import random

class Tank():
    """Описание танка"""
    def __init__(self, model, armor, min_damage, max_damage, health):
        self.model = model
        self.armor = armor
        self.health = health
        self.damage = random.randint(min_damage, max_damage)

    def print_info(self):
        print(self.model + " имеет лобовую броню ", self.armor, " мм при ", self.health, 
              " ед.здоровья и уроне ", self.damage, " ед.")

    def health_down(self, enemy_damage):
        self.health = self.health - enemy_damage


    def armor_down(self):
        if self.armor >= 15:
            self.armor = self.armor - 15
        elif self.armor < 15:
            self.armor = 0



    def shot(self, enemy):
        
        if enemy.health <= 0 or self.damage >= enemy.health:
            enemy.health = 0
            print("Танк ", enemy.model, " уничтожен")
        
        elif self.health == 0:
            return
        
        elif enemy.health > 0 and enemy.armor >= 15:
            enemy.armor_down()
            enemy.health_down(self.damage-30)
            print("Танк ", enemy.model, " получил ", self.damage-30, " урона")
        
        else:
            enemy.health_down(self.damage)
            print("Танк ", enemy.model, " получил ", self.damage, " урона")



tank1 = Tank("Т-34", 100, 50, 200, 1000)
tank2 = Tank("Tiger", 75, 200, 300, 1500)

tank1.print_info()
tank2.print_info()

tank1.shot(tank2)
tank2.shot(tank1)
tank1.shot(tank2)
tank2.shot(tank1)
tank1.shot(tank2)
tank2.shot(tank1)
tank1.shot(tank2)
tank2.shot(tank1)
tank1.shot(tank2)
tank2.shot(tank1)
tank1.shot(tank2)
tank2.shot(tank1)