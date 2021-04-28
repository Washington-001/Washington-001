#!/usr/bin/python2.7
"""Blank Python 2.7 file"""
maxhp = int(50)
hp = int(50)
import random
import time
print ("welcome to Ryder's house of monstrositys!!!")
time.sleep (2)
print ("can you escape?")
time.sleep (1)
difficulty = input ('what difficulty would you like, easy normal or hard?')
print ("... preparing dungeon ...")
time.sleep (2) 
print (".") 
time.sleep (0.5) 
print (".") 
time.sleep (0.5) 
print (".") 
time.sleep (0.5) 
if difficulty == " easy":
     print ('first encounter: Beatle!')
     encounter = "Beatle"
elif difficulty == "easy":
   print ('first encounter: Beatle!')
   encounter = "Beatle"
elif difficulty == " normal":
    print ("first encounter: Goblin!")
    encounter = "Goblin"
elif difficulty == "normal":
    print ("first encounter: Goblin!")
    encounter = "Goblin"
elif difficulty == " hard":
    print ("first encounter: Kobold ")
    encounter = "Kobold"
elif difficulty == "hard":
    print ("first encounter: Kobold ")
    encounter = "Kobold"
else:
    print ("ERROR INVALID DIFFICULTY BEEP BOOP BOOM")
    exit ()
if difficulty == "easy":
    enemyhp = int(20)
elif difficulty == ' easy':
    enemyhp = int(20)
elif difficulty == "normal":
    enemyhp = int(50)
elif difficulty == " normal":
    enemyhp = int(50)
elif difficulty == 'hard':
    enemyhp = int(100)
elif difficulty == " hard":
    enemyhp = int(100)
choice = input ("Run or Fight?")
if choice == " run":
    print ("GAME OVER!") 
    exit ()
elif choice == "run":
    print ("GAME OVER!") 
    exit ()
elif choice == (" fight"):
    print ("Battle Begin!") 
elif choice == ("fight"):
  print ("Battle Begin!") 
hit = int(7)
inventory = "empty"
print ("Your Turn!")
Action = input("what would you like to do: attack, magic, inventory, or retreat")
if Action == "attack":
    Action = input("here are your weapons: Basic sword, and Basic bow")
    if Action == "basic sword":
        Action = "Basic Sword"
    elif Action == "Basic sword":
        Action = "Basic Sword"
    elif Action == "Sword":
        Action = "Basic Sword"
    elif Action == "Sword":
        Action = "Basic Sword"
    if Action == "Basic Sword":
        hit = random.randint(1, 4)
        if hit > 1: 
            print ("you slash through the",encounter, "dealing 10 damage!")
    if Action == "Basic Bow":
        hit = random.randit(1, 4)
        if hit > 1:
            print ("you plunge your arrow into the", encounter, "dealing 10 damage")
elif Action == " attack":
    Action = input("here are your weapons: Basic sword, and Basic bow")
    if Action == "Basic Sword":
        hit = random.randint(1, 4)
        if hit > 1: 
            print ("you slash through the",encounter, "dealing 10 damage!")
    elif Action == "Sword":
        hit = random.randint(1, 4)
        if hit > 1:
            print ("you slash through the",encounter, "dealing 10 damage!")
    elif Action == "basic sword":
        hit = random.randint(1, 4)
        if hit > 1: 
            print ("you slash through the",encounter, "dealing 10 damage!")
    elif Action == "sword":
        hit = random.randint(1, 4)
        if hit > 1: 
            print ("you slash through the",encounter, "dealing 10 damage!")
    elif Action == "Basic Bow":
        hit = random.randit(1, 4)
        if hit > 1:
            print ("you plunge your arrow into the", encounter, "dealing 10 damage")
    elif Action == "Bow":
        if Action == "Basic Bow":
            hit = random.randit(1, 4)
            if hit > 1:
                print ("you plunge your arrow into the", encounter, "dealing 10 damage")
    elif Action == "basic bow":
        if Action == "Basic Bow":
            hit = random.randit(1, 4)
            if hit > 1:
                print ("you plunge your arrow into the", encounter, "dealing 10 damage")
    elif Action == "bow":
        if Action == "Basic Bow":
            hit = random.randit(1, 4)
            if hit > 1:
                print ("you plunge your arrow into the", encounter, "dealing 10 damage")
elif Action == "magic":
    choice = input("Your spells are: fire, and heal")
    if choice == " fire":
        choice = "fire"
    if choice == "fire":
        hit = random.randint(1, 5)
        if hit > 1:
            print ("Forming a ball of fire in your hand you hurl it at the", encounter, "dealing 15 damage")
            enemyhp = enemyhp - 15
        else:
            print ("you miss!")
    if choice == " heal":
        choice == "heal"
    if choice == "heal":
        if hp != maxhp:
            heal = random.randint(5, 15)
        else:
            print ("your health is already full")