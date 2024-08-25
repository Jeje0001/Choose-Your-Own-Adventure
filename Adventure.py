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
    ans= input("You come to a bridge do you want cross it or head back ? Enter either cross or back")
    if ans == "back":
        print("You go back  and lose")
    elif ans == "cross":
        ans=input("You crossed the bridge and met a stranger Do you talk to them Enter either yes or no")
        if ans == "yes":
            print("You talked to the stranger and they gave you gold Congratulations you won")


        elif ans == "no":
            print("you ignored the stranger and they are offended and you lose")
        
        else:
            print("Not a valid option you lose")



else:
    print("Not a valid option you lose")

print("Take you for trying " + name)