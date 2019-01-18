#   Nicholas Huntley
#   capacity = function for cap variable
#   cap = how many people allowed in the room
#   attendees = function for ppl variable
#   ppl = amount of people needing to attend
#   register = function for any_more variable
#   any_more = whether or not to check another room
#   error = if people are incapable of giving the program the variable it needs 

def capacity():
    cap = int(input("What is the capacity of the meeting room? "))
    return cap
def attendees():
    ppl= int(input("What is the amount of people that are going? "))
    return ppl
def register():
    limit= cap - ppl
    return abs(limit)
def rooms():
    any_more = input("Would you check another meeting room? (y/n) ")
    any_more = any_more.lower()
    while (any_more!= "y" and any_more != "n"):
       any_more = input("Do you want to check anymore rooms (y/n)? ")
       any_more = any_more.lower()
    return any_more

any_more = "y"
error = 1

while(any_more == "y"):
    cap = capacity()
    ppl = attendees()
    if(ppl > cap):
        limit = register()
        print("Holding a meeting her would be ", limit, " people over the limit.")
        any_more = rooms()
    else:
        print("You are all set to have the meeting in this room. ")
        any_more = rooms()

while(any_more !="y" and any_more !="n"):
    any_more = input("Only enter a lower case letter y or n. ")
    any_more = any_more.lower
    error = error + 1

    if(error == 3):
        any_more = "n"
        print("Read the directions more clearly next time.")

print("Have a nice meeting!")
