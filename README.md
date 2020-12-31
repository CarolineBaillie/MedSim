# Medical Diagnosis Simulation
 
## Why
At my highschool, I am co-head of the Medicine Club. Currently, we have split up into groups and are creating a medical diagnosis simulation. We create a patient portfolio and a list of symptoms, then give it to the other groups to attempt to diagnose. However, I thought it would be really cool if we could ask questions or perform tests on the patients without the creators present.  I wanted to do this in an interactive way, so I decided to use my winter break and django skills to create an app that we could actually use!
 
## What
As described above, this is a medical diagnosis simulation app. There are two initial options for a user once they have signing in: create a simulation, play a simulation.
If you choose to create, you will need to fill in all the necessary patient information as well as fill in any possible tests, questions, and hints. Once created, the simulation is available to everyone to play. Your only other job if you have created a simulation is to keep track of people's final diagnoses and tell the application whether they are correct or not.
If you play a simulation, you have access to all the patient information and any other additional information, tests, questions, or hints that the creator has provided you with. You can reply to simulations as many times as you would like and the goal is to get the correct diagnosis and the highest score. Be sure to save your progress every time you want to exit!
 
## How
In this application, all of the routing is done through python, the pages created with HTML and CSS, and the interactive section when playing a simulation uses Javascript. The hardest part was incorporating the simulation and javascript into the python, and making sure your progress would save. When tests are performed, questions are asked, and hints are viewed, I display the answer, then add the name of the test/question/hint to an array. When the submit or save button is pressed, it sends the arrays back to the python through an api.
 
## Navbar page options
**Guide:** This page that tells you all about how to use this app.
**Create:** On this page you create your own simulation. There are a lot of input boxes in order to gain the most information. Most boxes' inputs are required, but some are optional. On the top half it will say optional, but then all tests, questions, and hints are optional.
**My Simulations:** On this page all the simulations that you have created will appear. Additionally, at the top, if someone else has completed your simulation you will see their final diagnosis and will have to say whether it is correct or not.
**Browse:** Here you will see all simulations that are created. You will also be able to use the search bar to narrow down the results.
**Current:** All the simulations you are currently working on will be shown on this page.
**Completed:** All the simulations you have completed will be shown here. You can see the score and see if your diagnosis was correct or not. Note: you will not see the results appear here until the creator has approved your answer.
 
## Other information
I had to write all of the css and js inside the html functions because for some reason, the files won't connect. I have researched the issue and attempted many solutions, but none of them have worked. If you think you might be able to help please let me know!
 
## Code
### views.py:
**index:** This function renders home.html which is just a welcome message when opening the application or logging in.
**guide:** This function displays guide.html which has information on the app.
**create:** This function takes in all the information from the create form and saves it to the database.
**play:** This function is called when a user attempts to play a simulation. It checks to see if the user is just starting this simulation or if they are continuing it, and passes in the proper information to game.html (the file with code for the simulation).
**save:** This function is run when a player saves and exits a simulation. It updates the string of tests/questions/hints performed/asked/viewed.
**submit:** This function is run when a player submits a diagnosis for a simulation. It updates the string of tests/questions/hints performed/asked/viewed and changes the settings of the object so the creator can check if the diagnosis was correct.
**affirmed:** This function is called when a user accepts or declines the player's diagnosis. It calculates the player's final score and creates a new completed game object.
**reset:** This function is called when the reset button on a simulation is clicked. It deletes the information on the users actions on this simulation so that the user can play the simulation again.
**completed:** This function gathers all necessary information on completed simulations to display to the user.
**mySim:** This function shows the user all the simulations they have created, and if anyone has diagnosed their simulation, presents them with their answer and asks them to validate it.
**current:** This function shows the user all simulations they are currently playing.
**browse:** This function's GET method collects all of the simulations (either completed or current/unstarted) and displays them on a page. The POST method receives a search bar input and returns simulations with a matching or similar title.
**login_view:** This function checks the input values against the user database and if they match, logs a user in.
**logout_view:** This function logs a user out and redirects to the login page.
**register:** This function creates a new user with the submitted credentials.
### templates/simulation
**create.html:** This file contains the code for the create a simulation form. There are many different inputs so it is quite long.
**game.html:** This file displays the simulation. The information about the specific simulation is passed in as well as the information on the users current progress with the game. There is a lot of js at work in this file, and the result is a very interactive and fun page!
**guide.html:** This file displays instructions, tips, and other information about this app.
**home.html:** This is a welcome page.
**layout.html:** This is the file that sets up the structure for most of the other pages. All but game.html extend from this file.
**login.html:** This is the login form.
**register.html:** This is the registration form.
**simulation.html:** This is the file that shows all the simulations available. Based on its type, it returns different text and simulations.