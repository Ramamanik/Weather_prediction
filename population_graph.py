import matplotlib.pyplot as plt
import csv

years=[]
country1_population=[]
country2_population=[]

with open('population.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        print("test1",row)
        years.append(int(row[0]))
        print("test2",years )
        country1_population.append(int(row[1]))
        country2_population.append(int(row[2]))

# Create a line plot for population growth
plt.plot(years, country1_population, marker='o', label='country 1')
plt.plot(years, country2_population, marker='o', label='Country 2')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Population (in millions)')
plt.title('Population Growth Over Time')

# Add legend

# Show plot
plt.grid(True)
plt.savefig('matty_plot.jpeg')
#plt.show()

