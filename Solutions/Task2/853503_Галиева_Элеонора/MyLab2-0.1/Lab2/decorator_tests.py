import unittest
from Lab2_folder.decorator import Memoized


@Memoized
def random_func(a, b):
    return a + b * b


@Memoized
def random_unhashable_func(dict):
    return dict


class TestDecorator(unittest.TestCase):

    def test(self):
        self.assertEqual(random_func(1, 2), 5)
        self.assertEqual(random_func(1, 2), 5)
        self.assertEqual(random_unhashable_func({1, 2}), {1, 2})


if __name__ == '__main__':
    unittest.main()
