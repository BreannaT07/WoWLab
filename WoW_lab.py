#Defining the Base Class
    #Creating the Character Class
class Character:
  def __init__(self, name, race, level=1):
    self.name = name
    self.race = race
    self.__level = level
    
#Encapsulation
  #Iplementing Encapsulation
    #Adding a methond to display the character info
  def level_up(self):
    self.__level += 1\

  def special_ability(self):
    print("This character has no special abilities.")

  def show_info(self):
    print(f"Name: {self.name}\nRace: {self.race}\nLevel: {self.__level}")
    
#Inheritance and Specialization
    #Creating Specialized Classes
#Polymorphism 
  #Demostrating Polymorphism
class Pladin(Character): 
    def __init__(self, name, race, weapon):
        super().__init__(name, race)
        self.weapon = weapon
      
    def special_ability(self):
      print(f"{self.name} swings their {self.weapon} mightily!")
      
class Divine(Character):
    def __init__(self, name, race, magic_type):
        super().__init__(name, race)
        self.magic_type = magic_type
      
    def special_ability(self):
      print(f"{self.name} casts a powerful {self.magic_type} spell!")

#Creating the Characters
    #Creating the characters instances and interaction with them
arthas = Pladin("Arthas Menethil", "Pladin", "Sword")
velen = Divine("Velen", "Draenei", "Frost")

arthas.show_info()
arthas.special_ability()

velen.show_info()
velen.special_ability()
velen.level_up()
velen.show_info()
