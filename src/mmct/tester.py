import numpy as np
import random

from . import mc
from . import stat

class tester:

  ps = np.ones(1)
  n_obs = 1
  n_trials = 1e5
  statistics = np.zeros(1)

  def run_trials(self):
    # First, generate a cumulative sum of the probabilities in ps
    cps = np.zeros(self.ps.size)
    cps[0] = self.ps[0]
    for i in range(1,self.ps.size):
      cps[i] = cps[i-1] + self.ps[i]

    # Generate n_trials samples from the underlying distribution of ps
    self.statistics = np.zeros(self.n_trials)
    for i in range(0,self.n_trials):

      # Each distribution need n_obs observations
      rs = np.zeros(self.n_obs)
      # Generate n_obs random numbers in [0,1)
      for j in range(0,self.n_obs):
        rs[j] = random.random()

      # Generate a multinomial draw from the probabilities in ps (using cps)
      m = mc.get_multinom(cps,rs)

      # Calculate test statistic
      self.statistics[i] = stat.multinomialLLR(m,self.ps)


  def do_test(self, x):
    return 1.0
