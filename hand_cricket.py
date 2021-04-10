n=input('please enter your name:')
s=''
import random as r
k=l=g=m=0
################################toss
y=None
while y!='h' or y!='heads' or y!='t' or y!='tails':
  y=input('choose heads or tails (h/t) for toss:')
  if y=='h' or y=='heads' or y=='t' or y=='tails':
    break
  print("input doesn't exists.....    Enter again")
print('______________________________________________\n')
############################################ bat or bowl
d=r.randint(1,2)
if d==1:
  d="bat"
elif d==2:
  d="bowl"
########################################
o=r.randint(1,2)
if o==1:
  o="h"
elif o==2:
  o="t"
############################################
if y==o:
  print(n,'have won the toss.....')
  s=input('choose bat/bowl:')
else:
  print('computer have won the toss.....')
  print('computer has choosen',d)
#################################################
def innings1():
  print('______________________________________________\n')
  def bat():
    p=r.randint(1,6)
    global k
    global l
    while k!=p:
      k=input('your turn:')
      while(k>'6' or k<'1'):
        k=input('please enter a number between 1-6:')
        if k.isdigit() and (k<='6' and k>='1'):
          k=int(k)
          break
      else:
        k=int(k)
      p=r.randint(1,6)
      print('computer turn:',p,sep='')
      if k==p:
        print(n," scored:",l,sep='')
        break
      l+=k
  bat()
  print('______________________________________________\n')
  print('computer is batting now...')
  print('______________________________________________\n')
  def bowl():
    p=r.randint(1,6)
    global g
    global m
    global l
    while g!=p and m<=l:
      g=input('your turn:')
      while (g>'6' or g<'1'):
        g=input('please enter a number between 1-6:')
        if g.isdigit() and (g<='6' and g>='1'):
          g=int(g)
          break
      else:
        g=int(g)
      p=r.randint(1,6)
      print('computer turn:',p,sep='')
      if g==p:
        print("computer scored:",m,sep='')
        break
      m+=p
  bowl()
  print('______________________________________________\n')
#########################################################
def innings2():
  print('______________________________________________\n')
  def bowl():
    p=r.randint(1,6)
    global g
    global m
    while g!=p:
      g=input('your turn:')
      while (g>'6' or g<'1'):
        g=input('please enter a number between 1-6:')
        if g.isdigit() and (g<='6' and g>='1'):
          g=int(g)
          break
      else:
        g=int(g)
      p=r.randint(1,6)
      print('computer turn:',p,sep='')
      if g==p:
        print("computer scored:",m,sep='')
        break
      m+=p
  bowl()
  print('______________________________________________\n')
  print('you are batting now...')
  print('______________________________________________\n')
  def bat():
    p=r.randint(1,6)
    global k
    global l
    global m
    while k!=p and l<=m:
      k=input('your turn:')
      while (k>'6' or k<'1'):
        k=input('please enter a number between 1-6:')
        if k.isdigit() and (k<='6' and k>='1'):
          k=int(k)
          break
      else:
        k=int(k)
      p=r.randint(1,6)
      print('computer turn:',p,sep='')
      if k==p:
        print(n," scored:",l,sep='')
        break
      l+=k
  bat()
  print('______________________________________________\n')
############################################
if s=='bat' or d=='bowl':
  print(n,'is batting now...')
  innings1()
elif s=='bowl' or d=='bat':
  print('computer is batting now...')
  innings2()
elif s!='bat' and s!='bowl':
  print(n,'has choosen wrong\ncomputer is batting now...')
  innings2()
##################################################
if l>m:
  print(n,'wins by',l-m,'runs')
elif l<m:
  print('computer wins by',m-l,'runs')
elif l==m:
  print('match draws between',n,'and computer')
