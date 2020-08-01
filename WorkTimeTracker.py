#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import Libraries
from datetime import datetime
import csv

# Set the date of entry as the system's current date
current_date = datetime.now().date()

# Take users input on the start and stop times
client_name = input('Please enter the name of the client : ')
task_name = input('Please enter the name of the task you are undertaking : ')
start_time = input('Enter the time you started in the format Hour:Minute AM : ')
stop_time = input('Enter the time you ended in the format Hour:Minute PM : ')
time_format = '%I:%M %p' # this is the Hour:Minute AM/PM format

# Convert the string format time entered by the user into datetime 
# format using the datetime.strptime()
start_time = datetime.strptime(start_time, time_format)
stop_time = datetime.strptime(stop_time, time_format)

# Find the hours spend on a work during a day by dividing 
# the total seconds spent by 3600( i.e 3600 seconds makes 1 hour)
hours_spent = round(((stop_time - start_time).seconds) / 3600, 2)

# Calculate the amount of the money earned by the user in a day
pay_per_hour  = 5
amount_of_money = round(hours_spent * pay_per_hour, 2)

# Put the information for the user and program into a list named records
records = []

# Convert from datetime format to string using datetime.strftime
current_date = datetime.strftime(current_date, '%D')
start_time = datetime.strftime(start_time, time_format)
stop_time = datetime.strftime(stop_time, time_format)

# Add all information to the records list
records.append(current_date)
records.append(client_name)
records.append(task_name)
records.append(start_time)
records.append(stop_time)
records.append(hours_spent)
records.append(amount_of_money)

# Write records to the csv file using the csv module
with open('time_tracking_records.csv', mode = 'a') as time_tracking_records:
    record_writer = csv.writer(time_tracking_records, delimiter = ',')   
    record_writer.writerow(records)
	
# View the results
print ('\n')
print ('..'*40)
print ('Date : {}'.format(current_date))
print ('Total hours spent on the work : {}'.format(hours_spent))
print ("Amount of money earned for the day : ${:0,.2f}".format(amount_of_money))
print ('..'*40)
print ('Information written to records successfully')
