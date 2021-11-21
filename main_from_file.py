from functions import read_polygon_csv
from functions import read_input_csv
from functions import classify_points
from functions import write_to_csv
from plotter import Plotter

def main():
    plotter = Plotter()
    print(read_polygon_csv())

    print(read_input_csv())

    print(classify_points())

    print(write_to_csv())
    plotter.show()

if __name__ == '__main__':
    main()


