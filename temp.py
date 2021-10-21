# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
print("This calcualtor is used to find least subtract/add/multiply/divisibale number")
print("                   to get a perfect square                                  ")
import math
a=int(input("Enter an interger to find perfect square- "))
# to get lease subtract number
sq=int(math.sqrt(a))
s=sq**2
dif=a-s
# to get lease add number
sq2=sq+1
s=sq2**2
dif2=s-a

# to get least multiply
def prime_factors(num):  
    org=int(num)
    l1=[]
    l2=[]
    while num % 2 == 0:  
        #print(2,)  
        num = num / 2
        l1+=[2]
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:  
            #print(i,)  
            num = num / i  
            l1+=[i]
    if num > 2:  
        #print(num)
        l1+=[num]
    for k in set(l1):
        chk=l1.count(k)
        if chk>1:
            chk2=int(chk/2)
            while chk2==1:
                l1.remove(k)
                chk2=chk2-1
        if chk%2!=0:
            #print("no prime",k)
            l2+=[k]
    #print(l2)
    li_mu=1
    for x in l2:
        li_mu=int(li_mu*x)
    li_min=int(li_mu*org)
    li_sq=int(math.sqrt(li_min))
    div_mu=li_mu
    div_min=int(org/div_mu)
    div_sq=int(math.sqrt(div_min))
    print('Least multiply number is      {f} \n   and perfect square is      {l}'.format(f=li_mu,l=li_sq))
    print('Least divide number is        {f} \n   and perfect square is      {l}'.format(f=div_mu,l=div_sq))
prime_factors(a)

# to get least multiply

print('Least subtract number is      {f} \n   and perfect square is      {l}'.format(f=dif,l=sq))
print('Least add number is           {f} \n   and perfect square is      {l}'.format(f=dif2,l=sq2))

pickle.dump(dif2,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))