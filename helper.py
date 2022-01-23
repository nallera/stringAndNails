import math


def linspace(start, end, steps):
    if steps == 1:
        yield start
        return

    step = (end - start) / steps

    for i in range(steps):
        yield start + step * i


def generate_ellipse_points(r1, r2, n):
    x = []
    y = []

    theta = 0
    two_pi = math.pi * 2
    delta_theta = 0.0001
    num_integrals = round(two_pi/delta_theta)
    circ = 0

    for i in range(num_integrals):
        theta += i*delta_theta
        dpt = computeDpt(r1, r2, theta)
        circ += dpt

    next_point = 0
    run = 0
    theta = 0

    for i in range(num_integrals):
        theta += delta_theta
        sub_integral = n * run / circ
        if sub_integral >= next_point:
            x.append(r1 * math.cos(theta))
            y.append(r2 * math.sin(theta))

            next_point += 1
        run += computeDpt(r1, r2, theta)

    return x[:n], y[:n]


def computeDpt(r1, r2, theta):
    dpt_sin = math.pow(r1*math.sin(theta), 2.0)
    dpt_cos = math.pow( r2*math.cos(theta), 2.0)

    return math.sqrt(dpt_sin + dpt_cos)