from pc_ship_position import pc_select_ships 

def destroy_ship(grid, row, col):
    """This function checks if the opponent's ship was destroyed. 
    If yes, the ship is removed from the list of coordinates."""

    row = int(input("Enter the row (0 to 9) where you suspect a ship: "))
    col = int(input("Enter the column (0 to 9) where you suspect a ship: "))
   
    computer_choice = pc_select_ships(grid)

    if 0 <= row < len(grid) and 0 <= col < len(grid):
        computer_choice = grid[row][col]
        if computer_choice == ".":
            print("You missed! There is no ship there. ")
            return False 
        elif computer_choice == "0":
            print("You found a ship!")
            grid[row][col] = "."  # Mark the ship as destroyed in the grid
            return True
        else:
            print("Invalid coordinates. Please enter valid coordinates.")
            return False
            
