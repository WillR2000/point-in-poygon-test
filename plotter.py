from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

# if plotting does not work comment the following line
matplotlib.use('TkAgg')


class Plotter:
    # This class was provided at the start of the assignment by Aldo Lipani

    def __init__(self):
        plt.figure()

    # This method takes the x and y coordinates of the polygon.csv and plots them
    def add_polygon(self, xs, ys) -> object:
        plt.fill(xs, ys, 'lightgray', label='Polygon')  # This defines the characteristics of the polygon

    # This method takes the x and y coordinates from the input.csv and plots a line to demonstrate a ray from the\
    # Ray Casting Algorithm (RCA)
    # This method was created during the assessment to demonstrate the RCA
    def add_ray(self, x1, y1, x2, y2) -> object:
        plt.plot([x1, x2], [y1, y2], color='k', linestyle='--', linewidth=1)
        # This defines the characteristics of the ray

    # This method takes the x and y coordinates from the input.csv and plots the point within the figure
    def add_point(self, x, y, kind=None):
        if kind == 'outside':
            plt.plot(x, y, 'ro', label='Outside')  # This defines the characteristics of the point
        elif kind == 'boundary':
            plt.plot(x, y, 'bo', label='Boundary')  # This defines the characteristics of the point
        elif kind == 'inside':
            plt.plot(x, y, 'go', label='Inside')  # This defines the characteristics of the point
        else:
            plt.plot(x, y, 'ko', label='Unclassified')  # This defines the characteristics of the point

    # This method defines the characteristics of the overall plot using matplotlib
    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.title('Point in Polygon Test')
        plt.xlabel('x', color='k')  # This characteristic labels the x axis to complete the plot
        plt.ylabel('y', color='k')  # This characteristic labels the y axis to complete the plot
        plt.grid()  # This characteristic adds a grid to the plot to assist with user viewing.
        plt.show()
