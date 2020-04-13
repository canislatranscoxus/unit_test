'''
usage:  $ python dynamic_test_classes.py -v


references: https://eli.thegreenplace.net/2014/04/02/dynamically-generating-python-test-cases
'''

import unittest

class DynamicClassBase(unittest.TestCase):
    longMessage = True

def make_test_function(description, a, b):
    def test(self):
        self.assertEqual(a, b, description)
    return test

if __name__ == '__main__':
    testsmap = {
        'foo': [1, 1],
        'bar': [1, 2],
        'baz': [5, 5]}

    for name, params in testsmap.items():
        test_func = make_test_function(name, params[0], params[1])
        klassname = 'Test_{0}'.format(name)
        globals()[klassname] = type(klassname,
                                   (DynamicClassBase,),
                                   {'test_gen_{0}'.format(name): test_func})

    unittest.main()