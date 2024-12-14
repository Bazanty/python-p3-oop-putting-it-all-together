import io
import sys
from shoe import Shoe

class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        shoe = Shoe("Nike", 42)
        assert shoe.brand == "Nike"
        assert shoe.size == 42

    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        shoe = Shoe("Adidas", 40)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        shoe.size = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "size must be an integer\n"

    def test_can_cobble(self):
        '''outputs "Your shoe is as good as new!" when method cobble() is called'''
        shoe = Shoe("Puma", 44)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        shoe.cobble()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Your shoe is as good as new!\n"
