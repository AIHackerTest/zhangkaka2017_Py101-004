# !\usr\bin\env python3
# -*- coding:utf-8 -*-
from sys import argv
script, file1 = argv

x = open(file1, 'a') # 使用追加模式
x.write('What is color?')
x.close()
