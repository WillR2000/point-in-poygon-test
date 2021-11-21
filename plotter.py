from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

# if plotting does not work comment the following line
matplotlib.use('TkAgg')


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys) -> object:
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_ray(self, x1, y1, x2, y2) -> object:
        plt.plot([x1, x2], [y1, y2], color='k', linestyle='--', linewidth=1)

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
        plt.xlabel('x', color='k')
        plt.ylabel('y', color='k')
        plt.grid()
        plt.show()
