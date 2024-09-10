****Overview
This project involves a comprehensive automation and data processing system integrating various technologies to streamline data handling, validation, visualization, and user interaction. 
The project utilizes Blue Prism for automation, Python for data validation, and visualization, and Flask for user interface interactions. 

The following sections detail the technical aspects and workflow of the project.

****Automation Workflow

Data Validation
Python Script: The validation.py script is employed for data validation using the Pandas library.
Functionality: Validates the content of the existing dataset and updates the python graphs and tableau dashboard.
Scheduling: Executes automatically whenever a new Excel file is uploaded and is also scheduled to run daily at 9:00 AM through Windows Task Scheduler.

Data Visualization
Libraries: Uses Matplotlib and Seaborn for data visualization within Python.
Visualization Types: Includes charts and graphs to represent data insights effectively.
Tableau Integration: Connects visualizations to Tableau for advanced graphical representations.
Automatic Updates: Tableau Cloud is configured to automatically refresh and update the dashboard every time the underlying CSV data file is updated.

Web Interface
HTML and Flask: Provides a web interface for users to upload Excel files.
Functionality: The web interface allows users to upload an Excel file through a browser, which is then appended to the existing CSV dataset.
Data Checks: The Flask app performs various checks before appending the data to ensure data integrity and consistency.

Blue Prism Automation
Excel File Handling: Blue Prism monitors a local directory for new Excel files.
Automation Features: Executes the main.py script when a new file is detected.
User Interaction: Automatically responds with ‘y’ to prompts for file uploads, interacts with the local server, and completes the file upload process.

Windows Task Schedular Automation
A bash script "auto.bat" is scheduled to run everyday at 3 p.m. using Windows Task Schedular. It automatically responds with ‘n’ to prompts for file uploads.
The validation and data representation scripts are run to keep evrything up-to-date.

Detailed Workflow
File Detection: Blue Prism detects the presence of new Excel files in the specified folder.
Script Execution: Initiates the execution of main.py, which automates data handling tasks.
AcceptExcel.py: Supports upload of excel file, perform checks on it and appends it to csv.
Data Validation: validation.py performs data validation on the newly updated data.
Visualization Update: Matplotlib and Seaborn visualize the updated data, and Tableau Cloud refreshes the dashboard to reflect the latest data.

Setup Instructions
Blue Prism: Install and configure Blue Prism to monitor the designated folder and execute main.py.
Windows Task Scheduler: Set up tasks to run validation.py daily and to manage other scheduled tasks.
Python Libraries: Install necessary Python libraries using pip install pandas matplotlib seaborn tabpy.
Tableau: Publish dashboards to Tableau Cloud and configure automatic data source refresh.
Flask App: Set up the Flask app for file uploads and ensure it performs the necessary data checks.

Dependencies
Python 
Pandas
Matplotlib
Seaborn
TabPy
Flask
Blue Prism
Tableau Server/Cloud
Conclusion
This project integrates automation, data validation, visualization, and user interface components to create a seamless data processing pipeline. By leveraging Blue Prism for automation, Python for data handling, and Tableau for visualization, this solution ensures efficient and accurate data management.
