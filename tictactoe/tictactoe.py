def print_game_board(cells):
    print("---------")
    for i in range(0, len(cells), 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print("---------")

def check_game_state(cells):
    # Перевірити на можливість
    count_x = cells.count('X')
    count_o = cells.count('O')

    if abs(count_x - count_o) >= 2:
        return "Impossible"

    # Перевірити на перемогу "X" або "O"
    for i in range(0, 9, 3):
        if cells[i] == cells[i + 1] == cells[i + 2] and cells[i] != '_':
            return f"{cells[i]} wins"

    for i in range(3):
        if cells[i] == cells[i + 3] == cells[i + 6] and cells[i] != '_':
            return f"{cells[i]} wins"

    if cells[0] == cells[4] == cells[8] and cells[0] != '_':
        return f"{cells[0]} wins"

    if cells[2] == cells[4] == cells[6] and cells[2] != '_':
        return f"{cells[2]} wins"

    # Перевірити на нічию
    if '_' not in cells:
        return "Draw"

    # Гра не завершена
    return "Game not finished"

def is_valid_coordinates(coords, cells):
    if len(coords) != 2 or not coords[0].isdigit() or not coords[1].isdigit():
        return False

    x, y = map(int, coords)
    if not (1 <= x <= 3 and 1 <= y <= 3):
        return False

    index = (3 - y) * 3 + (x - 1)
    if cells[index] != '_':
        return False

    return True

def main():
    cells = "_________"
    print_game_board(cells)

    while True:
        coordinates = input("Enter the coordinates: ").split()

        if not is_valid_coordinates(coordinates, cells):
            if len(coordinates) == 2 and not coordinates[0].isdigit() and not coordinates[1].isdigit():
                print("You should enter numbers!")
            else:
                print("Coordinates should be from 1 to 3!")
            continue

        x, y = map(int, coordinates)
        index = (3 - y) * 3 + (x - 1)

        if cells[index] != '_':
            print("This cell is occupied! Choose another one!")
            continue

        cells = cells[:index] + 'X' + cells[index + 1:]
        print_game_board(cells)

        result = check_game_state(cells)
        if result != "Game not finished":
            print(result)
            break

        # Хід противника (нулик "O")
        while True:
            opponent_coords = input("Enter the coordinates for O: ").split()
            if not is_valid_coordinates(opponent_coords, cells):
                print("Invalid coordinates. Try again.")
                continue

            x, y = map(int, opponent_coords)
            index = (3 - y) * 3 + (x - 1)

            if cells[index] != '_':
                print("This cell is occupied! Choose another one!")
                continue

            cells = cells[:index] + 'O' + cells[index + 1:]
            print_game_board(cells)
            break

        result = check_game_state(cells)
        if result != "Game not finished":
            print(result)
            break

if __name__ == "__main__":
    main()
