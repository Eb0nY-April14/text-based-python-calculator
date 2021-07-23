![Calculator Image](screenshots/calculator_image_resize.jpg)

# Text-based Calculator

This is a calculator project that was created using Python Programming language. It is a very basic calculator with simple functionalities which allows a user to input a number or 2 numbers based on the operation to be performed and the code carries out the operation and returns the appropriate result. Interaction with the calculator is restricted to the terminal as Python is a back-end language so there is no GUI available to the user. They simply follow the text-based instructions displayed at the terminal aand if the instructions are followed correctly, they will get their desired result printed to the terminal.

![Calculator on Desktop, Laptop, Tablet & Smatphone](screenshots/am_i_responsive_calc_screenshot.png)

# Features

The calculator provides the basic function of a simple calculator which can be used by any one for their everyday mathematical operations.

# Existing Features

The features provided by the calculator are as follows:

* choice 'a' for Add ('+') operator to add two numbers 
* choice 'b' for Subtract ('-') operator to subtract two numbers
* choice 'c' for Multiply ('*') operator to multiply two numbers 
* choice 'd' for Divide ('/') operator to divide two numbers
* choice 'e' for Modulo ('%') operator to get the remainder of two  numbers after division
* choice 'f' for Power/Exponent ('**') operator to get the exponent of two numbers 
* choice 'g' for Square Root ('√') operator to get the square root of a number.

---

User Experience (UX)

* User stories

    * User Goals

        a) I want to be able to add two numbers together and get the right result.

        b) I want to be able to subtract two numbers and get the right result.
    
        c) I want to be able to multiply two numbers and get the right result. 

        d) I want to be able to divide two numbers and get the right result. 

        e) I want to be able to calculate the modulo (remainder after dividing two numbers) and get the right result. 
        
        f) I want to be able to calculate the exponent (power) of two numbers and get the right result.
        
        g) I want to be able to calculate the square root of a number and get the right result. 

        h) I want to be able to get feedback if wrong operand (number) is entered as input.

        i) I want to be able to get feedback if wrong operator is entered as input.
        
        j) I want to be able to continue using the calculator without running the app afresh and quit whenever I like.
        
# Flowchart

The flowchart was used to conceptualise/bring the text-based calculator idea to life. It was drawn manually using pencil and paper to depict how the flow of the program will go.

* View the flowchart below: 

![Calculator Flowchart](screenshots/text_based_calculator_flowchart.jpg)

# Technologies Used

* Language Used

    * Python

---

* Tools Used

    * The Flowchart was made manually using paper and pencil.

    * snipping tool to capture screenshots of pep8 validator result, result generated at terminal and images used in the README file.

* Issues Encountered and Resolved

    * When a user finishes an operation, I want the code to ask the user if he wants to perform any more calculation and if 'y' is chosen by the user, the program should present the user with the option to choose the operator and the operands needed again and perform the required calculation for as long as the user wants and to quit when the user chooses 'n'  but when I ran my code it was not performing as such. I knew I would need a while loop but where to place that in the code was tricky but after many failed attempts, I figured that the while loop should be added to the user's response of 'yes or no'. If Yes is chosen,it continues to loop and if No, it exits the calculator. I also called the calculate_operation() function within the while loop. See screenshot below:

    ![WhileLoop](screenshots/calc_loop.png)

    * Initially, the "choice" variable for the input operator was made as a standalone code and when the program is called to run again when a user chooses 'yes', the 'choice' variable could not be called which made it impossible for a user to choose their operator so I decided to wrap it into a function named choose_operator() and when the calculate_operation() is called, the choose_operator() function will be called first within it, and this approach worked. 

    * When the code was run in Gitpod workspace, every part worked perfectly well but on the deployed site, Heroku, it performed the required operation and displayed the final result but didn't display the loop question/message that says "Do you want to perform another calculation y/n?. On pressing the enter key, it then displays the question together with the goodbye message signalling the end without allowing the user to pick an option of 'y' or 'no'. After searching for resources online and trying several things, I found out that the solution to the issue was already explained in the deployment section of the love-sandwiches video, not adding a new line character ("\n") at the end of the question caused the error. See screenshot below:

    ![New Line](screenshots/new_line_error.png).


Frameworks, Libraries and Programs Used

