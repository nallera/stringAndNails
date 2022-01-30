import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="-f is the figure outline, use e for elipse, t for triangle"
                                                 " and r for rectangle, "
                                                 "-p are the figure outline parameters (width,height), "
                                                 "-n is the number of nails in the outline, -l is the number of "
                                                 "lines to plot, -a are the anchor parameters in the format "
                                                 "a_start,b_start,a_skip,b_skip, -t is for turtle plot (0/1)")
    parser.add_argument("-f", "--figure", help="Figure outline")
    parser.add_argument("-p", "--figureparams", help="Figure outline parameters")
    parser.add_argument("-n", "--nails", help="Number of nails")
    parser.add_argument("-l", "--lines", help="Number of lines")
    parser.add_argument("-a", "--anchor", help="Anchor parameters")
    parser.add_argument("-t", "--turtle", help="Turtle plot")
    args = parser.parse_args()

    try:
        if args.figureparams:
            if ";" in args.figureparams:
                params_aux = [[float(p) for p in e.split(",")] for e in args.figureparams.split(";")]
                args.figureparams = []
                for param_set in params_aux:
                    max_param = max(param_set)
                    args.figureparams.append([arg / max_param for arg in param_set])
            else:
                args.figureparams = [float(nail) for nail in args.figureparams.split(",")]
                max_param = max(args.figureparams)
                args.figureparams = [arg/max_param for arg in args.figureparams]
        else:
            args.figureparams = [1, 1]
    except ValueError:
        raise TypeError("-p needs to be a list of floats")

    try:
        if ";" in args.anchor:
            args.anchor = [[(float(v) if i == 1 else int(v)) for i, v in enumerate(e.split(","))] for e in args.anchor.split(";")]
        else:
            args.anchor = [(float(v) if i == 1 else int(v)) for i, v in enumerate(args.anchor.split(","))]
    except ValueError:
        raise TypeError("bad format in anchor parameters (-a)")

    try:
        if "," in args.nails:
            args.nails = [int(nail) for nail in args.nails.split(",")]
        else:
            args.nails = int(args.nails)
    except ValueError:
        raise TypeError("-n needs to be an integer")

    try:
        args.turtle = bool(int(args.turtle))
    except ValueError:
        raise TypeError("-t needs to be 0 or 1")

    try:
        args.lines = int(args.lines)
    except ValueError:
        raise TypeError("-l needs to be an integer")

    if args.figure not in ("e", "t", "r"):
        raise ValueError("-f must be one of the following: e, t, r")

    if args.figure == "t":
        if type(args.figureparams[0]) != list:
            largest = max(args.figureparams)
            index_largest = args.figureparams.index(largest)
            other_two = [p for i, p in enumerate(args.figureparams) if i != index_largest]
            if largest >= sum(other_two):
                raise ValueError("The sum of two sides of a triangle must be larger than the third")
        else:
            for params in args.figureparams:
                largest = max(params)
                index_largest = params.index(largest)
                other_two = [p for i, p in enumerate(params) if i != index_largest]
                if largest >= sum(other_two):
                    raise ValueError("The sum of two sides of a triangle must be larger than the third")

    return args
