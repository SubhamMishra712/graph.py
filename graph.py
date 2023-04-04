import matplotlib.pyplot as plt

# Input the waste data for a particular country
total_waste = [100, 150, 200, 250, 300]

# Define the x-axis labels for the waste data
years = [2016, 2017, 2018, 2019, 2020]

# Create a bar graph of the waste data
plt.bar(years, total_waste)

# Set the title and axis labels
plt.title('Total Waste in Country X')
plt.xlabel('Year')
plt.ylabel('Waste (tons)')

# Show the graph
plt.show()
