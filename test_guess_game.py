import unittest
import guess_game

class test_guess_game(unittest.TestCase):
    """
    Test Suite for MDA App
    """
    
    """
    Register Function
    """
    
    def test_username_not_blank(self):
        """
        Test to detect if username is blank
        """
        self.assertNotEqual(guess_game.validate_username("Mark123"), 0)
        self.assertNotEqual(guess_game.validate_username("#%$"), 0)
        self.assertNotEqual(guess_game.validate_username("Mark"), 0)
        self.assertNotEqual(guess_game.validate_username("13"), 0)

    
    def test_check_username_is_valid(self):
        """
        Test to ensure username cannot be blank
        """
        validate_username = guess_game.validate_username("Mark123")
        self.assertNotEqual(guess_game.validate_username("000"), 0)
        self.assertNotEqual(guess_game.validate_username("&%$"), 0)
        self.assertNotEqual(guess_game.validate_username("MA"), 0)


    def test_email_address_is_valid_length(self):
        """
        Test to ensure email address is a valid length (>=6)
        """
        validate_email_address = guess_game.validate_email_address("des@me.com")
        self.assertGreater(len(validate_email_address), 5)


    # def test_email_address_is_valid_characters
        """
        Test to ensure email address includes '@' and '.'
        MANUAL TEST CARRIED OUT IN COMMAND LINE TO CHECK VALID
        EMAIL LOOP. WILL ONLY ENSURE >5 length, '@' and '.' in 
        any combination. 'assertIn' method with a for loop possibly?
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
    
