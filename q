[33mcommit 623d7b96e4dc8baf97f1438e727aa14144c34f5e[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m)[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Tue Mar 6 08:49:54 2018 +0000

    challenge.js file created to add jquery

[33mcommit 21bea1aa2c6ea776fab76e3368ade6546fbbc62c[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Mon Mar 5 18:54:00 2018 +0000

    Unittest on function (limit_number_questions) to limit number of Guesses to Two per Challenge and revise scoring matrix

[33mcommit 18310e78396314834651a20e6822c5f0d7d6f25c[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Mon Mar 5 03:19:28 2018 +0000

    Refactored repeated code for Q&A section on Challenge pages: challenge_scoring(guess, answer)

[33mcommit f972f3895cb20d1b35c35de66cde7bda9fd4198d[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Mon Mar 5 02:57:32 2018 +0000

    Refactored repeated code for handling list appends

[33mcommit 5505648e996a0f13a78f69a99ff94b10f52b2577[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Mon Mar 5 00:42:02 2018 +0000

    Flash feature installed to display user's guess

[33mcommit 6226ce221b797499d22b898357c76fde25eb648c[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Sun Mar 4 23:49:53 2018 +0000

    Scoring function tested, defined on view page and added in to Challenge route to score user responses to questions

[33mcommit bf8806b10243ce1659436d8387b76d68ff86a77b[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Sun Mar 4 03:20:57 2018 +0000

    Username and Email stored in user_info.json as an object (dump). Page redirects built into functions.

[33mcommit 9d519e1b50689b09e167e7b3a5e63000e414048f[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Sun Mar 4 02:07:50 2018 +0000

    Challenges spread across 8 pages. Challenge.json inserted into each separately. Home Page & Challenged restyled

[33mcommit 17b83dabb49d6582836a55c486ed71bfbae6eca6[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Sat Mar 3 15:02:01 2018 +0000

    username and email requirement function added to sign in

[33mcommit 80e692ac157a32e5016214f99f59138978c651c4[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Sat Mar 3 13:19:32 2018 +0000

    user_info.txt file created to store sign-in details

[33mcommit 893bc400f26a4cb7682c945723700c74acddb10d[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Sat Mar 3 05:20:22 2018 +0000

    Flash imported into flask & Username Display on Challenge.html added

[33mcommit 1cf0fd1e6903820d757ea1f71b5982644202a5d0[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Sat Mar 3 04:33:34 2018 +0000

    Enter username and email form added to index.html with POST request enabled

[33mcommit 528d889a040be2b285180aedd46da6f50f8c3a56[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Sat Mar 3 00:52:32 2018 +0000

    Questions data read from json file to Challenge Template and iterated over to fill sections

[33mcommit 0ca3d444d0c60bfb0e278c4612345e5dcdc036eb[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Fri Mar 2 04:29:36 2018 +0000

    Template Challenge Page styled and render templates used

[33mcommit de9991adeb12368d55aad8e0fea41aeee2d914dc[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Thu Mar 1 22:27:18 2018 +0000

    json file with Challenge Quiz data created

[33mcommit 107331f682f5b0d0e9079ccef133aec6ff55dcad[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Thu Mar 1 04:19:32 2018 +0000

    Images uploaded for Challenge, index.html formatted and sample quiz page (challenge.html) created

[33mcommit dcc9f173c410bc21f3508c98ed5f4551831afce7[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Thu Mar 1 01:40:25 2018 +0000

    Template inheritance implemented. Bootstrap theme downloaded and boilerplate added to base.html

[33mcommit f4eca67fe51b1e361f6af076f226af783dc30d52[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Wed Feb 28 19:06:58 2018 +0000

    Routing between four main pages set up

[33mcommit f0c1c2c6d7eaa64a157dcb626aaf1bab3ed1682c[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Wed Feb 28 18:02:34 2018 +0000

    Flask imported

[33mcommit 17bd285a1985ff791aaed898556c600d6b6b2fed[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Wed Feb 28 03:14:52 2018 +0000

    Questions_Answers function: test to ensure 0 points awarded for incorrect and invalid answers

[33mcommit fb4d4e576343b0e06076c4ff6f44ab57a14e673b[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Wed Feb 28 03:12:15 2018 +0000

    Questions_Answers function: Test to ensure 'close enough' answer accepted and 5 points awarded

[33mcommit 4365edb75e1ddb9d5a4a5a20343ed07d975e635f[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Tue Feb 27 23:29:05 2018 +0000

    Questions_Answers function: Test to ensure correct answer is accepted and 10 points awarded

[33mcommit c2720ca700081dab0c1f229dc63837307ef4a621[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Tue Feb 27 12:20:23 2018 +0000

    Register function: refactored code

[33mcommit e0d589654bca702f22ce38706892d22c5e395a07[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Tue Feb 27 04:07:18 2018 +0000

    Register function: Test to ensure 'a' and '.' included in user email address

[33mcommit 037b10a7dfa5dae4c12f82f1bc94909b9e610171[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Tue Feb 27 03:17:13 2018 +0000

    Register function: Test user email address must be >5 characters

[33mcommit d48234843a5ffe07c41a3a78c38bb9e1b0ef3ee9[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Tue Feb 27 01:44:26 2018 +0000

    Register function: Test user prevented from proceeding until valid username entered

[33mcommit edc9139324016fa73135ad5f18eac4e9c9ea5858[m
Author: Deasun OD <des_donn@mailbox.org>
Date:   Mon Feb 26 23:14:46 2018 +0000

    Initial Commit. Register function: Test username is not blank
