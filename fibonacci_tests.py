from unittest import TestCase, TestSuite, defaultTestLoader

from fibonacci_funcs import __multiply_m2x2 as multiply_m2x2, __pow_m2x2 as pow_m2x2, \
                            fibonacci_logn, fibonacci_n, is_non_negative_int


class TestMultipleM2x2(TestCase):
    def test_mul0(self):
        m1 = [
            [1, 4],
            [2, 3],
        ]

        m2 = [
            [0, 0],
            [0, 0],
        ]

        expected_result = [
            [0, 0],
            [0, 0],
        ]

        self.assertEqual(multiply_m2x2(m1, m2), expected_result)

    def test_mul1(self):
        m1 = [
            [1, 4],
            [2, 3],
        ]

        m2 = [
            [1, 0],
            [0, 1],
        ]

        expected_result = [
            [1, 4],
            [2, 3],
        ]

        self.assertEqual(multiply_m2x2(m1, m2), expected_result)

    def test_mul_other(self):
        m1 = [
            [42, 4],
            [56, 18],
        ]

        m2 = [
            [23, 2],
            [11, 54],
        ]

        expected_result = [
            [1010, 300],
            [1486, 1084],
        ]

        self.assertEqual(multiply_m2x2(m1, m2), expected_result)


class TestPowM2x2(TestCase):
    def test_exp0(self):
        matrix = [
            [234, 45],
            [22, 1],
        ]

        expected_result = [
            [1, 0],
            [0, 1],
        ]

        self.assertEqual(pow_m2x2(matrix, 0), expected_result)

    def test_exp1(self):
        matrix = [
            [4, 574],
            [22, 1],
        ]

        expected_result = [
            [4, 574],
            [22, 1],
        ]

        self.assertEqual(pow_m2x2(matrix, 1), expected_result)

    def test_exp2(self):
        matrix = [
            [4, 574],
            [22, 1],
        ]

        expected_result = [
            [12644, 2870],
            [110, 12629],
        ]

        self.assertEqual(pow_m2x2(matrix, 2), expected_result)

    def test_exp33(self):
        matrix = [
            [1, 4],
            [2, 3],
        ]

        expected_result = [
            [38805107275644938151041, 77610214551289876302084],
            [38805107275644938151042, 77610214551289876302083],
        ]

        self.assertEqual(pow_m2x2(matrix, 33), expected_result)


class TestFibonacciLogN(TestCase):
    def test_calc(self):
        self.assertEqual(fibonacci_logn(0), 0)
        self.assertEqual(fibonacci_logn(1), 1)
        self.assertEqual(fibonacci_logn(2), 1)
        self.assertEqual(fibonacci_logn(30), 832040)
        self.assertEqual(fibonacci_logn(100), 354224848179261915075)
        self.assertEqual(fibonacci_logn(297), 52461916524905785334311649958648296484733611329035169538240802)
        self.assertEqual(fibonacci_logn(500), 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125)

    def test_incorrect_param(self):
        with self.assertRaises(ValueError):
            fibonacci_logn(-10)
        with self.assertRaises(ValueError):
            fibonacci_logn(1.0)
        with self.assertRaises(ValueError):
            fibonacci_logn(False)
        with self.assertRaises(ValueError):
            fibonacci_logn(None)
        with self.assertRaises(ValueError):
            fibonacci_logn([])


class TestFibonacciN(TestCase):
    def test_calc(self):
        self.assertEqual(fibonacci_n(0), 0)
        self.assertEqual(fibonacci_n(1), 1)
        self.assertEqual(fibonacci_n(2), 1)
        self.assertEqual(fibonacci_n(30), 832040)
        self.assertEqual(fibonacci_n(100), 354224848179261915075)
        self.assertEqual(fibonacci_n(297), 52461916524905785334311649958648296484733611329035169538240802)
        self.assertEqual(fibonacci_n(500), 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125)

    def test_incorrect_param(self):
        with self.assertRaises(ValueError):
            fibonacci_n(-10)
        with self.assertRaises(ValueError):
            fibonacci_n(1.0)
        with self.assertRaises(ValueError):
            fibonacci_n(False)
        with self.assertRaises(ValueError):
            fibonacci_n(None)
        with self.assertRaises(ValueError):
            fibonacci_n([])


class TestIsNonNegativeInt(TestCase):
    def test_true(self):
        self.assertTrue(is_non_negative_int(0))
        self.assertTrue(is_non_negative_int(1000))

    def test_false(self):
        self.assertFalse(is_non_negative_int(-10))
        self.assertFalse(is_non_negative_int(1.0))
        self.assertFalse(is_non_negative_int(False))
        self.assertFalse(is_non_negative_int(None))
        self.assertFalse(is_non_negative_int([]))


def get_test_suite():
    test_cases = (TestMultipleM2x2, TestPowM2x2, TestFibonacciLogN, TestFibonacciN, TestIsNonNegativeInt)

    suite = TestSuite()
    for test_class in test_cases:
        tests = defaultTestLoader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    return suite
