# AirBnB clone - The console
The AirBnB Clone Console is a command-line interface (CLI) tool designed to streamline the management and interaction with the AirBnB clone application. Through this console, users have the capability to perform operations such as creating, reading, updating, and deleting data from the application's database.
## General Use

### Step 1. Clone the Repository and Navigate to it

Clone the repository and move into the repository directory.

### Step 2. Run the Console

Locate the "console.py" file inside the repository. This file contains the command-line interpreter. Execute the following command in the terminal to launch it:

```bash
$ python3 console.py
```
### Step 3. Access the Console
Upon running the above command, you should see the prompt (hbnb) indicating that the console is ready for use.

### Step 4. View Available Commands
Type ? and press Enter to see a list of all available commands within the interpreter.

## Background Context

### First Step: Building a Command Interpreter
The first step in creating the AirBnB clone is to construct a command interpreter that will manage AirBnB objects.
This is a pivotal stage because the foundation laid here will be utilized in all subsequent projects,
including HTML/CSS templating, database storage, API, and front-end integration.

Each task is interconnected and serves the following purposes:

- Establish a parent class (BaseModel) responsible for the initialization, serialization, and deserialization of future instances.
- Create a straightforward serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> file.
- Develop all classes required for AirBnB (User, State, City, Place, etc.) that inherit from BaseModel.
- Set up the initial abstracted storage engine for the project: File storage.
- Formulate all unittests to validate the functionality of our classes and storage engine.
#### What's a Command Interpreter?
Remember the Shell? It's quite similar, but in our case, it's specifically tailored for our use.
We aim to manage the objects of our project, which includes tasks like:

- Creating a new object (e.g., a new User or a new Place).
- Retrieving an object from a file, a database, etc.
- Performing operations on objects (counting, computing stats, etc.).
- Updating attributes of an object.
- Destroying an object.

## Resources
__Read or watch__:
1. [cmd module](https://docs.python.org/3.8/library/cmd.html)
2. [cmd module in depth](http://pymotw.com/2/cmd/)
3. [uuid module](https://docs.python.org/3.8/library/uuid.html)
4. [datetime](https://docs.python.org/3.8/library/datetime.html)
5. [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
6. [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
7. [python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
8. [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
9. [python unittests](https://realpython.com/python-testing/)

## Conclusion
The AirBnB Clone - The Console is a robust tool that streamlines the management of the AirBnB clone application. 
Its user-friendly interface and powerful features have made it a popular choice among developers and users alike.

 -----------------------------------------------------------------------------------------------------------------------
## Python Scripts
 * Allowed editors: vi, vim, emacs
  * All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  * All your files should end with a new line
 * The first line of all your files should be exactly #!/usr/bin/python3
 * A README.md file, at the root of the folder of the project, is mandatory
*  Your code should use the pycodestyle (version 2.8.*)
 * All your files must be executable
 * The length of your files will be tested using wc
 * All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
 * All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
 * All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
 * A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
--------------------------------------------------------------------------------------------------------------------------------
## Python Unit Tests
 * Allowed editors: vi, vim, emacs
 * All your files should end with a new line
 * All your test files should be inside a folder tests
 * You have to use the unittest module
 * All your test files should be python files (extension: .py)
*  All your test files and folders should start by test_
 * Your file organization in the tests folder should be the same as your project
 * e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
 * e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
 * All your tests should be executed by using this command: python3 -m unittest discover tests
 * You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
 * All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
 * All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
*  All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
  We strongly encourage you to work together on test cases, so that you don’t miss any edge case
-----------------------------------------------------------------------------------------------------------------------------------------------
