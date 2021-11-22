import matplotlib.pyplot as plt
from plotter import Plotter


def read_polygon_csv():
    # This function reads the given polygon csv
    # Methods developed from Week 3 Lecture - Aldo Lipani
    with open('polygon.csv') as p:  # Open input polygon as p
        coordinates = p.readlines()  # Create coordinates list which is delimited by each line of the csv

    coordinates.pop(0)  # Remove the first line of the list, which contains the titles of the columns

    x_coord = []
    y_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')  # Split each part of the list by commas
        y_coord.append(int(y.strip()))  # Append the y values to a new list
        x_coord.append(int(x.strip()))  # Append the x values to a new list

    Plotter.add_polygon(0, x_coord, y_coord)  # Calls the plotter class and plots the polygon

    return x_coord, y_coord


def read_input_csv():
    # This function reads the given input csv
    # Methods developed from Week 3 Lecture - Aldo Lipani
    with open('input.csv') as i:  # Open input points as I
        points = i.readlines()  # Create points list which is delimited by each line of the csv

        points.pop(0)  # Remove the first line of the list, which contains the titles of the columns

        input_points = []

        for each_point in points:
            id, x, y = each_point.split(',')  # Split each part of the list by commas
            # Append ID, x and y into a new nested list. This allows for iteration through points\
            # whilst maintaining the ID
            input_points.append([str(id.strip()), float(x.strip()), float(y.strip())])

    return input_points


def min_poly_x():
    with open('polygon.csv') as p:  # Open input polygon as p
        coordinates = p.readlines()  # Create coordinates list which is delimited by each line of the csv

    coordinates.pop(0)  # Remove the first line of the list, which contains the titles of the columns

    x_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')  # Split each part of the list by commas
        x_coord.append(int(x.strip()))  # Append the x values to a new list

    # Method adapted from Week 3 Lecture: Aldo Lipani
    # This method find the smallest value in the given list by iterating through each value and comparing to the first
    # If the iterable is smaller than the original, the iterable becomes the residual which others are compared against
    # This repeats until there is no smaller value, resulting in the min value
    res = x_coord[0]
    for c in x_coord[1:]:
        if c < res:
            res = c
    return res


def min_poly_y():
    with open('polygon.csv') as p:  # Open input polygon as p
        coordinates = p.readlines()  # Create coordinates list which is delimited by each line of the csv

    coordinates.pop(0)  # Remove the first line of the list, which contains the titles of the columns

    y_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')  # Split each part of the list by commas
        y_coord.append(int(y.strip()))  # Append the y values to a new list

    # Method adapted from Week 3 Lecture: Aldo Lipani
    # This method find the smallest value in the given list by iterating through each value and comparing to the first
    # If the iterable is smaller than the original, the iterable becomes the residual which others are compared against
    # This repeats until there is no smaller value, resulting in the min value
    res = y_coord[0]
    for c in y_coord[1:]:
        if c < res:
            res = c
    return res


def max_poly_x():
    with open('polygon.csv') as p:  # Open input polygon as p
        coordinates = p.readlines()  # Create coordinates list which is delimited by each line of the csv

    coordinates.pop(0)  # Remove the first line of the list, which contains the titles of the columns

    x_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')  # Split each part of the list by commas
        x_coord.append(int(x.strip()))  # Append the x values to a new list

    # Method adapted from Week 3 Lecture: Aldo Lipani
    # This method find the largest value in the given list by iterating through each value and comparing to the first
    # If the iterable is larger than the original, the iterable becomes the residual which others are compared against
    # This repeats until there is no larger value, resulting in the max value
    res = x_coord[0]
    for c in x_coord[1:]:
        if c > res:
            res = c
    return res


def max_poly_y():
    with open('polygon.csv') as p:  # Open input polygon as p
        coordinates = p.readlines()  # Create coordinates list which is delimited by each line of the csv

    coordinates.pop(0)  # Remove the first line of the list, which contains the titles of the columns

    y_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')  # Split each part of the list by commas
        y_coord.append(int(y.strip()))  # Append the y values to a new list

    # Method adapted from Week 3 Lecture: Aldo Lipani
    # This method find the largest value in the given list by iterating through each value and comparing to the first
    # If the iterable is larger than the original, the iterable becomes the residual which others are compared against
    # This repeats until there is no larger value, resulting in the max value
    res = y_coord[0]
    for c in y_coord[1:]:
        if c > res:
            res = c
    return res


