import math

from helper import generate_ellipse_points, linspace


def define_nails(figure, figureparams, number_of_nails):
    nails = []

    if figure == "e":
        x, y = generate_ellipse_points(figureparams[0], figureparams[1], number_of_nails)
        nails = [(i, j) for i, j in zip(x, y)]
    elif figure == "r":
        total_length = 2 * figureparams[0] + 2 * figureparams[1]
        first_turn = figureparams[0]
        second_turn = figureparams[0] + figureparams[1]
        third_turn = 2 * figureparams[0] + figureparams[1]
        lengths = linspace(0, total_length, number_of_nails)
        for length in lengths:
            if length < first_turn:
                nails.append((-figureparams[0] + length * 2, figureparams[1]))
                continue
            if length < second_turn:
                nails.append((figureparams[0], figureparams[1] - (length - first_turn) * 2))
                continue
            if length < third_turn:
                nails.append((figureparams[0] - (length - second_turn) * 2, -figureparams[1]))
                continue
            else:
                nails.append((-figureparams[0], -figureparams[1] + (length - third_turn) * 2))
                continue
    elif figure == "t":
        total_length = sum(figureparams)
        step_size = total_length / number_of_nails

        longest_side = figureparams.index(max(figureparams))
        if longest_side == 0:
            figureparams = [figureparams[2], figureparams[0], figureparams[1]]
        elif longest_side == 2:
            figureparams = [figureparams[1], figureparams[2], figureparams[0]]

        a_length = figureparams[0]
        b_length = figureparams[1]
        c_length = figureparams[2]
        # angle_a is the angle opposing side a, and so on
        angle_a = math.acos((b_length**2 + c_length**2 - a_length**2) / (2 * b_length * c_length))
        angle_b = math.acos((c_length**2 + a_length**2 - b_length**2) / (2 * c_length * a_length))
        angle_c = math.pi - angle_a - angle_b

        slopeangle_a = math.pi / 2 - angle_b / 2
        slopeangle_b = angle_c - slopeangle_a
        slopeangle_c = slopeangle_b + angle_a
        slope_a = -math.tan(slopeangle_a)
        slope_b = math.tan(slopeangle_b)
        slope_c = math.tan(slopeangle_c)

        # upper vertix in 0,0
        b_vertix = (0, 0)
        a_side = linear_function(0, slope_a)
        c_side = linear_function(0, slope_c)

        x_c_vertix = a_length * math.cos(slopeangle_a)
        x_a_vertix = -c_length * math.cos(slopeangle_c)
        c_vertix = (x_c_vertix, a_side(x_c_vertix))
        a_vertix = (x_a_vertix, c_side(x_a_vertix))
        b_side_oo = c_vertix[1] - slope_b * c_vertix[0]
        b_side = linear_function(b_side_oo, slope_b)

        step_a = abs(step_size * math.cos(slopeangle_a))
        step_b = abs(step_size * math.cos(slopeangle_b))
        step_c = abs(step_size * math.cos(slopeangle_c))

        lengths = list(linspace(0, total_length, number_of_nails))
        first_turn_index = math.ceil(len(lengths) * figureparams[0] / total_length)
        second_turn_index = math.ceil(len(lengths) * (figureparams[0] + figureparams[1]) / total_length)
        first_turn_excess = lengths[first_turn_index] - figureparams[0]
        first_turn_excess = 0 if abs(first_turn_excess - step_size) < 10e-6 else first_turn_excess
        first_turn_excess_b_step = first_turn_excess * math.cos(slopeangle_b)
        second_turn_excess = lengths[second_turn_index] - figureparams[0] - figureparams[1]
        second_turn_excess = 0 if abs(second_turn_excess - step_size) < 10e-6 else second_turn_excess
        second_turn_excess_c_step = second_turn_excess * math.cos(slopeangle_c)

        for n in range(len(lengths)):
            if n < first_turn_index:
                nails.append((n * step_a, a_side(n * step_a)))
                continue
            if n < second_turn_index:
                x = c_vertix[0] - first_turn_excess_b_step - (n - first_turn_index) * step_b
                nails.append((x, b_side(x)))
                continue
            else:
                x = a_vertix[0] + second_turn_excess_c_step + (n - second_turn_index) * step_c
                nails.append((x, c_side(x)))
                continue

        centroid = ((a_vertix[0] + b_vertix[0] + c_vertix[0]) / 3, (a_vertix[1] + b_vertix[1] + c_vertix[1]) / 3)

        nails = [(2 * (n[0] - centroid[0]), 2 * (n[1] - centroid[1])) for n in nails]

    return nails


def linear_function(y0, slope):
    def lin(v):
        return y0 + slope * v

    return lin