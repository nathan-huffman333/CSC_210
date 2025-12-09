# city_data.py
# A class for storing a city's population data
# Starter Code from CSC 210
# Modified by: Nathan Huffman (with help from Anthony Frederick and ChatGPT)

class CityData:
    def __init__(self, name, start_year, end_year, data): # The constructor for the CityData class. Comprised of the name, start year, end year, and population data.
        self._name = name
        self._start_year = start_year
        self._end_year = end_year
        self._data = data
    
    @property 
    def name(self): # Function to return the name of the city as a string.
        return self._name
    
    @property
    def start_year(self): # Function to return the start year as an integer.
        return int(self._start_year)
    
    @property
    def end_year(self): # Function to return the end year as an integer.
        return int(self._end_year)
    
    @property # This function was made with the help of ChatGPT.
    def max_year(self): # Function to return the year with the maximum population by finding the index of the list with the max population and adding it to the start year.
        index = self._data.index(max(self._data)) 
        return self._start_year + index 

    @property # This function was made with the help of ChatGPT.
    def min_year(self): # Function to return the year with the minimum population by finding the index of the list with the min population and adding it to the start year.
        index = self._data.index(min(self._data)) 
        return self._start_year + index

    def __getitem__(self, year):
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year < self._start_year or year > self._end_year:
            raise IndexError("Year out of range")
        return self._data[year - self._start_year]
    
    # This function was made with the help of ChatGPT.
    def population_growth(self, start, end): # Function to calculate and return the total population growth between the two years provided.
        if start < self._start_year or end > self._end_year: # Throws an error if the provided years are out of range of the data.
            raise ValueError("Year out of range")
        return self._data[end - self._start_year] - self._data[start - self._start_year] 