def lines():
    with open('polygon.csv') as p:  # Open input polygon as p
        coordinates = p.readlines()  # Create coordinates list which is delimited by each line of the csv

    coordinates.pop(0)  # Remove the first line of the list, which contains the titles of the columns

    poly_id_x_y = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')  # Split each part of the list by commas
        poly_id_x_y.append([(int(x.strip())), (int(y.strip()))])  # Append the x and y values into a new list

    # This method duplicates every second set of coordinates to create a line start and finish point within a nested\
    # list. In doing this each list is now defines as a line with an X1, Y1 which is the start point and an X2, Y2\
    # which is the end point
    lines = poly_id_x_y[0] + poly_id_x_y[1], poly_id_x_y[1] + poly_id_x_y[2], poly_id_x_y[2] + poly_id_x_y[3], \
            poly_id_x_y[3] + poly_id_x_y[4], poly_id_x_y[4] + poly_id_x_y[5], poly_id_x_y[5] + poly_id_x_y[6], \
            poly_id_x_y[6] + poly_id_x_y[7], poly_id_x_y[7] + poly_id_x_y[8], poly_id_x_y[8] + poly_id_x_y[9], \
            poly_id_x_y[9] + poly_id_x_y[10], poly_id_x_y[10] + poly_id_x_y[11], poly_id_x_y[11] + \
            poly_id_x_y[12], poly_id_x_y[12] + poly_id_x_y[13], poly_id_x_y[13] + poly_id_x_y[14], \
            poly_id_x_y[14] + poly_id_x_y[15], poly_id_x_y[15] + poly_id_x_y[16], poly_id_x_y[16] + \
            poly_id_x_y[17], poly_id_x_y[17] + poly_id_x_y[18], poly_id_x_y[18] + poly_id_x_y[19], \
            poly_id_x_y[19] + poly_id_x_y[0]

    lines = list(lines)

    return lines


