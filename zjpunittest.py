# -*- coding: utf-8 -*-
import unittest
import fun

class Test_function(unittest.TestCase):

    def test01(self):
        a,b=5,6
        res=fun.add(a,b)
        self.assertEqual(res,11)

    def test02(self):
        a,b=2,3
        res=fun.multiply(a,b)
        self.assertEqual(res,5)

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Test_function)
    runner=unittest.TextTestRunner()
    runner.run(suite)
