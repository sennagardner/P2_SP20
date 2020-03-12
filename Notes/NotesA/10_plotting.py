import matplotlib.pyplot as plt
import random

plt.figure(1)  # create a new window/plot

plt.plot([120, 40, 10, 0])  # plot y against the index
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # ([x], [y])

plt.figure(2) # makes a second window/plot

x1 = [x for x in range(1, 11)]
y1 = [y ** 2 for y in x1]

plt.plot(x1, y1, color='green', marker='*', markersize=10, linestyle='--', alpha=0.5, label="myPlot")

# title axes label unit numbers key (TALUNK)
plt.xlabel('time (seconds)') # labels the x axis
plt.ylabel('excitement level (YAYS)')
plt.title('Example Plot')
plt.axis([0, 12, 0, 120]) # [xmin, xmax, ymin, ymax]


plt.show()  # opens the window/plot
