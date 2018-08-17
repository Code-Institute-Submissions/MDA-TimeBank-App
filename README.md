# MDA TimeBank app
A community tool to generate interest in timebanking economies

## Overview

### What is this application for?
**MDA TimeBank App** is a guessing game based on the results of peer-to-peer research (226 surveys) carried out by residents in the Market area of Belfast.

The TimeBank App is to be used at specific community events to generate discussion and interest in setting up a local, or joining a regional, TimeBank.

### What does it do?
After registering a username, participants guess answers to a series of questions based on the results of a community survey. At the end of the challenge, participants are provided with their final score in a table of  other participants' scores. They are presented with the concept and core values of TimeBanking (including an introductory youtube video), and contact details of their local TimeBank organiser/contact.

##### How the challenge is scored
> * Correct guesses are awarded with 10 points
> * Guesses within a +/-5 point range of the answer are awarded 5 points
> * All other valid (>=0) guesses are awarded 0 points
> * Players get 2 guesses per question

The **MDA TimeBank App** will be used by a cross section of the community including all ages and different IT proficiency. The app is desinged with simplicity in mind with players only being asked to enter guesses. The text is rendered in relativey large font for accessibility purposes.

The **MDA TimeBank App** is a 'conversation' starter and as such is not intended to convey excessive information or take too much time to complete. The game has 8 questions and can be completed in under 5 minutes with relative ease. The animations provide for a more stimulating UX without being distracting or taking too much time to complete.

### How does it work
The application uses the **Flask** microframework to route participants through the challenge and execute the programme. The programme is written in **python 2.7.6**

The site is styled with **Bootstrap** and **JQuery** code. The Bootstrap grid layout is used to make the application responsive across mobile, tablet and desktop devices. The site employs a **mobile-first** design and can be viewed [HERE](https://mda-timebank.herokuapp.com/). JQuery is used to provide events and animations on each of the challenge pages.

The information for each challenge is stored in the ```data/challenge.json``` file and rendered onto the template by passing the json formatted information to fill Flask's **jinja2** variables. 

Information needed for participants to progress through the challenge (current score, question information and attempts per question)  is stroed in the Flask 'context' which is updated after each question. The 'username' and 'final score' details are stored in the ```data/results.json``` file and rendered to the results table at the end of the challenge.

A JQuery function is included in results_table.html to reload the results page every 20 seconds so that players are added to the table when other users are reading or watching information from the carousel.

**AWS Cloud9** has been used to manage package dependencies for deployment of site on GitHub and Heroku. 


## Technology Used

### Specific technology used on the application includes:

#### Code
- **HTML**, **CSS**, **JQuery** and **Python 2.7.6**
    - Base languages used to create website
- [Flask](http://flask.pocoo.org/)
    - **Flask** is used to handle different view functions and enable template inheritance which guide the participant through the challenge
- [Bootstrap](http://getbootstrap.com/)
    - **Bootstrap v4** is used to render a responsive layout, including navigation bar, display table and carousel
- [JQuery](https://jquery.com)
    - **JQuery** adds animation styling to the site to enhance user experience
- [Sass](https://sass-lang.com/)
    - **Sass/scss** CSS extension is used to code and organise CSS stylesheets

#### Functionality
- [.json](https://www.json.org/)
    - **.json** lightweight data interchange format is used to store the challenge information (including url for images) rendered onto the challenge templates to progress through the successive questions.

#### Hosting
- [Heroku](https://www.heroku.com/)
    - The Cloud Application Platform **Heroku** hosts the MDA TimeBank Application. The GitHub repo is connected directly to the Heroku app and automatics deployments are enabled for when the project is pushed to github master repo.


## Testing
A **Test Driven Development** approach was used to develop the application. Manual tests were also used. The process applied with examples can be found [here](testing/tdd.md).


## Contributing
This project is customisable by saving your own survey information, in json format, into the ```data/challenge.json``` file, including the background images (with ones reflecting topic of the question) and text. All contributions to improving the code are welcomed, so make changes you think are needed/desired and submit a pull request

## Getting the code up and running
1. Create an environment running python 2.7.6 as the default in your IDE
2. Clone this repository by running the ```$ git clone https://github.com/Deasun/MDA-TimeBank-App.git``` command
3. pip install requirements
4. Run the app.py file and the app will be available for using your browser


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