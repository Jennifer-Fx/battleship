def pc_select_ships(grid):
    """PC randomly selects 5 coordinates on which, if they are empty spots, 5 ships will be placed."""
    num_ships = 5
    for _ in range(num_ships):
        while True:
            row = randint(0,9)
            col = randint(0,9)
            # check if spot is free
            if grid[row][col] == ".":
                grid[row][col] = "O"
                break
                 
    return grid