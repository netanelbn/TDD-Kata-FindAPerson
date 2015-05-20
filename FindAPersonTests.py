import unittest
from Crowdmap import Crowdmap
class FindAPersonTests(unittest.TestCase):
	def setUp(self):
		self.crowdmap = Crowdmap(["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley", "Missing Cowboy"])
		