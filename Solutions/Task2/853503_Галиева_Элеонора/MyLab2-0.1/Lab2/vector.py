import math


class Nvector:
    vector = []

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, other):
        if not isinstance(other, Nvector):
            raise TypeError("Wrong type for that operation.")
        if len(self.vector) != len(other.vector):
            raise Exception("Vectors must have same length.")
        result = list(map(lambda x, y: x + y, self.vector, other.vector))
        return result

    def __sub__(self, other):
        if not isinstance(other, Nvector):
            raise TypeError("Wrong type for that operation.")
        if len(self.vector) != len(other.vector):
            raise Exception("Vectors must have same length.")
        result = list(map(lambda x, y: x - y, self.vector, other.vector))
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = list(map(lambda x: x * other, self.vector))
        elif isinstance(other, Nvector):
            result = list(map(lambda x, y: x * y, self.vector, other.vector))
        else:
            raise TypeError("Wrong type for that operation.")
        return result

    def __eq__(self, other):
        if not isinstance(other, Nvector):
            raise TypeError("Wrong type for that operation.")
        if len(self.vector) != len(other.vector):
            raise Exception("Vectors must have same length.")
        if self.__len__() != other.__len__():
            return False
        else:
            return True

    def __len__(self):
        return float(math.sqrt(sum(x ** 2 for x in self.vector)))

    def get(self, index):
        if index >= len(self.vector):
            raise IndexError("Index out of range.")
        else:
            return self.vector[index]

    def scalar_product(self, other, alpha):
        if not isinstance(other, Nvector):
            raise TypeError("Wrong type for that operation.")
        return self.__len__() * other.__len__() * math.cos(alpha)

    def __str__(self):
        result = ""
        for x in self.vector:
            result += "{} ".format(x)
        return result[:-1]


