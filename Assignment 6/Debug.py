class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if (self.fur_length == "long"):
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
    def speed(self):
        if (self.model == "bugatti"):
            return("Your car has 1500 horse power")
        else:
            return("Your car sucks.")
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    dog1 = Dog(name = "Joe",age = 4)
    print(dog1.name, dog1.age)
    
    #and what about a new employee
    newEmployee = Employee(name = "Jose", idNumber = 1974, department = "circus")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)
    
    #now create and print out a cake you make
    myCake = Cake(flavor = "Chocolate", frosting = "vanilla")
    print(myCake.flavor, myCake.frosting)
    
    
    #and now create another cake and print it out
    mySecondCake = Cake(flavor = "Red Velvet", frosting = "Cream Cheese Frosting")
    print(mySecondCake.flavor, mySecondCake.frosting)
    
    #create a cat!
    cat1 = Cat(name = "Stella", age = 1, fur_length= "short")
    #create another cat!
    cat2 = Cat(name = "Aurora", age = 2, fur_length="Long")
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    
    #create a car!
    myCar = Car(model = "Toyota Corolla",year= 2007, color = "silver")
    #Now print out the function you made for car :)
    print(myCar.speed())
main()
