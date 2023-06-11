# las tuplas son inmutables - ordenadas - solo lectura

t1 = (1, 3, 5, 7)
t2 = 3, 10, 6, 5, 8
t3 = tuple([2, 4, 5])
t4 = tuple(()) # esto no sirve

print(type(t1))
print(type(t2))
print(type(t3))

l1 = list(t3)

print(type(l1))

