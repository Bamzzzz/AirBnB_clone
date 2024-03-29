0x00. AirBnB clone - The console
Group project
Python
OOP
By: Guillaume
Weight: 5
The project to be done by two people



Console:
The console is a command line interpreter that permits management of the backend
of AirBnB.

Using the Console
The AirBnB console can be run both interactively and non-interactively.

$ echo "help" | ./console.py
(hbnb)

EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
Alternatively, to use the AirBnB console in interactive mode, run the
file console.py by itself 

$ ./console.py

While running in interactive mode, the console displays a prompt for input:

$ ./console.py
(hbnb)

To quit the console, enter the command quit, or input an EOF signal
(ctrl-D).

$ ./console.py
(hbnb) quit
$

$ ./console.py
(hbnb) EOF
$

Testing:
Unittests for the AirBnB project are defined in the tests
folder. To run the entire test suite simultaneously, execute the following command:

$ python3 unittest -m discover tests


Alternatively, you can specify a single test file to run at a time:

$ python3 -m unittest tests/test_console.py
