rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("Welcome to Rock Paper Scissors! Are you ready to play?\n La primera imagen que se muestre en la pantalla será lo que usted ha seleccionado, la segunda imagen será lo que la computadora ha seleccionado, \n Justo después de esto un mensaje le dirá si ha ganado, perdido o empatado :)")

player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if player == "0":
    print(rock)
if player == "1":
    print(paper)
if player == "2":
    print(scissors)
    
list = ["0", "1", "2"]
computer = random.choice(list)
if computer == "0":
    print(rock)
if computer == "1":
    print(paper)
if computer == "2":
    print(scissors)

if player == computer:
    print("Empate!")
    
if player == "0" and computer == "1":
    print("Has perdido :(")
if player == "0" and computer == "2":
    print("Has ganado! :)")
    
if player == "1" and computer == "2":
    print("Has perdido :(")
if player == "1" and computer == "0":
    print("Has ganado! :)")
    
if player == "2" and computer == "0":
    print("Has perdido :(")
if player == "2" and computer == "1":
    print("Has ganado! :)")
