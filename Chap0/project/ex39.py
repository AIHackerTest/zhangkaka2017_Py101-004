cities = {'CS': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}


cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return  themap[state]
    else:
        return "Not found"

while True:
    print("State?(ENTER to quit)")
    state = input(">")
    if not state:
        break

    print(find_city(cities, state))

# 借用了某位同学的作业（很抱歉再回头找是哪位同学时搜了好几遍都找不到了TT），觉得他改的很棒！
