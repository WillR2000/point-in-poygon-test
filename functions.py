from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

# if plotting does not work comment the following line
matplotlib.use('TkAgg')


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


def open_poly_x():
    with open('polygon.csv') as p:
        coordinates = p.readlines()

    coordinates.pop()

    x_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')
        x_coord.append(x.strip())

    x_coordinates = [int(i) for i in x_coord]

    return x_coordinates


def open_poly_y():
    with open('polygon.csv') as p:
        coordinates = p.readlines()

    coordinates.pop(0)

    y_coord = []

    for each_coord in coordinates:
        id, x, y = each_coord.split(',')
        y_coord.append(y.strip())

    y_coordinates = [int(i) for i in y_coord]

    return y_coordinates


def min_poly_x():
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
        y_coord.append(y.strip())

    y_coord = [int(i) for i in y_coord]

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


def open_input():
    with open('input.csv') as I:
        points = I.readlines()

        points.pop(0)

        id_x_y = []

        for each_point in points:
            id, x, y = each_point.split(',')
            id_x_y.append([id.strip(), float(x.strip()), float(y.strip())])

        input_points = id_x_y

    return input_points


def mbr_plot():
    max_coords = max_poly_x(), max_poly_y()
    min_coords = min_poly_x(), min_poly_y()

    mbr_x = max_coords[0], max_coords[0], min_coords[0], min_coords[0]
    mbr_y = max_coords[1], min_coords[1], min_coords[1], max_coords[1]

    return mbr_x, mbr_y


def open_lines():
    with open('polygon.csv') as p:
        coordinates = p.readlines()

        coordinates.pop(0)

        poly_id_x_y = []

        for each_point in coordinates:
            id, x, y = each_point.split(',')
            poly_id_x_y.append([id.strip(), int(x.strip()), int(y.strip())])

        lines = []
        lines_2 = lines

        for each_vertex in poly_id_x_y:
            lines.append(each_vertex[0:3])

        for each_vertex in lines_2:
            if each_vertex[0] % 2 == 0:
                lines.append(each_vertex[0:3])
            else:
                ''

        final_lines = lines

    return final_lines


def line():
    with open('polygon.csv') as p:
        polygon_coords = p.readlines()

    polygon_coords.pop(0)

    x_coords = []
    y_coords = []

    for each_point in polygon_coords:
        id, x, y = each_point.split(',')
        x_coords.append(int(x))
        y_coords.append(int(y))

    vertices = list(zip(x_coords, y_coords))

    mlist = []
    clist = []

    for i in range(0, len(vertices)):
        run = x_coords[i] +1 - x_coords[i]
        rise = y_coords[i] +1  - y_coords[i]

        if run == 0:
            m = 'vertical'
        else:
            m = float(rise) / float(run)
        mlist.append(m)

        if m != 'vertical':
            c = y_coords[i] - m * x_coords[i]
        else:
            c = x_coords[i]
        clist.append(c)

    lines = list(zip(mlist, clist))

    return lines

