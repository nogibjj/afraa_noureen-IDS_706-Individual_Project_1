# IDS_706-Data_Engineering_Systems: : Mini-Project 1

[![CI](https://github.com/afraa-n/IDS_706-Data_Engineering_Systems/actions/workflows/cicd.yml/badge.svg)](https://github.com/afraa-n/IDS_706-Data_Engineering_Systems/actions/workflows/cicd.yml)

***

#### This template includes:
1. **.devcontainer**: configuration folder which contains a **Dockerfile** and **devcontainer.json**.
   - **Dockerfile**: specifies the instructions for building a Docker container image that will be used as the development environment.
   - **devcontainer.json**: defines the settings for the development container, such as which Dockerfile to use and environment variables.
3. **Makefile**: contains a set of rules that define how to compile source code, run tests, and perform other development tasks. 
4. **requirements.txt**: lists all the external libraries and dependencies required for the project to run correctly. It helps ensure that everyone working on the project uses the same versions of libraries, which is important for reproducibility and compatibility.
5. **workflows**: contains configuration files for defining and automating various tasks, processes, and workflows within the GitHub repository.
6. **main.py**: contains a basic function which displays system info.
7. **test_main.py**: python file to test the function in main.
8. **README**: gives developers a detailed description of the GitHub project.
9. **.gitignore**: specifies files and directories that should be ignored by Git, the version control system used by GitHub. Changes in files or directories in the .gitignore file will not be tracked by Git, and they will not be included in the version history.

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

