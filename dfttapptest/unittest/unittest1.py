#coding=utf-8
import unittest
class simpleTest(unittest.TestCase):
    def setUp(self):
        print 'start test.....'

    def tearDown(self):
        print 'end test.....'

    def testsum(self):
        self.assertEqual(3,3,'sum test fail')

    def testsub(self):
        self.assertEqual(2,2, 'sub test fail')


if __name__ == '__main__':
#     suite=unittest.TestLoader().loadTestsFromTestCase(simpleTest)
#     unittest.TextTestRunner.verbosity(2).run(suite)
    unittest.main()
