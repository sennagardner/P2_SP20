'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
'''

import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.figure(1)

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)

header = data.pop(0)
print(header)
print(data)

years = [int(x[0]) for x in data[20:]]
print(years)
rail_usage = [int(x[3]) for x in data[20:]]
bus_usage = [int(x[1]) for x in data[20:]]
total_ridership = [int(bus_usage[x]) + int(rail_usage[x]) for x in range(len(bus_usage))]
print(rail_usage)
print(bus_usage)
print(total_ridership)

graph = plt.figure(1, tight_layout=True)

plt.plot(years, rail_usage, label="RAIL")
plt.plot(years, bus_usage, label="BUS")
plt.plot(years, total_ridership, label="TOTAL")

plt.xlabel('Year')
plt.ylabel('Ridership')
plt.title('CTA Ridership from 2008-2018 on Bus, Rail and Total')
plt.legend(fancybox=True, shadow=True)
plt.axis([2008, 2018, 0, 550000000])

plt.show()


#6
# I notice that as rail usage increases, bus usage decreases. The discrepency between the two values seems to decrease as time goes on.
# This could be the case because people want to avoid traffic so they turn to taking the train, which never interacts with traffic.
# I also notice a steady decrease in overall usage. When I think about my own personal life, I have decreased my usage of public transportation because of how available things like Uber have become, so maybe that is true for others as well.