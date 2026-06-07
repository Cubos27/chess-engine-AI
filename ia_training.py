import chess
from random_ia import RandomIA

def run_game(print_termination=False):
    # RandomIA vs randomIA starting from a specific position
    fen_position = "8/8/8/8/8/8/R7/4K2k w - - 0 1"
    board = chess.Board(fen_position)
    random_ia = RandomIA()

    while not board.is_game_over():
        board_copy = board.copy()
        move = random_ia.random_move(board_copy)
        if move is not None:
            board.push(move)
    
    if board.is_game_over() and print_termination:
        result = board.outcome()
        print(result.termination)
        if result.winner == chess.WHITE:
            print("white won.")
        elif result.winner == chess.BLACK:
            print("Black won.")
        else: # if winner is None, then it was a draw
            print("Draw")
        print("Total moves:", board.fullmove_number)

    return board.result()

def run_multiple_games(number_games):
    results = {
        "1-0": 0,       # White wins
        "0-1": 0,       # Black wins
        "1/2-1/2": 0    # Draw
    }
    for i in range(number_games):
        game_result = run_game(print_termination=True)
        if game_result in results:
            results[game_result] += 1
        else:
            print(f"Unexpected result: {game_result}")

    print("Final Results:")
    print(results)

run_multiple_games(100)