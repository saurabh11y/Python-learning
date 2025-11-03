class employee:
    a = 1

class programer(employee):
    b = 2

class manager(programer):
    c = 3

o = employee()
print(o.a)

o = programer()
print(o.a,o.b)

o = manager()
print(o.a,o.b,o.c)

