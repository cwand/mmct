import numpy as np

# Monte Carlo utility functions

def get_multinom(c_prob,rs):

  res = np.zeros(c_prob.size)

  for r in rs:
    i = 0
    while r >= c_prob[i]:
      i += 1
    res[i] += 1

  return res
