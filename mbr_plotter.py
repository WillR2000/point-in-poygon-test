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
    max_coords = max_poly_x(), max_poly_y()
    min_coords = min_poly_x(), min_poly_y()

    mbr_x = max_coords[0], max_coords[0], min_coords[0], min_coords[0]
    mbr_y = max_coords[1], min_coords[1], min_coords[1], max_coords[1]

    return mbr_x, mbr_y

if __name__ == '__main__':
    main()