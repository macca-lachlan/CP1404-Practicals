username = input("Enter your name:")
menu = "display options\nHello (H)\nGoodbye (G)\nQuit (Q)"
print(menu)
user_choice = str(input("Please enter a character: ").upper())
while user_choice != "Q":
    if user_choice == "H":
        print("Hello " + username)
    elif user_choice == "G":
        print("Goodbye " + username)
    else:
        print("invalid choice")
    print(menu)
    user_choice = str(input("Please enter a character: ").upper())
print("finished")
