import unittest
import json
from Lab2_folder.to_json import to_json
from Lab2_folder.from_json import from_json

STR = "EKME"
BOOL = True
FLOAT = 1.123
NULL = None
BOOL_ARRAY = ["TruE", True, False, "false", 1, 0]
TUPLE_DICT = {(1, 2): "str"}
DICT = {1: "Ivan", 2: "Mark"}
DICT_ONLY_NUMS = {1: 2, 3: 4}
OBJECT = {"home": [2, 3, "cat", "dog"]}

SIMPLE_DICT = "{\"name\": \"Ivan\", \"surname\": \"Ivanov\"}"
COMPLEX_DICT = "{\"name\": [\"Ivan\", 1, 2], \"surname\": \"Ivanov\"}"
SIMPLE_LIST = "[\"TruE\", true, false, \"false\", 1, 0]"
ERROR_DICT_1 = "{{\"STR\": \"str\"}: 12}"
ERROR_DICT_2 = "{[\"STR\"]: 1}"
DOUBLE_LIST = "[[1, 2, 3], 4]"
DICT_IN_LIST = "[{\"STR\": true}, 12, 5, false]"


class TestJsonMethods(unittest.TestCase):
    # to json tests
    def test_str(self):
        self.assertEqual(to_json(STR), json.dumps(STR))

    def test_bool(self):
        self.assertEqual(to_json(BOOL), json.dumps(BOOL))

    def test_float(self):
        self.assertEqual(to_json(FLOAT), json.dumps(FLOAT))

    def test_none(self):
        self.assertEqual(to_json(NULL), json.dumps(NULL))

    def test_for_unhashable(self):
        with self.assertRaises(TypeError):
            to_json({[1, 2]: "STR"})

    def test_for_tuple(self):
        with self.assertRaises(TypeError):
            to_json(TUPLE_DICT)

    def test_for_dict(self):
        self.assertEqual(to_json(DICT), json.dumps(DICT))

    def test_for_dict_only_nums(self):
        self.assertEqual(to_json(DICT_ONLY_NUMS), json.dumps(DICT_ONLY_NUMS))

    def test_bool_array(self):
        self.assertEqual(to_json(BOOL_ARRAY), json.dumps(BOOL_ARRAY))

    def test_object(self):
        self.assertEqual(to_json(OBJECT), json.dumps(OBJECT))

    def test_for_error(self):
        with self.assertRaises(TypeError):
            to_json(self)

    # from json tests
    def test_simple_dict(self):
        self.assertEqual(from_json(SIMPLE_DICT), json.loads(SIMPLE_DICT))

    def test_complex_dict(self):
        self.assertEqual(from_json(COMPLEX_DICT), json.loads(COMPLEX_DICT))

    def test_expected_error(self):
        with self.assertRaises(TypeError):
            from_json(2)
        with self.assertRaises(TypeError):
            from_json(ERROR_DICT_1)
        with self.assertRaises(TypeError):
            from_json(ERROR_DICT_2)

    def test_simple_list(self):
        self.assertEqual(from_json(SIMPLE_DICT), json.loads(SIMPLE_DICT))

    def test_basic_type(self):
        self.assertEqual(from_json("3"), json.loads("3"))
        self.assertEqual(from_json("true"), json.loads("true"))
        self.assertEqual(from_json("false"), json.loads("false"))
        self.assertEqual(from_json("null"), json.loads("null"))

    def test_double_list(self):
        self.assertEqual(from_json(DOUBLE_LIST), json.loads(DOUBLE_LIST))

    def test_dict_in_list(self):
        self.assertEqual(from_json(DICT_IN_LIST), json.loads(DICT_IN_LIST))


if __name__ == '__main__':
    unittest.main()
