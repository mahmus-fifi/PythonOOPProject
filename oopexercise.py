"""
python oop example project 
written by Mahmud Shuaib 
september 11th 2023 
8:08 pm 
"""
# program to test python ojects 
class Dinosaur(object):
    """mimi is my baby dinosaur, ROAR!"""
    def __init__(self, roar_power_func):
        self.roar_power_func = roar_power_func
class Attack:
    def bite(self):
        print('mimi zombie bites')

    def smack(self):
        print('mimi zombie bites')

    def smash(self):
        print('mimi zombie bites')

    def eat(self):
        print('mimi zombie bites')

# create the objects of the dinosaur class 
attacks = Attack()
dinosaur = Dinosaur(roar_power_func= attacks.smack)
dinosaur.roar_power_func()


