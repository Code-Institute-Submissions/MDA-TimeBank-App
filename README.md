# MDA TimeBank app
A community tool to generate interest in timebanking economies

## Overview

### What is this application for?
**MDA TimeBank App** is a guessing game based on the results of peer-to-peer research (226 surveys) carried out by residents in the Markets area of Belfast.

The TimeBank App is to be used at specific community events to generate discussion and interest in setting up a local, or joining a regional, TimeBank.

### What does it do?
Participants guess answers to a series of questions based on the results of a community survey. As participants progress through the questions, they are introduced to the concept and core values of TimeBanking.

##### How the challenge is scored
> * Correct guesses are awarded with 10 points
> * Guesses within a 10 point range of the answer are awarded 5 points
> * All other valid (>=0) guesses are awarded 0 points

##### Building contacts through the app
> At the end of the challenge, participants are provided with their final score and must register to leave a comment, see the results table of other participants' scores, get more information about TimeBanking (including an introductory youtube video), and get details of their local TimeBank organiser/contact.

### How does it work
The application uses the **Flask** microframework to route participants through the challenge and executive the programme. The programme is written in **python 2.7.6**

The site is styled with **Bootstrap** and **JQuery** code. The Bootstrap grid layout is used to make the application responsive across mobile, tablet and desktop devices. The site is designed using a **mobile-first** design and can be viewed [HERE](insert link following deployment). JQuery is employed to provide animations on each of the quiz/challenge pages.

The information for each challenge is stored in the ```data/challenge.json``` file and rendered onto the templates by passing the json formatted information through the relevant views and rendered onto the corresponding templates. 

Participants scores are recorded in a list and compiled with user information logged at the registration stage of the app - which acts as a gateway to further information. These details are stored in a list of dictionaries, per session, in a ```data/user_info``` file.

**AWS Cloud9** has been used to manage package dependencies for deployment of site on github pages. 


## Tech Used

### Specific technology used on the application includes:

### Code
- **HTML**, **CSS**, **JQuery** and **Python**
    - Base languages used to create website
- **unittest** 
    - A test suite was developed using unittest 
