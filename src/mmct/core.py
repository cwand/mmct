from multiprocessing import Pool
import numpy as np
import numpy.typing as npt
from scipy.stats import multinomial


# Main class used for performing multinomial tests

class tester:

	n_samples = 1000  # The number of Monte Carlo samples to generate
	statistics = np.zeros(1)  # Test statistics of random samples

	# The test statistics can be fixed by setting fix to True. This prevents
	# rerunning the Monte Carlo sampling when running a new test. This can
	# be useful when testing or to save time (bias danger!)
	fix = False

	# Internal state objects
	__prob = np.ones(1)
	__n_obs = 0

	def generate_sample_stat(self, index: int) -> float:

		# The index argument is irrelevant but necessary to make Pool.map work

		# Generate a multinomial draw from hypothesised distribution
		m = multinomial.rvs(n=self.__n_obs, p=self.__prob, size=1)

		# Calculate test statistic
		y: float = multinomial.pmf(m, n=self.__n_obs, p=self.__prob)
		return y

	def mc_runs(self) -> None:
		# Reset statistics array
		self.statistics = np.zeros(self.n_samples)

		# Run Monte Carlo simulation:
		for i in range(0, self.n_samples):
			self.statistics[i] = self.generate_sample_stat(i)

	def do_test(self,
		x: npt.NDArray[np.int_], probs: npt.NDArray[np.float_]) -> float:

		if x.size != probs.size:
			raise ValueError('Input arrays must have the same number of elements')

		# Run samples if not fixed
		if not self.fix:

			self.__n_obs = np.sum(x)  # Total number of observations in x
			self.__prob = probs.copy()

			self.mc_runs()

		x_stat: float = multinomial.pmf(x, n=self.__n_obs, p=self.__prob)

		# Count number of trials with statistic smaller than x
		n_smaller = 0
		for s in self.statistics:
			if s <= x_stat:
				n_smaller += 1
		return n_smaller / self.statistics.size


# Derived class from tester that uses multithreading to speed up the monte carlo
# sampling

class mt_tester(tester):

	# Number of threads to use. If None, the system default is used
	# (typically the number of logical processors)
	threads = None

	def mc_runs(self) -> None:

		with Pool(processes=self.threads) as pool:
			res = pool.map(self.generate_sample_stat, range(0, self.n_samples))
		self.statistics = np.array(res)
