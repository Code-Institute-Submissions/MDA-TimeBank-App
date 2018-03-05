import unittest
import guess_game

class test_guess_game(unittest.TestCase):
    """
    Test Suite for MDA App
    """
    
    """
    Max 2 guesses test_guess_game
    """
    def test_limit_number_questions(self):
        """
        Test to check can take three arguments (2 guesses, 1 answer), exit if
        guess correct on first attempt, and return 10 points
        """
        self.assertNotEqual(guess_game.limit_number_questions(32, 21, 59), 10)
        self.assertNotEqual(guess_game.limit_number_questions("Mum", 21, 59), 10)
        self.assertEqual(guess_game.limit_number_questions(59, 21, 59), 10)
        self.assertNotEqual(guess_game.limit_number_questions(21, 59, 59), 10)
       
        """
        Test to check can take three arguments (2 guesses, 1 answer), move to
        second correct guess if first incorrect, and return 8 points
        """
        self.assertNotEqual(guess_game.limit_number_questions(59, 32, 59), 8)
        self.assertNotEqual(guess_game.limit_number_questions(59, "Crazy", 59), 8)
        self.assertEqual(guess_game.limit_number_questions(32, 59, 59), 8)
        self.assertNotEqual(guess_game.limit_number_questions(59, 59, 59), 8)
        
        """
        Test to check if second guess within <10 or >10 returns 5 points
        """
        self.assertNotEqual(guess_game.limit_number_questions(59, 55, 59), 5)
        self.assertNotEqual(guess_game.limit_number_questions(6, 59, 59), 5)
        self.assertEqual(guess_game.limit_number_questions(6, 55, 59), 5)
        self.assertEqual(guess_game.limit_number_questions(6, 62, 59), 5)
        self.assertNotEqual(guess_game.limit_number_questions("%&", 70, 59), 5)
        
        """
        Test to check if second wrong guess returns 0 points
        """
        self.assertNotEqual(guess_game.limit_number_questions(3, 59, 59), 0)
        self.assertNotEqual(guess_game.limit_number_questions(59, 3, 59), 0)
        self.assertEqual(guess_game.limit_number_questions(3, 3, 59), 0)
        self.assertEqual(guess_game.limit_number_questions("Crazy", 3, 59), 0)

        

        

if __name__ == '__main__':
    unittest.main()
    
