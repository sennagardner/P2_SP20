'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''

from NBAStats import data

#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)

print("#1", data.pop(0))

#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)

my_list = sorted(data, key=lambda x: x[-1])
mytoplist = []

for x in my_list:
  my_names = [x[2], x[-1]]
  mytoplist.append(my_names)

print("#2", mytoplist[-10:])

#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
kobe_find = []

for item in data:
    if item[2].upper() == "KOBE BRYANT":
        kobe_find.append(item)
    else:
        pass

kobe_points = []
for item in kobe_find:
    pts = item[-1]
    kobe_points.append(pts)

print("#3", sum(kobe_points))

#4  What player has the most 3point field goals in a single season. (3pts)

most_threes_list = []
most_threes = sorted(data, key=lambda x: x[34])
for item in most_threes:
  names = [item[1], item[2], item[34]]
  most_threes_list.append(names)

print("#4", most_threes_list[-1])

#5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)

w_list = []
most_ws = sorted(data, key=lambda x: x[25])
for item in most_ws:
    w_names = [item[1], item[2], item[25]]
    w_list.append(w_names)

print("#5", w_list[-1])

#6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".
# who is the oldest player of all time?

oldest_list = []
oldest = sorted(data, key=lambda x: x[4])
for item in oldest:
  names = [item[1], item[2], item[4]]
  oldest_list.append(names)

print("#6", oldest_list[-1:])

#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)
totalfreethrow = sorted(data, key=lambda x: x[-1])

top100 = totalfreethrow[-100:]

freethrowpts = sorted(top100, key=lambda x: x[43])
freethrowlist = []
for item in freethrowpts:
  name = [item[1], item[2], item[43]]
  freethrowlist.append(name)
print("#7")
print("a) The person with the best free throw percentage was:", freethrowlist[-1])
print("b) The person with the worst free throw percentage was:", freethrowlist[0])
