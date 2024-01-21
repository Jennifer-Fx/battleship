def create_grid(size):

    """Creates the starting grid for battleship"""

    grid = []
    for counter in range(size):
        currentLine = []
        for counter in range(size):
            currentLine.append(".")
        grid.append(currentLine)

    return grid

newgrid = create_grid(10)
for row in newgrid:
        print(" ".join(row))


