# Sorting

# swap values
import random
import time

a = 1
b = 2

temp = a  # temporary
a = b
b = temp  # swapped a and b so that a = 2 and b = 1

print(a, b)

# pythonic way
a, b = b, a

# make a random list of 100 numbers with values of 1 to 99
# use list comp
rando_list = [random.randrange(1, 100) for x in range(100)]
rando_list2 = rando_list[:]  # all of the rando list is being dumped into rando list 2 (copy)
print(rando_list)
start_time = time.perf_counter()

# SORTS THE RANDOM LIST (SELECTION)
for cur_pos in range(len(rando_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(rando_list)):
        if rando_list[scan_pos] < rando_list[min_pos]:
            min_pos = scan_pos
    rando_list[cur_pos], rando_list[min_pos] = rando_list[min_pos], rando_list[cur_pos]

print("Insertion sort time:", time.perf_counter() - start_time)
print(rando_list)

# INSERTION SORT
for key_pos in range(1, len(rando_list2)):
    key_val = rando_list2[key_pos]
    scan_pos = key_pos - 1  # look to dancer on the left
    while scan_pos >= 0 and rando_list2[scan_pos] > key_val:
        rando_list2[scan_pos + 1] = rando_list2[scan_pos]
        scan_pos -= 1
        rando_list2[scan_pos + 1] = key_val

print(rando_list2)

# MORE W FUNCTIONS
print("Hello", end=" ")  # uses an optional parameter which ahs a default value of "/n"
print("World", end="!\n")


def hello(name, time_of_day="morning"):
    print("Hello", name, "good", time_of_day)


hello("Owen")  # morning is the default value

# Lambda functions (anonymous function on a single line)
double_me = lambda x: x * 2
# double_me is a function that returns the value of x * 2
print(double_me(5))

sum_product = lambda a, b: [a + b, a * b]
print(sum_product(3, 2))

# REAL WORLD SORTING WITH PYTHON
my_list = [random.randrange(1, 100) for x in range(100)]

# SORT METHOD (CHANGES THE LIST IN PLACE)
print(my_list)
my_list.sort()  # default is to sort alphabetically or numerically small to large
print(my_list)

my_list.sort(reverse=True)
print(my_list)

# use a lambda as the key
my_2dlist = [[random.randrange(1, 100), random.randrange(1, 100)] for x in range(100)]
print(my_2dlist)

my_2dlist.sort()
print(my_2dlist) # only sorts it by the first value

my_2dlist.sort(key=lambda x: x[1])  # sorts by second item
print(my_2dlist)

my_2dlist.sort(key=lambda x: sum(x))
print(my_2dlist)

my_2dlist.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
print(my_2dlist)

# SORTED FUNCTION (RETURNS A NEW LIST)
new_list = sorted(my_2dlist, key=lambda x: sum(x))
print(new_list) # sorted by sum
print(my_2dlist) # sorted by difference