"""
Session Prompt: 
Write a Python program that declares a class describing 
your favorite animal. Have the data members of the class 
represent the following physical parameters of the animal: 
length of the arms (float), length of the legs (float), 
number of eyes (int), does it have a tail? (bool), 
is it furry? (bool).

Write an initialization function that sets the values 
of the data members when an instance of the class is created. 

Write a member function of the class to print out and describe 
the data members representing the physical characteristics of 
the animal.
"""


class YourFavoriteAnimal:
    #Initializes each of the necessary variables
    def __init__(self, lenArms, lenLegs, numEyes, hasTail, isFurry):
        self.lenArms = float(lenArms)
        self.lenLegs = float(lenLegs)
        self.numEyes = int(numEyes)
        self.hasTail = hasTail
        self.isFurry = isFurry
        pass

    #Formats the stored information as a nice string whenever it is asked to be a string.
    def __str__(self):
        #Corrects tense of eyes.
        tenseEyes = "eye" if self.numEyes == 1 else "eyes"

        #Corrects tense of length of arms
        tenseArms = f"Their arms are {self.lenArms} foot long." if self.numEyes == 1 else f"Their arms are {self.lenArms} feet long."

        #Corrects tense of length of feet
        tenseLegs = f"Their legs are {self.lenLegs} foot long." if self.numEyes == 1 else f"Their legs are {self.lenLegs} feet long."

        #Chooses correct description if has a tail or not
        describeTail = "They have a tail." if self.hasTail == True else "They don't have a tail."

        #chooses correct description if is furry or not
        describeFurry = "They are furry." if self.isFurry == True else "They aren't furry."
        
        #Assembles all 5 descriptions nicely
        formattedDescription = f"""
The following describes your favorite animal:
{tenseArms} {tenseLegs}
They have {self.numEyes} {tenseEyes}. {describeTail} {describeFurry}
"""
        #Returns the whole description.
        return formattedDescription

def main():
    
    #Below is a guessing game where the computer chooses an animal and describes it.
    #The player must enter the correct animal before the program ends.
    #It was created for the purpose of testing the class and class functions above.
    import random as r

    animals = {
               "dog": YourFavoriteAnimal(1.0, 1.0, 2, True, True), 
               "snake": YourFavoriteAnimal(0, 0, 2, True, False), 
               "bear": YourFavoriteAnimal(3.0, 3.0, 2, False, True)
               }
    animalList = ["dog", "snake", "bear"]
    animal = animalList[r.randint(0,2)]

    while True:
        print(animals[animal])
        answer = input("Guess your favorite animal:")
        if answer.strip().lower() == animal:
            break
        else:
            print("incorrect...")
    print('Correct!')

if __name__=="__main__":
    main()