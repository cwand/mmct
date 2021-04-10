
import unittest
import sys, os

import mmct.util as util

class TestNormL1(unittest.TestCase):

	def test_test(self):
		self.assertEqual(1+1,util.normL1(1))
