
# print("Hello world!")
# print("Bye world!")

# num1 = int(raw_input("Enter Number 1: "))
# num2 = int(raw_input("Enter Number 2: "))
# total = num1 + num2;
# print("The sum total is " + str(total))

# num = int(raw_input("Enter a number: "))
# if num > 0:
#     print("That's a positive number!")
# elif num < 0:
#     print("That's a negative number!")
# else:
#     print("Zero is neither a positive nor negative.")

# string = "hello there"
# for letter in string:
#     print(letter.upper())
# for i in range(5):
#     print(i)
#
# x = 1
# while x <= 5:
#     print(x)
#     x = x + 1

# my_name = "Uma"
# friend1 = "Aspen"
# friend2 = "Cole"
# friend3 = "Liv"
# print(
#     "My name is %s and my friends are %s, %s, and %s" %
#     (my_name, friend1, friend2, friend3)
# )
#
# name = "Marina"
# age = 19
# print("My name is " + name + " and I'm " + str(age) + " years old.")
# print("My name is %s and I'm %s years old." % (name, age))

def greetAgent(first_name, last_name):
    print("%s. %s %s." % (last_name, first_name, last_name))
greetAgent("John", "Smith")

def createAgentGreeting(first_name, last_name):
    return "%s. %s %s." % (last_name, first_name, last_name)
print(createAgentGreeting("Uma", "Nair"))
