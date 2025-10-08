#rpartition metodu
text=" I could eat banana every day banana my favorite fruit."
result=text.rpartition("banana")
print(result)

#find metodu
#Aranan alt stringin ilk geçtiği indexi döndürür.
#bulamazsa -1 döner.
text=" I could eat banana every day.Banana my favorite fruit."
result=text.find("banana")
print(result)

#rfind metodu 
#find gibidir ama en sondan aramaya başlar (index yine baştan sayılır).
text=" I could eat banana every day banana my favorite fruit."
result=text.rfind("banana")
print(result)
#arama işini ölçeklendirebilirsinde indexler arasında 
text=" I could eat banana every day Banana my favorite fruit."
result=text.rfind("banana",13,22)
print(result)

#rindex
#index gibidir ama en sondan arar. Bulamazsa hata verir.
text = "hello world"
print(text.rindex("o"))

#split metodu
#Stringi ayırıcıya göre listeye böler.
text = "apple,banana,cherry"
print(text.split(","))

text=" I could eat, banana every day, Banana my favorite, fruit."
result=text.split(",",2) #ayırıcıyı görünce verdiğimiz sayı kadar parçalar (baştan sona)
print(result)

#rsplit
#split gibidir ama sağdan başlayarak böler.
text = "apple,banana,cherry"
print(text.rsplit(",", 1))  # sadece 1 kez böler

#splitlines 
#her bir stringi satır sonlarına göre (\n) böler ve her bir satırı
#bir liste öğesi olarak döndürür gene bir listenin içinde
text = "Hello\nWorld\nPython"
result=text.splitlines()#parantez içi her zaman false idir
print(result)

#zfiil metodu
#Stringin soluna sıfır ekler
text = "50"#sonu sıfır alan sayılarda sıfırı(başka bir sayıda olabilirdi) ve ana sayıyıda sayarak ekler
result=text.zfill(4)#ama sıfır ekleme sağdan sola doğru
print(result)

text = "55"#
result=text.zfill(4)
print(result)