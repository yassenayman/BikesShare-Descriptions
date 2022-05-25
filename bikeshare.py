import time
import pandas as pd
import numpy as np
import datetime as dt

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
     city= input('Enter city u want explore about? chicago,new york city or washington? ').lower()
     if city in CITY_DATA:
         break
     else:
      print("Sorry , invalid input,try again ^-^ ")

    # get user input for month (all, january, february, ... , june)
    month=input('Second Step, Enter The month u want to explore')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Last Step, Enter the day u want to Explore')

    print('-'*40)
    return city, month, day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load
    df=pd.read_csv(CITY_DATA[city])
    # convert
    df['Start Time']=pd.to_datetime(df['Start Time'])
    # Extract month,hour,day
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour
  #  popular_hour =df['hour'].value_counts()
   # print('Most Frequent Start Hour:', popular_hour)

    return df


def time_stats(df):

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].value_counts().idxmax()
    print("The Most Common Month Is:", common_month)
    # display the most common day of week
    common_day=df['day'].value_counts().idxmax()
    print("The Most Common Day Is:", common_day)
    # display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    common_start_station=df['Start Station'].value_counts().idxmax()
    print("The Most Common Start Station Is: ",common_start_station)

    # display most commonly used end station
    common_end_station=df['End Station'].value_counts().idxmax()
    print("The Most Common End Station Is: ", common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_startend_station = df[['Start Station', 'End Station']].mode().loc[0] #combine
    print("The most commonly used start station and end station : "\
          .format(most_common_startend_station[0], most_common_startend_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel=sum(df['Trip Duration'])
    print(travel)

    # display mean travel time
    mean=np.mean(df['Trip Duration'])
    print(mean)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df['User Type'].value_counts()
    print(user_types)
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print(user_gender)


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year_birth = df['Birth Year'].min()
        print( earliest_year_birth)

        most_recent_year=df['Birth Year'].max()
        print( most_recent_year)

        most_common_year=df['Birth Year'].value_counts().idxmax()
        print( most_common_year)
    print("\nThis took %s seconds." % (time.time()-start_time))
    print('-'*40)


def display_data(df):
    """Displays some raws from data."""

    view_data = input("Would you like to view some rows of individual trip data? Enter yes or no?").lower()
    start_loc:int =0
    while (True):
        if view_data!="yes":
            break
        row=int(input("Enter num of raws you want to see: "))
        End=row + start_loc
        print(df.iloc[start_loc + End])
        start_loc += row
        view_display = input("Do you wish to continue?: ").lower()
        if view_display !='yes':
            return

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
            print("Thanks for ur time")
            break




if __name__ == "__main__":
	main()