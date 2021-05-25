import random ### Here you must define random for use. Otherwise, python3 will return as "radiant" not defined
player = input("Player, choose your dance: ").lower()
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "bolero"
elif rand_num == 1:
    computer = "hustle"
else:
    computer = "samba"
                         
print(f"Computer chooses {computer}" )
if player == computer:
    print("Both instructor and dancer choose same dance!")
elif player == "bolero":
    if computer == "samba":
        print("instructor chooses!")
    else:
        print("dancer chooses!")
elif player == "hustle":
    if computer == "bolero":
        print("instructor chooses!")
    else:
        print("instructor chooses!")
elif player == "samba":
    if computer == "hustle":
        print("instructor chooses!")
    else:
        print("dancer chooses!") 
else:
    print("Please enter a valid dance!")