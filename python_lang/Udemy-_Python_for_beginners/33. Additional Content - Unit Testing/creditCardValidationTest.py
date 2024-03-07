# creditCardValidationTest.py
import unittest
from creditCardValidation import * # import the functionality that you want to test

class creditCardValidationTest(unittest.TestCase):
    def test_validateCard_valid(self):
        result = validateCard(date(2029, 2, 2))
        self.assertEqual('Valid', result)

if __name__ == '__main__': # to invoke main() method in text editors where running tests is not supported
    # unittest.main()
    unittest.main(argv=[''], verbosity=2, exit=False)     # more verbosity
    # unittest.main(argv=[''], exit=False)    # for jupyter pass extra arguments