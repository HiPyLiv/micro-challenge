import palindrome_checker
import unittest


class palindromes(unittest.TestCase):
    pals = ('LOL',
            'madam',
            "123454321",
            'hannah')

    
    def test_pals(self):
        for test in self.pals:
            self.assertTrue(palindrome_checker.is_palindrome(test), 
            "Your palindrome checker failed to spot a palindrome: " + test)

    def test_false(self):
        self.assertFalse(palindrome_checker.is_palindrome("Madam I'm Saddam."), 
        "Your palindrome checker gave a false positive.")

if __name__== '__main__':
    unittest.main()
