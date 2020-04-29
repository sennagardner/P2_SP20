# Folium train map


# 15pts - Use folium to plot all of the L train stops in Chicago. Use an appropriate start zoom level.
# 5pts - Add the name to each stop as a popup. Add a train icon to each marker.  Save as an html page in the same folder.
# 3pts  - Color code all of the lines (make the pink line marker pink etc.)
# 2pts - Brown is not a default color name.  See if you can use the documentation for Folium to set a marker color through other means.

# Data set is in this folder, but can be found at: https://data.cityofchicago.org/api/views/8pix-ypme/rows.csv?accessType=DOWNLOAD

# Tricky parts of this one
## The location is in tuple format.  If you have trouble converting it, try this:
import folium
import csv
from folium import plugins


with open('CTA_-_System_Information_-_List_of__L__Stops (1).csv') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)


train_stopslist = [eval(x[-1]) for x in data]
stop_names = [x[3] for x in data]
color_list = []

for train in data:
    if train[7] == 'true':
        color_list.append('red')
    elif train[8] == 'true':
        color_list.append('blue')
    elif train[9] == 'true':
        color_list.append('green')
    elif train[10] == 'true':
        color_list.append('    #A52A2A')
    elif train[11] == 'true' or train[12] == 'true':
        color_list.append('purple')
    elif train[13] == 'true':
        color_list.append('#FFFF00')
    elif train[14] == 'true':
        color_list.append('pink')
    elif train[-2] == 'true':
        color_list.append('orange')
    else:
        color_list.append('black')


train_map = folium.Map(location=[41.880443, -87.644107], zoom_start=11)

for i in range(len(data)):
    folium.Marker(location=(train_stopslist[i]),
                  popup=stop_names[i],
                  icon=folium.plugins.BeautifyIcon(border_color=(color_list[i]), icon='train', prefix='fa')
                  ).add_to(train_map)


train_map.save('train_map.html')


# If you have extra time, try to put some html into the popup.

