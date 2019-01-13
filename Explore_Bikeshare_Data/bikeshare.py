import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = []
for key in CITY_DATA:
  cities.append(key)

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday' , 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input('Enter a city out of (chicago, new york city, washington) ' \
                     + 'to explore the data for ?\n'))
    city = city.strip().lower()
    print(city)
    while city not in cities:
      print('You must enter a city from given list.')
      city = str(input('Enter a city out of (chicago, new york city, washington) ' \
                       + 'to explore the data for ?\n')).lower()
      city = city.strip().lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input('Enter a month out of (all, january, february, march, april, ' \
                      + 'may, june) to explore the data for ?\n'))
    month = month.strip().lower()
    while month not in months:
      print('You must enter a month from given list.')
      month = str(input('Enter a month out of (all, january, february, march, april, ' \
                        + 'may, june) to explore the data for ?\n'))
      month = month.strip().lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input('Enter a day of week out of (all, monday, tuesday, wednesday, ' \
                    + 'thrusday, friday, saturday, sunday) ?\n'))
    day = day.strip().lower()
    while day not in days:
      print('You must enter a day from given list.')
      day = str(input('Enter a day of week out of (all, monday, tuesday, wednesday, ' \
                      + 'thrusday, friday, saturday, sunday) ?\n'))
      day = day.strip().lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        
        month = months.index(month)
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]-1
    print('Most common month: ', months[common_month])


    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week: ', common_day_of_week)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]
    print('Most common start hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common Start Station: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common End Station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End_Station'] = df['Start Station'] + ' - to - ' + df['End Station']
    frequent_trip = df['Start_End_Station'].mode()[0]
    print('Most frequent combination of start station and end station trip: \n', frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Trip Duration'] = pd.to_numeric(df['Trip Duration'], errors='raise', downcast='float')
    
    total_travel_duration = (df['Trip Duration'].sum())/60
    mean_travel_duration = (df['Trip Duration'].mean())/60
             
    # TO DO: display total travel time
    print('Total travel time {} minutes'.format(str(round(total_travel_duration,2))))

    # TO DO: display mean travel time
    print('Mean travel time {} minutes'.format(str(round(mean_travel_duration,2))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type  = df.groupby('User Type')['User Type'].count()

    print('Counts of User Types:')
    print(count_user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns.values.tolist():
        count_gender  = df.groupby('Gender')['Gender'].count()
        print('\nCounts of gender:')
        print(count_gender)
    else:
        print('\n Gender field is not available for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns.values.tolist():
        df['Birth Year'] = pd.to_numeric(df['Birth Year'], errors='raise', downcast='integer')
        
        earliest_bith_year = int(df['Birth Year'].min())
        recent_bith_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest birth year: ', earliest_bith_year)
        print('Most recent birth year: ', recent_bith_year)
        print('Most common birth year: ', common_birth_year)
    else:
        print('\n Birth Year field is not available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_next_5_row(df,n_rows,row_count):
    if n_rows+5 > row_count:
        print(df.iloc[n_rows:row_count])
        print('End of data set. No further raw data to see.')
    else:
        print(df.iloc[n_rows:n_rows+5])

    show_raw_data = str(input('Whould you like to further see raw data? (enter y/n)\n'))
    show_raw_data = show_raw_data.strip().lower()

    if show_raw_data == 'y':
        n_rows += 6
        display_next_5_row(df,n_rows,row_count)
    else:
        return None


def display_data(df):
    # TO DO: display top 5 rows
    n_rows = 0
    show_raw_data = str(input('Whould you like to see raw data? (enter y/n)\n'))
    show_raw_data = show_raw_data.strip().lower()
    while show_raw_data not in ['y','n']:
      print('Please enter valid input y/n')
      show_raw_data = str(input('Whould you like to see raw data? (enter y/n)\n'))
      show_raw_data = show_raw_data.strip().lower()

    if show_raw_data == 'y':
        row_count = df.shape[0]
        display_next_5_row(df,n_rows,row_count)
    else:
        return None

    print('-'*40)


def main():
    
    
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)
        
        if df.shape[0] > 0:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_data(df)
        else:
            print('There is no relevant data. Please choose some other filters')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
