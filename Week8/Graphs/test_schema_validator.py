import unittest
from schema_validator import *


class TestEqualizeListFunction(unittest.TestCase):

    def test_returns_correctly_list_of_values(self):
        schema = [
            'key1',
            'key2',
            [
                'key3',
                ['inner_key1', 'inner_key2']
            ]
        ]

        expected = ['key1', 'key2', 'key3', 'inner_key1', 'inner_key2']
        result = equalize_list(schema)

        self.assertEqual(result, expected)

    def test_correctly_returns_empty_list(self):
        schema = []
        expected = []
        result = equalize_list(schema)

        self.assertEqual(result, expected)


class TestEqualizeDictFunction(unittest.TestCase):

    def test_returns_correctly_list_of_values(self):
        data = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            }
        }

        expected = ['key1', 'key2', 'key3', 'inner_key1', 'inner_key2']
        result = equalize_dict(data)

        self.assertEqual(result, expected)

    def test_correctly_returns_empty_list(self):
        data = {}
        expected = []
        result = equalize_dict(data)

        self.assertEqual(result, expected)


class TestSchemaValidatorFunction(unittest.TestCase):

    def test_raises_exception_when_schema_is_not_list(self):
        with self.assertRaises(TypeError):
            schema_validator(1, {})

    def test_raises_exception_when_data_is_not_dict(self):
        with self.assertRaises(TypeError):
            schema_validator([], 1)

    def test_returns_true_when_schema_and_data_are_valid(self):
        schema = [
            'key1',
            'key2',
            [
                'key3',
                ['inner_key1', 'inner_key2']
            ]
        ]

        data = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            }
        }

        self.assertEqual(True, schema_validator(schema, data))

    def test_returns_false_when_schema_and_data_are_not_valid(self):
        schema = [
            'key1',
            'key2',
            [
                'key3',
                ['inner_key1', 'inner_key2']
            ]
        ]

        data = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            },
            'key4': 'val1'
        }

        self.assertEqual(False, schema_validator(schema, data))


if __name__ == '__main__':
    unittest.main()
