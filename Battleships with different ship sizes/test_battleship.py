import battleship_different_ship_sizes 

def test_place_computer_ships():
    ships = place_computer_ships()
    
    # Check if correct number of ships are created
    assert len(ships) == 6, "Incorrect number of ships"
    
    # Check if each ship is an instance of the Ship class
    assert all(isinstance(ship, Ship) for ship in ships), "Not all objects in list are instances of Ship"
    
    # Check if ships are correctly placed on the board
    for ship in ships:
        for coord in ship.coordinates:
            assert in_bounds(coord), "Ship coordinate out of bounds"