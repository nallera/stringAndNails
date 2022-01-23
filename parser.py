import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="-f is the figure outline, use c for circle and s for square, "
                                                 "-nn is the number of nails in the outline, -l is the number of "
                                                 "lines to plot, -a are the anchor parameters in the format "
                                                 "a_start,b_start,a_skip,b_skip, -t is for turtle plot (0/1)")
    parser.add_argument("-f", "--figure", help="Figure outline")
    parser.add_argument("-n", "--nails", help="Number of nails")
    parser.add_argument("-l", "--lines", help="Number of lines")
    parser.add_argument("-a", "--anchor", help="Anchor parameters")
    parser.add_argument("-t", "--turtle", help="Turtle plot")
    args = parser.parse_args()

    try:
        if ";" in args.anchor:
            args.anchor = [[int(i) for i in e.split(",")] for e in args.anchor.split(";")]
        else:
            args.anchor = [int(e) for e in args.anchor.split(",")]
    except ValueError:
        raise TypeError("bad format in anchor")

    try:
        if "," in args.nails:
            args.nails = [int(nail) for nail in args.nails.split(",")]
        else:
            args.nails = int(args.nails)
    except ValueError:
        raise TypeError("--n needs to be an integer")

    try:
        args.turtle = bool(int(args.turtle))
    except ValueError:
        raise TypeError("--n needs to be 0 or 1")

    try:
        args.lines = int(args.lines)
    except ValueError:
        raise TypeError("--l needs to be an integer")

    if args.figure not in ("c", "s"):
        raise ValueError("--f must be one of the following: c, s")

    return args
