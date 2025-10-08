text="The price is only {price:.2f} turkish lira."
text1="My name is {fname},I'm {age} years old".format(fname="Erdem",age=21)
text2="My name is {0},I'm {1} years old".format("Erdem",21)
text3= "My name is {},I'm {} years old".format("Erdem",21)

print(text1)
print(text2)
print(text3)

#format türleri

text="we do not have {:<10} score"
#:<10 demek arada 10 boşluk bırak ve stringi sola yasla,7 gelip 10 boşluğun ilkine yerleşir
#Kalan boşluklar sağda olur.
print(text.format(7))

text="we do not have {:>10} score"
#:<10 demek arada 10 boşluk bırak ve stringi sağa yasla,7 gelip 10 boşluğun sonuncusuna yerleşir
#Kalan boşluklar solda olur.
print(text.format(7))

text="we do not have {:^10} score"
#stringi 10 karakter genişliğini en ortasıan koyar yani ortalar.
#Eksik karakterler iki yana eşit boşluk bırakır.
print(text.format(2))

text="The score is {:=10} degrees celsius"
print(text.format(-3))
#üç sayısını 10 boşluk içinde en sağa atacak eksiyi ise en başa alarak ondan uzaklaştıracaktır
text="The score is {:=10} degrees celsius"
print(text.format(+3))
#aynısı (+6) gibi sayılar için geçerli değildir + işaretini yazmaz ama sayıyı en sağa atar gene.

#Sayı pozitif olsa da başına + koyar.
print("{:+}".format(42))   # +42
print("{:+}".format(-42))  # -42

print("{:-}".format(+42))
#artı işaretini de yok etmek içim {:-} kullanırız