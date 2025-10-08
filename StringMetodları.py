#capitalize metodu
text="welcome to this here"
result=text.capitalize()
print(result)
#ilk harfin büyük olmasını sağlar
#Geri kalan tüm harfleri küçük harfe çevirir.

#casefold metodu
text="WELCOME TO THE THİS HERE"#metnin tüm harflerini küçük hale getirir
result=text.casefold()
print(result)
#casefold>lower metodundan çünkü büyük işlerde daha fazla karakteri küçültür
#ancak casefold , lower dan daha yavaş çalışır

#title metodu
text="welcome to the this here"
result=text.title()
print(result)
#her kelimenin ilk harfini büyük yazdırır
#title metodu ' veya - gibi özel karakterlerden sonra gelen harfi de büyük yapabilir. Bu Python’un basit title() davranışıdır.

text="w7e8f5"#bu tarz ifadelerdesayılardan hemen sonraki harfleride büyük yazar hemde hepsini
result=text.title()
print(result)
#her kelimenin ilk harfini büyük yazdırır

#swapcase metodu
#Büyük herfleri küçük,küçük harfleri büyük yazar
text="Welcome To The This Here"
result=text.swapcase()
print(result)

#islower metodu
#tüm karakterler küçük mü?Küçükse true değilse false döndürür
text="Welcome To The This Here"
result=text.islower()
if(result):
    print("tüm harfleriniz küçük harf")
else:
    print("tüm harfleriniz küçük harf değil")

#isupper metodu
#tüm karakterler büyük mü?Büyükse true değilse false döndürür
text="WELCOME"
result=text.isupper()
if(result):
    print("tüm harfleriniz küçük harf")
else:
    print("tüm harfleriniz küçük harf değil")

#center metodu
#bir string’i belirli bir genişliğe ortalayarak döndürmek için kullanılır. 
#Yani metnin sağında ve solunda gerekli boşlukları ekleyerek, belirttiğiniz genişlikte bir “ortalanmış” metin oluşturur.
#kendiside dahil edilir  boşluğa,eleman sayısı çıkarılır boşluk ona göre ayarlanır
text="hello python"
result=text.center(20,"*")
print(result)
#mesela hello python 12 birim 20-12=8 ,4 e 4 sağ sol boşluk bırakılır