import random
#choice
mylist=["black","white","orange","purple","blue","green"]

print(random.choice(mylist))
#####################
text="python"#farklı örnek

print(random.choice(text))

########################
#choices

mylist=["cherry","strawberry","grape","banana","apple"]
print(random.choices(mylist))

mylist=["cherry","strawberry","grape","banana"]
print(random.choices(mylist,weights=[1,3,1,1],k=20))

#random.choices() listeden birden fazla rastgele eleman seçer.
#k=20 → 20 tane seçim yapılacak.
#Yani sonuçta 20 elemanlı bir liste döner.
#weights parametresi
#Burada ağırlıklar verilmiş: [1, 3, 1, 1].
#Bu ağırlıklar sırasıyla:
#cherry → 1
#strawberry → 3
#grape → 1
#banana → 1

mylist=["skoda","bmw","audi","nissan","toyota","volvo","ford"]#shuffle
random.shuffle(mylist)
print(mylist)
##############################
mylist=["skoda","bmw","audi","nissan","toyota","volvo","ford"]#shuffle
print(random.sample(mylist,k=2))
###############################
print(random.uniform(1, 5))   # Örn: 3.724571054 #uniform
##############################
print(random.triangular(1, 10, 5))  # 5 civarında yoğunlaşır #tringular #5 vermeseydin iki sayının ortalamasına yoğunlaşırdı

