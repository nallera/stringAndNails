from parser import parse_args
from plotter import plot_figure

if __name__ == '__main__':
    args = parse_args()

    plot_figure(args.figure, args.nails, args.lines, args.anchor, args.turtle)
