from plotter import Plotter



# class Pointresults:
#     def __init__(self, id, x, y, kind):
#         self.id = id
#         self.x = str(x)
#         self.y = str(y)
#         self.kind = kind


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
            id_x_y.append([str(id.strip()), float(x.strip()), float(y.strip())])

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
    coords = []
    classify_results = []

    # Methods developed from week 5 presentation - Aldo Lipani
    for value in read_input_csv():
        if min_poly_x() <= value[1] <= max_poly_x() and min_poly_y() <= value[2] <= max_poly_y():
            mbr_results.append(value)
        else:
            Plotter.add_point(0, value[1], value[2], kind='outside')
            classify_results.append([value, 'Outside'])

    for mbp in mbr_results:
        count = 0
        for line in lines():
            x1, x2, x3, = line[0], line[2], mbp[1]
            y1, y2, y3, = line[1], line[3], mbp[2]
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
        if count % 2 == 0:
            Plotter.add_point(0, x3, y3, kind='outside')
            Plotter.add_ray(0, x3, y3, 8, y3)
            classify_results.append([mbp, 'Outside'])
        else:
            Plotter.add_point(0, x3, y3, kind='inside')
            Plotter.add_ray(0, x3, y3, 8, y3)
            classify_results.append([mbp, 'Inside'])

    # Code lifted and adapted from:
    # https://www.kite.com/python/answers/how-to-determine-if-a-point-is-on-a-line-segment-in-python
    # Methods developed from week 5 presentation - Aldo Lipani
    for mbp in mbr_results:
        for line in lines():
            x1, x2, x3, = line[0], line[2], mbp[1]
            y1, y2, y3, = line[1], line[3], mbp[2]
            if x1 == x2:
                if (x3 == x2) and (y1 <= y3 <= y2):
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    Plotter.add_ray(0, x3, y3, 8, y3)
                    classify_results.append([mbp, 'Boundary'])
                elif (x3 == x2) and (y1 >= y3 >= y2):
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    Plotter.add_ray(0, x3, y3, 8, y3)
                    classify_results.append([mbp, 'Boundary'])
            elif y1 == y2:
                if (y3 == y2) and (x1 <= x3 <= x2):
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    Plotter.add_ray(0, x3, y3, 8, y3)
                    classify_results.append([mbp, 'Boundary'])
                elif (y3 == y2) and (x1 >= x3 >= x2):
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    Plotter.add_ray(0, x3, y3, 8, y3)
                    classify_results.append([mbp, 'Boundary'])
            elif (y3 - y1) == ((y2 - y1) / (x2 - x1)) * (x3 - x1):
                if (x1 <= x3 <= x2) and (y1 >= y3 >= y2):
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    Plotter.add_ray(0, x3, y3, 8, y3)
                    classify_results.append([mbp, 'Boundary'])
                elif (x1 >= x3 >= x2) and (y1 >= y3 >= y2):
                    Plotter.add_point(0, x3, y3, kind='boundary')
                    Plotter.add_ray(0, x3, y3, 8, y3)
                    classify_results.append([mbp, 'Boundary'])

    return classify_results


def write_to_csv():
    classify_results = classify_points()

    # for result in classify_results:
    #     result = str(result)
    #     classify_new.append(result)
    #
    # classify_results = classify_new

    print('Class', classify_results)


    with open("output.csv", "w") as c:
        c.write('ID, Position' + '\n')

        for result in classify_results:
            data = [str(int(result[0][0])), result[1]]
            c.write(','.join(data) + '\n')

        # for result in classify_results:
        #     data1 = result[2], result[4], result[6]
        #     data2 = result[8],'\n'
        #     data = data1 + data2
        #     c.write(data)
