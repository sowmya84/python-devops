import sys

type = sys.argv[1]

if type == "t2.micro":
    print("We will create instance for you")
elif type == "t2.small":
    print("It will charge 2 dollars")
elif type == "t2.medium":
    print("It will charge 4 dollars")
elif type == "t2.large":
    print("It will charge 6 dollars")
else:
    print("Please enter the valid isntance type")    
    