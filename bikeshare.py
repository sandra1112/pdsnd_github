import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

# test comment change
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
    city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()
    while city not in ['chicago', 'new york', 'washington']:
        city = input('Select only one of mentioned cities: ') 
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month - January, February, March, April, May, June or all? ').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('Choose only one of provided text values: ') 
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all? ').lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input('Choose only one of provided text values: ')

    #print('city is: ', city, ', month is: ', month, ' and day is: ', day)  
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
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month']==month] 
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()] 
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mode_mth = df['month'].mode()[0]
    print('The most common month is: ', mode_mth)

    # TO DO: display the most common day of week
    mode_d = df['day_of_week'].mode()[0]
    print('The most common day of the week is: ',mode_d)

    # TO DO: display the most common start hour
    mode_h = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is: ',mode_h)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_str_st = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', mode_str_st)

    # TO DO: display most commonly used end station
    mode_end_st = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', mode_end_st)

    # TO DO: display most frequent combination of start station and end station trip
    mode_com_station = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip is: \n', mode_com_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time in hours: ', float(total_time/3600))
    
    
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average travel time in minutes: ', float(avg_time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Counts of user types: \n', user_type)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('Counts of genders: \n', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    min_year = df['Birth Year'].min()
    max_year = df['Birth Year'].max()
    mode_year = df['Birth Year'].mode()[0]
    print('Oldest passanger was born in: ', int(min_year))
    print('Youngest passanger was born in: ', int(max_year))
    print('Most passangers were born in: ', int(mode_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays first five rows on bikeshare users."""
    
    print('\nDisplaying 5 lines of raw data...\n')
    start_time = time.time()
    
    #Ask user if they want to see 5 lines of data
    x=0
    while True:
        disp_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n').lower()
        if disp_data not in ['yes', 'no']:
            print('Please enter only Yes or No answer')
        elif disp_data == 'yes':
            print(df[x:x+5])
            x+=5
        else:
            break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

  
def new_display_data(df):
    """Displays first five rows on bikeshare users."""
    
    print('\nDisplaying 5 lines of raw data...\n')
    start_time = time.time()
    
    #Ask user if they want to see 5 lines of data
    start=0
    end=5
    while True:
        disp_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n').lower()
        if disp_data not in ['yes', 'no']:
            print('Please enter only Yes or No answer')
        elif disp_data == 'yes':
            print(df.iloc[start:end,:9])
            start+=5
            end+=5
        else:
            break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
	raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Goodbye!')
            break

if __name__ == "__main__":
	main()
