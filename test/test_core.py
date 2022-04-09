import unittest
import numpy as np

import mmct


class TestTester(unittest.TestCase):

	def test_tester_do_test_params(self):
		t = mmct.tester()
		t.n_samples = 200
		t.statistics = np.zeros(80)

		x = np.array([3, 4, 5, 6])
		t.do_test(x, np.array([0.2, 0.25, 0.3, 0.25]))

		self.assertEqual(t.statistics.size, 200)

	def test_tester_do_test_no_rerun_when_fixed(self):
		t = mmct.tester()
		t.n_samples = 4

		x = np.array([3, 4, 5, 6])

		t.do_test(x, np.array([0.2, 0.25, 0.3, 0.25]))

		# Set artificial and impossible statistics. If generate_samples is run, these
		# values will be overwritten, since they cannot occur mathematically
		t.statistics = np.array([10, 12, 14, 16])

		t.fix = True

		y = np.array([6, 5, 4, 3])

		t.do_test(y, np.array([0.2, 0.25, 0.3, 0.25]))

		self.assertEqual(t.statistics.size, 4)
		self.assertEqual(t.statistics[0], 10)
		self.assertEqual(t.statistics[1], 12)
		self.assertEqual(t.statistics[2], 14)
		self.assertEqual(t.statistics[3], 16)

	def test_tester_do_test_pvalue(self):
		t = mmct.tester()
		t.n_samples = 5

		x = np.array([1, 3, 1, 3])  # Prob = 0.0189
		t.do_test(x, np.array([0.05, 0.6, 0.1, 0.25]))

		# null prob: [0.05,0.6,0.1,0.25]
		# Sample 0: [0,4,2,2]			Prob = 0.03402
		# Sample 1: [1,5,2,0]			Prob = 0.00653184
		# Sample 2: [0,3,2,3]			Prob = 0.0189
		# Sample 3: [0,6,2,0]			Prob = 0.01306368
		# Sample 4: [1,1,5,1]			Prob = 0.0000252
		t.statistics = np.array([0.03402, 0.00653184, 0.0189, 0.01306368, 0.0000252])
		t.fix = True

		p = t.do_test(x, np.array([0.05, 0.6, 0.1, 0.25]))

		self.assertEqual(p, 0.8)

		x = np.array([8, 0, 0, 0])  # Prob = 3.90625 × 10^-11
		p = t.do_test(x, np.array([0.05, 0.6, 0.1, 0.25]))

		self.assertEqual(p, 0.0)

		x = np.array([1, 2, 2, 3])  # Prob = 0.004725
		p = t.do_test(x, np.array([0.05, 0.6, 0.1, 0.25]))

		self.assertEqual(p, 0.2)

	def test_tester_do_test_error_x_probs_not_same_dim(self):
		t = mmct.tester()
		x = np.array([3, 4, 5])
		p = np.array([0.3, 0.6, 0.05, 0.05])
		self.assertRaises(ValueError, t.do_test, x, p)


class TestMTTester(unittest.TestCase):

	def test_mttester_do_test_params(self):
		t = mmct.mt_tester()
		t.n_samples = 200
		t.statistics = np.zeros(80)

		x = np.array([3, 4, 5, 6])
		t.do_test(x, np.array([0.2, 0.25, 0.3, 0.25]))

		self.assertEqual(t.statistics.size, 200)
