# Hello, world.
name = input("Can I have your name, please? ")
print(name, ", that's a nice name!")
print("--------")
user_age = int(input("May I ask how old are you? "))
print("Got it! You are", user_age, " years old")
member = int(input("Do you have an account number? "))
if member == 5212419:
    print("--------")
    print("Welcome, your excellency!")
else:
    print("You don't have an account number,", name, "but it's alright!")


def main():
    print("--------")
    if user_age < 20:
        print("     ")
        print("You're too young to be an interepreter, ", name)
    elif user_age > 70:
        print("     ")
        print("I admire your spirit,", name, ", but shouldn't you be enjoying your retirement?")
    else:
        language_check()

def language_check():
    print("     ")
    print("Okay, now let's see if you know any foreign languages")
    lanspoken = int(input("How many lanaguages do you speak? (Number only)"))
    if lanspoken == 2:
        second_lan = input("Fantastic, what is your second language?  ")
        print(second_lan, ", right?")
        lan_response = input("(y/n)")
        if lan_response == "y":
            print("Okay, got it!")
            education_check()
        else:
            language_check()
    elif lanspoken >= 3:
        print("Wow!", name, ", that's a lot of languages!")
        print("     ")
        lang_three = input("What are they? ")
        print("They are ", lang_three)
        answer = input("Correct? (n/y)")
        if answer == "y":
            print("Good! Let's continue.")
        education_check()

def education_check ():
    print("--------")
    print("Now, let's talk about your education")
    print("     ")
    print("1. Undergraduate Degree")
    print("2. Master's Degree")
    print("3. PhD")
    print("4. No degrees")
    edu_level = int(input("What are your education level?"))
    if edu_level == 4:
        print("--------")
        print("Unfortunately,", name)
        print("Interpreters are recommended to have a undergraduate degree or above.")
    else:
        print("--------")
        results_release()

def results_release():
    print(name, ", looks like you can be a capable interpreter")
    print("Here are the reasons:")
    print("First, you're ", user_age, ", which is a prime age")
    print("Second, you can speak more than one language, don' you, ", name)
    print("Last but not least, you're an educated individual")
    print("Come and join us!")
    print("      ")
    exit()

main()