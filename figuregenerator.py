from helper import generate_ellipse_points, linspace


def define_nails(figure, figureparams, number_of_nails):
    nails = []

    if figure == "e":
        x, y = generate_ellipse_points(figureparams[0], figureparams[1], number_of_nails)
        nails = [(i, j) for i, j in zip(x, y)]
    if figure == "r":
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

    return nails
