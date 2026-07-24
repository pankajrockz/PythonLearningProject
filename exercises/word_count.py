countries  = ['India', 'United States', 'Australia', 'Ireland', 'Germany', 'Sri Lanka', 'Iceland', 'Cuba', 'Italy',
              'Iran', 'France', 'Poland']
#Count all the countries which are starting with 'I'
counter = 0
for country in countries:
    if country[0] == 'I':
        counter += 1
print(counter)

#Another way using startswith
counter = 0
for country in countries:
    if country.startswith('I'):
        counter += 1
print(counter)

# Now print all the countries starting with 'I'
i_countries = []
for country in countries:
    if country.startswith('I'):
        i_countries.append(country)
print(i_countries)
