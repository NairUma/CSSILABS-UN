def plurali():
    user_sat = True
    while user_sat == True:
        try:
            user_number = int(raw_input("Int: "))
            user_word = raw_input("Word: ")
            if user_number == 1:
                print(str(user_number) + " " + user_word)

            elif user_word[-2:] == "sh" or user_word[-2:] == "ch":
                print(str(user_number) + " " + user_word + "es")

            elif user_word[-2:] == "us":
                print(str(user_number) + " " + user_word[:-2] + "i")

            elif user_word[-2:] == "ay" or user_word[-2:] == "oy":
                print(str(user_number) + " " + user_word[:-1] + "s")

            elif user_word[-2:] == "ey" or user_word[-2:] == "uy":
                print(str(user_number) + " " + user_word[:-1] + "s")

            elif user_word[-1] == "y":
                print(str(user_number) + " " + user_word[:-1] + "ies")

            elif user_word[-3:] == "ife":
                print(str(user_number) + " " + user_word[:-3] + "ives")

            else:
                print(str(user_number) + " " + user_word + "s")
                
            user_dat = raw_input("Type 'Y' to try again: ")
            if user_dat == "Y":
                user_sat = True
            else:
                user_sat = False
        except ValueError:
            print("Please enter a number!")
plurali()
