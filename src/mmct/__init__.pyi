import numpy as np
import numpy.typing as npt
from multiprocessing import Pool


class tester:

	n_samples: int
	statistics: npt.NDArray[np.float_]

	fix: bool

	def generate_sample_stat(self, index: int) -> float: ...

	def mc_runs(self, n_obs: int, probs: npt.NDArray[np.float_]) -> None: ...

	def do_test(self,
		x: npt.NDArray[np.int_], probs: npt.NDArray[np.float_]) -> float: ...
