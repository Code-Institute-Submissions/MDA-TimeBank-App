import unittest
import guess_game

class test_guess_game(unittest.TestCase):
    """
    Test Suite for MDA App
    """
    def test_username_not_blank(self):
        """
        Test to detect if username is blank
        """
        username = guess_game.username("")
        self.assertNotEqual(len(username), 1)

    
    def test_check_username_is_valid(self):
        """
        Test to ensure username cannot be blank
        """
        validate_username = guess_game.validate_username("Mark123")
        self.assertNotEqual(len(validate_username), 0)


    def test_email_address_is_valid_length(self):
        """
        Test to ensure email address is a valid length (>=6)
        """
        email_address = guess_game.email_address("des@me.com")
        self.assertGreater(len(email_address), 5)


    # def test_email_address_is_valid_characters
        """
        Test to ensure email address includes '@' and '.'
        MANUAL TEST CARRIED OUT IN COMMAND LINE TO CHECK VALID
        EMAIL LOOP. WILL ONLY ENSURE >5 length, '@' and '.' in 
        any combination.
        """
        


if __name__ == '__main__':
    unittest.main()
    
