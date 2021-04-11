
import unittest
import numpy as np

import mmct.mc as mc

class TestGetMultinomObs(unittest.TestCase):

  def test_2d(self):
    self.assertEqual(0,mc.get_multinom_obs([0.3,0.7],0.29))
    self.assertEqual(1,mc.get_multinom_obs([0.6,0.4],0.60))
    self.assertEqual(1,mc.get_multinom_obs([0.98,0.02],0.99))

  def test_3d(self):
    self.assertEqual(0,mc.get_multinom_obs([0.3,0.05,0.65],0.29))
    self.assertEqual(1,mc.get_multinom_obs([0.3,0.05,0.65],0.32))
    self.assertEqual(2,mc.get_multinom_obs([0.3,0.05,0.65],0.36))
