## General Information
### Developer
Dessie Donnelly (email: des_donn@mailbox.org)

### Partner
Market Development Association C/O Market Community Centre Belfast BT1 3JD (tel: 028 90312272)
Contact: Fionntan Hargey (email: fionntanh@hotmail.com)

### Project Overview
The <strong>Markets Development Association (MDA): TimeBank App</strong> is a guessing game based on the
results of peer-to-peer research (226 surveys) carried out by residents in the Markets area of Belfast.
 The research aimed to get a snapshot of priority social, economic and cultural 
 needs in the community as well as a detailed skills audit.

As participants work their way through the TimeBank App, they are progressively introduced
to the concept of Timebanking and its resonance with the survey results.

The TimeBank App is to be used at specific community events to generate discussion 
and interest. It has the capacity, per session, to store useful comments and 
emails of people who want more information.

## Functionality:
### Description
The TimeBank App has the following functionalities:
<ul>
<li>Landing Page with Start Game Button and navbar - further info and start</li>
<li>Animated Challenge Pages</li>
<li>Scoring: user input, storing user input, attributing points based on accuracy, 
    updating & displaying ongoing score, tallying, logging and displaying total score</li>
<li>Alert Messages</li>
<li>Registration</li>
<li>League Table with collated points and message</li>
<li>Further Information</li>
</ul>

### Technologies
The Questions and Answers were written and stored in .json format (challenge.json) 
and rendered into html using the Python Flask microframework.

The <strong>Game Logic</strong> was protoyped in Python shell and deployed utilising 
the Flask microframework, specifically:
<ul>
<li><strong>keeping score</strong> - user guesses are stored in a temporary python list (score). The score 
    is tallied following the last question and appended to a seprate python list (final_score). 
    json.dump is used to store the final score (alongside user registration details)
    in a .txt outfile (user_info.txt). The temporary score list is emptied once a user starts a new game,
    and the process repeats.</li>
<li><strong>displaying score</strong> - flask's flash() method is used to provide users with an ongoing score 
    update prior to each new question. The flash() method is used again to display 
    user's Final Score on the registration page</li>
<li><strong>page progression</strong> - flask's redirect() function is used to automatically guide 
    the user through the questions once the game has started</li>
<li>registration - user input (name, email address & comments) is captured by 
    using a HTTP POST request and appended to the outfile (user_info.txt)</li>
</ul>

Page transitions and animations to enhacne UX and guide user through the application 
were written using Javascript and the JS library jQuery. Javascript was also used:
<ul>
<li>to process user input by attaching an AJAX Request to a jQuery button in order to 
avoid page reload</li>
<li>to refresh the Message Board every 10 seconds and ensure score table and comments
are kept up to date for community events</li>
</ul>

A CSS bootstrap theme (https://blackrockdigital.github.io/startbootstrap-resume/) 
was utilised during initial implementation stages, but heavily edited and added to 
as the design developed to match functionalities required for the TimeBank App.

The original navigation bar colour and drop-down functionality, default header font, as 
well as the flexbox formatting is retained, the rest of the styling was created 
by the developer specifically for the Timebank App. 



### Deployment
The MDA: TimeBank app was deployed to the cloud platform Heroku (insert link)


### Testing
"In this section, summarise your approach to testing and provide pseudocode you have written to develop your tests"

There were three distinct approaches taken to testing durig this project:
a) prototype development
b) testing before deployment
c) testing on functions

Each stage required refactoring post-testing.


A <strong>Prototype</strong> of the TimeBank App was first developed and tested in a python interpreter 
to determine the functions required to run the game (/testing/timeBankTeaser_proto.py)
PSUEDOCODE

Tests were developed on the following functionalities:
<ul>
<li>Registration authentication - no blank inputs for username and email, limited character count for email. 
PSUEDOCODE
Example:

def test_username_not_blank(self):
 self.assertNotEqual(guess_game.validate_username("Mark123"), 0)
        self.assertNotEqual(guess_game.validate_username("#%$"), 0)
        self.assertNotEqual(guess_game.validate_username("Mark"), 0)
        self.assertNotEqual(guess_game.validate_username("13"), 0)
        
<em>This process was eventually simplified using bootstrap.</em></li>

<li>A testing suite (/testing/manual_tests) was set up to manually test that data retrieved from user input was being stored to .txt file successfully</li>
PSUEDOCODE
<li>First Scoring tests - Test to check can take three arguments (2 guesses, 1 answer), exit if
        guess correct on first attempt, and return 10 points
Test to check can take three arguments (2 guesses, 1 answer), move to
        second correct guess if first incorrect, and return 8 points
Test to check if second guess within  less than 10 or gtr than 10 returns 5 points
Test to check if second wrong guess returns 0 points


Example:
    def test_limit_number_questions(self):
        """
        Test to check can take three arguments (2 guesses, 1 answer), exit if
        guess correct on first attempt, and return 10 points
        """
        self.assertNotEqual(guess_game.limit_number_questions(32, 21, 59), 10)
        self.assertNotEqual(guess_game.limit_number_questions("Mum", 21, 59), 10)
        self.assertEqual(guess_game.limit_number_questions(59, 21, 59), 10)
        self.assertNotEqual(guess_game.limit_number_questions(21, 59, 59), 10)

</li>




<li>Scoring a) test to check whether 10 awarded for correct answers, b) test to 
    check whether 5 awarded for answers which are within range of 10 lower or 
    higher than answer, c) test to check whether 0 awarded for incorrect and invalid answers
PSUEDOCODE
Example:
def test_ask_questions(self):
 self.assertEqual(guess_game.ask_questions(23, 23), 10)
        self.assertNotEqual(guess_game.ask_questions("hello", 23), 10)
        self.assertNotEqual(guess_game.ask_questions("&%$", 3), 10)
        self.assertNotEqual(guess_game.ask_questions(32, 3), 10)

</li>

</ul>



when code developed and dependent on files, run it in replit with hypothetical variables, lists
using python print() function in Command Line to monitor outputs of code between functions


## Images
All images used on the site are from FREEIMAGES (https://www.freeimages.com/)
and used under their CONTENT LICENSE AGREEMENT.
