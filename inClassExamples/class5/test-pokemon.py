from class_pokemon import Pokemon

#main program to test pokemon class
def main():

    #creating a new instance of pokemon
    #ommitted parameters take default values
    my_togepi = Pokemon("Togepi", ["Metronome"], 40)

    #access individual variables of the instance
    print(my_togepi.name)
    print(my_togepi.moveset)
    print(my_togepi.current_hp)
    print(my_togepi.max_hp)

    #use methods of the class pokemon
    my_togepi.talk()

    #take some damage
    print(my_togepi.current_hp)
    my_togepi.damage(25)
    print(my_togepi.current_hp)
    pass
    print()

    #take a potion
    my_togepi.potion()
    print(my_togepi.current_hp)

    #learn a new move
    my_togepi.learn("Growl")
    print(my_togepi.moveset)
    my_togepi.learn("Yawn")
    print(my_togepi.moveset)
    my_togepi.learn("Wish")
    print(my_togepi.moveset)
    my_togepi.learn("Tackle")
    print(my_togepi.moveset)

if __name__ == "__main__":
    main()