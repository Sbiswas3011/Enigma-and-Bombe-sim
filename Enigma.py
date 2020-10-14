# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:55:08 2020

@author: Snehangsu
"""
from tkinter import *



rty1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ref1=['h','q','u','t','v','m','r','a','l','s','z','i','f','y','x','w','b','g','j','d','c','e','p','o','n','k']
ref2=['f','q','i','k','y','a','s','n','c','r','d','w','u','h','x','z','b','j','g','v','m','t','l','o','e','p']
ref3=['c','r','a','h','q','n','i','d','g','m','l','k','j','f','p','o','e','b','w','v','z','t','s','y','x','u']

R1=['z', 'x', 'v', 'u', 'k', 'o', 'f', 'h', 'd', 'q', 'i', 't', 'm', 'l', 'w', 'e', 'n', 'p', 'y', 'b', 'g', 'r', 's', 'c', 'j', 'a']
R2=['d', 'i', 't', 'l', 's', 'e', 'r', 'y', 'x', 'w', 'h', 'g', 'z', 'q', 'v', 'c', 'n', 'j', 'u', 'a', 'm', 'p', 'o', 'f', 'b', 'k']
R3=['p', 'y', 'g', 'c', 'k', 'z', 'w', 'e', 'l', 'd', 'j', 'a', 'u', 'q', 'n', 'm', 'i', 't', 'b', 'h', 's', 'r', 'o', 'f', 'v', 'x']
R4=['i', 'c', 'g', 'z', 'e', 'm', 'j', 'n', 'v', 'b', 'd', 'o', 'a', 'w', 'p', 'h', 'y', 's', 'f', 'r', 'q', 'l', 'k', 'x', 'u', 't']
R5=['v', 't', 'g', 'q', 'i', 'u', 'r', 'b', 's', 'h', 'm', 'n', 'd', 'z', 'a', 'c', 'l', 'x', 'j', 'y', 'o', 'e', 'p', 'f', 'k', 'w']

R1_internal=[25,22,19,17,6,9,-1,0,-5,7,-2,8,0,-2,8,-11,-3,-2,6,-18,-14,-4,-4,-21,-15,-25]
R2_internal=[3,7,17,8,14,-1,11,17,15,13,-3,-5,13,3,7,-13,-3,-8,2,-19,-8,-6,-8,-18,-23,-15]
R3_internal=[15,23,4,-1,6,20,16,-3,3,-6,-1,-11,8,3,-1,-3,-8,2,-17,-12,-2,-4,-8,-18,-3,-2]
R4_internal=[8,1,4,22,0,7,3,6,13,-8,-7,3,-12,9,1,-8,8,1,-13,-2,-4,-10,-12,0,-4,-6]
R5_internal=[21,18,4,13,4,15,11,-6,10,-2,2,2,-9,12,-14,-13,-5,6,-9,5,-6,-17,-7,-18,-14,-3]

reflector=[ref1,ref2,ref3]
rotorI=[R1_internal,R2_internal,R3_internal,R4_internal,R5_internal]
rotorE=[R1,R2,R3,R4,R5]

def shift(n,ar):
    temp=[]
    
    n=int(n)
    for i in range(0,n-1):
        temp.append(ar[i])
    del ar[0:n-1]
    ar=ar+temp
    return ar

def rotate(l, n):
    return l[n:] + l[:n]
    
def RR(m,lists): 
    output_list = [] 
      
    n=len(lists)
    for j in range(0,m):
        output_list.append(lists[n-1])
    
        for i in range(0,n-1):
            output_list.append(lists[i])
          
    return output_list 


root = Tk()
root.title("Enigma Simulator")
#root.geometry("1000x350")
l1=Label(root,text="Encrypt/Decrypt").grid(row=0,column=0,columnspan=1,padx=5,pady=5)
l2=Label(root,text="Output").grid(row=1,column=0,columnspan=1,padx=5,pady=5)

e = Entry(root,width=100,borderwidth=4)
e.grid(row=0,column=1,columnspan=5,padx=5,pady=5)
e2 = Entry(root,width=100,borderwidth=4)
e2.grid(row=1,column=1,columnspan=5,padx=5,pady=5)
 
def reset(): 
    global FL_list
    global ref
    global O1
    global O2
    global O3
    global rotorI
    rotorI[O1-1]=rotorI[O1-1]
    e2.delete(0,'end')
    e4.delete(0,'end')
    e4.insert(0,0)
    e.delete(0,'end')
    FL_list.clear()
    ref=0
    O1=0
    O2=0
    O3=0
    var1=IntVar(root)
    var1.set(1)
    var2=IntVar(root)
    var2.set(1)
    var3=IntVar(root)
    var3.set(1)
    var4=IntVar(root)
    var4.set(1)
    var5=IntVar(root)
    var5.set(1)
    var6=IntVar(root)
    var6.set(1)
    InternalR1.config(textvariable=var1)
    InternalR2.config(textvariable=var2)
    InternalR3.config(textvariable=var3)
    ExternalR1.config(textvariable=var4)
    ExternalR2.config(textvariable=var5)
    ExternalR3.config(textvariable=var6)


var1=IntVar(root)
var1.set(1)
var2=IntVar(root)
var2.set(1)
var3=IntVar(root)
var3.set(1)
var4=IntVar(root)
var4.set(1)
var5=IntVar(root)
var5.set(1)
var6=IntVar(root)
var6.set(1)

rotor_cnt=0 
O1=0
O2=0
O3=0  
def rotor_input(i): 
    global rotor_cnt,O1,O2,O3
    if rotor_cnt==0:
        O1=int(i)
    elif rotor_cnt==1:
        O2=int(i)
    elif rotor_cnt==2:
        O3=int(i)
        rotor_cnt=-1
   
    rotor_cnt+=1
    print(O1,O2,O3)

I_button=Button(root,text="I",padx=50,pady=20,command=lambda: rotor_input(1)).grid(row=2,column=1)
II_button=Button(root,text="II",padx=50,pady=20,command=lambda: rotor_input(2)).grid(row=2,column=2)
III_button=Button(root,text="III",padx=50,pady=20,command=lambda: rotor_input(3)).grid(row=2,column=3)
IV_button=Button(root,text="IV",padx=50,pady=20,command=lambda: rotor_input(4)).grid(row=2,column=4)
V_button=Button(root,text="V",padx=50,pady=20,command=lambda: rotor_input(5)).grid(row=2,column=5)


InternalR1=IntVar()
InternalR2=IntVar()
InternalR3=IntVar()
ExternalR1=IntVar()
ExternalR2=IntVar()
ExternalR3=IntVar()

#this is not working
InternalR1 = Spinbox(root, from_=1, to=26,font=("helvetica",10),textvariable=var1)
InternalR1.grid(row=3,column=1)
InternalR2 = Spinbox(root, from_=1, to=26,font=("helvetica",10),textvariable=var2)
InternalR2.grid(row=3,column=3)
InternalR3 = Spinbox(root, from_=1, to=26,font=("helvetica",10),textvariable=var3)
InternalR3.grid(row=3,column=5)

ExternalR1 = Spinbox(root, from_=1, to=26,font=("helvetica",10),textvariable=var4)
ExternalR1.grid(row=4,column=1)
ExternalR2 = Spinbox(root, from_=1, to=26,font=("helvetica",10),textvariable=var5)
ExternalR2.grid(row=4,column=3)
ExternalR3 = Spinbox(root, from_=1, to=26,font=("helvetica",10),textvariable=var6)
ExternalR3.grid(row=4,column=5)

ref=0

def reflector_input(i):
    global ref
    ref=i
   
    

I2_button=Button(root,text="I",padx=50,pady=20,command=lambda: reflector_input(1)).grid(row=5,column=1)
II2_button=Button(root,text="II",padx=50,pady=20,command=lambda: reflector_input(2)).grid(row=5,column=3)
III2_button=Button(root,text="III",padx=50,pady=20,command=lambda: reflector_input(3)).grid(row=5,column=5)

e3 = Entry(root,width=60,borderwidth=4)
e3.grid(row=6,column=1,columnspan=3,padx=5,pady=5)

e4 = Entry(root,width=20,borderwidth=4)
e4.grid(row=6,column=5,columnspan=1,padx=5,pady=5)
e4.insert(0,0)

FL_list=[]#flip list
cnt_flip=0
def enter_key():
    cnt_flip=0
    if e4.get()=="13":
        e4.insert(0,"13 is MAX")
    else:
        FL=e3.get()
        if not any(FL[0] in x for x in FL_list) and not any(FL[1] in x for x in FL_list):
            FL_list.append([FL[0],FL[1]])
            cnt_flip+=1
        else:
            print("pair cable in use")
            e3.delete(0,END)
            
    if(cnt_flip>0):
        i=int(e4.get())+1
        e4.delete(0,END)
        e3.delete(0,END)
        e4.insert(0,i)
        
    
    
enter_button=Button(root,text="ENTER",padx=50,pady=10,command=enter_key).grid(row=6,column=4)


def encrypt(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list):
    
    e2.delete(0,END)
    IR1=int(InternalR1.get())
    IR2=int(InternalR2.get())
    IR3=int(InternalR3.get())
    ER1=int(ExternalR1.get())
    ER2=int(ExternalR2.get())
    ER3=int(ExternalR3.get())
    
    rotorI[O1-1]=shift(IR1,rotorI[O1-1]) 
    rotorI[O2-1]=shift(IR2,rotorI[O2-1])
    rotorI[O3-1]=shift(IR3,rotorI[O3-1]) 
    
    #print(rotorI[O1-1])
    print(IR1)
    
    for i in range(0,26):
        if(ord(rty1[i])+rotorI[O1-1][i]>122):
            rotorE[O1-1][i]=chr(96+((ord(rty1[i])+rotorI[O1-1][i])-122))
        elif(ord(rty1[i])+rotorI[O1-1][i]<97):
            rotorE[O1-1][i]=chr(123-(97-(ord(rty1[i])+rotorI[O1-1][i])))
        else:
            rotorE[O1-1][i]=chr(ord(rty1[i])+rotorI[O1-1][i])
    #print(rotorE[O1-1])
    for j in range(0,26):
        if(ord(rty1[j])+rotorI[O2-1][j]>122):
            rotorE[O2-1][j]=chr(96+((ord(rty1[j])+rotorI[O2-1][j])-122))
        elif(ord(rty1[j])+rotorI[O2-1][j]<97):
            rotorE[O2-1][j]=chr(123-(97-(ord(rty1[j])+rotorI[O2-1][j])))
        else:
            rotorE[O2-1][j]=chr(ord(rty1[j])+rotorI[O2-1][j])

    for k in range(0,26):
    #print(k)
        if(ord(rty1[k])+rotorI[O3-1][k]>122):
            rotorE[O3-1][k]=chr(96+((ord(rty1[k])+rotorI[O3-1][k])-122))
        elif(ord(rty1[k])+rotorI[O3-1][k]<97):
            rotorE[O3-1][k]=chr(123-(97-(ord(rty1[k])+rotorI[O3-1][k])))
        else:
            rotorE[O3-1][k]=chr(ord(rty1[k])+rotorI[O3-1][k])
            
    #print(rotorE[O1-1])
    print(rotorI[O1-1])
    
    rotorE[O1-1]=shift(ER1,rotorE[O1-1]) 
    rotorE[O2-1]=shift(ER2,rotorE[O2-1])
    rotorE[O3-1]=shift(ER3,rotorE[O3-1]) 
    
    #print(rotorE[O1-1])
    
    
    #print(O1,O2,O3)
    st=str(e.get())
    r1_cnt=0
    r2_cnt=0
    r3_cnt=0
    for i in range(0,len(st)):
        if(st[i]==" "):
            #print(" ",end='')
            e2.insert(i," ")
            continue
        else:
            cnt=0
            s1=rotorE[O1-1][ord(st[i])-97]#step 1
            s2=rotorE[O2-1][ord(s1)-97]#step 2
            s3=rotorE[O3-1][ord(s2)-97]#step 3
            s4=reflector[ref-1][ord(s3)-97]#step 4
            s5=rty1[rotorE[O3-1].index(s4)]#step 5
            s6=rty1[rotorE[O2-1].index(s5)]#step 6
            s7=rty1[rotorE[O1-1].index(s6)]#step 7
            for left, right in FL_list:
                if(s7==left):
                    s7=right
                    cnt+=1
                    #print(s7,end='')
                    e2.insert(i,s7)
                elif(s7==right):
                    s7=left
                    cnt+=1
                    #print(s7,end='')
                    e2.insert(i,s7)
            if(cnt==0):
                #print(s7,end='')
                e2.insert(i,s7)
            rotorE[O1-1]=RR(1,(rotorE[O1-1]))
            r1_cnt+=1
            if(r1_cnt>25):
                rotorE[O2-1]=RR(1,(rotorE[O2-1]))
                r2_cnt+=1
                r1_cnt=0
            if(r2_cnt>25):
                rotorE[O3-1]=RR(1,(rotorE[O3-1]))
                r3_cnt+=1
                r2_cnt=0
                
    rotorI[O1-1]=rotate(rotorI[O1-1],-(IR1-1)) 
    rotorI[O2-1]=rotate(rotorI[O2-1],-(IR2-1))
    rotorI[O3-1]=rotate(rotorI[O3-1],-(IR3-1)) 
                

def decrypt(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list):
    
    e2.delete(0,END)
    IR1=int(InternalR1.get())
    IR2=int(InternalR2.get())
    IR3=int(InternalR3.get())
    ER1=int(ExternalR1.get())
    ER2=int(ExternalR2.get())
    ER3=int(ExternalR3.get())
    
    rotorI[O1-1]=shift(IR1,rotorI[O1-1]) 
    rotorI[O2-1]=shift(IR2,rotorI[O2-1])
    rotorI[O3-1]=shift(IR3,rotorI[O3-1]) 
    
    #print(rotorI[O1-1])
    
    for i in range(0,26):
        if(ord(rty1[i])+rotorI[O1-1][i]>122):
            rotorE[O1-1][i]=chr(96+((ord(rty1[i])+rotorI[O1-1][i])-122))
        elif(ord(rty1[i])+rotorI[O1-1][i]<97):
            rotorE[O1-1][i]=chr(123-(97-(ord(rty1[i])+rotorI[O1-1][i])))
        else:
            rotorE[O1-1][i]=chr(ord(rty1[i])+rotorI[O1-1][i])
            
    #print(rotorE[O1-1])
        
        
    for i in range(0,26):
        if(ord(rty1[i])+rotorI[O2-1][i]>122):
            rotorE[O2-1][i]=chr(96+((ord(rty1[i])+rotorI[O2-1][i])-122))
        elif(ord(rty1[i])+rotorI[O2-1][i]<97):
            rotorE[O2-1][i]=chr(123-(97-(ord(rty1[i])+rotorI[O2-1][i])))
        else:
            rotorE[O2-1][i]=chr(ord(rty1[i])+rotorI[O2-1][i])
        
        
    for i in range(0,26):
        if(ord(rty1[i])+rotorI[O3-1][i]>122):
            rotorE[O3-1][i]=chr(96+((ord(rty1[i])+rotorI[O3-1][i])-122))
        elif(ord(rty1[i])+rotorI[O3-1][i]<97):
            rotorE[O3-1][i]=chr(123-(97-(ord(rty1[i])+rotorI[O3-1][i])))
        else:
            rotorE[O3-1][i]=chr(ord(rty1[i])+rotorI[O3-1][i])
    
    rotorE[O1-1]=shift(ER1,rotorE[O1-1]) 
    rotorE[O2-1]=shift(ER2,rotorE[O2-1])
    rotorE[O3-1]=shift(ER3,rotorE[O3-1]) 
    
    #print(rotorE[O1-1])
    

    st=list(e.get())
    r1_cnt=0
    r2_cnt=0
    r3_cnt=0
    for i in range(0,len(st)):
        if(st[i]==" "):
            #print(" ",end='')
            e2.insert(i," ")
            continue
        else:
            cnt=0
            for left, right in FL_list:
                if(st[i]==left):
                    st[i]=right
                    cnt+=1                   
                elif(st[i]==right):
                    st[i]=left
                    cnt+=1                              
            s1=rotorE[O1-1][ord(st[i])-97]#step 1
            s2=rotorE[O2-1][ord(s1)-97]#step 2
            s3=rotorE[O3-1][ord(s2)-97]#step 3
            s4=reflector[ref-1][ord(s3)-97]#step 4
            s5=rty1[rotorE[O3-1].index(s4)]#step 5
            s6=rty1[rotorE[O2-1].index(s5)]#step 6
            s7=rty1[rotorE[O1-1].index(s6)]#step 7
            #print(s7,end='')
            e2.insert(i,s7)
            rotorE[O1-1]=RR(1,(rotorE[O1-1]))
            r1_cnt+=1
            if(r1_cnt>25):
                rotorE[O2-1]=RR(1,(rotorE[O2-1]))
                r2_cnt+=1
                r1_cnt=0
            if(r2_cnt>25):
                rotorE[O3-1]=RR(1,(rotorE[O3-1]))
                r3_cnt+=1
                r2_cnt=0
                
    rotorI[O1-1]=rotate(rotorI[O1-1],-(IR1-1)) 
    rotorI[O2-1]=rotate(rotorI[O2-1],-(IR2-1))
    rotorI[O3-1]=rotate(rotorI[O3-1],-(IR3-1)) 
    

reset_button=Button(root,text="RESET",padx=40,pady=20,command=reset).grid(row=7,column=1)
encrypt_button=Button(root,text="ENCRYPT",padx=40,pady=20,command=lambda: encrypt(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list)).grid(row=7,column=3)
decrypt_button=Button(root,text="DECRYPT",padx=40,pady=20,command=lambda: decrypt(O1,O2,O3,rotorI,rotorE,ref,reflector,FL_list)).grid(row=7,column=5)

root.mainloop()
