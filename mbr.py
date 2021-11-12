from functions import open_poly_x
from functions import open_poly_y

from functions import min_poly_x
from functions import max_poly_x
from functions import max_poly_y
from functions import min_poly_y
from functions import open_input_x
from functions import open_input_y

from functions import Plotter

def main():
    x_coords = open_poly_x()
    y_coords = open_poly_y()

    max_coords = max_poly_x(x_coords), max_poly_y(y_coords)
    min_coords = min_poly_x(x_coords), min_poly_y(y_coords)

    mbr_x = max_coords[0], max_coords[0], min_coords[0], min_coords[0]
    mbr_y = max_coords[1], min_coords[1], min_coords[1], max_coords[1]

    Plotter.add_mbr(0, mbr_x, mbr_y)
    Plotter.add_polygon(0, open_poly_x(), open_poly_y())
    Plotter.add_point(0, open_input_x(), open_input_y())
    Plotter.show(0)

if __name__ == '__main__':
    main()