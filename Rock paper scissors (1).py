#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


def gamewin(comp, you):
    #if two values are equal match is tie
    if comp==you:
        return None
    
    #Check the the possibilities
    
    elif comp=='Rock':
        if you=="Scissor":
            return False
        elif you=="Paper":
            return True
    
    elif comp=='Paper':
        if you=="Scissor":
            return True
        elif you=="Rock":
            return False
    
    elif comp=='Scissor':
        if you=="Paper":
            return False
        elif you=="Rock":
            return True
        
        
print("comp turn:Rock, Paper, Scissor ?")
randno = random.randint(1,3)
if randno==1:
    comp="Rock"
elif randno==2:
    comp="Paper"
elif randno==3:
    comp='Scissor'
            
you= input("Your turn::Rock, Paper, Scissor")
a = gamewin(comp, you)
        
print(f" computer chose {comp}")
print(f" you chose {you}")
        
        
if a==None:
    print("Game is tie")
elif a:
    print("you won")
else:
    print("You lose")


# In[ ]:




