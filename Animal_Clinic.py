# m03 Tutorial - Functional vs OOP Programming
# author: Xander Jewell
# created: 2022-02-01
# Creating a program to simulate an animal clinic

# Creating the main class called Pet
class Pet():
    def __init__(self, petType, name, age, weight, color, isVaccinated, note):
        self.petType = petType
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.isVaccinated = isVaccinated
        self.note = note

class Dog(Pet):
    # Setting Vaccination to No and petType to Dog
    def __init__(self, name, age, weight, color, note, isNeutured, isCute, 
                isVaccinated = "No", petType = "Dog"):
        # Setting Attributes specifically for this class
        self.isNeutred = isNeutured
        self.isCute = isCute
        # Initializing the Parent Class
        super().__init__(petType, name, age, weight, color, isVaccinated, note)
        
    # Printing the details of the dog
    def show_dogdetails(self):
        print(f"\nPet Type: {self.petType}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight (lbs): {self.weight}")
        print(f"Color: {self.color}")
        print(f"Vaccination Status: {self.isVaccinated}")
        print(f"Note: {self.note} ")
        print(f"Cute or Not: {self.isCute}")
        print(f"Is he neutured? : {self.isNeutred}")
    
class Cat(Pet):
    # Setting Vaccination to No and petType to Cat
    def __init__(self, name, age, weight, color, note, istheDevil, 
                isVaccinated = "No", petType = "Cat"):
        # Setting attrributes specifically for this class
        self.istheDevil = istheDevil
        # Initializing the Parent Class
        super().__init__(petType, name, age, weight, color, isVaccinated, note)

    # Showing the Details of the Cat
    def show_catdetails(self):
        print(f"\nPet Type: {self.petType}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight (lbs): {self.weight}")
        print(f"Color: {self.color}")
        print(f"Vaccination Status: {self.isVaccinated}")
        print(f"Note: {self.note} ")
        print(f"Is it the Devil?: {self.istheDevil}")

# Creating the Animals for the Shelter
Dog1 = Dog("Bubba", "15", "100", "Brown","A very cute chocolate lab.", "Yes", "Yes")
Dog1.show_dogdetails()

Cat1 = Cat("Deborah", "11", "220", "Orange", "She stinks so much.", "YES")
Cat1.show_catdetails()

Dog2 = Dog("Gomer", "12", "150", "Chocolate", "He is an amazing listener.", 
            "Yes", "Yes")
Dog2.show_dogdetails()

Cat2 = Cat("Felicia", "5", "45", "White", "She can be a drama queen.", "No")
Cat2.show_catdetails()

Dog3 = Dog("Tim", "2", "54", "Golden", "He is a great hunter dog.", "No", "Yes")
Dog3.show_dogdetails()

Cat3 = Cat("Beth", "10", "225", "Black", "The literal devil.", "YES")
Cat3.show_catdetails()