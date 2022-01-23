from helper import generate_ellipse_points, linspace


def define_nails(figure, figureparams, number_of_nails):
    nails = []

    if figure == "e":
        x, y = generate_ellipse_points(figureparams[0], figureparams[1], number_of_nails)
        nails = [(i, j) for i, j in zip(x, y)]
    if figure == "r":
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