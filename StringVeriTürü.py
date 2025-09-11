#stringler birer dizidir
#ilk ifade sıfır ile başlar
cars=["bmv","volvo","skoda","nissan"]
print(cars[1])

text="Hello, Python!"
print(text[5])

#stringlerde döngü kullanımı
text="Python is weird"
for x in text:#texti x'in içine boşalttı
    print(x)

#stringhte uzunluk
text="python is cool"
print(len(text))#len fonksiyonu kullanılır

#in=belirli bir ifadenin veya karakterin stringte olup olmadığını kontrol ederken kullanılır
text="The best languages in life are free"
print("best" in text)#diğer bir yol

#diğer bir yol
text="The best languages in life are free"
search="best"
print(search in text)#diğer bir yol
#if ile
text="The best languages in life are free"
if search in text:
    print("Yes, 'best' is present")