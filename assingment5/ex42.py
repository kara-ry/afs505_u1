## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


## Dog is-a object of animal which is a class
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## cat is-a object of animal which is a class
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a name 
        self.name = name


## The person has-a object self 
class Person(object):

    def __init__(self, name):
        ## self has-a name 
        self.name = name

        # Person has-a pet of some kind 

        self.pet = None

## Employee has-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? Person has-a name and has-a salary
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary


## Fish has-a object 
class Fish(object):
    pass

## Fish is-a class, has-a Salmon object
class Salmon(Fish):
    pass

## Fish is a class, has an object halibut
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## Mary has-a pet satan is-a cat 
mary.pet = satan

## Frank is-a employee has-a salary 120,000
frank = Employee("Frank", 120000)

## frank has-a pet rover is-a dog
frank.pet = rover 

## Flipper is-a fish
flipper = Fish()

## salmon is-a crous 
crouse = Salmon()

## harry is-a Halibout
harry = Halibut()
