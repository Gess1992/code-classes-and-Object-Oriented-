class Animal:
#represente an instance class
    def __init__(self, habitat, diet):
      self.habitat = 'Jungle'
      self.diet = 'meat'

    def speak(self):
        print(f"I live in the {self.habitat} and eat {self.diet}")

animal_1 = Animal() #add a pair of parentheses evoking aclass like an instance 
animal_1.speak()