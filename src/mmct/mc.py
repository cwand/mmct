import numpy as np

# Monte Carlo utility functions

def get_multinom_obs(prob,r):

  i = 0
  c_prob = prob[0]
  while c_prob <= r:
    i += 1
    c_prob += prob[i]
  return i