def classify_points():
    mbr_results = []  # Create new list to later append results of Minimum bounding rectangle (MBR) Algorithm
    classify_results = []  # Create new list to later append results of Ray Casting Algorithm (RCA)

    # Methods developed from week 5 presentation - Aldo Lipani
    # MBR Algorithm
    # This compares the input values from the input.csv file with the minimum and maximum values from the polygon.csv
    # This method uses elimination of points between algorithms. Eg. if the point is outside the MBR, there is no need/
    # to use the RCA
    for value in read_input_csv():  # Iterates through each set of coordinates from input.csv
        if min_poly_x() <= value[1] <= max_poly_x() and min_poly_y() <= value[2] <= max_poly_y():
            # Compares the values to the minimum and maximum x and y coordinates from polygon.csv
            mbr_results.append(value)  # If input within the MBR, it is appended to this list for use later in the RCA
        else:  # If the point is outside the MBR, we already know it is outside the polygon
            Plotter.add_point(0, value[1], value[2], kind='outside')
            # Calls plotter class and adds input to the final polygon, defining its kind as outside
            classify_results.append([value, 'Outside'])
            # Appends input and kind into results list for output.csv at the end

    for mbp in mbr_results:  # Iterates through each set of coordinates that are inside the MBR
        count = 0  # Sets count to 0, the count will increase based on how many lines the ray crosses
        for line in lines():  # Iterates through each line
            x1, x2, x3, = line[0], line[2], mbp[1]  # Classifies each coordinate in a more understandable way
            y1, y2, y3, = line[1], line[3], mbp[2]
            if x3 < x1 or x3 < x2:  # Ensures each input point is left of the line, as the ray heads off to the right
                if y1 <= y3 < y2 or y2 <= y3 < y1:  # Ensures each point is between the upper and lower y line values
                    count = count + 1
                # Special cases - these next rules increase the count to ensure accuracy in the method above
                if y3 == y1 or y3 == y2:  # If the ray passes through a vertex increases the count to ensure odd/even\
                    # calculation is correct
                    count = count + 2
                if y1 == y2 == y3:  # If the ray passes through a line parallel to the x axis it increases\
                    # the count to ensure odd/even calculation is correct
                    count = count + 2
                if x1 > x2 and y1 > y2:
                    if y3 == y2 and x1 >= x3 >= x2:
                        # If the ray begins below a decreasing line and within the x coordinates of the line it\
                        # increases the count to ensure the odd/even calculation is correct
                        count = count + 1
        if count % 2 == 0:  # Calculate if the count is even
            Plotter.add_point(0, x3, y3, kind='outside')  # Call plotter class and add point to plot as outside
            Plotter.add_ray(0, x3, y3, 8, y3)  # Plots the ray originating from the input coordinate
            classify_results.append([mbp, 'Outside'])  # Appends input point to results list with classification outside
        else:  # If the count is odd
            Plotter.add_point(0, x3, y3, kind='inside')  # Call plotter class and add point to plot as inside
            Plotter.add_ray(0, x3, y3, 8, y3)  # Plots the ray originating from the input coordinate
            classify_results.append([mbp, 'Inside'])  # Appends input point to results list with classification inside

    # Special Case - Boundary Points
    # Code lifted and adapted from:
    # https://www.kite.com/python/answers/how-to-determine-if-a-point-is-on-a-line-segment-in-python
    # Methods developed from week 5 presentation - Aldo Lipani
    for mbp in mbr_results:  # Iterates through each point that is inside the MBR
        for line in lines():  # Iterates through each line from polygon.csv
            x1, x2, x3, = line[0], line[2], mbp[1]  # Classifies each coordinate in a more understandable way
            y1, y2, y3, = line[1], line[3], mbp[2]
            if x1 == x2:  # If line parallel to the y axis
                if (x3 == x2) and (y1 <= y3 <= y2):
                    # If the x of the point lies is equal to the x of the line ending and the y of the point lies\
                    # within the upper y coordinate and lower y coordinate of the line
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    # Call plotter class and add point to plot as boundary
                    classify_results.append([mbp, 'Boundary'])
                    # Appends input point to results list with classification inside
                elif (x3 == x2) and (y1 >= y3 >= y2):
                    # If the x of the point lies is equal to the x of the line ending and the y of the point lies\
                    # within the lower y coordinate and upper y coordinate of the line
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    # Call plotter class and add point to plot as boundary
                    classify_results.append([mbp, 'Boundary'])
            elif y1 == y2:  # If the line is parallel to the x axis
                if (y3 == y2) and (x1 <= x3 <= x2):
                    # If the y of the point lies is equal to the y of the line ending and the x of the point lies\
                    # within the upper x coordinate and lower x coordinate of the line
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    # Call plotter class and add point to plot as boundary
                    classify_results.append([mbp, 'Boundary'])
                    # Appends input point to results list with classification inside
                elif (y3 == y2) and (x1 >= x3 >= x2):
                    # If the y of the point lies is equal to the y of the line ending and the x of the point lies\
                    # within the lower x coordinate and upper x coordinate of the line
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    # Call plotter class and add point to plot as boundary
                    classify_results.append([mbp, 'Boundary'])
                    # Appends input point to results list with classification inside
            elif (y3 - y1) == ((y2 - y1) / (x2 - x1)) * (x3 - x1):  # If the y input minus the start of the y line\
                # is equal to the slope of the line
                if (x1 <= x3 <= x2) and (y1 >= y3 >= y2):
                    # If the input x and y coordinates are within the lower and upper x and y lines respectively
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    # Call plotter class and add point to plot as boundary
                    classify_results.append([mbp, 'Boundary'])
                    # Appends input point to results list with classification inside
                elif (x1 >= x3 >= x2) and (y1 >= y3 >= y2):
                    # If the input x and y coordinates are within the upper and lower x and y lines respectively
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    # Call plotter class and add point to plot as boundary
                    classify_results.append([mbp, 'Boundary'])
                    # Appends input point to results list with classification inside

    return classify_results


