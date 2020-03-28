import unittest
import json
from Lab2.to_json import to_json
from Lab2.from_json import from_json

STR = "EKME"
BOOL = ["TruE", True, False, "false", 1, 0]
OBJECT = {"home": [2, 3, "cat", "dog"]}

SIMPLE_DICT = "{\"name\": \"Ivan\", \"surname\": \"Ivanov\"}"
COMPLEX_DICT = "{\"name\": [\"Ivan\", 1, 2], \"surname\": \"Ivanov\"}"


class TestJsonMethods(unittest.TestCase):
    def test_str(self):
        self.assertEqual(to_json(STR), json.dumps(STR))

    def test_bool(self):
        self.assertEqual(to_json(BOOL), json.dumps(BOOL))

    def test_object(self):
        self.assertEqual(to_json(OBJECT), json.dumps(OBJECT))

    def test_for_error(self):
        with self.assertRaises(TypeError):
            to_json(self)

    def test_for_from_json_simple(self):
        self.assertEqual(from_json(SIMPLE_DICT), json.loads(SIMPLE_DICT))

    def test_for_from_json_complex(self):
        self.assertEqual(from_json(COMPLEX_DICT), json.loads(COMPLEX_DICT))


if __name__ == '__main__':
    unittest.main()