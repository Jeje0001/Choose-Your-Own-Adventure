name= input("Type Your Name ? ")
answer= input(name + " Do you want to play the game").lower()

if answer == "yes":
    print("Welcome to the game " + name )
else:
    print("Bye " + name)
    quit()


ans = input("You are on a road it has come to an end you can only go to the left or right which would you like to go ? ").lower()

if ans == "left":
    ans= input("You found yourself close to a river do you want to swim or walk across it ? Type walk to walk or swim to swim ? ")
    if ans == "swim":
        print("You swan across and you were eaten by an alligator")
    elif ans == "walk":
        print("You walked for many miles, ran out of water and died")
    else:
        print("Not a valid option you lose")
elif ans == "right":
    #COntinue at 1:02:06
    print()

else:
    print("Not a valid option you lose")