# city_reader.py
# Read the city data from a CSV File
# Starter Code from CSC 210
# Modified by: Nathan Huffman (with help from Anthony Frederick and ChatGPT)

import csv
from csv import DictReader
from city_data import CityData

def read_city_from_csv(file_path, city_name):
    years = [] # List to store the years for the specific city.
    populations = [] # List to store the populations for the specific city.
    
    DictReader(open(file_path)) 
    with open(file_path, mode='r') as csv_file: # Opens the CSV file for reading.
        csv_reader = csv.DictReader(csv_file) # Uses DictReader to read the CSV file into a dictionary format.
        for row in csv_reader:
            if row['City'] == city_name: # Checks if the CSV row matches the city name provided before assigning values to the lists.
                year = int(row['Year']) # Converts the year to an integer before appending it to the list.
                years.append(year)
                population = int(row['Population']) # Converts the population to an integer before appending it to the list.
                populations.append(population)
    
    if not years: # If the years list is empty, it means the city was not found in the CSV file, so an error is raised.
        raise ValueError(f"City '{city_name}' not found in {file_path}")
    
    # This return statement was made with the help of ChatGPT.
    return CityData(name = city_name, start_year = min(years), end_year = max(years), data = populations) # Creates and returns a CityData object with the appropriate data.