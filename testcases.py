import unittest

class TestClass(unittest.TestCase):

    @classmethod
    def  setUpClass(self):
        print('----setup class----')
    @classmethod
    def tearDownClass(self):
        print('-----tear down class----')

    def setUp(self):
        print('-----Setup----')

    def tearDown(self):
        print('----TearDown----')
    
    def test_Method1(self):
        #print('first')
        self.assertEqual(1,1)

    def test_Method2(self):
        #print('second')
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()

    