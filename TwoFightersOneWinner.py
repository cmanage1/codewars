#Create a function that returns the name of the winner in a fight between two fighters.
#Each fighter takes turns attacking the other and whoever kills the other first is victorious. 
#Death is defined as having health <= 0.
#EXAMPLE
#class Fighter(object):
#    def __init__(self, name, health, damage_per_attack):
#        self.name = name
#        self.health = health
#        self.damage_per_attack = damage_per_attack
#
#    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
#    __repr__=__str__


def declare_winner(fighter1, fighter2, first_attacker):
      while fighter1.health > 0 and fighter2.health > 0:
          if fighter2.name == first_attacker:
              fighter1.health-= fighter2.damage_per_attack
              if fighter1.health > 0:
                  fighter2.health-= fighter1.damage_per_attack
          else:
              fighter2.health-= fighter1.damage_per_attack
              if fighter2.health > 0:
                  fighter1.health-= fighter2.damage_per_attack
              
      return fighter2.name if (fighter1.health < fighter2.health) is True else fighter1.name
