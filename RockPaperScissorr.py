import random
item_list = ["rock","paper","scissor"]
user_choice = input("enter your move = Rock,Paper,Scissor")
comp_choice = random.choice(item_list)
print(f"User choice ={user_choice},computer choice = {comp_choice}")
if user_choice == comp_choice:
    print("Both chooses same:=Match Tie")
elif user_choice == "Rock":
     if comp_choice == "paper":
          print("Paper covers Rock = computer wins")
     else:
          print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
     if comp_choice == "Scissor":
          print("scissor cuts the paper,computer")
     else:
          print("paper covers rock, you win")

elif user_choice == "Scissors":
     if comp_choice == "Paper":
          print("Scissor cuts paper, you win")

     else:
          print("rock smashes scissor, computer win")