from unittest import TestCase, main
import doctest
from uheba_01 import lek25_doctest_unittest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(lek25_doctest_unittest))
    return tests

class TestDivisor(TestCase):
    def test_zero_raises(self):
        with self.assertRaises(ValueError):
            lek25_doctest_unittest.divide(10, 0)


if __name__ == '__main__':
    main()
