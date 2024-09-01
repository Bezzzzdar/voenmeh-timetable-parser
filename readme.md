# About app:
This application is a parser of the schedule by groups for students of BSTU "Voenmeh"
The reason for creating the application is that the schedule on the official website is not the most convenient and understandable. I am also tired of transferring the schedule from the website to a separate application every semester.  

# Author
Student of group **I911S**, **Rastegaev Ivan**
Corporate email - **i911s19@voenmeh.ru**

# Python dependencies:
* PyQt5
* beautifulsoup4
* requests
* lxml

# Virtual environment (execute from the project root): 
* `cd voenmeh-timetable-parser`
* `python -m venv .venv`
* `.\.venv\Scripts\Activate.ps1`
* `.\.venv\Scripts\pip install -r requirements.txt`

# How-to build the project (Windows 10):
* First you net to setup the virtual environment (see previous section)
* Then run in terminal:
`.\.venv\Scripts\pyinstaller.exe --onefile --noconsole -n 'BSTU Voenmeh Timetable' --icon=.\app\icons\timetable_icon.ico .\app\src\main.py`

# TODO List:
* Schedule by teacher
* Сustom notes for any lesson
* Editing the timetable (**in progress**)
* Docker
* Porting to Android and IOS