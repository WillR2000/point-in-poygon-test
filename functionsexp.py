from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt




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

def lines():
    with open('polygon.csv') as p:
        coordinates = p.readlines()

        coordinates.pop(0)

        poly_id_x_y = []

        for each_point in coordinates:
            id, x, y = each_point.split(',')
            poly_id_x_y.append([(int(x.strip())), (int(y.strip()))])

        lines = poly_id_x_y[0] + poly_id_x_y[1], poly_id_x_y[1] + poly_id_x_y[2], poly_id_x_y[2] + poly_id_x_y[3], \
                poly_id_x_y[3] + poly_id_x_y[4], poly_id_x_y[4] + poly_id_x_y[5], poly_id_x_y[5] + poly_id_x_y[6], \
                poly_id_x_y[6] + poly_id_x_y[7], poly_id_x_y[7] + poly_id_x_y[8], poly_id_x_y[8] + poly_id_x_y[9], \
                poly_id_x_y[9] + poly_id_x_y[10], poly_id_x_y[10] + poly_id_x_y[11], poly_id_x_y[11] + poly_id_x_y[12], \
                poly_id_x_y[12] + poly_id_x_y[13], poly_id_x_y[13] + poly_id_x_y[14], poly_id_x_y[14] + poly_id_x_y[15], \
                poly_id_x_y[15] + poly_id_x_y[16], poly_id_x_y[16] + poly_id_x_y[17], poly_id_x_y[17] + poly_id_x_y[18], \
                poly_id_x_y[18] + poly_id_x_y[19], poly_id_x_y[19] + poly_id_x_y[0]

    lineslist = list(lines)

    return lineslist



def classify_points():
    mbr_results = []

    # Methods developed from week 5 presentation - Aldo Lipani
    for value in read_input_csv():
        if min_poly_x() <= value[0] <= max_poly_x() and min_poly_y() <= value[1] <= max_poly_y():
            mbr_results.append(value)
        else:
            Plotter.add_point(0, value[0], value[1], kind='outside')

    # Code lifted and adapted from:
    # https://www.kite.com/python/answers/how-to-determine-if-a-point-is-on-a-line-segment-in-python
    # Methods developed from week 5 presentation - Aldo Lipani

    for mbp in mbr_results:
        count = 0
        for line in lines():
            x1, x2, x3, = line[0], line[2], mbp[0]
            y1, y2, y3, = line[1], line[3], mbp[1]

            if x3 < x1 or x3 < x2:
                if y1 <= y3 < y2 or y2 <= y3 < y1:
                    count = count + 1
                if y3 == y1 or y3 == y2:
                    count = count + 2
                if y1 == y2 == y3:
                    count = count + 2
                if x1 > x2 and y1 > y2:
                    if y3 == y2 and x1 >= x3 >= x2:
                        count = count + 1

            if x1 == x2:
                if (x3 == x2) and (y1 <= y3 <= y2):
                    count = 100
                elif (x3 == x2) and (y1 >= y3 >= y2):
                    count = 100
            elif y1 == y2:
                if (y3 == y2) and (x1 <= x3 <= x2):
                    count = 100
                elif (y3 == y2) and (x1 >= x3 >= x2):
                    count = 100
            elif (y3 - y1) == ((y2 - y1) / (x2 - x1)) * (x3 - x1):
                if (x1 <= x3 <= x2) and (y1 >= y3 >= y2):
                    count = 100
                elif (x1 >= x3 >= x2) and (y1 >= y3 >= y2):
                    count = 100

            if count == 100:
                Plotter.add_point(0, x3, y3, kind='boundary')
            elif count % 2 == 0:
                Plotter.add_point(0, x3, y3, kind='outside')
            else:
                Plotter.add_point(0, x3, y3, kind='inside')


        # count = 0
        # for line in lines():
        #     p1x = line[0]
        #     p1y = line[1]
        #     p2x = line[2]
        #     p2y = line[3]
        #     if xy[0] < p1x or xy[0] < p2x:
        #         if p1y <= xy[1] < p2y or p2y <= xy[1] < p1y:
        #             count = count + 1
        #         if xy[1] == p1y or xy[1] == p2y:
        #             count = count + 2
        #         if p1y == p2y == xy[1]:
        #             count = count + 2
        #         if p1x > p2x and p1y > p2y:
        #             if xy[1] == p2y and p1x >= xy[0] >= p2x:
        #                 count = count + 1
        # if count % 2 == 0:
        #     Plotter.add_point(0, xy[0], xy[1], kind='outside')
        # else:
        #     Plotter.add_point(0, xy[0], xy[1], kind='inside')







