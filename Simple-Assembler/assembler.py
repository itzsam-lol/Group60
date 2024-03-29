import sys
import os



reg=["R0","R1","R2","R3","R4","R5","R6"]
opcodess={"add":"00000","sub":"00001","mov":"00010","ld":"00100","st":"00101","mul":"00110"
        ,"div":"00111","rs":"01000","ls":"01001","xor":"01010","or":"01011","and":"01100"
        ,"not":"01101","cmp":"01110","jmp":"01111","jlt":"11100","jgt":"11101","je":"11111","hlt":"11010"}

reg_codes={"R0":"000",
           "R1":"001",
           "R2":"010",
           "R3":"011",
           "R4":"100",
           "R5":"101",
           "R6":"110",
           "FLAGS":"111"}

reg_val={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS":0}

var_address={}

var_val={}

mem_address={} 

error_print=[]
flag=0
var_ct=True

def binarytodec(b):

    i =1
    d =0 
    b=b[::-1]
    for x in b :
        if x == "1":
            d=d+i
        i=i*2
    return d

def dectobinary(d):
    zero=7-len(bin(d)[2:])
    ans="0"*zero+bin(d)[2:]
    return(ans)
def invert(b):
    k=""
    for i in b:
        if(i=="0"):
            k=k+"1"
        else:
            k=k+"0"
    return k
l=[]
for kx in sys.stdin:
   l.append(kx)

for i in range(len(l)):
    l[i]=list(map(str,l[i].strip().split()))
for i in range(len(l)):
  if l[i][-1]=="hlt" and i!=len(l)-1:
    error_print.append("halt is not the last instruction\n")
    flag=1
for i in range(len(l)):
    if l[i][0]=="var" and var_ct==True:
        continue
    elif l[i][0]!="var" and var_ct==True:
        var_ct=False
    elif l[i][0]!="var" and var_ct==False:
       continue
    elif l[i][0]=="var" and var_ct==False:
        error_print.append("Variable not defined at start.\n")
        flag=1
        break
 

    
    
j=0
while j==0:
    if len(l[j])==0:
      continue
    if(l[j][0]=="var"):
        temp=l.pop(j)
        l.append(temp)
        continue
    break

for i in range(len(l)):

    if len(l[i])==0:
      continue
    if(l[i][0]=="var"):
        var_address[l[i][1]]=dectobinary(i)
        var_val[l[i][1]]=0
   
    if (l[i][0][-1]==":" ):
      if (l[i][0][-2]!=" "):
        mem_address[l[i][0][:-1]]=dectobinary(i)
        l[i].pop(0) 
      else:
        error_print.append(f"Syntax error in line no.{i+1 +len(var_val)}")
        flag=1
        break

if flag==0:
  try:
    list_print=[]
    hlt_check=0
    for i in l:

        st=""
        mylist=i
        if len(mylist)==0:
          continue
        if mylist[0]=='add':
            if 0<=int(reg_val[mylist[2]])+int(reg_val[mylist[3]])<=127 :
                reg_a=mylist[1]
                reg_b=mylist[2]
                reg_c=mylist[3]
                if reg_a not in reg or reg_b not in reg or reg_c not in reg :
                          error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
                        

                else:
                  st2=opcodess["add"]+"00"+reg_codes[reg_a]+reg_codes[reg_b]+reg_codes[reg_c]
                  st=st2+"\n"
                  list_print.append(st)

        elif mylist[0]=="sub":
            if 0<=int(reg_val[mylist[2]])-int(reg_val[mylist[3]])<=127 :
                reg_a=mylist[1]
                reg_b=mylist[2]
                reg_c=mylist[3]
                if reg_a not in reg or reg_b not in reg or reg_c not in reg :
                  error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
                else:
                  st2=opcodess["sub"]+"00"+reg_codes[reg_a]+reg_codes[reg_b]+reg_codes[reg_c]
                  st=st2+"\n"
                  list_print.append(st)



        elif mylist[0]=="mul":
            if 0<=int(reg_val[mylist[2]])*int(reg_val[mylist[3]])<=127 :
                reg_a=mylist[1]
                reg_b=mylist[2]
                reg_c=mylist[3]
                if reg_a not in reg or reg_b not in reg or reg_c not in reg :
                  error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
                else:
                  st2=opcodess["mul"]+"00"+reg_codes[reg_a]+reg_codes[reg_b]+reg_codes[reg_c]
                  st=st2+"\n"
                  list_print.append(st)


        elif mylist[0]=="xor":
            reg_a=mylist[1]
            reg_b=mylist[2]
            reg_c=mylist[3]
            if reg_a not in reg or reg_b not in reg or reg_c not in reg :
                  error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
            else:
              st2=opcodess["xor"]+"00"+reg_codes[reg_a]+reg_codes[reg_b]+reg_codes[reg_c]
              st=st2+"\n"
              list_print.append(st)

        elif mylist[0]=="or":
            reg_a=mylist[1]
            reg_b=mylist[2]
            reg_c=mylist[3]
            if reg_a not in reg or reg_b not in reg or reg_c not in reg :
                  error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
            else:
              st2=opcodess["or"]+"00"+reg_codes[reg_a]+reg_codes[reg_b]+reg_codes[reg_c]
              st=st2+"\n"
              list_print.append(st)


        elif mylist[0]=="and":
            
            reg_a=mylist[1]
            reg_b=mylist[2]
            reg_c=mylist[3]
            if reg_a not in reg or reg_b not in reg or reg_c not in reg :
                  error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
            else:
              st2=opcodess["and"]+"00"+reg_codes[reg_a]+reg_codes[reg_b]+reg_codes[reg_c]
              st=st2+"\n"
              list_print.append(st)
    #mera code
    #move immediate 
        elif mylist[0]=="mov":
            string_move=str(mylist[2])
            if string_move[0]=="$":
                reg_a=mylist[1]
                if reg_a not in reg:
                  error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
                else:
                  val_1=int(mylist[2][1:])
                  if 0<=val_1<=127:
                    reg_val[mylist[1]]=val_1
                    st2=opcodess["mov"]+"0"+reg_codes[reg_a]+dectobinary(val_1)
                    st=st2+"\n"
                    list_print.append(st)
                    reg_val[mylist[1]]=0
                  else:
                    error_print.append(f"Broken Immediate values (more than 7 bits) in line no. { l.index(mylist)+1+len(var_val)}\n")
    #move register
            else:
                reg_a=mylist[1]
                reg_b=mylist[2]
                if reg_a not in reg or reg_b not in reg_codes:
                  error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
                else:
                  reg_val[mylist[1]]=reg_val[mylist[2]]
                  x="00011"
                  st2=x+"00000"+reg_codes[reg_a]+reg_codes[reg_b]
                  st=st2+"\n"
                  list_print.append(st)
                  reg_val[mylist[1]]=0
                  reg_val[mylist[2]]=0
        elif mylist[0]=="div":
            reg_a=mylist[1]
            reg_b=mylist[2]
            if reg_a not in reg or reg_b not in reg:
              error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
            else:
              x=reg_val[reg_a]
              y=reg_val[reg_b]
              st2= opcodess["div"]+"00000"+reg_codes[reg_a]+reg_codes[reg_b]
              st=st2+"\n"
              list_print.append(st)
              if y==0:
                  reg_val["R1"]=0
                  reg_val["R0"]=0
              else:
                  quo=x//y
                  remainder=x%y
                  reg_val["R0"]=quo
                  reg_val["R1"]=remainder
  
        elif mylist[0]=="ld":
            reg_a= mylist[1]
            var_name= mylist[2]
            if reg_a not in reg:
              error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
            else:
                if var_name in var_val:
                    st2=opcodess["ld"]+"0"+reg_codes[reg_a]+var_address[var_name]
                    st=st2+"\n"
                    list_print.append(st)
                else:
                  error_print.append(f"Variables not declared or Use of undefined variables in line no. { l.index(mylist)+len(var_val)+1}\n")
            

        elif mylist[0]=="st":
            reg_a= mylist[1]
            var_name= mylist[2]
            if reg_a not in reg :
              error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
            else:
              if var_name in var_val:
                var_val[var_name]=reg_val[reg_a]
                st2=opcodess["st"]+"0"+reg_codes[reg_a]+var_address[var_name]
                st=st2+"\n"
                list_print.append(st)
                reg_val[reg_a]=0
              else:
                error_print.append(f"Variables not declared or Use of undefined variables in line no. { l.index(mylist)+1+len(var_val)}\n")
        elif mylist[0]=="rs":
            reg_a= mylist[1]
            if reg_a not in reg:
              error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
            else:
              dol=mylist[2][0]
              if dol=="$":
                if 0<=int(mylist[2][1:])<=127:
                  im_val= dectobinary( int(mylist[2][1:]))
                  reg_val[reg_a]= reg_val[reg_a]>>int(mylist[2][1:])
                  st2=opcodess["rs"]+"0"+reg_codes[reg_a]+im_val
                  st=st2+"\n"
                  list_print.append(st)
                else:
                  error_print.append(f"Illegal Immediate values (more than 7 bits) in  line no. { l.index(mylist)+1+len(var_val)}\n")
              else:
                error_print.append(f"General Syntax Error in  line no. { l.index(mylist)+1+len(var_val)}\n")
              

        elif mylist[0]=="ls":
            reg_a= mylist[1]
            if reg_a not in reg :
              error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
            else:
              dol=mylist[2][0]
              if dol=="$": 
                if 0<=int(mylist[2][1:])<=127:
                  im_val= dectobinary( int(mylist[2][1:]))
                  reg_val[reg_a]= reg_val[reg_a]<<int(mylist[2][1:])
                  st2=opcodess["ls"]+"0"+reg_codes[reg_a]+im_val
                  st=st2+"\n"
                  list_print.append(st)
                else:
                  error_print.append(f"Broken Immediate values (more than 7 bits) in  line no. { l.index(mylist)+1+len(var_val)}\n")
              else:
                error_print.append(f"Syntax Error in  line no. { l.index(mylist)+1+len(var_val)}\n")
        elif mylist[0]=="not":
            reg_a=mylist[1]
            reg_b=mylist[2]
            if reg_a not in reg or reg_b not in reg:
              error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
            else:
              reg_val[reg_a]=binarytodec(invert(dectobinary(reg_val[reg_b])))
              st2= opcodess["not"]+"00000"+reg_codes[reg_a]+reg_codes[reg_b]
              st=st2+"\n"
              list_print.append(st)
              reg_val[reg_a]=0

        elif mylist[0]=="cmp":
            reg_a=mylist[1]
            reg_b=mylist[2]
            if reg_a not in reg or reg_b not in reg:
              error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
            else:
              st2= opcodess["cmp"]+"00000"+reg_codes[reg_a]+reg_codes[reg_b]
              st=st2+"\n"
              list_print.append(st)
          
        elif mylist[0]=="jmp":
            
            lab_name=mylist[1]
            if lab_name in mem_address:
              st2= opcodess["jmp"]+"0000"+mem_address[lab_name]
              st=st2+"\n"
              list_print.append(st)
            else:
              error_print.append(f"Use of undefined labels in line no. { l.index(mylist)+1+len(var_val)}\n")

        elif mylist[0]=="jlt":
            lab_name=mylist[1]
            if lab_name in mem_address:
              st2= opcodess["jlt"]+"0000"+mem_address[lab_name]
              st=st2+"\n"
              list_print.append(st)
            else:
              error_print.append(f"Use of undefined labels in line no. { l.index(mylist)+1+len(var_val)}\n")
            

        elif mylist[0]=="jgt":
            lab_name=mylist[1]
            if lab_name in mem_address:
              st2= opcodess["jgt"]+"0000"+mem_address[lab_name]
              st=st2+"\n"
              list_print.append(st)
            else:
              error_print.append(f"Use of undefined labels in line no. { l.index(mylist)+1+len(var_val)}\n")

        elif mylist[0]=="je":
            lab_name=mylist[1]
            if lab_name in mem_address:
              st2= opcodess["je"]+"0000"+mem_address[lab_name]
              st=st2+"\n"
              list_print.append(st)
            else:
              error_print.append(f"Use of undefined labels in line no. { l.index(mylist)+1+len(var_val)}\n")

        elif mylist[0]=="hlt":
            st2=opcodess["hlt"]+"00000000000"
            st=st2+"\n"
            list_print.append(st)
            hlt_check=1
            break
        elif mylist[0]=="var":
          break
        else:
          error_print.append(f"Wrong instruction name or register name in line no. { l.index(mylist)+1+len(var_val)}\n")
          break
          

    if hlt_check==0:
        error_print.append(f"Missing halt instruction\n")

  except:
    error_print.append(f"General syntax error on line { l.index(mylist)+1+len(var_val)}\n")
if len(error_print)==0:
  if len(list_print)>127:
    final_list=list_print[:128]
  else:
    final_list=list_print 
    for kx in final_list:
        sys.stdout.write(kx)
else:

    sys.stdout.write(error_print[0])

print(error_print)
l=0
