import unittest
from nextVersion import nextVersion

class TestNextVersion(unittest.TestCase):
    def testNextVersionFunction(self):
        '''
        This tests the basic functionality of nextVersion given
        correct parameters.
        '''
        output = nextVersion("1.2.3")
        assert output == "1.2.4"

        output = nextVersion("0.9.9")
        assert output == "1.0.0"

        output = nextVersion("1")
        assert output == "2"

        output = nextVersion("1.2.3.4.5.6.7.8")
        assert output == "1.2.3.4.5.6.7.9"

        output = nextVersion("9.9")
        assert output == "10.0"

        output = nextVersion("99.9")
        assert output == "100.0"
    
    def testNextVersionInvalidArguments(self):
        '''
        This tests that the function terminates correctly
        given incorrect parameters.
        '''
        with self.assertRaises(SystemExit) as se:
            nextVersion(3)

        self.assertEqual(se.exception.code, -1)

        with self.assertRaises(SystemExit) as se:
            nextVersion("a")

        self.assertEqual(se.exception.code, -1)

        with self.assertRaises(SystemExit) as se:
            nextVersion("-1")

        self.assertEqual(se.exception.code, -1)

if __name__ == '__main__':
    unittest.main()