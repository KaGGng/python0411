# DemoDict3.py

a = [1,2,3]
b = a

a[0] = 38
print(a)
print(b)
print(id(a),id(b))

#깊은복사
a =[100,200,300]
b = a[:]
a[0] = 101
print(a)
print(b)
print(id(a),id(b))