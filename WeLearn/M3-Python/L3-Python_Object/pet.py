# class Pet(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# my_pet = Pet("Fido", 3)
# print("My pet is %s is %s years old" % (my_pet.name, my_pet.age))
# my_pet2 = Pet("Vel", 6)
# print("My pet is %s is %s years old" % (my_pet2.name, my_pet2.age))
# my_pet3 = Pet("Seven", 2)
# print("My pet is %s is %s years old" % (my_pet3.name, my_pet3.age))
# class Student(object):
#     def __init__(self, major, year):
#         self.major = major
#         self.year = year
# freshman = Student("Computer Science", "Freshman")
# print("I am a %s in %s" % (freshman.year, freshman.major))
# sophomore = Student("Political Science", "Sophomore")
# print("I am a %s in %s" % (sophomore.year, sophomore.major))
# junior = Student("Civil Engineering", "Junior")
# print("I am a %s in %s" % (junior.year, junior.major))
# senior = Student("Biology", "Senior")
# print("I am a %s in %s" % (senior.year, senior.major))

class Pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "happy"

    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood = "lethargic"
    def move(self):
        print("> %s wants to play!" % self.name)
        if self.mood != "happy":
            self.mood = "happy"
            print("> %s is having a great time!" % self.name)
            self.is_hungry = True
        else:
            print("> %s is getting worn out!" % self.name)
            self.mood = "tired"
            self.is_hungry = True
the_pet = Pet("Kit", 4, "Cat")
# the_pet.eat()
# print("Is my pet hungry? %s" % the_pet.is_hungry)
# print("My pet's feelings: %s" % the_pet.mood)
the_pet.move()