1. Git

    * Git was used for version control by utilising the Gitpod terminal to commit to Git and push to GitHub.

2. GitHub

    * GitHub was used to store the project's code after being pushed from Git.

I am aware that the requirements.txt file is empty since I didn't need it for my project but I have left it in because I know it's needed for the Heroku to run

## Testing

PEP8 online validation tool was used to validate the code to ensure there were no syntax errors or improper code indentation. It passed the test as seen in the screenshot below:

![PEP8 Testing](screenshots/pep8_validator.png)


### Testing User Stories from User Experience (UX) Section

i. I want to be able to add two numbers together and get the right result.

    a. User inputs two numbers, the app performs the addition operation and produces the correct result as seen in the screenshots below:

![addition Screenshot](screenshots/add_calc_screenshot1.png)
![addition Screenshot](screenshots/add_calc_screenshot2.png)

ii. I want to be able to subtract two numbers and get the right result.

    a. User inputs two numbers, the app performs the subtraction operation and produces the correct result as seen in the screenshots below: 

![subtraction Screenshot](screenshots/subtract_calc_screenshot1.png)
![subtraction Screenshot](screenshots/subtract_calc_screenshot2.png)

iii. I want to be able to multiply two numbers and get the right result.

    a.  User inputs two numbers, the app performs the multiplication operation and produces the correct result as seen in the screenshots below: 

![multiplication Screenshot](screenshots/multiply_calc_screenshot1.png)
![multiplication Screenshot](screenshots/multiply_calc_screenshot2.png) 

iv. I want to be able to divide two numbers and get the right result.

    a. User inputs two numbers, the app performs the division operation and produces the correct result as seen in the screenshots below:

![division Screenshot](screenshots/divide_calc_screenshot1.png)
![division Screenshot](screenshots/divide_calc_screenshot2.png) 

v. I want to be able to calculate the modulo (remainder after dividing two numbers) and get the right result.

    a. User inputs two numbers, the app performs the modulo operation and produces the correct result as seen in the screenshots below:

![Modulo Screenshot](screenshots/modulo_calc_screenshot1.png)
![Modulo Screenshot](screenshots/modulo_calc_screenshot2.png)

vi. I want to be able to calculate the exponent (power) of two numbers and get the right result.

    a. User inputs two numbers, the app performs the exponent operation and produces the correct result as seen in the screenshots below:

![Exponent Screenshot](screenshots/exponent_calc_screenshot1.png)
![Exponent Screenshot](screenshots/exponent_calc_screenshot2.png) 

vii. I want to be able to calculate the square root of a number and get the right result. 

    a. User inputs one number only, the app performs the square root operation and produces the correct result as seen in the screenshot below: 

![SquareRoot Screenshot](screenshots/sqroot_calc_screenshot.png)

viii. I want to be able to get feedback if wrong operand (number) is entered as input.

    a. User inputs incorrect operand, the app displays the message "Invalid input - NOT a number, Please try again!" to the screen and gives them the opportunity to re-choose a valid operand. See screenshots below: 

![Wrong Operand Screenshot](screenshots/invalid_operand_input_calc_screenshot1.png)
![Wrong Operand Screenshot](screenshots/invalid_operand_input_calc_screenshot2.png)

ix. I want to be able to get feedback if wrong operator is entered as input.

    a. User inputs incorrect choice of operator, the app proceeds to ask the user to input the 2 numbers, then it displays the error message "The Final Result of your calculation is Null. You entered an invalid operator" and asks the user if he wants to perform another Calculation as seen in the screenshot below:

![Wrong Operator Screenshot](screenshots/invalid_operator_input_calc_screenshot.png)

x. I want to be able to continue using the calculator without running the app afresh and quit whenever I like.

    a. Once the app displays the result of the current calculation, it asks the user if he wants to perform another calculation. If 'y' or 'Y' is chosen, the app continues by asking the user to choose the operator needed and the whole process is repeated again for as many times as the user wants but if 'n' or 'N' is chosen, the calculator app displays goodbye message to the user and quits as seen in the screenshots below:

![Replay Quit Screenshot](screenshots/quit_replay_calc_screenshot1.png)
![Replay Quit Screenshot](screenshots/quit_replay_calc_screenshot2.png) 
![Replay Quit Screenshot](screenshots/quit_replay_calc_screenshot3.png)
![Replay Quit Screenshot](screenshots/quit_replay_calc_screenshot4.png)

