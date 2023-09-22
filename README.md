# IDS_706 - Data Engineering Systems 
## Individual-Project 1 : Continuous Integration using GitHub Actions of Python Data Science Project

[![OnInstall](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/actions/workflows/test.yml)
***

### Goal of the Project
Individual-Project 1 modifies [this existing Github template](https://github.com/afraa-n/IDS_706-Data_Engineering_Systems) by handling the loading and manipulation of a Global Country Information Dataset 2023 stored in a `.csv` file using the Pandas library. This entails extracting meaningful insights from the dataset by generating descriptive statistics. This project also represents the relationship between Birth Rate and Infant Mortality Rate across countries worldwide as a scatter plot. This project also identifies and presents the details of the country with the highest Infant Mortality Rate from the dataset. 

The accompanying Makefile automates essential development tasks, making it easier for developers to maintain code quality, run tests, and streamline the development workflow.

Dataset used: [Global Country Information Dataset 2023 Data Set](https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023)

***

### YouTube Link to the Demo

Link: [https://www.youtube.com/watch?v=7gZjw3W69Kc](https://www.youtube.com/watch?v=7gZjw3W69Kc)

***

### Structure of this Project

1. Jupyter Notebook - `desc_stats.ipynb` (under src):
   - This notebook contains cells that perform descriptive statistics using Pandas Library.
   - It is also tested using nbval plugin for pytest.

2. Python Script - `script.py` (under src):
   - This script performs the same descriptive statistics (as *desc_stats.ipynb*) using Pandas Library.

3. Python file - `lib.py` (under src):
   - This file contains the common code shared between the *script.py* and *desc_stats.ipynb*.

4. `Makefile`:
   - Runs all tests (including the notebook, script and lib).
   - Formats code with Python black.
   - Lints code with Ruff.
   - Installs code via:  pip install -r requirements.txt

5. `test_script.py`:
   - This file is used to test the python script - *script.py*

6. `test_lib.py`:
   - This file is used to test the python file - *lib.py*

7. `requirements.txt`:
   -  This file lists all the external libraries and dependencies required for the project to run correctly. 

8. GitHub Actions:
   - Performs all four Makefile commands with badges for each one in the README.md

***
### Commands to Run the Repo

To run the project, you can use the Makefile and follow these commands:
1. ```
   # To install the required the python packages
   make install
   ```
2. ```
   # To check code style
   make lint
   ```
3. ```
   # To run tests
   make test
   ```
4. ```
   # To format the code
   make format
   ```
5. ```
   # To perform all the above tasks (install, test, format, lint)
   make all
   ```

***

### Result

1. On running ```make lint```:

![make lint](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/assets/143756865/6493bb36-19c5-427b-9b37-d0513f4fe9bd)

2. On running ```make test```, it passes the test:

![make test 1](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/assets/143756865/bfa12827-6271-4e73-be87-21f7d6df89d7)
![make test 2](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/assets/143756865/60e6e999-94ca-46b6-984b-49bf164f2203)

3. On running ```make format```:

![make format](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/assets/143756865/997903ed-2969-438a-aa92-8aaabc263844)

***

### Output from Descriptive Statistics

On running the test script/notebook, it displays the descriptive statistics from the dataset as well as the country with the highest infant mortality rate. This file generates and displays the plot for Birth Rate vs Infant Mortality Rate. It also ensures that valid values are returned from the scripts using the assert statements.

![desc stats](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/assets/143756865/196bbf2b-d2c1-4382-872a-8f3f9419d9b7)
![infant mortality stats](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/assets/143756865/efb37169-6de8-4ede-bead-b848a34406c0)

***

### Data Visualization (Birth Rate vs Infant Mortality scatter plot)

![plot](https://github.com/nogibjj/afraa_noureen-IDS_706-Individual_Project_1/assets/143756865/b9a0f5d2-15ee-4a91-b154-0b39cf374a24)

***
