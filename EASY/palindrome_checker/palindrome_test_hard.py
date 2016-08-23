'''
This test file is a little harder to pass, but remember, if you've passed the easy test, you're already halfway
to passing the hard test! See if you can turn the hard case into an easy case.
'''

import palindrome_checker
import unittest


class palindromes(unittest.TestCase):
    pals = ('LOL',
            'Madam',
            "Madam I'm Adam",
            'As I pee, sir, I see Pisa!',
            'T. Eliot, top bard, notes putrid tang emanating, is sad. I’d assign it a name: gnat dirt upset on drab pot-toilet.',
            'Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.',
            "Dammit I'm mad.\nEvil is a deed as I live.\nDammit I'm mad.")

    
    def test_pals(self):
        for test in self.pals:
            self.assertTrue(palindrome_checker.is_palindrome(test), 
            "Your palindrome checker failed to spot a palindrome: " + test)

    def test_false(self):
        self.assertFalse(palindrome_checker.is_palindrome("Madam I'm Saddam."), 
        "Your palindrome checker gave a false positive.")

if __name__== '__main__':
    unittest.main()
