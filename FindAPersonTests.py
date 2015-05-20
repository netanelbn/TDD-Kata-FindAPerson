import unittest
from Crowdmap import Crowdmap
class FindAPersonTests(unittest.TestCase):
	def setUp(self):
		self.crowdmap = Crowdmap(["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley", "Missing Cowboy"])
			def test_getAllPostsForName(self):
		posts = self.crowdmap.get_all_posts_for("Or")
		self.assertEquals(posts,["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"])
		
	def test_getAllPostForMissingName(self):
		posts = self.crowdmap.get_all_posts_for("Joe")
		self.assertEquals([],posts)
		