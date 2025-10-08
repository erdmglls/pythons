x=20
y=60
if x>y:
    print(x,"is greater than",y)
else:
    print(x,"less than",y)
#-----------------------------------------------

print("bool('python'):",bool("python"))
print("bool(7):",bool(7))
print("bool(['pineapple','melon','apple']):", bool(['pineapple','melon','apple']))
print("bool(''):",bool("")) 
print("bool(0):",bool(0))                             
#(0) ve boş karaktere false döndürüyor sadece
#-----------------------------------------------
def myFunciton():
    return False
if myFunciton():
    print ("YES")
else:
    print("NO")
#----------------------------------------------
def myFunciton():
    return False
if myFunciton():
    print ("YES")
else:
    print("NO")
#----------------------------------------------
def myFunciton():
    return True
if myFunciton():
    print ("YES")
else:
    print("NO")
#----------------------------------------------
def myFunciton():
    return False
if True:
    print ("YES")
else:
    print("NO")
#---------------------------------------------
def myFunciton():
    return False
if False:
    print ("YES")
else:
    print("NO")