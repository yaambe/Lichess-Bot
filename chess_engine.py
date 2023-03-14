import chess # 1.9.4
import chess.engine

# set the path of the chess engine here
engine = chess.engine.SimpleEngine.popen_uci(r"/opt/homebrew/bin/stockfish")