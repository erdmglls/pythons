#count belirli bir stringin kaç kere geçtiğini yazar
text="python is so easy.My homework is so easy"
result=text.count("easy")
print(result)

text="Phthon is so easy.My homework is so easy" 
result=text.count("easy",11,19)
print(result)
#bir indeks belirterek hangi değerler arasında aranacağını belirleyebilriz

#starswith metodu
#String’in belirtilen değerle başlayıp başlamadığını True/False döndürür.
text="Welcome to my world.My world is python"
result=text.startswith("to")
print(result)
#bunu da indeksle sınırlandırabiliriz bu sefer true dönecektir
text="Welcome to my world.My world is python"
result=text.startswith("to",8,12)
print(result)

#endswith metodu
#String’in belirtilen değerle bitip bitmediğini True/False döndürür.
text="Welcome to my world.My world is python"
result=text.endswith("on")
print(result)#gene burada da indeks belirtebiliriz

#expandtabs metodu
#verilen değere göre ifadeler arasında boşluk bırakır bunuda \t kullanarak yaparız
#değer vermezsen 1 tab boşluk bırakır = 8
text="p\ty\tt\th\to\tn"
print(text)
print(text.expandtabs(2))
print(text.expandtabs(4))
print(text.expandtabs(6))

#find string metodu
#stringte belirtilen değeri arar ve ilk bulduğu andaki indeks değerini döndürür
#bulamazsa -1 döndürür
text="Phthon is so easy.My homework is so easy" 
result=text.find("h")#burada da index belirterek aralıkta bakabilirsin
print(result)
# sıfırdan saymaya başladığımızı unutma

#index metodu
#find() gibidir, ama bulamazsa hata (ValueError) verir
text="Python is so good"
result=text.index("is")
print(result)

#isalnum metodu
#String sadece alfanümerik (harf + rakam) içeriyorsa True.
print("Python3".isalnum())  # True
print("Python 3".isalnum()) # False (boşluk var)

#isalpha metodu
#String sadece harflerden oluşuyorsa True.
print("Python".isalpha())  # True
print("Python3".isalpha()) # False

#isascii metodu
#Tüm karakterler ASCII tablosunda ise True.
print("Python".isascii())  # True
print("ö".isascii())       # False

#isdecimal()
#String sadece ondalık rakamlardan oluşuyorsa True.
print("123".isdecimal())   # True
print("½".isdecimal())     # False
