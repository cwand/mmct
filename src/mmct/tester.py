import numpy as np
import random

from . import stat

# Generate a ultinomially distributed set of observations

def get_multinom(c_prob,rs):

  res = np.zeros(c_prob.size)

  for r in rs:
    # TODO: binary search since c_prob should be increasing
    i = 0
    while r >= c_prob[i]:
      i += 1
    res[i] += 1

  return res


# Main class used for performing multinomial tests

class tester:

	n_trials = 1000
	statistics = np.zeros(1)
	fix = False

	def run_trials(self, probs, n):
		# First, generate a cumulative sum of the probabilities in ps
		cps = np.zeros(probs.size)
		cps[0] = probs[0]
		for i in range(1,probs.size):
			cps[i] = cps[i-1] + probs[i]

		# Generate n_trials samples from the underlying distribution of ps
		self.statistics = np.zeros(self.n_trials)
		for i in range(0,self.n_trials):

			# Each distribution need n observations
			rs = np.zeros(n)
			# Generate n_obs random numbers in [0,1)
			for j in range(0,n):
				rs[j] = random.random()

			# Generate a multinomial draw from the probabilities in ps (using cps)
			m = get_multinom(cps,rs)

			# Calculate test statistic
			self.statistics[i] = stat.multinomialLLR(m,probs)


	def do_test(self, x, probs):

		if x.size != probs.size:
			raise ValueError('Input arrays must have the same number of elements')


		# Run trials
		self.run_trials(probs, np.sum(x))

		# Calculate statistic of x
		x_stat = stat.multinomialLLR(x, probs)

		# Count number of trials with statistic smaller than x
		n_smaller = 0
		for s in self.statistics:
			if s <= x_stat:
				n_smaller += 1
		return n_smaller/self.statistics.size
