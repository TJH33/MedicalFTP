# Medical Data Evaluation
This project simulates a scenario where data, in a CSV format, is stored on an private FTP server and a client-side program is required to perform two functions:
* Automated Collection of the CSV files at regular intervals.
* A UI application which can retrieve the CSV files from a given point in time.

Alongside this, the CSV files have to meet given requirements in order to be considered valid.

Due to Git configuration issues, the blank username commits are **Thomas H2**

## Running The Project
1. Install the project's requirements using pip from the requirements.txt

        pip install -r requirements.txt

2. Start the FTP server, put your desired directory you would like to point your FTP server to and your IP address.

        python ftp_server.py

3. To start the project, run the python command below.

        python main_gui.py