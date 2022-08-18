# <u>FTP Server Report</u>

# <u>Team</u>

Charlie S1 - QWatt
Thomas H2 - TJH33
Oscar JM - Kynemo
Ben S1 - b3nns

# <u>Tasks</u>
Python Server - Ben S1 & Thomas H2
GUI -  Thomas H2 & Charlie S1
CSV Validator - Oscar JM
Scheduler - Thomas H2
Report - Ben S1

# <u>Project Planning</u>

To begin our project, our met and worked on creating a plan for doing the project. Thomas H2 created a breakdown of tasks.

1 - Client-Side Application Development; GUI Development and scheduled cron-job scrip.
2- Data processing; Batch ID validation, readings validation and directory validation.

In our first group meeting, we discussed our strengths with regards to programming and came to the conclusion that our FTP server would be written in Python as this is a language we are all familiar and comfortable with. In this meeting, we agreed on who would complete what tasks in the project breakdown, ensuring no one was given too much work and no one given too little.

In this meeting we also agreed on a schuedule for our team to meet once a week to discuss the progress we had made and if we needed assistance on our tasks that we had agreed to do previously. 

# <u>Project Execution </u>
<u>FTP Server</u>

The FTP server was completed by Thomas H2 and Ben S1. The code begins with importing the required handlers and servers to run an FTP server in python, these were imported from pyftpdlib. The port that the server listens on is 2121 with a default username and password assigned to it.v

In the main body of the code, an authorizer defines new users as having full read and write permissions, this allows admins to add new users and allows the new users to make full use of the FTP server. Below this the server has a banner which says what it is and asks that the server is not misused. After this a range of ports are specified to be used for passive connection. At the end of the main body, the code then defines the maximum number of connections allowed to the server at each time and the maximum number of connections from the same IP.

<u>CSV Validator</u>

The csv_validator file was written by Oscar. It starts by opening the csv file and validating the header of the csv object in python matches the header which is expected. It then loops to check every line (apart from the header line) in the CSV for duplicate batch ids, invalid timestamps, invalid readings and if there is too many readings.

<u>Scheduler</u>

The Scheduler was created by Thomas H2. The purpose of the scheduler is to allow to admin of the FTP server to download files on a set schedule. To begin modules are imported from apscheduler and datetime to allow for scheduling of tasks and then ftplib is imported to allow FTP connection.

The function then begins with scheduling an event at a chosen date and time to begin the job. If there is already another job running then the program wont run again. The job then begins downloads the file from the FTP server using an annoymous login.

<u>Main GUI</u>

The Main GUI was created by Thomas H2. The overall aim of the GUI is to make using the FTP server possible for people who may have never used a CLI in their life. The GUI code begins with multiple imports from tkinter, scheduler, datetime and ftplib. The main functions then begins with setting the size and title for the GUI window. Next there is a label created which shows the user the two options they have with the GUI, direct download or to schedule a download. Next up there is a calander which allows the user to choose a date and time for when they want a download to be compleeted. The function ends with getting the files from the server and logging in using annonymous credentials.

# <u>Report</u>
The report was written by Ben S1. This was done once all the coding was complete and was completed using the commentary on each file along with what was said at meetings.

# <u>Team Work</u>
Overall our team worked well together and gelled well. We didn't have any issues when choosing what tasks would be done by who and worked hard on our respective roles. In terms of communication our team done this well, being able to get ahold of each other when needed and not having any issues asking for help.

For team leadership our team didn't outright choose a leader and trusted each other to work responsibly and to the best of our abilities. This allowed everyone to work well without any one person trying to oversee everything.

One of the problems our team encountered was trying to work this project in with our personal projects and our busy lives in general. We resolved this by doing as much work as we could when we could without burning ourselves out and setting time aside for both projects. Another problem we encountered was not using GitHub as much as we should've, it meant there was a bit of a rush at the end to get all information and files in the one area. 

# <u>Conclusion</u>
Overall we believe the solution we have delivered is a simple, yet effective and delivers on the project deliverables. The FTP server has security features and the GUI means anyone who isn't familiar with CLI can access it. 
