# Module07 Website

Sean McGrath-Bennett
May 31, 2022
Foundations of Programming: Python
Assignment 07
[GitHubURL]: (https://github.com/seanybmb/IntroToProg-Python-Mod07)

Creating the Pickling and Error Handling Script

Introduction

This paper outlines the necessary steps to create the scripts to save to a binary file and outlines several ways of error handling.  I used several sources to learn about, and dive into error handling and pickling, including:
•	[Exception Handling] (https://www.tutorialsteacher.com/python/exception-handling-in-python)
•	[Pickling] (https://www.synopsys.com/blogs/software-security/python-pickling/)
•	Python Programming, Third Edition

Writing and Running the Pickling and Error Handling Script

I wrote and ran the script using PyCharm and saved the scripts into two different files
I first imported the pickle and then defined my variables. Next I processed the data by defining the functions which would be both written and read. And then finally is the user input section that then presents the data, stores it into a list, stores the list in a binary file. The data is then read, the file closed and then the information is printed.
Once the code was in place, I ran the code in PyCharm and via a Console Application. (Figure 1)

![Exception Handling Python Code](https://github.com/seanybmb/IntroToProg-Python-Mod07/blob/main/Figure1.png?raw=true "Exception Handling Python Code")

Figure 1: Pickle Code Running

I changed the directory to the folder the script was in, typed “python” and then ran the script successfully.  Once done, I hit enter which then prompts me to make my selection. I input several pieces of data which was then pickled and added to the file. (Figure 2)

![Exception Handling Python Code](https://github.com/seanybmb/IntroToProg-Python-Mod07/blob/main/Figure2.png?raw=true "Exception Handling Python Code")

Figure 2: Console Application running Python Pickling Script

![Exception Handling Python Code](https://github.com/seanybmb/IntroToProg-Python-Mod07/blob/main/Figure3.png?raw=true "Exception Handling Python Code")

Figure 3: Notepad file

For exception handling I covered three scenarios by using try:, except:, else:, and finally: - In this script we put in scenarios including: not having a file already created, inputting the wrong type of data or adding a zero.
Once the code was in place, I ran the code in PyCharm and via a Console Application. (Figure 4)

![Exception Handling Python Code](https://github.com/seanybmb/IntroToProg-Python-Mod07/blob/main/FIgure4.png?raw=true "Exception Handling Python Code")

Figure 4: Exception Handling Code Running

I changed the directory to the folder the script was in, typed “python” and then ran the script successfully.  Once done, I hit enter which then prompts me to make my selection. I input several pieces of data which was then pickled and added to the file. (Figure 5)

![Exception Handling Python Code](https://github.com/seanybmb/IntroToProg-Python-Mod07/blob/main/FIgure5.png?raw=true "Exception Handling Python Code")

Figure 5: Console Application running Python Exception Handling Script

Summary

This paper described the process, using PyCharm (to create the Home Inventory Menu Script) and then explains how to run the script using Command Prompt to create a console application that receives input and writes the input information to a text file.
