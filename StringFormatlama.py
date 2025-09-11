#string formatlama
age=21
text="My name is Erdem, I am "+str(age)#age doğrudan içeri yazılmaz çünkü
#aynı tür değiller tür dönüşümü lazım
print(text)

#string formatlama 2
age=21
text="My name is Erdem, I am {}".format(age)
print(text)
#burada .format kullanarak age isimli değişkenin köşeli parantez içerisine girmesini sağlarız

#string formatlama 3
age=21
name="Erdem Gül"
text="My name is {}, I am {} ".format(name,age)
print(text)
#bu şekilde farklı değişkenler ile çeşitlendirebiliriz
#normalde burada name=0 age=1 dir

#string formatlama 4
age=21
name="Erdem Gül"
text="My name is {1}, I am {0} ".format(name,age)
print(text)
#indeks içerisine sayı yazabilir yerlerini değiştirebirsinc

#f-string kullanımı 
age=21
name="Erdem Gül"
text=f"My name is {name}, I am {age} "
print(text)
#bu yöntem kullanılırken öncelikli olarak f ifadesini metnin başına getirmelisin
#sonrasında değişken isimleri köşeli parantez içine yazılmalı^
#kullanımı daha kolay ve etkili

price=19.925
text=f"The price is {price} turkish lira"
print(text)

price=19.875
text=f"The price is {price:.1f} turkish lira"
print(text)
#{price:.19f} kullanımı ben 19.875 sayısının virgülden sonraki tek basamğını istiyorum float olarak demek