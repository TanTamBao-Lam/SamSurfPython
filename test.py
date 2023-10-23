import datetime
import surfshop
import unittest


class TestSurfShop(unittest.TestCase):
    """
    In your class, create a setup fixture that runs before every test.
    It should instantiate a new ShoppingCart object and assign it to an instance variable called self.cart.
    Your tests can then use self.cart to reference your instance of the ShoppingCart class.
    """

    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    """
    Test ShoppingCart.add_surfboards() with 1 as input for quantity and verify if the message is
    'Successfully added 1 surfboard to cart!'
    
    To do that, assertEqual() should be used as it compared two value and make sure they are equal.
    """

    def test_add_surfboards(self):
        message = self.cart.add_surfboards(quantity=1)
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

    """
    Test ShoppingCart.add_surfboards() with quantity = 2 as input.
    """

    def test_add_surfboards_with_2_as_input(self):
        message = self.cart.add_surfboards(quantity=2)
        self.assertEqual(message, f'Successfully added 2 surfboards to cart!')

    """
    Parameterize the test
    """

    def test_add_surfboards_parameterized(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

    """
    Test ShoppingCart.add_surfboards() with quantity = 5 as input.
    Should pass as exception is raised
    
    The test used assertRaises() to verify specific exception is raised by specific function 
    """

    @unittest.skip
    def test_too_many_boards_error_exception(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    """
    Test apply_locals_discount function
    
    assertTrue is used for method checks that passed argument to True.
    """

    # @unittest.expectedFailure
    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

    def test_invalid_checkout_date(self):
        current_date = datetime.datetime.now()
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, current_date)


if __name__ == '__main__':
    unittest.main()
