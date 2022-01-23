import itertools
import math
from helper import linspace
from turtle import *
import matplotlib.pyplot as plt


def plot_figure(figure, number_of_nails, number_of_lines, anchor_params, turtle_on):
    if turtle_on:
        nails = define_nails(figure, number_of_nails)
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
                nails = define_nails(figure, nn)
                nails_coords = list(zip(*nails))

                pattern_points = generate_pattern(nails, number_of_lines, anchor_params)
                pattern_points_coords = list(zip(*pattern_points))

                plot_single(ax[math.floor(index/n_cols), index % n_cols], nails_coords, pattern_points_coords, anchor_params)
            plt.show()
        elif type(anchor_params[0]) == list:
            n_cols = math.ceil(len(anchor_params) / 2)
            fig, ax = plt.subplots(nrows=2, ncols=n_cols)

            for index, ap in enumerate(anchor_params):
                nails = define_nails(figure, number_of_nails)
                nails_coords = list(zip(*nails))

                pattern_points = generate_pattern(nails, number_of_lines, ap)
                pattern_points_coords = list(zip(*pattern_points))

                plot_single(ax[math.floor(index/n_cols), index % n_cols], nails_coords, pattern_points_coords, ap)

            plt.show()
        else:
            nails = define_nails(figure, number_of_nails)
            nails_coords = list(zip(*nails))

            pattern_points = generate_pattern(nails, number_of_lines, anchor_params)
            pattern_points_coords = list(zip(*pattern_points))

            fig, ax = plt.subplots()
            plot_single(ax, nails_coords, pattern_points_coords, anchor_params)
            plt.show()


def plot_single(ax, nails_coords, pattern_points_coords, anchor_params):
    ax.scatter(nails_coords[0], nails_coords[1])
    ax.set_aspect('equal')

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


def define_nails(figure, number_of_nails):
    nails = []

    if figure == "c":
        angles = linspace(-math.pi, math.pi, number_of_nails)
        nails = [(math.cos(angle), math.sin(angle)) for angle in angles]
    if figure == "s":
        lengths = linspace(0, 4, number_of_nails)
        for length in lengths:
            if length < 1:
                nails.append((-1 + length * 2, 1))
                continue
            if length < 2:
                nails.append((1, 1 - (length - 1) * 2))
                continue
            if length < 3:
                nails.append((1 - (length - 2) * 2, -1))
                continue
            else:
                nails.append((-1, -1 + (length - 3) * 2))
                continue

    return nails


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
