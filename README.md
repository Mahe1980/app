# App

This application is developed using Flask Python 3 Framework. This application returns sum of list elements from the url `http://localhost:5000/total`.

The following folders contain: 
 - `src` source for the application.
 - `test` unit tests for the application.   


### Setting up the virtual environment

1. Update `PYTHONPATH` to include current project

       export PYTHONPATH=${PYTHONPATH}:<Project Root Directory>

2. Ensure that Python version 3.6+ is installed on the system.

3. Create a new virtual env specific to this project e.g.

        python -m venv  .venv

   where `.venv` is the folder the virtual environment is configured in.  `.venv` is only an example, it can be a path as well.

4. Activate the virtual environment e.g.

        source .venv/bin/activate

5. Navigate to project root directory and run the below command to install necessary python modules

        pip install -r requirements.txt
        
### Test

1) From the project root directory, run `python -m pytest tests`

### Execution

1) Navigate to `<project root>/src` and run `python app.py`

2) Open browser and go the URL `http://localhost:5000/total`