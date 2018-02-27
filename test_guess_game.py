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
        Test to ensure username cannot be black
        """
        check_username = guess_game.check_username("Paul")
        self.assertNotEqual(len(check_username), 0)
        

if __name__ == '__main__':
    unittest.main()