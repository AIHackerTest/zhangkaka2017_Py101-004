# !/usr/bin/env python3

from sys import argv
from os.path import exists # exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

open(to_file, 'w').write(open(from_file).read()) # 改写成一行

print("Alright, all done.")
