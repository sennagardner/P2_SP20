
'''
Greenhouse gas emissions (GHG) vs. square footage for all school buildings in Chicago

Data set used will be Chicago Energy Benchmark info from 2018
data can be found at...
https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD

Energy Efficiency of Chicago Schools (35pts)

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2015 to 2018.
We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
Challenge (for fun):
An efficient school would have a large ratio of sqft to ghg.
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:
- Scatter plot the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (10pts)
- Data includes ONLY data for K-12 Schools. (5pts)
- Data includes ONLY data for 2018 reporting. (5pts)
- Label x and y axis and give appropriate title. (5pts)
- Annotate Francis W. Parker. (5pts)
- Create a best fit line for schools shown. (5pts)


Extra Credit: Add a significant feature to your graph that helps tell the story of your data.  (feel free to use methods from matplotlib.org). (10pts)

Note: With extra credit you will earn you a max of 35pts (100%) for the assignment.
Maybe you can try one of the following or think up your own:
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)


Note 2:  This is a tough assignment to do on your own.  Do your best with what you have.
'''


import csv
import matplotlib.pyplot as plt
import numpy as np


with open("Chicago_Energy_Benchmarking.csv") as f:
    reader = csv.reader(f, delimiter=",")
    data = list(reader)


header = data.pop(0)
print(header)

new_data = []

plt.figure("Chicago School GHG Emissions", figsize=(12, 6))
# plt.scatter(building_sf, total_emissions)

plt.ylabel("Total Emissions")
plt.xlabel("Total Square Footage")
plt.title("Total Emissions v. Total Square Footage")
plt.grid(color="black")

for school in data:
    try:
        float(school[24])
        float(school[10])
        if school[9] == "K-12 School" and school[0] == "2018":
            new_data.append(school)
    except:
        print(school[2], "invalid data")

new_data.sort(key=lambda x: float(x[25]), reverse=True)

building_sf = [float(x[10]) for x in new_data]
total_emissions = [float(x[24]) for x in new_data]
names = [x[2] for x in new_data]


color = []
for i in range(len(new_data)):
    if new_data[i][2] == "Francis W Parker School":
        color.append("blue")
    elif i < 30:
        color.append("red")
    else:
        color.append("green")

plt.annotate(names[names.index("Francis W Parker School")], xy=(building_sf[names.index("Francis W Parker School")], total_emissions[names.index("Francis W Parker School")]))

plt.scatter(building_sf, total_emissions, alpha = 0.3, c=color)
plt.figure(1, tight_layout=True)

p = np.polyfit(building_sf, total_emissions, 1)
print(p)

x = [x for x in range(1000000)]
y = [p[0] * y + p[1] for y in x]

plt.plot(x, y)
plt.show()