- [Flask](http://flask.pocoo.org/)
    - **Flask** is used to handle different view functions which guide the participant through the challenge, 
- [Bootstrap](http://getbootstrap.com/)
    - **Bootstrap 3.3.7** is used to render a responsive layout, including navigation bar and display table
- [JQuery](https://jquery.com)
    - **JQuery** adds animation styling to our site to enhance user experience. The JQuery plug-in **Marquee** was used to display the scrolling alerts
- [Sass](https://sass-lang.com/)
    - **Sass/scss** CSS extension is used to code and organise CSS stylesheets


### Functionality
- [AWS S3](https://aws.amazon.com/s3/)
    - **AWS S3** cloud storage is used to store the static and media files for the application.

### Hosting
- [Heroku](https://www.heroku.com/)
    - The Cloud Application Platform **Heroku** hosts the MDA TimeBank Application.


## Testing
The MDA TimeBank App was first prototyped on the python shell (see file ```testing/timeBankTeaser_proto.py```) to identify the core features and functionalities that would be required for the flow of the challenge.

**Two main functions** were identified: 
* assess how close to/far off the guess was to the answer,
* attribute a score based on that guess.

A **Test Driven Development** approach was used to develop this code using the folllowing steps:

1. Identify the functionality that needs to be built and write pseudocode
2. Write the code
3. Write a test for this function
3. Run a deliberately failing test
4. Edit the test and make it pass
5. Refactor code if necessary
6. Repeat each of these steps for each new feature. Tests should continue to pass as the function is constructed.

#### 1. Identify the functionality that needs to be built and write pseudocode
Here is an example of the pseudocode developed for the two main functions involved in calculating user score:

**Guess range relative to answer Test:** 
> * GUESS is less than 0 (invalid GUESS)
> * GUESS and ANSWER are equal
> * GUESS is within a +10 range of ANSWER
> * GUESS is within a -10 range of ANSWER

**Score based on GUESS range relative to ANSWER Test:**
> * if GUESS is less than 0, score is 0
> * if GUESS is equal to ANSWER, score is 10
> * if GUESS is 10 or more numbers greater than ANSWER, score is 0
> * if GUESS is 10 or more numbers fewer than ANSWER, score is 0


### 2. Write a test for this feature
Each new feature in the function was tested and used only once all of the tests in the test suite were passing.

*For example here is the first code developed for the guess_range() function:*

> GUESS is less than 0 (invalid GUESS)*


    def guess_range(guess, answer):
        if guess < 0:
            return True
    
### 3. Run a failing test
*The above code was then tested with a deliberately failing outcome:*

    assert guess_range(3, 4) == True, "Guess is less than 0"
    print("All tests passed!")

    $ python3 testing/testing.py
    Traceback (most recent call last):
        File "testing/testing.py", line 25, in <module>
        assert guess_range(3, 4) == True, "Guess is 0"
        AssertionError: Guess is 0

### 4. Edit and make it pass
*The test was then amended to produce a passing outcome:*

    assert guess_range(-2, 4) == True, "Guess is less than 0"

    $ python3 testing/testing.py
    "All tests passed!"

*The next feature was then added to the existing existing function:*

    def guess_range(guess, answer):
        if guess < 0:
        return True
    <!--new line of code-->
    elif guess == answer:
        return True

*and tested, first producing a failing outcome, then edited to pass:*

    assert guess_range(-5, 4) == True, "Guess is less than 0"
    assert guess_range(15, 15) == True, "Guess is equal to answer"
    "All tests passed!"

### 5. Refactor code
Steps 1-4 were repeated until the function had been completed and as the two functions were to be merged, the code was refactored when the individual functions had been tested separately. For example:


*Assessing the accuracy of the guess*

    def guess_range(guess, answer):
        if guess < 0:
            return True

*and calculating a score based on this guess*

    score_test = []

    def allocate_points(guess, answer):
        0 points
        if guess < 0:
            score_test.append(0)
            return int(sum(score_test))

*was refactored to:*

    score = []

    def calc_score(guess, answer):
        if guess < 0:
            points = 0
            score.append(points)
            return int(sum(score))

*and tested, with the scores accumulating as they would during the challenge:*

    assert calc_score(-5, 8) == 0, "Guess is below 0, score is 0"
    ...
    assert calc_score(8, 8) == 10, "Guess is equal to answer, score is 10"
    assert calc_score(9, 18) == 15, "Guess is within 10- point range of answer, score is 5"
    assert calc_score(22, 18) == 20, "Guess is within 10+ point range of answer, score is 5
    "All tests passed!"

### 6. Repeat previous steps
These steps were repeated until all tests were passing and the code was refactored.

The registration function was also tested manually by mimicking the .txt (```test_user_data```) file storage.

The testing suite (with development code) is found in ```testing/testing.py``` 


## Contributing
This project is customisable by entering your own relevant surevy information into the ```data/challenge.json``` file and changing the background images in the static files.

### Getting the code up and running
1. Create an environment running python 2.7.6 as the default in your IDE
2. Clone this repository by running the ```git clone https://github.com/Deasun/snAPP.git``` command
3. pip install requirements


## Credits

### Media
All images used on the site are from [FREEIMAGES](https://www.freeimages.com)
and used under their CONTENT LICENSE AGREEMENT.

The youtube video is a product of [TimeRepublik](https://timerepublik.com/)

### Developer
Dessie Donnelly (email: des_donn@mailbox.org)

### Partner
Market Development Association C/O Market Community Centre Belfast BT1 3JD (tel: 028 90312272)
Contact: Fionntan Hargey (email: fionntanh@hotmail.com)