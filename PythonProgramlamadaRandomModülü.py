import random

print(random.random()) #random metodu

#########################

random.seed(10)
print(random.random())  # Her zaman aynı çıktı: 0.5714025946899135
print(random.random())  # Her zaman aynı çıktı: 0.4288890546751146
#İlk print(random.random()) çağrısı, tohum 10'dan başlayarak dizideki ilk rastgele sayıyı üretir.
#İkinci print(random.random()) çağrısı ise, aynı tohum 10'dan başlayarak dizideki ikinci rastgele sayıyı üretir.
#Bu yüzden, her iki çıktı da farklıdır çünkü aynı rastgele sayı dizisinin farklı elemanları gösteriliyor.
#random.seed(10) satırını programın en başına koyduğunuz sürece, her çalıştırdığında bu iki print çağrısı her zaman aynı iki değeri üretecektir.
# rastgele sayılar aynı sırayla gelir hep

##########################

state = random.getstate()  # durumu kaydeder
print(random.random())      # Örn: 0.639
print(random.random())      # Örn: 0.025

random.setstate(state)      # durumu geri yükler
print(random.random())      # 0.639 (tekrar aynı)
print(random.random())      # 0.025 (tekrar aynı)

##########################

import random

print(random.getrandbits(8))  # 0–255 arası rastgele sayı
print(random.getrandbits(4))  # 0–15 arası rastgele sayı

#########################

import random

print(random.randrange(1, 10))       # 1 ile 9 arasında
print(random.randrange(0, 20, 5))    # 0,5,10,15 arasından rastgele

#########################

import random

print(random.randint(1, 6))  # Zar atma örneği: 1–6
print(random.randint(10, 20)) # 10–20 arası rastgele sayı

