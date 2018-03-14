import unittest
import guess_game

class test_guess_game(unittest.TestCase):
    """
    Test Suite for MDA App
    """

    """
    UNTESTED! Cleaning code for Questions Function 0,5,10 scores
    """
    def limit_number_questions(self):
        """
        Test to check whether 10 awarded for correct answers 
        """
        self.assertEqual(guess_game.limit_number_questions(3, 23), 10)
        self.assertNotEqual(guess_game.limit_number_questions("hello", 23), 10)
        self.assertNotEqual(guess_game.limit_number_questions("&%$", 3), 10)
        self.assertNotEqual(guess_game.limit_number_questions(32, 3), 10)
      
    # def limit_number_questions_5(self):
    #     """
    #     Test to check whether 5 awarded for answers which are within range of  
    #     10 lower or higher than answer
    #     """
    #     self.assertEqual(guess_game.limit_number_questions("rt", 30), 5)
    #     self.assertEqual(guess_game.limit_number_questions(39, 30), 5)
    #     self.assertNotEqual(guess_game.limit_number_questions("hello", 30), 5)    
    
    # def limit_number_questions_0(self):
    #     """
    #     Test to check whether 0 awarded for incorrect and invalid answers
    #     """
    #     self.assertEqual(guess_game.limit_number_questions(19, 30), 0)
    #     self.assertEqual(guess_game.limit_number_questions(41, 30), 0)
    #     self.assertEqual(guess_game.limit_number_questions("hello", 30), 0)
    #     self.assertEqual(guess_game.limit_number_questions(-1, 30), 0)
    

        

if __name__ == '__main__':
    unittest.main()
    
