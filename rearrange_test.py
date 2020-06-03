#!/usr/bin/env python3
import  unittest
import rearrange

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelasce, Ada"
        expected = "Ada Lovelasce"
        self.assertEqual(rearrange.rearrange_name(testcase), expected)


    def test_emty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange.rearrange_name(testcase), expected)


    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange.rearrange_name(testcase), expected)

    def single(self):
        testcase = "Plato"
        expected = "Plato"
        self.assertEqual(rearrange.rearrange_name(testcase), expected)


unittest.main()