def write_to_csv():
    # This function writes our new list of results to output.csv
    # Methods developed from Week 3 Lecture - Aldo Lipani
    classify_results = classify_points()  # Calls list of results to this function
    with open("output.csv", "w") as c:  # Opens output.csv
        c.write('ID, Position' + '\n')  # Writes the titles of each column

        for result in classify_results:  # Iterates through each point in the list of results
            data = [str(int(result[0][0])), result[1]]  # Converts integer data into a string
            c.write(','.join(data) + '\n')
            # Writes data into the csv, creating a new line after each result in the list



# THIS IS AN ADDITIONAL FEATURE
def classify_point_experiment():
    # This method is an adaption on classify_points() from the functions.py file. For an overview of the mathematical\
    # methods, refer to the functions.py file
    x_coord, y_coord = read_polygon_csv()  # Calls x coordinates and y coordinates from polygon.csv
    x = float(input('x Coordinate: '))
    y = float(input('Y Coordinate: '))
    # Error handling functionality learnt from: https://realpython.com/python-exceptions/
    if x > 8 or y > 8 or x < -3 or y < -3:
        raise Exception('Error: Coordinates very far from Polygon')
    # This presents the user with an error if the inputted point is very far from the polygon.csv plot

    result = 0  # Result in this function does not have to be defined through a count method. When the point finds\
    # the right classification, the result is set as Outside, Inside or Boundary

    # Methods developed from week 5 presentation - Aldo Lipani
    if min(x_coord) <= x <= max(x_coord) and min(y_coord) <= y <= max(y_coord):
        ''
    else:
        Plotter.add_point(0, x, y, kind='outside')
        result = 'Outside'

    count = 0
    for line in lines():
        x1, x2, x3, = line[0], line[2], x
        y1, y2, y3, = line[1], line[3], y
        if x < x1 or x < x2:
            if y1 <= y < y2 or y2 <= y < y1:
                count = count + 1
            if y == y1 or y == y2:
                count = count + 2
            if y1 == y2 == y:
                count = count + 2
            if x1 > x2 and y1 > y2:
                if y == y2 and x1 >= x >= x2:
                    count = count + 1
    if count % 2 == 0:
        Plotter.add_point(0, x, y, kind='outside')  # Call plotter class and add point to plot as outside
        Plotter.add_ray(0, x, y, 8, y)  # Plots the ray originating from the input coordinate
        result = 'Outside'
    else:
        Plotter.add_point(0, x, y, kind='inside')  # Call plotter class and add point to plot as inside
        Plotter.add_ray(0, x, y, 8, y)  # Plots the ray originating from the input coordinate
        result = 'Inside'

    # Code lifted and adapted from:
    # https://www.kite.com/python/answers/how-to-determine-if-a-point-is-on-a-line-segment-in-python
    # Methods developed from week 5 presentation - Aldo Lipani
    for line in lines():
        x1, x2, x3, = line[0], line[2], x
        y1, y2, y3, = line[1], line[3], y
        if x1 == x2:
            if (x3 == x2) and (y1 <= y3 <= y2):
                Plotter.add_point(0, x3, y3, kind='boundary')
                # Call plotter class and add point to plot as boundary
                result = 'Boundary'
            elif (x3 == x2) and (y1 >= y3 >= y2):
                Plotter.add_point(0, x3, y3, kind='boundary')
                # Call plotter class and add point to plot as boundary
                result = 'Boundary'
        elif y1 == y2:
            if (y3 == y2) and (x1 <= x3 <= x2):
                Plotter.add_point(0, x3, y3, kind='boundary')
                # Call plotter class and add point to plot as boundary
                result = 'Boundary'
            elif (y3 == y2) and (x1 >= x3 >= x2):
                Plotter.add_point(0, x3, y3, kind='boundary')
                # Call plotter class and add point to plot as boundary
                result = 'Boundary'
        elif (y3 - y1) == ((y2 - y1) / (x2 - x1)) * (x3 - x1):
            if (x1 <= x3 <= x2) and (y1 >= y3 >= y2):
                Plotter.add_point(0, x3, y3, kind='boundary')
                # Call plotter class and add point to plot as boundary
                result = 'Boundary'
            elif (x1 >= x3 >= x2) and (y1 >= y3 >= y2):
                Plotter.add_point(0, x3, y3, kind='boundary')
                # Call plotter class

    plt.savefig('pip_output_fig.svg')
    print('Your point is located:', result)

    return result




