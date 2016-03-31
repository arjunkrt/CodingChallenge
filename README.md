# CodingChallenge

Pre requistes:
1. Python
   Install python 2.7 if it is not installed in your system

2. Flask
   If Python Flask is not installed, then install  flask using the command

    "sudo pip install flask"

Clone the git repository using the command:

git clone https://github.com/arjunkrt/CodingChallenge.git

Once that is done go inside the Coding Challenge folder and then go inside the FlaskApp folder run the app.py
using the command python app.py

Once that is done you can directly goto the weburl : http://localhost:5000/ to run the application

You need internet connection for the CSS to work.

There are 2 functionalities which are handled in this form:
1. Given an IP address and Subnet MAask, it should return the Network Block and Host ID

2. Second one is if you input a set of logs in the text area provided and if you click on valid log results it will
 display the valid logs only


Sample Test Cases:

For Case 1.

Input IP Address: 192.168.2.1
Subnet Mask: 255.255.255.0

Output will return the Network Block: 192.168.2.0
Host ID: 0.0.0.1

If you give invalid IP address nothing is returned.

For Case 2.

Log Input:

<DATE> <LOG LEVEL> [<USER>:<FUNCTION>(:<SUBFUNCTION>)] <MESSAGE>
2003-07-08 16:49:45,896 ERROR [user1:mainfunction:subfunction] We have a problem
2003-07-08 16:49:46,896 INFO [user1:mainfunction] We don't have a problem
2003-07-08 16:49:45,896 CRITICAL [user1:mainfunction:subfunction] We have a problem
2003-07-08 16:45,896 ERROR [user1:mainfunction:subfunction] We have a problem
2003-07-085 16:45:13,896 ERROR [best user ever:mainfunction:subfunction] We have a problem

Log output:
<Date> <Log Level> <User> <Main Function> <Sub Function> <Logged Message>
2003-07-08 16:49:45,896 ERROR user1 mainfunction subfunction We have a problem
2003-07-08 16:49:46,896 INFO user1 mainfunction We don't have a problem

It will display the Date, Log level, user, Main function, sub function and logged messages seperated by space.
Following validations are done here:
Log level will be from either of these 3: ERROR, INFO and DEBUG.
Time should have minutes and seconds, if not that log is ignored.
User shouldn't have spaces in between.
Subfunction is not mandatory


