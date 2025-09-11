name = "Erdem"
print(type(name))   # <class 'str'>

a = 42
print(type(a))   # <class 'int'>

pi = 3.14
print(type(pi))   # <class 'float'>

z = 2 + 3j
print(type(z))   # <class 'complex'>

numbers = [1, 2, 3, 4]
print(type(numbers))   # <class 'list'>

colors = ("red", "green", "blue")
print(type(colors))   # <class 'tuple'>

r = range(5)   # 0,1,2,3,4
print(list(r)) # [0, 1, 2, 3, 4]
print(type(r)) # <class 'range'>

student = {"ad": "Erdem", "yas": 20}
print(type(student))   # <class 'dict'>

letters = {"a", "b", "c", "a"}
print(letters)        # {'a', 'b', 'c'}
print(type(letters))  # <class 'set'>

fs = frozenset([1, 2, 3, 2])
print(fs)             # frozenset({1, 2, 3})
print(type(fs))       # <class 'frozenset'>

x = True
y = False
print(type(x))   # <class 'bool'>

# Python Veri Tipleri Özet

# 1. str (string)
text = "Merhaba Python"
print("String:", text, "| Tipi:", type(text))

# 2. int (tam sayı)
num_int = 42
print("Integer:", num_int, "| Tipi:", type(num_int))

# 3. float (ondalıklı sayı)
num_float = 3.14
print("Float:", num_float, "| Tipi:", type(num_float))

# 4. complex (karmaşık sayı)
num_complex = 2 + 3j
print("Complex:", num_complex, "| Tipi:", type(num_complex))

# 5. list (liste)
my_list = [1, 2, 3, "python"]
print("List:", my_list, "| Tipi:", type(my_list))

# 6. tuple (demet - değiştirilemez liste)
my_tuple = (10, 20, 30)
print("Tuple:", my_tuple, "| Tipi:", type(my_tuple))

# 7. range (sayı aralığı)
my_range = range(5)
print("Range:", list(my_range), "| Tipi:", type(my_range))

# 8. dict (sözlük)
my_dict = {"ad": "Ali", "yas": 20}
print("Dict:", my_dict, "| Tipi:", type(my_dict))

# 9. set (küme - sırasız, tekrar eden değer yok)
my_set = {1, 2, 3, 3, 4}
print("Set:", my_set, "| Tipi:", type(my_set))

# 10. frozenset (değiştirilemez küme)
my_frozenset = frozenset([1, 2, 2, 3])
print("Frozenset:", my_frozenset, "| Tipi:", type(my_frozenset))

# 11. bool (True/False)
flag = True
print("Bool:", flag, "| Tipi:", type(flag))