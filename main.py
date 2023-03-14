# ~ Python 3.10.6

import chess
import chess.engine
import pyautogui as pg # 0.9.53
import webdriver
import chess_engine
import white_board
import black_board
import positions
import pyautogui as pg
import requests # 2.28.1
stockfish_path = r"/opt/homebrew/bin/stockfish"

engine = chess_engine.chess.engine.SimpleEngine.popen_uci(stockfish_path)
webdriver.driver.get("https://lichess.org/")

# click function
def click_square(square):
    # Get the coordinates of the square
    x, y = squares[square]['x'], squares[square]['y']
    # Move the mouse to the center of the square and click
    pg.moveTo(x, y) #pg.moveTo(x, y, duration=0.25) if you want to specify speed
    pg.click()


# checking for move constantly # white
def check_for_move_white():
    while True:
        response = requests.get(game_url)
        html_content = response.text
        # the start and end string string are found from web scraping the lichess page
        start = '[Termination &quot;Unterminated&quot;]\n\n'
        end = ' *</div></div></aside><div class="round__board main-board">'
        start_index = html_content.find(start) + len(start)
        end_index = html_content.find(end)
        game = html_content[start_index:end_index].replace(".", "")
        game_moves = game.split(' ')
        opponent_move = game_moves[-1]
        try:
            move_flag = int(game_moves[-3])
            board.push_san(opponent_move)
            break
        except IndexError:
            pass
        except ValueError:
            move_flag = False
#  check for the move constantly # black

def check_for_move_black():
    while True:
        response = requests.get(game_url)
        html_content = response.text
        # the start and end string string are found from web scraping the lichess page
        start = '[Termination &quot;Unterminated&quot;]\n\n'
        end = ' *</div></div></aside><div class="round__board main-board">'
        start_index = html_content.find(start) + len(start)
        end_index = html_content.find(end)
        game = html_content[start_index:end_index].replace(".", "")
        game_moves = game.split(' ')
        opponent_move = game_moves[-1]
        try:
            move_flag = int(game_moves[-2])
            board.push_san(opponent_move)
            break
        except IndexError:
            pass
        except ValueError:
            move_flag = False

# from here user can click on any game he/she likes or create a game, we just need the game URL to scrape the moves
game_url = input('enter your game URL: ')
Our_Color = input("enter color as 'w' or 'b': ")

if Our_Color == 'w':
    engine_color = 'WHITE'
    Opponent_Color = 'BLACK'
else:
    engine_color = 'BLACK'
    Opponent_Color = 'WHITE'

# we figure out our color to set up the board, the following code is error prone on a mac so I commented the following
# part, you can add it if you like, or if you're on windows. Just make sure the pixels are correct.
# king_color = pg.screenshot().getpixel((pg.position(positions.king_position['x'], positions.king_position['y'])))
# Our_Color = 'WHITE' if king_color[0] == 255 else 'BLACK'
# Opponent_Color = 'BLACK' if king_color[0] == 255 else 'WHITE'
# engine_color = Our_Color

# verifying the board and colors
print(f'you are {Our_Color} Yameen. And opponent is playing {Opponent_Color}\n')

# as its a single screen we first have to press our chess board some where to activate that window
pg.click(positions.random_point_on_board['x'],positions.random_point_on_board['y'])


if engine_color == 'WHITE':
    squares = white_board.white_chess_board_dict
    board = chess.Board(white_board.white_board_fen)
    count = 1
    while not board.is_game_over():
        # Check whose turn it is to move
        if board.turn:
            # It's White's turn, let the engine play
            result = engine.play(board, chess.engine.Limit(time=0.200))
            #print(result.move.uci())
            board.push(result.move)

            # result.move.uci() is in uci which gives two squares like how we need.
            our_move = [result.move.uci()[i:i+2] for i in range(0, len(result.move.uci()), 2)]
            click_square(our_move[0])
            click_square(our_move[1])
        else:
            check_for_move_white()
    engine.quit()
    # resets the engine by reinitializing it for another game
    engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
else:
    squares = black_board.black_chess_board_dict
    board = chess.Board(black_board.black_board_fen)
    while not board.is_game_over():
        if board.turn:
            check_for_move_black()
        else:
            # It's Black's turn, let the engine play
            result = engine.play(board, chess.engine.Limit(time=0.200))
            board.push(result.move)
            # result.move.uci() is in uci which gives two squares like how we need.
            our_move = [result.move.uci()[i:i+2] for i in range(0, len(result.move.uci()), 2)]
            click_square(our_move[0])
            click_square(our_move[1])
    engine.quit()
    # resets the engine by reinitializing it for another game
    engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)