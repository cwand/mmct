import unittest
import numpy as np

import mmct

class TestTester(unittest.TestCase):

  def test_tester_run_trials(self):
    t = mmct.tester()
    t.n_trials = 10
    t.run_trials()
    self.assertEqual(t.statistics.size,10)
