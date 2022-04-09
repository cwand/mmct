import mmct
import time
import numpy as np

t0 = time.time()

tx = mmct.tester()
tx.n_samples = 30000

p1 = tx.do_test(
	np.array([0, 0, 2, 4, 5, 2, 3, 1, 0, 1, 2]),
	np.array([1 / 36, 2 / 36, 3 / 36, 4 / 36, 5 / 36, 6 / 36, 5 / 36, 4 / 36, 3 / 36, 2 / 36, 1 / 36]))
print(f'Calculated p-value: {p1:.3f}')

t1 = time.time()


print('')
print("Time: {:.4f}s".format(t1 - t0))
