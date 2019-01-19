# Data Scientist Foundations Nanodegree
# Exploring Data
## Project: Explore Bikeshare Data

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)


If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included. 

### Objective

The objective of this project is to creating an interactive application that allow the user to explore the Bike Share Data. Allowing user to see the stats like 

1. Popular times of travel

    most common month
    most common day of week
    most common hour of day

2. Popular stations and trip

    most common start station
    most common end station
    most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

    total travel time
    average travel time

4. User info

    counts of each user type
    counts of each gender (only available for NYC and Chicago)
    earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Run

In a terminal or command window, navigate to the top-level project directory `Explore_Bikeshare_Data/` (that contains this README) and run one of the following commands:

```bash
python bikeshare.py
```

The application will ask you question about what filters you want to apply on the data. Enter your chooses and application will provide you the stats by apploying your chooses on the data. 

### Data

The Bike Share datasets are provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. There are three city dataset files used:
    
    chicago.csv
    new_york_city.csv
    washington.csv

**Core Features**
1. Start Time (e.g., 2017-01-01 00:07:57)
2. End Time (e.g., 2017-01-01 00:20:53)
3. Trip Duration (in seconds - e.g., 776)
4. Start Station (e.g., Broadway & Barry Ave)
5. End Station (e.g., Sedgwick St & North Ave)
6. User Type (Subscriber or Customer)

