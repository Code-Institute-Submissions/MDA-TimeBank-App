import unittest
import guess_game

class test_guess_game(unittest.TestCase):
    """
    Test Suite for MDA App
    """
    
    """
    Quetions_Answers Function
    """
    
    def test_ask_questions(self):
        """
        Test to check whether 10 awarded for correct answers 
        """
        self.assertEqual(guess_game.ask_questions(23, 23), 10)
        self.assertNotEqual(guess_game.ask_questions("hello", 23), 10)
        self.assertNotEqual(guess_game.ask_questions("&%$", 3), 10)
        self.assertNotEqual(guess_game.ask_questions(32, 3), 10)
      
    def test_questions_scores_5(self):
        """
        Test to check whether 5 awarded for answers which are within range of  
        10 lower or higher than answer
        """
        self.assertEqual(guess_game.ask_questions(23, 30), 5)
        self.assertEqual(guess_game.ask_questions(39, 30), 5)
        self.assertNotEqual(guess_game.ask_questions("hello", 30), 5)    
    
    def test_questions_scores_0(self):
        """
        Test to check whether 0 awarded for incorrect and invalid answers
        """
        self.assertEqual(guess_game.ask_questions(19, 30), 0)
        self.assertEqual(guess_game.ask_questions(41, 30), 0)
        self.assertEqual(guess_game.ask_questions("hello", 30), 0)
        self.assertEqual(guess_game.ask_questions(-1, 30), 0)

if __name__ == '__main__':
    unittest.main()
    
