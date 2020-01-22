import string as s
import random as r
lengthOfPassword = int(input("Enter The Legnth Of Your Password"))
#temp = lengthOfPassword
letters = int(input("Enter Number Of Letters In The Password"))
numbers= int(input("Enter Number Of Numbers In The Password"))
digits = s.digits
symbols ="!~@#$%^&*(){}|?"
bothAscii = s.ascii_letters
emptyList1 =[]
emptyList2 =[]
emptyList3 =[]
while lengthOfPassword != 0:
    for i in range (0,letters): #For Letters
        #newPassword = "".join(r.choice(bothAscii))
        
        emptyList1.append(r.choice(bothAscii))
        lengthOfPassword -=1
#newPassword1 = newPassword
    for i in range (0,numbers): #For numbers
        #newPassword ="".join(r.choice(digits))
        
        emptyList2.append(r.choice(digits))
        lengthOfPassword -=1
#newPassword2 = newPassword
    if lengthOfPassword != 0 :
        for i in range(0,lengthOfPassword):
            #newPassword = "".join(r.choice(symbols))
            
            emptyList3.append(r.choice(symbols))
            lengthOfPassword -=1
if len(emptyList3)!=0:
    newPassword3 = "".join(emptyList3)
newPassword1 = "".join(emptyList1)
newPassword2 = "".join(emptyList2)
#newPassword3 = newPassword
if len(emptyList3)!=0 :
    newPassword = newPassword1+newPassword2+newPassword3
else:
    newPassword = newPassword1+newPassword2
result=list(newPassword)
r.shuffle(result)
res = ''.join(result)
print(res)
