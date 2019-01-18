#Nicholas Huntley
#maximum = maximum allowed amount of people
#people = amount of people attending
#capreach = whether or not max capacity is reached 

any_more_data = "y"

while(any_more_data == "y"):
    maximum = int(input("What is the maximun alowed number of people? "))
    people = int(input("How many people are atteneding? "))
    capreach = maximum - people
    
    if (capreach < 0):
        capreach = capreach * -1
        print("You are ", capreach, " person(s) over the limit. If these people attend it will be  illegal.")
        any_more_data = input("Would you like to check another room? (y/n) ").lower()
        while(any_more_data !="y" and any_more_data !="n"):
            any_more_data = input("You must enter a y or n. ").lower()

    elif (capreach >= 0):
        capreach2 = maximum - people 
        print("You are all set to use this room for a meeting and can have ", capreach2, " more person(s) attend.")
        any_more_data = input("Would you like to check another room? (y/n) ").lower()
        while(any_more_data !="y" and any_more_data !="n"):
            any_more_data = input("You must enter a y or n. ").lower()

print("Have a nice meeting!")
