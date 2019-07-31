# students = ["Alice", "Javi", "Damien"]
# students.append("Delilah")
# print(students)
# students.insert(1, "Zoe")
# print(students)
# students = ["Alice", "Javi", "Damien", "Javi"]
# students.remove("Javi")
# print(students)

# smith_siblings = ["Emily", "Monique", "Giovanni"]
# for name in smith_siblings:
#     print(name + " Smith")

# smith_siblings = ["Emily", "Monique", "Giovanni", "Brianna", "Javi", "Damien", "Alice", "Zoe", "Jay"]
# for index in range(len(smith_siblings)):
#     smith_siblings[index] = smith_siblings[index] + " Smith"
# print(smith_siblings)
# print index

# names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
# for i in range(len(names)):
#     if names[i] == "Jon":
#         names[i] += " Snow"
#     else:
#         names[i] += " Stark"
# print(names)

# superheroes = ["Captain Marvel", "Wonder Woman", "Storm", "Kamala Khan", "Bumblebee", "Jessica Jones"]
# print(superheroes)
# demoted_hero = raw_input("What superhero do you want to eliminate from the top 5?")
# if demoted_hero in superheroes:
#     superheroes.remove(demoted_hero)
#     print("Top 5 Heroes: ", superheroes)
# else:
#     print("Hero not found.")

# names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
# print(names[::-1])
# print(names[4:2:-1])

state = ["California", "Texas", "New York", "Michgan"]
abbr = ["CA", "TX", "NY", "MI"]
for index in range(len(state)):
    print(abbr[index] + " stands for " + state[index])
