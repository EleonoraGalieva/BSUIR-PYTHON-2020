import Lab2.sort
from Lab2.vector import Nvector
from Lab2.from_json import from_json
from Lab2.to_json import to_json
from Lab2.singleton import Singleton


def task2():
    v1 = Lab2.vector.Nvector([1, 2])
    v2 = Lab2.vector.Nvector([3, 4])
    print(v1 + v1)
    print(v1 - v2)
    print(v1.__len__())


def task3():
    OBJECT = {"home": [2, 3, "cat", "dog"]}
    print(Lab2.to_json.to_json(OBJECT))


def task4():
    SIMPLE_DICT = "{\"name\": \"Ivan\", \"surname\": \"Ivanov\"}"
    print(Lab2.from_json.from_json(SIMPLE_DICT))


if __name__ == '__main__':
    print("Some tests from lab:")
    print("Sum, sub of vectors [1, 2] and [3, 4]. And len([1,2])")
    task2()
    print("To json")
    task3()
    print("From json")
    task4()
