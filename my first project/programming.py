
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

for i in "giraffe academy":
    print(i)    

for a in range(5):
    if a==2:
        print("aaa")
    else:
        print("bbb")    
    
def raise_to_power (base_num , pow_num):
    result=1
    for index in range (pow_num):
        result=result*base_num
    return result
print(raise_to_power(5,1))

number= [[1,2,3],[4,5,6],[7,8,9]]    
for a in number:
    for i in number:
        print(i)            

try:
    number=int(input("enter  a number:"))   
    print(number)           
except:
    print('invalid object')  
 
with open("customer.txt","w") as f:
    f.write("Nosirbek\nAli\nVali")

with open("customer.txt","r") as f:
    print(f.read())     
   
with open("customer.txt","a") as f:
    f.write("behruz\n,ali\n,nabi\n")

aa=open("customer.txt","r")
for i in aa.readlines():
    print(i)
 
class student:
    def __init__(self, fakulteti, guruhi, GPA):
        self.fakulteti = fakulteti
        self.guruhi = guruhi
        self.GPA = GPA
talaba1=student("servis","irb",3)   
talaba2=student("iqtisod","IK",5)
print(talaba1.fakulteti)
""" 
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
class Question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer

questions=[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
] 

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score += 1
    print("you got "+ str(score)+"/"+str(len(questions))+"correct")  

run_test(questions)            