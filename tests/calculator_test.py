from unittest import TestCase, main
from uheba_01.lek23_unittest_coverage import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('3-1'), 2)

    def test_multi(self):
        self.assertEqual(calculator('2*2'), 4)

    def test_devide(self):
        self.assertEqual(calculator('10/2'), 5.0)

    def test_no_sings(self):
        with self.assertRaises(ValueError) as e:
            calculator('abrakadabra')
        self.assertEqual("Выражение должно содержать хотя бы один знак (+-/*)",
                         e.exception.args[0])

    def test_two_sings(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать 2 целые числа и 1 знак',
                         e.exception.args[0])


    def test_many_sings(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2*2')
        self.assertEqual('Выражение должно содержать 2 целые числа и 1 знак',
                         e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.2+2.2')
        self.assertEqual('Выражение должно содержать 2 целые числа и 1 знак',
                         e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Выражение должно содержать 2 целые числа и 1 знак',
                         e.exception.args[0])


if __name__ == '__main__':
    main()
