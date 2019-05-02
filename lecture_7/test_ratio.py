from unittest import TestCase
from ratio import *


class TestRatio(TestCase):
    def test___init__(self):
        self.assertTrue(Ratio(1, 1).denominator == 1)
        self.assertTrue(Ratio(-1, -1).denominator == 1)
        self.assertTrue(str(Ratio(1, 2)) == "1/2")
        self.assertTrue(str(Ratio(1, 1)) == "1")
        self.assertTrue(Ratio(1,2) == Ratio(1,2))
        self.assertTrue(str(Ratio(1, 2).expand(1)) == "1/2")
        self.assertTrue(str(Ratio(2, 6).reduce()) == "1/3")
        self.assertTrue(str(Ratio(1, 1) + Ratio(1, 1)) == "2")
        self.assertTrue(str(Ratio(1, 2) + Ratio(1, 3)) == "5/6")


