import random

# Ship Class
class Ship:
    def __init__(self, size, orientation, location):
        self.size = size

        if orientation == 'horizontal' or orientation == 'vertical':
            self.orientation = orientation
        else:
            raise ValueError("Value must be 'horizontal' or 'vertical'.")

        if orientation == 'horizontal':
            if location['row'] in range(10):
                self.coordinates = []
                for index in range(size):
                    if location['col'] + index in range(10):
                        self.coordinates.append({'row': location['row'], 'col': location['col'] + index})
                    else:
                        raise IndexError("Column is out of range.")
            else:
                raise IndexError("Row is out of range.")

        elif orientation == 'vertical':
            if location['col'] in range(10):
                self.coordinates = []
                for index in range(size):
                    if location['row'] + index in range(10):
                        self.coordinates.append({'row': location['row'] + index, 'col': location['col']})
                    else:
                        raise IndexError("Row is out of range.")
            else:
                raise IndexError("Column is out of range.")

    def __str__(self):
        return str(self.coordinates)


# Function to check if a coordinate is within bounds
def in_bounds(coord):
    return 0 <= coord['row'] < 10 and 0 <= coord['col'] < 10


# Function to check if a ship is already occupying a coordinate
def occupied(coord, occupied_coords):
    return coord in occupied_coords


# Function to place ships on the board
def place_computer_ships():
    ships = []
    occupied_coords = []

    # Place 5-space ship
    ship_size = 5
    orientation = random.choice(['horizontal', 'vertical'])
    location = {'row': random.randint(0, 9), 'col': random.randint(0, 9)}
    ship = Ship(ship_size, orientation, location)
    for coord in ship.coordinates:
        if in_bounds(coord) and not occupied(coord, occupied_coords):
            occupied_coords.append(coord)
        else:
            raise IndexError("Ship placement out of bounds or overlapping")
    ships.append(ship)

    # Place two 3-space ships
    for _ in range(2):
        ship_size = 3
        orientation = random.choice(['horizontal', 'vertical'])
        location = {'row': random.randint(0, 9), 'col': random.randint(0, 9)}
        ship = Ship(ship_size, orientation, location)
        for coord in ship.coordinates:
            if in_bounds(coord) and not occupied(coord, occupied_coords):
                occupied_coords.append(coord)
            else:
                raise IndexError("Ship placement out of bounds or overlapping")
        ships.append(ship)

    # Place three 2-space ships
    for _ in range(3):
        ship_size = 2
        orientation = random.choice(['horizontal', 'vertical'])
        location = {'row': random.randint(0, 9), 'col': random.randint(0, 9)}
        ship = Ship(ship_size, orientation, location)
        for coord in ship.coordinates:
            if in_bounds(coord) and not occupied(coord, occupied_coords):
                occupied_coords.append(coord)
            else:
                raise IndexError("Ship placement out of bounds or overlapping")
        ships.append(ship)

    return ships


def place_user_ships():
    ships = []
    occupied_coords = []

    # Place 5-space ship
    print("Place your 5-space ship:")
    ship_size = 5
    while True:
        try:
            row = int(input("Enter row (0-9): "))
            col = int(input("Enter column (0-9): "))
            orientation = input("Enter orientation (horizontal/vertical): ")
            location = {'row': row, 'col': col}
            ship = Ship(ship_size, orientation, location)
            for coord in ship.coordinates:
                if in_bounds(coord) and not occupied(coord, occupied_coords):
                    occupied_coords.append(coord)
                else:
                    raise IndexError("Ship placement out of bounds or overlapping")
            ships.append(ship)
            break
        except (ValueError, IndexError, ValueError) as e:
            print(e)

    # Place two 3-space ships
    for _ in range(2):
        print(f"Place your {3}-space ship:")
        while True:
            try:
                ship_size = 3
                row = int(input("Enter row (0-9): "))
                col = int(input("Enter column (0-9): "))
                orientation = input("Enter orientation (horizontal/vertical): ")
                location = {'row': row, 'col': col}
                ship = Ship(ship_size, orientation, location)
                for coord in ship.coordinates:
                    if in_bounds(coord) and not occupied(coord, occupied_coords):
                        occupied_coords.append(coord)
                    else:
                        raise IndexError("Ship placement out of bounds or overlapping")
                ships.append(ship)
                break
            except (ValueError, IndexError, ValueError) as e:
                print(e)

    # Place three 2-space ships
    for _ in range(3):
        print(f"Place your {2}-space ship:")
        while True:
            try:
                ship_size = 2
                row = int(input("Enter row (0-9): "))
                col = int(input("Enter column (0-9): "))
                orientation = input("Enter orientation (horizontal/vertical): ")
                location = {'row': row, 'col': col}
                ship = Ship(ship_size, orientation, location)
                for coord in ship.coordinates:
                    if in_bounds(coord) and not occupied(coord, occupied_coords):
                        occupied_coords.append(coord)
                    else:
                        raise IndexError("Ship placement out of bounds or overlapping")
                ships.append(ship)
                break
            except (ValueError, IndexError, ValueError) as e:
                print(e)

    return ships

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))


# Function to create the player's board
def create_grid(size):
    """Creates the starting grid for battleship."""
    grid = []
    for _ in range(size):
        current_line = []
        for _ in range(size):
            current_line.append(".")
        grid.append(current_line)
    return grid


# Function for the player to take a turn
def player_turn(board, ships):
    print("Player's Turn:")
    row = int(input("Enter row (0-9): "))
    col = int(input("Enter column (0-9): "))
    coord = {'row': row, 'col': col}
    for ship in ships:
        if coord in ship.coordinates:
            print("Hit!")
            board[row][col] = 'X'
            return True
    print("Miss!")
    board[row][col] = 'O'
    return False


# Function for the computer to take a turn
def computer_turn(board, ships):
    print("Computer's Turn:")
    row = random.randint(0, 9)
    col = random.randint(0, 9)
    coord = {'row': row, 'col': col}
    for ship in ships:
        if coord in ship.coordinates:
            print("Hit!")
            board[row][col] = 'X'
            return True
    print("Miss!")
    board[row][col] = 'O'
    return False


# Function to check if all ships are sunk
def all_sunk(ships):
    grid = create_grid(10)
    for ship in ships:
        for coord in ship.coordinates:
            if grid[coord['row']][coord['col']] != 'X':
                return False
    return True


# Main function to run the game
def main():
    grid = create_grid(10)
    player_ships = place_user_ships()
    computer_ships = place_computer_ships()

    while True:
        if player_turn(grid, computer_ships):
            if all_sunk(computer_ships):
                print("Player wins!")
                break

        if computer_turn(grid, player_ships):
            if all_sunk(player_ships):
                print("Computer wins!")
                break

if __name__ == "__main__":
    main()
