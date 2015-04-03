#!/bin/env python

import unittest

from dicto import dicto


class DictoTest(unittest.TestCase):

    def setUp(self):

        # make normal dict
        self.value = {
            'one': 1,
            'two': 2,
            'hello': 'world',
            'tlist': [1, 2, 3],
            'tdict': {
                '1': 'one',
                '2': 'two',
            }
        }

        # make dicto 1 using attributes
        self.d1 = dicto()
        self.d1.one = 1
        self.d1.two = 2
        self.d1.hello = 'world'
        self.d1.tlist = list([1, 2, 3])
        self.d1.tdict = dict({'1': 'one', '2': 'two'})

        # make dicto 2 using dict
        self.d2 = dicto(self.value)

    def test_int_one_from_attribute(self):
        self.assertEqual(1, self.d1.one)
        self.assertEqual(1, self.d1['one'])
        self.assertEqual(self.d1.one, self.d1['one'])

    def test_int_one_from_dict(self):
        self.assertEqual(1, self.d2.one)
        self.assertEqual(1, self.d2['one'])
        self.assertEqual(self.d2.one, self.d2['one'])

    def test_int_two_from_attribute(self):
        self.assertEqual(2, self.d1.two)
        self.assertEqual(2, self.d1['two'])
        self.assertEqual(self.d1.two, self.d1['two'])

    def test_int_two_from_dict(self):
        self.assertEqual(2, self.d2.two)
        self.assertEqual(2, self.d2['two'])
        self.assertEqual(self.d2.two, self.d2['two'])

    def test_compare_dict_to_dicto_from_attribute(self):
        self.assertEqual(self.value, self.d1)

    def test_compare_dict_to_dicto_from_dict(self):
        self.assertEqual(self.value, self.d2)


if __name__ == '__main__':
    import sys

    suite = unittest.TestSuite()

    if len(sys.argv) == 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(
            DictoTest
        )
    else:
        for test_name in sys.argv[1:]:
            suite.addTest(
                DictoTest(test_name)
            )

    unittest.TextTestRunner(verbosity=2).run(suite)
