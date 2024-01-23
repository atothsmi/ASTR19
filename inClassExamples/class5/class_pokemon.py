#define a class of a type of pokemon
#aech element of the class is an instance

class Pokemon:
    max_hp = 50

    #initialize instance variables
    def __init__(self, name="Missingo", moveset=[], current_hp=max_hp):
        self.name = name                #creates attributes belonging
        self.moveset = moveset          #to each instance of the class
        self.current_hp = current_hp    #runs whenever a new instance is created
        
        if current_hp > 0:
            self.fainted = False
        else:
            self.fainted = True
    
    #functions applied to instances are called methods
    #make pokemon talk
    def talk(self):
        print(f"{self.name}!")
        print()

    def damage(self, damage):
        print(f"{self.name} is taking damage!")
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.current_hp = 0
            print(f"{self.name} fainted!")

    def heal(self, heal):
        if heal + self.current_hp > self.max_hp:
            print(f"{self.name} healed {self.max_hp - self.current_hp} hp!")
            self.current_hp = self.max_hp
        else:
            print(f"{self.name} healed {heal} hp!")
            self.current_hp += heal
            
    def potion(self):
        print(f"Trainer used a potion.")
        self.heal(20)

    def learn(self, new_move):
        print(f"{self.name} is attempting to learn {new_move}.")

        if len(self.moveset) == 4:
            print(f"but {self.name} already knows 4 moves!")
            print(f"{self.name} did not learn {new_move}.")
            

        else:
            self.moveset.append(new_move)
            print(f"{self.name} learned {new_move}!")
        

         
        
        