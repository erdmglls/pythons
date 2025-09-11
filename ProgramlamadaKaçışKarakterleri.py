#escape characters

text="Python\nis\ndoing\nwell"#\n karakteri
print(text)

text="Hello\rPy"#\r karakteri
print(text)

text="Hello\tPython"#\t bir tab boşluk bırakır
print(text)

text="Hello\bPython"#\b bir önceki karakteri siler ve üzerine yazar
print(text)

text="\120\171\164\150\157\156"#octal sayılar
print(text)

text="\x50\x79\x74\x68\x6F\x6E"#hexadecimal
print(text)