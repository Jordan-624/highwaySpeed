# Print instructions for user.

print("Welcome to the highway travel advisor.")
print("This applicaiton has been configured to work")
print("with travel on I-15 within the State of Utah.")
print("We'll ask for a few pieces of information,")
print("then give you advice on your travel.")
print("")

# Grab input from the user.

mile1 = input("You entered I-15 at what mile marker? ")
mile2 = input("At what mile market on I-15 will you exit? ")
hours = input("How many hours from now do you want to arrive? ")
speed = input("Expected average speed in MPH? ")
print("")

# Calculations

new_mile = abs(float(mile2)-float(mile1))
time = float(new_mile) / float(speed)
new_time = float(hours) - float(time)

# If & Output.
    
if float(speed) > float(80):
    print("Your speed is dangerously high. SLOW DOWN!")
    print("Thank you for using the highway travel advisor.")
elif float(speed) < float(60):
    print("Your speed is WAY too slow. You'll be a hindrance to other traffic.")
    print("Thank you for using the highway travel advisor.")
elif new_time > 0:
    print("You will travel:", int(new_mile), "miles.")
    print("Leave in the next", new_time, "hours to arrive on time.")
    print("Thank you for using the highway travel advisor.")
elif new_time < 0:
    change_time = abs(new_time)
    print("You won't be able to get there on time. You'll be", change_time, "hours late.")
    print("Thank you for using the highway travel advisor.")