#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Import Libraries
from datetime import datetime
import csv

client_name = input("Please enter the name of the client: \n")
task_name = input("Please enter the name of the task you are undertaking: \n")

# Set the date of entry as the system's current date
current_date = datetime.now().date()

# Take users input on the start and stop times
start_time = input('Enter the time you started in the format Hour:Minute AM : ')
stop_time = input('Enter the time you ended in the format Hour:Minute PM : ')
time_format = '%I:%M %p' # this is the Hour:Minute AM/PM format


# Convert the string format time entered by the user into datetime 
# format using the datetime.strptime()
start_time = datetime.strptime(start_time, time_format)
stop_time = datetime.strptime(stop_time, time_format)
