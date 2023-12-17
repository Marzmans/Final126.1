'''
Checklist items that I completed in consolidation project:
1.6 - You can run a Python script from a command line using additional arguments.
3.17 - Imported a module I created myself.
3.18 - I used sys.argv for user input at command line
3.20 - Wrote results of program out to a file
3.21 - In my with open statement in my ciphers, I used append mode on 'with open statement' to append results of the program to a file
4.9 - raised an error and provided a helpful error message to the user
5.7 - Creating a List Manually
5.8 - Appending an item to a list
5.10 - Removing an item from a list
5.15 - Creating a dictionary manually
5.17 - Accessing Keys of a dictionary
5.18 - Iterating through items of a dictionary
5.19 - Updating values in dictionairy systematically
6.1 - I had a README for the last project
6.2 - I wrote documentation comments at the top of my script
6.5 - I wrote sufficient and useful documentation
6.7 - I chose an appropriate license for my last project (MIT)
Git - I completed all of the Git requirements for the last project

To Do in This Project: 
NumPy and Pandas 8.1-4
Webscraping and JSON - 10.1-3 

In my second final project I will cover:
3.19, 5.9, 5.11, 5.12, 5.13, 5.14

'''

import numpy as np
import pandas as pd
import requests as req
from bs4 import BeautifulSoup #10.2Used bs4 to scrape
import os

#10.1 - I want to scrape populations of cities in India with over 1mil as it the most populated country
url="https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"

response=req.get(url)

print(response.text)

#10.3 - Used polite code to scrape
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', attrs={'class':'wikitable'})

#8.2 - Below I use tables from the webscraped wikipage to read data into data frames instead of csv 
df1=pd.read_html(str(table)) #reading in html data into list
type(df1)

df1=pd.DataFrame(df1[0]) #making into dataframe object
type(df1)

print(df1.head())

#drop unwanted columns
data = df1.drop(["Rank", "Ref", "Population (2001)[3][a]"], axis=1)
#rename cols
data = data.rename(columns={"State or union territory": "State","Population (2011)[3]": "Population"})

print(data.head())
print(data.columns)

data['Population'] = pd.to_numeric(data['Population'])

#Below are 8.1 items
median = int((data['Population'].median()))
average = int((data['Population'].mean()))
total = int((data['Population'].sum()))
median_population = str(median) + " People"

print(median_population)

data_sorted = data.sort_values(by='Population', ascending=False)
top_5_states = data_sorted.head(5) #store the highest 5 population states and cities
print(top_5_states)

#8.3 items below
above_med = data[data['Population'] > median]
above_avg = data[data['Population'] > average]
print(above_avg)
print(above_med)

#8.4 items below
csv_file_path = os.path.join(str(os.getcwd()), 'data_output.csv')
print(csv_file_path)

data.to_csv(csv_file_path, index=False)

above_med_csv_path = os.path.join(str(os.getcwd()), 'above_med_population.csv')

above_avg_csv_path = os.path.join(str(os.getcwd()), 'above_avg_population.csv')

above_med.to_csv(above_med_csv_path, index=False)

above_avg.to_csv(above_avg_csv_path, index=False)

