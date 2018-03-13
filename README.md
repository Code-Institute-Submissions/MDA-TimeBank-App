Markets Development Association: TimeBank App

Purpose:

Target Group:
Accessibility issues and temporary use. Large fonts and one breakpoint. 

Functionality:

How Achieved Functionality:
Python
Flask
    used operator import itemgetter, attrgetter to order table in descending order
Ajax request
    handle POST requests without requiring page reload
jquery
    style transitions in challenge pages, Smoothe user experience
CSS & SCSS

Data Structure:
list updated & .txt storage
list objects (sets?) required updated as challenged progressed and made composite at end. Suited best

User feedback
Required ajax as logging scores and HTTP requests were forcing page reload. Messy user experience
and poor functionality (fade-ins)
Could not use Flask's Flash method to show scores back, so used jquery
Flask method was used to thank people for registering


Testing Methodology:
    when code developed and dependent on files, run it in replit with hypothetical variables, lists
using python print() function in Command Line to monitor outputs of code between functions
    Ran test on compiling of user info data (user_info_test.py file). Creating different lists to store & dump data
    Problem retaining temporary data in list to redner league table. Few iterations using three lists 
    to transfer and empty. resolved with 'w' - final capture of info - overwrite previous

Bugs:
Background Image element losing proportion when scaled down(challenge_2, _4, _6, _8, message_board - erratically
