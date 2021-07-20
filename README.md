![Calculator Image](screenshots/calculatorImageResize.jpg)

# Text-based Calculator

This is a calculator project that was created using Python Programming language. It is a very basic calculator with simple functionalities which allows a user to input a number or 2 numbers based on the operation to be performed and the code carries out the operation and returns the appropriate result. Interaction with the calculator is restricted to the terminal as Python is a back-end language so there is no GUI available to the user. They simply follow the text-based instructions displayed at the terminal aand if the instructions are followed correctly, they will get their desired result printed to the terminal.

![Calculator on Desktop, Laptop, Tablet & Smatphone](screenshots/amIResponsiveCalcScreenshot.PNG)

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
        ![addition Screenshot](screenshots/addCalcScreenshot1.PNG)
        ![addition Screenshot](screenshots/addCalcScreenshot2.PNG)

        b) I want to be able to subtract two numbers and get the right result.
        ![subtraction Screenshot](screenshots/subtractCalcScreenshot1.PNG)
        ![subtraction Screenshot](screenshots/subtractCalcScreenshot2.PNG)

        c) I want to be able to multiply two numbers and get the right result.
        ![multiplication Screenshot](screenshots/multiplyCalcScreenshot1.PNG)
        ![multiplication Screenshot](screenshots/multiplyCalcScreenshot2.PNG) 

        d) I want to be able to divide two numbers and get the right result.
        ![division Screenshot](screenshots/divideCalcScreenshot1.PNG)
        ![division Screenshot](screenshots/divideCalcScreenshot2.PNG) 

        e) I want to be able to calculate the modulo (remainder after dividing two numbers) and get the right result. 
        ![modulo Screenshot](screenshots/moduloCalcScreenshot1.PNG)
        ![modulo Screenshot](screenshots/moduloCalcScreenshot2.PNG)

        f) I want to be able to calculate the exponent (power) of two numbers and get the right result.
        ![Exponent Screenshot](screenshots/exponentCalcScreenshot1.PNG)
        ![Exponent Screenshot](screenshots/exponentCalcScreenshot2.PNG) 

        g) I want to be able to calculate the square root of a number and get the right result. 
        ![SquareRoot Screenshot](screenshots/sqrootCalcScreenshot.PNG)

        h) I want to be able to get feedback if wrong operand (number)  is entered as input.
        ![Wrong Operand Screenshot](screenshots/invalidOperandInputCalcScreenshot1.PNG)
        ![Wrong Operand Screenshot](screenshots/invalidOperandInputCalcScreenshot.PNG)

        i) I want to be able to get feedback if wrong operator is entered as input.
        ![Wrong Operator Screenshot](screenshots/invalidOperatorInputCalcScreenshot.PNG)

        j) I want to be able to continue using the calculator without running the app afresh and quit whenever I like.
        ![ReplayQuitScreenshot](screenshots/quitReplay CalcScreenshot1.PNG)

        ![ReplayQuitScreenshot](screenshots/quitReplay CalcScreenshot2.PNG) 

        ![ReplayQuitScreenshot](screenshots/quitReplay CalcScreenshot3.PNG)

        ![ReplayQuitScreenshot](screenshots/quitReplay CalcScreenshot4.PNG) 
        

# Flowchart

The flowchart was used to conceptualise/bring the text-based calculator idea to life. It was drawn manually using pencil and paper to depict how the flow of the program will go.

* View the flowchart below: 

![Calculator Flowchart](screenshots/textBasedCalculatorFlowchart.jpg)

# Technologies Used

* Language Used

    * Python

---

* Tools Used

    * The Flowchart was made manually using paper and pencil.

    * snipping tool to capture screenshots of pep8 validator result, result generated at terminal and images used in the README file.

* Issues Encountered and Resolved

    * When a user finishes an operation, I want the code to ask the user if he wants to perform any more calculation and if 'y' is chosen by the user, the program should present the user with the option to choose the operator and the operands needed again and perform the required calculation for as long as the user wants and to quit when the user chooses 'n'  but when I ran my code it was not performing as such. I knew I would need a while loop but where to place that in the code was tricky but after many failed attempts, I figured that the while loop should be added to the user's response of 'yes or no'. If Yes is chosen,it continues to loop and if No, it exits the calculator. I also called the calculate_operation() function within the while loop. See screenshot below:

    ![WhileLoop](screenshots/calcLoop.PNG)

    * Initially, the "choice" variable for the input operator was made as a standalone code and when the program is called to run again when a user chooses 'yes', the 'choice' variable could not be called which made it impossible for a user to choose their operator so I decided to wrap it into a function named choose_operator() and when the calculate_operation() is called, the choose_operator() function will be called first within it, and this approach worked. 

    * When the code was run in Gitpod workspace, every part worked perfectly well but on the deployed site, Heroku, it performed the required operation and displayed the final result but didn't display the loop question/message that says "Do you want to perform another calculation y/n?. On pressing the enter key, it then displays the question together with the goodbye message signalling the end without allowing the user to pick an option of 'y' or 'no'. After searching for resources online and trying several things, I found out that not adding a new line character ("\n") at the end of the question caused the error. See screenshot below:

    ![New Line](screenshots/newLineError.PNG).






 Getting to implement feedback message that asks the user if they wish to perform another calculation 

In the course of developing this app, I wanted to implement

I am aware that the requirements.txt file is empty since I didn't need it for my project but I have left it in because I know it's needed for the Heroku to run