import unittest
from createSpiral import createSpiral

class TestCreateSpiral(unittest.TestCase):
    def testCreateSpiralFunction(self):
        '''
        This tests the basic functionality of createSpiral given
        correct parameters.
        '''
        output = createSpiral(0)
        assert output == []

        output = createSpiral(1)
        assert output == []

        output = createSpiral(3)
        assert output == [[1,2,3],[8,9,4],[7,6,5]]

        output = createSpiral(4)
        assert output == [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

        output = createSpiral(5)
        assert output == [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
    
    def testCreateSpiralInvalidArguments(self):
        '''
        This tests that the function terminates correctly
        given incorrect parameters.
        '''
        with self.assertRaises(SystemExit) as se:
            createSpiral("a")

        self.assertEqual(se.exception.code, -1)

        with self.assertRaises(SystemExit) as se:
            createSpiral("1.3")

        self.assertEqual(se.exception.code, -1)

        with self.assertRaises(SystemExit) as se:
            createSpiral(1.3)

        self.assertEqual(se.exception.code, -1)

        with self.assertRaises(SystemExit) as se:
            createSpiral(-1)

        self.assertEqual(se.exception.code, -1)

if __name__ == '__main__':
    unittest.main()