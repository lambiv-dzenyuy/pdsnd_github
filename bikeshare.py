import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


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
    
    #prompting user to input city
    city=input('choose which city you want to explore chicago, new york city or washington : ').lower()
    
    #making sure user inputs the a correct city name by checking if entered name is in CITY_DATA
    while city not in CITY_DATA:
        #if the entered name is not in CITY_DATA we continously prompt the user to re-enter on till one that matches our data is entered
        city=input('Make sure inputed the city name correctly please try again : ').lower


    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('Will you like like to filter by all month or a specific month. Choose (all, january, ..., june) : ')
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month=input('you might have enterd the month wrongly please try again : ').lower


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Will you like like to filter by all days or a specific day. Choose (all, monday, ..., sunday) : ')
    while day not in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturay', 'sunday']:
        day=input('please choose a correct day and try again : ').lower()


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
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    #return filtered dataframe to suit user choices
    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] =  pd.DatetimeIndex(df['Start Time']).month
    popular_hour = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    print('Most Popular MOnth is:',months[popular_hour-1])
    

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day=df['day_of_week'].mode()[0]
    
    print('Most common day of Week is : ', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour =df['hour'].mode()[0]
    
    print('Most Common Start Hour:', common_hour)





    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    common_start_station =df['Start Station'].mode()[0]
    
    print('Most Common Start Station:', common_start_station)

   


    # TO DO: display most commonly used end station
    common_end_station =df['End Station'].mode()[0]
    
    print('Most Commonly used End Station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_end_start_station =df[['Start Station', 'End Station']]
   
    most_common= (common_end_start_station['Start Station'] + ';' + common_end_start_station['End Station']).mode()[0]

    
    print('Most frequently  used Start and End Station:', most_common)
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df_time=df[['Start Time', 'End Time']]
    df_time['time']=pd.to_datetime(df_time['End Time'])-pd.to_datetime(df_time['Start Time'])
    total=df_time['time'].sum()
    print('The total travel time is ', total)
    # TO DO: display mean travel time
    mean=df_time['time'].mean()
    print('The mean travel time is ', mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('Here is a display of counts of all user types', user_types)


    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Here is a display of counts of all user Genders', user_types)
        
    except:
        print('No Information about gender is available for this city')
        

    


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        birth=df['Birth Year']
        
        earliest=birth.min()
        print('The earliest year of birth is ', earliest)
        
        most_recent=birth.max()
        print('The most recent year of birth is', most_recent)
        
        common=birth.mode()[0]
        print('The most common year of Birth is ', common)
    
    except:
        print('No Information about gender is available for this city')
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data=='yes' and start_loc != df.size):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
