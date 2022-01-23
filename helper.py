def linspace(start, end, steps):
    if steps == 1:
        yield start
        return

    step = (end - start) / steps

    for i in range(steps):
        yield start + step * i
