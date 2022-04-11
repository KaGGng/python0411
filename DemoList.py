# DemoList.py


from gc import collect
from turtle import color


colors = ["red","blue","green"]

print(len(colors))
print(colors)
print(type(colors))
print(colors[0])

for item in colors:
    print(item)



colors +=["red"]
print(colors)

colors +="red"
print(colors)

print(colors.pop())

colors.remove("red")

colors.extend(["blue","yellow","pink"])
print(colors)

colors.reverse()
print(colors)


tp =(1,2,3)
print(tp)
print(type(tp))
print(len(tp))
print(tp[0])

def calc(a,b):
    return a*b, a*b

print(calc(3,4))
