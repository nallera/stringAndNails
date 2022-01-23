import itertools
import math

from figuregenerator import define_nails
from turtle import *
import matplotlib.pyplot as plt


def plot_figure(figure, figureparams, number_of_nails, number_of_lines, anchor_params, turtle_on):
    if turtle_on:
        nails = define_nails(figure, figureparams, number_of_nails)
        pattern_points = generate_pattern(nails, number_of_lines, anchor_params)

        screen = Screen()
        screen.setup(600, 600)
        screen.setworldcoordinates(-1.25, -1.25, 1.25, 1.25)
        turtle = Turtle()
        turtle.speed(10)

        turtle_plot(nails, screen, turtle, False, False, 'blue')
        turtle_plot(pattern_points, screen, turtle, True, True, 'black')
    else:
        if type(number_of_nails) == list:
            n_cols = math.ceil(len(number_of_nails) / 2)
            fig, ax = plt.subplots(nrows=2, ncols=n_cols)

            for index, nn in enumerate(number_of_nails):
                nails = define_nails(figure, figureparams, nn)
                nails_coords = list(zip(*nails))

                pattern_points = generate_pattern(nails, number_of_lines, anchor_params)
                pattern_points_coords = list(zip(*pattern_points))

                plot_single(ax[math.floor(index/n_cols), index % n_cols], nails_coords, pattern_points_coords, anchor_params)

            plt.show()
        elif type(anchor_params[0]) == list:
            n_cols = math.ceil(len(anchor_params) / 2)
            fig, ax = plt.subplots(nrows=2, ncols=n_cols)

            for index, ap in enumerate(anchor_params):
                nails = define_nails(figure, figureparams, number_of_nails)
                nails_coords = list(zip(*nails))

                pattern_points = generate_pattern(nails, number_of_lines, ap)
                pattern_points_coords = list(zip(*pattern_points))

                plot_single(ax[math.floor(index/n_cols), index % n_cols], nails_coords, pattern_points_coords, ap)

            plt.show()
        elif type(figureparams[0]) == list:
            n_cols = math.ceil(len(figureparams) / 2)
            fig, ax = plt.subplots(nrows=2, ncols=n_cols)

            for index, fp in enumerate(figureparams):
                nails = define_nails(figure, fp, number_of_nails)
                nails_coords = list(zip(*nails))

                pattern_points = generate_pattern(nails, number_of_lines, anchor_params)
                pattern_points_coords = list(zip(*pattern_points))

                plot_single(ax[math.floor(index/n_cols), index % n_cols], nails_coords, pattern_points_coords, anchor_params)

            plt.show()
        else:
            nails = define_nails(figure, figureparams, number_of_nails)
            nails_coords = list(zip(*nails))

            pattern_points = generate_pattern(nails, number_of_lines, anchor_params)
            pattern_points_coords = list(zip(*pattern_points))

            fig, ax = plt.subplots()
            plot_single(ax, nails_coords, pattern_points_coords, anchor_params)
            plt.show()


def plot_single(ax, nails_coords, pattern_points_coords, anchor_params):
    ax.scatter(nails_coords[0], nails_coords[1])
    ax.set_aspect('equal')
    ax.set(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25))

    ax.plot(pattern_points_coords[0], pattern_points_coords[1], linewidth=0.25, color='black',
            label=f"{len(nails_coords[0])} nails, anchor starts: "
                  f"[{anchor_params[0]},{math.floor(len(nails_coords[0])/anchor_params[1])}], "
                  f"anchor steps: {anchor_params[2:4]}")
    plt.show(block=False)
    ax.legend(bbox_to_anchor=(1.1, 1.1), loc='upper right')


def turtle_plot(points, screen, turtle, pendown, tracer, color):
    if not tracer:
        screen.tracer(0, 0)
    else:
        screen.tracer(1, 1)

    turtle.color(color)

    if pendown:
        turtle.pendown()
    else:
        turtle.penup()

    for x, y in points:
        turtle.goto(x, y)
        if not pendown:
            turtle.dot()

    if not tracer:
        screen.update()


def generate_pattern(nails, number_of_lines, anchor_params):
    a_start = anchor_params[0]
    b_start = math.floor(len(nails)/anchor_params[1])

    a_skip = anchor_params[2]
    b_skip = anchor_params[3]

    a_end = a_start + number_of_lines * a_skip
    b_end = b_start + number_of_lines * b_skip

    a = range(a_start, a_end, a_skip)
    b = range(b_start, b_end, b_skip)

    a = [point % len(nails) for point in a]
    b = [point % len(nails) for point in b]

    order = list(itertools.chain(*zip(a, b)))

    pattern_points = [nails[i] for i in order]

    return pattern_points
