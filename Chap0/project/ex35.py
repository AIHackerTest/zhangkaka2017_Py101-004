# !/usr/bin/env python3
from sys import exit

def gold_room():
    print("-"*40) #分割线==
    print("Welcome to the gold room.")
    print("This room is full of gold. How much do you take?")
    next = input("> ")

    while not next.isdigit():
        print("Please give me a number.")
        next = input("> ")
        #控制输入必为数字

    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("-"*40)
    print("There is a bear here.\nThe bear has a bunch of honey.")
    print("The fat bear is in front of another door.\nHow are you going to move it?")
    #为了少打个print，做个试验，不提倡，因为。。不美观。。。
    bear_moved = False
    print("1.take honey.")
    print("2.taunt bear.")
    print("3.open door.")
    # 容易写==
    
    while True:
        next = input("> ")
        if next == "1":
            dead("The bear looks at you then slaps your face off.")
        elif next == "2" and not bear_moved:
            print("The bear has moved from the door.  You can go through it now.")
            bear_moved = True
        elif next == "2" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "3" and not bear_moved:
            print("Ahh, That's impossible.")
        elif next == "3" and bear_moved:
            gold_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("-"*40)
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    else:
        dead("Anyway dead.")

start()
