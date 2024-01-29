def create_grid(size):
    """Creates the starting grid for battleship"""
    grid = []
    for counter in range(size):
        currentLine = []
        for counter in range(size):
            currentLine.append(".")
        grid.append(currentLine)
    return grid


def evaluate_and_place(grid, row, col):
    """Evaluates if spot is free = "." and then allows a ship to be placed """
    if grid[row][col] == ".":
        grid[row][col] = "X"  # "X" = user ships and "O" can be PC ships
        return True
    else:
        print("Invalid position. Position is not free.")
        return False

          
def user_select_ships(grid, num_ships):
    """Allows the user to select positions for their ships, tests, if the position is within
     boundaries of battle field and by using the evaluate_and_place function
     it also tests if the spot is free."""
    num_ships = 5   # this can be changed or also made a function input.
    for ships in range(num_ships):
        while True:
            try:
                row = int(input(f"Enter the row (0 to 9) for your ship number: {ships} "))
                col = int(input(f"Enter the column (0 to 9)for your ship number: {ships} "))
            
                # Check if the position is within the grid boundaries 
                if 0 <= row < len(grid) and 0 <= col < len(grid):
                    placed = evaluate_and_place(grid, row, col)
                    break
                else:
                    print("Invalid position. Row and column must be between 0 and 9.")
            except ValueError:
                print("Invalid input. Please try again.")
    return grid


# This here is to test if the function works. It creates a grid and runs the user_select_ships function.    
grid = create_grid(10)
user_select_ships(grid, 3)


