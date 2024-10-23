import json
import os
from datetime import datetime, timedelta
from prettytable import PrettyTable

def load_plant_data(filename):
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the JSON file
    filepath = os.path.join(current_directory, filename)
    
    with open(filepath, 'r') as file:
        return json.load(file)

def creating_watering_schedule(plants, start_date, num_weeks=12):
    # Dictionary to keep track of watering days
    schedule = {plant['name']: [] for plant in plants}
    
    # Total number of days we need to schedule for
    total_days = num_weeks * 7 #num_weeks is already stated as 12
    
    # Create a list of weekdays (0 = Monday, 1 =Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6=Sunday)
    weekdays = [0, 1, 2, 3, 4] # Plants are only watered on weekdays

    # Iterate over each plant, determining watering days
    for plant in plants:
        watering_frequency = plant['watering_frequency']  # Get the watering frequency for the plant from the json data
        current_date = start_date
        
        # Start with the first watering day
        schedule[plant['name']].append(current_date)
        
        # Generate upcoming watering dates until total days is reached
        while current_date <= start_date + timedelta(days=total_days):
            # Move to the next watering date based on the frequency
            current_date += timedelta(days=watering_frequency)
            
            # skipping weekends
            while current_date.weekday() not in weekdays:
                current_date += timedelta(days=1)
            
            # Only add the date if it's within 12 weeks, although this could be changed if the schedule needed to be longer (along with num_weeks variable)
            if current_date <= start_date + timedelta(days=total_days):
                schedule[plant['name']].append(current_date)
    
    return schedule

# Formatting and printing schedule using PrettyTable
def print_schedule(schedule, num_weeks):
    
    table = PrettyTable()
    
    # Defining table header
    table.field_names = ["Week"] + list(schedule.keys())
    
    # Populate the table with weeks and watering dates
    for week in range(num_weeks):
        week_dates = [f"Week {week + 1}"]  # Start with the week number
        for plant in schedule.keys():
            # Check if there are watering dates for the plant in this week
            week_start = datetime.now() + timedelta(weeks=week)
            week_end = week_start + timedelta(days=7)
            dates_in_week = [date.strftime('%Y-%m-%d') for date in schedule[plant] if week_start <= date < week_end]
            
            # Formatting the dates or using an X if there is no dates, indicating the plant doesnt need to be watered that week
            week_dates.append(", ".join(dates_in_week) if dates_in_week else "X")
        
        # Adding that week row to the table
        table.add_row(week_dates)
    
    print(table)

def main():
    plants = load_plant_data('plant_sample_data.json')  # Ensure the correct filename

    """
    CHANGE THE STRING ABOVE TO THE JSON FILE THAT YOU WANT TO USE, MAKE SURE THE JSON FILE IS IN THE SAME FOLDER AS THIS PYTHON FILE.
    I have created another JSON file with example plant data as additional test data.
    """
    
    # Geting next Mondays date
    today = datetime.now()
    next_monday = today + timedelta(days=(7 - today.weekday() % 7))

    watering_schedule = creating_watering_schedule(plants, next_monday)

    print_schedule(watering_schedule, num_weeks=12)

if __name__ == '__main__':  # Ensure that the main() function runs only when the script is executed directly, allowing the code to be reused in other scripts without running the main functionality automatically
    main()





