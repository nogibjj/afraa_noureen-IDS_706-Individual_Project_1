# IDS_706 - Data Engineering Systems 
## Mini-Project 2 : Pandas Descriptive Statistics Script

[![CI](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/actions/workflows/cicd.yml)

***

### Goal of the Project
Mini-Project 2 modifies [this existing Github template](https://github.com/afraa-n/IDS_706-Data_Engineering_Systems) by handling the loading and manipulation of a movies dataset stored in a `.csv` file using the Pandas library. 

This entails extracting meaningful insights from the dataset by generating descriptive statistics. This project also represents the relationship between popularity ratings and average ratings out of 10 as a scatter plot. This project also identifies and presents the movies with the highest ratings from the dataset. 

The accompanying Makefile automates essential development tasks, making it easier for developers to maintain code quality, run tests, and streamline the development workflow.

Note: Summary Report on the dataset is generated as a `.html` file.  

Dataset used: [Top-Rated Movies Data Set](https://www.kaggle.com/datasets/khalidalam980/top-rated-movies-data-set)

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

![make lint](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/0d61460a-1e5e-434d-ab62-2e067781663d)

2. On running ```make test```, it passes the test:

![make test](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/fc55736c-ab86-4b7e-95f6-4c695adc1c37)

3. On running ```make format```:

![make format](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/e9f384ce-2d4b-49e4-af50-bec7981e76d7)

***

### Output from test_main.py

On running test_main.py, it displays the descriptive statistics from the dataset as well as the top rated movies. This file generates and displays the plot for popularity vs vote_average. It also ensures that there is a valid value returned from display_highest_votes() (from main.py) using the assert statement.

![test_main 1](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/08cab468-0621-441d-b76a-1c72306c77f8)
![test_main 2](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/528f973e-7d6c-4a74-9250-4ee75f343129)

***

### Data Visualization (popularity vs vote_average scatter plot)

![graph](https://github.com/nogibjj/afraa_noureen-IDS_706-Mini_Project_2/assets/143756865/ca9213e0-95c3-4a9a-b6f8-ceec80b95a61)

***
