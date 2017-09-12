# !\usr\bin\env python3
# -*- coding:utf-8 -*-

dict = {}
with open("weather_info.txt") as f: # with as的用法，同常规提取文件方法的不同，值得学习
  for line in f:
    (key, val) = line.split(',') # split()
    dict[key]= val

history_list = []
while True:
  code_or_city = input("您输入的指令或者要查询天气的城市是：")

  if  code_or_city in dict.keys():
    weather ='{0}的天气是:{1}'.format(code_or_city,dict[code_or_city])# format()
    print (weather)
    history_list.append(weather)
  elif code_or_city == "help":
    print ('''
      输入城市名，查询该城市的天气；
      输入help，显示帮助文档；
      输入history，显示查询历史；
      输入quit，退出程序；
      ''')
  elif code_or_city == "history":
      print("您的查阅历史记录如下:")
      for item in history_list:
        print(item)
  elif code_or_city == "quit":
      quit() # quit函数
  else:
      print ("您的输入有误，请尝试输入help获得帮助文档")
