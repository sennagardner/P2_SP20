# Universal Gravity Calculator (12pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r ** 2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following
done = False
G = 6.67e-11
# (3pts) takes the inputs for mass 1, mass 2, and distance between the two objects (m1, m2, and r)
# (2pts) keeps asking for inputs until they are valid (see while loop from notes)
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (3pts) calculates the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.
while not done:
    try:
        mass1 = int(input("Mass value 1: "))
        mass2 = int(input("Mass value 2: "))
        radius = int(input("Radius value: "))
        f = G * (mass1 * mass2) / radius ** 2
        print("Force is {:.2e}".format(f))
        done = True
    except ValueError:
        print("You entered an invalid number.")
    except ZeroDivisionError:
        print("You can't divide by zero")










