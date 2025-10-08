#isdigit metodu
#tüm karakterlerin rakam olup olmadığını kontrol eder
#rakamsa True,değilse false döndürür
text="546321"
result=text.isdigit()
print(result)#true

#isidentifier metodu
#değişken adlandırılmlası esnasın a-z,0-9 ve (_) kullanıma izin verir
#sayı ile başlamasına ve isimler arasında boşluk olmasına izin vermez
#ona göre true false döndürür
a="ErdemGül"
b="7isim"
c="ERDEM_GÜL"
print(a.isidentifier())#true
print(b.isidentifier())#false
print(c.isidentifier())#true

#isnumeric metodu
#stringin sadece sayısal karakterlerden oluşup oluşmadığını kontrol eder
#isdigit() ten farkı roma rakamlaı,üst indis gibi farklı sayısal ifadeleride true kabul eder
#bu şartlara göre true false döndürür
#-8 gibi ifadelerde false döndürür 
#ondalıklı 2.3 gibi sayılarda false döndürür
text="552555"
result=text.isnumeric()
print(result)

#isprintable metodu
#stringin bütün karakterleri ekrana yazılabilir mi diye bakar
#escape karakterleri (\n\t gibi) ekrana yazdırılamaz bu yüzden false döner
text="ERDEM\nGÜL"
result=text.isprintable()
print(result)#false

#isspace metodu
#stringteki tüm karakterlerin boşluktan olumşması gerekir
#boşluk ise true,değil ise false döner
text="          "
result=text.isspace()
print(result)#true

#istitle metodu
#string içindeki her bir kelimenin büyük harflerle başlayıp
#başlamadığını kontrol eder # büyükse true değilse false döner
text="Welcome My Home"
result=text.istitle()
print(result)#true

#join metodu
#Bir stringi ayırıcı (separator) gibi kullanarak listedeki elemanları birleştirir.
text="ERDEM","GÜL","PYTHON","Studio"
result="*".join(text)
print(result)

names="apple","banana","blueberry"
mySeparator=":"
text=mySeparator.join(names)
print(text)

#ljust and rjust metodları
#stringi verilen uzunluğa göre sola yaslar,boş kalan kısımları başka bir karakterle doldurabilir
text="banana"
result=text.ljust(20,"+")
print(result,"my favorite fruit")

#Stringi verilen uzunluğa göre sağa yaslar, boş kalan kısımları başka bir karakterle doldurabilir.
text="banana"
result=text.rjust(20,"-")
print(result,"my favorite fruit")











