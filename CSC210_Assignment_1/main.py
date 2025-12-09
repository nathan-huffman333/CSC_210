# main.py
# Load city population data and draw a chart
# Starter Code from CSC 210

from city_reader import read_city_from_csv

def draw_city_population_charts(city_datas):
    import matplotlib.pyplot as plt

    for city_data in city_datas:
        years = list(range(city_data.start_year, city_data.end_year + 1))
        data = [city_data[year] for year in years]
        plt.plot(years, data, marker='o', label=city_data.name)

    plt.title("Population Growth")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.grid()
    plt.show()
    

def main():
    allentown = read_city_from_csv('pop.csv', 'Allentown')
    reading = read_city_from_csv('pop.csv', 'Reading')
    for year in range(allentown.start_year, allentown.end_year + 1):
        print(f"Year: {year}, Allentown Population: {allentown[year]}, Reading Population: {reading[year]}")
    draw_city_population_charts([allentown, reading])


if __name__ == '__main__':
    main()