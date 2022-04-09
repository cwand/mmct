import numpy as np
import numpy.typing as npt
from multiprocessing import Pool

# Main class used for performing multinomial tests

class tester:

	n_samples: int  # The number of Monte Carlo samples to generate
	statistics: npt.NDArray[np.float_]  # Test statistics of random samples

	# The test statistics can be fixed by setting fix to True. This prevents
	# rerunning the Monte Carlo sampling when running a new test. This can
	# be useful when testing or to save time (bias danger!)
	fix: bool

	def generate_sample_stat(self, index: int) -> float: ...

	def mc_runs(self) -> None: ...

	def do_test(self,
		x: npt.NDArray[np.int_], probs: npt.NDArray[np.float_]) -> float: ...



# Derived class from tester that uses multithreading to speed up the monte carlo
# sampling

class mt_tester(tester):

	# Number of threads to use. If None, the system default is used
	# (typically the number of logical processors)
	threads: int
