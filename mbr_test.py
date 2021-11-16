from functions import open_poly_x
from functions import open_poly_y

from functions import min_poly_x
from functions import max_poly_x
from functions import max_poly_y
from functions import min_poly_y
from functions import open_input_x
from functions import open_input_y
from functions import mbr_plot

from functions import open_input

from functions import Plotter


def main():
    results = []

    for value in open_input():
        if min_poly_x() < value[1] < max_poly_x() and min_poly_y() < value[2] < max_poly_y():
            value.append('inside')
            results.append(value)
        else:
            value.append('outside')
            results.append(value)

    print(results)
    print(open_input())

    #Plotter.add_mbr(0, mbr_plot()[0], mbr_plot()[1])
    ###Plotter.add_polygon(0, open_poly_x(), open_poly_y())
    ##Plotter.add_point(0, open_input_x(), open_input_y())
    #Plotter.show(0)

if __name__ == '__main__':
    main()
