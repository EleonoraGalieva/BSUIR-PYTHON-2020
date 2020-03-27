import unittest
from Lab2.sort import sort_file
import random


def create_file(file_name):
    with open(file_name, "w") as f:
        f.writelines("{}\n".format(random.randint(-1000000, 1000000)) for _ in range(500000))


class TestSortMethods(unittest.TestCase):
    test_list = []

    def create_list(self, file_to_sort):
        with open(file_to_sort, "r") as f:
            for line in f:
                self.test_list.append(int(line))

    def compare(self, sorted_file):
        sorted_list = []
        with open(sorted_file, "r") as f:
            for line in f:
                sorted_list.append(int(line))
        if sorted_list == sorted(self.test_list):
            return True
        else:
            return False

    def test_sort(self):
        self.create_list("numbers.txt")
        sort_file("numbers.txt", "sorted_numbers.txt", 1000)
        self.assertTrue(self.compare("sorted_numbers.txt"))
        with self.assertRaises(FileNotFoundError):
            sort_file("nmbrs.txt", "sorted_numbers.txt", 1000)


if __name__ == '__main__':
    unittest.main()
