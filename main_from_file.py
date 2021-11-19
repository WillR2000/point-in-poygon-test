from functions import read_polygon_csv
from functions import read_input_csv
from functions import mbr
from functions import point_on_line
from functions import rca2
from plotter import Plotter

def main():
    plotter = Plotter()
    print(read_polygon_csv())

    print(read_input_csv())

    print(mbr(), point_on_line(), rca2())

    print('write output.csv')

    print('plot polygon and points')
    plotter.show()

if __name__ == '__main__':
    main()


