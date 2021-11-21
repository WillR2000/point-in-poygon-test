from plotter import Plotter
from functions import lines
from functions import read_polygon_csv


def classify_point():
    # This method is an adaption on classify_points() from the functions.py file. For an overview of the mathematical\
    # methods, refer to the functions.py file
    x_coord, y_coord = read_polygon_csv()  # Calls x coordinates and y coordinates from polygon.csv
    x = float(input('x Coordinate: '))  # Invites the user to input a X coordinate to test
    y = float(input('Y Coordinate: '))  # Invites the user to input a Y coordinate to test

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
                # Call plotter class and add point to plot as boundary
                result = 'Boundary'

    return result


def main():
    print('Insert point information:')
    plotter = Plotter()
    result = classify_point()
    print('The position of your point is:', result)

    plotter.show()


if __name__ == '__main__':
    main()
