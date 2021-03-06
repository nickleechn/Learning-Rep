# Hello, world.

print("Welcome!")
first_name = input("What's your first name?")
last_name = input("What's your last name?")
full_name = f"{first_name} {last_name}"
greeting = f"Hello, {full_name.title()}, it is nice to meet you!"
print(greeting) #This part greets the user and engage them in the program

print("--------") #Checks the age of the user and eliminate those who do not fit in the range
user_age = int(input("May I ask how old are you? "))
print("- Got it! You are", user_age, " years old")
member = int(input("Do you have an account number? \nIf you don't, please type any number."))
if member == 5212419:
    print("--------")
    print("- Confirmed. You're logged in as a member.")
else:
    print(f"- It looks like you are not registered, {first_name.title()}, but it's alright")

def main():
    print("--------")
    if user_age < 20:
        print("     ")
        print()
        print(f"- You're a bit young to be an interpreter, {first_name.title()}, aren't you?")
    elif user_age > 70:
        print("     ")
        print("- I admire your spirit,", first_name, ", but shouldn't you be enjoying your retirement?")
    else:
        language_check()

def language_check(): #Check if a user speaks more than one language
    print("     ")
    print("- Okay, now let's see if you know any foreign languages")
    lanspoken = int(input("How many lanaguages do you speak? (Number only)"))
    if lanspoken == 2:
        second_lan = input("- Fantastic, what is your second language?  ")
        add_lan = []
        add_lan.append(second_lan)
        print(f"You speak {add_lan[0]}, correct?")
        lan_response = input("(y/n)")
        if lan_response == "y":
            print("- Okay, got it!")
            education_check()
        else:
            language_check()
    elif lanspoken >= 3:
        print(f"- Wow!, {first_name.title()}, that's a lot of languages!")
        print()
        duolingo_list = []
        first_lan = input("What's your second language?") #Ask user of their second language
        duolingo_list.append(first_lan) #Add it to the list
        two_lan = input("What's your third language?") #same
        duolingo_list.append(two_lan)
        print(f"- You speak: {duolingo_list[0].title()} and {duolingo_list[1].title()}.")
        answer = input("Correct? (n/y)")
        if answer == "y":
            print("- Good! Let's continue.")
            education_check()
        else:
            re_attempt = input("- Would you like to start over? (y/n) ")
            if re_attempt == "y":
                main()
            else:
                print("- Thank you for using this program. Goodbye.")
                exit()

def education_check (): #Check if user holds a degree
    print("--------")
    print("Now, let's talk about your education")
    print("     ")
    print("1. Undergraduate Degree \n2. Master's Degree \n3. PhD \n4. No Degrees")
    edu_level = int(input("What are your education level?"))
    if edu_level == 4:
        print("--------")
        print("- Unfortunately,", first_name)
        print("Interpreters are recommended to have a undergraduate degree or above.")
        re_attempt = input("- \tWould you like to start over? (y/n) ")
        if re_attempt == "y":
            main()
        else:
            print("- Thank you for using this program. Goodbye.")
            exit()
    else:
        print("--------")
        results_release()

def results_release(): #Inform user of the result
    print(f"{first_name.title()}, you can be a capable interpreter!\nHere are the reasons:\n\tFirst, you are {user_age}, which is a prime age. \n\tSecond, you can speak more than one language, don't you, {first_name.title()}? \n\tLast but not least, you're an educated individual. \n\tCome and join us!")
    exit()

main()