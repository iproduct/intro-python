from unittest.mock import MagicMock
import unittest

class ProductionClass:
    def method(self, *args, **kwargs):
        print(kwargs)
        return sum(args)

class WidgetTestCase(unittest.TestCase):
    def test_production_class_method(self):
        thing = ProductionClass()
        thing.method = MagicMock(return_value=3)
        self.assertEqual(3, thing.method(3, 4, 5, key='value'))
        thing.method.assert_called_with(3, 4, 5, key='value')
