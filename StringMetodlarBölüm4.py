#strip metodu
#Bir stringin başında ve sonunda bulunan boşlukları (veya belirtilen karakterleri) siler.
text="    BMW    "
result=text.strip()
print("My favorite",result,"this one.")
#lstrip metodu
#soldaki boşlukları siler
text="    BMW    "
result=text.lstrip()
print("My favorite",result,"this one.")
#rstrip metodu
#sağ kısımda kalan boşlukları siler
text2 = "---Python---"
print(text2.strip("-")) #belirtilen karakterlerde silinebilir

#maketrans string metodu ve translate string metodu 
#bu ikisi birlikte kullanılır
#maketrans() → belirtilen karakterleri değiştirmek için kullanılır
#karakterleri dönüştürmek için bir çeviri tablosu oluşturur.
#translate() → string içindeki karakterleri değiştirir.
text="Hello Python"
result=str.maketrans("P","T")
print(text.translate(result))

myDict={108:65}
text="Hello Pyhton"
result=str.maketrans(myDict)
print(text.translate(result))

text2="Hello, Python"
x="PH"
y="Tm"
result=str.maketrans(x,y)
print(text2.translate(result))

#partition mwtodu
#Bir stringi, verilen ayırıcıya göre 3 parçaya böler
#Ayırıcıdan önceki kısım,Ayırıcı,Ayırıcıdan sonraki kısım
text="I could eat banana all day"
result=text.partition("banana")
print(result)
#stringte olmayan bir değişken arandığında stringin bütün parçasını tek bir veri olarak kabul eder 2. ve 3 kısmı ise boş bırakır.
text="I could eat banana all day"
result=text.partition("5")
print(result)

#replace metodu
#Bir string içindeki belirtilen kısmı başka bir şeyle değiştirir.
text="I could eat banana all day"
result=text.replace("banana","lemon")
print(result)

text="I could eat banana banana banana all day"
result=text.replace("banana","lemon",2)
print(result)
#2 parametresi ile ilk 2 tane ifadeyi değiştir diğerine dokunma deriz.