---

# Cloning (Local Deployment)

* To run this application locally, the repository can be cloned (i.e copy the app onto their machine and run it locally from there) by following the steps below:

1. Type the following command into your terminal:
git clone https://github.com/Eb0nY-April14/text-based-python-calculator.git

2. After the project is cloned, you would normally install the packages from the requirements.txt file using this command: 
pip3 install -r requirements.txt
However, this project does not contain any external Python packages but it's still needed (i.e requirements.txt file) purely for the Heroku setup. 

# Deployment

* To deploy this Project to Heroku, follow the steps below:

  1. Firstly, in order for the input method to work correctly in the deployed platform Heroku, a new line character needs to be added at the end of the input text and save it or else the text will not show up in the terminal. 

  2. Next, create a list of requirements that the project needs in order to run. Since several dependencies such as gspread and google-auth were installed into the workspace when we set it up initially, Heroku needs to install these dependencies as well and they need to go into the requirements.txt file.  
  To create the list of requirements, type the command below into the terminal:
  pip3 freeze > requirements.txt
  Then press the 'Enter' key.

  3. Go to Heroku website and create an account with them by clicking on the link below:
  https://id.heroku.com/login
  Fill out the form by providing your details such as First Name, Last Name, Email Address, Role e.g 'student', your Country i.e location, and Language i.e Python.  Confirm you are human and not a robot, then click the "Create free account" button on the page.

  4. Go to the email used for heroku registration and open up the confirmation email sent out to you. Click the link provided to confirm and you will be taken to another page to create a password, then click on the "SET PASSWORD AND LOGIN BUTTON". A welcome message is displayed so click on the "CLICK HERE TO PROCEED" button, accept their terms of service and the heroku dashboard will be displayed.

  5. From the Heroku dashboard, click on the "Create new app" button, give your app a name which has to be unique, select your region and click on the "Create app" button. 

  6. Click on the "Settings" tab at the top of the page and scroll down to locate the 'Config Vars' section, then click on the 'Reveal Config Vars'. In the 'KEY' field, type into it the word "CREDS" all in capital letters and for the 'VALUE' field, go over to your workspace, copy the entire creds.json file and paste it into the 'VALUE' field, then click the 'Add' button.

  7. Next, scroll down again to locate the 'Buildpacks' section and click on the "Add buildpack" button, then select "Python" as the first buildpack needed and click the "Save changes" button. 
  Click on the "Add buildpack" button again, select the "node.js" as the second buildpack needed and click the "Save changes" button.
  Ensure that the buildpacks are in the order of Python on top and node.js underneath or else click and drag them to the right order.

  8. Click on the "Deploy" tab at the top of the page and choose GitHub as the deployment method, then scroll down a little and click on the "Connect to GitHub" button.
  
  9. Search for your repository name by typing the name you gave it into the search box and click "Search" button, then click on "connect" to link up your Heroku app to your GitHub repository code.

  10. Next, scroll down to the "Automatic deploys" section and click the 'Enable Automatic Deploys' button so that Heroku can rebuild the app every time a new change is pushed to your code on GitHub.

  11. Finally, a message which says "Your app was successfully deployed" is displayed and a 'View' button is also provided to take you to the deployed link. 

  12. On the deployed site, the program starts (i.e runs) automatically but to restart it (i.e run it again), click the "RUN PROGRAM" button at the top of the page.

View the live project [here](https://my-text-based-calculator.herokuapp.com/)


View the GitHub Repository [here](https://github.com/Eb0nY-April14/text-based-python-calculator)


I am aware that the requirements.txt file has no content in it. I didn't use it since it's not needed for my project but it was left in because it is required in order for heroku to run perfectly.

* Credits

  * Stack Overflow resource on asking user for input until a valid reponse is given using while loop, handling exceptions using "try and except" to detect when the user enters data that can't be parsed
  https://stackoverflow.com/a/23294659 

  * Acknowledgements

    * Cohort Facilitator Kasia for her continuous help and support.

    * My mentor Tim Nelson for his immense help, continuous guidance and feedback.

    * Stack Overflow Website for helpful resources especially with handling exceptions and looping continuously until valid input and response are provided.

