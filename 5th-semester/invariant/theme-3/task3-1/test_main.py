import unittest
import main

class InstancesTest(unittest.TestCase):
    def test_instances(self):
        c = main.CurrencyInfo()
        self.assertIsInstance(c, main.CurrencyInfo)


    def test_instances_ids(self):
        ids = []
        for i in range(10):
            ids.append(id(main.CurrencyInfo()))
        self.assertEqual(ids.count(id(main.CurrencyInfo())), len(ids))


    def test_result_type(self):
        c = main.CurrencyInfo()
        self.assertIsInstance(c.get_currencies(), dict)