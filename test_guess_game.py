import unittest
import guess_game

class test_guess_game(unittest.TestCase):
    """
    Test Suite for MDA App
    """
    def test_username_not_blank(self):
        """
        Test to ensure username is not blank
        """
        username = guess_game.username("Mark123")
        self.assertNotEqual(len(username), 0)
    
    def test_username