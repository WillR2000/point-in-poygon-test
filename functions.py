from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt


def mbr():
    max_coords = max_poly_x(), max_poly_y()
    min_coords = min_poly_x(), min_poly_y()

    mbr_x = max_coords[0], max_coords[0], min_coords[0], min_coords[0]
    mbr_y = max_coords[1], min_coords[1], min_coords[1], max_coords[1]

    return mbr_x, mbr_y
def open_input_x():
    with open('input.csv') as I:
        points = I.readlines()

    points.pop(0)

    point_x = []

    for each_point in points:
        id, x, y = each_point.split(',')
        point_x.append(x.strip())

    input_x = [float(i) for i in point_x]

    return input_x


def open_input_y():
    with open('input.csv') as I:
        points = I.readlines()

    points.pop(0)

    point_y = []

    for each_point in points:
        id, x, y = each_point.split(',')
        point_y.append(y.strip())

    input_y = [float(i) for i in point_y]

    return input_y


class Geometry:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Line(Geometry):

    def __init__(self, name, point_1, point_2):
        super().__init__(name)
        self.__point_1 = point_1
        self.__point_2 = point_2

    def point(self, name, x, y):
        super().__init__(name)
        self.__x = x
        self.__y = y


class Polygon(Geometry):

    def __init__(self, name, points):
        super().__init__(name)
        self.__points = points

    def get_points(self):
        return self.__points

    def lines(self):
        res = []
        points = self.get_points()
        point_a = points[0]
        for point_b in points[1:]:
            res.append(Line(point_a.get_name() + '-' + point_b.get_name(), point_a, point_b))
            point_a = point_b
        res.append(Line(point_a.get_name() + '-' + points[0].get_name(), point_a, points[0]))
        return res


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys) -> object:
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_mbr(self, xs, ys) -> object:
        plt.fill(xs, ys, 'gray', label='MBR')

    def add_point(self, x, y, kind=None):
        if kind == 'outside':
            plt.plot(x, y, 'ro', label='Outside')
        elif kind == 'boundary':
            plt.plot(x, y, 'bo', label='Boundary')
        elif kind == 'inside':
            plt.plot(x, y, 'go', label='Inside')
        else:
            plt.plot(x, y, 'ko', label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()


def read_polygon_csv():
    with open('polygon.csv') as p:
        coordinates = p.readlines()

    coordinates.pop(0)

    x_coord = []
    y_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')
        y_coord.append(int(y.strip()))
        x_coord.append(int(x.strip()))

    Plotter.add_polygon(0, x_coord, y_coord)

    return x_coord, y_coord

def read_input_csv():
    with open('input.csv') as I:
        points = I.readlines()

        points.pop(0)

        id_x_y = []

        for each_point in points:
            id, x, y = each_point.split(',')
            id_x_y.append([float(x.strip()), float(y.strip())])

        input_points = id_x_y

    return input_points

def min_poly_x():
    with open('polygon.csv') as p:
        coordinates = p.readlines()

    coordinates.pop(0)

    x_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')
        x_coord.append(int(y.strip()))

    res = x_coord[0]
    for c in x_coord[1:]:
        if c < res:
            res = c
    return res

def min_poly_y():
    with open('polygon.csv') as p:
        coordinates = p.readlines()

    coordinates.pop(0)

    y_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')
        y_coord.append(int(y.strip()))

    res = y_coord[0]
    for c in y_coord[1:]:
        if c < res:
            res = c
    return res

def max_poly_x():
    with open('polygon.csv') as p:
        coordinates = p.readlines()

    coordinates.pop(0)

    x_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')
        x_coord.append(x.strip())

    x_coord = [int(i) for i in x_coord]

    res = x_coord[0]
    for c in x_coord[1:]:
        if c > res:
            res = c
    return res

def max_poly_y():
    with open('polygon.csv') as p:
        coordinates = p.readlines()

    coordinates.pop(0)

    y_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')
        y_coord.append(y.strip())

    y_coord = [int(i) for i in y_coord]

    res = y_coord[0]
    for c in y_coord[1:]:
        if c > res:
            res = c
    return res

def mbr():
    with open('input.csv') as I:
        points = I.readlines()

        points.pop(0)

        id_x_y = []

        for each_point in points:
            id, x, y = each_point.split(',')
            id_x_y.append([float(x.strip()), float(y.strip())])

        input_points = id_x_y
        print(id_x_y)

    mbr_results = []

    for value in input_points:
        if min_poly_x() <= value[0] <= max_poly_x() and min_poly_y() <= value[1] <= max_poly_y():
            mbr_results.append(value)
        else:
            Plotter.add_point(0, value[0], value[1], kind='outside')

    return mbr_results

# Code lifted and adapted from: https://www.kite.com/python/answers/how-to-determine-if-a-point-is-on-a-line
# Methods developed from week 5 presentation - Aldo Lipani
def point_on_line():
    x_coord, y_coord = read_polygon_csv()
    mbr_results = mbr()

    poly_points = (list(zip(x_coord, y_coord)))
    points = mbr_results

    point_on_line_results = []
    pt1 = poly_points[0]
    for pt2 in poly_points[1:]:
        for pt3 in points[0:]:
            x1, x2, x3, = pt1[0], pt2[0], pt3[0]
            y1, y2, y3, = pt1[1], pt2[1], pt3[1]
            if x1 == x2:
                if (x3 == x2) and (y1 <= y3 <= y2):
                    Plotter.add_point(0, x3, y3, kind='boundary')
                elif (x3 == x2) and (y1 >= y3 >= y2):
                    Plotter.add_point(0, x3, y3, kind='boundary')
            elif y1 == y2:
                if (y3 == y2) and (x1 <= x3 <= x2):
                    Plotter.add_point(0, x3, y3, kind='boundary')
                elif (y3 == y2) and (x1 >= x3 >= x2):
                    Plotter.add_point(0, x3, y3, kind='boundary')
            elif (y3 - y1) == ((y2 - y1)/(x2 - x1)) * (x3 - x1):
                if x1 <= x3 <= x2 and y1 >= y3 >= y2:
                    Plotter.add_point(0, x3, y3, kind='boundary')
                elif x1 >= x3 >= x2 and y1 >= y3 >= y2:
                    Plotter.add_point(0, x3, y3, kind='boundary')
        pt1 = pt2

def lines():
    with open('polygon.csv') as p:
        coordinates = p.readlines()

        coordinates.pop(0)

        poly_id_x_y = []

        for each_point in coordinates:
            id, x, y = each_point.split(',')
            poly_id_x_y.append([(int(x.strip())), (int(y.strip()))])

        lines = poly_id_x_y[0] + poly_id_x_y[1], poly_id_x_y[1] + poly_id_x_y[2], poly_id_x_y[2] + poly_id_x_y[3],\
                poly_id_x_y[3] + poly_id_x_y[4], poly_id_x_y[4] + poly_id_x_y[5], poly_id_x_y[5] + poly_id_x_y[6],\
                poly_id_x_y[6] + poly_id_x_y[7], poly_id_x_y[7] + poly_id_x_y[8], poly_id_x_y[8] + poly_id_x_y[9],\
                poly_id_x_y[9] + poly_id_x_y[10], poly_id_x_y[10] + poly_id_x_y[11], poly_id_x_y[11] + poly_id_x_y[12],\
                poly_id_x_y[12] + poly_id_x_y[13], poly_id_x_y[13] + poly_id_x_y[14], poly_id_x_y[14] + poly_id_x_y[15], \
                poly_id_x_y[15] + poly_id_x_y[16], poly_id_x_y[16] + poly_id_x_y[17], poly_id_x_y[17] + poly_id_x_y[18], \
                poly_id_x_y[18] + poly_id_x_y[19], poly_id_x_y[19] + poly_id_x_y[0]

        lines = list(lines)

    return lines

def rays():
    rays = []

    for point in read_input_csv():
        point.append(99999)
        point.append(point[1])
        rays.append(point)

    return rays

# Lifted and adapted from StackOverflow
# https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
# Methods developed from week 5 presentation - Aldo Lipani
def line_intersection(line, ray):

    line_slope = (line[3] - line[1]) / (line[2] - line[0])
    ray_slope = (ray[3] - ray[1]) / (ray[2] - ray[0])

    line_ycept =  line[1] - line_slope * line[0]
    rayycept = ray[1] - ray_slope * ray[0]

    def line_intersect(m1, b1, m2, b2):
        if m1 == m2:
            print("These lines are parallel!!!")
            return None

        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        return x, y

    return line_intersect()

def rca():
    results = []
    count = 0
    for ray in rays():
        for line in lines():
            if point_on_line(line, ray):
                results.append('boundary')
            else:
                if line_intersection(line, ray) == Exception:
                    ''
                else:
                    x, y = line_intersection()
                    if min_poly_x() < x < max_poly_x() and min_poly_y() < y < max_poly_y():
                        count = + 1

    for point in read_input_csv():
        if (count % 2) == 0:
            point.append('outside')
            results.append(point)
        else:
            point.append('inside')
            results.append(point)

        return results




















