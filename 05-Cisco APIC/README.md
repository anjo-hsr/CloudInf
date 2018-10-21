# Cisco APIC python configuration program via Ciscos HTTP REST API
## Note, this is a Python 3 project
Run the main.py file under ./src/ and use the defaults if not sure how to configure the script. By default the user
_group1_ and the given password for this user will be used.  
Note, that all the needed JSON files are located under ./src/_json 
---
Please go through the following steps to run the script:
* Install a venv (virtual environment). To do this please follow these steps in PyCharm:
  1. Open the project 05-Cisco APIC in Pycharm.
  2. Go via File &rarr; New Project &rarr; _Pure Python_ &rarr; Select for Location the current project folder and under
Project Interpreter select **Python 3.x** as the base interpreter &rarr; Confirm the upcomming warning with **No** &rarr;
Start the project in the current window.
* Install **requests** into the venv. To do this please follow these steps in PyCharm:
  1. Open Settings... _(Ctrl. + Alt. + S)
  2. Navigate to _Project: 05-Cisco APIC &rarr; Project Interpreter_
  3. Add a new package with the **+** icon and install there the package *requests*