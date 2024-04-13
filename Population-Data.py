import json

# Load the data into a list.
filename = 'population_data.json'
f = open(filename)

pop_data = json.load(f)

# Print the 2010 population for each country.

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
print(country + ": " + str(population))
