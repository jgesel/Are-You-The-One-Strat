#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import random
from scipy.special import comb
import math

NUM_PLAYERS = 10


# In[5]:


match_prob = np.ones([NUM_PLAYERS, NUM_PLAYERS])/NUM_PLAYERS
match_prob


# In[20]:


def generate_matches():
    l = list(range(NUM_PLAYERS))
    random.shuffle(l)
    return l

m = generate_matches()
print(m)


# In[35]:


def countDer(n): 
      
    # Base cases 
    if (n == 1): return 0
    if (n == 0): return 1
    if (n == 2): return 1
      
    # countDer(n) = (n-1)[countDer(n-1) + der(n-2)] 
    return (n - 1) * (countDer(n - 1) + 
                      countDer(n - 2)) 
  
def p_number_lights_on(n, total_players):
    der = countDer(total_players - n)
    right_com = comb(total_players, n, exact=True)
    return (der*right_com)/math.factorial(total_players)

def calc_prob_match(n, prev, players_left):
    p_lights_on = p_number_lights_on(n,players_left)
    p_lights_on_match = p_number_lights_on(n-1,players_left-1)
    return (p_lights_on_match*prev)/p_lights_on

def update_prob(n, prev, players_left, match):
    old_match_prob = prev[match]
    new_match_prob = calc_prob_match(n, old_match_prob, players_left)
    change = 1/(new_match_prob/old_match_prob)
    new_prob = prev * change
    new_prob[match] = new_match_prob
    return new_match_prob

    
    
    


# In[37]:




