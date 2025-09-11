x = 10
y = 3.14
z = "Erdem"

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>

a = 5
b = float(a)
print(b)        # 5.0
print(type(b))  # <class 'float'>

c = 3.99
d = int(c)
print(d)        # 3 (ondalıklı kısmı siler)
print(type(d))  # <class 'int'>

x = 10
y = str(x)
print(y)        # '10'
print(type(y))  # <class 'str'>

s1 = "20"
s2 = "3.14"

print(int(s1))   # 20
print(float(s2)) # 3.14

my_list = [1, 2, 3]

# list → tuple
t = tuple(my_list)
print(t)          # (1, 2, 3)
print(type(t))    # <class 'tuple'>

# list → set
s = set(my_list)
print(s)          # {1, 2, 3}
print(type(s))    # <class 'set'>
