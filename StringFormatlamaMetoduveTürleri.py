#sayıların arasına binlik ayırıcı (,) yani virgül koyar.
text="My world is {:,} years old"
print(text.format(13000000))

#sayıların arasına binlik ayırıcı (_) koyar.
text="My world is {:_} years old"
print(text.format(13000000))

#sayıyı binary (ikilik sistem) olarak gösterir.
#Yani 0 ve 1’lerden oluşan ikili sayı karşılığını verir.
text="The binary version of {0} is {0:b}" 
print(text.format(6))

#sayının unicode da karşılık geldiği değer gösterir
text="The unicode version of {0} is {0:c}" 
print(text.format(350))

text="The binary version of {0} is {0:d}" 
print(text.format(0b101))
#kontrol edelim #sayıyı decimal (10’luk sistemde) gösterir.
print(bin(5))#sayıy binary olarak gösterir

#sayıyı bilimsel gösterim (scientific notation / üstel gösterim) biçiminde yazar
text="we have {:e} dog"#büyük E de aynı işe yarar
print(text.format(7))

#virgülden sonra 2 basamak almamızı sağlar
text="The price is {:.2f}"# 2 olmasaydı tek basamak alırdı sayı olmasaydı
print(text.format(54.5465))

#oktav [8lik gösterim] değerinin kaça denk geldiğini buldurur
text="The binary version of {0} is {0:o}" 
print(text.format(25))

#hexadecimal [16 lik gösterim] değerinin kaça denk geldiğini buldurur
text="The hexadecimal version of {0} is {0:X}" 
print(text.format(19))

#aynı şekilde sayıyı yazar
text="The binary version of {0} is {0:n}" 
print(text.format(20))

#yüzde olarak belirtmemizi sağlar
text="The number is {:.0%}" #burada yanına ekstra bir (.) eklemek 
print(text.format(0.70))

