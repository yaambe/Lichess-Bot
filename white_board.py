import positions

def get_center_of_square(x1, y1, x2, y2, row, col):
    square_width = (x2 - x1) / 8
    square_height = (y2 - y1) / 8
    x_center = x1 + (col * square_width) + (square_width / 2)
    y_center = y1 + (row * square_height) + (square_height / 2)
    return int(x_center), int(y_center)

def create_chess_board_dict(x1, y1, x2, y2):
    chess_board_dict = {}
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for row in range(8):
        for col in range(8):
            square_name = columns[col] + str(8 - row)
            x, y = get_center_of_square(x1, y1, x2, y2, row, col)
            chess_board_dict[square_name] = {'x': x, 'y': y}
    return chess_board_dict

x1, y1 = positions.top_left['x'], positions.top_left['y']
x2, y2 = positions.bottom_right['x'], positions.bottom_right['y']
white_chess_board_dict = create_chess_board_dict(x1, y1, x2, y2)

white_board_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"