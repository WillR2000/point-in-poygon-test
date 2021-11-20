from functions import read_polygon_csv
from functions import read_input_csv
from functions import mbr
from functions import classify_points

from plotter import Plotter

def main():
    plotter = Plotter()
    print(read_polygon_csv())

    print(read_input_csv())

    print(classify_points())

    print('write output.csv')

    print('plot polygon and points')
    plotter.show()

if __name__ == '__main__':
    main()


