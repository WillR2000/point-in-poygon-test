from plotter import Plotter
from functions import lines
from functions import read_polygon_csv
def classify_point():
    x_coord, y_coord = read_polygon_csv()
    x = float(input('x Coordinate: '))
    y = float(input('Y Coordinate: '))
    result = 0

    # Methods developed from week 5 presentation - Aldo Lipani
    if min(x_coord) <= x <= max(x_coord) and min(y_coord) <= y <= max(y_coord):
        ''
    else:
        Plotter.add_point(0, x, y, kind='outside')
        result = 'Outside'

    count = 0
    for line in lines():
        p1x = line[0]
        p1y = line[1]
        p2x = line[2]
        p2y = line[3]
        if x < p1x or x < p2x:
            if p1y <= y < p2y or p2y <= y < p1y:
                count = count + 1
            if y == p1y or y == p2y:
                count = count + 2
            if p1y == p2y == y:
                count = count + 2
            if p1x > p2x and p1y > p2y:
                if y == p2y and p1x >= x >= p2x:
                    count = count + 1
    if count % 2 == 0:
        Plotter.add_point(0, x, y, kind='outside')
        result = 'Outside'
    else:
        Plotter.add_point(0, x, y, kind='inside')
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
                result = 'Boundary'
            elif (x3 == x2) and (y1 >= y3 >= y2):
                Plotter.add_point(0, x3, y3, kind='boundary')
                result = 'Boundary'
        elif y1 == y2:
            if (y3 == y2) and (x1 <= x3 <= x2):
                Plotter.add_point(0, x3, y3, kind='boundary')
                result = 'Boundary'
            elif (y3 == y2) and (x1 >= x3 >= x2):
                Plotter.add_point(0, x3, y3, kind='boundary')
                result = 'Boundary'
        elif (y3 - y1) == ((y2 - y1) / (x2 - x1)) * (x3 - x1):
            if (x1 <= x3 <= x2) and (y1 >= y3 >= y2):
                Plotter.add_point(0, x3, y3, kind='boundary')
                result = 'Boundary'
            elif (x1 >= x3 >= x2) and (y1 >= y3 >= y2):
                Plotter.add_point(0, x3, y3, kind='boundary')
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


