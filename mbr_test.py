from functions import min_poly_x
from functions import max_poly_x
from functions import max_poly_y
from functions import min_poly_y
from functions import open_input

from plotter import Plotter


def main():
    results = []

    for value in open_input():
        for lists in open_input():
            if min_poly_x() < value[1] < max_poly_x() and min_poly_y() < value[2] < max_poly_y():
                lists.append('go')
            else:
                lists.append('ro')

        results = lists

    print(results)


if __name__ == '__main__':
    main()
