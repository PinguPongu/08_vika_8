from typing import Tuple, List


# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

STARTING_LOCATION = (1, 1)
FINAL_DESTINATION = (3, 1)
LEVER_LOCATION = ((1, 2), (2, 2), (2, 3), (3, 2))

coin_count = 0

def main():
    global coin_count
    location = STARTING_LOCATION
    while location != FINAL_DESTINATION:
        location = play_one_move(location)

    print(f"Victory! Total coins {coin_count}.")

def play_one_move(location: Tuple[int]) -> Tuple[int]:
    """Plays one move of the game.

    Returns updated location.
    """

    valid_directions = find_directions(location)
    direction = get_direction(valid_directions)

    if direction in valid_directions:
        location = move(direction, location)
        if location in LEVER_LOCATION:
            pull_lever()
    else:
        print("Not a valid direction!")

    return location


def find_directions(location: Tuple[int]) -> Tuple[str]:
    """Returns valid directions as a string given the supplied location."""
    
    if location == (1, 1):
        valid_directions = (NORTH,)
    elif location == (1, 2):

        valid_directions = NORTH, EAST, SOUTH
    elif location == (1, 3):
        valid_directions = EAST, SOUTH
    elif location == (2, 1):
        valid_directions = (NORTH,)
    elif location == (2, 2):
        valid_directions = SOUTH, WEST

    elif location == (2, 3):
        valid_directions = EAST, WEST

    elif location == (3, 2):
        valid_directions = NORTH, SOUTH

    elif location == (3, 3):
        valid_directions = SOUTH, WEST

    return valid_directions


def get_direction(valid_directions: Tuple[str]) -> str:
    print_directions(valid_directions)
    return input("Direction:\n").lower()


def print_directions(available_directions: Tuple[str]) -> None:
    print("You can travel: ", end="")

    one_done_already = False
    for direction in available_directions:
        if one_done_already:
            print(" or ", end="")

        if direction == NORTH:
            print("(N)orth", end="")
        elif direction == EAST:
            print("(E)ast", end="")
        elif direction == SOUTH:
            print("(S)outh", end="")
        elif direction == WEST:
            print("(W)est", end="")

        one_done_already = True

    print(".")


def move(direction: str, location: Tuple[int]) -> Tuple[int]:
    """Returns updated location given the direction."""

    x, y = location

    if direction == NORTH:
        y += 1
    elif direction == SOUTH:
        y -= 1
    elif direction == EAST:
        x += 1
    elif direction == WEST:
        x -= 1

    return x, y


def pull_lever():
    user_input = input("Pull a lever (y/n):")
    global coin_count
    if user_input.lower() == "y":
        coin_count += 1
 
        print(f"You received 1 coin, your total is now {coin_count}.")


if __name__ == "__main__":
    main()
