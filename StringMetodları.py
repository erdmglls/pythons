#capitalize metodu
text="welcome to this here"
result=text.capitalize()
print(result)
#ilk harfin büyük olmasını sağlar

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

text="w7e8f5"#bu tarz ifadelerdesayılardan hemen sonraki harfleride büyük yazar hemde hepsini
result=text.title()
print(result)
#her kelimenin ilk harfini büyük yazdırır

#swapcase metodu
#Büyük herfleri küçük,küçük harfleri büyük yazar
text="Welcome To The This Here"
result=text.swapcase()
print(result)
