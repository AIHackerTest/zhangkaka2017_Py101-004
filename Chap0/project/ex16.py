# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from sys import argv
script, filename = argv
print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?") # input

print("Opening the file...")
target = open(filename, 'w') # truncate部分省略

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n') # 三行合成一行

print("And finally, we close it.")
target.close()
