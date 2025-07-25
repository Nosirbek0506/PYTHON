
"""
name="Nosirbek Yuldoshev"
print(name +" yaxshi inson")
print(name.upper().isupper())
print(len(name))
print(name.index("Y"))
print(name.replace("Nosirbek","Nodir")) 

num=-5
print(str(abs(num))+' my favourite number')


num=5
print(pow(num,3))
print(round(5.8))
from math import *
print(floor(5.8))

name = input('enter your name:')
print("hello " + name)

num1=int(input('enter your number:'))
num2=int(input('enter another nummber'))
result=num1+num2
print(result)

lists=[1,3,4,8]
print(lists[2:])

lists=[1,3,4,8]
lists[1]=5
print(lists[1:])

lists=[1,3,4,8]
lists1=["nosirbek",'nodirbek']
lists.extend(lists1)
print(lists)

lists=[1,3,4,8]
lists.append(10)
print(lists)

names=['nosir','nodir','bobur','nabi']
names.insert(2,'bekzod')
print(names)


names=['nosir','nodir','bobur','nabi']
names.remove('nodir')
print(names)


names=['nosir','nodir','nodir',"nodir",'bobur','nabi']
print(names.count('nodir'))

names=['nosir','nodir','nodir',"nodir",'bobur','nabi']
names.sort()
print(names)

lists=[1,3,4,8]
lists.reverse()
print(lists)

names=['nosir','nodir','nodir',"nodir",'bobur','nabi']
families=names.copy()
print(families)

def cube(num):
    return num**3
kub=cube(6)
print(kub)

raqamlar=(5,10,16,20,24)
for raqam in raqamlar:
    if raqam<10:
        print(raqam,"10 dan past")
    elif raqam<20:
        print(raqam,"20 dan past")   
    elif raqam<30:
        print(raqam,"24 dan past")    
    else:
        print(raqam,"juda katta raqam")    

is_male=True  
is_age = True
if is_male and is_age:
    print("you are gogd") 
elif not is_male and not is_age:
    print("you are bad")


def max_num(num1,num2,num3,num4):
    if num1>=num2 and num2>=num3 and num3>=num4:
        return num1
    elif num2>=num1 and num2>=num3 and num3>=num4 :
        return num2
    elif num3>=num1 and num3>=num2 and num3>=num4:
        return num3
    else:
        return  num4
print(max_num(5,10,85,2))


num1=float(input('enter first number:'))
op=input('enter operator:')
num2=float(input('enter second number:'))

if op =="+":
    print(num1+num2)
elif op == "-":
    print(num1-num2) 
elif op =="/":
    print(num1/num2)  
elif op =="*":
    print(num1*num2)     

else:
    print('invalid operator')    

fname=input('enter your fname: ')
op=input('enter operator: ')
lname=input('enter your lname:+')
if op =="+":
    print(len(fname)+len(lname))
elif op == "-":
    print(len(fname)-len(lname)) 
elif op =="/":
   print(len(fname)/len(lname))
elif op =="*":
    print(len(fname)*len(lname))
else:
    print("else")    
    
   
months={
  "jan":"january",
  "feb":"february",
  "mar":"march",
  "apr":"april",
  "my":"may",
  "jun":"june"
 }   

print(months["apr"])
print(months.get("jun"))


a=2
while a<10:
     a+=1
     if a==7:
          break # 7 ga yetganda to'xta
     print (a)

secret_word = "giraffe"
guess=""
while guess !=secret_word:   #guessing game
    guess=input("enter guess:") 
print("you win")    
"""
secret_word = "giraffe"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False
while guess !=secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("enter guess:") 
        guess_count+=1
    else:
        out_of_guesses=True
    if out_of_guesses:
        print("out_of_guesses,YOU LOSE")
    else:
        print("you win")

    