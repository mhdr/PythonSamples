from unittest import TestCase
from Math import Math

__author__ = 'Mahmood'


class TestMath(TestCase):
    def test_sum(self):
        math=Math()
        first= math.sum(1,2)
        second=3
        self.assertEqual(first,second)

    def test_sum2(self):
        math=Math()
        first= math.sum(1,2)
        second=4
        self.assertEqual(first,second)
